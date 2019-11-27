# Exercico 1 - Dicionario
# Escreva programa que leia os dados de cerveja
# Cerveja: Marca, tipo , IBU , ABV , Volume , EBC
# Crie um dicionario para armazenar os dados
# Imprima os dados do dicionario (não dicionario completo)

marca = (input('Informe a marca da cerveja'))
tipo = (input('Informe o Tipo da cerveja'))
ibu = (input('Informe o IBU da cerveja'))
abv = (input('Informe o ABV da cerveja'))
ebc = (input('Informe o EBC da cerveja'))
volume = (input('Informe o Volume da cerveja'))

cerveja = {'Marca':marca , 'Tipo':tipo , 'IBU':ibu , 'ABV':abv , 'EBC':ebc , 'Volume':volume}
print(f"{cerveja['Marca']} - {cerveja['Tipo']} - {cerveja['Volume']} - {cerveja['EBC']} - {cerveja['ABV']} - {cerveja['IBU']} - ")

            