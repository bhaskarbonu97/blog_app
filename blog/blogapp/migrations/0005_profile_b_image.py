# Generated by Django 2.2.1 on 2019-08-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20190823_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='b_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
