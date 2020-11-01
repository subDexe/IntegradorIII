from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from oficina.models import Oficina


class FuncionarioManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, cpf, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Funcionários devem ter um email cadastrado'))
        if not cpf:
            raise ValueError(_('Funcionários devem ter um cpf cadastrado'))
        email = self.normalize_email(email)
        user = self.model(email=email, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, password, oficina=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        if not oficina:
            superuseroficina = Oficina(cnpj="oficinasuperuser", nomeFantasia="padron", razaoSocial="nordap", cep="3", telefone="42", email="offfina@offfina.com")
            superuseroficina.save()

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        return self.create_user(email, cpf, password, oficina=superuseroficina, **extra_fields)

class Funcionario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=60)
    nome = models.TextField(max_length=35)
    cep = models.TextField(blank=True, null=True)
    cpf = models.TextField(unique=True, primary_key=True)
    dataNascimento = models.DateTimeField(null = True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    oficina = models.ForeignKey(Oficina, default=None, blank=True, null=True, on_delete=models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf']

    objects = FuncionarioManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
