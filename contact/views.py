from django.shortcuts import render
from contact.models import WebPageOwnerInfo
from django.http import HttpResponse
from django.views import generic

class WebPageOwnerInfoView(generic.ListView):
    model = WebPageOwnerInfo

from django.shortcuts import get_object_or_404

def owners2(request):
    webPageOwnerInfo = get_object_or_404(WebPageOwnerInfo, pk=0)
    print(webPageOwnerInfo)
    return render(request, 'contact/templates/owner_info.html', context={'owner': webPageOwnerInfo})


def index(request):
    return HttpResponse("<h1>Welcome to the contact page</h1>")

def index2(request):
    return HttpResponse("Hello World2")


def owners(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    all_objects = WebPageOwnerInfo.objects.all()

    owner_name = all_objects[0].owner_name
    owner_twitter = all_objects[0].owner_twitter
    owner_description = all_objects[0].owner_description

    context = {
        'owner_name': owner_name,
        'owner_twitter': owner_twitter,
        'owner_description': owner_description,
    }

    # Render the HTML template index_catalog.html with the data in the context variable
    #return render(request, 'index_catalog.html', context=context)
    return render(request, 'index.html', context=context)

