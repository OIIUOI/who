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
    path('q3_agg/', views.Q3_Aggressive.as_view(), name = "q3-agg"),
    path('q3_stam/', views.Q3_Stamina.as_view(), name = "q3-stam"),
    path('q4_act/', views.Q4_Independence.as_view(), name = "q4-ind"),
    path('q4_learn/', views.Q4_Learn.as_view(), name = "q4-learn"),

    path('q2_stam/', views.Q2_Stamina.as_view(), name = "q2-stam"),
    path('q3_ag/', views.Q3_Agg.as_view(), name = "q3-ag"),
    path('q3_ind/', views.Q3_Independence.as_view(), name = "q3-ind"),
    path('q4_learn2/', views.Q4_Learn2.as_view(), name = "q4-lea"),
    
    path('q3-insist/', views.Q3_Insist.as_view(), name='q3-ins'),
    path('q4-agg/', views.Q4_Aggressive.as_view(), name="q4-agg")
    ################## result ####################
    path('r-grayhound/', views.R_Grayhound.as_view(), name = "r-gray"),
    path('r-sivaInu/', views.R_SivaInu.as_view(), name = "r-siva"),
    path('r-jindo/', views.R_Jindo.as_view(), name = "r-jindo"),
    
]

''' 
r-shihtzu
r-chihuahua
r-husky
r-corgi
r-pomeranian
r-yorkshire
r-Bedlington_Terrier
'''