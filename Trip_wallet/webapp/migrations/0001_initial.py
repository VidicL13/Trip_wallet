# Generated by Django 2.0.5 on 2018-06-10 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currancy', models.CharField(blank=True, max_length=30)),
                ('value', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('post', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tax_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user_type', models.CharField(blank=True, max_length=30, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('value', models.FloatField(blank=True)),
                ('type', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('receiver', models.CharField(max_length=250)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_payed', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_payed', to=settings.AUTH_USER_MODEL)),
                ('user_recieved', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_recieved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionInvolvment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('transaction', models.ManyToManyField(related_name='transaction_involvment', to='webapp.Transaction')),
                ('user', models.ManyToManyField(related_name='user_involvment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('transaction', models.ManyToManyField(related_name='transaction_label', to='webapp.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('country', models.CharField(blank=True, max_length=250)),
                ('discription', models.CharField(blank=True, max_length=2500)),
                ('users', models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
