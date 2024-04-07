import pandas as pd

# Classe que representa um filme
class Filme: 
    def __init__(self, id, nome, genero, ano):
        self.id = id  
        self.nome = nome  
        self.genero = genero  
        self.ano = ano

    def get_descricao_filme(self):
        return f"ID: {self.id}, Nome: {self.nome}, Gênero: {self.genero}, Ano: {self.ano}"
    
# Classe que representa um catálogo com métodos que permitem gerenciar uma lista de objetos
class Catalogo:
    def __init__(self, titulo, arquivo_csv):
        self.titulo = titulo
        self.arquivo_csv = arquivo_csv
        self.filmes = []  # Lista para armazenar os objetos Filme
        self.ids_existentes = set()  # Conjunto para armazenar IDs existentes
        self.carregar_do_csv()  # Carregar dados do arquivo CSV ao inicializar

    # Método responsável por incluir um filme (objeto) no catálogo (csv)
    def incluir_filme(self, filme):
        # Gera automaticamente um novo ID para cada objeto filme
        ids_filmes_existem = [int(f.id) for f in self.filmes if pd.notna(f.id)]
        novo_id = max(ids_filmes_existem, default=0) + 1
        id_filme = str(novo_id)  # Converte para string
        print(f"ID do filme não fornecido. Gerado automaticamente: {id_filme}")
        # Verifica se o ID do filme já existe no catálogo
        if id_filme in self.ids_existentes:
            print(f"Erro: Já existe um filme com o ID '{id_filme}' no catálogo.")
            return
        # Verifica se o ano do filme é um número inteiro
        try:
            ano_filme = int(filme.ano)
        except ValueError:
            print(f"Erro: Ano do filme '{filme.ano}' não é um número inteiro.")
            return
        # Cria um novo objeto Filme com ID gerado automaticamente
        novo_filme = Filme(id_filme, filme.nome, filme.genero, filme.ano)
        self.filmes.append(novo_filme)  # Adiciona o objeto na lista
        self.ids_existentes.add(id_filme)  # Adiciona o ID ao conjunto
        print(f"Filme '{filme.nome}' adicionado ao catálogo com ID {id_filme}.")
        self.salvar_no_csv()  # Chama o método e salva os dados no arquivo CSV após adicionar um filme.  

    # Método responsável por mostrar o catálogo    
    def mostrar_catalago(self):
        print("Filmes no Catálogo:")
        for filme in self.filmes:
            print(filme.get_descricao_filme())
    
    # Método responsável por excluir um filme do catálogo
    def excluir_filme(self, id_filme):
        # Verifica se o ID do filme a ser excluído é um número inteiro
        try:
            id_filme = int(id_filme)
        except ValueError:
            print(f"Erro: ID do filme '{id_filme}' não é um número inteiro.")
            return

        # Verifica se o filme existe
        filme_encontrado = None  # Inicializa uma variável sem valor
        for filme in self.filmes:  # Itera sobre a lista
            if pd.notna(filme.id) and filme.id == id_filme:  # Verifica se o id não é NaN e se é o mesmo que estamos procurando
                filme_encontrado = filme  # A variável filme_encontrado passa a ter o valor de filme
                break

        if filme_encontrado:
            self.filmes.remove(filme_encontrado)  # O objeto filme é removido da lista
            self.ids_existentes.remove(id_filme)  # Remover o ID como número inteiro
            self.salvar_no_csv()  # Exporta a informação para o csv.
            print(f"Filme com ID {id_filme} removido do catálogo.")
        else:
            print(f"Erro: Filme com ID {id_filme} não encontrado no catálogo.")

    # Método responsável por salvar os dados do catálogo no arquivo CSV
    def salvar_no_csv(self):
        dados = {'id': [], 'nome': [], 'genero': [], 'ano': []}  # Dicionário com quatro listas vazias para armazenar os dados dos filmes
        for filme in self.filmes:
            dados['id'].append(filme.id)
            dados['nome'].append(filme.nome)
            dados['genero'].append(filme.genero)
            dados['ano'].append(filme.ano)

        df_atualizado = pd.DataFrame(dados)  # O dicionário de dados é convertido em DataFrame
        # Remove linhas duplicadas e salva no arquivo CSV 
        df_atualizado.drop_duplicates(inplace=True)  # Remove linhas duplicadas
        df_atualizado.to_csv(self.arquivo_csv, index=False)  # Escreve os dados do DataFrame no arquivo CSV
        print(f"Dados salvos em {self.arquivo_csv}.")

    # Método responsável por importar os dados do arquivo CSV para o catálogo
    def carregar_do_csv(self):
        try:
            df = pd.read_csv(self.arquivo_csv)  # O arquivo CSV é lido e armazenado em um DataFrame
            df.drop_duplicates(inplace=True)  # Remove linhas duplicadas
            # Limpar os dados existentes antes de carregar novos dados
            self.filmes = []
            self.ids_existentes = set()

            for index, row in df.iterrows():  # Itera sobre cada linha do DataFrame
                if pd.notna(row['id']) and row['id'] != 'nan':  # Verifica se o valor na coluna 'id' não é NaN
                    id_filme = int(row['id'])  # Converte o ID para inteiro
                    novo_filme = Filme(id_filme, row['nome'], row['genero'], row['ano'])  # Cria um novo objeto Filme
                    self.filmes.append(novo_filme)  # Adiciona o filme à lista
                    self.ids_existentes.add(id_filme)  # Adicionar o ID ao conjunto

            print(f"Dados carregados de {self.arquivo_csv}.")
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_csv} não encontrado. Criando um novo arquivo.")
            self.salvar_no_csv()  # Se o arquivo não existir, cria um novo
