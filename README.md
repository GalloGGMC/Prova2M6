# Prova 2 do Módulo 6

- Aluno: Gabriel Gallo Menequini Coutinho

## Instruções para a execução:

- Clone o repositório em sua máquina
- Abra o diretório no ambiente de execução preferido
- Crie um terminal
- Execute os seguintes comandos em ordem:
  - "python -m venv venv" 
  - "venv\Scripts\activate" 
  - "pip install requirements.txt"
  - "python haarModel.py"
  
## Perguntas:

### 1) Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

O método escolhido foi o Haar Cascade que funciona definindo uma série de kernels que serão passados pela imagem para a detecção de padrões em áreas retângulares na imagem. Assim, o método precisa de pelo menos um arquivo de definição dos padrões a serem buscados e ao definir os padrões, percorremos cada imagem utilizando uma convolução com os kernels definidos e com base na semelhança com e a precisão do modelo é retornado na imagem onde o modelo adiciona um indicador caso o padrão exista na imagem. 

## 2) Classifique os modelo em termos de viabilidade técnica, facilidade de implementação e versatilidade da solução.

- Classificação de viabilidade:
  
  - HAAR Cascade
  - NN Linear
  - CNN
  - Filtros de correlação cruzada
  
**Justificativa:** o HAAR Cascade é um modelo fácil de se utilizar, leve e facilmente modificável. O NN Linear é um pouco mais difícil de utilizar pois deve-se criar o número de camadas e neurônios do modelo antes do treino, contudo, fornece resultados melhores ao possuir um dataset com imagens diferentes, não atentando-se apenas a um padrão.

O CNN é parecido com o NN Linear, porém é mais complexo por adicionar camadas convolucionais, o que em troca oferece mais confiança para a categorização em diferentes casos. Por fim, o modelo de filtros de correlação cruzada é o modelo mais simples da lista, porém, ele é muito limitado aos padrões de busca (templates fornecidos), ainda mais que o HAAR Cascade, desta maneira, acredito que ele seja o modelo menos viável.

----------------------------------------------

- Classificação de facilidade de implementação:
  
  - Filtros de correlação cruzada
  - HAAR Cascade
  - NN Linear
  - CNN
  
**Justificativa:** O modelo de filtros de correlação cruzada é o mais fácil de implementar pois ele consiste apenas em encontrar determinado template na imagem fornecida. Após ele está o HAAR Cascade pois ele possui uma estratégia semelhante de implementação, porém, com um nível de abstração maior e com padrões menos bem definidos.

Depois encontra-se o NN Linear porque ele é um modelo de rede neural, ou seja, possui uma abstração ainda mais intensa e os padrões a serem reconhecidos não são definidos por exemplo, mas por uma função recompensa e uma função risco. Por fim, o CNN é o modelo mais difícil de ser implementado pois ele possui a complexidade do NN Linear além de adicionar camadas convolucionais para o processamento da imagem.

---------------------------------------

- Classificação de versatilidade:
  
  - CNN
  - NN Linear
  - HAAR Cascade
  - Filtros de correlação cruzada

  
**Justificativa:** O CNN possui a maior versatilidade dos modelos pois ele não está restrito nem a templates pré-criados ou a apenas transformações lineares, ajustando-se com base no dataset de treino. O NN Linear encontra-se logo após o CNN pois possui a semelhança de não depender de templates existentes e derivar o padrão dos dados, porém, ele só faz transformações lineares.

O HAAR Cascade encontra-se depois por depender de um template, porém, ele depende de um processamento de imagem com diferentes filtros, diferentemente dos filtros de correlação cruzada que utilizam apenas um tipo de template para processar a imagem e tentar identificar o padrão procurado.

## 3) Classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face:

- Classificação:
  
  - HAAR Cascade
  - Filtros de correlação cruzada
  - CNN
  - NN Linear
  
**Justificativa:** O modelo HAAR Cascade é muito bom em encontrar padrões específicos em imagens além de ter um pouco mais de flexibildade por empregar diferentes kernels de procura, fazendo com que mesmo que todos os sinais experados não sejam encontrados na imagem, o modelo ainda pode conseguir classificar corretamente.

Os filtros de correlação cruzadas é semelhante ao HAAR Cascade ao buscar por um template na imagem, contudo é muito mais restrito pois a identificação é feita comparando a um template, assim, mesmo que a emoção seja a mesma do template, ele não reconhece em algumas instâncias.

O CNN possui um tremendo poder de identificar padrões e classificá-los, contudo, não há exatamente um controle dos padrões que o modelo utilizará para identificar e categorizar, desta maneira, dependendo de um dataset maior, mais tempo de treino e mais processamento, o que reduz a sua viabilidade.

Por último, o NN Linear possui problemas semlhantes ao CNN além de apresentar uma redução na capacidade de identificação por possuir apenas transformações lineares entre camadas, portanto, demorando ainda mais e necessitando de mais tempo de treino.

## 4) Algum dos modelos possui a capacidade de considerar variações de um frame para outro e caso não haja, quais alterações poderiam ser feitas para que isso seja possível?

Na solução apresentada neste repositório, não foi implementado, contudo, com os modelos de rede neural (NN Linear e CNN) seria possível de considerar variações de frame pois podemos, por exemplo, adicionar um input que diz o que foi predito na última propagação.