from django.conf import settings

from utils import vk_api


def get_feedback_list():
    res = vk_api.send_request('board.getComments', {
        'group_id': settings.VK_GROUP_ID,
        'topic_id': settings.VK_TOPIC_ID,
        'extended': True,
        'sort': 'asc'
    })

    if res.status_code == 200:
        data = res.json()
        return data['response']['items']
    return []


def get_users_info(id_list):
    res = vk_api.send_request('users.get', {
        'user_ids': ','.join(map(lambda i: str(i), id_list))
    })

    if res.status_code == 200:
        data = res.json()
        return data['response']
    return []
