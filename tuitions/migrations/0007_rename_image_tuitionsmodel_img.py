# Generated by Django 4.2.7 on 2024-01-18 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0006_remove_tuitionsmodel_cls_tuitionsmodel_cls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuitionsmodel',
            old_name='image',
            new_name='img',
        ),
    ]
