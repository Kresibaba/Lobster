# Generated by Django 2.0.6 on 2018-10-04 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobster', '0012_auto_20181004_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='rnlist',
            name='projects',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lobster.Projects'),
            preserve_default=False,
        ),
    ]
