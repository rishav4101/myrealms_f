# Generated by Django 3.0.4 on 2020-04-11 21:02

import blogs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_post_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', blogs.models.CategoryField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='hits',
            new_name='views',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='post',
            name='category1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category1', to='blogs.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category2', to='blogs.Category'),
            preserve_default=False,
        ),
    ]
