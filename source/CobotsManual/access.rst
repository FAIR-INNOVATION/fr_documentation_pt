WebApp Acesso e Login
===========================

.. toctree:: 
   :maxdepth: 6

Acessar a Interface WebApp
------------------------------------

1. Ligue a caixa de controle e conecte o cabo de rede ao PC;
2. No PC, abra o navegador Chrome e acesse o endereço de destino 192.168.58.2;
3. Insira o nome de usuário e a senha e clique em login para acessar o WebApp.

O nome de usuário inicial é admin e a senha é 123.

.. figure:: teaching_pendant_software/001.png
   :width: 6in
   :align: center

.. centered:: Figura 2.1‑1 Interface de Login

Conhecendo Brevemente a Interface WebApp
--------------------------------------------------------

Após o login bem-sucedido, o sistema entra na “Interface Inicial”, que inclui principalmente:

1. Logotipo da FAIRINO;
2. Botão de recolher/expandir o menu;
3. Barra de menu;
4. Área de controle do robô;
5. Área de status do robô;
6. Robô 3D simulado — operações da cena 3D;
7. Robô 3D simulado — operações do robô;
8. Funções complementares do robô;
9. Status do robô e funções complementares.

Conforme ilustrado no diagrama da interface inicial do sistema abaixo:

.. image:: teaching_pendant_software/002.png
   :align: center
   :width: 6in

.. centered:: Figura 2.2‑1 Diagrama da Interface Inicial do Sistema

Área de Controle
~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/064.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Abrir Programa de Ensinamento**
   
   Função: Abrir o programa de ensinamento para programação textual, programação gráfica e programação por gráfico de nós

.. note:: 
   .. image:: teaching_pendant_software/003.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Habilitar**
   
   Função: Habilitar o robô

.. note:: 
   .. image:: teaching_pendant_software/004.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Iniciar**
   
   Função: Enviar e iniciar a execução do programa de ensinamento

.. note:: 
   .. image:: teaching_pendant_software/005.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Parar**
   
   Função: Parar a execução do programa de ensinamento atual

.. note:: 
   .. image:: teaching_pendant_software/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Pausar/Retomar**
   
   Função: Pausar e retomar o programa de ensinamento atual

.. important::
   O comando de pausa no final do programa não pode ser executado.

Barra de Status
~~~~~~~~~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/011.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Erro de Execução do Robô**
   
   Função: Indica que há um erro na execução do robô; fica oculto quando não há erro.

.. note:: 
   .. image:: teaching_pendant_software/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado do Robô**
   
   Função: Stopped (Parado), Running (Executando), Pause (Pausado), Drag (Arrastar)

.. note:: 
   .. image:: teaching_pendant_software/010.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Coordenadas da Ferramenta, Peça, Eixo Extensor e Número da Carga**
   
   Função: Canto superior esquerdo — número atual do sistema de coordenadas da ferramenta; canto superior direito — número atual do sistema de coordenadas da peça; canto inferior esquerdo — número atual do sistema de coordenadas do eixo extensor; canto inferior direito — número atual da carga.

.. note:: 
   .. image:: teaching_pendant_software/009.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Percentual de Velocidade de Execução**
   
   Função: Velocidade atual do robô ao operar no modo selecionado.

.. note:: 
   .. image:: teaching_pendant_software/012.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Automático**
   
   Função: Modo de operação automática do robô. Ao alternar do modo manual para o automático e especificar a velocidade global, ela é ajustada automaticamente para o valor definido.

.. note:: 
   .. image:: teaching_pendant_software/013.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Manual**
   
   Função: Modo manual do robô para realizar operações de ensinamento.

.. note:: 
   .. image:: teaching_pendant_software/065.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Recolher/Expandir Status do Robô**
   
   Função: Recolher/expandir informações sobre sistema de coordenadas da ferramenta, sistema de coordenadas da peça, sistema de coordenadas do eixo extensor, carga, estado de arrasto do robô, modo local/remoto, estado de conexão, modo BOOT e informações da conta.

Clique no botão recolher para visualizar o conteúdo do status abaixo.

.. note:: 
   .. image:: teaching_pendant_software/008.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas da Ferramenta**
   
   Função: Exibe o número do sistema de coordenadas da ferramenta atualmente em uso.

.. note:: 
   .. image:: teaching_pendant_software/027.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas da Peça**
   
   Função: Exibe o número do sistema de coordenadas da peça atualmente em uso.
   
.. note:: 
   .. image:: teaching_pendant_software/028.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas do Eixo Extensor**
   
   Função: Exibe o número do sistema de coordenadas do eixo extensor atualmente em uso.

.. note:: 
   .. image:: teaching_pendant_software/066.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Carga**
   
   Função: Exibe o peso da carga atual e as coordenadas X, Y, Z do centro de massa.

.. note:: 
   .. image:: teaching_pendant_software/014.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Arrasto do Robô**
   
   Função: Indica que o robô pode ser arrastado atualmente.

.. note:: 
   .. image:: teaching_pendant_software/015.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Arrasto do Robô**
   
   Função: Indica que o robô não pode ser arrastado atualmente.

.. note:: 
   .. image:: teaching_pendant_software/068.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Local do Robô**
   
   Função: Indica que o robô é controlado atualmente pela caixa de controle.

.. note:: 
   .. image:: teaching_pendant_software/067.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Remoto do Robô**
   
   Função: Indica que o robô só pode ser controlado por CLP atualmente.

.. note:: 
   .. image:: teaching_pendant_software/017.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Conexão**
   
   Função: Robô conectado.

.. note:: 
   .. image:: teaching_pendant_software/016.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Desconexão**
   
   Função: Robô desconectado.

.. note:: 
   .. image:: teaching_pendant_software/018.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Informações da Conta**
   
   Função: Exibe o nome de usuário, permissões e opção para sair da conta.