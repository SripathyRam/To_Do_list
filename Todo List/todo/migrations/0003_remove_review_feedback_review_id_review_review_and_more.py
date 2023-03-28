# Generated by Django 4.1.2 on 2022-10-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='feedback',
        ),
        migrations.AddField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]