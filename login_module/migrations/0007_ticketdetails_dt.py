# Generated by Django 2.2 on 2019-04-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0006_auto_20190411_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketdetails',
            name='dt',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]