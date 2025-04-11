#!/bin/sh

host="$POSTGRES_HOST"
port="${POSTGRES_PORT:-5432}"

echo "⏳ Waiting for PostgreSQL at $host:$port..."

while ! nc -z "$host" "$port"; do
  sleep 1
done

echo "✅ PostgreSQL is up - continuing..."
exec "$@"