Pontos de Ensinamento
==============================

.. toctree:: 
   :maxdepth: 6

O gerenciamento de ensinamento é dividido em dois modos: "Modo de Sistema" e "Modo de Tabela de Pontos". Isso permite que, ao chamar programas do manipulador, diferentes tabelas de pontos possam ser usadas para implementar diferentes esquemas de detecção, atendendo às necessidades de receitas. Posteriormente, para cada novo equipamento ou produto adicionado, o pacote de dados da tabela de pontos pode ser baixado para o robô através do host, e o pacote de dados da tabela de pontos recém-criado pelo robô também pode ser enviado para o host.

**Modo de Sistema**: Suporta "importar, exportar, excluir, renomear, modificar, sobrescrever, visualizar" o conteúdo dos pontos de ensinamento, bem como movimento passo a passo até o ponto de ensinamento.

.. image:: points/001.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-1 Interface de Gerenciamento de Ensinamento - Modo de Sistema

**Modo de Tabela de Pontos**: Suporta "adicionar, aplicar, renomear, excluir, importar, exportar" tabelas de pontos, "excluir, modificar, visualizar e sobrescrever" o conteúdo dos pontos dentro da tabela de pontos, bem como movimento passo a passo até o ponto de ensinamento.

.. image:: points/002.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-2 Interface de Gerenciamento de Ensinamento - Modo de Tabela de Pontos

O canto superior direito da interface de gerenciamento de ensinamento exibe a barra de operação do corpo do robô. Nesta interface, o usuário pode mover o corpo do robô e, em seguida, realizar operações de sobrescrita de dados dos pontos de ensinamento.

.. image:: points/003.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-3 Interface de Gerenciamento de Ensinamento - Barra de Operação do Corpo do Robô

No canto superior direito dos dados da tabela de pontos de ensinamento, é possível inserir o nome do ponto de ensinamento para pesquisar. Nos dados da tabela de pontos de ensinamento, ao clicar no nome do ponto de ensinamento, ele entra em modo de edição. Insira o nome modificado e clique fora da área do nome do ponto de ensinamento para concluir a modificação.

.. note:: 
   .. image:: points/004.png
      :height: 0.75in
      :align: left

   Nome: **Botão Importar**
   
   Função: Importar arquivo de pontos de ensinamento.

.. note:: 
   .. image:: points/005.png
      :height: 0.75in
      :align: left

   Nome: **Botão Exportar**
   
   Função: Exportar arquivo de pontos de ensinamento.

.. note:: 
   .. image:: points/006.png
      :height: 0.75in
      :align: left

   Nome: **Botão Excluir**
   
   Função: Após selecionar um ou mais pontos de ensinamento e clicar no botão "Excluir" acima da tabela, uma mensagem "Clique novamente no botão excluir para confirmar a exclusão" aparecerá. Após clicar novamente, as informações do(s) ponto(s) serão excluídas.

.. note:: 
   .. image:: points/007.png
      :height: 0.75in
      :align: left

   Nome: **Botão Sobrescrever Ponto**
   
   Função: Clique para sobrescrever o ponto de ensinamento com os dados de posição atuais do robô. Na janela pop-up, selecione "Sincronizar programa de ensinamento".

.. image:: points/008.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-4 Sobrescrever Ponto de Ensinamento

.. note:: 
   .. image:: points/009.png
      :height: 0.75in
      :align: left

   Nome: **Botão Editar**
   
   Função: Clique para confirmar a modificação dos valores x, y, z, rx, ry, rz e v do ponto de ensinamento.

.. important:: 
   Os valores modificados para x, y, z, rx, ry, rz do ponto de ensinamento não devem exceder a área de trabalho do robô.

.. note:: 
   .. image:: points/010.png
      :height: 0.75in
      :align: left

   Nome: **Botão Detalhes**
   
   Função: Clique para visualizar os detalhes do ponto de ensinamento.

.. image:: points/011.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-5 Detalhes do Ponto de Ensinamento

.. note:: 
   .. image:: points/012.png
      :height: 0.75in
      :align: left

   Nome: **Botão Iniciar Execução**
   
   Função: Clique para selecionar o modo de movimento de ponto único e mover o robô para a posição desse ponto. Selecione PTP para movimento ponto a ponto ou Lin para movimento linear.

.. image:: points/013.png
   :width: 6in
   :align: center

.. centered:: Figura 12.1-6 Executar Ponto de Ensinamento