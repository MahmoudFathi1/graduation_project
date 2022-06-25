# Generated by Django 3.2.5 on 2022-06-18 18:44

import authentications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentications.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email_address'),
        ),
    ]