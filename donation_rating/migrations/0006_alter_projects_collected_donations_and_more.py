# Generated by Django 4.0.2 on 2022-02-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_rating', '0005_remove_projectimages_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='collected_donations',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_target',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_upvotes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_votes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
