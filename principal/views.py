from django.shortcuts import render
from .models import User , Category,Favorite,Notification,Order,Product,PurchaseHistory,ShoppingCart

# Create your views here.
def IndexView(request):
    '''Esto es la pagina principal'''
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get(username='usuarioPrueba')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
    return render(request,"index.html",{"usuario":usuario})
    ###
    
    

def PerfilView(request):
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get(username='usuarioPrueba')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
    return render(request,"perfil.html",{"usuario":usuario})
def OfertarMaterialView(request):
    try:
        # Busca al usuario con el nombre de usuario "usuarioPrueba"
        usuario = User.objects.get(username='usuarioPrueba')# Busca al usuario por su username
    except User.DoesNotExist:
        usuario = None  # Si no existe, asigna None
    return render(request,"ofertarMaterial.html",{"usuario":usuario})
