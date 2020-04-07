from django.shortcuts import render

# Create your views here.
# request가 들어왔을 때, home이라는 html을 갔다줘! :
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')