# Generated by Django 2.0.5 on 2018-06-12 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180612_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='users',
            new_name='friends',
        ),
    ]
