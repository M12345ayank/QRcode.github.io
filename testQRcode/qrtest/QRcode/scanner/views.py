from django.shortcuts import render
from scanner.models import Register,Login

# Create your views here.
#from django.shortcuts import  render, redirect
#from .forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import messages

def register_request(request):
    if request.method=="POST":
        vehicle = request.POST['vehicle']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        ins = Register(vehicle=vehicle, password=password, phone=phone, email=email)
        ins.save()

        print("data has been written to database")
    return render(request, 'register.html')
          
        


		#form = NewUserForm(request.POST)
		#if form.is_valid():
			#user = form.save()
			#login(request, user)
			#messages.success(request, "Registration successful." )
			#return redirect("main:homepage")
		#messages.error(request, "Unsuccessful registration. Invalid information.")
	#form = NewUserForm()
	#return render (request=request, template_name="register.html", context={"register_form":form})
def login(request):
    if request.method=="POST":
        vehicle = request.POST['vehicle']
        password = request.POST['password']

        all_members=Register.objects.filter(vehicle=vehicle,password=password).values()
        if all_members.exists():
            return render(request, 'profile.html',{'all':all_members})
        else:  
            print(all_members)
            return render(request, 'error.html')
    print("data has been written to database")
    return render(request, 'login.html')