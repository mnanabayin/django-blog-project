from django.contrib import admin

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
	def body_first_60(self):
		return self.body[:60]

class Comment(models.Model):
	body = models.TextField()
	author = models.CharField(max_length=60)  
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	post = models.ForeignKey(Post,related_name='comments')

	#def __unicode__(self):
	#	return self.author

	def body_first_60(self):
		return self.body[:60]



class CommentInline(admin.TabularInline):
	model = Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'updated')
	search_fields = ('title','body')
	list_filter = ('created','updated')
	inlines = [CommentInline]


class CommentAdmin(admin.ModelAdmin):
	
	list_display = ('post', 'author','body_first_60','created','updated')
	list_filter = ('created','author')
	


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register(CommentInline,PostAdmin)
"""
admin.site.register(CommentInline)
admin.site.register(PostAdmin)
admin.site.register(CommentAdmin)
"""
