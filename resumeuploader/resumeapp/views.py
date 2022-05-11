from django.shortcuts import render
from django.views import View
from .models import Resume1
from .forms import ResumeForm


# Create your views here.
class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        candidates = Resume1.objects.all()
        return render(request,'resumeapp/home.html',{'candidates':candidates,'form':form})

    def post(self,request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'resumeapp/home.html',{'form':form})

class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume1.objects.get(pk=pk)
        return render(request,'resumeapp/candidate.html',{'candidate':candidate})

