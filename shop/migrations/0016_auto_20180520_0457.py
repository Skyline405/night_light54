# Generated by Django 2.0.5 on 2018-05-20 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20180520_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryprop',
            name='category',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='product',
        ),
        migrations.RemoveField(
            model_name='offerprop',
            name='category_prop',
        ),
        migrations.RemoveField(
            model_name='offerprop',
            name='offer',
        ),
        migrations.DeleteModel(
            name='CategoryProp',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='OfferProp',
        ),
    ]