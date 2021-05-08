# Generated by Django 3.1.5 on 2021-01-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(max_length=100)),
                ('author_last_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.IntegerField()),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
    ]
