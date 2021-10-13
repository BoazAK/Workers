from django.contrib import admin
from .models import Position, Workers

# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title']

class WorkersAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'work_code', 'mobile', 'position')
    list_filter = ['position']
    list_per_page = 100

admin.site.site_header = 'Enregistrement des employés'
admin.site.site_title = 'Enregistrement des employés'

admin.site.register(Position, PositionAdmin)
admin.site.register(Workers, WorkersAdmin)
