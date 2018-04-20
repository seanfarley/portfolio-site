from django.contrib import admin
from .models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):

	class Media:
		js = (
			'/static/js/jquery-2.2.4.min.js',
			'/static/ckeditor/ckeditor.js',
			'/static/js/custom.js',
		)
		css = {
            'all': ('/static/css/custom.css',)
        }

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
