# Generated by Django 4.2.7 on 2024-01-18 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0009_remove_reviewmodel_created_remove_reviewmodel_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tuitions.tuitionsmodel'),
        ),
    ]