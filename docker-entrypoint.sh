#!/bin/bash
set -e

# Función para esperar a que PostgreSQL esté disponible
wait_for_postgres() {
  echo "Esperando a que PostgreSQL esté disponible..."
  while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER > /dev/null 2>&1; do
    echo "PostgreSQL no disponible, esperando..."
    sleep 1
  done
  echo "PostgreSQL disponible. Continuando."
}

# Ejecutar migraciones y crear datos iniciales solo si se especifica
if [ "$1" = "django" ]; then
  wait_for_postgres
  
  echo "Aplicando migraciones..."
  python manage.py migrate --noinput
  
  if [ "$LOAD_INITIAL_DATA" = "true" ]; then
    echo "Cargando datos iniciales..."
    python crear_datos_prueba.py
  fi
  
  echo "Iniciando servidor Django..."
  exec python manage.py runserver 0.0.0.0:8000
  
elif [ "$1" = "gunicorn" ]; then
  wait_for_postgres
  
  echo "Aplicando migraciones..."
  python manage.py migrate --noinput
  
  if [ "$LOAD_INITIAL_DATA" = "true" ]; then
    echo "Cargando datos iniciales..."
    python crear_datos_prueba.py
  fi
  
  echo "Iniciando Gunicorn..."
  exec gunicorn sia_colegios.wsgi:application --bind 0.0.0.0:8000
  
else
  exec "$@"
fi 