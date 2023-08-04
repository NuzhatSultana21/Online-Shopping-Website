# Generated by Django 4.1 on 2022-09-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='mcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=70)),
                ('pid', models.IntegerField()),
                ('cdate', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='morder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=70)),
                ('pid', models.IntegerField()),
                ('remarks', models.CharField(max_length=20)),
                ('odate', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]