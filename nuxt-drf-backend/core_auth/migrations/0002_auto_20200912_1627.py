# Generated by Django 2.1.5 on 2020-09-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30, verbose_name='location'),
        ),
    ]
