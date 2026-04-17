Apêndice
=================

.. toctree:: 
    :maxdepth: 5

Download do Código Fonte
------------------------------------------------
Encontre o módulo "Downloads de Materiais" na documentação FAIRINO (https://fairino-doc-pt.readthedocs.io/latest/), clique no botão "C#SDK" e, na página à direita, clique em "FAIRINOC#SDK" e aguarde o download ser concluído no navegador.

.. image:: image/001.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑1 Download do código fonte do SDK C#
    
Baixe e descompacte o SDK C#. A estrutura do diretório do projeto é mostrada abaixo. A pasta `examples` contém exemplos de teste, a pasta `src` contém o SDK C#, `Fairino.sln` é a solução do projeto, e `Dlls` contém os arquivos de biblioteca.

.. image:: image/010.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑2 Exemplo da estrutura de arquivos do SDK C#

Localize o arquivo de solução chamado `fairino.sln`, clique duas vezes para abri-lo. A estrutura de arquivos é mostrada na figura abaixo.

.. image:: image/011.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑3 Exemplo da estrutura de arquivos do projeto no Visual Studio 2022

Compilação do Código Fonte na Plataforma Windows
-----------------------------------------------------

Compilação do SDK C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clique no projeto FRRobot, clique com o botão direito e selecione "Propriedades". Selecione a versão do framework .NET.

.. image:: image/012.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑1 Configurar Propriedades

.. image:: image/013.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑2 Selecionar o framework .NET

.. image:: image/014.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑3 Gerar o projeto FRRobot no modo Release

Ajuste o Visual Studio 2022 para o modo Release e recompile o projeto FRRobot. A biblioteca de link dinâmico (DLL) será gerada na pasta `\bin\Release`.

.. image:: image/015.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑4 Configurar o modo Release

.. image:: image/016.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑5 Recompilar o projeto FRRobot no modo Release

.. image:: image/016.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑6 Gerar a biblioteca de link dinâmico (DLL)

Uso do SDK C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clique com o botão direito no projeto `testFrRobot` e selecione "Definir como Projeto de Inicialização".

.. image:: image/017.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑7 Definir como Projeto de Inicialização
 
A interface de teste do SDK C# é mostrada na figura abaixo.

.. image:: image/018.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑8 Interface de Teste do SDK C#

Precauções
---------------------------------------

Possíveis Problemas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tratamento de Código Atualizado sem Efeito
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Se, após reescrever o código e reiniciar o projeto, o projeto ainda executar o código antigo, considere as seguintes etapas:

Recompile o projeto: Conforme orientado na etapa 3.2, recompile ou atualize a configuração e os arquivos do projeto.

Códigos de Erro
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Quando o valor de retorno é 0, a operação está normal. Se o valor de retorno não for 0, consulte a tabela de códigos de erro.