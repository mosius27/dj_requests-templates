from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    recipe = DATA['omlet']
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    recipe = DATA['pasta']
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    recipe = DATA['buter']
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
