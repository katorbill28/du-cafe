from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE = EXPLORE PAGE
    path('', views.explore, name='home'),

    # PAGE 2 = CAMPUS OVERVIEW PAGE (NORTH/SOUTH/OFF)
    path('campuses/', views.campuses_overview, name='campuses'),

    # CAMPUS LIST PAGE
    path('campus/<str:campus>/', views.campus_list, name='campus_list'),

    # CAFE DETAIL PAGE
    path('cafe/<int:cafe_id>/', views.cafe_detail, name='cafe_detail'),

    # FINDER PAGE (optional)
    path('finder/', views.finder_home, name='finder'),
]

