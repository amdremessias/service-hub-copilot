# Database Schema - Service Hub

## Diagrama ER

```
┌──────────────┐
│    Users     │
├──────────────┤
│ id (PK)      │
│ email        │
│ password     │
│ first_name   │
│ last_name    │
│ phone        │
│ role         │
│ is_active    │
│ is_verified  │
│ created_at   │
│ updated_at   │
└──────────────┘
       │
       ├─────────────────┬─────────────────┐
       │                 │                 │
   (1:1)            (1:N)              (1:N)
       │                 │                 │
       ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Technician   │  │  Bookings    │  │   Reviews    │
├──────────────┤  ├──────────────┤  ├──────────────┤
│ id (PK)      │  │ id (PK)      │  │ id (PK)      │
│ user_id (FK) │  │ client_id(FK)│  │booking_id(FK)│
│ company_name │  │ technician..│  │reviewer_id..│
│ bio          │  │ service_id..│  │technician...│
│ rating       │  │ scheduled.. │  │ rating       │
│ hourly_rate  │  │ address      │  │ comment      │
│ is_verified  │  │ status       │  │ professionalism│
└──────────────┘  │ created_at   │  │ punctuality  │
       │          │ updated_at   │  │ quality      │
   (M:N)         └──────────────┘  └──────────────┘
       │               │
   Specialization      │ (1:N)
                       │
                       ├──────────────────┐
                       │                  │
                   (1:N)              (1:N)
                       │                  │
                       ▼                  ▼
            ┌──────────────┐    ┌──────────────┐
            │   Services   │    │   Payments   │
            ├──────────────┤    ├──────────────┤
            │ id (PK)      │    │ id (PK)      │
            │technician_id │    │ booking_id..│
            │ category_id  │    │ user_id (FK) │
            │ title        │    │ amount       │
            │ description  │    │ status       │
            │ price        │    │ stripe_id    │
            │ duration     │    │ created_at   │
            │ is_available │    │ updated_at   │
            └──────────────┘    └──────────────┘
                  │
              (1:N)│
                  │
                  ▼
          ┌──────────────┐
          │   Category   │
          ├──────────────┤
          │ id (PK)      │
          │ name         │
          │ description  │
          │ icon_url     │
          └──────────────┘

┌──────────────────┐
│   Chat Rooms     │
├──────────────────┤
│ id (PK)          │
│ client_id (FK)   │
│ technician_id(FK)│
│ booking_id       │
│ created_at       │
└──────────────────┘
       │
   (1:N)│
       │
       ▼
┌──────────────────┐
│ Chat Messages    │
├──────────────────┤
│ id (PK)          │
│ chat_room_id(FK) │
│ sender_id (FK)   │
│ content          │
│ is_read          │
│ created_at       │
└──────────────────┘
```

## Tabelas Detalhadas

### users
Tabela principal de usuários do sistema.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Email do usuário |
| password_hash | VARCHAR(255) | NOT NULL | Hash bcrypt da senha |
| first_name | VARCHAR(100) | NOT NULL | Primeiro nome |
| last_name | VARCHAR(100) | NOT NULL | Sobrenome |
| phone | VARCHAR(20) | | Telefone |
| profile_picture | VARCHAR(500) | | URL da foto de perfil |
| bio | TEXT | | Biografia |
| role | ENUM | NOT NULL | client, technician, admin |
| is_active | BOOLEAN | DEFAULT TRUE | Conta ativa |
| is_verified | BOOLEAN | DEFAULT FALSE | Email verificado |
| created_at | TIMESTAMP | DEFAULT NOW() | Data de criação |
| updated_at | TIMESTAMP | DEFAULT NOW() | Data de atualização |

**Índices:**
- PRIMARY KEY (id)
- UNIQUE (email)
- INDEX (role)
- INDEX (created_at)

### technicians
Perfis de técnicos cadastrados.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| user_id | INTEGER | FOREIGN KEY, UNIQUE | Referência ao usuário |
| company_name | VARCHAR(255) | | Nome da empresa |
| bio | TEXT | | Descrição profissional |
| years_of_experience | INTEGER | DEFAULT 0 | Anos de experiência |
| rating | FLOAT | DEFAULT 0.0 | Avaliação média (0-5) |
| total_reviews | INTEGER | DEFAULT 0 | Total de avaliações |
| hourly_rate | FLOAT | NOT NULL | Valor hora |
| is_verified | INTEGER | DEFAULT 0 | 0=unverified, 1=verified, 2=rejected |
| document_url | VARCHAR(500) | | URL do documento de verificação |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Índices:**
- PRIMARY KEY (id)
- UNIQUE (user_id)
- INDEX (is_verified)
- INDEX (rating)

### specializations
Especialidades dos técnicos (ar condicionado, hidráulica, etc).

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| name | VARCHAR(100) | UNIQUE, NOT NULL | Nome da especialidade |
| description | TEXT | | Descrição |
| created_at | TIMESTAMP | DEFAULT NOW() | |

### technician_specialization
Tabelassociativa (relação M:N entre técnicos e especialidades).

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| technician_id | INTEGER | FOREIGN KEY, PRIMARY KEY | |
| specialization_id | INTEGER | FOREIGN KEY, PRIMARY KEY | |

### service_categories
Categorias de serviços.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| name | VARCHAR(100) | UNIQUE, NOT NULL | Nome da categoria |
| description | TEXT | | Descrição |
| icon_url | VARCHAR(500) | | URL do ícone |
| created_at | TIMESTAMP | DEFAULT NOW() | |

