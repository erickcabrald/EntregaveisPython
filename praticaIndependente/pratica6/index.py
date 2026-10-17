
class Livro:
    """Representa um livro da biblioteca."""

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.autor = autor
        self.disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Usuario:
    """Representa um usuário da biblioteca."""

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Usuário: {self.nome}"

    def __str__(self):
        return self.apresentar()


class Aluno(Usuario):
    """Representa um aluno da biblioteca."""

    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self):
        return f"Aluno: {self.nome} - Matrícula: {self.matricula}"


class Professor(Usuario):
    """Representa um professor da biblioteca."""

    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Professor: {self.nome} - Disciplina: {self.disciplina}"


class Emprestimo:
    """Controla o empréstimo de um livro."""

    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

    def realizar(self):
        if self.livro.disponivel:
            self.livro.disponivel = False
            print(f"Livro '{self.livro.titulo}' emprestado para {self.usuario.nome}.")
        else:
            print("Livro indisponível.")

    def devolver(self):
        self.livro.disponivel = True
        print(f"Livro '{self.livro.titulo}' devolvido.")


livro1 = Livro("Dom Casmurro", "Machado de Assis")
aluno1 = Aluno("Erick", "2026001")
professor1 = Professor("Marcos", "Programação")

print(livro1)
print(aluno1)
print(professor1)

usuarios = [aluno1, professor1]

for usuario in usuarios:
    print(usuario.apresentar())

emprestimo1 = Emprestimo(livro1, aluno1)
emprestimo1.realizar()
emprestimo1.realizar()
emprestimo1.devolver()
emprestimo1.realizar()
