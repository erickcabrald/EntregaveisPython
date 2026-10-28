from abc import ABC, abstractmethod

class Funcionario(ABC):
    """Classe abstrata que representa um funcionário genérico."""
    
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or len(valor.strip()) < 3:
            raise ValueError("O nome deve conter pelo menos 3 caracteres.")
        self._nome = valor.title()

    @property
    def salario_base(self) -> float:
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor: float):
        if valor < 1320.0:
            raise ValueError("O salário base não pode ser menor que o salário mínimo (R$ 1320.00).")
        self._salario_base = valor

    @abstractmethod
    def calcular_remuneracao_total(self) -> float:
        """Método abstrato para calcular a remuneração total do funcionário."""
        pass

    def __str__(self) -> str:
        return f"{self.nome} - Salário Base: R${self.salario_base:.2f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome='{self.nome}', salario_base={self.salario_base})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Funcionario):
            return NotImplemented
        return self.salario_base == outro.salario_base

    def __lt__(self, outro: object) -> bool:
        if not isinstance(outro, Funcionario):
            return NotImplemented
        return self.salario_base < outro.salario_base


class Desenvolvedor(Funcionario):
    """Classe que representa um desenvolvedor, herda de Funcionario."""
    
    def __init__(self, nome: str, salario_base: float, linguagem_principal: str):
        super().__init__(nome, salario_base)
        self.linguagem_principal = linguagem_principal

    @property
    def linguagem_principal(self) -> str:
        return self._linguagem_principal

    @linguagem_principal.setter
    def linguagem_principal(self, valor: str):
        if not valor.strip():
            raise ValueError("A linguagem de programação não pode ficar em branco.")
        self._linguagem_principal = valor

    def calcular_remuneracao_total(self) -> float:
        """Polimorfismo: Devs recebem 10% de adicional por produtividade técnica."""
        return self.salario_base * 1.10

    def __str__(self) -> str:
        return f"[Dev] {super().__str__()} | Linguagem: {self.linguagem_principal}"


class Gerente(Funcionario):
    """Classe que representa um gerente, herda de Funcionario."""
    
    def __init__(self, nome: str, salario_base: float, bonus_cargo: float):
        super().__init__(nome, salario_base)
        self.bonus_cargo = bonus_cargo

    @property
    def bonus_cargo(self) -> float:
        return self._bonus_cargo

    @bonus_cargo.setter
    def bonus_cargo(self, valor: float):
        if valor < 0:
            raise ValueError("O bônus do cargo não pode ser negativo.")
        self._bonus_cargo = valor

    def calcular_remuneracao_total(self) -> float:
        """Polimorfismo: Gerentes recebem o salário base + bônus fixo."""
        return self.salario_base + self.bonus_cargo

    def __str__(self) -> str:
        return f"[Gerente] {super().__str__()} | Bônus: R${self.bonus_cargo:.2f}"


class Departamento:
    """Classe que utiliza composição para gerenciar funcionários."""
    
    def __init__(self, nome_departamento: str, membros: list = None):
        self.nome_departamento = nome_departamento
        # Prevenindo o uso de lista mutável como valor padrão
        self._membros = membros if membros is not None else []

    @property
    def nome_departamento(self) -> str:
        return self._nome_departamento

    @nome_departamento.setter
    def nome_departamento(self, valor: str):
        if not valor.strip():
            raise ValueError("O nome do departamento é obrigatório.")
        self._nome_departamento = valor

    def adicionar_funcionario(self, funcionario: Funcionario):
        if not isinstance(funcionario, Funcionario):
            raise TypeError("Apenas objetos do tipo Funcionario podem ser adicionados.")
        self._membros.append(funcionario)

    def processar_folha_pagamento(self):
        """Demonstra o Polimorfismo iterando sobre os membros."""
        print(f"\n--- Folha de Pagamento: Departamento {self.nome_departamento} ---")
        total = 0
        for membro in self._membros:
            pagamento = membro.calcular_remuneracao_total()
            total += pagamento
            print(f"{membro.nome} vai receber: R${pagamento:.2f}")
        print(f"Total da Folha: R${total:.2f}\n")


if __name__ == "__main__":
    print("--- Testes de Validação com Try/Except ---")
    try:
        dev_invalido = Desenvolvedor("Ana", 1000.0, "Python") # Vai falhar (salário < 1320)
    except ValueError as e:
        print(f"Erro capturado na criação: {e}")

    try:
        dev_invalido_2 = Desenvolvedor("A", 2000.0, "Java") # Vai falhar (nome curto)
    except ValueError as e:
        print(f"Erro capturado na criação: {e}")

    # Criação de 10 instâncias válidas para a demonstração
    ti = Departamento("Tecnologia da Informação")
    
    dev1 = Desenvolvedor("Carlos Silva", 5000.0, "Python")
    dev2 = Desenvolvedor("Mariana Costa", 6500.0, "TypeScript")
    dev3 = Desenvolvedor("João Souza", 4500.0, "Java")
    dev4 = Desenvolvedor("Ana Oliveira", 7000.0, "Go")
    dev5 = Desenvolvedor("Pedro Mendes", 4000.0, "C#")
    dev6 = Desenvolvedor("Lucas Almeida", 5500.0, "Rust")
    dev7 = Desenvolvedor("Julia Ferreira", 6200.0, "Python")
    dev8 = Desenvolvedor("Beatriz Gomes", 4800.0, "JavaScript")
    gerente1 = Gerente("Roberto Carvalho", 10000.0, 3000.0)
    gerente2 = Gerente("Fernanda Lima", 12000.0, 4500.0)

    # Demonstrando Composição
    for f in [dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, gerente1, gerente2]:
        ti.adicionar_funcionario(f)

    # Polimorfismo na prática
    ti.processar_folha_pagamento()

    print("--- Testes de Dunder Methods ---")
    print(f"Representação (__repr__): {repr(dev1)}")
    print(f"Comparação de Igualdade (__eq__): dev1 == dev2? {dev1 == dev2}")
    print(f"Comparação de Tamanho (__lt__): dev5 é menor que dev1 (salário)? {dev5 < dev1}")