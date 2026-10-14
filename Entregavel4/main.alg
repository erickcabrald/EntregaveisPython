algoritmo "SistemaProdutos"

var
    nomes: vetor[1..100] de caractere
    categorias: vetor[1..100] de caractere
    precos: vetor[1..100] de real
    i, j, n, opcao: inteiro
    aux_preco, soma, menor, maior: real
    aux_nome, aux_categoria: caractere
    valor: real
    repetida: logico

inicio
    n <- 0

    escreva("Quantidade de produtos: ")
    leia(n)

    para i de 1 ate n faca
        escreva("Nome: ")
        leia(nomes[i])
        escreva("Preco: ")
        leia(precos[i])
        escreva("Categoria: ")
        leia(categorias[i])
    fimpara

    escreva("Preco para filtragem: ")
    leia(valor)

    para i de 1 ate n faca
        se precos[i] > valor entao
            escreval(nomes[i], " - R$ ", precos[i])
        fimse
    fimpara

    // Ordenacao crescente: metodo da bolha
    para i de 1 ate n - 1 faca
        para j de 1 ate n - i faca
            se precos[j] > precos[j + 1] entao
                aux_preco <- precos[j]
                precos[j] <- precos[j + 1]
                precos[j + 1] <- aux_preco

                aux_nome <- nomes[j]
                nomes[j] <- nomes[j + 1]
                nomes[j + 1] <- aux_nome

                aux_categoria <- categorias[j]
                categorias[j] <- categorias[j + 1]
                categorias[j + 1] <- aux_categoria
            fimse
        fimpara
    fimpara

    // Categorias unicas
    escreval("Categorias:")
    para i de 1 ate n faca
        repetida <- falso

        para j de 1 ate i - 1 faca
            se categorias[i] = categorias[j] entao
                repetida <- verdadeiro
            fimse
        fimpara

        se repetida = falso entao
            escreval(categorias[i])
        fimse
    fimpara

    // Estatisticas
    menor <- precos[1]
    maior <- precos[1]
    soma <- 0

    para i de 1 ate n faca
        se precos[i] < menor entao
            menor <- precos[i]
        fimse

        se precos[i] > maior entao
            maior <- precos[i]
        fimse

        soma <- soma + precos[i]
    fimpara

    escreval("Menor preco: R$ ", menor)
    escreval("Maior preco: R$ ", maior)
    escreval("Media: R$ ", soma / n)

    // Relatorio final
    escreval("Relatorio de produtos:")
    para i de 1 ate n faca
        escreval(nomes[i], " - R$ ", precos[i],
                 " - ", categorias[i])
    fimpara

fimalgoritmo