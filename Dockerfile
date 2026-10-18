# 1-bosqich: UV binar faylini olish
FROM ghcr.io/astral-sh/uv:latest AS uv_bin

FROM python:3.13-slim

# Muhit o'zgaruvchilari
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT="/opt/venv" \
    PATH="/opt/venv/bin:$PATH"

# Ishchi katalog
WORKDIR /app

# uv binar faylini nusxalash
COPY --from=uv_bin /uv /uvx /bin/

# Tizim paketlarini yangilash
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Loyiha konfiguratsiya fayllarini nusxalash
COPY pyproject.toml uv.lock ./

# Bog'liqliklarni /opt/venv ichiga o'rnatish
RUN uv sync --frozen --no-install-project

# Loyiha kodlarini nusxalash
COPY . .

# Loyihaning o'zini o'rnatish
RUN uv sync --frozen

# Port
EXPOSE 8000

# Standart ishga tushirish buyrug'i
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
