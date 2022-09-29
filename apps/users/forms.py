"""
Extending django admin forms
"""
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form for user model"""
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """Custom user creation form for user model"""
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
