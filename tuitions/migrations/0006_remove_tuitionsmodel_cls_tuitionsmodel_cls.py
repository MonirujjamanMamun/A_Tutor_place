# Generated by Django 4.2.7 on 2024-01-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0005_remove_tuitionsmodel_cls_tuitionsmodel_cls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuitionsmodel',
            name='cls',
        ),
        migrations.AddField(
            model_name='tuitionsmodel',
            name='cls',
            field=models.ManyToManyField(to='tuitions.userclassmodel'),
        ),
    ]
