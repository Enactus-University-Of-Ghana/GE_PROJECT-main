from multiprocessing import context
from pyexpat import model
from django.forms import Form
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from . models import ProjectModel, TaskModel,report,document
from . forms import TaskModelForm, TaskUpdateForm, reportform,ProjectForm,fileform
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django import db
from django.http import HttpResponse#import http.Response
from django.db import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import get_user_model
# Create your views here.

@login_required()
def index(request):
    if request.method=='POST':#if there is a request to post
        form=TaskModelForm(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/task')
    else:
        form=TaskModelForm()

    data=TaskModel.objects.all().order_by('piority')# the same as TaskModel.objects.raw('select * from "taskapp_Taskmodel" ')

    total_task=data.count()
    total_completed_task=TaskModel.objects.filter(status='Complete').count()
    total_pending_task=TaskModel.objects.filter(status='Pending').count()
    total_cancelled_task=total_task-(total_completed_task+total_pending_task)
    high_risk=TaskModel.objects.filter(piority='high').count()
    med_risk=TaskModel.objects.filter(piority='medium').count()
    low_risk=TaskModel.objects.filter(piority='low').count()
    amount=TaskModel.objects.all()
    
    total_budget=0
    total_cost=0
    
    for p in data:
        t=TaskModel.objects.filter(projects=p.id)
        total_budget=0
        total_cost=0
        percentage=0
        completed_task=t.filter(status='Complete').count()
        pending_task=t.filter(status='Pending').count()
        if completed_task+pending_task==0:
            percentage=0
        else:
            percentage=(completed_task/(completed_task+pending_task))*100
        p.percentage=percentage
        for task in t:
            total_budget=total_budget+task.budget
            total_cost=total_cost+task.cost
        p.budget=total_budget
        p.project_number=total_cost
    

    for task in amount:
        total_budget=total_budget+task.budget
        total_cost=total_cost+task.cost
    

    balance=total_budget-total_cost
    context={
        'data':data,
        'total_budget':total_budget,
        'balance':balance,
        'total_cost':total_cost,
        'form':form,
        'total_task':total_task,
        'completed_task':completed_task,
        'pending_task':pending_task,
        'total_completed_task':total_completed_task,
        'total_pending_task':total_pending_task,

        'high_risk':high_risk,
        'medium_risk':med_risk,
        'low_risk':low_risk,
        'total_cancelled_task':total_cancelled_task,
    }
    return render(request,"task.html",context)#loads the html file.passes in data from the modles file
@login_required()
def project(request):
    data=ProjectModel.objects.all().order_by('-date')
    completed_task=TaskModel.objects.filter(status='Complete').count()
    pending_task=TaskModel.objects.filter(status='Pending').count()
    
    work=TaskModel.objects.all()
    if request.method=='POST':#if there is a request to post
        form=ProjectForm(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/project')
    else:
        form=ProjectForm()



    for p in data:
        t=TaskModel.objects.filter(projects=p.id)
        task=TaskModel.objects.all()
        total_budget=0
        total_cost=0
        percentage=0
        completed_task=t.filter(status='Complete').count()
        pending_task=t.filter(status='Pending').count()
        if completed_task+pending_task==0:
            percentage=0
        else:
            percentage=(completed_task/(completed_task+pending_task))*100
        p.percentage=percentage
        for task in t:
            total_budget=total_budget+task.budget
            total_cost=total_cost+task.cost
        p.budget=total_budget
        p.project_number=total_cost
        

    #balance=total_budget-total_cost
    #total_project=data.count()
    #completed_task=TaskModel.objects.filter(status='Complete').count()
    #pending_task=TaskModel.objects.filter(status='Pending').count()
    #cancelled_task=total_task-(completed_task+pending_task)

    context={
        'form':form,
        'data':data,
        'work':work,


    }
    return render(request,"project.html",context)
@login_required()
def about(request):
    return render(request,"about.html")
@login_required()
def delete(request,pk):
    item=TaskModel.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/task')
    return render(request,"delete.html")
@login_required()
def edit(request,pk):
    item=TaskModel.objects.get(id=pk)

    if request.method=='POST':
        form=TaskUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/task')
    else:
        form=TaskUpdateForm(instance=item)


    context={
        'form':form
    }
    return render(request,'edit.html',context)
@login_required()
def reports(request):
    data=report.objects.all()
    if request.method=='POST':#if there is a request to post
        form=reportform(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/report')
    else:
        form=reportform()
    
    context={
        'data':data,
        'form':form,
    }

    return render(request,"reports.html",context)#loads the html file.passes in data from the models file
@login_required()
def edit_report(request,pk):
    item=report.objects.get(id=pk)

    if request.method=='POST':
        form=reportform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/report')
    else:
        form=reportform(instance=item)
        
    context={
        'form':form,
    }
    return render(request,"editreport.html",context)
@login_required()
def delete_report(request,pk):
    item=report.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/report')
    return render(request,"delete.html")
    
@login_required()
def dashboard(request):
    return render(request,"dashboard.html")
@login_required()
def edit_project(request,pk):
    item=ProjectModel.objects.get(id=pk)

    if request.method=='POST':
        form=ProjectForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/project')
    else:
        form=ProjectForm(instance=item)
        
    context={
        'form':form,
    }
    return render(request,"editproject.html",context)

@login_required()
def delete_project(request,pk):
    item=ProjectModel.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/project')
    return render(request,"deleteproject.html")
@login_required()
def todo(request):
    data=TaskModel.objects.all().order_by('id')
    pdata=ProjectModel.objects.all().order_by('-date')
    for p in pdata:
        t=TaskModel.objects.filter(projects=p.id)
        total_budget=0
        total_cost=0
        percentage=0
        completed_task=t.filter(status='Complete').count()
        pending_task=t.filter(status='Pending').count()
        if completed_task+pending_task==0:
            percentage=0
        else:
            percentage=(completed_task/(completed_task+pending_task))*100
        p.percentage=percentage
        for task in t:
            total_budget=total_budget+task.budget
            total_cost=total_cost+task.cost
        p.budget=total_budget
        p.project_number=total_cost

    context={
        'data':data,
        'pdata':pdata,
    }
    return render(request,"todo.html",context)
@login_required()
def budget(request):
    data=TaskModel.objects.all().order_by('-date')
    pdata=ProjectModel.objects.all().order_by('-date')
    for p in pdata:
        t=TaskModel.objects.filter(projects=p.id)
        total_budget=0
        total_cost=0
        completed_task=t.filter(status='Complete').count()
        pending_task=t.filter(status='Pending').count()
        for task in t:
            total_budget=total_budget+task.budget
            total_cost=total_cost+task.cost
        p.budget=total_budget
        p.project_number=total_cost
        if completed_task+pending_task==0:
            percentage=0
        else:
            percentage=(completed_task/(completed_task+pending_task))*100
        p.percentage=percentage
    context={
        'data':data,
        'pdata':pdata,
    }
    return render(request,"budget.html",context)
@login_required()
def timeline(request):
    data=TaskModel.objects.all().order_by('-date')
    pdata=ProjectModel.objects.all().order_by('-date')
    
    context={
        'data':data,
        'pdata':pdata,
    }
    return render(request,"timeline.html",context)
@login_required()
def risk(request):
    data=TaskModel.objects.all().order_by('-date')
    pdata=ProjectModel.objects.all().order_by('-date')
    high_risk=TaskModel.objects.filter(piority='high').count()
    med_risk=TaskModel.objects.filter(piority='medium').count()
    low_risk=TaskModel.objects.filter(piority='low').count()
    context={
        'data':data,
        'pdata':pdata,
        'high_risk':high_risk,
        'medium_risk':med_risk,
        'low_risk':low_risk,
    }
    return render(request,"risk.html",context)
@login_required()
def logout_request(request):
    logout(request)
    messages.info(request,"you are logged out")
    return redirect('login/')

@login_required()
def file(request):
    data=document.objects.all()
    if request.method=='POST':#if there is a request to post
        form=fileform(request.POST,request.FILES)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/file')
    else:
        form=fileform()
    
    context={
        'data':data,
        'form':form,
    }
    return render(request,"file.html",context)

@login_required()
def edit_file(request,pk):
    item=document.objects.get(id=pk)

    if request.method=='POST':
        form=fileform(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/file')
    else:
        form=fileform(instance=item)
        
    context={
        'form':form,
    }
    return render(request,"editfile.html",context)

@login_required()
def delete_file(request,pk):
    item=ProjectModel.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/project')
    return render(request,"deletefile.html")