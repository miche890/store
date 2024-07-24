from django.contrib import admin
from .models import Banners, PromotionalVideo


# Register your models here.
@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'highlight')


@admin.register(PromotionalVideo)
class PromotionalVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'active')
