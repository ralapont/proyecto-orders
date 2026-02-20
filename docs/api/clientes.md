# API – Servicio de Clientes

## POST /clientes

Crea un nuevo cliente.

### Body
{
  "nombre": "Juan",
  "email": "juan@example.com"
}

### Respuesta 201
{
  "id": "65b1f8e2c9a1",
  "nombre": "Juan",
  "email": "juan@example.com"
}