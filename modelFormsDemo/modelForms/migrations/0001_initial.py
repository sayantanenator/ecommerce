# Generated by Django 4.1 on 2022-08-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productTitle', models.CharField(max_length=30)),
                ('productCost', models.IntegerField()),
                ('productOwner', models.CharField(max_length=30)),
            ],
        ),
    ]
