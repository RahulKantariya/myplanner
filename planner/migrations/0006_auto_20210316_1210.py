# Generated by Django 3.1.5 on 2021-03-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20210314_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='AfterWakeUp',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='BeforeBreakfast',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Breakfast',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Dinner',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='DueToDietFor',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Excercise',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Lunch',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='MidNeightDrink',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Snacks',
            field=models.TextField(blank=True),
        ),
    ]