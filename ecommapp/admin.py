from django.contrib import admin
from .models import cupon, estado_pedido, categoria, cliente, producto, pedido, detalle_pedido

# Register your models here.
class cuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'descuento' )

admin.site.register(cupon, cuponAdmin)

class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria','igv','imagen','precio', 'descuento' )

admin.site.register(producto, productoAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion' )

admin.site.register(categoria, categoriaAdmin)

class clienteAdmin(admin.ModelAdmin):
    #list_display = ('username', 'nombre', 'email', 'password' )
    list_display = ('nombre', 'email', 'password' )

admin.site.register(cliente, clienteAdmin)

class pedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'subtotal', 'igv', 'total', 'cliente', 'estado', 'cupon' )

admin.site.register(pedido, pedidoAdmin)

class detallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'subtotal' )

admin.site.register(detalle_pedido, detallePedidoAdmin)

class estadoPedidoAdmin(admin.ModelAdmin):
    field = ('descripcion' )

admin.site.register(estado_pedido, estadoPedidoAdmin)