from extra_pages.models import DeliveryVariant, QuestionAnswer
from shop.views import nl_render
from utils import feedback_api


def delivery(req):
    delivery_variants = DeliveryVariant.objects.filter(visible=True)
    return nl_render(req, 'pages/delivery.html', {'delivery_variants': delivery_variants})


def question_answer(req):
    questions = QuestionAnswer.objects.filter(visible=True)
    return nl_render(req, 'pages/question_answer.html', {'questions': questions})


def feedback_page(req):
    feedback_list = feedback_api.get_feedback_list()

    fb_list = []
    uid_list = []

    for item in feedback_list:
        from_id = item['from_id']
        if from_id > 0 and item['text']:
            fb_list.append(item)
            uid_list.append(from_id)

    users_list = feedback_api.get_users_info(uid_list)

    users = {}
    for user in users_list:
        users[user['id']] = '%s %s' % (user['first_name'], user['last_name'])

    return nl_render(req, 'pages/feedback.html', {'feedback_list': fb_list, 'users': users})
