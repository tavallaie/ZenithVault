# Generated by Django 5.0.7 on 2024-07-25 01:15

import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='content',
        ),
        migrations.RemoveField(
            model_name='content',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='content',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='content',
            name='license',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='contents.contenttype'),
        ),
        migrations.AddIndex(
            model_name='content',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='contents_co_search__4b84b5_gin'),
        ),
    ]
