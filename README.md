# Service Hub - SaaS Marketplace de Técnicos e Serviços

Platforma completa para conectar clientes a técnicos e prestadores de serviço qualificados.

## 🚀 Features

- ✅ **Autenticação JWT** - Segurança robusta com tokens
- ✅ **Perfis de Técnicos** - Cadastro completo com especialidades
- ✅ **Sistema de Categorias** - Organização de serviços
- ✅ **Agendamento** - Marcação com calendário integrado
- ✅ **Avaliações e Reviews** - Sistema de reputação
- ✅ **Chat em Tempo Real** - Comunicação entre usuários
- ✅ **Sistema de Pagamento** - Integração Stripe
- ✅ **Dashboard Admin** - Gerenciamento da plataforma

## 🏗️ Stack Tecnológico

### Frontend
- **Next.js 14** - React framework moderno
- **TypeScript** - Tipagem segura
- **Tailwind CSS** - Estilização utilitária
- **Zustand** - Gerenciamento de estado
- **Axios** - Cliente HTTP
- **Socket.io** - Comunicação em tempo real

### Backend
- **FastAPI** - Framework Python assíncrono
- **SQLAlchemy** - ORM poderoso
- **Pydantic** - Validação de dados
- **PostgreSQL** - Banco de dados robusto
- **Redis** - Cache e sessões
- **Stripe** - Processamento de pagamentos

### DevOps
- **Docker** - Containerização
- **Docker Compose** - Orquestração
- **GitHub Actions** - CI/CD (em progresso)

## 📋 Quick Start

### Com Docker Compose (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/amdremessias/service-hub-copilot.git
cd service-hub-copilot

# Crie o arquivo .env
cp docker.env.example .env

# Inicie os containers
docker-compose up -d

# Acesse
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Instalação Local

Veja [docs/SETUP.md](docs/SETUP.md) para instruções detalhadas.

## 📚 Documentação

- [Setup Guide](docs/SETUP.md) - Instalação e configuração
- [API Documentation](docs/API.md) - Endpoints e schemas
- [Database Schema](docs/DATABASE.md) - Estrutura do banco de dados
- [Contributing Guide](docs/CONTRIBUTING.md) - Como contribuir

## 🗂️ Estrutura do Projeto

```
service-hub-copilot/
├── backend/                    # API FastAPI
│   ├── app/
│   │   ├── api/                # Rotas da API
│   │   ├── models/             # Modelos SQLAlchemy
│   │   ├── schemas/            # Schemas Pydantic
│   │   ├── core/               # Configurações e segurança
│   │   └── main.py             # Aplicação FastAPI
│   ├── requirements.txt         # Dependências Python
│   ├── Dockerfile              # Build do backend
│   └── .env.example            # Variáveis de ambiente
│
├── frontend/                   # Aplicação Next.js
│   ├── src/
│   │   ├── app/                # Rotas Next.js
│   │   ├── components/         # Componentes React
│   │   ├── hooks/              # Custom hooks
│   │   ├── lib/                # Utilitários
│   │   ├── store/              # Estado global (Zustand)
│   │   ├── styles/             # Estilos globais
│   │   └── types/              # Tipos TypeScript
│   ├── package.json            # Dependências Node
│   ├── Dockerfile              # Build do frontend
│   ├── tailwind.config.ts       # Configuração Tailwind
│   └── next.config.ts          # Configuração Next.js
│
├── docs/                       # Documentação
│   ├── SETUP.md                # Guia de instalação
│   ├── API.md                  # Documentação da API
│   ├── DATABASE.md             # Schema do banco
│   └── CONTRIBUTING.md         # Como contribuir
│
├── docker-compose.yml          # Orquestração Docker
├── .gitignore                  # Arquivos ignorados
├── README.md                   # Este arquivo
└── LICENSE.md                  # Licença MIT
```

## 🔑 Variáveis de Ambiente

Veja `.env.example` no backend e frontend para todas as variáveis disponíveis.

### Backend essenciais:
```env
DATABASE_URL=postgresql://user:pass@localhost/service_hub
SECRET_KEY=sua-chave-secreta
STRIPE_SECRET_KEY=sk_test_...
```

### Frontend essenciais:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_...
```

## 🧪 Testes

```bash
# Backend
cd backend
pytest
pytest --cov

# Frontend
cd frontend
npm test
npm run type-check
```

## 📈 Roadmap

- [ ] Autenticação OAuth2 (Google, GitHub)
- [ ] Notificações por email
- [ ] SMS com Twilio
- [ ] Relatórios avançados
- [ ] Mobile app (React Native)
- [ ] Integração com Google Calendar
- [ ] Suporte multilingue
- [ ] Sistema de referência

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](docs/CONTRIBUTING.md) para detalhes.

## 📞 Contato

- 💬 Abra uma issue para bugs ou sugestões
- 📧 Email: contato@servicehub.com
- 🐦 Twitter: @servicehub

## 📄 Licença

Este projeto está sob a licença MIT - veja [LICENSE.md](LICENSE.md) para detalhes.

## ✨ Agradecimentos

Obrigado a todos os contribuidores e mantenedores!

---

**Desenvolvido com ❤️ para conectar técnicos e clientes**
