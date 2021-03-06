# Generated by Django 2.0.6 on 2018-08-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobster', '0008_remove_projects_h_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='rn_IRAS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_LMA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_embed_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_emission',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_half_life',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_name',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_spec_activ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_total_activ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='rn_vllw_class',
            field=models.IntegerField(default=0),
        ),
    ]
