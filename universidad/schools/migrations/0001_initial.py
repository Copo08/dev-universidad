# Generated by Django 4.1 on 2022-08-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('school_id', models.IntegerField()),
                ('adress', models.CharField(max_length=120)),
                ('areas', models.CharField(max_length=30)),
                ('majors', models.CharField(max_length=30)),
                ('schedule', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'schools',
            },
        ),
    ]