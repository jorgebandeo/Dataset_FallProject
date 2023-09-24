"""
----------------- normalization data set for yolo -----------------
the algorit estracr image and file to contain label map for convert format 
(x1,y1,x2,y2) to (x center, y center, height, width). also conver the name class 
standart for dataset "Person" in 0.

after complit normalization go the code "teste normalization" for evaluation result 

Alert: do not repit the process, or reault in fatal errors at the yolo 

author: Jorge Bandeo

Date of crate: 24/08/2023
Date of modification 24/08/2023
"""


import os
from tqdm import tqdm
import cv2

# Caminho para a pasta com os arquivos de rótulo
folder_path = 'pessoas'

# Caminho para a pasta com as imagens
images_folder_path = 'pessoas'

# Procura por arquivos de texto na pasta e suas subpastas
for root, dirs, files in os.walk(folder_path):
    for file in tqdm(files):
        if file.endswith('.txt'):
            # Caminho completo para o arquivo de texto
            txt_path = os.path.join(root, file)
            # Lê o conteúdo do arquivo de texto
            with open(txt_path, 'r') as f:
                lines = f.readlines()
            # Normaliza as linhas
            new_lines = []
            for line in lines:
                # Substitui "Person" por "0"
                new_line = line.replace('Person', '0')
                # Divide a linha em valores
                values = new_line.split()
                # Obtém o nome do arquivo de imagem correspondente
                image_name = os.path.splitext(file)[0] + '.jpg'
                # Caminho completo para o arquivo de imagem
                image_path = os.path.join(images_folder_path, image_name)
                # Lê a imagem
                image = cv2.imread(image_path)
                # Obtém as dimensões da imagem
                height, width, _ = image.shape
                # cálcula o centro da box 
                x_centro = (float(values[1]) + float(values[3])) /2
                y_centro = (float(values[2]) + float(values[4])) /2
                # Cálcula a atura e larcura da imagem
                width_box = abs(float(values[1]) - float(values[3]))
                height_box = abs(float(values[2]) - float(values[4]))
                # Normaliza as coordenadas da caixa delimitadora
                x_center_normalizado = x_centro / width
                y_center_normalizado = y_centro / height
                largura_normalizada = width_box / width
                altura_normalizada = height_box / height
                # Cria a nova linha com as coordenadas normalizadas da caixa delimitadora
                new_line = f'0 {x_center_normalizado} {y_center_normalizado} {largura_normalizada} {altura_normalizada}\n'
                new_lines.append(new_line)
            # Salva as alterações no arquivo de texto
            with open(txt_path, 'w') as f:
                f.writelines(new_lines)