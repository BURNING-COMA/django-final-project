# Generated by Django 4.0.2 on 2022-02-18 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donation_rating', '0011_remove_projects_user_delete_projectrate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('end_date', models.DateField()),
                ('total_target', models.IntegerField(blank=True, default=0)),
                ('total_upvotes', models.IntegerField(blank=True, default=0)),
                ('total_votes', models.IntegerField(blank=True, default=0)),
                ('collected_donations', models.IntegerField(blank=True, default=0)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_upvote', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_rating.projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
