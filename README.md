# 🔗 QR Code Generator & Scanner (Django)

A Django-based web application that allows you to **generate QR codes** from any text or URL and **scan uploaded images** to decode QR codes.  
This project was built for learning Django, and it demonstrates working with **models, views, templates, static files, forms, and third-party libraries**.

---

## ✨ Features

- 🖼️ **Generate QR Code** from text or URL  
- 📥 **Download QR Code** as PNG  
- 📷 **Scan QR Code** from uploaded images (JPG/PNG)  
- 🌐 **Open from phone** by generating QR with your PC’s LAN IP  
- 🗂️ **Admin panel support** — view all generated QR codes  
- 🎨 **Responsive UI** with custom CSS styling  
- 🔒 Environment-based settings (`SECRET_KEY`, `DEBUG`, etc.)  

---

## 🛠️ Tech Stack

- **Backend:** [Django 5](https://www.djangoproject.com/)  
- **Database:** SQLite (default)  
- **Frontend:** HTML, CSS, Django Templates  
- **Libraries:**  
  - [qrcode](https://pypi.org/project/qrcode/) (QR generation)  
  - [Pillow](https://pypi.org/project/Pillow/) (image handling)  
  - [pyzbar](https://pypi.org/project/pyzbar/) (QR code decoding)  
  - [opencv-python](https://pypi.org/project/opencv-python/) (optional preprocessing)  

---

## 📂 Project Structure

```
QR_GEN_SCAN/               # Main Django project folder
│── QR_GEN_SCAN/           # Settings, URLs, WSGI/ASGI
│── core/                  # Base app (home page, base template, static files)
│── scanner/               # QR generator + scanner app
│   ├── templates/         # generator.html, scan.html
│   ├── models.py          # GeneratedQR model
│   ├── views.py           # generate_qr, scan_qr logic
│── manage.py              # Django CLI entrypoint
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## ⚡ Quick Start (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Milind1234/QR_Code_Generator_-_Scanner_Using_Django.git
cd qr-gen-scan
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the development server
```bash
python manage.py runserver
```

👉 Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📱 Access from Phone (LAN)

1. Find your PC’s IP:
   ```bash
   ipconfig   # Windows
   ```
   Example: `192.168.0.106`

2. Run Django server for LAN access:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. On your phone (same Wi-Fi), open:
   ```
   http://192.168.0.106:8000
   ```

4. Generate a QR with this link → scan with phone camera → site opens 🎉

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](docs/screenshots/home.png)

### 🎨 Generate QR
![Generate Page](docs/screenshots/generate.png)

### 📷 Scan QR
![Scan Page](docs/screenshots/scan.png)

*(Add your screenshots under `docs/screenshots/` and update paths.)*

---

## 📖 Usage Guide

### Generate QR
1. Navigate to `/scanner/generate/`  
2. Enter text or URL  
3. Click **Generate**  
4. Download PNG or scan directly with your phone  

### Scan QR
1. Navigate to `/scanner/scan/`  
2. Upload a PNG/JPG with a QR code  
3. App decodes the QR and shows the text/link  

---

## 🔒 Security Notes

- `SECRET_KEY` should not be committed publicly. Use environment variables in production.  
- `DEBUG = False` in production.  
- Use PostgreSQL or MySQL instead of SQLite for production.  
- Restrict `ALLOWED_HOSTS` to your domain/IP.  

---

## 🚀 Deployment (Optional)

For production deployment, consider:  
- [PythonAnywhere](https://www.pythonanywhere.com/)  
- [Heroku](https://www.heroku.com/)  
- [Render](https://render.com/)  
- [Railway](https://railway.app/)  

Checklist for production:
```bash
# In settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Collect static files
python manage.py collectstatic
```

Use **gunicorn + whitenoise** for serving Django + static files.

---

## 🧪 Running Tests
```bash
python manage.py test
```

---

## 📌 Future Improvements
- 📱 Add **real-time scanning via webcam/phone camera** (JS + WebRTC)  
- 📄 Export QR codes to **PDF**  
- 🗂️ Add **user authentication** (each user manages their QR codes)  
- 🔗 Provide a **REST API** (using Django REST Framework)  

---

## 🙋 Author

👤 **Milind Chavan**  
📧 myprojects525@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/milind-chavan-47a250214/) | [GitHub](https://github.com/Milind1234)

---

## 📝 License

This project is licensed under the MIT License — you are free to use and modify it.
S