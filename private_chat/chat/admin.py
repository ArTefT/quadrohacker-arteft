from django.contrib import admin
import models

@admin.register(models.UserMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['autor', 'date_message']
    
    readonly_fields = ['autor']
#admin.site.register(models.UserMessage)
