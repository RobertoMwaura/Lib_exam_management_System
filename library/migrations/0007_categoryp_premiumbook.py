# Generated by Django 5.0.2 on 2024-03-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_myusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categoriesp')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='PremiumBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('pdf', models.FileField(upload_to='pdf')),
                ('junior_books', models.BooleanField(default=False)),
                ('senior_books', models.BooleanField(default=False)),
                ('lower_books', models.BooleanField(default=False)),
                ('categoryp', models.ManyToManyField(related_name='books', to='library.categoryp')),
            ],
        ),
    ]
