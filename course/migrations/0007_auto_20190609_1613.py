# Generated by Django 2.2.2 on 2019-06-09 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20190609_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
