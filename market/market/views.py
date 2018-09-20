from market.models import Category
from django.http import HttpResponse


def data_manipulation(request):
    res = ''

    # Filtering Data:
    qs = Category.objects.filter(name="paul")
    res += " Found : %s results <br> "%len(qs)

    # Ordering Results:
    qs = Category.objects.order_by("name")

    for elt in qs:
        res += elt.name + '<br>'

    return HttpResponse(res)




