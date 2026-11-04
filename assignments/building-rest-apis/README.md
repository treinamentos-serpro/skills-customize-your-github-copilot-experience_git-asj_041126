# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará métodos HTTP, rotas, validação de dados com modelos Pydantic e respostas de erro.

## 📝 Tasks

### 🛠️ Implementar Rotas de Leitura

#### Description
Implemente os endpoints que permitem listar tarefas e consultar uma tarefa pelo identificador.

#### Requirements
O programa concluído deve:

- Disponibilizar `GET /tasks` para retornar todas as tarefas.
- Disponibilizar `GET /tasks/{task_id}` para retornar a tarefa com o identificador informado.
- Retornar o status HTTP `404` quando o identificador não corresponder a uma tarefa existente.

### 🛠️ Implementar Operações de Criação, Atualização e Remoção

#### Description
Complete a API para permitir que clientes criem, atualizem e removam tarefas.

#### Requirements
O programa concluído deve:

- Disponibilizar `POST /tasks` para criar uma tarefa com título e estado de conclusão, atribuindo um identificador único e retornando o status HTTP `201`.
- Disponibilizar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa existente.
- Disponibilizar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar o status HTTP `404` ao tentar atualizar ou remover uma tarefa inexistente.
- Manter as tarefas em memória durante a execução e permitir explorar e testar os endpoints pela documentação interativa em `/docs`.
- Instalar `fastapi` e `uvicorn`, renomear `starter-code.py` para `main.py` e iniciar a API com `uvicorn main:app --reload`.