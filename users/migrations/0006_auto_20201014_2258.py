# Generated by Django 3.1.1 on 2020-10-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201014_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='profile_pics/'),
        ),
    ]
