# Rahmatullayev.uz — Shaxsiy Portfolio va Blog Vebsayti

Ushbu hujjat loyihaning umumiy g'oyasi, talablari, arxitekturaviy tamoyillari va tavsiya etiladigan texnologik yechimlarini belgilab beradi.

---

## 1. Loyiha Haqida

**Rahmatullayev.uz** — dasturchining shaxsiy brendi, portfoliosi, texnik blogi hamda professional tajribasini namoyish etuvchi zamonaviy, tezkor va estetik jihatdan mukammal veb-platforma.

### Asosiy Bo'limlar:
1. **Bosh sahifa / Men haqimda (Home / About):** Qisqacha tanishuv, professional yo'nalish, asosiy ko'nikmalar (skills), tajriba xronologiyasi (timeline) va CV yuklab olish imkoniyati.
2. **Loyihalar (Projects):** Amalga oshirilgan loyihalar katalogi (skrinshotlar, tavsif, ishlatilgan texnologiyalar, GitHub va Live Demo havolalari, loyiha statusi).
3. **Blog (Articles/Posts):** Texnik maqolalar, tajribalar, kod parchalari (code snippets) va amaliy qo'llanmalar. Markdown formatini qo'llab-quvvatlash va sintaksis ranglash (syntax highlighting).
4. **Bog'lanish (Contact):** Aloqa shakli (Contact Form), ijtimoiy tarmoqlar havolalari hamda xabarlarni Telegram bot yoki emailga yuborish mexanizmi.

---

## 2. Texnologiyalar Steki (Tech Stack)

Foydalanuvchi talablari va tavsiya etiladigan optimal yechimlar:

| Qatlam | Texnologiya | Izoh |
| :--- | :--- | :--- |
| **Dasturlash tili** | **Python 3.13** | Eng so'nggi barqaror versiya, yuqori tezlik va zamonaviy til xususiyatlari. |
| **Paket menejeri** | **uv** (Astral) | Eng tezkor zamonaviy Python paket menejeri (`pyproject.toml` asosida). |
| **Asosiy Framework** | **Django 5.x** | Barqaror, xavfsiz, o'rnatilgan ORM va qulay admin panelga ega to'liq backend. |
| **Ma'lumotlar bazasi**| **PostgreSQL 16+** | Ishonchli, kuchli va relational ma'lumotlar bazasi. |
| **Konteynerizatsiya** | **Docker & Docker Compose** | Web, DB va Redis servislarini bitta muhitda boshqarish. |
| **Kesh & Xabarlar** | **Redis 7+** | Sahifalar va qismlarni keshlash, seanslarni saqlash va tezkor javob vaqti. |
| **CSS & Dizayn** | **Tailwind CSS 3/4** | Utility-first CSS, toza minimalizm, Dark/Light mode integratsiyasi. |
| **Interaktivlik** | **HTMX & Vanilla JS** | Og'ir frontend frameworklarsiz (React/Vue) tezkor filtrlash, qidiruv va dinamik yuklanish. |
| **Kontent tahriri** | **Markdown + Pygments** | Blog postlar va loyiha matnlarini Markdown formatida yozish va kodlarni chiroyli ranglash. |
| **Statik fayllar** | **WhiteNoise** | Statik fayllarni konteyner ichida samarali tarqatish va siqish (gzip/brotli). |
| **Linter / Formatter**| **Ruff** | Python kodlari tozaligi va PEP 8 standartlari uchun ultra-tezkor vosita. |

---

## 3. Dizayn va UI/UX Konsepsiyasi

* **Uslub:** Minimalizm, zamonaviy typografiya, toza bo'shliqlar (whitespace), professional visual ritm.
* **Mavzular (Theme):**
  * **Light Mode:** Asosiy oq/och fon (`#FFFFFF`, `#F8FAFC`), matn to'q kulrang (`#0F172A`), urg'u (accent) yashil rang (`#059669` - Emerald-600).
  * **Dark Mode:** Asosiy chuqur to'q fon (`#09090B` - Zinc-950 yoki `#0B0F17`), matn och kulrang (`#F1F5F9`), urg'u ochiq neft/zumrad yashil (`#10B981` / `#34D399` - Emerald-400).
* **Ranglar Palitrasi:**
  * **Asosiy yashil:** `#10B981` (Emerald-500), `#059669` (Emerald-600), `#047857` (Emerald-700).
  * **Fonlar:** Oq (`#FFFFFF`) va Chuqur qora (`#09090B`).
  * **Chegaralar (Borders):** Yengil va ko'zga tashlanmaydigan nozik chiziqlar (`zinc-200` / `zinc-800`).
* **Responsiveness:** Barcha qurilmalarga (Mobile, Tablet, Desktop) to'liq moslashuvchan grid va flex tizimi.
* **Mavzu almashtirish (Theme Switcher):**
  * Foydalanuvchi tanlovini `localStorage`da saqlash.
  * Tizimning o'z sozlamalarini (`prefers-color-scheme`) avtomatik aniqlash.
  * Sahifa yuklanishida oq/qora miltillash (FOUC — Flash of Unstyled Content) oldini olish uchun boshlang'ich inline script.

---

## 4. Tavsiya Etiladigan Qo'shimcha Funksionalliklar

1. **SEO va Social Media (OpenGraph):**
   * Avtomatik XML Sitemap (`django.contrib.sitemaps`).
   * `robots.txt` fayli.
   * Har bir maqola va loyiha uchun dinamik OpenGraph va Twitter Card meta teglar.
2. **O'qish vaqti (Reading Time):**
   * Har bir blog maqolasi uchun so'zlar soniga asoslangan taxminiy o'qish vaqtini hisoblash.
3. **Qidiruv va Filtrlash:**
   * Loyihalar va maqolalarni texnologiyalar, teglar va kalit so'zlar bo'yicha tezkor (HTMX orqali sahifani qayta yuklamasdan) filtrlash.
4. **Xavfsizlik:**
   * `.env` orqali maxfiy kalitlarni yashirish.
   * CSRF, XSS himoyalari, xavfsiz HTTP headerlari (HSTS, Content-Security-Policy).
   * Contact form uchun spam himoyasi (Honeypot maydoni yoki Cloudflare Turnstile).
5. **Admin panel qulayligi:**
   * Zamonaviy va qulay Django Unfold yoki Jazzmin admin temasi (ixtiyoriy, chiroyli boshqaruv uchun).
