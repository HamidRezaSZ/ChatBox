# Generated by Django 4.1.1 on 2022-09-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='img/default-avatar.jpeg', upload_to='img/'),
        ),
    ]
