# Generated by Django 4.1 on 2022-08-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_item_category_alter_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Футболки'), ('H', 'Толстовки'), ('B', 'Рюкзаки')], max_length=2),
        ),
    ]
