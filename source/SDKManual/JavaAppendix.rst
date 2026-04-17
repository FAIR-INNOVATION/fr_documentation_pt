Apêndice
=================

.. toctree::
    :maxdepth: 5

Download do Código Fonte
------------------------------------------------

Na documentação FAIRINO (https://fairino-doc-pt.readthedocs.io/latest/), encontre o módulo "Download de Materiais", clique no botão "Java SDK" e, na página à direita, clique em "FAIRINOJavaSDK" e aguarde o download ser concluído pelo navegador.

.. image:: image/019.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑1 Download do código fonte do Java SDK

Descompacte o pacote compactado. O diretório de arquivos é mostrado abaixo, onde:

fairino_Java_SDK_maven: código fonte (.java) e arquivos de biblioteca (.jar) compilados no ambiente Windows;

.. image:: image/020.png
   :width: 4in
   :align: center

.. centered:: Figura 16.1‑2 Diretório de arquivos do Java SDK

Acesse a pasta fairino_Java_SDK_maven, que contém os diretórios mostrados na figura, onde:

- lib: arquivos jar de dependência usados no código fonte;
- src: arquivos de código fonte do Java SDK;
- target: arquivos de biblioteca (.jar) gerados a partir do código fonte do Java SDK;

.. image:: image/021.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑3 Diretório de código fonte e arquivos de biblioteca do Java SDK

Compilação do Código Fonte no Windows
-------------------------------------------------------------
① Instalar e configurar a ferramenta de build — Maven

Site para download e instalação do Maven: Welcome to Apache Maven – Maven

Após a instalação e configuração, conforme mostrado abaixo, a saída de maven --version no terminal exibirá as seguintes informações

.. image:: image/022.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑1 Instalação e configuração do Maven

② Abra o terminal no diretório do código fonte do Java SDK e digite mvn package para gerar o arquivo de biblioteca (.jar),

.. image:: image/023.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑2 Compilação do Java SDK para arquivo de biblioteca

③ No diretório do código fonte, localize a pasta "target" e dentro dela encontre os arquivos fairino-jar-with-dependencies.jar e fairino.jar gerados pela compilação, conforme mostrado na figura

.. image:: image/024.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑3 Arquivos jar gerados

④ Ao usar o Java SDK do robô colaborativo, vá ao IDEA, clique sequencialmente em File -> Project Structure -> Libraries, adicione o arquivo .jar gerado na etapa anterior e use import fairino.*; no arquivo para utilizar o arquivo .jar gerado.