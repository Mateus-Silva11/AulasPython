from Aula_54.Dao.filme_model import FilmeDao

dao = FilmeDao()
filmes = dao.list_all()
for f in filmes:
    print(f)