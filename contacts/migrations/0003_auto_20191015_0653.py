# Generated by Django 2.2.6 on 2019-10-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191015_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='job',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
