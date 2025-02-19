import cv2
from google.colab.patches import cv2_imshow  # Importa a função para exibir imagens no Colab

# Função para processar a imagem e reconhecer os rostos
def processar_imagem(imagem_path):
    # Carregar a imagem
    imagem_bgr = cv2.imread(imagem_path)
    imagem_gray = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2GRAY)

    # Carregar o classificador Haar para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Inicializar uma lista para os nomes das pessoas
    face_names = [f'#{i+1}' for i in range(len(faces))]

    # Desenhar as caixas ao redor dos rostos e os rótulos
    for (x, y, w, h), name in zip(faces, face_names):
        # Desenhar o retângulo ao redor do rosto
        cv2.rectangle(imagem_bgr, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        # Ajustar o tamanho da fonte baseado na largura do rosto
        font_scale = w / 100  # Ajuste esse valor para mais ou menos conforme necessário
        
        # Definir um tamanho mínimo de fonte (por exemplo, 0.8)
        font_scale = max(font_scale, 0.8)  # Garante que a fonte não fique menor que 0.8

        font = cv2.FONT_HERSHEY_DUPLEX
        
        # Desenhar a caixa de fundo para o nome
        cv2.rectangle(imagem_bgr, (x, y - 35), (x + w, y), (0, 0, 255), cv2.FILLED)
        
        # Desenhar o texto com tamanho ajustado
        cv2.putText(imagem_bgr, name, (x + 6, y - 6), font, font_scale, (255, 255, 255), 1)

    # Exibir a imagem com os rostos detectados e os rótulos
    cv2_imshow(imagem_bgr)  # Usa cv2_imshow ao invés de cv2.imshow
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Solicitar o caminho da imagem ao usuário
imagem_path = input("Digite o caminho da imagem que deseja processar: ")
processar_imagem(imagem_path)
