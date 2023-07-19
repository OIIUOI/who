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
            return redirect('ifdog:q2-loy')
        
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
            return redirect('ifdog:r-gray')
        elif score < 1:
            return redirect('ifdog:r-siva')
        else:
            return redirect('ifdog:r-jindo')
        
class Q3_Stamina(TemplateView):
    template_name = "question/stem.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < -1:
            return redirect('ifdog:q4-ind')
        elif score < 1:
            return redirect('ifdog:r-bedling')
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
            return redirect('ifdog:r-york')
        else:
            return redirect('ifdog:r-pome')
            
            
        
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
            return redirect('ifdog:r-shihTzu')
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
                return redirect('ifdog:r-dachshund')
        else:
            if score < 0:
                return redirect('ifdog:r-spitz')
            else:
                return redirect('ifdog:r-papillon')
        
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
            return redirect('ifdog:r-sheepdog')
        else:
            return redirect('ifdog:r-collie')

class Q4_Aggressive(TemplateView):
    template_name = "question/agg.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score < 0:
            return redirect('ifdog:r-samoyed')
        else:
            return redirect('ifdog:r-schnauzer')
        
class Q2_loyalty(TemplateView):
    template_name = "question/loyal.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < 1:
            response = redirect('ifdog:q3-indep')
            response.set_cookie("score", score)
            return response
        else:
            return redirect('ifdog:q3-learn')
        
class Q3_Independence2(TemplateView):
    template_name = "question/ind.html"
    
    def post(self, request):
        loy_score = request.COOKIES['score']
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if loy_score < -1:
            if score <= 0:
                return redirect('ifdog:r-beagle')
            else:
                return redirect('ifdog:r-golden')
        else:
            if score <= 0:
                return redirect('ifdog:q4-act')
            else:
                return redirect('ifdog:r-bichon')
            
class Q4_Activity(TemplateView):
    template_name = "question/act.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score <= 0:
            return redirect('ifdog:r-bichon')
        else:
            return redirect('ifdog:r-poodle')

class Q3_Learn(TemplateView):
    template_name = "question/learn.html"
    
    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3

        if score < -1:
            return redirect('ifdog:r-pug')
        elif score < 1:
            return redirect('ifdog:r-cockerSpaniel')
        else:
            return redirect('ifdog:q4-ag')

class Q4_Agg(TemplateView):
    template_name = "question/agg.html"

    def post(self, request):
        [q1, q2, q3] = map(int, [
            request.POST.get("q1"), request.POST.get("q2"), request.POST.get("q3")
            ])
        score = q1 + q2 + q3
        
        if score < 1:
            return redirect('ifdog:r-labrador')
        else:
            return redirect('ifdog:r-dobermann')

################## RESULT #####################

class R_Grayhound(TemplateView):
    template_name = "result/r-grayhound.html"

class R_SivaInu(TemplateView):
    template_name = "result/r-sivainu.html"

class R_Jindo(TemplateView):
    template_name = "result/r-jindo.html"

class R_Yorkshire(TemplateView):
    template_name = "result/r-yorkshire.html"

class R_Pomeranian(TemplateView):
    template_name = "result/r-pomeranian.html"

class R_Bedlington(TemplateView):
    template_name = "result/r-bedling.html"

class R_SiberianHusky(TemplateView):
    template_name = "result/r-husky.html"

class R_WelshCorgi(TemplateView):
    template_name = "result/r-corgi.html"

class R_ShihTzu(TemplateView):
    template_name = "result/r-shihTzu.html"

class R_Chihuahua(TemplateView):
    template_name = "result/r-chihuahua.html"

class R_Spitz(TemplateView):
    template_name = "result/r-spitz.html"

class R_Papillon(TemplateView):
    template_name = "result/r-papillon.html"

class R_Maltese(TemplateView):
    template_name = "result/r-maltese.html"

class R_Papillon(TemplateView):
    template_name = "result/r-papillon.html"

class R_Dachshund(TemplateView):
    template_name = "result/r-dachshund.html"

class R_Sheepdog(TemplateView):
    template_name = "result/r-sheepdog.html"

class R_BorderCollie(TemplateView):
    template_name = "result/r-collie.html"

class R_Samoyed(TemplateView):
    template_name = "result/r-samoyed.html"

class R_Schnauzer(TemplateView):
    template_name = "result/r-schnauzer.html"

class R_Beagle(TemplateView):
    template_name = "result/r-beagle.html"

class R_GoldenRetriever(TemplateView):
    template_name = "result/r-golden.html"

class R_Poodle(TemplateView):
    template_name = "result/r-poodle.html"

class R_Cavalier(TemplateView):
    template_name = "result/r-cavalier.html"

class R_Bichon(TemplateView):
    template_name = "result/r-bichon.html"

class R_Pug(TemplateView):
    template_name = "result/r-pug.html"

class R_CockerSpaniel(TemplateView):
    template_name = "result/r-cockerSpaniel.html"

class R_LabradorRetriever(TemplateView):
    template_name = "result/r-labradorRetriever.html"

class R_Dobermann(TemplateView):
    template_name = "result/r-dobermann.html"