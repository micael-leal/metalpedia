from django.contrib import admin
from .models import Band,News
# Register your models here.


class YourModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(YourModelAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['notes'].widget.attrs['style'] = 'height: 200em;'
        return form
    
admin.site.register(Band,YourModelAdmin)
admin.site.register(News)