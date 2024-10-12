from django.contrib import admin
from .models import Doacao
from .models import Doador

@admin.register(Doacao)

class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_material', 'quantidade', 'data_doacao', 'doador','produto')
admin.site.register(Doador)
