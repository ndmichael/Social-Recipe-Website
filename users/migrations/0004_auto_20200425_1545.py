# Generated by Django 2.1.7 on 2020-04-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='details',
            field=models.TextField(default='No profile details set yet by the user', max_length=200),
        ),
    ]