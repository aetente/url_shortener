from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError
from urlshortener.models import UrlModel
from django.views.decorators.csrf import csrf_exempt

# i just didn't want to do forms to be quick


@csrf_exempt
def create_view(request):

    if request.method == 'GET':
        return HttpResponse("no get")
    elif request.method == 'POST':
        # get base url to print it on response
        str_host = request.get_host()
        url_entity = UrlModel()
        try:
            url_entity.original_url = request.POST["url"]

            # short url created on save
            short_url_ent = url_entity.save()
            short_url = short_url_ent.shortened_url

            return HttpResponse(str_host + "/s/" + short_url)
        except:
            return HttpResponseServerError("error create")
    # just in case
    return HttpResponseServerError("error request")


def redirect_view(request, shortened_url):

    try:
        # find the url
        the_url = UrlModel.objects.get(shortened_url=shortened_url)
        # count the click
        the_url.hits += 1
        # update the model
        the_url.save()
        # redirect to original url
        return HttpResponseRedirect(the_url.original_url)

    except:
        raise Http404('could not find the link')


def hit_link(request, shortened_url):

    try:
        # find the url
        the_url = UrlModel.objects.get(shortened_url=shortened_url)
        # count the click
        the_url.hits += 1
        # update the model
        the_url.save()
        # show the hit count
        return HttpResponse("times the link " + str(the_url.original_url) + " was hit: " + str(the_url.hits))

    except:
        raise Http404('could not find the link')
