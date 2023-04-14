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
            return redirect('ifdog:q2-stam')
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
            return redirect('ifdog:r-yorkshire')
        else:
            return redirect('ifdog:r-pomeranian')
            
            
        
class Q4_Learn(TemplateView):
    template_name = "question/learn.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score <= 0:
            return redirect('ifdog:r-husky')
        else:
            return redirect('ifdog:r-corgi')
            
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
        response = redirect('ifdog/q4-lea')
        response.set_cookie("score", score)
        return response
        
class Q4_Learn2(TemplateView):
    template_name = "question/learn.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        ind_score = request.COOKIES['score']
        
        if ind_score < 0: # if dependent
            if score < -2:
                return redirect('ifdog:r-maltese')
            else:
                return redirect('r-dachshund')
        else:
            if score < 0:
                return redirect('r-spitz')
            else:
                return redirect('r-papillon')
        
class Q3_Insist(TemplateView):
    template_name = 'question/insist.html'

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score < 0:
            return redirect('ifdog:q4-act')
        else:
            return redirect('ifdog:q4-agg')
        
class Q4_Activity(TemplateView):
    template_name="question/act.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score < 0:
            return redirect('ifdog:r-shetlandSheepdog')
        else:
            return redirect('ifdog:r-borderCollie')

class Q4_Aggressive(TemplateView):
    template_name="question/agg.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score < 0:
            return redirect('ifdog:r-samoyed')
        else:
            return redirect('ifdog:r-Schnauzer')
################## RESULT #####################

class R_Grayhound(TemplateView):
    template_name = "result/r-grayhound.html"


class R_SivaInu(TemplateView):
    template_name = "result/r-sivainu.html"

class R_Jindo(TemplateView):
    template_name = "result/r-jindo.html"

class R_Bedlington(TemplateView):
    template_name = "result/r-bed.html"