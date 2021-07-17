# Generated by Django 3.2.5 on 2021-07-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0007_watchpoint_abbreviation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='patrollers',
        ),
        migrations.AddField(
            model_name='team',
            name='patrollers',
            field=models.ManyToManyField(blank=True, null=True, to='locator.Patroller'),
        ),
    ]