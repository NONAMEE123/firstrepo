from django import forms

from .models import signup
from .models import Document


class contactForm(forms.Form):
    fullname = forms.CharField()
    emai = forms.CharField()
    telephone = forms.CharField()



class signupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['email','fullname']
        #def clean_email(self):
            #email = self.cleaned_data.get('email')
            #email_base, provider = email.split("@")
            #domain, extension = provider.split(',')
            #if not extension == "gov":
                #raise forms.ValidationError("please enter .gov domain")

            #return email


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )



