# Generated by Django 2.0.5 on 2019-02-25 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_trip_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user_payed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_payed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user_recieved',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_recieved', to=settings.AUTH_USER_MODEL),
        ),
    ]