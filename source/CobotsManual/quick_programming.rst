Programação Rápida do Robô
=====================================

Introdução às Instruções de Movimento Simples
------------------------------------------------------------

**Comando PTP**: Clique no ícone “Ponto a Ponto” para entrar na interface de edição de comandos PTP.

Você pode selecionar o ponto a ser alcançado. A configuração do tempo de transição suave permite que o movimento deste ponto para o próximo seja contínuo. A configuração de deslocamento permite selecionar o deslocamento com base no sistema de coordenadas base ou no sistema de coordenadas da ferramenta, exibindo as configurações de deslocamento x, y, z, rx, ry, rz. O caminho específico do PTP é o caminho ideal planejado automaticamente pelo controlador de movimento. Clique em “Adicionar” e “Aplicar” para salvar esta instrução.

.. image:: teaching_pendant_software/055.png
   :width: 6in
   :align: center

.. centered:: Figura 5.1‑1 Interface do Comando PTP

**Comando Lin**: Clique no ícone “Linear” para entrar na interface de edição de comandos Lin.

A função desta instrução é semelhante à instrução “PTP”, mas o caminho para o ponto alcançado por esta instrução é uma linha reta.

.. image:: teaching_pendant_software/057.png
   :width: 6in
   :align: center

.. centered:: Figura 5.1‑2 Interface do Comando Lin

Operações com Arquivos de Programa
----------------------------------------

Use a barra de ferramentas no topo da árvore de programas para modificá-la.

.. note:: 
   .. image:: coding/006.png
      :height: 0.75in
      :align: left

   Nome: **Abrir**
   
   Função: Abre um arquivo de programa do usuário.

.. note:: 
   .. image:: coding/007.png
      :height: 0.75in
      :align: left

   Nome: **Novo**
   
   Função: Cria um novo arquivo de programa selecionando um modelo.
   
.. note:: 
   .. image:: coding/008.png
      :height: 0.75in
      :align: left

   Nome: **Importar**
   
   Função: Importa um arquivo para a pasta de programas do usuário.

.. note:: 
   .. image:: coding/009.png
      :height: 0.75in
      :align: left

   Nome: **Exportar**
   
   Função: Exporta um arquivo de programa do usuário para o computador local.

.. note:: 
   .. image:: coding/010.png
      :height: 0.75in
      :align: left

   Nome: **Salvar**
   
   Função: Salva o conteúdo editado do arquivo.

.. note:: 
   .. image:: coding/011.png
      :height: 0.75in
      :align: left

   Nome: **Salvar Como**
   
   Função: Renomeia o arquivo e o salva na pasta de programas do usuário ou de modelos.

.. note:: 
   .. image:: coding/012.png
      :height: 0.75in
      :align: left

   Nome: **Copiar**
   
   Função: Copia um nó, permitindo usá-lo em outras operações (por exemplo, colá-lo em outra posição da árvore de programas).

.. note:: 
   .. image:: coding/013.png
      :height: 0.75in
      :align: left

   Nome: **Colar**
   
   Função: Permite colar um nó previamente cortado ou copiado.

.. note:: 
   .. image:: coding/014.png
      :height: 0.75in
      :align: left

   Nome: **Cortar**
   
   Função: Corta um nó, permitindo usá-lo em outras operações (por exemplo, colá-lo em outra posição da árvore de programas).

.. note:: 
   .. image:: coding/015.png
      :height: 0.75in
      :align: left

   Nome: **Excluir**
   
   Função: Exclui um nó da árvore de programas.

.. note:: 
   .. image:: coding/016.png
      :height: 0.75in
      :align: left

   Nome: **Mover para Cima**
   
   Função: Move o nó para cima.

.. note:: 
   .. image:: coding/017.png
      :height: 0.75in
      :align: left

   Nome: **Mover para Baixo**
   
   Função: Move o nó para baixo.

.. note:: 
   .. image:: coding/018.png
      :height: 0.75in
      :align: left

   Nome: **Alternar Modo de Edição**
   
   Função: Alterna entre o modo de árvore de programas e o modo de edição Lua.

Escrevendo e Executando um Programa
----------------------------------------

O lado esquerdo é principalmente para adicionar comandos de programa. Clique no ícone acima de cada palavra-chave para entrar na interface detalhada de adição do comando à direita. As operações para adicionar um comando ao arquivo são divididas em dois tipos principais:

- 1. Abra a instrução relacionada e clique no botão “Aplicar” para adicioná-la ao programa.
- 2. Clique primeiro no botão “Adicionar”. Neste momento, o comando ainda não está salvo no arquivo de programa. É necessário clicar em “Aplicar” para salvá-lo no arquivo.

O segundo método aparece frequentemente quando múltiplas instruções do mesmo tipo são enviadas. Para este tipo de comando, adicionamos a função de botão “Adicionar” e a exibição do conteúdo das instruções já adicionadas. Clicar em “Adicionar” adiciona uma instrução. As instruções já adicionadas são exibidas. Clicar em “Aplicar” salva as instruções adicionadas no arquivo aberto à direita.

Clique no botão “Iniciar” para executar o programa. Clique no botão “Parar” para interromper a execução. Clique no botão “Pausar/Retomar” para pausar ou retomar a execução. Durante a execução do programa, o nó do programa em execução atual é destacado em verde.

No modo manual, clique no primeiro ícone à direita do nó para fazer o robô executar apenas aquela instrução individualmente. O segundo ícone serve para editar o conteúdo do nó.

.. image:: coding/001.png
   :width: 6in
   :align: center

.. centered:: Figura 5.3‑1 Interface da Árvore de Programas