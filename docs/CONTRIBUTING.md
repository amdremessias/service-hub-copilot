# Contributing Guide

## Como Contribuir

Todas as contribuições são bem-vindas! Siga estes passos:

### 1. Fork o Repositório

Clique no botão "Fork" no GitHub

### 2. Clone Seu Fork

```bash
git clone https://github.com/seu-usuario/service-hub-copilot.git
cd service-hub-copilot
```

### 3. Crie uma Branch para Sua Feature

```bash
git checkout -b feature/sua-feature
# ou
git checkout -b fix/seu-bug
```

### 4. Faça Suas Mudanças

- Mantenha o código limpo e bem documentado
- Siga o estilo de código do projeto
- Adicione testes para novas funcionalidades

### 5. Commit Suas Mudanças

```bash
git add .
git commit -m "Mensagem clara descrevendo a mudança"
```

### 6. Push para Sua Branch

```bash
git push origin feature/sua-feature
```

### 7. Abra um Pull Request

Vá para o repositório no GitHub e clique em "New Pull Request"

## Convenções

### Commits

Use mensagens claras e descritivas:

```
feat: Adiciona novo endpoint de agendamento
fix: Corrige erro de validação de email
docs: Atualiza documentação da API
test: Adiciona testes para autenticação
```

### Branches

- `main`: Produção
- `dev`: Desenvolvimento
- `feature/*`: Novas funcionalidades
- `fix/*`: Correções de bugs
- `docs/*`: Documentação

### Code Style

**Python:**
- Siga PEP 8
- Use type hints
- Máximo 100 caracteres por linha

**TypeScript/JavaScript:**
- Use Prettier para formatação
- Use ESLint
- Máximo 80 caracteres por linha

## Testes

Antes de fazer um pull request:

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

## Reportando Bugs

Ao reportar um bug, inclua:

1. Descrição clara do problema
2. Steps para reproduzir
3. Comportamento esperado
4. Comportamento atual
5. Screenshots (se aplicável)
6. Sua versão do SO e navegador

## Sugestões de Features

Para sugerir uma feature:

1. Abra uma issue
2. Descreva a feature em detalhes
3. Explique por que seria útil
4. Liste exemplos de implementação

## Código de Conduta

- Seja respeitoso com os outros contribuidores
- Não há spam, abuso ou conteúdo ofensivo
- Trabalhe juntos para resolver conflitos

## Dúvidas?

Abra uma issue ou entre em contato com os mantenedores.

Obrigado por contribuir! 🎉
