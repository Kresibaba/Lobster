# Generated by Django 2.0.6 on 2018-08-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobster', '0006_projects_waste_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='H_3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
