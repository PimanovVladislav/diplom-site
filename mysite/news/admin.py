from django.contrib import admin
from .models import New,Tags

class NewAdmin(admin.ModelAdmin):
    list_display = ("id", "title" ,"likes","tags", "is_published","date_published")
    list_display_links = ("id", "title")
    search_fields = ("title","content")
    list_editable = ("is_published","likes")
    list_filter = ("is_published","tags" )

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_editable = ("name",)
admin.site.register(New,NewAdmin)
admin.site.register(Tags,TagsAdmin)
