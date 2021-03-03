from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def create_poll(request):

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = PollForm()

    context = {'form':form}

    return render(request,'poll/create_poll.html',context)

def home(request):
    polls = Poll.objects.all().order_by('-id')
    context = {'polls':polls}
    return render(request,'poll/home.html',context)

def vote(request,pk):
    poll = Poll.objects.get(pk=pk)

    if request.method == 'POST':
        selected_option = request.POST['poll']

        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400,'Invalid Form')

        poll.save()
        return redirect('poll:result',poll.id)

    context = {'poll':poll}
    return render(request,'poll/vote.html',context)

def result(request,pk):
    poll = Poll.objects.get(pk=pk)
    context = {'poll':poll}

    return render(request,'poll/result.html',context)
