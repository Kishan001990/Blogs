from django.contrib import admin
from .models import Category,Post

# Register your models here.


#for configuration of Category Admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_tag')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js', 'js/script.js',)


    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)