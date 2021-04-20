from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanici adi')
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label='Kullanici adi')
    #Yeni ekeme BASLANGIC
    first_name = forms.CharField(max_length=50, label='Adi')
    last_name = forms.CharField(max_length=50, label='Soyadi')
    email = forms.CharField(max_length=50, label='E-Mail')
    #Yeni ekeme BITIS
    password = forms.CharField(
        max_length=20, label='Parola', widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label='Parolayi Dogrula', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        #Yeni ekeme BASLANGIC
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        #Yeni ekeme BITIS
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar eslesmiyor')

        values = {

            'username': username,
            'first_name': first_name,  # Yeni ekeme
            'last_name': last_name,  # Yeni ekeme
            'email': email,  # Yeni ekeme
            'password': password
        }
        return values
