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
    path('q4_ind/', views.Q4_Independence.as_view(), name = "q4-ind"),
    path('q4_learn/', views.Q4_Learn.as_view(), name = "q4-learn"),

    path('q2_stam/', views.Q2_Stamina.as_view(), name = "q2-stam"),
    path('q3_ag/', views.Q3_Agg.as_view(), name = "q3-ag"),
    path('q3_ind/', views.Q3_Independence.as_view(), name = "q3-ind"),
    path('q4_learn2/', views.Q4_Learn2.as_view(), name = "q4-lea"),
    
    path('q3_insist/', views.Q3_Insist.as_view(), name='q3-ins'),
    path('q4_agg/', views.Q4_Aggressive.as_view(), name="q4-agg"),

    path('q2_loyalty/', views.Q3_loyalty.as_view(), name="q2-loy"),
    path('q3_indep/', views.Q3_Independence2.as_view(), name="q3-indep"),
    path('q4_act/', views.Q4_Activity.as_view(), name='q4-act'),
    path('q3_learn/', views.Q3_Learn.as_view(), name="q3-learn"),
    path('q4_ag/', views.Q4_Agg.as_view(), name="q4-ag"),

    ################## result ####################
    path('r-grayhound/', views.R_Grayhound.as_view(), name = "r-gray"),
    path('r-sivaInu/', views.R_SivaInu.as_view(), name = "r-siva"),
    path('r-jindo/', views.R_Jindo.as_view(), name = "r-jindo"),
    path('r-yorkshire/', views.R_Yorkshire.as_view(), name = "r-yorkshire"),
    path('r-pome/', views.R_Pomeranian.as_view(), name = "r-pome"),
    path('r-bedling/', views.R_Bedlington.as_view(), name = "r-bedling"),
    path('r-siberian/', views.R_SiberianHusky.as_view(), name = "r-husky"),
    path('r-corgi/', views.R_WelshCorgi.as_view(), name = "r-corgi"),
    path('r-shihTzu/', views.R_ShihTzu.as_view(), name = "r-shihTzu"),
    path('r-chihuahua/', views.R_Chihuahua.as_view(), name = "r-chihuahua"),
    path('r-spitz/', views.R_Spitz.as_view(), name = "r-spitz"),
    path('r-papillon/', views.R_Papillon.as_view(), name = "r-papillon"),
    path('r-maltese/', views.R_Maltese.as_view(), name = "r-maltese"),
    path('r-papillon/', views.R_Papillon.as_view(), name = "r-papillon"),
    path('r-dachshund/', views.R_Dachshund.as_view(), name = "r-dachshund"),
    path('r-sheepdog/', views.R_Sheepdog.as_view(), name = "r-sheepdog"),
    path('r-collie/', views.R_BorderCollie.as_view(), name = "r-collie"),
    path('r-samoyed/', views.R_Samoyed.as_view(), name = "r-samoyed"),
    path('r-schnauzer/', views.R_Schnauzer.as_view(), name = "r-schnauzer"),
    path('r-beagle/', views.R_Beagle.as_view(), name = "r-beagle"),
    path('r-golden/', views.R_GoldenRetriever.as_view(), name = "r-golden"),
    path('r-poodle/', views.R_Poodle.as_view(), name = "r-poodle"),
    path('r-cavalier/', views.R_Cavalier.as_view(), name = "r-cavalier"),
    path('r-bichon/', views.R_Bichon.as_view(), name = "r-bichon"),
    path('r-pug/', views.R_Pug.as_view(), name = "r-pug"),
    path('r-cockerSpaniel/', views.R_CockerSpaniel.as_view(), name = "r-cockerSpaniel"),
    path('r-labradorRetriever/', views.R_LabradorRetriever.as_view(), name = "r-labrador"),
    path('r-dobermann/', views.R_Dobermann.as_view(), name = "r-dobermann"),
]
