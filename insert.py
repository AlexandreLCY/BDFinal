import pandas as pd

# Carregar todas as planilhas fornecidas para manipulação de dados e preparação para inserção no banco de dados
# Caminho dos arquivos
diretores_path = '/dataset/dataset/diretores.xlsx'
generos_path = '/dataset/generos.xlsx'
imdb_path = '/dataset/imdb.xlsx'

# Carregar os dados dos arquivos Excel
diretores_df = pd.read_excel(diretores_path)
generos_df = pd.read_excel(generos_path)
imdb_df = pd.read_excel(imdb_path)

# Exibir os primeiros registros para confirmar o conteúdo e estrutura
diretores_df.head(), generos_df.head(), imdb_df.head()


# Ajuste para garantir que o campo de avaliação seja convertido apenas se for numérico, evitando erros de tipo

# Reinicializar as listas de comandos SQL
insert_filme = []
insert_genero = []
insert_direcao = []
insert_tem = []
insert_produzido = []

# 1. Inserir dados na tabela Filme
for index, row in imdb_df.iterrows():
    id_filme = index + 1  # Usando o índice como ID do filme, começando em 1
    titulo = str(row['Series_Title']).replace("'", "''") if pd.notna(row['Series_Title']) else ''
    link = str(row['Poster_Link']) if pd.notna(row['Poster_Link']) else ''
    duracao = float(row['Runtime'].split()[0]) if pd.notna(row['Runtime']) else 0.0  # Extrair apenas o número de minutos
    
    # Ajuste no campo de avaliação para evitar erros de tipo
    avaliacao = float(row['IMDB_Rating']) if pd.notna(row['IMDB_Rating']) and isinstance(row['IMDB_Rating'], (int, float)) else 0.0
    sinopse = str(row['Overview']).replace("'", "''") if pd.notna(row['Overview']) else ''

    # Gerar comando SQL para inserir na tabela Filme
    insert_filme.append(f"INSERT INTO Filme (IDfilme, Sinopse, Titulo, Link, Avaliacao, Duracao) "
                        f"VALUES ({id_filme}, '{sinopse}', '{titulo}', '{link}', {avaliacao}, {duracao});")

# 2. Inserir dados na tabela Genero
for index, row in generos_df.iterrows():
    genero_id = row['Genre_ID']
    genero_nome = str(row['Genre']).replace("'", "''") if pd.notna(row['Genre']) else ''
    # Gerar comando SQL para inserir na tabela Genero
    insert_genero.append(f"INSERT INTO Genero (id, Genero) VALUES ({genero_id}, '{genero_nome}');")

# 3. Inserir dados na tabela Direcao
for index, row in diretores_df.iterrows():
    diretor_id = row['Director_ID']
    diretor_nome = str(row['Director']).replace("'", "''") if pd.notna(row['Director']) else ''
    # Gerar comando SQL para inserir na tabela Direcao
    insert_direcao.append(f"INSERT INTO Direcao (ID, Nome) VALUES ({diretor_id}, '{diretor_nome}');")

# 4. Inserir dados na tabela tem (associação entre Filme e Genero)
for index, row in imdb_df.iterrows():
    id_filme = index + 1  # ID do filme
    # Processar os IDs dos gêneros, separando por vírgulas
    genero_ids = str(row['Genre_IDs']).split(',') if pd.notna(row['Genre_IDs']) else []
    for genero_id in genero_ids:
        genero_id = genero_id.strip()  # Remover espaços em branco
        # Gerar comando SQL para inserir na tabela tem
        insert_tem.append(f"INSERT INTO tem (fk_Genero_id, fk_Filme_IDfilme) VALUES ({genero_id}, {id_filme});")

# 5. Inserir dados na tabela produzido (associação entre Direcao e Filme com DataLancamento)
for index, row in imdb_df.iterrows():
    id_filme = index + 1  # ID do filme
    diretor_id = row['Director_ID']
    data_lancamento = str(row['Released_Year']) if pd.notna(row['Released_Year']) else '1900'
    # Gerar comando SQL para inserir na tabela produzido
    insert_produzido.append(f"INSERT INTO produzido (fk_Direcao_ID, fk_Filme_IDfilme, DataLancamento) "
                            f"VALUES ({diretor_id}, {id_filme}, '{data_lancamento}-01-01');")

# Armazenar todos os comandos em um único dicionário para organização
insert_commands = {
    "Filme": insert_filme,
    "Genero": insert_genero,
    "Direcao": insert_direcao,
    "tem": insert_tem,
    "produzido": insert_produzido
}

# Salvar os comandos SQL em um arquivo .sql

# Caminho para o arquivo .sql de saída
output_sql_path = '/dataset/insert_commands.sql'

# Escrever os comandos em um arquivo .sql
with open(output_sql_path, 'w') as file:
    for table, commands in insert_commands.items():
        file.write(f"-- Inserções para a tabela {table}\n")
        for command in commands:
            file.write(command + "\n")
        file.write("\n")


