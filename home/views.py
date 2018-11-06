from django.shortcuts import render # HttpResponse

def home_view(request):
    if request.user.is_authenticated():  # oturum açılırsa
        context = {
            'isim': 'Lombakcan',
        }
    else:  # oturum açılmazsa
        context = {
            'isim': 'Misafir',
        }


    return render(request, 'home.html', context)