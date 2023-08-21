from django.contrib import admin
from .models import Post,Message

class MessageAdmin(admin.ModelAdmin):
	model=Message
	list_display=['name','email','readed']

admin.site.register(Post)
admin.site.register(Message,MessageAdmin)
