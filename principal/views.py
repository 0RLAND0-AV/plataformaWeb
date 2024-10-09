from django.shortcuts import render
from .models import User , Category,Favorite,Notification,Order,Product,PurchaseHistory,ShoppingCart
from django.contrib import messages



# Create your views here.
def IndexView(request):
    '''Esto es la pagina principal'''
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get( user_id ='7df58b9d71f346ceac7174bc2a4b13d5')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
        
    productos = Product.objects.all() #obtengo todos los productos
    return render(request,"index.html",{"usuario":usuario, "productos": productos})
    ###
    
    

def PerfilView(request):
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get(user_id ='7df58b9d71f346ceac7174bc2a4b13d5')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
    return render(request,"perfil.html",{"usuario":usuario})
def OfertarMaterialView(request):
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get(user_id ='7df58b9d71f346ceac7174bc2a4b13d5')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
    return render(request,"ofertarMaterial.html",{"usuario":usuario})

