# Generated by Django 2.2.1 on 2019-06-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190621_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
