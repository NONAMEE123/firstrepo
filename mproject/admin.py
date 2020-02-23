from django.contrib import admin
# Register your models here.

from .models import signup

from .form import signupform


class signupadmin(admin.ModelAdmin):
    list_display = ["__str__","fullname","telephone"]
    form = signupform
    
    #class Meta:
        #model = signup

#integration with admin
admin.site.register(signup,signupadmin)
