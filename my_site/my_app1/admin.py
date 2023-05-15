from django.contrib import admin
from .models import Position
from .models import Categories
# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_update', 'photo', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('published',)  # possibility to edit in admin-panel
    list_filter = ('published', 'time_create')  # additional panel with filters in admin-panel
    prepopulated_fields = {'slug_for_position': ("title",)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories_name')
    list_display_links = ('id', 'categories_name')
    prepopulated_fields = {"slug_for_categories": ('categories_name',)}


admin.site.register(Position, PositionAdmin)
admin.site.register(Categories, CategoriesAdmin)

# admin.site.register(Position)
# admin.site.register(Categories)