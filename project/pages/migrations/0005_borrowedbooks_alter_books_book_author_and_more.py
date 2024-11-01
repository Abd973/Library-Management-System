# Generated by Django 5.0.4 on 2024-05-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrowedbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(default='0', max_length=50)),
                ('book_name', models.CharField(default='book', max_length=50)),
                ('book_author', models.CharField(default='author', max_length=50)),
                ('book_category', models.CharField(default='category', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(default='author', max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_category',
            field=models.CharField(default='category', max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(default='book', max_length=50),
        ),
    ]