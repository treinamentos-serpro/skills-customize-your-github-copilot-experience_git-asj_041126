# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Escreva testes automatizados para a API de tarefas criada na assignment Building REST APIs with FastAPI. Use `pytest` e `TestClient` para verificar respostas HTTP, comportamento dos endpoints e isolamento entre testes.

## 📝 Tasks

### 🛠️ Preparar o Cliente de Testes

#### Description
Configure o ambiente de testes para enviar requisições à aplicação FastAPI sem iniciar um servidor externo e para reiniciar os dados antes de cada teste.

#### Requirements
O programa concluído deve:

- Instalar `pytest`, `httpx`, `fastapi` e `uvicorn`.
- Renomear o código concluído da API para `main.py` e o arquivo inicial de testes para `test_main.py`.
- Usar `TestClient` com a aplicação definida em `main.py`.
- Usar uma fixture do `pytest` para limpar a lista de tarefas e reiniciar o próximo identificador antes de cada teste.
- Executar os testes com `pytest -q`.

### 🛠️ Testar Operações Bem-Sucedidas

#### Description
Escreva testes para confirmar que a API lista, cria, consulta, atualiza e remove tarefas corretamente.

#### Requirements
O programa concluído deve:

- Confirmar que `GET /tasks` retorna status `200` e uma lista vazia quando não há tarefas.
- Confirmar que `POST /tasks` retorna status `201` e a tarefa criada com um identificador.
- Confirmar que `GET /tasks/{task_id}` retorna a tarefa correspondente.
- Confirmar que `PUT /tasks/{task_id}` retorna a tarefa atualizada com status `200`.
- Confirmar que `DELETE /tasks/{task_id}` remove a tarefa e retorna status `204`.

### 🛠️ Testar Respostas de Erro

#### Description
Verifique como a API responde quando uma tarefa não existe ou quando os dados enviados são inválidos.

#### Requirements
O programa concluído deve:

- Confirmar que consultar, atualizar ou remover uma tarefa inexistente retorna status `404`.
- Confirmar que criar uma tarefa sem o campo obrigatório `title` retorna status `422`.
- Executar os testes em qualquer ordem sem que os dados de um teste afetem os demais.