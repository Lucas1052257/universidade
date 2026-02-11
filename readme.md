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
