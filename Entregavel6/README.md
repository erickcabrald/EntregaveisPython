# Sistema de Gestão de RH em Python 🐍

Projeto final (Sprint 6) focado na consolidação dos conceitos de Programação Orientada a Objetos (POO). Este sistema gerencia funcionários de uma empresa utilizando herança, polimorfismo, encapsulamento e composição.

## 📐 Diagrama de Classes

```mermaid
classDiagram
    class Funcionario {
        <<Abstract>>
        - str _nome
        - float _salario_base
        + str nome
        + float salario_base
        + calcular_remuneracao_total()* float
        + __str__() str
        + __repr__() str
        + __eq__(outro) bool
        + __lt__(outro) bool
    }

    class Desenvolvedor {
        - str _linguagem_principal
        + str linguagem_principal
        + calcular_remuneracao_total() float
        + __str__() str
    }

    class Gerente {
        - float _bonus_cargo
        + float bonus_cargo
        + calcular_remuneracao_total() float
        + __str__() str
    }

    class Departamento {
        - str _nome_departamento
        - list _membros
        + str nome_departamento
        + adicionar_funcionario(Funcionario)
        + processar_folha_pagamento()
    }

    Funcionario <|-- Desenvolvedor : Herança (É UM)
    Funcionario <|-- Gerente : Herança (É UM)
    Departamento o-- Funcionario : Composição (TEM UM)