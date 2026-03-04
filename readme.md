# Projeto Universidade 

Modelagem em Orientação à objetos 
das Entidades Alunos, Cursos e 
Turmas.

## Caso de Uso 
```mermaid
flowchart LR
    Usuario([Secretária])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Tranfererir Alunos))


Usuario --> UC1
Usuario --> UC2
Usuario --> UC3

```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno{
        - Nome
        - Email
        - CPF
        - Telefone
        - Endereço
        - Matricula
        + cadastrar()
        + editar()
        + transferencia()
    }
```

## Dependências
- **VS COD**: IDE(Interface de Desenvolvimento)
- **Mermaid**: Linguagem para confecção de diagramas  em documentos MD (Mark Down)
- **Material Icon Theme**: Tema para colorir as pastas
- **Git Lens**: Interface gráfica  pra o versionamento .git  integrada ao VSCode.

## Diagrama de Sequência - **Cadastro**
```mermaid
sequenceDiagram 
    participant UI as TelaCadastro 
    participant Entidade as Aluno 
    participant DB as MySQL 
    participant Banco as MySQL Server 

    UI ->> Entidade: cria Aluno(...) 
    UI ->> DB: connect() 
    UI ->> Entidade: cadastrar(DB) 
    Entidade ->> DB: execute_query(INSERT) 
    DB ->> Banco: Envia SQL 
    Banco -->> DB: Confirmação 
    DB -->> Entidade: lastrowid 
    UI ->> DB: disconnect()
```
## Diagrama de Sequência - **Listagem**
```mermaid
sequenceDiagram
    participant UI as TelaListagem
    participant Entidade as Aluno
    participant DB as MySQL
    participant Banco as MySQL Server

    UI ->> DB: connect()
    UI ->> Entidade: listar(DB)
    Entidade ->> DB: execute_query(SELECT)
    DB ->> Banco: Envia SQL (SELECT)
    Banco -->> DB: Retorna registros
    DB -->> Entidade: lista de alunos
    Entidade -->> UI: lista de alunos
    UI ->> UI: preencher QTableWidget
    UI ->> DB: disconnect()
```
