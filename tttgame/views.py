from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.


def index(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        char_choice = request.POST.get('char_choice')
        return redirect('/play/%s?&choice=%s'
                        % (room_code, char_choice))
    return render(request, 'index.html', {})


def game(request, room_code):
    choice = request.GET.get('choice')
    if choice not in ['X', 'O']:
        return Http404("[-] Your Choice Does Not Exist!", "[+] Choice Should Be 'X' Or 'O'.")
    context = {
        'char_choice': choice,
        'room_code': room_code
    }
    return render(request, 'game.html', context)
