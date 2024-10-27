import pandas as pd

director_mapping_path = '/dataset/diretores.xlsx'
genre_mapping_path = '/dataset/generos.xlsx'
imdb_top_path = '/dataset/imdb_top_1000.xlsx'

director_mapping_df = pd.read_excel(director_mapping_path)
genre_mapping_df = pd.read_excel(genre_mapping_path)
imdb_top_df = pd.read_excel(imdb_top_path)

director_mapping_df.head(), genre_mapping_df.head(), imdb_top_df.head()

imdb_top_df = imdb_top_df.merge(director_mapping_df, on='Director', how='left')

genre_mapping_dict = dict(zip(genre_mapping_df['Genre'], genre_mapping_df['Genre_ID']))

imdb_top_df['Genre_IDs'] = imdb_top_df['Genre'].apply(
    lambda x: ', '.join(str(genre_mapping_dict[genre.strip()]) for genre in x.split(','))
)

imdb_top_df = imdb_top_df.drop(columns=['Director', 'Genre']).rename(columns={'Director_ID': 'Director_ID', 'Genre_IDs': 'Genre_IDs'})

imdb_output_path = '/dataset/imdb.xlsx'
imdb_top_df.to_excel(imdb_output_path, index=False)

imdb_output_path

