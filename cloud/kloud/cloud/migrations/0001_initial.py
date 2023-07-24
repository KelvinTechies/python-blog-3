# Generated by Django 4.2.3 on 2023-07-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200, unique=True)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=200)),
                ('Unique_Number', models.CharField(max_length=7)),
                ('Created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
