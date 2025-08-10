
from django.template import loader
from django.http import HttpResponse
from .models import Members


# Create your views here.



def members(request):
    members_list = Members.objects.all()
    template = loader.get_template('member_list.html')
    context = {
        "all_members": members_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    member_detail = Members.objects.get(id=id)
    template = loader.get_template("member_detail.html")

    context = {
        "member_detail": member_detail
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")

    return HttpResponse(template.render())