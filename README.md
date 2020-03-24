##MODULE
 [+] pip install virtualenvwrapper-win <br>
 [+] pip install django

##STEP
 [+] mkvirtualenv <name> สำหรับการจำลอง
    [+] workon <name> ถ้าต้องการเลือก envใหม่

 [+]django-admin startproject <name>

 [+]python manage.py runserver  ทดสอบการใช้งาน

##STRUCTURE

[+] manage.py ไฟล์สำหรับการสั่งรันต่างๆ ที่เกี่ยวข้อกับ django เช่น Run server
[+] __init__.py initial มีไว้เก็บ Python Package
[+] setting.py ไฟล์สำหรับการตั้งค่าตัวโปรเจค เช่น ตั้งค่าแอพ ,เวลา,ฐานข้อมูล
[+] urls.py ไฟล์ที่ใช้เก็บการ Routing ของ HTTP request หรือ เรียกอีกอย่างว่า url pattern
[+] wsgi.py  ไฟล์ที่ใช้เก็บข้อมูลโปรเจคสำหรับการ Deployment (Production)
