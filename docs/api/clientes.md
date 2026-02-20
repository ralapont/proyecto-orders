📘 Servicio de Clientes – Documentación de API

## POST /clientes
Crea un nuevo cliente en el sistema.

🛠️ Verbo HTTP
POST

🧭 Router
/clientes

📥 Body de entrada — ClienteCreate
Descripción: Objeto que contiene los datos necesarios para registrar un nuevo cliente.

Esquema
```
{
  "nombre": "string",
  "email": "string (email válido)",
  "direccion": {
    "tipo_via": "string",
    "nombre_via": "string",
    "numero_via": "string",
    "codigo_postal": "string",
    "ciudad": "string",
    "provincia": "string"
  }
}
```


Ejemplo
```
{
  "nombre": "Juan Pérez",
  "email": "juan.perez@example.com",
  "direccion": {
    "tipo_via": "Calle",
    "nombre_via": "Gran Vía",
    "numero_via": "45",
    "codigo_postal": "28013",
    "ciudad": "Madrid",
    "provincia": "Madrid"
  }
}
```

📤 Respuesta 201 — ClienteResponse
Descripción: El cliente ha sido creado correctamente.
Se devuelve el objeto completo con su identificador único.

Esquema
```
{
  "id": "string",
  "nombre": "string",
  "email": "string",
  "direccion": {
    "tipo_via": "string",
    "nombre_via": "string",
    "numero_via": "string",
    "codigo_postal": "string",
    "ciudad": "string",
    "provincia": "string"
  }
}
```

Ejemplo
```
{
  "id": "65b1f8e2c9a1",
  "nombre": "Juan Pérez",
  "email": "juan.perez@example.com",
  "direccion": {
    "tipo_via": "Calle",
    "nombre_via": "Gran Vía",
    "numero_via": "45",
    "codigo_postal": "28013",
    "ciudad": "Madrid",
    "provincia": "Madrid"
  }
}
```


📌 Códigos de respuesta

| Código | Descripción                  | 
| 201    | Cliente creado correctamente | 


📌 Códigos de respuesta
|  |  | 
|  |  | 



(Actualmente no se contemplan otros códigos de salida.)

