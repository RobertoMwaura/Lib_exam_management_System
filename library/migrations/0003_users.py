# Generated by Django 5.0.2 on 2024-03-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_highschool_books_book_academic_books_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
