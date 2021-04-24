from django.shortcuts import  render,redirect
from .models import  Profile
from .render import Render
from reportlab.pdfgen import canvas
import io
from django.http import FileResponse
from .form import profileform
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.core.files import  File
from django.http import HttpResponse


def Homepage(request):
    return render(request,"planner/Homepage.html")

# ----for new user---

def index(request):
    return render(request,"planner/index.html")

def profile(request):
    if(request.method == 'POST'):
        name=request.POST['name']
        weight=request.POST['weight']
        height=request.POST['height']
        gender=request.POST['gender']
        startingdate=request.POST['startingdate']
        endingdate=request.POST['endingdate']
        duetodietfor=request.POST['duetodietfor']
        carbohydrates=request.POST['carbohydrates']
        fats=request.POST['fats']
        protein=request.POST['protein']
        text1=request.POST['text1']
        text2=request.POST['text2']
        text3=request.POST['text3']
        text4=request.POST['text4']
        text5=request.POST['text5']
        text6=request.POST['text6']
        text7=request.POST['text7']
        text8=request.POST['text8']
        text9=request.POST['text9']
        profiledata=Profile(Name=name,Weight=weight,Height=height,Gender=gender,StartingDate=startingdate,EndingDate=endingdate,
                     DueToDietFor=duetodietfor,Carbohydrates=carbohydrates,Fats=fats,Protin=protein,AfterWakeUp=text1,
                     BeforeBreakfast=text2,Breakfast=text3,Lunch=text4,Snacks=text5,Dinner=text6,MidNeightDrink=text7,
                     Notes=text8,Excercise=text9)
        profiledata.save()
        profileid=Profile.Id
        print(profileid)
        params={'profileid':profileid}
        return  render(request,"planner/profile.html",params)
    return render(request,"planner/profile.html")

def preview(request):
    return render(request,"planner/basicdetails.html")


def basicdetail(request):
    profiles = Profile.objects.all()
    params = {'profiles': profiles}
    if(request.method == 'POST'):
        id = request.POST['id']
        print(id)
        profile = Profile.objects.filter(Id =id)

        print(profile)
        return render(request,"planner/basicdetails.html",{'profile':profile[0]})
    return render(request,"planner/basicdetails.html",params)

def some_view(request,id):
    profile=Profile.objects.get(Id=id)
    return Render.render('planner/example.html',{'profile':profile})


def listplan(request):
    profiles=Profile.objects.all()
    params={'profiles':profiles}
    return render(request,"planner/listplans.html",params)


def existingplan(request):
    return render(request, "planner/existingplan.html")

def updateform(request,id):
        profile = Profile.objects.filter(Id=id)
        return render(request,'planner/update.html',{'profile':profile[0]})

def update(request,id):
    if request.method == 'POST':
        profile=Profile.objects.get(Id=id)
        name = request.POST['name']
        profile.Name=name
        weight = request.POST['weight']
        profile.Weight=weight
        height = request.POST['height']
        profile.Height=height
        gender = request.POST['gender']
        profile.Gender=gender
        startingdate = request.POST['startingdate']
        profile.StartingDate=startingdate
        endingdate = request.POST['endingdate']
        profile.EndingDate=endingdate
        duetodietfor = request.POST['duetodietfor']
        profile.DueToDietFor=duetodietfor
        carbohydrates = request.POST['carbohydrates']
        profile.Carbohydrates=carbohydrates
        fats = request.POST['fats']
        profile.Fats=fats
        protein = request.POST['protein']
        profile.Protin=protein
        text1 = request.POST['text1']
        profile.AfterWakeUp=text1
        text2 = request.POST['text2']
        profile.BeforeBreakfast = text2
        text3 = request.POST['text3']
        profile.Breakfast = text3
        text4 = request.POST['text4']
        profile.Lunch = text4
        text5 = request.POST['text5']
        profile.Snacks = text5
        text6 = request.POST['text6']
        profile.Dinner = text6
        text7 = request.POST['text7']
        profile.MidNeightDrink = text7
        text8 = request.POST['text8']
        profile.Notes = text8
        text9 = request.POST['text9']
        profile.Excercise = text9
        # profile.save(update_fields=['Name','Weight'])
        profile.save()
        return render(request,"planner/basicdetails.html")





def trackerdetail(request):
    profiles = Profile.objects.all()
    params = {'profiles': profiles}
    return render(request,'planner/trackerdetails.html',params)

def new(request):
    profiles=Profile.objects.all()
    param={'profiles':profiles}
    return render(request,'planner/new.html',param)