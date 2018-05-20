from django.shortcuts import render

from extra_pages.models import DeliveryVariant, QuestionAnswer
from shop.models import Category


def delivery(req):
    categories = Category.objects.all()
    delivery_variants = DeliveryVariant.objects.all()
    return render(req, 'pages/delivery.html',
                  context={'delivery_variants': delivery_variants, 'categories': categories})


def question_answer(req):
    categories = Category.objects.all()
    questions = QuestionAnswer.objects.all()
    return render(req, 'pages/question_answer.html', context={'questions': questions, 'categories': categories})


def feedback_page(req):
    return render(req, 'pages/feedback.html')
