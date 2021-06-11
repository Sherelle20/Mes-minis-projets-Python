from django.shortcuts import render, redirect, reverse
from .models import *
from django.db.models import F
from django.contrib.auth import authenticate, login as Dlogin, logout as Dlogout
from django.http import Http404


def home(request):

    ###charger les produits dans le home
    produits = Produit.objects.filter(poster = True).order_by("base_price")[:3]
    produits1 = Produit.objects.filter(poster = True).order_by("base_price")[3:]

    
    popular_product = Produit.objects.filter(buy_number__gte = 20)

    if request.method == "POST":
        price = request.POST.get('price')
        popular_product = Produit.objects.filter(buy_number__gte = 20 , base_price = price)

    produit_search = Produit.objects.all()[:3]
    
    var = False
    if not popular_product:
        var = False
    else:
        var = True
    
        
    

    context = {'popular_product':popular_product, 'produits':produits, 'produits1':produits1, 'produit_search':produit_search, 'var':var}
    
    return render(request, 'market/home.html', context)

    
    ###search
    #produit_search = Produit.objects.all()
    
    ##filter
    """
    ctxr = {}
    var = False
    if request.method == "POST":
        price = request.POST["price"]
        filter_product = Produit.objects.filter(base_price = price)
        var = True
        ctxr = {'filter_product':filter_product,'var':var}
        
        
    else:
        ctxr
    """

    


def learnmore(request, idp):

    produit = Produit.objects.get(pk = idp)
    context = {'produit': produit}

    return render(request, 'market/learnmore.html', context)

def register(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(email = email, password = password, name = name, phone = phone, address = address)
        Dlogin(request, user)
        return redirect('home')
    return render(request,'market/register.html')

def liker(request, id_p):
    "fonction pour enregistrer un like"
    produit = Produit.objects.get(pk = id_p)
    produit.like_number = F('like_number') + 1
    produit.save()

    return redirect(request.META['HTTP_REFERER'])

def produit(request):
    return render(request, 'market/produit.html')

def categorie(request):
    return render(request, 'market/categorie.html')

def about(request):
    return render(request, 'market/about.html')

def page_membre(request, email):

    ctx = {}
    user = User.objects.get(email = email)

    #Achat
    achats = Achat.objects.filter(client__email = email)
    produits = []
    for achat in achats:
        produits.append(achat.produits)

    ctx = {'user':user, 'produits':produits}
    return render(request, 'market/page_membre.html', ctx)


def login(request):
    print("entrer dans login")

    confirmed = False
    ctx = {}
    if request.method == 'POST':
        email = request.POST['email']
        #password = request.POST['password']

        #user = authenticate(request, email=email)
        try:
            user = User.objects.filter(email = email)
        except Exception:
            return Http404()
        
        
        if user:
        #if user is not None:
            #Dlogin(request, user)
                return redirect('page_membre', email)
        else:
            print("user is not authenticated")
        return redirect('login')
    else:
        ctx
    print("sortie de login")
    return render(request, 'market/login.html')







"""
def Login(request):
    return render(request, 'base/login.html')


def user_login(request):
    #'name','telephone','adress','email','password','sing_up_date'
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        telephone = request.POST.get('telephone')
        adress = request.POST.get('adress')
        email = request.POST.get('email')
        sing_up_date = request.POST.get('adress')
        user = authenticate(username=name, password=password, telephone=telephone, adress=adress, email=email, sing_up_date=sing_up_date)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'base/login.html', {})

def Login(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user.Client.name = form.cleaned_data.get('name')
        user.Client.password = form.cleaned_data.get('password')
        user.Client.email = form.cleaned_data.get('email')
        user.Client.telephone = form.cleaned_data.get('telephone')
        user.Client.adress= form.cleaned_data.get('adress')
        user.Client.sing_up_date = form.cleaned_data.get('sing_up_date')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'base/login.html', {'form': form})
"""