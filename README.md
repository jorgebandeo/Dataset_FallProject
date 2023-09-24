<h1 align="center"> ~ Dataset FallProject ~ </h1>

Para construir modelos de IA, utilizamos dois grupos de conjuntos de dados. O primeiro é destinado à detecção de pessoas, enquanto o segundo se concentra na classificação de quedas. Vamos descrever, identificar, categorizar esses conjuntos de dados e detalhar os métodos de carregamento. Além disso, neste repositório, forneceremos informações sobre a normalização e sua importância para garantir o uso adequado dos dados.

## 1.1 Detecção de Pessoas

   Para a tarefa de detecção de pessoas, utilizamos o conjunto de dados disponibilizado pelo Google por meio da ferramenta OIDv4. Você pode obter mais informações sobre este conjunto de dados [neste link](https://storage.googleapis.com/openimages/web/index.html). Para baixar imagens com suas respectivas etiquetas que indicam as áreas onde as pessoas estão localizadas e seu estado, siga as etapas abaixo:
   <details>
   <summary><strong> Instalação</strong></summary>
   
   1. Clone este repositório
         ```bash
         git clone https://github.com/EscVM/OIDv4_ToolKit.git
         ```
      
  2. Acesse a pasta clonada
         ```bash
         cd OIDv4_ToolKit
         ```
      
   3. Instale as dependências necessárias
         ```bash
         pip3 install -r requirements.txt
         ```
   </details>
   <details>
   <summary><strong> Download</strong></summary>
   
   Para o processo de download, você precisará especificar que deseja baixar o conjunto de dados "Person". Use os comandos fornecidos no repositório da ferramenta e selecione a função "download all" para baixar todas as imagens relacionadas à classe "pessoa".
   ```Cmd
   python main.py downloader --classes Person --type_csv all
   ```
      
   O comando baixará todos os dados para a pasta "OIDv4_ToolKit\OID\Dataset". Dentro dessa pasta, você encontrará três subdiretórios: "treinamento", "teste" e "validação". Inicialmente, recomendamos o treinamento com um subconjunto limitado de dados. Posteriormente, o próximo modelo usará o conjunto de dados completo e incorporará perturbações ambientais e elétricas para aprimorar a robustez do programa final.
   </details>
   <details>
   <summary><strong>Normalização</strong></summary>
   
   Para normalizar esse conjunto de dados, implementamos três códigos em Python. O primeiro código adiciona rótulos às imagens usando as coordenadas dos pixels para garantir que o conjunto de dados utilize o padrão de localização e tamanho absoluto da imagem para mapear objetos. Em seguida, convertemos esses rótulos para o formato exigido pelo YOLO, que é (x central, y central, altura, largura), onde a altura e a largura se referem às distâncias do centro até as bordas da caixa delimitadora. Essa conversão segue as especificações fornecidas no utilitário e no repositório/site oficial do YOLO, que descrevem o formato do mapeamento e os valores numéricos em porcentagens, em vez de pixels.
      
   Depois de verificar que a conversão foi realizada corretamente, podemos prosseguir com o treinamento.
      
   Os códigos completos e informações detalhadas sobre a transformação estão disponíveis em outro repositório. Você pode encontrar mais informações [neste link](https://1drv.ms/f/s!ArPFsy1SEFgWhIhjBBqUEIBE25SlMw?e=5LFAFo).
</details>


## 1.2 Classificação de Quedas

   Ao lidar com o conjunto de dados de quedas, enfrentamos desafios relacionados à quantidade e qualidade dos dados disponíveis. Embora tenhamos encontrado vários conjuntos de dados que continham informações sobre quedas, muitos deles não continham marcações específicas que indicassem como recortar as pessoas nas imagens. No entanto, encontramos dois conjuntos de dados relevantes que incluíam essas marcações, um composto por vídeos e outro por imagens variadas. Agora, vamos explicar o processo de trabalho com esses dados da mesma forma que fizemos com o conjunto de dados de detecção de pessoas.

<details>
<summary><strong>1.2.1 Conjuntos de Dados Mapeados</strong></summary>

- [UTTEJ KUMAR KANDAGATLA - Conjunto de Dados de Detecção de Quedas](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset)

   Este conjunto de dados valioso e acessível no Kaggle é composto por 485 imagens, cada uma delas acompanhada de suas respectivas marcações e classes relacionadas à detecção de quedas.
      
   **Como fazer o download:**
   1. Acesse o [link de download](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset/download?datasetVersionNumber=1).
   2. Ao clicar no link, você obterá um arquivo compactado no formato .rar contendo todos os arquivos do conjunto de dados.
      
   **Sobre o Conjunto de Dados:**
   Inicialmente, o autor compilou imagens de várias fontes e criou um conjunto de dados personalizado para detecção de quedas. Este conjunto de dados possui dois diretórios principais de imagens: "train" (374 imagens), usado para treinamento, e "Val" (111 imagens), usado para validação. Além disso, há um diretório de rótulos ("labels") que também é dividido em "train" e "Val", contendo arquivos de texto com rótulos para cada imagem correspondente.
      
   Para gerar esses rótulos, o autor utilizou o site makesense.ai, onde inicialmente enviou as imagens e criou rótulos. No contexto deste conjunto de dados, os rótulos incluem categorias como "Queda Detectada", "Caminhada" e "Sentado". Após o upload das imagens, foram criadas caixas delimitadoras (bounding boxes) para as imagens contendo pessoas, e as respectivas categorias foram atribuídas a essas caixas delimitadoras.

- [ImViA - Conjunto de Dados de Detecção de Quedas](https://imvia.u-bourgogne.fr/en/database/fall-detection-dataset-2.html)

   Este conjunto de dados é composto por cinco grupos de vídeos, cada um deles gravado em quartos diferentes. Três dos quartos possuem marcações de mapeamento e classes para as atividades registradas, enquanto os outros dois não possuem essas marcações.
      
   **Como fazer o download:**
   1. Acesse o [link de download](http://imvia.u-bourgogne.fr/database/FallDataset.zip).
   2. Ao clicar no link, você fará o download de um arquivo compactado no formato .rar que contém cinco subpastas, cada uma correspondendo a um dos quartos onde as gravações foram feitas.
      
   **Sobre o Conjunto de Dados:**
   Este conjunto de dados foi criado para avaliar métodos de detecção automática de quedas em gravações de vídeo realistas. Ele inclui 191 vídeos gravados em diversos locais, como casas de idosos e escritórios, capturando atividades diárias normais, incluindo quedas. Cada vídeo é acompanhado de anotações que indicam a posição da queda nas sequências de imagem, além de caixas delimitadoras que identificam a localização do corpo humano em cada quadro. Esse conjunto de dados permite avaliar a eficácia de algoritmos de detecção de quedas em diferentes cenários e condições, sendo uma ferramenta valiosa para a pesquisa em reconhecimento de atividades humanas e segurança, especialmente para o auxílio a idosos.
   </details>

<details>
<summary><strong>1.2.2 Conjuntos de Dados Não Mapeados</strong></summary>


   - [Adhikari, Kripesh, Hamid Bouchachia, and Hammadi Nait-Charif - Conjunto de Dados de Quedas](https://falldataset.com)

      Este conjunto de dados é categorizado como "não mapeado", o que sugere que pode não conter anotações específicas para a localização das pessoas nas imagens. Para baixar este conjunto de dados, siga estas etapas:
      
      1. Acesse o [link de download](https://falldataset.com/data/).
      
      2. Na página, você encontrará várias pastas, cada uma contendo um conjunto de dados de vídeo fragmentado em imagens .png.
      
      3. Você pode fazer o download de cada conjunto de dados individualmente, clicando nas pastas correspondentes. No entanto, observe que esse processo pode ser demorado, pois envolve baixar várias pastas separadamente.
      
      **Sobre o Conjunto de Dados:**
      Este conjunto de dados consiste em imagens RGB e de profundidade capturadas por um sensor Kinect não calibrado, com dimensões de 320x240 pixels. Compreende um total de 21.499 imagens, das quais 16.794 são para treinamento, 3.299 para validação e 2.543 para teste. As imagens foram gravadas em 5 locais diferentes, apresentando 8 ângulos de visão distintos. Cinco participantes executaram atividades cotidianas, incluindo ficar em pé, sentar, deitar, inclinar e rastejar. Cada imagem contém um único participante. O conjunto de treinamento usa imagens de um homem de 32 anos e uma mulher de 28 anos, enquanto o conjunto de teste inclui imagens de dois participantes femininos de 19 e 40 anos e um homem de 50 anos. Todas as imagens estão dispostas em sequência, sem repetição, e cada conjunto inclui versões espelhadas horizontalmente das imagens originais para aumentar a quantidade de dados.

   - [Michal Kępski](http://fenix.ur.edu.pl/mkepski/ds/uf.html)
      Este conjunto de dados, conhecido como "UR Fall Detection Dataset" de Michal Kępski, é uma valiosa fonte de informações para a detecção de quedas e atividades diárias. Contém 70 sequências, compostas por 30 quedas e 40 atividades diárias registradas com a ajuda de câmeras Microsoft Kinect e dados acelerométricos correspondentes. Os detalhes sobre o conjunto de dados são os seguintes:
      
      - 30 sequências de quedas.
      - 40 sequências de atividades diárias.
      - As quedas são gravadas com duas câmeras Microsoft Kinect (câmera 0 e câmera 1).
      - As atividades diárias são gravadas com apenas uma câmera (câmera 0) e um acelerômetro.
      - Os dados do sensor foram coletados usando dispositivos PS Move (60Hz) e x-IMU (256Hz).
      - O conjunto de dados é organizado com sequências de imagens de profundidade e RGB para cada câmera, dados de sincronização e dados brutos do acelerômetro.
      - Cada fluxo de vídeo é armazenado em um arquivo zip separado no formato de sequência de imagens em PNG.
      - Os dados de profundidade são armazenados no formato PNG16 e requerem redimensionamento com a fórmula dada.
      
      Para fazer o download de um conjunto de dados específico, você pode seguir as instruções fornecidas na tabela abaixo, que lista as sequências disponíveis:
      
      | #  | Dados de Profundidade  | Dados RGB | Dados de Sincronização | Dados do Acelerômetro | Vídeo |
      |---|-----------------------|-----------|------------------------|-----------------------|-------|
      | 01 | fall-01-cam0-d.zip   | fall-01-cam1-d.zip | fall-01-cam0-rgb.zip   | fall-01-cam1-rgb.zip | fall-01-data.csv | fall-01-acc.csv | cam0 cam1 |
      | 02 | fall-02-cam0-d.zip   | fall-02-cam1-d.zip | fall-02-cam0-rgb.zip   | fall-02-cam1-rgb.zip | fall-02-data.csv | fall-02-acc.csv | cam0 cam1 |
      | 03 | fall-03-cam0-d.zip   | fall-03-cam1-d.zip | fall-03-cam0-rgb.zip   | fall-03-cam1-rgb.zip | fall-03-data.csv | fall-03-acc.csv | cam0 cam1 |
      | ...  | ... | ... | ... | ... | ... | ... | ... |
      
      Para fazer o download, siga os seguintes passos:
      
      1. Acesse o [link do conjunto de dados](http://fenix.ur.edu.pl/mkepski/ds/uf.html).
      
      2. Explore a lista de sequências disponíveis e identifique aquelas que deseja baixar.
      
      3. Para cada sequência, clique nos links correspondentes para fazer o download dos dados de profundidade, dados RGB, dados de sincronização e dados do acelerômetro, conforme necessário.
      
      4. O download resultará em arquivos zip contendo as informações relevantes para cada sequência.
      </details>

 <details>
   <summary><strong>1.2.3 Normalização de Dados</strong></summary>

Ao realizar a normalização de dados, nos deparamos com várias dificuldades. A classificação se torna eficaz apenas quando nosso objeto de estudo está destacado na imagem. Portanto, é necessário recortar as imagens para conter apenas as pessoas. No entanto, para realizar esse recorte de forma eficaz e rápida, precisamos que as etiquetas (labels) contenham os mapeamentos apropriados. Infelizmente, não conseguimos aplicar esse método em todos os casos; somente nos dados da ImViA foi possível, pois tínhamos descrito adequadamente o método de mapeamento e, após verificação, o recorte mostrou-se eficiente para todos os dados mapeados. Para os demais conjuntos de dados, o trabalho necessário foi mais árduo, exigindo o recorte manual das imagens. Abaixo, descreveremos o processo para cada conjunto de dados:
   <details>
   <summary><strong>UTTEJ KUMAR KANDAGATLA </strong></summary>
   Para tornar o uso deste conjunto de dados possível, tomamos algumas medidas iniciais. Primeiramente, notamos que os nomes das imagens indicavam seu estado, "fall" ou "not fall", o que nos permitiu separá-los facilmente, mesmo quando armazenados em uma única pasta. Além disso, identificamos um problema ao realizar testes com os rótulos mapeados: os recortes resultantes estavam incorretos, pois a pessoa não estava contida na região recortada. Não conseguimos compreender o método de mapeamento utilizado, o que nos levou a realizar os recortes manualmente.

   Para resolver esse problema, desenvolvemos um código que percorre uma pasta principal e suas subpastas, coletando todas as imagens. Em seguida, o código abre cada imagem e permite que o usuário utilize o cursor para recortar a região de interesse. A imagem recortada é então salva em uma nova pasta criada na pasta raiz do conjunto de dados.
   
   É importante destacar que, após efetuar o recorte, não há um botão de "desfazer". Portanto, para voltar atrás, você pode acessar a pasta de [Classificação](https://github.com/jorgebandeo/Dataset_FallProject/tree/main/recorte%20manual) no repositório para acessar as versões originais das imagens ou realizar o processo novamente, caso necessário.
   </details>
   <details>
   <summary><strong>ImViA</strong></summary>
   Para este dataset, inicialmente, cada frame de vídeo foi transformado em uma imagem separada. Posteriormente, foi empregado um arquivo CSV correspondente ao vídeo para recortar as áreas que não incluíam a pessoa. Embora o código específico não tenha sido apresentado devido à sua indisponibilidade, ele segue a seguinte lógica:

   1. Carregue o arquivo CSV que contém informações sobre o vídeo, como coordenadas da pessoa em cada frame.
      Iteração pelos Frames:

   2. Para cada linha no arquivo CSV (cada frame do vídeo):
      Extraindo Coordenadas:

   3. Extraia as coordenadas que representam a posição da pessoa no frame. Isso pode incluir informações sobre o canto superior esquerdo (x1, y1) e o canto inferior direito (x2, y2) do retângulo que envolve a pessoa.
      Recorte da Área da Pessoa:

   4. Utilize as coordenadas extraídas para recortar a área da imagem que contém a pessoa. Isso pode ser feito definindo uma região de interesse (ROI) na imagem original com base nas coordenadas.
      Salvando o Recorte:

   5. Salve o recorte da área da pessoa como uma nova imagem ou frame, que pode ser posteriormente usado no conjunto de dados.
      Repetição:

   6. Repita o processo para todas as linhas do arquivo CSV, processando cada frame do vídeo e extraindo a área da pessoa.
   </details>
   <details>
   <summary><strong>Adhikari, Kripesh, Hamid Bouchachia, and Hammadi Nait-Charif  E Michal Kępski</strong></summary>

   Para os dois conjuntos de dados restantes, a ideia principal é aplicar o modelo obtido para aprimorar esses conjuntos e criar um único conjunto de dados coeso e funcional. Este conjunto resultante será caracterizado por melhorias de qualidade, a partir das quais será possível coletar mais dados relevantes, aproveitando as próprias melhorias feitas anteriormente. Isso criará um ciclo de aprimoramento contínuo, onde o conjunto de dados se torna cada vez mais útil e valioso.
   </details>
Para expandir nossa base de dados, planejamos utilizar os resultados da detecção e classificação para identificar quedas automaticamente. Posteriormente, essas quedas seriam verificadas visualmente por meio de um sistema de revisão, semelhante a um processo de revisão de timelapse em um editor de vídeo convencional. Dessa forma, poderíamos validar os resultados e garantir a qualidade das anotações adicionais.
</details><br>
