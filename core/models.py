from django.db import models
#import datetime
from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"

class Colecao(models.Model):
    # cod = models.IntegerField('Codigo', default=0)
    nome = models.CharField('Nome', max_length=50)


    class Meta:
        verbose_name_plural = 'Coleções'
        verbose_name = 'Coleção'

    def __str__(self):
        return '{}'.format(
            self.nome,
        )

class Caixa(models.Model):
    numero = models.IntegerField('Numero da caixa', default=0)
    etiqueta = models.CharField('Etiqueta', max_length=50)
    cor = models.CharField('Cor', max_length=50)

    class Meta:
        verbose_name_plural = 'Caixas'
        verbose_name = 'Caixa'

    def __str__(self):
        return '{}'.format(
            self.cor,
        )

class Revista(models.Model):
    numeroEdicao = models.IntegerField('Numero de edição', default=0)
    ano = models.IntegerField('Ano', default=0)
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Revistas'
        verbose_name = 'Revista'

    def __str__(self):
        return '{}'.format(
            self.numeroEdicao,
        )



class Amigo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    nomeMae = models.CharField('Nome da mãe', max_length=100)
    telefone = models.CharField('Telefone', max_length=50)
    GrupoAmigo_choices = (
        ('Prédio', 'Prédio'),
        ('Escola', 'Escola'),
    )
    grupoAmigo = models.CharField('Grupo de amigo', max_length=50, choices=GrupoAmigo_choices)

    class Meta:
        verbose_name_plural = 'Amigos'
        verbose_name = 'Amigo'


class Emprestimo(models.Model):
    dataEmprestimo = models.DateField('Data do emprestimo')
    dataDevolucao = models.DateField('Data da devolução')

    class Meta:
        verbose_name_plural = 'Empréstimos'
        verbose_name = 'Empréstimo'