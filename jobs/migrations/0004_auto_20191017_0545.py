# Generated by Django 2.2.6 on 2019-10-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_application_is_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Email',
            new_name='email',
        ),
    ]