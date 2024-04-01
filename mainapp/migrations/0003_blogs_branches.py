# Generated by Django 5.0.3 on 2024-03-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_appointment_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
                ('date', models.DateField()),
                ('h1', models.TextField(blank=True, null=True)),
                ('p1', models.TextField(blank=True, null=True)),
                ('h2', models.TextField(blank=True, null=True)),
                ('p2', models.TextField(blank=True, null=True)),
                ('h3', models.TextField(blank=True, null=True)),
                ('p3', models.TextField(blank=True, null=True)),
                ('h4', models.TextField(blank=True, null=True)),
                ('p4', models.TextField(blank=True, null=True)),
                ('h5', models.TextField(blank=True, null=True)),
                ('p5', models.TextField(blank=True, null=True)),
                ('h6', models.TextField(blank=True, null=True)),
                ('p6', models.TextField(blank=True, null=True)),
                ('h7', models.TextField(blank=True, null=True)),
                ('p7', models.TextField(blank=True, null=True)),
                ('r1', models.TextField(blank=True, null=True)),
                ('r2', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ('h1',),
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='branches')),
                ('map', models.TextField()),
            ],
            options={
                'verbose_name': 'branches',
            },
        ),
    ]
