from django.contrib import admin
from .models import Category ,Favorite,Notification,Order,Product,PurchaseHistory,ShoppingCart, User,ProductImage

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude = ('user_id',)
    fields=["username","numeroCelular","imagenPerfil","email","password","created_at","account_status","role"]
    list_display =["username","email","created_at"] #lo que se va mostrar
admin.site.register(User,UserAdmin)#para registrar 1 forma

@admin.register(Category)#forma para registrar 2
class CategoriaAdmin(admin.ModelAdmin):#lo que se puede editar
    fields=["name","description"]
    list_display =["name"]

@admin.register(Product)
class ProductoAdmin(admin.ModelAdmin):
    fields=["user","name","description","price","created_at","province","address","product_status","publication_status","category","image"]
    list_display =["user","name","price","created_at"]

@admin.register(Order)
class OrdenAdmin(admin.ModelAdmin):
    fields=["buyer","product","total_price","order_date"]
    list_display =["total_price","order_date"]

@admin.register(ShoppingCart)
class CarritoAdmin(admin.ModelAdmin):
    fields=["user","product","added_at"]
    list_display =["product","added_at"]

@admin.register(Favorite)
class FavoritoAdmin(admin.ModelAdmin):
    fields=["user","product","favorited_at"]
    list_display =["product","favorited_at","user"]

@admin.register(PurchaseHistory)
class HistorialAdmin(admin.ModelAdmin):
    fields=["user","product","purchase_date","total_price"]
    list_display =["user","product","total_price"]

@admin.register(Notification)
class NotificacionAdmin(admin.ModelAdmin):
    fields=["user","message","created_at","is_read"]
    list_display =["user","message","is_read"]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    fields=["product","image","created_at"]
    list_display =["created_at"]