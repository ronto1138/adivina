from django import forms
from usrcontrol.models import User

class NewUserForm(forms.ModelForm):
    #here the validations should be
    class Meta():
        model = User
        fields = '__all__'