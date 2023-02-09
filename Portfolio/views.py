from django.shortcuts import render

def HomePage(request):
    return render(request,'HomePage.html')

def AboutMe(request):
    return render(request,'AboutMe.html')

def EducationHistory(request):
    return render(request,'EdHist.html')

def SocialMedia(request):
    return render(request,'SocialMedia.html')

def Otherthings(request):
    return render(request,'Oth.html')