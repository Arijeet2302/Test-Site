# Generated by Django 4.1.7 on 2023-03-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
