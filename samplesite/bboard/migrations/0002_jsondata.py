# Generated by Django 3.0.2 on 2020-02-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AttributeName', models.CharField(max_length=50)),
                ('AttributeID', models.CharField(max_length=50)),
                ('AttributeContent', models.TextField(db_index=True, max_length=50)),
            ],
        ),
    ]
