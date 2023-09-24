import os
from PIL import Image

def listar_elementos_pasta(caminho):
    itens = []
    for pasta_atual, subpastas, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            itens.append(os.path.join(pasta_atual, arquivo))
    return itens

def recortar_imagens():
    path_datas = "C:/Users/jorge/Desktop/dataset/original/quedas/Fall Detection Dataset UTTEJ/images"
    path_labels = "C:/Users/jorge/Desktop/dataset/original/quedas/Fall Detection Dataset UTTEJ/labels"

    path = [path_datas, path_labels]

    # Recolhe todos os elementos na pasta
    itens = [os.listdir(path_datas), os.listdir(path_labels)]

    # Filtrando apenas por pastas
    Sub = [
        [item for item in itens[0] if os.path.isdir(os.path.join(path_datas, item))],
        [item for item in itens[1] if os.path.isdir(os.path.join(path_labels, item))]
    ]

    path_sub = []
    for i in range(len(Sub)):
        lina = []
        for j in Sub[i]:
            lina.append(path[i] + "/" + j)
        path_sub.append(lina)

    arquivos = []
    for i in range(len(path_sub)):
        lina = []
        for j in path_sub[i]:
            lina.append(listar_elementos_pasta(j))
        arquivos.append(lina)

    for i in range(len(arquivos[0])):  # Pega as pastas das imagens
        for j in arquivos[i]:  # Pega a primeira
            for d in j:
                img_nome = os.path.basename(d).split(".")[0]
                for txt in arquivos[1][i]:
                    txt_name = os.path.basename(txt).split(".")[0]
                    if img_nome == txt_name:
                        imagem = Image.open(d)
                        largura, altura = imagem.size
                        print(largura, altura)
                        with open(txt, "r") as arquivo:
                            # Lê o conteúdo do arquivo
                            conteudo = arquivo.read().split(" ")
                        conteudo = [float(conteudo[0]),
                                    float(conteudo[1]) * largura,
                                    float(conteudo[2]) * largura,
                                    float(conteudo[3]) * altura,
                                    float(conteudo[4]) * altura]
                        print(conteudo)
                        
                        # Recorte manual
                        esquerda = int(conteudo[1])
                        superior = int(conteudo[3])
                        direita = int(conteudo[2])
                        inferior = int(conteudo[4])
                        
                        imagem_cortada = imagem.crop((esquerda, superior, direita, inferior))
                        
                        imagem_cortada.show()
                        j.remove(d)
                        arquivos[1][i].remove(txt)
                        break

if __name__ == "__main__":
    recortar_imagens()
