# Generated by Django 2.2 on 2019-04-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0003_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='cost',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
