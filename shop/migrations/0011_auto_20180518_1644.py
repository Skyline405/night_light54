# Generated by Django 2.0.5 on 2018-05-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20180518_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('visible', models.BooleanField(default=True, verbose_name='Видимость')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props', to='shop.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'параметры',
                'verbose_name': 'параметр',
            },
        ),
        migrations.CreateModel(
            name='ProductProp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('visible', models.BooleanField(default=True, verbose_name='Видимость')),
                ('value', models.CharField(default='', max_length=255, verbose_name='Значение')),
            ],
            options={
                'verbose_name_plural': 'параметры',
                'verbose_name': 'параметр',
            },
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='shop.Product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='productprop',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='props', to='shop.Offer', verbose_name='Предложение'),
        ),
    ]