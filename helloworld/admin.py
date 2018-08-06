from django.contrib import admin
from . import models

# Register your models here.
class KlassAdmin(admin.ModelAdmin):
	list_display = ('name', 'note')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'klass', 'address')
	list_editable = ['klass']
	list_per_page = 5
	search_fields = ['name', 'klass__name']


admin.site.register(models.Klass, KlassAdmin)
admin.site.register(models.Student, StudentAdmin)
