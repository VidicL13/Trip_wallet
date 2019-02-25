# Generated by Django 2.0.5 on 2019-02-25 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0007_auto_20190225_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='involved',
            field=models.ManyToManyField(related_name='involved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='trip',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, related_name='Trip', to='webapp.Trip'),
            preserve_default=False,
        ),
    ]
