# Generated by Django 2.0.7 on 2018-08-13 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_project_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
