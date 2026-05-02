# Setup Guide - Service Hub

## Pré-requisitos

- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Docker e Docker Compose
- Git

## Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/amdremessias/service-hub-copilot.git
cd service-hub-copilot
```

### 2. Setup Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Copiar arquivo de ambiente
cp .env.example .env

# Instalar dependências
pip install -r requirements.txt

# Executar migrations (quando estiverem configuradas)
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

O backend estará disponível em: `http://localhost:8000`

Documentação interativa da API: `http://localhost:8000/docs`

### 3. Setup Frontend

```bash
cd frontend

# Copiar arquivo de ambiente
cp .env.example .env.local

# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em: `http://localhost:3000`

## Docker Compose

Para rodar a aplicação completa com Docker:

```bash
# Na raiz do projeto

# Criar arquivo .env na raiz
cp docker.env.example .env

# Subir os containers
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar os containers
docker-compose down
```

**URLs de acesso:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Estrutura do Banco de Dados

O banco de dados é criado automaticamente na primeira execução.

Tabelas principais:
- `users`: Usuários (clientes, técnicos, admins)
- `technicians`: Perfis de técnicos
- `specializations`: Especialidades dos técnicos
- `services`: Serviços oferecidos
- `service_categories`: Categorias de serviços
- `bookings`: Agendamentos
- `reviews`: Avaliações
- `payments`: Pagamentos
- `chat_rooms`: Salas de chat
- `chat_messages`: Mensagens de chat

## Variáveis de Ambiente

### Backend (.env)

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/service_hub

# JWT
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# Email (opcional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha

# Stripe (opcional)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...

# Redis
REDIS_URL=redis://localhost:6379

# Environment
ENVIRONMENT=development
DEBUG=True
```

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_WS_URL=ws://localhost:8000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_...
```

## Próximos Passos

1. Configurar variáveis de ambiente
2. Configurar banco de dados
3. Implementar autenticação OAuth2
4. Integrar Stripe para pagamentos
5. Implementar WebSockets para chat em tempo real
6. Adicionar testes automatizados
7. Configurar CI/CD
8. Deploy em produção

## Troubleshooting

### Erro de conexão com banco de dados

```bash
# Verificar se PostgreSQL está rodando
psql -U servicehub -d service_hub -h localhost
```

### Porta 8000 já está em uso

```bash
# Encontrar e matar o processo
lsof -i :8000
kill -9 <PID>
```

### Frontend não conecta com backend

- Verificar se `NEXT_PUBLIC_API_URL` está correto
- Verificar CORS no backend
- Verificar se backend está rodando

## Suporte

Para dúvidas ou problemas, abra uma issue no repositório.
