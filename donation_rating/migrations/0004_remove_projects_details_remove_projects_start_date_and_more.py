# Generated by Django 4.0.2 on 2022-02-18 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_rating', '0003_rename_general_rate_projects_total_upvotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='details',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='title',
        ),
    ]