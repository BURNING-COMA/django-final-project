# Generated by Django 4.0.2 on 2022-02-18 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('total_target', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('general_rate', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_rating.category')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donation_rating.projectimages')),
                ('tags', models.ManyToManyField(to='donation_rating.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_upvote', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_rating.projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_rating.projects'),
        ),
    ]
