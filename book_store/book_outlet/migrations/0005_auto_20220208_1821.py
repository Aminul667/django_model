# Generated by Django 3.2.9 on 2022-02-08 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_auto_20220204_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_namr',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='last_namr',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_outlet.author'),
        ),
    ]
