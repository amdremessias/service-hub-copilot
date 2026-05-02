# API Documentation - Service Hub

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Todas as requisições autenticadas requerem o header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

#### Register

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "role": "client"
}

Response 201:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### Login

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response 200:
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### Get Current User

```http
GET /auth/me
Authorization: Bearer <token>

Response 200:
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "client",
  "is_active": true,
  "is_verified": false,
  "created_at": "2026-05-02T08:00:00Z"
}
```

### Users

#### Get Current User Profile

```http
GET /users/me
Authorization: Bearer <token>

Response 200:
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+55 11 99999-9999",
  "bio": "Técnico especializado",
  "role": "technician",
  "is_active": true,
  "is_verified": true
}
```

#### Update User Profile

```http
PUT /users/me
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+55 11 99999-9999",
  "bio": "Bio atualizada"
}

Response 200: (User object)
```

#### Get User by ID

```http
GET /users/{user_id}

Response 200: (User object)
```

### Technicians

#### Create Technician Profile

```http
POST /technicians
Authorization: Bearer <token>
Content-Type: application/json

{
  "company_name": "Tech Solutions",
  "bio": "Especialista em instalação",
  "years_of_experience": 5,
  "hourly_rate": 150.00,
  "specialization_ids": [1, 2]
}

Response 201:
{
  "id": 1,
  "user_id": 1,
  "company_name": "Tech Solutions",
  "bio": "Especialista em instalação",
  "years_of_experience": 5,
  "rating": 0.0,
  "total_reviews": 0,
  "hourly_rate": 150.00,
  "is_verified": 0,
  "specializations": []
}
```

#### List Technicians

```http
GET /technicians?skip=0&limit=10&specialization_id=1

Response 200:
[
  {
    "id": 1,
    "user_id": 1,
    "company_name": "Tech Solutions",
    "years_of_experience": 5,
    "rating": 4.8,
    "total_reviews": 25,
    "hourly_rate": 150.00,
    "is_verified": 1,
    "specializations": [
      {
        "id": 1,
        "name": "Instalação de ar condicionado",
        "description": "..."
      }
    ]
  }
]
```

#### Get Technician

```http
GET /technicians/{technician_id}

Response 200: (Technician object)
```

#### Update Technician

```http
PUT /technicians/{technician_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "company_name": "Updated Name",
  "hourly_rate": 200.00,
  "specialization_ids": [1, 2, 3]
}

Response 200: (Technician object)
```

### Services

#### List Service Categories

```http
GET /services/categories

Response 200:
[
  {
    "id": 1,
    "name": "Ar Condicionado",
    "description": "...",
    "icon_url": "..."
  }
]
```

#### List Services

```http
GET /services?skip=0&limit=10&category_id=1&technician_id=1

Response 200:
[
  {
    "id": 1,
    "technician_id": 1,
    "category_id": 1,
    "title": "Instalação de Ar Condicionado",
    "description": "Instalação profissional de ar condicionado",
    "price": 500.00,
    "duration_minutes": 120,
    "is_available": true,
    "image_url": "..."
  }
]
```

#### Get Service

```http
GET /services/{service_id}

Response 200: (Service object)
```

### Bookings

#### Create Booking

```http
POST /bookings
Authorization: Bearer <token>
Content-Type: application/json

{
  "service_id": 1,
  "technician_id": 1,
  "scheduled_date": "2026-05-10T14:00:00Z",
  "duration_minutes": 120,
  "address": "Rua das Flores, 123",
  "latitude": "-23.5505",
  "longitude": "-46.6333",
  "notes": "Notas adicionais"
}

Response 201:
{
  "id": 1,
  "client_id": 1,
  "technician_id": 1,
  "service_id": 1,
  "scheduled_date": "2026-05-10T14:00:00Z",
  "duration_minutes": 120,
  "address": "Rua das Flores, 123",
  "status": "pending",
  "created_at": "2026-05-02T09:00:00Z"
}
```

#### Get My Bookings

```http
GET /bookings/my-bookings?skip=0&limit=10
Authorization: Bearer <token>

Response 200: (Array of Booking objects)
```

#### Get Booking

```http
GET /bookings/{booking_id}

Response 200: (Booking object)
```

#### Update Booking

```http
PUT /bookings/{booking_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "scheduled_date": "2026-05-11T14:00:00Z",
  "status": "confirmed"
}

Response 200: (Booking object)
```

### Reviews

#### Get Technician Reviews

```http
GET /reviews/technician/{technician_id}?skip=0&limit=10

Response 200: (Array of Review objects)
```

#### Get Review

```http
GET /reviews/{review_id}

Response 200:
{
  "id": 1,
  "booking_id": 1,
  "reviewer_id": 1,
  "technician_id": 1,
  "rating": 5,
  "comment": "Excelente serviço!",
  "professionalism": 5,
  "punctuality": 5,
  "quality": 5
}
```

### Chat

#### List Chat Rooms

```http
GET /chat/rooms
Authorization: Bearer <token>

Response 200: (Array of ChatRoom objects)
```

#### Get Chat Room

```http
GET /chat/rooms/{room_id}
Authorization: Bearer <token>

Response 200: (ChatRoom object)
```

#### Get Chat Messages

```http
GET /chat/rooms/{room_id}/messages?skip=0&limit=50
Authorization: Bearer <token>

Response 200: (Array of ChatMessage objects)
```

## Error Responses

### 401 Unauthorized

```json
{
  "detail": "Unauthorized",
  "error_code": "UNAUTHORIZED"
}
```

### 404 Not Found

```json
{
  "detail": "Resource not found",
  "error_code": "NOT_FOUND"
}
```

### 422 Validation Error

```json
{
  "detail": "Validation failed",
  "error_code": "VALIDATION_ERROR"
}
```

## Rate Limiting

- 100 requisições por minuto por IP
- 1000 requisições por hora por usuário

## Pagination

A maioria dos endpoints de listagem suporta paginação:

```
GET /endpoint?skip=0&limit=10
```

- `skip`: Número de registros a pular (default: 0)
- `limit`: Número de registros a retornar (default: 10, max: 100)

## Versioning

A API segue versionamento semântico. A versão atual é v1.

Próximas versões podem ser acessadas em:
```
/api/v2/...
```
