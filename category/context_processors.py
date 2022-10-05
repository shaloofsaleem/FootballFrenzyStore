
from category.models import *


def category(request):
    return{
        'context_category': Category.objects.all().filter(is_active=True),
    }





