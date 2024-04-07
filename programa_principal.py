# impotação das classes através do módulo classes_filmes
from classes_filmes2 import Filme, Catalogo

# função para exibir as opções de escolha do utilizador
def exibir_menu():
    print("\nGerenciar Lista de Filmes:")
    print("1. Adicionar Filme")
    print("2. Excluir Filme")
    print("3. Mostrar Catálogo")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    return escolha

# Programa principal
def main():
    # Define o nome do arquivo CSV onde os dados dos filmes são armazenados
    # Este arquivo será usado para carregar os dados do catálogo de filmes e salvar as alterações feitas pelo usuário.
    arquivo_csv = 'filmes.csv'
    # Cria um objeto da classe Catalogo para gerenciar os filmes
    # O objeto é inicializado com o título "FilmesCatalogo" e o nome do arquivo CSV definido acima.
    catalogo_filmes = Catalogo("FilmesCatalogo", arquivo_csv)

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            # Solicitar detalhes do filme ao utilizador
            ano_filme = input("Digite o ano de lançamento do filme: ")
            try:
                ano_filme = int(ano_filme)
            except ValueError:
                print("Erro: Ano do filme deve ser um número inteiro.")
                continue

            nome_filme = input("Digite o nome do filme: ")
            genero_filme = input("Digite o gênero do filme: ")

            # Cria um objeto Filme com os atributos fornecidos pelo utilizador
            # None representa o id que será gerado automaticamente
            novo_filme = Filme(None, nome_filme, genero_filme, ano_filme)

            # O Objeto passa pelo método incluir filme no catálogo.
            catalogo_filmes.incluir_filme(novo_filme) 

        elif escolha == '2':
            # Solicita o ID do filme a ser excluído
            id_filme_excluir = input("Digite o ID do filme a ser excluído: ")
            catalogo_filmes.excluir_filme(id_filme_excluir)

        elif escolha == '3':
             catalogo_filmes.mostrar_catalago()

        elif escolha == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1-4).")

if __name__ == "__main__":
    main()
