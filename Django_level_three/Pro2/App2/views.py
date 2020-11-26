from django.shortcuts import render
#from App2.models import User
from App2.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'App2/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error form invalid')
    return render(request, 'App2/users.html',{'form':form})
