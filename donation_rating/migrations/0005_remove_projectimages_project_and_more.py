# Generated by Django 4.0.2 on 2022-02-18 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_rating', '0004_remove_projects_details_remove_projects_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimages',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ProjectImages',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]