# Generated by Django 2.0.6 on 2018-07-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobster', '0004_auto_20180721_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currproject',
            name='name',
        ),
        migrations.AddField(
            model_name='projects',
            name='volume_net',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='weight_net',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CurrProject',
        ),
    ]
