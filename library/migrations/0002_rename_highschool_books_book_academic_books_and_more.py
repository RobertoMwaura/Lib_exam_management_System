# Generated by Django 5.0.2 on 2024-03-16 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='highschool_books',
            new_name='academic_books',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='playgroup_books',
            new_name='biography_books',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='primary_books',
            new_name='selfdev_books',
        ),
    ]