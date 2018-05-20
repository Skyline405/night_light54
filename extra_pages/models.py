from django.db import models
from night_light.models import BaseModel


# Delivery variant
class DeliveryVariant(BaseModel):
    title = models.CharField('Название', default='', max_length=32)
    region = models.CharField('Регион доставки', default='', max_length=32)
    duration = models.CharField('Срок доставки', default='', max_length=32)
    description = models.TextField('Описание', default='')
    cost = models.PositiveIntegerField('Стоимость', default=0)

    class Meta:
        verbose_name = 'вариант доставки'
        verbose_name_plural = 'варианты доставки'


# Question
class QuestionAnswer(BaseModel):
    question = models.CharField('Вопрос', default='', max_length=32)
    answer = models.TextField('Ответ', default='')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос-ответ'
        verbose_name_plural = 'вопросы-ответы'
