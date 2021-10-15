from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .ubicacion import Ubicacion


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    idUsuario = models.BigAutoField(primary_key=True)
    correo = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=256)
    tipoDocumento = models.CharField(max_length=30)
    numeroDocumento = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    fechaNacimiento = models.DateField(null=True)
    telefono = models.BigIntegerField(null=True)
    ubicacion = models.ForeignKey(
        Ubicacion, related_name='usuario', on_delete=models.CASCADE, null=True, blank=True, default=None)
    fotoPerfil = models.URLField(null=True)
    administrador = models.BooleanField(default=False)
    codigo = models.BigIntegerField(unique=True, null=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'correo'
