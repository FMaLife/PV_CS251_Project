venv\Scripts\activate
python manage.py runserver
http://127.0.0.1:8000/admin/

# README Setup Guide

คู่มือนี้อธิบายขั้นตอนสำหรับเพื่อนในทีมตั้งแต่ clone โปรเจกต์, ติดตั้ง Python และ PostgreSQL, รัน Django migrations, สร้าง superuser และเปิดหน้า Django Admin ได้สำเร็จ

> คู่มือนี้อิงการใช้งานบน **Windows + PowerShell + Django + PostgreSQL**

---

## 1) สิ่งที่ต้องมีในเครื่องก่อน

ติดตั้งโปรแกรมเหล่านี้ก่อน:

- Git
- Python 3.11
- PostgreSQL
- pgAdmin 4
- VS Code หรือ editor ที่ถนัด

เช็กใน PowerShell ได้ด้วยคำสั่ง:

```powershell
git --version
python --version
pip --version
```

---

## 2) Clone โปรเจกต์จาก GitHub

เปิด PowerShell แล้วไปโฟลเดอร์ที่ต้องการเก็บงาน เช่น

```powershell
cd D:\
mkdir CS251
cd CS251
```

จากนั้น clone repo:

```powershell
git clone <URL-REPO>
```

ตัวอย่าง:

```powershell
git clone https://github.com/ชื่อเจ้าของrepo/ชื่อrepo.git
```

แล้วเข้าโฟลเดอร์โปรเจกต์:

```powershell
cd ชื่อrepo
```

ถ้าต้องใช้ branch เฉพาะ:

```powershell
git branch -a
git checkout ชื่อbranch
```

ถ้า branch อยู่บน remote แต่ยังไม่มีในเครื่อง:

```powershell
git checkout -b ชื่อbranch origin/ชื่อbranch
```

---

## 3) เข้าโฟลเดอร์ backend ที่มี `manage.py`

```powershell
cd backend
dir
```

ควรเห็นไฟล์ประมาณนี้:

```text
manage.py
backend\
accounts\
stock\
catalog\
cart_delivery\
order_payment\
```

---

## 4) สร้าง virtual environment

อยู่ในโฟลเดอร์ `backend` แล้วรัน:

```powershell
python -m venv venv
```

---

## 5) Activate virtual environment

ทุกครั้งที่เปิด terminal ใหม่ ต้อง activate ก่อน:

```powershell
venv\Scripts\activate
```

ถ้าสำเร็จจะเห็น `(venv)` ขึ้นหน้าบรรทัดคำสั่ง

---

## 6) ติดตั้ง dependencies

ถ้ามี `requirements.txt` ให้รัน:

```powershell
pip install -r requirements.txt
```

ถ้ายังไม่มี ให้ติดตั้งขั้นต่ำอย่างน้อย:

```powershell
pip install django psycopg2-binary
```

เช็กเวอร์ชัน Django:

```powershell
python -m django --version
```

---

## 7) สร้างฐานข้อมูลใน PostgreSQL

### วิธีผ่าน pgAdmin

1. เปิด **pgAdmin 4**
2. ล็อกอินเข้า PostgreSQL server
3. คลิกขวาที่ `Databases`
4. เลือก **Create > Database...**
5. ตั้งชื่อ database เช่น:

```text
smart_furniture_db
```

6. กด Save

---

## 8) ตั้งค่า `DATABASES` ใน Django

เปิดไฟล์ `settings.py` แล้วหาส่วน `DATABASES`

ตัวอย่าง:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smart_furniture_db',
        'USER': 'postgres',
        'PASSWORD': 'รหัสผ่าน_postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

ถ้าโปรเจกต์ใช้ `.env` ให้ใส่ค่าให้ตรงกับเครื่องตัวเอง

ตัวอย่าง `.env`:

```env
DB_NAME=smart_furniture_db
DB_USER=postgres
DB_PASSWORD=รหัสผ่าน_postgres
DB_HOST=localhost
DB_PORT=5432
```

---

## 9) เช็ก `INSTALLED_APPS`

ใน `settings.py` ควรมี app เหล่านี้

```python
'accounts',
'stock',
'catalog',
'cart_delivery',
'order_payment',
```

และ app มาตรฐานของ Django:

```python
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
```

---

## 10) รัน migrations

ถ้ามี migration อยู่แล้ว:

```powershell
python manage.py migrate
```

ถ้ายังไม่มี migration ของ app ให้รัน:

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

## 11) สร้าง superuser

ใช้สำหรับล็อกอินหน้า admin:

```powershell
python manage.py createsuperuser
```

กรอก:

- Username
- Email address
- Password

---

## 12) รัน Django server

```powershell
python manage.py runserver
```

ถ้าสำเร็จ จะขึ้นประมาณนี้:

```text
Starting development server at http://127.0.0.1:8000/
```

---

## 13) เปิดหน้า admin

เปิด browser แล้วเข้า:

```text
http://127.0.0.1:8000/admin/
```

หรือ

```text
http://localhost:8000/admin/
```

จากนั้นล็อกอินด้วย superuser ที่สร้างไว้

---

## 14) ลำดับคำสั่งแบบสั้นสุด

```powershell
git clone <URL-REPO>
cd ชื่อrepo
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

จากนั้นเปิด:

```text
http://127.0.0.1:8000/admin/
```

---

## 15) ถ้าเปิด `/admin/` ได้ แต่ไม่เห็น model

ให้เช็กไฟล์ `admin.py` ของแต่ละ app ว่ามีการ register model หรือยัง เช่น:

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

---

## 16) ปัญหาที่พบบ่อย

### 1. `ModuleNotFoundError`
ยังไม่ได้ activate venv หรือยังไม่ได้ install package

```powershell
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. `database "..." does not exist`
ยังไม่ได้สร้าง database ใน PostgreSQL

### 3. `connection to server at "localhost" failed`
PostgreSQL ยังไม่เปิด หรือค่าการเชื่อมต่อใน `settings.py` ไม่ตรง

### 4. `psycopg2` error
ยังไม่ได้ลง PostgreSQL driver

```powershell
pip install psycopg2-binary
```

### 5. `relation ... already exists`
ใช้ฐานข้อมูลเก่าที่เคยมีตารางอยู่แล้ว อาจต้องลบ database เดิมแล้วสร้างใหม่

### 6. เข้าหน้า admin ได้ แต่ล็อกอินไม่ได้
ให้สร้าง superuser ใหม่

```powershell
python manage.py createsuperuser
```

---

## 17) เวลาเปิดโปรเจกต์รอบถัดไป

ถ้า setup ครั้งแรกเสร็จแล้ว รอบต่อไปใช้แค่นี้:

```powershell
cd D:\CS251\ชื่อrepo\backend
venv\Scripts\activate
python manage.py runserver
```

ถ้ามี migration ใหม่จากเพื่อน ให้ pull แล้วรัน:

```powershell
git pull
python manage.py migrate
```

---

## 18) ข้อแนะนำสำหรับงานทีม

- ให้ทุกคนใช้ Python เวอร์ชันใกล้กัน
- ใช้ชื่อ database คนละชื่อถ้ากลัวชนกัน
- อย่า commit โฟลเดอร์ `venv/`
- ควรมีไฟล์ `requirements.txt`
- ถ้าเปลี่ยน models แล้ว commit migration ขึ้น git ด้วย

---

จบขั้นตอน เพื่อนในทีมควร clone โปรเจกต์, ตั้ง PostgreSQL, migrate และเปิดหน้า admin ได้เรียบร้อย
