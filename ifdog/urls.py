'''
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
'''
from django.urls import path
from . import views

app_name = 'ifdog'

urlpatterns = [
    path('q1/', views.Q1_Social.as_view(), name = "q1-social"),
    path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
    path('test/', views.test, name='test'),
    # path('q2_act/', views.Q3_Aggressive.as_view(), name = "q3-agg"),
    # path('q2_act/', views.Q3_Stamina.as_view(), name = "q3-sta"),
    # path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
    # path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
    # path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
    # path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
    # path('q2_act/', views.Q2_Activity.as_view(), name = "q2-act"),
]
