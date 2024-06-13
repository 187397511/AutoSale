from django.contrib import admin
from .models import Team
# Register your models here.

class team_admin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'designation')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter= ('designation', )

admin.site.register(Team, team_admin)
