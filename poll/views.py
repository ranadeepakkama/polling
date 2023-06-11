from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .form import newForm, userCreatedPollFm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Polling
from django.contrib.auth.models import User



# Create your views here.

def register(request):
    form = newForm()
    if request.method == 'POST':
        form = newForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request,'new user registerd successfully ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request,'register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user) 
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    context = {}
    return render(request,'login.html',context)


def logoutRequest(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def homePage(request):
    user = request.user
    if request.method == 'POST':
        return redirect('poll')
    context = {'user': user}
    return render(request, 'index.html',context)

@login_required(login_url='/login')
def pollPage(request):
    data = Polling.objects.all()
    context = {'data': data}
    return render(request, 'poll.html',context)

@login_required(login_url='/login')
def createPoll(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        form = userCreatedPollFm(request.POST)
        k = Polling(question= question)
        if form.is_valid():
            k = form
        k.save()
        return redirect('poll')
    else:
        form = userCreatedPollFm()
    context = {'form': form}
    return render(request, 'createPoll.html',context)

@login_required(login_url='/login')
def deletePoll(request,id):
    data = get_object_or_404(Polling,id = id)
    data.delete()
    return redirect('poll')

@login_required(login_url='/login')
def search(request):
    query = request.GET.get('q')
    if query:
        filter_data = Polling.objects.filter(question__icontains = query)
    else:
        filter_data = None
    
    return render(request,'poll.html',{'filter_data': filter_data})

@login_required(login_url='/login')
def votePage(request, id):
    data = get_object_or_404(Polling, id=id)
    user = request.user
    print(user)


    if user not in data.voters.all():
        if request.method == 'POST':
            select_choice = request.POST.get('data')
            if select_choice == 'option1':
                data.option1_count += 1
            elif select_choice == 'option2':
                data.option2_count += 1
            elif select_choice == 'option3':
                data.option3_count += 1
            else:
                return HttpResponse('Invalid choice')
            
            
            data.total_result = (data.option1_count + data.option2_count + data.option3_count)
            data.voters.add(user)
            data.save()
            print(data.total_result)
        
            return redirect('result', id=data.id)
    else:
        messages.error(request,"You have already voted")

    
    context = {'poll': data}
    return render(request, 'votePage.html', context)



@login_required(login_url='/login')
def result(request,id):
    data = get_object_or_404(Polling,id = id)
    context = {'data':data}
    return render(request,'votePage.html',context)

def user(request):
    data = request.user
    context = {'data':data}
    return render(request,'user.html',context)

    