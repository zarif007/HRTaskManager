# Generated by Django 3.2.4 on 2021-06-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_alter_user_in_club_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, choices=[('HR', 'Human Resources')], max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, choices=[('General Member', 'General Member'), ('Executive', 'Executive'), ('Senior Executive', 'Senior Executive'), ('Assistant Director', 'Assistant Director'), ('Director', 'Director')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='hr_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(blank=True, choices=[(0, 'Free'), (1, 'Busy')], default=1, null=True),
        ),
    ]
