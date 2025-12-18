# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#         path('contact/', views.contact, name='contact'),  # ✅ Add this line
#        path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]


# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),  # ✅ Add this
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/hero/', views.dashboard_hero, name='dashboard_hero'),
    path('dashboard/about/', views.dashboard_about, name='dashboard_about'),
    path('dashboard/services/', views.dashboard_services, name='dashboard_services'),
    path('dashboard/features/', views.dashboard_features, name='dashboard_features'),
    path('dashboard/whychoose/', views.dashboard_whychoose, name='dashboard_whychoose'),
    path('dashboard/footer/', views.dashboard_footer, name='dashboard_footer'),
    path('contact/', views.contact, name='contact'),
]


