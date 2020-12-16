from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Welcome to this fpl web page</h1>"
                        "<a href=../home/>Home</a>"
                        "<br>"
                        "<a href=../contact/>Contact</a>"
                        "<br>"
                        "<a href=../catalog/>Catalog</a>"
                        "<br>"
                        "<a href=../admin/>Admin</a>")
                        # to navigate into other pages in home
                        # -> home/further

def index2(request):

    context = {
        'test': 1,
    }
    return render(request, 'index_home.html', context=context)



