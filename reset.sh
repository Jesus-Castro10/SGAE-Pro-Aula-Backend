#!/bin/bash
echo "🔁 Limpiando migraciones..."

# Limpiar archivos en sgae_app/migrations (excepto __init__.py)
find sgae_app/migrations -type f -name "*.py" ! -name "__init__.py" -delete
find sgae_app/migrations -type f -name "*.pyc" -delete

# Limpiar archivos en auth_app/migrations (excepto __init__.py)
find auth_app/migrations -type f -name "*.py" ! -name "__init__.py" -delete
find auth_app/migrations -type f -name "*.pyc" -delete

echo "🗑️  Eliminando base de datos local..."
rm -f db.sqlite3

echo "⚙️  Regenerando migraciones..."
python3 manage.py makemigrations

echo "🧱 Aplicando migraciones..."
python3 manage.py migrate

echo "✅ Proceso completado. Base de datos y migraciones reiniciadas."
