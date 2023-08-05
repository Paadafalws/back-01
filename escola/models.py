from django.db import models


class TipoApolice(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class TipoVendaApolice(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Apolice(models.Model):
    descricao = models.CharField(max_length=200)
    tipo_apolice = models.ForeignKey(TipoApolice, on_delete=models.CASCADE)
    tipo_venda = models.ForeignKey(TipoVendaApolice, on_delete=models.CASCADE)
    arquivo = models.FileField(default="")
    
    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    nome = models.CharField(max_length=30,blank=True, default="")
    rg = models.CharField(max_length=9,blank=True, default="")
    cpf = models.CharField(max_length=11,blank=True, default="")
    data_nascimento = models.DateField(blank=True, default="")
    celular = models.CharField(max_length=11, default="")
    foto = models.FileField(blank=True, default="")
    apolices = models.ManyToManyField(Apolice)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M')
