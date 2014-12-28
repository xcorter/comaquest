from django.contrib import admin
from main.models import *




admin.site.register(Order)
admin.site.register(Time)
admin.site.register(Quest)
admin.site.register(Contact)
admin.site.register(QuestImage)
admin.site.register(About)


class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('admin_image',)
    list_display = ('admin_image',)
    fields = ('admin_image', 'image')

admin.site.register(Slider, SliderAdmin)