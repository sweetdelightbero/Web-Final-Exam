# Django Import
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages



# Python Import
import random

# Create your views here.
def Homepage(request):
    if request.POST.get('start',''):
        return redirect('Game')
    return render(request, 'index.html')

def Game(request):
    gamelist = ['rock', 'paper', 'scissors']
    bot_action = random.choice(gamelist)
    if request.method == 'POST':
        user_answer = request.POST.get('name','')

        if user_answer == bot_action:

            messages.info(request, "Both players selected. It's a tie!")
            return redirect('Game')

        elif user_answer == "rock":
            if bot_action == "scissors":
                messages.info(request,"You Choose Rock and Computer Choose Scissors.. You win!")
                return redirect('Game')
               
            else:
               
                messages.info(request,"Computer Choose Paper! You lose.")
                return redirect('Game')

                

        elif user_answer == "paper":
            if bot_action == "rock":

                messages.info(request,"You Choose Paper and Computer Choose Rock.. You win!")
                return redirect('Game')
                
            else:
                
                messages.info(request,"Computer Choose Scissors! You lose.")
                return redirect('Game')
                

        elif user_answer == "scissors":
            if bot_action == "paper":
               
                messages.info(request,"You Choose Scissor and Computer Choose Paper.. You win!")
                return redirect('Game')
                
            else:
               
                messages.info(request,"Computer Choose Rock! You lose.")
                return redirect('Game')

    
                
    
    return render(request, 'game.html')