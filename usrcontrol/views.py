from django.shortcuts import render
from adivina.forms import NewUserForm
from usrcontrol.models import User
# Create your views here.

def index(request):
    return render(request,'adivina/index.html')

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
            
    return render(request,'usrcontrol/users.html', {'form':form})

def ranking(request):
    ranking_list = User.objects.order_by('intentos')
    ranking_dict = {'users':ranking_list}
    return render(request,'usrcontrol/rankings.html', context=ranking_dict)