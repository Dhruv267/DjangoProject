# Generated by Django 2.2 on 2019-04-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0004_ticket_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainnm', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=5)),
                ('src', models.CharField(max_length=15)),
                ('dest', models.CharField(max_length=15)),
                ('num', models.CharField(max_length=1)),
                ('mail', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='ticket',
        ),
    ]
