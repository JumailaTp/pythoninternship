# Generated by Django 4.1.4 on 2023-01-29 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_discription_catagory_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]
