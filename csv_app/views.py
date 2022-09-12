import csv

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from csv_app.forms import Registration_form
from csv_app.models import Employee

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_page(request):
    
    if request.method =='POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user = authenticate(request,username=username,password=password)
            if user :
                login(request,user)
                messages.success(request,f'you are logged in successfully {username}')
                return redirect('home')
            else:
                messages.error(request,"please provide correct credencials")    
    
        else:
            messages.error(request,"please provide correct credencials")    
    form = AuthenticationForm()
    return render(request,'login.html',{'data':form})

def logout_app(request):
    logout(request,) 
    messages.info(request,'log out successfully')
    return redirect('login')


def home(request):
    
    return render(request,'home.html')
def export_csv(request):
    data = Employee.objects.filter(active = True)
    # print(data)
    
    
    
    response = HttpResponse(content_type = 'text/csv')
    csv_writer = csv.writer(response)
    csv_writer.writerow(['ID','NAME','SALARY','COMPANY','DESIGNATION','DOJ','ACTIVE'])
    for emp in data.values_list('id','name','salary','company','Designation','DOJ','active'):
        csv_writer.writerow(emp)
    
    response['Content-Disposition'] = 'attachment; filename = "emp_data.csv"'
    
    return response

def import_csv(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        # print('please provide CSV file ')
        messages.error(request,'Please provide csv file to load the data')
        return render(request,'upload.html') 
    
    file_data = csv_file.read().decode("utf-8")   
    messages.info(request,'file loaded successfully ,processing to load the data')
    lines = file_data.split("\n") 
    # print(lines)       
    for i  in range(1,len(lines)-1):
        # print(i)
        fields = lines[i].split(",")
        # print(fields)
        # print(fields[1],fields[2])

        a = Employee(name = fields[1],salary =fields[2],company=fields[3],Designation = fields[4])
        a.save()
        
    messages.success(request,"data saved successfully")
        # print(fields)
    return redirect('home')     
		
    
def reg_form(request):
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'User created successfully ...!!!')
            return redirect('home')
        else:
            messages.error(request,'Please provide correct details ')    
            
    form = Registration_form 
    return render(request,'rf.html',{'data':form})   

    
    