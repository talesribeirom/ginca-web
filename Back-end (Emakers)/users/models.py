from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    PermissionsMixin
)


class User_Manager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Usuários precisam de um nome')

        if not email:
            raise ValueError('Usuários precisam de um email')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Nome', max_length=100, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    is_active = models.BooleanField(default=True)
    
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
    	(MALE, 'Masculino'),
    	(FEMALE, 'Feminino'),
    ]
    sex = models.CharField(verbose_name='Sexo', max_length=1, choices=SEX_CHOICES, default=MALE)
    
    objects = User_Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    class Meta:
        verbose_name='Usuário'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
