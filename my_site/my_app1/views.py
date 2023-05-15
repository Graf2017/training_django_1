from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def mainpage(request):
    any_name = {
        'title': "Головна"
    }
    return render(request, 'my_app1/mainpage.html', context=any_name)


def catalog(request):
    context = {
        'title': "Категорії товарів",
    }
    return render(request, 'my_app1/catalog.html', context=context)


def box(request):
    box_list = Position.objects.filter(in_box=True)
    context = {
        'title': "Кошик",
        'box_list': box_list,
    }
    return render(request, 'my_app1/box.html', context=context)


def delivery(request):
    context = {
        'title': "Доставка та оплата",
    }
    return render(request, 'my_app1/delivery.html', context=context)


def about(request):
    context = {
        'title': "Про нас",
    }
    return render(request, 'my_app1/about.html', context=context)


def show_position(request, position_slug, name_of_categories):
    a_pos = get_object_or_404(Position, slug_for_position=position_slug)
    context = {
        'title': a_pos.title,
        'description': a_pos.description,
        'photo': a_pos.photo,
        'price': a_pos.price
    }
    return render(request, 'my_app1/position.html', context=context)


def show_positions(request, name_of_categories):
    cat = Categories.objects.get(slug_for_categories=name_of_categories)
    title = cat.categories_name
    positions = cat.position_set.all().filter(published=True)
    context = {
        'positions': positions,
        'title': title,
    }
    return render(request, 'my_app1/positions.html', context=context)


def add_position(request):
    if request.method == 'POST':
        form = AddPosition(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')

    else:
        form = AddPosition()
    return render(request, 'my_app1/add_position.html', {'form': form, 'title': "Додати товар"})


def login(request):
    pass
