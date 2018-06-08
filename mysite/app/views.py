from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader


from .models import *

def get_actual_offers(offers):
    actual_offers = []
    for offer in offers:
        if offer.is_actual:
            actual_offers.append(offer)
    return actual_offers


def index(request):
    offers = Offer.objects.order_by('DateFrom')
    offers = get_actual_offers(offers)

    template = loader.get_template('app/index.html')
    context = {
        'offers': offers,
               }
    return HttpResponse(template.render(context, request))


def detail(request, offerID):
    offer = Offer.objects.get(pk=offerID)

    template = loader.get_template('app/detail.html')
    context = {'offer': offer, }
    return HttpResponse(template.render(context, request))

