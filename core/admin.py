from django.contrib import admin

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'controle de emprestimo'
admin.site.site_title= 'Titulo HTML do site'

from core.models import Revista
from core.models import Amigo
from .models import Caixa
from core.models import Emprestimo
from core.models import Colecao


#class ColecaoAdmin(admin.ModelAdmin):
#    list_display = ('cod', 'nome')

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('numeroEdicao', 'ano')

class AmigoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nomeMae', 'telefone', 'grupoAmigo')
    search_fields = ('nome',)

class CaixaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'etiqueta', 'cor')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('dataEmprestimo', 'dataDevolucao')
    list_filter = ('dataEmprestimo', 'dataDevolucao')

admin.site.register(Colecao)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Caixa, CaixaAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
