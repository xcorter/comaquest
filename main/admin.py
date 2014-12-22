from django.contrib import admin
from main.models import About, Slider


class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('admin_image',)
    list_display = ('admin_image',)
    fields = ('admin_image', 'image')


admin.site.register(About)
admin.site.register(Slider, SliderAdmin)