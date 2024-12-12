from django.contrib import admin
from .models import Images,Contact,ImageUpload
# Register your models here.

admin.site.register(Images)
admin.site.register(Contact)
admin.site.register(ImageUpload)