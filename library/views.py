from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib import messages
from .models import Book, PremiumBook, User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request, 'index.html')   


def books(request):
    academic_books = Book.objects.filter(academic_books=True)
    selfdev_books = Book.objects.filter(selfdev_books=True)
    biography_books = Book.objects.filter(biography_books=True)
    return render(request, 'freebooks.html',{'academic_books': academic_books, 'selfdev_books' : selfdev_books, 'biography_books' : biography_books})

@login_required()
def jbooks(request):
    junior_books = PremiumBook.objects.filter(junior_books=True)
    
    return render(request, 'jbooks.html',{'junior_books': junior_books, })

@login_required()
def sbooks(request):
    senior_books = PremiumBook.objects.filter(senior_books=True)
    return render(request, 'sbooks.html',{'senior_books': senior_books, })

@login_required()
def lbooks(request):
    lower_books = PremiumBook.objects.filter(lower_books=True)
    
    return render(request, 'lbooks.html',{'lower_books': lower_books, })


def bsearched(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        bsearched = Book.objects.filter(title__contains = search_query)
        return render(request, 'booksearched.html',{'search_query':search_query, 'bsearched': bsearched } )
    else:
        return render(request, 'booksearched.html', {})
@login_required()
def psearched(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        psearched = PremiumBook.objects.filter(title__contains = search_query)
        return render(request, 'pbooksearched.html',{'search_query':search_query, 'psearched': psearched } )
    else:
        return render(request, 'pbooksearched.html', {})
    
def totalbooks(request):
    books= Book.objects.all
    bcount= len(books)
    
    return render(request, 'freebooks.html', bcount)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        user = auth.authenticate( username= username, password = password )

        if user is not None:
            auth.login(request,user)
            return redirect ('authorisation')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required()
def authorisation(request):
    if request.method =='POST':
        usertype = request.POST['usertype']
        if usertype == ('junior'):
            return redirect ('junior')
        if usertype == ('senior'):
            return redirect ('senior')
        if usertype == ('lower'):
            return redirect ('lower')
        
    else:    
        return render(request, 'authorisation.html') 
    
@login_required()
def junior(request):
    
    return render(request,'junior.html')
@login_required()
def senior(request):

    return render(request, 'senior.html')  
@login_required()
def lower(request):
    return render(request, 'lower.html')  