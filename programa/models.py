# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models

class Acesso(models.Model):
    login = models.CharField(max_length=20L)
    senha = models.CharField(max_length=20L)
    class Meta:
        db_table = 'acesso'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True, db_column='ID_EMPRESA') # Field name made lowercase.
    nome = models.CharField(max_length=50L, db_column='NOME') # Field name made lowercase.
    endereco = models.CharField(max_length=50L, db_column='ENDERECO') # Field name made lowercase.
    bairro = models.CharField(max_length=50L, db_column='BAIRRO') # Field name made lowercase.
    cidade = models.CharField(max_length=50L, db_column='CIDADE') # Field name made lowercase.
    estado = models.CharField(max_length=2L, db_column='ESTADO') # Field name made lowercase.
    telefone = models.CharField(max_length=15L, db_column='TELEFONE') # Field name made lowercase.
    email = models.CharField(max_length=50L, db_column='EMAIL') # Field name made lowercase.
    cep = models.IntegerField(db_column='CEP') # Field name made lowercase.
    site = models.CharField(max_length=50L, db_column='SITE') # Field name made lowercase.
    creci = models.CharField(max_length=10L, db_column='CRECI') # Field name made lowercase.
    popup = models.BooleanField(db_column='POPUP') # Field name made lowercase.
    logo = models.CharField(max_length=50L, db_column='LOGO') # Field name made lowercase.
    analytics = models.CharField(max_length=50L, db_column='ANALYTICS') # Field name made lowercase.
    class Meta:
        db_table = 'empresa'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, db_column='ID_USUARIO') # Field name made lowercase.
    id_empresa = models.IntegerField(db_column='ID_EMPRESA') # Field name made lowercase.
    nome = models.CharField(max_length=300L, db_column='NOME') # Field name made lowercase.
    senha = models.CharField(max_length=300L, db_column='SENHA') # Field name made lowercase.
    email = models.CharField(max_length=80L, unique=True, db_column='EMAIL') # Field name made lowercase.
    endereco = models.CharField(max_length=50L, db_column='ENDERECO') # Field name made lowercase.
    telefone = models.CharField(max_length=13L, db_column='TELEFONE') # Field name made lowercase.
    telefone2 = models.CharField(max_length=13L, db_column='TELEFONE2') # Field name made lowercase.
    telefone3 = models.CharField(max_length=13L, db_column='TELEFONE3') # Field name made lowercase.
    ativo = models.CharField(max_length=3L, db_column='ATIVO') # Field name made lowercase.
    tipo = models.CharField(max_length=3L, db_column='TIPO') # Field name made lowercase.
    class Meta:
        db_table = 'usuario'

class Imovel(models.Model):
    id_imovel = models.IntegerField(primary_key=True, db_column='ID_IMOVEL') # Field name made lowercase.
    cod_imovel = models.IntegerField(db_column='COD_IMOVEL') # Field name made lowercase.
    id_usuario = models.ForeignKey(Usuario, related_name = 'idempresa_usuario',db_column='ID_USUARIO') # Field name made lowercase.
    id_empresa = models.ForeignKey(Empresa, related_name = 'idempresa_imovel', db_column='ID_EMPRESA') # Field name made lowercase.
    finalidade = models.CharField(max_length=300L, db_column='FINALIDADE') # Field name made lowercase.
    tipo = models.CharField(max_length=300L, db_column='TIPO') # Field name made lowercase.
    endereco = models.CharField(max_length=300L, db_column='ENDERECO') # Field name made lowercase.
    numero = models.IntegerField(db_column='NUMERO') # Field name made lowercase.
    bairro = models.CharField(max_length=300L, db_column='BAIRRO') # Field name made lowercase.
    cidade = models.CharField(max_length=300L, db_column='CIDADE') # Field name made lowercase.
    estado = models.CharField(max_length=2L, db_column='ESTADO') # Field name made lowercase.
    valor_real = models.DecimalField(decimal_places=2, max_digits=12, db_column='VALOR_REAL') # Field name made lowercase.
    valor = models.DecimalField(decimal_places=2, max_digits=12, db_column='VALOR') # Field name made lowercase.
    forma_pgto = models.CharField(max_length=255L, db_column='FORMA_PGTO', blank=True) # Field name made lowercase.
    dormitorios = models.IntegerField(db_column='DORMITORIOS') # Field name made lowercase.
    suite = models.IntegerField(db_column='SUITE') # Field name made lowercase.
    banheiros = models.IntegerField(db_column='BANHEIROS') # Field name made lowercase.
    garagem = models.IntegerField(db_column='GARAGEM') # Field name made lowercase.
    idade = models.IntegerField(db_column='IDADE') # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True) # Field name made lowercase.
    condicao = models.CharField(max_length=300L, db_column='CONDICAO') # Field name made lowercase.
    data = models.DateField(db_column='DATA') # Field name made lowercase.
    chaves = models.CharField(max_length=300L, db_column='CHAVES', blank=True) # Field name made lowercase.
    proprietario = models.CharField(max_length=300L, db_column='PROPRIETARIO') # Field name made lowercase.
    proprietario_tel = models.CharField(max_length=300L, db_column='PROPRIETARIO_TEL') # Field name made lowercase.
    proprietario_end = models.CharField(max_length=300L, db_column='PROPRIETARIO_END') # Field name made lowercase.
    documentos = models.CharField(max_length=300L, db_column='DOCUMENTOS') # Field name made lowercase.
    area_terreno = models.FloatField(db_column='AREA_TERRENO') # Field name made lowercase.
    area_construida = models.FloatField(null=True, db_column='AREA_CONSTRUIDA', blank=True) # Field name made lowercase.
    anuncio = models.CharField(max_length=3L, db_column='ANUNCIO') # Field name made lowercase.

    def __unicode__(self):
        return unicode(self.id_imovel)

    """
        Método que retorna a foto da fachada

        return string foto
    """
    #def photo(self):
    #    foto = Fotos.objects.filter(id_imovel=self.id_imovel, id_empresa=self.id_empresa.id_empresa, fachada=1, foto__contains='_1.')[:1]
    #    for f in foto:
    #        foto = f.foto
    #    return foto

    def fotos(self):
        fotos = Fotos.objects.filter(id_empresa=self.id_empresa, id_imovel=self.id_imovel, fachada=1) #retirei: fachada=1
        return fotos
    
    class Meta:
        db_table = 'imovel'

class Fotos(models.Model):
    id_foto = models.IntegerField(primary_key=True, db_column='ID_FOTO') # Field name made lowercase.
    id_imovel = models.ForeignKey(Imovel, related_name = 'imovel', db_column='ID_IMOVEL') # Field name made lowercase.
    cod_imovel = models.ForeignKey(Imovel, related_name = 'codimovel_fotos', db_column='COD_IMOVEL') # Field name made lowercase.
    id_empresa = models.ForeignKey(Empresa, related_name = 'idempresa_fotos', db_column='ID_EMPRESA') # Field name made lowercase.
    foto = models.CharField(max_length=300L, db_column='FOTO') # Field name made lowercase.
    descricao = models.CharField(max_length=300L, db_column='DESCRICAO', blank=True) # Field name made lowercase.
    fachada = models.IntegerField(null=True, db_column='FACHADA', blank=True) # Field name made lowercase.
    id_imovel_antigo = models.IntegerField(null=True, db_column='ID_IMOVEL_ANTIGO', blank=True) # Field name made lowercase.
    cod_imovel_antigo = models.IntegerField(null=True, db_column='COD_IMOVEL_ANTIGO', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'fotos'
