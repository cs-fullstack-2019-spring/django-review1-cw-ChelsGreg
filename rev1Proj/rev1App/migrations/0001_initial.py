# Generated by Django 2.0.6 on 2019-02-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alcPercent', models.IntegerField(default=0)),
                ('serveGlass', models.CharField(max_length=100)),
            ],
        ),
    ]
