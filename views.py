
from django.shortcuts import redirect, render
from .models import Participant
from .forms import ParticipantForm
from django.contrib import messages
# Create your views here.
def home(request):
    all_participants= Participant.objects.all
    return render(request , 'home.html' , {'all':all_participants})

def come(request):
    if request.method == "POST" :
        form= ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            name = request.POST['name']
            branch = request.POST['branch']
            phone = request.POST['phone']
            roll = request.POST['roll']
            email = request.POST['email']
            subit = request.POST['subit']
            messages.success(request,('error'))
            # return redirect('come')
            return render(request , 'come.html' , { 'name':name,
             'branch':branch,
             'email' :email,
             'roll': roll,
              'phone':phone,
              'subit':subit
             
             })
        messages.success(request, ('submitted'))
        return render(request,'thankyou')
        # return redirect('thankyou.html')
    else :
         
        return render(request , 'come.html' , {})
