import cv2

# Caminho para a imagem
image_path = 'pessoas/ff950903e4824055.jpg'

# Caminho para o arquivo de texto com as coordenadas normalizadas das caixas delimitadoras
txt_path = 'pessoas/ff950903e4824055.txt'

# Lê a imagem
image = cv2.imread(image_path)

# Obtém as dimensões da imagem
height, width, _ = image.shape

# Lê as coordenadas normalizadas das caixas delimitadoras do arquivo de texto
with open(txt_path, 'r') as f:
    for line in f:
        # Converte a linha em uma lista de valores
        values = line.strip().split()
        # Obtém as coordenadas normalizadas da caixa delimitadora (x_center, y_center, w, h)
        x_center, y_center, w, h = [float(v) for v in values[1:]]
        # Desnormaliza as coordenadas da caixa delimitadora
        x1 = int((x_center + w / 2) * width)
        y1 = int((y_center + h / 2) * height)
        x2 = int((x_center - w / 2) * width)
        y2 = int((y_center - h / 2) * height)
        # Desenha a caixa delimitadora na imagem
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Mostra a imagem com as caixas delimitadoras
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()