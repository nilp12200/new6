from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"home.html")
def loginpage(request):
    return render(request,"login.html")
def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        MobileNumber = request.POST.get('mobile_number')
        password = request.POST.get('password')
        print(uname, MobileNumber, password)
        # Here you should save the data to the database or perform any other actions
        # For example, you can create a new user object and save it
        # user = User.objects.create(username=uname, mobile_number=MobileNumber, password=password)
        # After saving, you might want to redirect the user to another page, such as a login page
        # return redirect('loginpage')
    return render(request, "login.html")

    