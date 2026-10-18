# Bosqichma-bosqich Amalga Oshirish Rejasi (PLAN.md)

Ushbu reja **Rahmatullayev.uz** shaxsiy portfolio va blog vebsaytini noldan to'liq ishga tushirish bosqichlarini belgilaydi.

---

## 📌 1-Bosqich: Loyiha Muhiti va Konteynerizatsiyani Sozlash
- [x] `uv` paket menejeri orqali loyihani initsializatsiya qilish (`pyproject.toml`).
- [x] Python 3.13 talabi bilan asosiy kutubxonalarni qo'shish:
  - `django`, `psycopg[binary]`, `django-environ`, `redis`, `django-redis`, `whitenoise`, `markdown`, `pygments`, `pillow`, `bleach`, `requests`, `gunicorn`, `ruff`.
- [x] `.gitignore` va `.env.example` fayllarini yaratish.
- [x] Ko'p bosqichli samarali `Dockerfile` yozish (`uv` keshlaridan foydalanadigan).
- [x] `docker-compose.yml` faylini tuzish (`web`, `db` (Postgres 16), `redis` (Redis 7)).
- [x] Konteynerlar o'rtasidagi tarmoq va ma'lumotlar hajmlarini (volumes) to'g'ri ulash.

---

## 📌 2-Bosqich: Django Asosiy Konfiguratsiyasi (Config & Core)
- [x] Modulli Django loyiha strukturasini tuzish (`config/settings/base.py`, `local.py`, `production.py`).
- [x] Ma'lumotlar bazasi (PostgreSQL) va Kesh (Redis) ulanishlarini sozlash.
- [x] `apps/common` ilovasini yaratish (qayta ishlatiluvchi `TimeStampedModel` va yordamchi funksiyalar).
- [x] Admin panel sozlamalari va o'zbek/ingliz tillari sozlamalari.
- [x] Boshlang'ich migratsiyalarni amalga oshirish va Docker muhitida test qilish.

---

## 📌 3-Bosqich: Frontend Fundamenti, Tailwind CSS va Dark/Light Mode
- [x] Tailwind CSS sozlamalarini o'rnatish (Dark mode sinflari, Yashil va Oq ranglar palitrasi).
- [x] `templates/base.html` asosiy shablonini loyihalash:
  - Seo metateglari, responsive viewport.
  - FOUC (miltillash) bo'lmasligi uchun tejamkor inline JavaScript.
  - Minimalistik va zamonaviy Header / Navbar (Mobil menyu va Desktop menyu).
  - Dark/Light mode almashtirgich (Theme switcher) tugmasi (quyosh va oy ikonkalari bilan).
  - Minimalistik Footer (Ijtimoiy tarmoqlar havolalari, mualliflik huquqi).

---

## 📌 4-Bosqich: "Men Haqimda" va Bosh Sahifa (`apps/pages`)
- [x] `pages` ilovasini yaratish:
  - Bosh sahifa (Home / Hero section): Qisqacha o'zingiz haqingizda, jozibali sarlavha, "Loyihalarni ko'rish" va "Bog'lanish" tugmalari.
  - Men haqimda (About Me): Batafsil bio, tajriba yillari, ta'lim.
  - Ko'nikmalar (Tech Skills): Kategoriyalarga bo'lingan texnologiyalar (Backend, DevOps, Database, Tools) kartochkalari.
  - Tajriba xronologiyasi (Work Experience Timeline).
  - Rezyume (CV) yuklab olish tugmasi.

---

## 📌 5-Bosqich: "Loyihalar" Bo'limi (`apps/projects`)
- [x] `projects` ilovasi ma'lumotlar modellarini yaratish:
  - `Technology` (nomi, ikonkasi, rangi).
  - `ProjectCategory` (Web, Mobile, Open Source, API va h.k.).
  - `Project` (sarlavha, slug, qisqa tavsif, batafsil markdown matn, rasm, GitHub URL, Live Demo URL, saralash tartibi, featured statusi).
- [x] Django Admin panelida loyihalarni qulay boshqarish interfeysi.
- [x] Loyihalar ro'yxati sahifasi (`/projects/`):
  - Kategoriyalar va texnologiyalar bo'yicha qulay filtrlash.
  - Zamonaviy loyiha kartochkalari (rasm, teglar, linklar).
- [x] Loyiha tafsilotlari sahifasi (`/projects/<slug>/`):
  - Skrinshotlar, batafsil arxitektura tavsifi, ishlatilgan stek.

---

## 📌 6-Bosqich: "Blog" Bo'limi (`apps/blog`)
- [x] `blog` ilovasi ma'lumotlar modellarini yaratish:
  - `BlogCategory`, `BlogTag`.
  - `BlogPost` (sarlavha, slug, rasm, qisqa xulosa, Markdown matn, o'qish vaqti, ko'rishlar soni, nashr etilgan vaqt, status).
- [x] Markdown formatini xavfsiz HTML ga aylantirish va Pygments orqali kod sintaksisini ranglash.
- [x] Maqolalar ro'yxati sahifasi (`/blog/`):
  - Teglar bo'yicha filtrlash, qidiruv paneli, sahifalash (pagination).
- [x] Maqola o'qish sahifasi (`/blog/<slug>/`):
  - Chiroyli typografiya (`prose`, `dark:prose-invert`).
  - Maqolani ijtimoiy tarmoqlarda ulashish tugmalari.

---

## 📌 7-Bosqich: "Bog'lanish" Bo'limi (`apps/contact`)
- [x] `ContactMessage` modeli va Django Form yaratish (Ism, Email, Mavzu, Xabar).
- [x] Spam himoyasi (Honeypot maydoni).
- [x] Xabar kelganda avtomatik ravishda:
  - Ma'lumotlar bazasida saqlash.
  - Telegram bot orqali shaxsiy profilingizga darhol bildirishnoma (alert) yuborish.
- [x] Foydalanuvchiga muvaffaqiyatli yuborilganlik haqida estetik xabar chiqarish.

---

## 📌 8-Bosqich: Kesh (Redis), SEO, Xavfsizlik va Unumdorlik
- [x] Redis orqali seanslar va sahifalarni keshlash sozlamalari (`django-redis`).
- [x] Ma'lumot o'zgarganda tegishli sahifa keshini avtomatik tozalash (signals).
- [x] Statik fayllarni WhiteNoise orqali siqish va keshlash.
- [x] XML Sitemap (`/sitemap.xml`) va `robots.txt` integratsiyasi.
- [x] Barcha sahifalar uchun dinamik OpenGraph va Twitter Card meta teglari.

---

## 📌 9-Bosqich: Yakuniy Sinov va Hujjatlashtirish
- [x] Barcha sahifalarning Light va Dark modeda to'g'ri ko'rinishini tekshirish.
- [x] Mobil va planshet qurilmalarda responsivlikni test qilish.
- [x] Docker Compose orqali bitta buyruq bilan to'liq loyihani ishga tushirishni tekshirish (`docker compose up --build`).
- [x] `README.md` fayliga to'liq ishga tushirish va foydalanish yo'riqnomasini yozish.
