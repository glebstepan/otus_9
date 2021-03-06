# Generated by Django 2.2.2 on 2019-06-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='course.Course'),
        ),
    ]
