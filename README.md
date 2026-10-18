# Rahmatullayev.uz — Shaxsiy Portfolio & Texnik Blog

Zamonaviy, tezkor, estetik va to'liq **Django 5.x**, **Python 3.13**, **PostgreSQL**, **Redis**, **Docker**, **Tailwind CSS** hamda **HTMX** texnologiyalari asosida yaratilgan dasturchining shaxsiy portfolio va blog vebsayti.

---

## 🚀 Texnologiyalar Steki

- **Dasturlash tili:** Python 3.13
- **Paket menejeri:** [uv](https://github.com/astral-sh/uv) (Astral)
- **Backend Freymvork:** Django 5.x (Modulli arxitektura)
- **Ma'lumotlar Bazasi:** PostgreSQL 16
- **Kesh & Xabarlar:** Redis 7 (`django-redis`)
- **Konteynerizatsiya:** Docker & Docker Compose
- **Frontend & Stil:** Tailwind CSS (Dark/Light mode, Emerald/Yashil va Oq minimalist dizayn)
- **Interaktivlik:** HTMX (sahifani qayta yuklamasdan qidirish va filtrlash)
- **Kontent tahriri:** Markdown + Pygments (Kod sintaksisini ranglash) + Bleach (XSS xavfsizligi)
- **Statik fayllar:** WhiteNoise
- **Kod sifati va Linter:** Ruff

---

## 📋 Sayt Bo'limlari

1. **Bosh Sahifa (Home / Hero):** Qisqacha tanishuv, kasbiy unvon, asosiy texnologiyalar steki, tanlangan loyihalar va aloqa chaqiruvi.
2. **Men Haqimda (About):** Batafsil tarjimai hol, toifalangan ko'nikmalar (Backend, Database, DevOps, Tools), ish tajribasi xronologiyasi (Timeline) va CV (Rezyume) yuklab olish.
3. **Loyihalar (Projects):** Amalga oshirilgan loyihalar katalogi, toifalar bo'yicha HTMX jonli filtrlash, GitHub & Jonli Demo havolalari hamda har bir loyihaning batafsil sahifasi.
4. **Blog (Articles):** Jonli qidiruv (debounce), teglar, o'qish vaqti hisoblagichi, ko'rishlar statistikasi, ijtimoiy tarmoqlarga ulashish (Telegram, Twitter/X, LinkedIn) hamda Markdown kod sintaksisi ranglanishi.
5. **Bog'lanish (Contact):** Aloqa kartochkalari, Honeypot spam himoyasiga ega aloqa shakli, xabarlarni bazada saqlash va Telegram bot orqali shaxsiy profilingizga darhol bildirishnoma yuborish.
6. **SEO & Qidiruv:** Avtomatik `/sitemap.xml`, `/robots.txt` hamda OpenGraph / Twitter Card metateglari.

---

## 🛠️ Tezkor Ishga Tushirish

### 1-usul: Docker Compose orqali (Tavsiya etiladi)

Loyihani barcha xizmatlar (Django Web, PostgreSQL va Redis) bilan bitta buyruqda ishga tushiring:

```bash
# 1. Loyihani klonlash
git clone https://github.com/rahmatullayev/rahmatullayev-uz.git
cd rahmatullayev-uz

# 2. Muhit o'zgaruvchilarini nusxalash
cp .env.example .env

# 3. Docker konteynerlarini ko'tarish
docker compose up --build -d

# 4. Boshlang'ich migratsiyalarni amalga oshirish
docker compose exec web python manage.py migrate

# 5. Namunaviy ma'lumotlarni bazaga yuklash
docker compose exec web python manage.py seed_pages
docker compose exec web python manage.py seed_projects
docker compose exec web python manage.py seed_blog

# 6. Admin foydalanuvchi yaratish
docker compose exec web python manage.py createsuperuser
```

Sayt brauzeringizda tayyor: **`http://localhost:8000`**  
Admin boshqaruv paneli: **`http://localhost:8000/admin`**

---

### 2-usul: Lokal Muhitda (`uv` bilan)

Agar loyihani Docker'siz kompyuteringizda to'g'ridan-to'g'ri ishga tushirmoqchi bo'lsangiz:

```bash
# 1. Bog'liqliklarni o'rnatish
uv sync

# 2. Migratsiyalarni amalga oshirish
uv run python manage.py migrate

# 3. Namunaviy ma'lumotlarni yuklash
uv run python manage.py seed_pages
uv run python manage.py seed_projects
uv run python manage.py seed_blog

# 4. Superuser yaratish
uv run python manage.py createsuperuser

# 5. Serverni ishga tushirish
uv run python manage.py runserver
```

---

## 🤖 Telegram Bot Bildirishnomasini Sozlash

Saytdan yuborilgan xabarlarni to'g'ridan-to'g'ri Telegramingizga qabul qilish uchun:

1. Telegramda [@BotFather](https://t.me/BotFather) orqali yangi bot oching va `API_TOKEN` oling.
2. [@userinfobot](https://t.me/userinfobot) orqali o'zingizning shaxsiy `CHAT_ID` raqamingizni aniqlang.
3. `.env` faylida quyidagi qatorlarni to'ldiring:
   ```env
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
   TELEGRAM_CHAT_ID=123456789
   ```

---

## 🧪 Kod Sifatini Tekshirish (Linter & Formatter)

Ruff yordamida kodni tekshirish va formatlash:

```bash
# Linter tekshiruvi
uv run ruff check .

# Avtomatik to'g'rilash va formatlash
uv run ruff check --fix .
uv run ruff format .
```

---

## 📄 Litsenziya

Ushbu loyiha MIT litsenziyasi asosida tarqatiladi.
Muallif: **Sardor Rahmatullayev**
