from django.shortcuts import render, get_object_or_404

from .models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'costs/index.html', {'items': items})


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'costs/detail.html', {'item': item})
