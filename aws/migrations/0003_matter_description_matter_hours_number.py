# Generated by Django 4.0.3 on 2022-03-04 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_rename_person_matter'),
    ]

    operations = [
        migrations.AddField(
            model_name='matter',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='matter',
            name='hours_number',
            field=models.IntegerField(null=True),
        ),
    ]
