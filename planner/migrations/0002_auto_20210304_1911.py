# Generated by Django 3.1.5 on 2021-03-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DueToDietFor',
            field=models.TextField(),
        ),
    ]
