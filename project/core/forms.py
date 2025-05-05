from django import forms
from .models import Review, Book, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    # Optionally add validation to the username or email fields if needed
    

class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']  # Include bio and location for profile info

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none'}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Only allow the user to submit rating and content
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-3 border border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Write your review here...'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'w-full p-3 border border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-blue-500'})
        }
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'condition', 'image', 'categories', 'location']  # Fields to edit
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'categories': forms.CheckboxSelectMultiple(),  # For multiple categories selection
        }

