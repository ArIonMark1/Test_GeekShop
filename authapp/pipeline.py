from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode
import requests
from django.conf import settings
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'google':
        return

    api_url = urlunparse(('https', 'api.google.com', '/method/users.get', None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                                access_token=response['access_token'],
                                                v='5.92')),None))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if 'photo_max_orig' in data:
        photo_content = requests.get(data['photo_max_orig'])
        with open (f'{settings.MEDIA_ROOT}/users_avatars/{user.pk}.jps', 'wb') as photo_file:
            photo_file.write(photo_content.content)
            user.avatar = f'users_avatars/{user.pk}.jpg'

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.google.GoogleOAuth')

    user.save()
