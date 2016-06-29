from django.contrib import admin
import models

#admin.site.register(UserProfile)

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    readonly_fields = ['username', 'email', 'password']
