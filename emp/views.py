from math import e
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm
from .models import Department, Employee, Truck
from django.core.paginator import Paginator
from django.db.models import Q  # Import Q for search queries

# Register
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my_login")
    context = { 'regform': form}
    return render(request, 'register.html', context=context)

# Login
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'logform': form}
    return render(request, 'my_login.html', context=context)

# Dashboard
@login_required(login_url='my_login')
def dashboard(request):
    return render(request, 'dashboard.html')

# Employees
@login_required(login_url='my_login')
def all_employees(request):
    search_query = request.GET.get('q', '')
    
    if search_query:
        employees = Employee.objects.filter(
            Q(employeename__icontains=search_query)
        )
    else:
        employees = Employee.objects.all().order_by('employeename')
    
    per_page = request.GET.get('per_page', 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10
    
    paginator = Paginator(employees, per_page)
    page_number = request.GET.get('page', 1)
    employees = paginator.get_page(page_number)
    
    return render(request, 'emp/allemployees.html', {
        "allemployees": employees,
        "search_query": search_query,
        "per_page": per_page
    })

    return render(request, 'emp/allemployees.html', {"allemployees": emp})


@login_required(login_url='my_login')
def add_employee(request):
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Corrected typo here
        
        e = Employee(
            employeename=employeename,
            email=email,
            phone=phone
            
        )
        e.save()
        return redirect('allemployees')
    
    return render(request, 'emp/addemployee.html')

@login_required(login_url='my_login')
def single_employee(request, empid):
    emp = get_object_or_404(Employee, pk=empid)  # Added error handling
    return render(request, 'emp/singleemployee.html', {'singleemp': emp})

@login_required(login_url='my_login')
def update_employee(request, empid):
    emp = get_object_or_404(Employee, pk=empid)
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if not employeename:
            return render(request, 'emp/updateemployee.html', {
                'singleemp': emp,
                'error_message': 'Employee name is required.'
            })
        emp.employeename = employeename
        emp.email = email
        emp.phone = phone
        emp.save()
        return redirect('allemployees')  # Changed hardcoded URL to URL name
    
    return render(request, 'emp/updateemployee.html', {'singleemp': emp})

@login_required(login_url='my_login')
def delete_employee(request, empid):
    e = Employee.objects.get(pk=empid)
    e.delete()
    return redirect('allemployees')

# Departments
@login_required(login_url='my_login')
def all_departments(request):
    search_query = request.GET.get('q', '')

    if search_query:
        dep = Department.objects.filter(
            Q(department__icontains=search_query) |
            Q(building__icontains=search_query)
        )
    else:
        dep = Department.objects.all().order_by('department')
    
    per_page = request.GET.get('per_page', 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    paginator = Paginator(dep, per_page)
    page_number = request.GET.get('page', 1)
    departments = paginator.get_page(page_number)

    return render(request, 'emp/alldepartments.html', {
        "alldepartments": departments,
        "search_query": search_query,
        "per_page": per_page
    })

@login_required(login_url='my_login')
def add_department(request):
    if request.method == 'POST':
        # Retrieve data from the form
        department = request.POST.get('department')
        building = request.POST.get('building')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        # Create a new Department object
        emp = Department(
            department=department,  # Assigning form data to model fields
            building=building,
            email=email,
            contact=contact
        )
        
        # Save the object to the database
        emp.save()

        # Redirect to a page after successful save
        return redirect('/alldepartments')
        
    return render(request, 'emp/adddepartment.html')

@login_required(login_url='my_login')
def single_department(request, empid):
    department = get_object_or_404(Department, pk=empid)
    return render(request, 'emp/singledepartment.html', {'singledepartment': department})

@login_required(login_url='my_login')
def update_department(request, empid):
    department = get_object_or_404(Department, pk=empid)
    if request.method == 'POST':
        department_name = request.POST.get('department')
        building = request.POST.get('building')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        if not department_name:
            return render(request, 'emp/updatedepartment.html', {
                'department': department,
                'error_message': 'Department name is required.'
            })
        department.department = department_name
        department.building = building
        department.email = email
        department.contact = contact
        department.save()
        return redirect('alldepartments')
    return render(request, 'emp/updatedepartment.html', {'department': department})

@login_required(login_url='my_login')
def delete_department(request, empid):
    e = Department.objects.get(pk=empid)
    e.delete()
    return redirect('alldepartments')

# Trucks
@login_required(login_url='my_login')
def all_trucks(request):
    search_query = request.GET.get('q', '')
    selected_day = request.GET.get('day', '')
    sort_order = request.GET.get('sort', 'asc')

    # Set the selected day to today's day if no day is specified
    if not selected_day:
        selected_day = datetime.now().strftime('%A')  # e.g., 'Monday', 'Tuesday'

    trucks = Truck.objects.all()

    # Filter by search query
    if search_query:
        trucks = trucks.filter(
            Q(truck_number__icontains=search_query) |
            Q(origin__icontains=search_query) |
            Q(destination__icontains=search_query) |
            Q(operator__icontains=search_query)
        )

    # Filter by selected day if a specific day is chosen
    if selected_day and selected_day != 'All':
        trucks = trucks.filter(day__icontains=selected_day)

    # Sort by departure time
    sort_field = '-departure_time' if sort_order == 'desc' else 'departure_time'
    trucks = trucks.order_by(sort_field)

    # Pagination
    per_page = request.GET.get('per_page', 10)
    paginator = Paginator(trucks, per_page)
    page_number = request.GET.get('page', 1)
    trucks_paginated = paginator.get_page(page_number)


    return render(request, 'emp/alltrucks.html', {
        "alltrucks": trucks_paginated,
        "search_query": search_query,
        "selected_day": selected_day,  # Pass the selected day to the template
        "per_page": per_page,
        "sort_order": sort_order,
    })
    


@login_required(login_url='my_login')
def add_truck(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        departure_time = request.POST.get('departure_time')
        tender = request.POST.get('tender')
        truck_number = request.POST.get('truck_number')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        operator = request.POST.get('operator')
        contact = request.POST.get('contact')
        e = Truck()
        e.day = day
        e.departure_time = departure_time
        e.tender = tender
        e.truck_number = truck_number
        e.origin = origin
        e.destination = destination
        e.operator = operator
        e.contact = contact
        e.save()

        return redirect('/alltrucks')
    
    return render(request, 'emp/addtruck.html')

@login_required(login_url='my_login')
def single_truck(request, id):
    truck = get_object_or_404(Truck, pk=id)
    return render(request, 'emp/singletruck.html', {'singletruck': truck})

@login_required(login_url='my_login')
def update_truck(request, id):
    truck = get_object_or_404(Truck, pk=id)
    if request.method == 'POST':
        departure_time = request.POST.get('departure_time')
        tender = request.POST.get('tender')
        truck_number = request.POST.get('truck_number')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        operator = request.POST.get('operator')
        contact = request.POST.get('contact')


        if not departure_time:
            return render(request, 'emp/updatetruck.html', {
                'truck': truck,
                'error_message': 'Departure time is required.'
            })
        truck.departure_time = departure_time
        truck.tender = tender
        truck.truck_number = truck_number
        truck.origin = origin
        truck.destination = destination
        truck.operator = operator
        truck.contact = contact
        truck.save()

        return redirect('alltrucks')

    return render(request, 'emp/updatetruck.html', {'truck': truck})

@login_required(login_url='my_login')
def all_rosters(request):
    return render(request, 'emp/allrosters.html')

@login_required(login_url='my_login')
def delete_truck(request, empid):
    e = Truck.objects.get(pk=empid)
    e.delete()
    return redirect('alltrucks')

# Logout
def user_logout(request):
    auth.logout(request)
    return redirect("my_login")