### services
Serviços oferecidos pelos técnicos.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| technician_id | INTEGER | FOREIGN KEY, NOT NULL | Técnico que oferece |
| category_id | INTEGER | FOREIGN KEY, NOT NULL | Categoria do serviço |
| title | VARCHAR(255) | NOT NULL | Título do serviço |
| description | TEXT | NOT NULL | Descrição completa |
| price | FLOAT | NOT NULL | Preço do serviço |
| duration_minutes | INTEGER | NOT NULL | Duração estimada |
| is_available | BOOLEAN | DEFAULT TRUE | Disponível |
| image_url | VARCHAR(500) | | URL da imagem |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Índices:**
- PRIMARY KEY (id)
- INDEX (technician_id)
- INDEX (category_id)
- INDEX (is_available)

### bookings
Agendamentos de serviços.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| client_id | INTEGER | FOREIGN KEY, NOT NULL | Cliente |
| technician_id | INTEGER | FOREIGN KEY, NOT NULL | Técnico |
| service_id | INTEGER | FOREIGN KEY, NOT NULL | Serviço |
| scheduled_date | TIMESTAMP | NOT NULL | Data/hora agendada |
| duration_minutes | INTEGER | NOT NULL | Duração |
| address | VARCHAR(500) | NOT NULL | Endereço do serviço |
| latitude | VARCHAR(50) | | Latitude (GPS) |
| longitude | VARCHAR(50) | | Longitude (GPS) |
| notes | TEXT | | Notas adicionais |
| status | ENUM | DEFAULT 'pending' | pending, confirmed, in_progress, completed, cancelled, no_show |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Índices:**
- PRIMARY KEY (id)
- INDEX (client_id)
- INDEX (technician_id)
- INDEX (scheduled_date)
- INDEX (status)

### reviews
Avaliações de clientes sobre técnicos.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| booking_id | INTEGER | FOREIGN KEY, UNIQUE, NOT NULL | Agendamento |
| reviewer_id | INTEGER | FOREIGN KEY, NOT NULL | Quem avaliou |
| technician_id | INTEGER | FOREIGN KEY, NOT NULL | Técnico avaliado |
| rating | FLOAT | NOT NULL | Avaliação geral (1-5) |
| comment | TEXT | | Comentário |
| professionalism | FLOAT | | Profissionalismo (1-5) |
| punctuality | FLOAT | | Pontualidade (1-5) |
| quality | FLOAT | | Qualidade (1-5) |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

### payments
Registro de pagamentos.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| booking_id | INTEGER | FOREIGN KEY, UNIQUE, NOT NULL | Agendamento |
| user_id | INTEGER | FOREIGN KEY, NOT NULL | Usuário que pagou |
| amount | FLOAT | NOT NULL | Valor do pagamento |
| status | ENUM | DEFAULT 'pending' | pending, processing, completed, failed, refunded |
| stripe_payment_id | VARCHAR(255) | | ID do pagamento Stripe |
| stripe_invoice_id | VARCHAR(255) | | ID da fatura Stripe |
| payment_method | VARCHAR(50) | | card, bank_transfer, etc |
| transaction_id | VARCHAR(255) | | ID da transação |
| notes | VARCHAR(500) | | Notas |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Índices:**
- PRIMARY KEY (id)
- UNIQUE (booking_id)
- INDEX (user_id)
- INDEX (status)
- INDEX (stripe_payment_id)

### chat_rooms
Salas de chat entre clientes e técnicos.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| client_id | INTEGER | FOREIGN KEY, NOT NULL | Cliente |
| technician_id | INTEGER | FOREIGN KEY, NOT NULL | Técnico |
| booking_id | INTEGER | | Agendamento relacionado |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

### chat_messages
Mensagens de chat.

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|----------|
| id | SERIAL | PRIMARY KEY | ID único |
| chat_room_id | INTEGER | FOREIGN KEY, NOT NULL | Sala de chat |
| sender_id | INTEGER | FOREIGN KEY, NOT NULL | Remetente |
| content | TEXT | NOT NULL | Conteúdo da mensagem |
| is_read | INTEGER | DEFAULT 0 | 0=unread, 1=read |
| created_at | TIMESTAMP | DEFAULT NOW() | |

**Índices:**
- PRIMARY KEY (id)
- INDEX (chat_room_id)
- INDEX (sender_id)
- INDEX (is_read)

## Migrations

As migrations serão executadas automaticamente na primeira execução.

```bash
# Criar nova migration
alembic revision --autogenerate -m "Descrição da mudança"

# Aplicar migrations
alembic upgrade head

# Reverter última migration
alembic downgrade -1
```

## Constraints e Relacionamentos

### Cascata de Deleção

- Ao deletar um usuário, seu perfil de técnico é deletado
- Ao deletar um agendamento, a avaliação relacionada é deletada
- Ao deletar uma sala de chat, as mensagens são deletadas

### Integridade Referencial

- Não é possível criar um agendamento sem um serviço válido
- Não é possível criar uma avaliação sem um agendamento completado
- Não é possível criar um pagamento sem um agendamento válido

## Queries Comuns

### Técnicos mais avaliados

```sql
SELECT t.id, u.first_name, u.last_name, t.rating, t.total_reviews
FROM technicians t
JOIN users u ON t.user_id = u.id
ORDER BY t.rating DESC
LIMIT 10;
```

### Agendamentos pendentes

```sql
SELECT b.id, u.first_name, s.title, b.scheduled_date
FROM bookings b
JOIN users u ON b.client_id = u.id
JOIN services s ON b.service_id = s.id
WHERE b.status = 'pending'
ORDER BY b.scheduled_date ASC;
```

### Receita total

```sql
SELECT SUM(amount) as total_revenue
FROM payments
WHERE status = 'completed';
```
