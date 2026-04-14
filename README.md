.venv\Scripts\activate
python manage.py runserver
http://127.0.0.1:8000/admin/

python -m http.server 3000
http://127.0.0.1:3000/frontend/preview.html

ไม่มีไรจะเทส git

# README Setup Guide

คู่มือนี้สรุปแค่ขั้นตอนที่ต้องพิมพ์ใน terminal และผลที่ควรเกิดขึ้น เพื่อให้เพื่อนในทีมเปิด backend, Django Admin และหน้าพรีวิวฟร้อนเอนด์ได้

## 1) Clone โปรเจกต์

พิมพ์ใน PowerShell:

```powershell
git clone https://github.com/FMaLife/PV_CS251_Project.git
cd PV_CS251_Project
```

สิ่งที่ควรเกิดขึ้น:
- จะมีโฟลเดอร์ `PV_CS251_Project` ถูกสร้างขึ้น
- เมื่อ `cd` เข้าไปแล้ว จะเห็นโฟลเดอร์ `backend` และ `frontend`

---

## 2) เข้า backend

```powershell
cd backend
dir
```

สิ่งที่ควรเกิดขึ้น:
- ควรเห็นไฟล์ `manage.py`
- ควรเห็นโฟลเดอร์ประมาณนี้:
  - `Group10_CS251_Project`
  - `accounts`
  - `stock`
  - `catalog`
  - `cart_delivery`
  - `order_payment`

---

## 3) สร้างและเปิด virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

สิ่งที่ควรเกิดขึ้น:
- จะมีโฟลเดอร์ `venv`
- หลัง activate แล้ว บรรทัดคำสั่งจะขึ้น `(venv)` ด้านหน้า

ตัวอย่าง:

```text
(venv) PS D:\CS251\PV_CS251_Project\backend>
```

---

## 4) ติดตั้ง package

```powershell
pip install -r requirements.txt
```

สิ่งที่ควรเกิดขึ้น:
- package ต่าง ๆ จะถูกติดตั้ง
- ถ้าสำเร็จจะเห็นข้อความประมาณ `Successfully installed ...`

ถ้าไม่มี `requirements.txt` ให้ใช้:

```powershell
pip install django psycopg2-binary python-decouple
```

---

## 5) สร้างฐานข้อมูล PostgreSQL และตั้งค่า `.env`

ให้สร้าง database ใน PostgreSQL ไว้ก่อน เช่นชื่อ:

```text
smart_furniture_db
```

แล้วสร้างไฟล์ `.env` ในโฟลเดอร์ `backend` โดยใส่ค่าประมาณนี้:

```env
SECRET_KEY=django-insecure-change-this
DEBUG=True

DB_NAME=smart_furniture_db
DB_USER=postgres
DB_PASSWORD=รหัสผ่านของตัวเอง
DB_HOST=localhost
DB_PORT=5432
```

สิ่งที่ควรเกิดขึ้น:
- Django จะสามารถเชื่อมต่อ PostgreSQL ได้ตอนรัน migration

---

## 6) รัน migrations

```powershell
python manage.py migrate
```

สิ่งที่ควรเกิดขึ้น:
- จะเห็นข้อความประมาณนี้:

```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, ...
Running migrations:
  Applying ...
  OK
```

แปลว่าตารางถูกสร้างในฐานข้อมูลแล้ว

---

## 7) สร้าง superuser

```powershell
python manage.py createsuperuser
```

สิ่งที่ควรเกิดขึ้น:
- ระบบจะถาม `Username`
- ระบบจะถาม `Email address`
- ระบบจะถาม `Password`

ถ้าสำเร็จจะเห็นประมาณนี้:

```text
Superuser created successfully.
```

---

## 8) รัน Django server

```powershell
python manage.py runserver
```

สิ่งที่ควรเกิดขึ้น:
- จะเห็นข้อความประมาณนี้:

```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Starting development server at http://127.0.0.1:8000/
```

แปลว่า backend เปิดแล้ว

---

## 9) เปิด Django Admin

เปิด Chrome แล้วเข้า URL นี้:

```text
http://127.0.0.1:8000/admin/
```

สิ่งที่ควรเกิดขึ้น:
- จะเห็นหน้า login ของ Django Admin
- ให้ล็อกอินด้วย superuser ที่สร้างไว้
- ถ้าสำเร็จจะเข้าหน้าจัดการข้อมูลหลังบ้าน

---

## 10) เปิดหน้าพรีวิวฟร้อนเอนด์

เปิด terminal ใหม่ แล้วพิมพ์:

```powershell
cd D:\CS251\PV_CS251_Project\frontend
dir
```

สิ่งที่ควรเกิดขึ้น:
- ควรเห็นไฟล์ HTML สำหรับทดลองหน้าเว็บ เช่น
  - `preview.html`
  - `pv_cs251_api_demo.html`
  - `admin_inventory_demo.html`

จากนั้นให้เปิดไฟล์ HTML ด้วย Chrome หรือ Live Server

สิ่งที่ควรเกิดขึ้น:
- จะเห็นหน้าเว็บพรีวิวของฟร้อนเอนด์
- ถ้า backend ยังรันอยู่ที่ `http://127.0.0.1:8000` หน้าเว็บจะสามารถเรียก API ได้

---

## 11) ถ้าจะเปิดโปรเจกต์รอบถัดไป

ครั้งต่อไปไม่ต้องสร้าง venv ใหม่ แค่พิมพ์:

```powershell
cd D:\CS251\PV_CS251_Project\backend
venv\Scripts\activate
python manage.py runserver
```

แล้วเปิด:

```text
http://127.0.0.1:8000/admin/
```

---

## 12) ถ้ามีปัญหา

### เปิด server ไม่ได้
ให้เช็กว่า activate venv แล้วหรือยัง

```powershell
venv\Scripts\activate
```

### ต่อ database ไม่ได้
ให้เช็กว่า PostgreSQL เปิดอยู่ และค่าใน `.env` ตรงกับเครื่องตัวเอง

### เปิด admin ไม่ได้
ให้เช็กว่า runserver อยู่ และเข้า URL นี้ให้ถูก:

```text
http://127.0.0.1:8000/admin/
```

### หน้าเว็บฟร้อนเปิดได้ แต่เรียก API ไม่ได้
ให้เช็กว่า backend ยังรันอยู่ที่:

```text
http://127.0.0.1:8000
```

---

จบขั้นตอน เพื่อนในทีมควรเปิด backend, เข้า Django Admin และเปิดหน้าพรีวิวฟร้อนเอนด์ได้
