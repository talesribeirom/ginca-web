from django import forms
from .models import	User

# Formulário que valida e salva a senha do usuário
class User_Creation_Form(forms.ModelForm):
    
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação da senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'sex')

    def clean_password2(self):
        # Confirma se as senhas conferem
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem")
            
        return password2

    def save(self, commit=True):
        # Criptografa a senha como hash e salva no banco
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user

# Formulário para alteração dos dados do usuário
class User_Change_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'password')

    def save(self, commit=True):
        # Criptografa a senha como hash e salva no banco
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            
        return user