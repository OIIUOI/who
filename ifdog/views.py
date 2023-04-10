from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.http import JsonResponse

# Create your views here.

class Q1_Social(TemplateView):
    template_name = "question/q1.html"

    def post(self, request):
        q1, q2, q3 = request.POST.get("q1")
        print(q1)
        
        if q1 == "-2":
            return redirect('ifdog:q2-act')
        # elif score == "mid":
        #     return redirect('ifdog:q2-strength')
        # else:
        #     return redirect('ifdog:q2-activity')
        return redirect('ifdog:q2-at')

def test(request):
    if request.method == "POST":
        print(request.POST)
        return redirect('ifdog:q2-act')
    return render(request, 'question/q1.html')
        
class Q2_Activity(TemplateView):
    template_name = "question/q2.html"

    # def post(self, request):
    #     score = request.POST.get("score")
    #     if score == "calm":
    #         return redirect('ifdog:q3-agg')
    #     else:
    #         return redirect('ifdog:q3-sta')
        
# class Q3_Aggressive(View):
#     def get(self, request):
#         return render(request, 'ifdog:q3-agg')

#     def post(self, request):
#         score = request.POST.get("score")
#         if score == "up":
#             return redirect('r-jindo')
#         elif score == "middle":
#             return redirect('r-siba')
#         else:
#             return redirect('r-gray')
        
# class Q3_Stamina(View):
#     def get(self, request):
#         return render(request, 'ifdog:q3-sta')

#     def post(self, request):
#         score = request.POST.get("score")
#         if score == "up":
#             return redirect('ifdog:q4-learn')
#         elif score == "middle":
#             return redirect('r-bedlington')
#         else:
#             return redirect('ifdog:q4-ind')

# class Q4_Independence(View):
#     def get(self, request):
#         return render(request, 'ifdog:q4-ind')

#     def post(self, request):
#         score = request.POST.get("score")
#         if score == "independent":
#             return redirect('r-yorkshire')
#         else:
#             return redirect('r-pomeranian')
        
# class Q4_Learn(View):
#     def get(self, request):
#         return render(request, 'ifdog:q4-learn')

#     def post(self, request):
#         score = request.POST.get("score")
#         if score == "high":
#             return redirect('r-corgi')
#         else:
#             return redirect('r-husky')