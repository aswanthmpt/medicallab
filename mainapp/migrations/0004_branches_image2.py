# Generated by Django 5.0.3 on 2024-03-31 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_blogs_branches'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='image2',
            field=models.ImageField(default=0, upload_to='branches'),
            preserve_default=False,
        ),
    ]
