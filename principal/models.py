from django.db import models
from django.utils import timezone

# Create your models here.
# aqui creo mi modelo de la base de datos

class User(models.Model):
    username = models.CharField(max_length=150, unique=True,null= False ,blank=False)
    numeroCelular = models.CharField(max_length=15,default='00000000')  # Número de teléfono (ajusta el tamaño según sea necesario)
    imagenPerfil = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Ruta para la imagen de perfil
    email = models.EmailField(unique=True,null= False ,blank=False)
    password = models.CharField(max_length=128,null= False ,blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    account_status = models.CharField(max_length=20, default='active')
    role = models.CharField(max_length=20, default='user')

    class Meta:
        db_table = "Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    province = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    product_status = models.CharField(max_length=50, blank=True, null=True)
    publication_status = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    class Meta:
        db_table = "Productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Compras"
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Carritos"
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Favoritos"
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return self.name

class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "Historiales"
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "Notificaciones"
        verbose_name = "Notificacione"
        verbose_name_plural = "Notificaciones"

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "ProductImages"
        verbose_name = "Imagen del Producto"
        verbose_name_plural = "Imágenes del Producto"

    def __str__(self):
        return f"Imagen de {self.product.name}"
