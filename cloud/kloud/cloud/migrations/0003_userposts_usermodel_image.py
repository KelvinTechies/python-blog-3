# Generated by Django 4.2.3 on 2023-07-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_rename_user_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('PostImage', models.ImageField(upload_to='Post_Image/')),
                ('Category', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
