# Generated by Django 2.1.7 on 2019-03-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afrolov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train', models.CharField(max_length=200)),
            ],
        ),
    ]
