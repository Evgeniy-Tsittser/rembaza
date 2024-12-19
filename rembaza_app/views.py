from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import MonthWorks, WaterTable, SeverageTable, YEAR_CHOICES

"""Представление для страницы выбора отчетного года:
 - отображает ссылки для перенаправления на страницу с данными по выбранному году"""


def year_view(request):
    years = [year[0] for year in YEAR_CHOICES]
    context = {'years': years}
    return render(request, 'rembaza_app/year_page.html', context)


"""Представление для страницы выбора отчетного месяца и таблицы годового итога 
по водоснабжению или водоотведению
 - отображает ссылки для перенаправления на страницу с таблицами значений по отчетному месяцу или по году"""


def year_detail(request, year):
    monthworks = MonthWorks.objects.filter(year=year)
    watertable = WaterTable.objects.filter(year=year)
    severagetable = SeverageTable.objects.filter(year=year)
    context = {
        'year': year,
        'monthworks': monthworks,
        'watertable': watertable,
        'severagetable': severagetable
    }
    return render(request, 'rembaza_app/year_detail.html', context)


"""Представление для отображения страницы с таблицей работ по выбранному месяцу"""


def monthworks_list(request, year, month):
    works = MonthWorks.objects.filter(year=year, month=month)
    context = {
        'works': works,
        'month_name': dict(MonthWorks.MONTH_CHOICES)[month]
    }
    return render(request, 'rembaza_app/monthworks_list.html', context)


"""Представление для отображения страницы с суммарной таблицей годовых работ по водоснабжению"""


def watertable_view(request, year):
    try:
        watertables = WaterTable.objects.filter(year=year)
    except Exception as e:
        return HttpResponse(e)
    context = {
        'watertables': watertables,
        'year': year}
    return render(request, 'rembaza_app/watertable.html', context)


"""Представление для отображения страницы с суммарной таблицей годовых работ по водотведению"""


def severagetable_view(request, year):
    try:
        severagetables = SeverageTable.objects.filter(year=year)
    except Exception as e:
        return HttpResponse(e)
    context = {'severagetables': severagetables,
               'year': year}
    return render(request, 'rembaza_app/severagetable.html', context)
