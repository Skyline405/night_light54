# Generated by Django 2.0.5 on 2018-05-17 07:04

from django.db import migrations, models
import django.db.models.deletion
import shop.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
                ('title', models.CharField(default='', max_length=32, verbose_name='Название')),
                ('region', models.CharField(default='', max_length=32, verbose_name='Регион доставки')),
                ('duration', models.CharField(default='', max_length=32, verbose_name='Срок доставки')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('cost', models.PositiveIntegerField(default=0, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Вариант доставки',
                'verbose_name_plural': 'Варианты доставки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('waiting', 'Не принят'), ('confirmed', 'Принят'), ('sended', 'Отправлен'), ('completed', 'Доставлен')], default='waiting', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='ProductProp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
            ],
            options={
                'verbose_name': 'Параметр товара',
                'verbose_name_plural': 'Параметры товара',
            },
        ),
        migrations.CreateModel(
            name='PropSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Параметры',
            },
        ),
        migrations.CreateModel(
            name='PropValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=255, verbose_name='Значение')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prop_value', to='shop.PropSchema', verbose_name='Параметр')),
            ],
            options={
                'verbose_name': 'Значение параметра',
                'verbose_name_plural': 'Значения параметров',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('visible', models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость')),
                ('question', models.CharField(default='', max_length=32, verbose_name='Вопрос')),
                ('answer', models.TextField(default='', verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос-ответ',
                'verbose_name_plural': 'Вопросы-ответы',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['ordering'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Краткое описание категории (Может быть пустым)', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='', help_text='Картинка, которая будет отображаться рядом с названием категории', upload_to=shop.utils.utils.make_upload_path, verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='category',
            name='ordering',
            field=models.PositiveIntegerField(default=0, help_text='Чем меньше значение, тем выше категория', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='product',
            name='best_flag',
            field=models.BooleanField(default=False, help_text='Добавить флаг "Бестселлер" в карточку товара', verbose_name='"Best" флаг'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='event_duration',
            field=models.DateTimeField(default=0, verbose_name='Длительность акции'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='visible',
            field=models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во в наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, help_text='Скидка на товар в процентах', verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to=shop.utils.utils.make_upload_path, verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Цена на товар в рублях', max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='visible',
            field=models.BooleanField(default=True, help_text='Скрыть или показать', verbose_name='Видимость'),
        ),
        migrations.AddField(
            model_name='propschema',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='props', to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='productprop',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='productprop',
            name='prop_desc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.PropSchema', verbose_name='Параметр'),
        ),
        migrations.AddField(
            model_name='productprop',
            name='values',
            field=models.ManyToManyField(blank=True, to='shop.PropValue', verbose_name='Значения'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар'),
        ),
    ]