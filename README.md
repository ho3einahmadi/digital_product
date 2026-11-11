# digital_product — Digital products catalogue (Django)

**English** · [فارسی](#فارسی)

A Django project for a digital-products catalogue: hierarchical categories, products with images, and downloadable files attached to each product. Everything is managed from the Django admin.

### Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # or export DJANGO_SECRET_KEY / DJANGO_DEBUG
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Environment: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` (`1`/`0`), `DJANGO_ALLOWED_HOSTS` (comma separated). With `DJANGO_DEBUG=0` the app refuses to start without a real secret key.

### Models
`Category` (self-referencing), `Product` (many-to-many categories), `File` (upload per product).

---

<a id="فارسی"></a>

<div dir="rtl">

## digital_product — Digital products catalogue (Django)

یک پروژهٔ جنگو برای کاتالوگ محصولات دیجیتال: دسته‌بندی چندسطحی، محصول با تصویر، و فایل‌های قابل‌دانلود برای هر محصول. همه‌چیز از پنل ادمین جنگو مدیریت می‌شود.

### راه‌اندازی
```bash
python -m venv .venv && source .venv/bin/activate   # ویندوز: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # یا DJANGO_SECRET_KEY و DJANGO_DEBUG را export کنید
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
متغیرها: `DJANGO_SECRET_KEY`، `DJANGO_DEBUG` (مقدار `1` یا `0`)، `DJANGO_ALLOWED_HOSTS` (با ویرگول). اگر `DJANGO_DEBUG=0` باشد و کلید واقعی تنظیم نشده باشد، برنامه اجرا نمی‌شود.

### مدل‌ها
`Category` (دسته‌بندی تو در تو)، `Product` (ارتباط چندبه‌چند با دسته‌ها)، `File` (فایل آپلودی برای هر محصول).

</div>
