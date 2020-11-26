from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context_dict)

def relative(request):
    return render(request,'basic_app/relative_urls_templates.html')
