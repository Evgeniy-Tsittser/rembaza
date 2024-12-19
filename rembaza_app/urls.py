from django.urls import path
from .views import year_view, year_detail, monthworks_list, watertable_view, severagetable_view

urlpatterns = [
    path('', year_view, name='years'),
    path('year_detail/<int:year>', year_detail, name='year_detail'),
    path('month/<int:year>/<int:month>/', monthworks_list, name='monthworks_list'),
    path('water/<int:year>/', watertable_view, name='watertable'),
    path('severage/<int:year>', severagetable_view, name='severagetable'),
]
