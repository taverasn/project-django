# Generated by Django 3.1.7 on 2021-03-10 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0013_auto_20210306_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountphoto',
            name='account',
        ),
        migrations.AddField(
            model_name='accountphoto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
