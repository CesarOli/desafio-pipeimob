#!/bin/sh
# Aguarda o banco de dados estar pronto antes de subir o app

echo "Aguardando o banco de dados iniciar..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Banco de dados iniciado, subindo o app..."
exec "$@"