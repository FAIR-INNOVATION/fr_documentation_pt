Instalação e Alimentação do Robô
===========================================

.. toctree:: 
   :maxdepth: 6

Instalando o Braço Robótico
----------------------------------

Ao instalar o robô colaborativo em uma base de montagem, use a quantidade correta de parafusos (com resistência não inferior a classe 8.8) para fixar o robô firmemente na base. Recomenda-se o uso de dois furos de pino na base, combinados com pinos, para posicionar o robô. Isso aumenta a precisão da instalação e evita o movimento do robô devido a colisões. Quando o robô tem altos requisitos de precisão de operação, certifique-se de adicionar pinos para posicioná-lo.

.. centered:: Tabela 1.1-1 Padrões das Peças de Instalação do Robô

.. list-table::
   :widths: 80 50 50 50
   :header-rows: 0
   :align: center

   * - **Modelo do Robô Colaborativo**
     - **Parafuso**
     - **Torque do Parafuso**
     - **Especificação do Furo do Pino**

   * - FR3
     - 4 parafusos M6
     - ≥10 Nm
     - φ5mm

   * - FR3-WMS
     - 4 parafusos M6
     - ≥10 Nm
     - φ5mm

   * - FR3-WML
     - 4 parafusos M6
     - ≥10 Nm
     - φ5mm

   * - FR3-C
     - 4 parafusos M6
     - ≥10 Nm
     - φ5mm

   * - FR5-C
     - 4 parafusos M6
     - ≥10Nm
     - φ5mm
   
   * - FR5
     - 4 parafusos M8
     - ≥20 Nm
     - φ8mm

   * - FR10
     - 4 parafusos M8
     - ≥25 Nm
     - φ8mm

   * - FR16
     - 4 parafusos M8
     - ≥25 Nm
     - φ8mm

   * - FR20
     - 6 parafusos M10
     - ≥45 Nm
     - φ8mm

   * - FR30
     - 6 parafusos M10
     - ≥45 Nm
     - φ8mm

   * - FR30L
     - 6 parafusos M10
     - ≥45 Nm
     - φ8mm

.. important:: 
   Recomenda-se que a base de montagem do robô atenda aos seguintes requisitos para garantir uma instalação firme e estável:
   
   (1) A base de montagem do robô deve ser suficientemente robusta e ter capacidade de carga adequada. Deve ser capaz de suportar pelo menos 5 vezes o peso do robô e pelo menos 10 vezes o torque do eixo 1.

   (2) A superfície da base de montagem do robô deve ser plana para garantir contato firme com a superfície de montagem do robô.

   (3) A base de montagem do robô deve ser rígida o suficiente e firmemente fixada para não ressoar com o robô.

   (4) Quando o robô e outros componentes se movem simultaneamente, a base de montagem deve ser isolada de outros componentes móveis. Não os fixe juntos para evitar interferência de vibração durante o movimento.

   (5) Se o robô estiver montado em uma plataforma móvel ou eixo externo, a aceleração da plataforma móvel ou eixo externo deve ser a mais baixa possível.

Conectando o Painel de Controle
---------------------------------------

Esta série de robôs pode ser configurada com três tipos diferentes de painéis de controle quanto à entrada de energia. Consulte a placa de identificação do painel de controle para informações detalhadas sobre a entrada de energia. O robô requer aterramento elétrico. As conexões externas do sistema de controle do manipulador usam conectores plugáveis para instalação rápida.

A. 30-60 VCC
B. 176-264 VCA~50-60 Hz
C. 100-240 VCA~50-60 Hz

.. note:: Os painéis de controle com entrada CA têm duas versões: uma de tensão estreita e outra de ampla tensão. Os terminais de fiação e a aparência dos painéis de controle são idênticos. Eles não podem ser diferenciados apenas pela aparência. Por favor, verifique a placa de identificação do painel de controle e confirme antes de ligar.

O painel de fiação do robô colaborativo é mostrado na figura abaixo:

.. image:: installation/037.png
   :width: 6in
   :align: center

.. centered:: Figura 1.2-1 Painel de Fiação do Painel de Controle

A interface do painel de botões é, por padrão, a porta de controle do painel de ensinamento, com o endereço IP 192.168.58.2. Use um cabo de rede para conectar a interface do painel de botões a um computador. Defina o endereço IP do computador para 192.168.58.10 ou para o mesmo segmento de rede. Abra o navegador Google Chrome e digite 192.168.58.2 para acessar a página do painel de ensinamento.

Conhecendo o Painel de Botões e o LED da Extremidade
---------------------------------------------------------------

