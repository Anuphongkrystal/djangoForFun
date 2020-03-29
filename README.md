##MODULE
 [+] pip install virtualenvwrapper-win <br>
 [+] pip install django<br>
 [+] pip install mysqlclient<br>
      - แก้ปัญหา 
##STEP
[+] create folder mkdir  <name>
 [+] mkvirtualenv <name> ชื่อสำหรับใช้ตั้ง env นั้นๆ <br>
    [+] workon <name> ถ้าต้องการเลือก envใหม <br>
    [+] deactivate <name> ออกจากการทำงาน env <br>

 [+]django-admin startproject <name> <br>
 [+]python manage.py runserver <br>
 [+]python manage.py startapp <name> <br>



##ENV
[+] beta

##STRUCTURE

###djangoforfun (MAIN):
  [+] manage.py ไฟล์สำหรับการสั่งรันต่างๆ ที่เกี่ยวข้อกับ django เช่น Run server <br>
  [+] __init__.py initial มีไว้เก็บ Python Package <br>
  [+] setting.py ไฟล์สำหรับการตั้งค่าตัวโปรเจค เช่น ตั้งค่าแอพ ,เวลา,ฐานข้อมูล<br>
  [+] urls.py ไฟล์ที่ใช้เก็บการ Routing ของ HTTP request หรือ เรียกอีกอย่างว่า url pattern<br>
  [+] wsgi.py  ไฟล์ที่ใช้เก็บข้อมูลโปรเจคสำหรับการ Deployment (Production)<br>

###blogs :
  [+] Desc : การทำงานจะทำเฉพาะแค่นี้เท่าไหนนั้น <br>
  [+] เปรียบเสมือน มีโปรเจคใหญ่และแอพย่อยข้างใน <br>

#MVT(MODEL-VIEW-TEMPLATE)
[+] Model คือส่วนที่เก็บ APPLICATION <br>
[+] VIEW สำหรับประมวลผลคำสั่งต่างๆ (เหมือน CONTROLLER) แล้วโยนไปแสดงผลตรงส่วน TEMPLATE<br>
[+] TEMPLATE คือ หน้าตา APPLICATION <br>
