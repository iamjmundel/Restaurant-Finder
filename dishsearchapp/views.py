from django.shortcuts import render
from dishsearchapp.models import Dish
import math

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        dishes = Dish.objects.filter(name__icontains=query)
        result = sorted([(dish, dish.restaurant, dish.restaurant.rating) for dish in dishes], key=lambda x:x[2])[::-1]
        results=[]
        for i in result:
            if i[1] not in results:
                results.append(i[1])

    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)

