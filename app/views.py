from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
# Create your views here.
def Home(request):
    return render(request, "app/home.html")

def Register(request):
    return render(request, "app/registration.html")

def add(request):
    return render(request, "app/add.html")

def Registration(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST.get('confirm_password')

        if password == cpassword:
            new_data_created = User.objects.create(
                username=username,
                first_name = name,
                email = email,
            )
            new_data_created.set_password(password)
            new_data_created.save()
            return redirect("login")
        else:
            return render(request, "app/registration.html")
    return HttpResponse("error")

def Login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("show_book")
            else:
                pass
        return render(request, "app/login.html")
    
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        genre = request.POST.get('genre')
        price = request.POST.get('price')

        book = Book.objects.create(title=title, author=author, isbn=isbn, genre=genre, price=price, user=request.user)
        
        return redirect("show_book")
    else:
        return render(request, 'app/add.html')

def book_list(request):
    queryset = Book.objects.all()
    name = request.GET.get('search')

    if name:
        queryset = queryset.filter(title__icontains=name) | queryset.filter(author__icontains=name)

    return render(request, 'app/home.html', {'queryset': queryset, 'name': name})

def updated(request, pk):
    updated_data = get_object_or_404(Book, pk=pk)
    return render(request, "app/update.html", {"updated_data": updated_data})

def updated_book(request, pk):
    updated_data = get_object_or_404(Book, pk=pk)
    updated_data.title = request.POST.get("title")
    updated_data.author = request.POST.get("author")
    updated_data.isbn = request.POST.get("author")
    updated_data.genre = request.POST.get("genre")
    updated_data.price = request.POST.get("price")
    updated_data.save()
    return redirect("show_data")

def Delete_data(request, pk):
    data = get_object_or_404(Book, pk=pk)
    data.delete()
    return redirect("show_book")

def signout(request):
    if User.is_authenticated:
        logout(request)
        return redirect("login")
    return