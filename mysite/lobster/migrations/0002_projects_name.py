# Generated by Django 2.0.1 on 2018-06-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='name',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]