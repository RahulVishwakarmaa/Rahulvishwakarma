from django.shortcuts import render,redirect
import faker
fake=faker.Faker()
from .models import EmployeeData,feedbackData
from .form import CreateUserForm
from django.http.response import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register_page(request):
    if request.user.is_authenticated:
        return redirect( 'main_page')
    else:
        if request.method=='POST':
            forms=CreateUserForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect("login")
            else:
                messages.warning(request, 'Filled Incorrect Details**')
                return redirect('register')
        else:
            forms=CreateUserForm()
            return render(request,'register_file.html',{'forms':forms})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfull..')
                return redirect('main_page')
            else:
                messages.warning(request,'Username or Password Incorrect')
                return render(request,'login_page.html')
        else:
            return render(request,'login_page.html')






# Create your views here.


def employee_data(request):
    for i in range(1000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            job = fake.random_element(elements=('Admin', 'HR', 'SOFTWARE', 'TRAINER'))
            email = fake.email()
            salary = fake.random_element(elements=(10000, 20000, 30000, 40000, 50000))
            company= fake.random_element(elements=('Wipro','TCS','CTS','Infosys'))
            city = fake.random_element(elements=('DEORIA', 'GORAKHPUR', 'LUCKNOW', "KANPUR"))
            state = fake.random_element(elements=('UTTARPRADESH','MADHYAPRADESH','BIHAR',"UTTARAKHAND"))
            address = fake.address()

            EmployeeData(
                first_name=first_name,
                last_name=last_name,
                job=job,
                email=email,
                salary=salary,
                company=company,
                city=city,
                state=state,
                address=address,
            ).save()
    return HttpResponse("Data Save")


@login_required(login_url=('login'))
def main_page(request):
    return render(request,'main_page.html')


def feching_data(request):
    employees=EmployeeData.objects.all()
    return render (request,'Employee_data.html',{'employees':employees})


#For lko citys
@login_required(login_url=('login'))
def Lucknow_employee_data(request):

    if request.method=='POST':
        company1=request.POST.get('company1')

        employees = EmployeeData.objects.filter(city='LUCKNOW')& EmployeeData.objects.filter(company=company1)
        total_lko_emps = len(employees)
        return render(request, 'lucknow_data.html', {'employees': employees, 'total_lko_emp': total_lko_emps,'company1':company1})
    else:
        employees=EmployeeData.objects.filter(city='LUCKNOW')
        total_lko_emps= len(employees)
        return render(request,'lucknow_data.html',{'employees':employees,'total_lko_emp':total_lko_emps})


#for Gorakhpur city


@login_required(login_url=('login'))
def Gorakhpur_employee_data(request):
    if request.method=='POST':
        company1=request.POST.get('company1')
        employees = EmployeeData.objects.filter(city='GORAKHPUR') & EmployeeData.objects.filter(company=company1)
        total_gkp_emps = len(employees)
        return render(request, 'gorkhpur_data.html', {'employees': employees, 'total_gkp_emp': total_gkp_emps,'company1':company1})
    else:
        employees=EmployeeData.objects.filter(city='GORAKHPUR')
        total_gkp_emps = len(employees)
        return render(request,'gorkhpur_data.html',{'employees':employees,'total_gkp_emp':total_gkp_emps})

#For Deoria Data

@login_required(login_url=('login'))
def Deoria_employee_data(request):
    if request.method=='POST':
        company1=request.POST.get('company1')
        employees=EmployeeData.objects.filter(city='DEORIA')&EmployeeData.objects.filter(company=company1)
        total_deo_emps= len(employees)
        return render(request,'deoria_data.html',{'employees':employees,'total_deo_emp':total_deo_emps,'company1': company1})
    else:
        employees = EmployeeData.objects.filter(city='DEORIA')
        total_deo_emps = len(employees)
        return render(request, 'deoria_data.html', {'employees': employees, 'total_deo_emp': total_deo_emps})


#For Kanpur data
@login_required(login_url=('login'))
def Kanpur_employee_data(request):
    if request.method=='POST':
        company1=request.POST.get('company1')
        employees=EmployeeData.objects.filter(city='KANPUR') & EmployeeData.objects.filter(company=company1)
        total_knp_emps = len(employees)
        return render(request,'kanpur_data.html',{'employees':employees,'total_knp_emp':total_knp_emps,'company1':company1})
    else:

        employees = EmployeeData.objects.filter(city='KANPUR')
        total_knp_emps = len(employees)
        return render(request, 'kanpur_data.html', {'employees': employees, 'total_knp_emp': total_knp_emps})


def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successfully..')
    return redirect('login')




#feedback
@login_required(login_url=('login'))
def feedback_view(request):
    if request.method =='GET':
        return render(request,'feedback.html')
    else:

        sname1 =request.POST.get('sname')

        rating1 =request.POST.get('rating')
        feedback1 =request.POST.get('feedback')

        data1=feedbackData(
            name=sname1,

            rating=rating1,
            feedback=feedback1,

        )
        data1.save()
        feedbacks= feedbackData.objects.all()
        return render(request,'feedback.html',{'feedbacks':feedbacks})

