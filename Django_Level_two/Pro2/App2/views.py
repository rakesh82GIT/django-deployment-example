from django.shortcuts import render
from App2.models import User
# Create your views here.
def index(request):
    return render(request,'App2/index.html')

def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'App2/users.html',context=user_dict)
