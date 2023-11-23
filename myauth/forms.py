from django.forms import ModelForm
from myauth.models import NewUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django import forms
# from PIL import Image


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password1', 'password2', )
      

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
 

class AccountVerificationForm(ModelForm):
	id = forms.IntegerField(min_value=1)
	
	class Meta:
		model = NewUser
		fields = ('is_active', 'id' )
      

class TutorRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password1', 'password2', )
        # widgets = {
        #     'country': forms.SelectMultiple(attrs={'class': 'input-text', 'autofocus': True}),
        #     }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
 
class TutorAccRegistrationForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', ) #'image' )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['image'].widget.attrs.update({'placeholder': 'Enter your image'})
        self.fields['bio'].widget.attrs.update({'placeholder': 'Enter your bio'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AccountAuthenticationForm(UserChangeForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = NewUser
		fields = ('email', 'password')
       
        

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})
		self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
		
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})
 
   
    
                 
    

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = NewUser
		fields = ['country', 'email', 'username', 'first_name', 'last_name', 'phone',  ]

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = NewUser.objects.exclude(pk=self.instance.pk).get(email=email)
		except NewUser.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = NewUser.objects.exclude(pk=self.instance.pk).get(username=username)
		except NewUser.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
		self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
		
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		fields = ('bio',   'facebook_link','instagram_link','twitter_link','linkedin_link',)
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['image'].widget.attrs.update({'placeholder': 'Enter your image'})
		self.fields['bio'].widget.attrs.update({'placeholder': 'Enter your bio'})

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class ProfilePicUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		fields = ('bio',)
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['image'].widget.attrs.update({'placeholder': 'Enter your image'})

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})