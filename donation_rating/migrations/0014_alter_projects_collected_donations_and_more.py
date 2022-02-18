# Generated by Django 4.0.2 on 2022-02-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_rating', '0013_alter_projectrate_user_alter_projects_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='collected_donations',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_target',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_upvotes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='total_votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]