# Generated by Django 3.2.5 on 2021-07-16 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0003_auto_20210716_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='patrollers',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='watch_point',
        ),
        migrations.AlterField(
            model_name='shift',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('patrollers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='locator.patroller')),
                ('shift', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='locator.shift')),
                ('watch_point', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='locator.watchpoint')),
            ],
        ),
    ]
