from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
import uuid
    
    
class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError("Users must have a telephone")
        user = self.model(
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class Type(models.Model):
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=uuid.uuid5(uuid.uuid4(), name="mader_user")
    )
    created_at = models.DateTimeField(
        verbose_name="data de criação",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="data de atualização",
        auto_now=True
    )
    name = models.CharField(
        verbose_name="nome",
        max_length=256
    )
    permission = models.JSONField(
        verbose_name="lista de permissões" #{"app": "permission(R/W)"}
    )


class User(AbstractBaseUser):
    name = models.CharField(
        verbose_name="name",
        max_length=256
    )
    phone = models.CharField(
        verbose_name="telefone ou whatsapp",
        max_length=11,
        unique=True
    )
    type = models.ForeignKey(
        to="user.Type",
        on_delete=models.CASCADE,
        verbose_name="tipo",
        related_name="+",
        editable=True,
        null=True,
        blank=True
    )
    store = models.ForeignKey(
        to="store.Store",
        on_delete=models.CASCADE,
        verbose_name="loja",
        related_name="+",
        null=True,
        blank=True,
        editable=True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    
    @property
    def is_staff(self):
        return self.staff
    
    
    @property
    def is_admin(self):
        return self.admin
