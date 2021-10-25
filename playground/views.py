from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db import transaction
from store.models import Product
from tags.models import TaggedItem

# @transaction.atomic()


def say_hello(request):
    # # AND
    # queryset = Product.objects.filter(unit_price__range=(20, 30), collection__gt=900)

    # # OR
    # queryset = Product.objects.filter(
    #     Q(unit_price__range=(20, 30)) | Q(collection__gt=900))

    # # Compare fields
    # queryset = Product.objects.filter(collection=F('id'))

    # # inverse sorting
    # queryset = Product.objects.order_by('-unit_price')

    # # get only some culomns
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')

    # # related tables
    # queryset = Product.objects.select_related('collection').all()

    # do transaction
    with transaction.atomic():
        # Related apps
        queryset = TaggedItem.unpublished_objects.get_tags_for(Product, 1)

    # row sql querys
    queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'abdelhalim', 'products': list(queryset)})
