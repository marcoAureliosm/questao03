from django.contrib import admin
from .models import *
from  datetime import *

class despesasAdmin(admin.ModelAdmin):
    list_display = ('data', 'formas_pagamento','vencimento','quitado','proximoVencimento')
    list_filter = ('data', 'formas_pagamento','quitado','vencimento')

    def proximoVencimento(self, obj):
        return  date.today()<=obj.data + timedelta(days=-2)
    proximoVencimento.short_description = "proximo do vencimento"
    proximoVencimento.boolean = True
admin.site.register(despesas,despesasAdmin)
# Register your models here.
