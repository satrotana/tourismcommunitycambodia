from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext

def home(request):
    return render(request,'index.html')

def about_nactec_national(request):
    return render(request,'community/national.html')

def about_nactec_city_town(request):
    return render(request,'community/city_town.html')

def documentations(request):
    return render(request,'documentations/doc.html')

def documentations_other(request):
    return render(request,'documentations/doc_other.html')

def news(request):
    return render(request,'post/news.html')

def news_details(request,id):
    return render(request,'post/news_details.html')

def contact(request):
    return render(request,'contacts/contacts.html')

def community(request):
    return render(request,'community/communitylist.html')

def translate(language):
    cur_langauge = get_language()
    try:
        activate(language)
        text = gettext(language)
    finally:
        activate(cur_langauge)
    return text