Painel de Botões
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Painel de Botões 60 (POE)(BX01)
+++++++++++++++++++++++++++++++++++++++

.. figure:: installation/058.png
   :align: center
   :width: 6in

.. centered:: Figura 1.3-1 Painel de Botões 60 (POE)

Painel de Botões 60 (POE)(BX02)-V1.0
++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: installation/059.png
   :width: 6in
   :align: center

.. centered:: Figura 1.3-2 Painel de Fiação do Painel de Controle

.. centered:: Tabela 1.3-1 Descrição dos Botões do Painel de Fiação do Painel de Controle

.. list-table::
   :widths: 50 200
   :header-rows: 0
   :align: center

   * - **Nome do Botão**
     - **Função**

   * - Botão de Parada de Emergência
     - Quando pressionado, o robô entra em estado de parada de emergência.

   * - Iniciar/Parar
     - Inicia/para a execução do programa.

   * - Porta de Rede
     - Conecta ao painel de ensinamento web.

   * - Desligar
     - Temporariamente não ativado.

   * - Registrar Ponto
     - Registra um ponto de ensinamento.

   * - Modo de Ensinamento
     - Entra/sai do modo de ensinamento.

   * - Modo de Operação
     - Alterna entre os modos automático e manual.

   * - Modo de Arrasto
     - Entra/sai do modo de arrasto.

Painel de Botões 60 (POE)(BX02)-V2.0
++++++++++++++++++++++++++++++++++++++++++++

.. image:: installation/079.png
   :width: 6in
   :align: center

.. centered:: Figura 1.3-3 Painel de Fiação do Painel de Controle

.. centered:: Tabela 1.3-2 Descrição dos Botões do Painel de Fiação do Painel de Controle

.. list-table::
   :widths: 50 200
   :header-rows: 0
   :align: center

   * - **Nome do Botão**
     - **Função**

   * - Botão de Parada de Emergência
     - Quando pressionado, o robô entra em estado de parada de emergência.

   * - Iniciar/Parar
     - Inicia/para a execução do programa.

   * - Porta de Rede
     - Conecta ao painel de ensinamento web.

   * - Reset de IP
     - Redefine o IP da porta de rede.

   * - Registrar Ponto
     - Registra um ponto de ensinamento.

   * - Limpeza com um Toque
     - Limpa todos os erros recuperáveis.

   * - Modo de Operação
     - Alterna entre os modos automático e manual.

   * - Modo de Arrasto
     - Entra/sai do modo de arrasto.

LED da Extremidade
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. centered:: Tabela 1.3-3 Definição do LED da Extremidade

.. list-table::
   :widths: 120 100
   :header-rows: 0
   :align: center

   * - **Função**
     - **Cor do LED**

   * - Quando a comunicação não está estabelecida
     - Alterna entre "apagado", "vermelho", "verde", "azul"

   * - Modo Automático
     - Azul fixo

   * - Modo Manual
     - Verde fixo

   * - Modo de Arrasto
     - Azul esverdeado (ciano) fixo

   * - Registro de ponto pelo painel de botões (apenas ao usar o painel de botões)
     - Pisca roxo duas vezes

   * - Entrando no estado sem painel de botões (apenas ao usar o painel de botões)
     - Pisca azul esverdeado (ciano) duas vezes

   * - Início da execução (apenas ao usar o painel de botões)
     - Pisca azul duas vezes

   * - Parada da execução (apenas ao usar o painel de botões)
     - Pisca vermelho duas vezes

   * - Erro (apenas ao usar o painel de botões)
     - Vermelho fixo

   * - Calibração do zero concluída
     - Pisca azul esverdeado (ciano) três vezes

   * - Desabilitação
     - Pisca amarelo duas vezes

Habilitando Após Ligar
------------------------------

Antes de ligar, verifique se o botão de parada de emergência do painel de botões está na posição de liberado. Pressione o botão vermelho no painel de controle para ligar. Após a habilitação bem-sucedida, o LED da extremidade ficará verde fixo.

Desligando a Alimentação
------------------------------

.. important:: 
   Ao usar este equipamento, certifique-se de parar todos os programas em execução, desativar as funções de consulta de status e confirmar que o estado de operação está "Parado" antes de desligar a alimentação. Esta operação visa proteger o equipamento e a segurança dos dados armazenados, evitando perda de dados ou danos ao sistema devido a uma interrupção repentina de energia.

.. image:: installation/078.png
   :width: 6in
   :align: center

.. centered:: Figura 1.5-1 Botão de Desligar