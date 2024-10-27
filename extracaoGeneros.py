import pandas as pd

file_path = '/dataset/GENERO.xlsx'
genero_df = pd.read_excel(file_path)

genero_df.head()

genero_df['Genre'] = genero_df['Genre'].str.split(',\s*')

exploded_genre_df = genero_df.explode('Genre').reset_index(drop=True)

exploded_genre_df['Genre_ID'] = exploded_genre_df['Genre'].factorize()[0] + 1

exploded_genre_df = exploded_genre_df[['Genre_ID', 'Genre']].drop_duplicates().reset_index(drop=True)

output_path = '/dataset/generos.xlsx'
exploded_genre_df.to_excel(output_path, index=False)

output_path
