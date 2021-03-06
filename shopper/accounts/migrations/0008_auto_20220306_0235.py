# Generated by Django 3.2 on 2022-03-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220305_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
