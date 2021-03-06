# Generated by Django 2.2.6 on 2019-10-13 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
                ('Email', models.EmailField(max_length=255)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tech_included',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tech', models.TextField(blank=True, default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.TextField(choices=[('Internship', 'Internship'), ('Freelance', 'Freelance'), ('Fulltime', 'Fulltime'), ('Temporary', 'Temporary')])),
                ('description', models.TextField(blank=True, default='empty')),
                ('location', models.TextField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='job_thumbnail')),
                ('experience_level', models.TextField(max_length=250)),
                ('salary', models.IntegerField()),
                ('is_featured', models.BooleanField(default=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='jobs.Category')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.Company')),
                ('tech', models.ManyToManyField(to='jobs.Tech_included')),
            ],
        ),
    ]
