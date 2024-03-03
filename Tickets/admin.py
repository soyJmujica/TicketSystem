from django.contrib import admin
from .models import CreateOffer, CreateAddendum, CreateListing, CreateMLSsheet, CreateSearch, CreateDotloop
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	"""docstring for TaskAdmin"""
	readonly_fields = ("created",)
		

admin.site.register(CreateOffer, TaskAdmin)
admin.site.register(CreateAddendum, TaskAdmin)
admin.site.register(CreateListing, TaskAdmin)
admin.site.register(CreateMLSsheet, TaskAdmin)
admin.site.register(CreateSearch, TaskAdmin)
admin.site.register(CreateDotloop, TaskAdmin)