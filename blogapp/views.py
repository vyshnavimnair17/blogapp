from django.shortcuts import render, redirect
from .models import Category, Current, Review, Favourite, Tbr


# Create your views here.

def homepage(request):
    profile = Category.objects.all()
    return render(request, 'homepage.html', {"data": profile})


def add_blog(request):
    if request.method == 'POST':
        print(request.POST)
        item = Category()
        item.title = request.POST.get("title")
        item.author = request.POST.get("author")
        item.synopsis = request.POST.get("synopsis")
        item.description = request.POST.get("description")
        item.image = request.POST.get("image")
        item.save()
        return redirect('/homepage')
    return render(request, 'create_blog.html')


def current(request, cur_id):
    read = Current.objects.get(id=cur_id)
    return render(request, 'current_read.html', {"data": read})


def review(request):
    bookrev = Category.objects.all()
    return render(request, 'book_review.html', {"data": bookrev})


def book_detail(request, cat_id):
    book = Category.objects.get(cat_id=cat_id)
    return render(request, 'description.html', {"data": book})


def tbr(request):
    list = Tbr.objects.all()
    return render(request, 'tbr_list.html', {"data": list})


def favourite(request, cat_id):
    favourite = Category.objects.get(cat_id=cat_id)
    year_obj = Favourite(favourite=favourite)
    year_obj.save()
    return render(request, 'favourites.html', {"data": year_obj})


