# Generated by Django 2.1.3 on 2018-11-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebScraperETL', '0002_productid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.CharField(max_length=50)),
                ('parameter', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='opinion',
            name='productID',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]