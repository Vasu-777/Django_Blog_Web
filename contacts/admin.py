from django.contrib import admin
from .models import Subscriber,Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email')
    list_display_links=('name', 'email')
admin.site.register(Contact,ContactAdmin)
admin.site.register(Subscriber)
