produto = "Mouse Gamer WIFI"

if "Mouse".lower() in produto.lower():
    print("---> Produto encontrado <---")
else:
    print("---> Produto não encontrado <---")


valores = [20,71, 100, 30]

def dobrar (valor):
    resultado =  valor* 2
    return resultado 
print(dobrar (11))

valores_novos = []
for valor in valores:
    valores_novos.append(dobrar(valor))
print(valores_novos)

alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite um nome que deseja inspecionar: ")
for item in alunos:
    if aluno_procurado.lower() in item.lower():
        print(item)
