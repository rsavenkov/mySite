# Generated by Django 2.1.7 on 2019-03-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20190303_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('data', models.DateField()),
            ],
        ),
    ]
