from django.contrib import admin
from .models import Post #เข้าไปที่  models.py และไปเอา class Post()
# Register your models here.

# กำหนดตัว Model ที่เราสร้างขึ้นให้ Admin มองเห็นและจัดการได้
admin.site.register(Post)
