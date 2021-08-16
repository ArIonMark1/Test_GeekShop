# Generated by Django 2.2.24 on 2021-08-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формирование'), ('STP', 'паредан на обработку'), ('DLV', 'доставка'), ('DN', 'выдан'), ('CNC', 'отменен')], default='FM', max_length=3),
        ),
    ]