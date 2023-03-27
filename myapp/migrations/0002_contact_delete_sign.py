# Generated by Django 4.1.7 on 2023-03-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='sign',
        ),
    ]