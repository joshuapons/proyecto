# Generated by Django 3.0.4 on 2020-03-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_typecontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='document',
            field=models.FileField(default='', null=True, upload_to='uploads/contact'),
        ),
    ]
