from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.http import JsonResponse

# Create your views here.

class Q1_Social(TemplateView):
    template_name = "question/social.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")])
        score = q1 + q2 + q3
        
        if score < -1:
            return redirect('ifdog:q2-act')
        elif score < 1:
            return redirect('ifdog:q2-strength')
        else:
            return redirect('ifdog:q2-activity')
        
class Q2_Activity(TemplateView):
    template_name = "question/act.html"

    def post(self, request):
        [q1, q2, q3] = map(int,[
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score <= 0:
            return redirect('ifdog:q3-agg')
        else:
            return redirect('ifdog:q3-stam')
        
class Q3_Aggressive(TemplateView):
    template_name = "question/agg.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < -1:
            return redirect('ifdog:r-grayhound')
        elif score < 1:
            return redirect('ifdog:r-siva')
        else:
            return redirect('ifdog:r-zindo')
        
class Q3_Stamina(TemplateView):
    template_name = "question/stem.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < -1:
            return redirect('ifdog:ind')
        elif score < 1:
            return redirect('ifdog:r-bed')
        else:
            return redirect('ifdog:q4-learn')

class Q4_Independence(TemplateView):
    template_name = "question/ind.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        if score <= 0:
            return redirect('r-yorkshire')
        else:
            return redirect('r-pomeranian')
            
            
        
class Q4_Learn(TemplateView):
    template_name = "question/learn.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score <= 0:
            return redirect('r-husky')
        else:
            return redirect('r-corgi')
            
class Q2_Stamina(TemplateView):
    template_name = "question/stem.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < -1:
            return redirect('ifdog:q3-agg')
        elif score < 1:
            return redirect('ifdog:q3-ind')
        else:
            return redirect('ifdog:q3-ins')

class Q3_Agg(TemplateView):
    template_name = "question/agg.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < 1:
            return redirect('ifdog:r-shihtzu')
        else:
            return redirect('ifdog:r-chihuahua')

class Q3_Independence(TemplateView):
    template_name = "question/ind.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        ### cookie
        return redirect
        
class Q4_Learn(TemplateView):
    template_name = "question/learn.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score <= 0:
            return redirect('r-husky')
        else:
            return redirect('r-corgi')

        
################## RESULT #####################

class R_Grayhound(TemplateView):
    template_name = "result/r-grayhound.html"


class R_SivaInu(TemplateView):
    template_name = "result/r-sivainu.html"

class R_Jindo(TemplateView):
    template_name = "result/r-jindo.html"

class R_Bedlington(TemplateView):
    template_name = "result/r-bed.html"