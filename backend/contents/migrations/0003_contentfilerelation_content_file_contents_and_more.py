# Generated by Django 5.0.7 on 2024-07-25 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_contenttype_filecontent_textcontent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentFileRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.content')),
                ('file_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.filecontent')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='file_contents',
            field=models.ManyToManyField(related_name='contents', through='contents.ContentFileRelation', to='contents.filecontent'),
        ),
        migrations.CreateModel(
            name='ContentTextRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.content')),
                ('text_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.textcontent')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='text_contents',
            field=models.ManyToManyField(related_name='contents', through='contents.ContentTextRelation', to='contents.textcontent'),
        ),
        migrations.CreateModel(
            name='MetaDataField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field_type', models.CharField(choices=[('char', 'CharField'), ('text', 'TextField'), ('int', 'IntegerField'), ('float', 'FloatField'), ('date', 'DateField'), ('datetime', 'DateTimeField'), ('bool', 'BooleanField'), ('email', 'EmailField'), ('url', 'URLField')], max_length=50)),
                ('required', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadata_fields', to='contents.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='MetaDataValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata_values', to='contents.content')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.metadatafield')),
                ('file_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata_values', to='contents.filecontent')),
                ('text_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata_values', to='contents.textcontent')),
            ],
        ),
    ]
