# Generated by Django 3.1.4 on 2020-12-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('year_c', models.CharField(max_length=500)),
                ('links_c', models.CharField(max_length=500)),
                ('price_USE_c', models.CharField(max_length=500)),
                ('price_UA_c', models.CharField(max_length=500)),
                ('city_c', models.CharField(max_length=500)),
            ],
        ),
    ]
