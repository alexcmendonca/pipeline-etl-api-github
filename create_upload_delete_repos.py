from manipula_repos import ManipulaRepositorios

# instanciando um objeto
novo_repo = ManipulaRepositorios('alexcmendonca')

# criando repositório
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

# adicionando arquivos salvos no repositorio criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')

# deletando repositório
nome_repo = 'meu-projeto'
novo_repo.delete_repo(nome_repo)