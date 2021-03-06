# Generated by Django 3.1.5 on 2021-02-16 09:51

from django.db import migrations, models
import django.db.models.deletion
import eda.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('path', models.CharField(default='path', max_length=250, primary_key=True, serialize=False)),
                ('icon', models.ImageField(blank=True, upload_to='')),
                ('code', models.FileField(blank=True, default=None, upload_to=eda.models.get_code_upload_path)),
                ('properties', models.TextField(default='{}')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('name', models.CharField(default='New_Template', max_length=250, primary_key=True, serialize=False)),
                ('elements', models.ManyToManyField(to='eda.Element')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(default='New_Project', max_length=250, primary_key=True, serialize=False)),
                ('elements', models.ManyToManyField(to='eda.Element')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='eda.projecttemplate')),
            ],
        ),
    ]
