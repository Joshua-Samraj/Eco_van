from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
# Create your views here.

def index(request):
    
    fund_data = {'raised': 0, 'goal': 1}  # prevent division by zero
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, 'fund.txt'), 'r') as f:
            lines = f.readlines()
            fund_data = dict(line.strip().split('=') for line in lines)
            fund_data['raised'] = int(fund_data['raised'])
            fund_data['goal'] = int(fund_data['goal'])
            print(fund_data['goal'])
            print("get data")
    except Exception as e:
        print("Error reading fund data:", e)

    return render(request, 'index.html', fund_data)


# Hardcoded admin credentials (for demo only)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard_new')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('admin_login')
    return render(request, 'admin_login.html')

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    

    fund_file = os.path.join(settings.BASE_DIR, 'fund.txt')  # safer if used with write permissions


    fund_data = {'raised': 0, 'goal': 1}

    if request.method == 'POST':
        # Save changes to fund.txt
        raised = request.POST.get('raised')
        goal = request.POST.get('goal')
        try:
            with open(fund_file, 'w') as f:
                f.write(f'raised={raised}\n')
                f.write(f'goal={goal}\n')
            messages.success(request, 'Fund data updated successfully.')
        except Exception as e:
            messages.error(request, f'Error saving data: {e}')

    # Load current fund data
    try:
        with open(fund_file, 'r') as f:
            lines = f.readlines()
            fund_data = dict(line.strip().split('=') for line in lines)
            fund_data['raised'] = int(fund_data['raised'])
            fund_data['goal'] = int(fund_data['goal'])
    except Exception as e:
        messages.error(request, f'Error reading fund data: {e}')

    return render(request, 'admin_dashboard.html', {'fund_data': fund_data})
