from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')
def aboutus(request):
    if request.method == 'POST':
        # Handle aboutus logic here
        pass
    return render(request, 'app2/aboutus.html')

def contactus(request):
    if request.method == 'POST':
        # Handle contactus logic here
        pass
    return render(request, 'app2/contactus.html')