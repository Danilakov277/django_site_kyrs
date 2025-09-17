from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.utils.html import strip_tags
from django.core.validators import RegexValidator

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=66,
                              widget=forms.EmailInput(attrs={'class': 'input-register form-control','placeholder': 'Your email'}))
    first_name = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your first name'}))
    last_name = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your last name'}))
    password1 = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'input-register form-control',
            'placeholder': 'Your password'
        })
    )
    password2 = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'input-register form-control',
            'placeholder': 'Confirm your password'
        })
    )
    is_trener = forms.BooleanField(required=False, 
                                   label='I am trener',
                                   widget=forms.CheckboxInput(attrs={'class':'checbox-input-register'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','password1', 'password2','is_trener')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
    def save(self,comit=True):
        user = super().save(commit=False)
        user.username = None
        user.is_trener = self.cleaned_data['is_trener']
        if comit:
            user.save()
        return user


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email',widget=forms.TextInput(attrs={'autofocus':True,'class':'input-register form-control','placeholder':'Your email'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autofocus':True,'class':'input-register form-control','placeholder':'Your password'}))
    

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(self.request, username = email, password=password)
            if(self.user_cache is None):
                raise forms.ValidationError('Invalid email or password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('this accaunt is inactive.')
        return self.cleaned_data


class CustomUserUpdatedForm(forms.ModelForm):
    phone = forms.CharField(required=False,
                            validators=[RegexValidator(r'^\+?1?\d{9,15}$',"Enter a valid phone number.")],
                            widget=forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your phone number'}))
    first_name = forms.CharField(required=True,
                                 max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your first name'}))
    last_name = forms.CharField(required=True,
                                 max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your last name'}))
    email = forms.EmailField(required=False,
                                 widget=forms.EmailInput(attrs={'class': 'input-register form-control','placeholder': 'Your email'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone')
        widgets = {
            'email':forms.EmailInput(attrs={'class': 'input-register form-control','placeholder': 'Your email'}),
            'first_name':forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your first name'}),
            'last_name':forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your last name'}),
            'phone':forms.TextInput(attrs={'class': 'input-register form-control','placeholder': 'Your phone number'}),
            }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('email'):
            cleaned_data['email'] = self.instance.email
            for field in['phone']:
                if cleaned_data.get(field):
                    cleaned_data[field] = strip_tags(cleaned_data[field])
            return cleaned_data 
