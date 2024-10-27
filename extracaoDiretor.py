import pandas as pd

director_file_path = '/dataset/diretor.xlsx'
director_df = pd.read_excel(director_file_path)
director_df.head()
director_df['Director_ID'] = director_df['Director'].factorize()[0] + 1

director_df = director_df[['Director_ID', 'Director']].drop_duplicates().reset_index(drop=True)

director_output_path = '/dataset/diretores.xlsx'
director_df.to_excel(director_output_path, index=False)

