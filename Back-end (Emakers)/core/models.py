from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

class Pontuacao(models.Model):
    descricaoPontuacao = models.TextField('Descrição', max_length=255)
    pontosEquivalentes = models.IntegerField()

    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'

    def __str__(self):
        return self.descricaoPontuacao

class Usuario(models.Model):
    nomeUsuario = models.CharField('Nome', max_length=255)
    emailUsuario = models.CharField('Email', max_length=255)
    sexoUsuario = models.CharField('Sexo', max_length=1)
    pontuacoes = models.ForeignKey(Pontuacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeUsuario

class Login(models.Model):
    nomeUsuario = models.CharField('Usuário', max_length=100)
    senhaUsuario = models.CharField('Senha', max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Usuario_possui_pontuacao(models.Model):
    nomeUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pontuacaoUsuario = models.ForeignKey(Pontuacao, on_delete=models.PROTECT)
    comentarioPontuacao = models.TextField('Comentario', max_length=255)

class Ranking(models.Model):
    pontuacaoTotal = models.IntegerField(default=0)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, sexUser, scores, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an name')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            sexUser=sexUser,
            scores=scores,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, sexUser, password, scores=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
            sexUser=sexUser,
            scores=scores,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name='Name', max_length=100, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    sexUser = models.CharField(verbose_name='Sex', max_length=100)
    scores = models.ForeignKey(Pontuacao, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth', 'sexUser']

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
        return self.is_admin