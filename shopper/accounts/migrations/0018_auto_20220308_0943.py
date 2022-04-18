# Generated by Django 3.2 on 2022-03-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20220308_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procategory', models.CharField(choices=[('Food', 'Food'), ('Clothing', 'Clothing'), ('Home Appliances', 'Home Appliances'), ('Groceries', 'Groceries'), ('Medical Aids', 'Medical Aids')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]