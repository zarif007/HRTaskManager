# Generated by Django 3.2.4 on 2021-06-07 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_user_hr_poits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hr_poits',
            new_name='hr_points',
        ),
    ]