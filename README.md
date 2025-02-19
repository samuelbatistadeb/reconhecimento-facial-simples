# Projeto de Detecção de Rostos com OpenCV

Este projeto utiliza a biblioteca **OpenCV** para realizar a detecção de rostos em imagens, com a finalidade de identificar automaticamente rostos e exibir seus nomes em caixas proporcionais ao tamanho de cada rosto detectado.

## Descrição do Projeto

O sistema processa uma imagem fornecida pelo usuário, detecta todos os rostos presentes nela e exibe uma caixa vermelha ao redor de cada rosto. Além disso, o sistema gera dinamicamente rótulos com nomes como "Pessoa 1", "Pessoa 2", e assim por diante. Os nomes são dimensionados proporcionalmente ao tamanho de cada rosto, garantindo legibilidade e ajuste automático em diferentes cenários.

## Funcionalidades

- **Detecção de rostos:** Utiliza o classificador Haar do OpenCV para identificar rostos frontais em uma imagem.
- **Caixas de destaque:** Desenha caixas vermelhas ao redor de cada rosto detectado.
- **Nomes dinâmicos:** Atribui nomes como "Pessoa 1", "Pessoa 2", etc., para cada rosto detectado e ajusta automaticamente o tamanho da fonte com base na largura do rosto.
- **Proporção da fonte:** A escala da fonte é proporcional ao tamanho do rosto, garantindo legibilidade, independentemente do tamanho do rosto na imagem.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **OpenCV**: Biblioteca para processamento de imagem, utilizada para carregar, modificar e detectar rostos nas imagens.
- **Google Colab**: Ambiente de execução utilizado, com o auxílio da função `cv2_imshow` para exibir as imagens no ambiente Jupyter.

## Instalação

Para rodar este projeto, é necessário instalar a biblioteca **OpenCV** no seu ambiente Python. Para instalar o OpenCV, execute:

```bash
pip install opencv-python
```
Se você estiver usando o Google Colab, a biblioteca já está pré-instalada.

## Como Usar
Faça o download ou clone este repositório em sua máquina local.
Execute o script detectar_rostos.py (ou qualquer outro nome que você atribuir ao arquivo Python).
O script solicitará que você insira o caminho para a imagem que deseja processar.
O script irá processar a imagem e exibirá uma versão dela com os rostos detectados e nomes ajustados.

### Exemplo de execução no código Python
```bash
imagem_path = input("Digite o caminho da imagem que deseja processar: ")
processar_imagem(imagem_path)
```
## Detalhes Técnicos
 - **Classificador Haar**: O projeto utiliza o Haar Cascade Classifier, que é um algoritmo baseado em aprendizado de máquina para a detecção de objetos, neste caso, rostos.
 - **Escalabilidade da Fonte**: O tamanho da fonte para os nomes exibidos é calculado com base na largura de cada rosto detectado. A fonte é dimensionada para garantir que o texto seja legível sem sobrecarregar o espaço ao redor do rosto.
## Considerações
A precisão da detecção pode ser afetada por diversos fatores, como a qualidade da imagem, iluminação e posição dos rostos.
O sistema está configurado para detectar rostos frontais. Caso o rosto esteja de lado ou em ângulos incomuns, a detecção pode falhar.
Este projeto foi desenvolvido para ser executado em ambientes como o Google Colab ou sistemas locais com suporte a OpenCV.
# Contribuições
Contribuições são bem-vindas! Se você encontrar melhorias ou bugs, fique à vontade para abrir issues ou enviar pull requests.

---
**Desenvolvido por**: Samuel Batista  
**Data**: Fevereiro de 2025
