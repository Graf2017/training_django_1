from django import template
from my_app1.models import *

register = template.Library()


@register.simple_tag(name='get_cats')  #
def get_categories(sort='categories_name', cat_id=None):
    if not cat_id:
        return Categories.objects.order_by(sort)
    else:
        return Categories.objects.get(pk=cat_id)


@register.inclusion_tag('my_app1/tags/get_categories.html')  #
def get_cats_select(sort=None, cat_selected=0):
    if not sort:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('my_app1/tags/main_menu.html')
def main_menu():
    menu = [{'title': "Головна", 'url_name': 'mainpage'},
            {'title': "Каталог товарів", 'url_name': 'catalog'},
            {'title': "Кошик", 'url_name': 'box'},
            {'title': "Доставка та оплата", 'url_name': 'delivery'},
            {'title': "Про нас", 'url_name': 'about'},
            {'title': "Додати товар", 'url_name': 'add_position'}]

    return {'menu': menu}
