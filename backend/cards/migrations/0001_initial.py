# Generated by Django 4.2.3 on 2023-07-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('definition', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('definition', models.CharField(max_length=400)),
                ('conjugations', models.JSONField()),
            ],
        ),
    ]
