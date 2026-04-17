Informações de Status
=================================

.. toctree:: 
   :maxdepth: 6

Log do Sistema
----------------------------

Ao entrar pela primeira vez na interface “Informações de Status — Log do Sistema”, todos os dados de log do dia são exibidos por padrão.

Os dados de log são classificados por nível, atualmente divididos em: Todos, Erros e Avisos, Configurações Básicas, Configurações de Segurança, Configurações de Periféricos, Operações do Corpo, Programas de Ensinamento, Aplicações de Ferramentas, Configurações do Sistema e Importação/Exportação de Arquivos.

Há uma caixa de pesquisa no canto superior direito da tabela de dados. O usuário pode inserir critérios de filtro para filtrar de acordo com a necessidade. A interface é mostrada abaixo:

.. image:: status/001.png
   :width: 6in
   :align: center

.. centered:: Figura 13.1‑1 Interface de Log do Sistema

Consulta de Status
----------------------------

Uso da Função
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ligue a caixa de controle e conecte o cabo de rede ao PC.
2. Abra um navegador no PC e acesse o endereço alvo 192.168.58.2. Faça login com o nome de usuário admin e senha 123 para entrar na página.
3. Clique no menu “Informações de Status” na barra lateral esquerda e, em seguida, em “Consulta de Status” para entrar na interface de consulta de status, conforme mostrado abaixo.

.. image:: status/002.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑1 Consulta de Status

.. note:: 
   .. image:: status/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Consultar**
   
   Função: Clica para enviar o comando de consulta dos dados do gráfico/trajetória. Representa o estado de não consultado.

.. note:: 
   .. image:: status/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Mover para a Direita**
   
   Função: Clica para adicionar o item selecionado à esquerda aos subitens à direita.

.. note:: 
   .. image:: status/008.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Excluir**
   
   Função: Clica para excluir o subitem selecionado à direita.

.. note:: 
   .. image:: status/009.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Limpar**
   
   Função: Clica para limpar todos os subitens à direita.

4. Selecione a exibição em gráfico, preencha o tempo da forma de onda. Na configuração de parâmetros à esquerda, selecione os parâmetros desejados e clique no botão “Mover para a Direita” para adicioná-los à lista à direita.

.. note:: O tempo da forma de onda pode ser personalizado (10-30s). No máximo 6 parâmetros podem ser selecionados na configuração.

5. Clique no botão “Consultar” para iniciar a consulta. Com base na configuração dos parâmetros, um gráfico de linhas com dados em tempo real será exibido, conforme mostrado abaixo.

.. image:: status/003.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑2 Exibição em Gráfico

Exportação do Gráfico
~~~~~~~~~~~~~~~~~~~~~~~~

1. Clique no título do gráfico para abrir uma caixa de diálogo e modificar o título diretamente, conforme mostrado abaixo.

.. image:: status/004.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑3 Renomear o Título do Gráfico

2. Após clicar com sucesso no botão “Parar Consulta” e interromper a consulta, o botão de download será exibido. Clique em “Download” e o navegador baixará o arquivo do gráfico com o nome do título do gráfico. Conforme mostrado na figura abaixo.

.. image:: status/005.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑4 Exportação do Gráfico

Exibição da Visualização de Dados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Após parar a consulta, clique no botão de visualização de dados no canto superior direito do gráfico, conforme mostrado abaixo.

.. image:: status/010.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑5 Botão de Visualização de Dados

2. Os dados na visualização são mostrados na figura. O conteúdo dos dados suporta cópia.

.. image:: status/011.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑6 Exibição da Visualização de Dados

Filtragem de Dados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Após parar a consulta, insira os valores mínimo/máximo de x/y. O intervalo de dados do gráfico também mudará correspondentemente, conforme mostrado abaixo.

.. image:: status/012.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑7 Interface de Filtragem de Dados

2. Clique no botão “Restaurar”. O intervalo de dados do gráfico retorna ao padrão, conforme mostrado abaixo.

.. image:: status/013.png
   :width: 6in
   :align: center

.. centered:: Figura 13.2‑8 Restauração de Dados