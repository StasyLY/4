from django.contrib import admin
from .models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','description', 'price', 'created_date','auction', 'updated_date']

    list_filter = ['auction', 'created_at', 'updated_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Торг не уместен')
    def make_auction_as_false(self, request,queryset):
        queryset.update(auction=False)
    @admin.action(description='Торг возможен')
    def make_auction_as_true(self, request,queryset):
        queryset.update(auction=True)
    fieldsets = (('Общее', {'fields':('title','description'),}),('Финансы', {'fields':('price','auction'), 'classes':['collapse']}))   



admin.site.register(Advertisement, AdvertisementAdmin)




# Register your models here.
