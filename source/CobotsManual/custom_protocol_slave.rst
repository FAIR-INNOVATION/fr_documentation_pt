Modo Escravo do Robô
===============================================================

.. toctree:: 
   :maxdepth: 6

Visão Geral
-------------------

Para facilitar o controle do movimento do robô por um CLP através de diferentes protocolos de barramento industrial (CC-Link, Profinet, Ethernet/IP, EtherCAT), as placas FRJ-PCIeN-EIP/CC/PN-RJ-V10 e FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20 são adicionadas ao gabinete de controle mini integrado. O modo escravo do robô é desenvolvido para realizar as seguintes funções:

- 1. O dispositivo mestre envia sinais de entrada para o escravo do robô para controlar o robô a executar ações correspondentes, por exemplo: controlar a saída DO do gabinete de controle do robô, controlar o movimento do robô, etc.;

- 2. O dispositivo mestre lê o valor do endereço correspondente para obter os dados de estado em tempo real correspondentes do robô, por exemplo: dados das juntas do robô, posição TCP, se o robô concluiu o movimento, etc.

Configuração do Ambiente
--------------------------

O modelo da placa e a versão do software são descritos a seguir:

.. list-table:: 
   :widths: 20 50 30
   :header-rows: 1
   :align: center

   * - **Tipo de Protocolo**
     - **Modelo da Placa**
     - **Versão do Software do Robô**

   * - CC-Link IEF Basic
     - Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.4 e superior

   * - CC-Link IEF Basic
     - Placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20
     - V3.9.6 e superior

   * - Profinet
     - Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.4 e superior

   * - Profinet
     - Placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20
     - V3.9.6 e superior

   * - Ethernet/IP
     - Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.4 e superior

   * - Ethernet/IP
     - Placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20
     - V3.9.6 e superior

   * - EtherCAT
     - Placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20
     - V3.9.6 e superior

Instalação da Placa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) Verificação dos materiais: A aparência da placa FRJ-PCIeN e das peças de chapa metálica complementares é mostrada abaixo.

.. image:: remote_mode/001.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-1 Chapa de Instalação (Frente)

.. image:: remote_mode/002.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-2 Chapa de Instalação (Verso)

.. image:: remote_mode/003.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-3 Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10

.. image:: remote_mode/004.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-4 Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10

(2) Instale a placa no gabinete de controle mini integrado, conforme mostrado na figura.

.. image:: remote_mode/005.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-5 Diagrama de Instalação da Chapa Metálica

.. image:: remote_mode/008.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-6 Diagrama de Instalação da Placa Mãe Principal

.. image:: remote_mode/009.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-7 Diagrama de Instalação da Placa de Expansão da Porta RJ45

.. note:: Nota: Todos os parafusos devem ser apertados.

(3) A fiação entre o gabinete de controle do robô e o CLP é mostrada na figura abaixo.

.. image:: remote_mode/010.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-8 Diagrama de Fiação do Gabinete de Controle & CLP Mitsubishi    

.. image:: remote_mode/011.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-9 Diagrama de Fiação do Gabinete de Controle & CLP Siemens

.. image:: remote_mode/012.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-10 Diagrama de Fiação do Gabinete de Controle & CLP Inovance

.. image:: remote_mode/013.png
   :width: 4in
   :align: center

.. centered:: Figura 19.2-11 Diagrama de Fiação do Gabinete de Controle & CLP Inovance

.. note:: 
    1: Gabinete de controle do robô (porta de rede da placa);
    2: Switch;
    3: PC portátil;
    4: CLP Mitsubishi (porta de rede CC-Link IEF Basic);
    5: CLP Siemens (porta de rede Profinet);
    6: CLP Inovance (Ethernet/IP);
    7: CLP Inovance (porta de rede EtherCAT);
        
Configuração do Ambiente CLP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O ambiente de teste construído para implementar os comandos escravos de cada protocolo é mostrado na tabela a seguir, incluindo o modelo do CLP, a versão do firmware e o software de teste usados em cada protocolo.

.. centered:: Tabela 2-1 Ambiente de Teste

.. list-table:: 
   :widths: 20 40 40
   :header-rows: 1
   :align: center

   * - Protocolo
     - Profinet
     - CC-link

   * - Marca
     - Siemens
     - Mitsubishi

   * - Modelo
     - CPU 1515-2 PN
     - FX5S-30TR/DS

   * - Firmware
     - 6ES75152AM020AB0
     - 30MR/ES V1.3

   * - Software
     - TIA Portal V17
     - GXWorks3V1.097B

   * - Endereço IP da Placa
     - Configurável
     - Configurável

   * - Endereço IP do CLP
     - Não precisa estar na mesma sub-rede
     - Mesma sub-rede
		
.. list-table:: 
   :widths: 20 40 40
   :header-rows: 1
   :align: center

   * - Protocolo
     - Ethernet/IP
     - EtherCAT

   * - Marca
     - Inovance
     - Inovance

   * - Modelo
     - Easy521-0808TN
     - Easy521-0808TN

   * - Firmware
     - /
     - /

   * - Software
     - AutoShop 4.11.0.1
     - AutoShop 4.11.0.1

   * - Endereço IP da Placa
     - Configurável
     - Configurável

   * - Endereço IP do CLP
     - Mesma sub-rede
     - Mesma sub-rede
		
Inovance Ethernet/IP
+++++++++++++++++++++++++++++++++++++++++++++++++++++

(1) Importação do Arquivo EDS

Abra o software de programação Inovance AutoShop, crie um novo projeto CLP e selecione "EtherNet/IP Devices" na caixa de ferramentas à direita.

Clique com o botão esquerdo em "EtherNet/IP", clique com o botão direito para abrir a caixa de diálogo "Importar EDS". Confirme com o botão esquerdo e encontre a pasta que contém o arquivo EDS da placa. Após a importação bem-sucedida, o nome da placa aparecerá no diretório "EtherNet/IP Devices". Feche o projeto e reabra-o para concluir a importação do arquivo EDS.

.. image:: custom_protocol_slave/001.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/002.png
   :width: 6in
   :align: center

(2) Configuração de Parâmetros EtherNet/IP

Clique duas vezes no escravo em "EtherNet/IP" na barra de ferramentas esquerda para abrir a janela de configuração de parâmetros:

.. image:: custom_protocol_slave/003.png
   :width: 6in
   :align: center

Preencha o endereço IP da placa:

.. image:: custom_protocol_slave/004.png
   :width: 6in
   :align: center

Clique para selecionar "Conexão" para definir o tamanho em bytes de entrada e saída de dados:

.. image:: custom_protocol_slave/005.png
   :width: 6in
   :align: center

Clique em "Editar Conexão" para entrar na janela pop-up e altere os bytes de entrada e saída para 256:

.. image:: custom_protocol_slave/006.png
   :width: 6in
   :align: center

Clique para selecionar "Conjunto de Dados", defina o tipo de dados de entrada e saída como "INT" e o comprimento do bit como "2048":

.. image:: custom_protocol_slave/007.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/008.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/009.png
   :width: 6in
   :align: center

Após definir os parâmetros do "Conjunto de Dados" com sucesso, clique para selecionar "Mapeamento de E/S EtherNet/IP" e insira D0 e D200 respectivamente. D0 e D200 correspondem aos endereços iniciais das matrizes de recebimento e envio no lado do CLP.

.. image:: custom_protocol_slave/010.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/011.png
   :width: 6in
   :align: center

(3) Download do Programa

Abra o programa de teste, modifique o endereço IP do CLP para que esteja na mesma sub-rede da placa e execute o programa após o download.

Siemens Profinet
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

(1) Importação do Arquivo GSD (Arquivo XML)

Abra o software de programação Siemens TIA Portal V17, crie um novo projeto CLP, selecione "Dispositivos e Redes" e clique duas vezes em 6ES7 515-2AM02-0AB0 no "Catálogo de Hardware" à direita para adicionar o módulo CLP.

.. image:: custom_protocol_slave/012.png
   :width: 6in
   :align: center

Na barra de menu do software TIA PORTAL, selecione "Opções" -> "Gerenciar arquivos de descrição de estação geral (GSD)" para instalar ou excluir arquivos GSD já instalados.

.. image:: custom_protocol_slave/013.png
   :width: 6in
   :align: center

Para instalar arquivos GSD, selecione "Gerenciar arquivos de descrição de estação geral (GSD)" como acima. A janela "Gerenciar arquivos de descrição de estação geral" aparece.

Selecione a pasta que contém os arquivos GSD a serem instalados no "Caminho de origem", selecione um ou mais arquivos para instalar na lista de arquivos GSD exibida e clique no botão "Instalar". Conforme mostrado na figura abaixo.

.. image:: custom_protocol_slave/014.png
   :width: 6in
   :align: center

Após a instalação bem-sucedida, o dispositivo com o arquivo GSD instalado pode ser encontrado em "Outros dispositivos de campo" no catálogo de hardware, conforme mostrado na figura abaixo.

.. image:: custom_protocol_slave/015.png
   :width: 6in
   :align: center

Atribuição de E/S: Procure módulos no diretório e arraste Input e Output.

.. image:: custom_protocol_slave/016.png
   :width: 6in
   :align: center

Compilar o programa: Clique duas vezes para entrar em "Dispositivos e Redes" na árvore do projeto à esquerda, clique com o botão direito no módulo "PLC_1", selecione "Compilar" no menu suspenso e clique em "Hardware e software (somente alterações)". Após a conclusão da compilação, "Compilação concluída" aparecerá na parte inferior da visualização do software:

.. image:: custom_protocol_slave/017.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/018.png
   :width: 6in
   :align: center

Baixar o programa para o dispositivo: Clique duas vezes para entrar em "Dispositivos e Redes" na árvore do projeto à esquerda, clique com o botão direito no módulo "PLC_1", selecione "Baixar para dispositivo" no menu suspenso e clique em "Hardware e software (somente alterações)":

.. image:: custom_protocol_slave/019.png
   :width: 6in
   :align: center

Pesquisar e baixar o dispositivo: Após a janela pop-up, configure o tipo de interface PG/PC conforme mostrado abaixo, clique em "Iniciar pesquisa", selecione o dispositivo para o qual o programa precisa ser baixado e clique em "Baixar":

.. image:: custom_protocol_slave/020.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/021.png
   :width: 6in
   :align: center

Mitsubishi CC-link
+++++++++++++++++++++++++++++++++++++++++++++++++

(1) Configurações CC-Link IEF Basic

Habilitar CC-link: Selecione "Porta Ethernet" na barra de menu de navegação esquerda, defina o endereço IP do CLP para garantir que esteja na mesma sub-rede do endereço da placa Jiyuan. Clique em "Uso CC-link IEF Basic" e selecione "Usar":

.. image:: custom_protocol_slave/022.png
   :width: 6in
   :align: center

Configurações de Configuração de Rede CC-Link: Também nas configurações CC-Link IEF Basic, selecione "Configurações de Configuração de Rede" e escolha o módulo geral CC-Link IEF Basic. Arraste-o para o canto inferior esquerdo da visualização para concluir a configuração de hardware:

.. image:: custom_protocol_slave/023.png
   :width: 6in
   :align: center
   
.. image:: custom_protocol_slave/024.png
   :width: 6in
   :align: center

Defina os pontos da estação escrava e o endereço IP:

.. image:: custom_protocol_slave/025.png
   :width: 6in
   :align: center
   
.. image:: custom_protocol_slave/026.png
   :width: 6in
   :align: center

Configurações de Atualização CC-Link: Também nas configurações CC-Link IEF Basic, clique em "Configurações de Atualização" e personalize as configurações de transmissão: 256 bytes de recebimento, 256 bytes de envio.
   
.. image:: custom_protocol_slave/027.png
   :width: 6in
   :align: center

(2) Download do Programa

Após abrir o programa de teste, clique em "Online" -> "Escrever para Controlador Programável" para entrar na interface de download.
   
.. image:: custom_protocol_slave/028.png
   :width: 6in
   :align: center

Após abrir a interface de download, clique em "Parâmetro + Programa" no canto superior esquerdo e clique em "Executar" no canto inferior direito para baixar e aguardar a conclusão do download.
   
.. image:: custom_protocol_slave/029.png
   :width: 6in
   :align: center

Inovance EtherCAT
++++++++++++++++++++++++++++++++++++++++++++++

(1) Importação do Arquivo XML

Abra o software de programação Inovance AutoShop, crie um novo projeto CLP e selecione "EtherCATDevices" na caixa de ferramentas à direita:
   
.. image:: custom_protocol_slave/030.png
   :width: 6in
   :align: center

Clique com o botão esquerdo em "EtherCATDevices", clique com o botão direito para abrir a caixa de diálogo "Importar Dispositivo XML". Confirme com o botão esquerdo e encontre a pasta que contém o arquivo XML da placa.

Após a importação bem-sucedida, o nome da placa aparecerá no diretório "EtherCAT Devices". Feche o projeto e reabra-o para concluir o processo de importação do arquivo XML.
   
.. image:: custom_protocol_slave/031.png
   :width: 6in
   :align: center

(2) Adicionar Escravo EtherCAT

Barra de ferramentas direita → "EtherCAT Devices" → "Other Devices" → "JIYuan" → "Xone-PCIe-ECATs". Clique duas vezes em "Xone-PCIe-ECATs" para adicionar o escravo EtherCAT. Agora você pode ver que o escravo foi adicionado com sucesso sob o mestre EtherCAT na árvore do projeto à esquerda.
   
.. image:: custom_protocol_slave/032.png
   :width: 6in
   :align: center
   
.. image:: custom_protocol_slave/033.png
   :width: 6in
   :align: center

(3) Adicionar PDO
   
.. image:: custom_protocol_slave/034.png
   :width: 6in
   :align: center
   
.. image:: custom_protocol_slave/035.png
   :width: 6in
   :align: center

(4) Mapeamento de Endereços EtherCAT

Clique duas vezes na tabela de variáveis na barra de ferramentas esquerda para criar uma nova matriz de entrada de 256 bytes com endereço de componente suave D0. Crie uma nova matriz de saída de 256 bytes com endereço de componente suave D200.
   
.. image:: custom_protocol_slave/036.png
   :width: 6in
   :align: center

Em "EtherCAT" na barra de ferramentas esquerda, clique duas vezes em "Xone-PCIe-ECATs". Na caixa de diálogo exibida, clique em "Mapeamento de Funções de E/S", clique na caixa para vincular o endereço da variável. Na caixa de diálogo exibida, clique em "Tabela de Variáveis", selecione a entrada/saída correspondente e clique em "OK". Vincule outros endereços em ordem usando o mesmo procedimento.
   
.. image:: custom_protocol_slave/037.png
   :width: 6in
   :align: center

(5) Download do Programa

Abra o programa de teste, altere o endereço IP do CLP para que esteja na mesma sub-rede da placa e execute o programa após o download.

Instruções Operacionais Relacionadas ao Modo Escravo do Robô
--------------------------------------------------------------------------------------

Carregar Modo Escravo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) Abra o WebApp, vá para Configurações Iniciais -> Periféricos -> Comunicação da Placa -> Configuração Manual.
   
.. image:: custom_protocol_slave/038.png
   :width: 6in
   :align: center

Primeiro, configure o endereço IP da placa. Se deixado em branco, a placa iniciará com o IP padrão: 192.168.0.100. Atualmente, a configuração de IP é aplicável apenas aos protocolos EIP e CC-link; para o protocolo PN, o IP é atribuído pelo mestre CLP que escaneia o dispositivo escravo.

.. note:: Após alterar o endereço IP na página, você precisa carregar o modo escravo para que ele entre em vigor.
   
Em seguida, selecione as funções de mapeamento necessárias para DI, DO e AO (ver apêndice). O significado de cada parâmetro é o seguinte:

- DI é para controle do robô: O escravo do robô recebe o sinal de entrada externo e executa a função mapeada;
- DO é para saída de estado do robô: O escravo do robô envia sinais de estado de volta ao mestre;
- AO é para feedback de estado do robô: O escravo do robô envia dados de estado de volta ao mestre. AO0~AO15 são inteiros com sinal (int16), AO16~AO31 são números de ponto flutuante de precisão simples (float).

(2) Clique no botão "Configurar" para gerar o arquivo lua de protocolo aberto.
   
.. image:: custom_protocol_slave/039.png
   :width: 6in
   :align: center

.. note:: O arquivo lua de protocolo aberto suporta download e pode ser importado na interface de configuração automática.

Um exemplo do programa gerado é o seguinte:

.. code-block:: console
   :linenos:

   local id = 3 
   local ctrlDI = {0, 0, 0, 0, 0, 0}
   local funcDI = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
   local DOState = {0, 0, 0, 0, 0, 0, 0, 0}
   local AOState = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
   -- Launch the board communication process
   SetFieldBusIP("192.168.0.99")
   LoadFieldBusSlave()
   sleep_ms(8000)
   while(1) do
      -- Set the DO status
      CtrlBoxDO, CtrlBoxCO, CtrlBoxDI, CtrlBoxCI, errState, motionState, moveToOriginState, robotStartDoneState, modeChangeState, programStartStopState, emergencyState, reduceState, collision, enablestate, safetyStop0, safetyStop1, pauseState, interfereState = GetRobotFuncDOState()
      DOState[1] = CtrlBoxDO
      DOState[2] = CtrlBoxCO
      DOState[3] = CtrlBoxDI
      DOState[4] = CtrlBoxCI
      local ctrlWord0 = 0
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 0, errState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 1, motionState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 2, moveToOriginState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 3, robotStartDoneState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 4, modeChangeState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 5, programStartStopState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 6, emergencyState)
      ctrlWord0 = SetBitWithIndex(ctrlWord0, 7, reduceState)
      DOState[5] = ctrlWord0
      local ctrlWord1 = 0
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 0, collision)
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 1, enablestate)
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 2, safetyStop0)
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 3, safetyStop1)
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 4, pauseState)
      ctrlWord1 = SetBitWithIndex(ctrlWord1, 5, interfereState)
      DOState[6] = ctrlWord1
      SetFieldBusDOState(DOState)

      -- Set the AO status
      mainErrCode, subErrCode, TCPSpeed, axisPos1, axisPos2, axisPos3, axisPos4, axisPos5, axisPos6, jointVelFeedback1, jointVelFeedback2, jointVelFeedback3, jointVelFeedback4, jointVelFeedback5, jointVelFeedback6, jointCurFeedback1, jointCurFeedback2, jointCurFeedback3,jointCurFeedback4,jointCurFeedback5,jointCurFeedback6, jointTorqueFeedback1, jointTorqueFeedback2,jointTorqueFeedback3,jointTorqueFeedback4, jointTorqueFeedback5, jointTorqueFeedback6, cartPosx, cartPosy, cartPosz, cartPosrx, cartPosry, cartPosrz = GetRobotFuncAOState()
      AOState[1] = mainErrCode
      AOState[2] = subErrCode
      AOState[17] = axisPos1
      AOState[18] = axisPos2
      AOState[19] = axisPos3
      AOState[20] = axisPos4
      AOState[21] = axisPos5
      AOState[22] = axisPos6
      AOState[23] = cartPosx
      AOState[24] = cartPosy
      AOState[25] = cartPosz
      AOState[26] = cartPosrx
      AOState[27] = cartPosry
      AOState[28] = cartPosrz
      SetFieldBusAOState(AOState)
      sleep_ms(10) 

      -- Set the DI status
      -- Configue the DI function and update it in real-time
      ctrlDI[1],ctrlDI[2],ctrlDI[3],ctrlDI[4],ctrlDI[5],ctrlDI[6] = GetFieldBusDIState()
      funcDI[1] = ctrlDI[1] 
      funcDI[2] = ctrlDI[2] 
      funcDI[3] = GetBitWithIndex(ctrlDI[3], 0)
      funcDI[4] = GetBitWithIndex(ctrlDI[3], 1)
      funcDI[5] = GetBitWithIndex(ctrlDI[3], 2)
      funcDI[6] = GetBitWithIndex(ctrlDI[3], 3)
      funcDI[7] = GetBitWithIndex(ctrlDI[3], 4)
      funcDI[8] = GetBitWithIndex(ctrlDI[3], 5)
      funcDI[9] = GetBitWithIndex(ctrlDI[3], 6)
      funcDI[10] = GetBitWithIndex(ctrlDI[3], 7)
      funcDI[11] = GetBitWithIndex(ctrlDI[4], 0)
      funcDI[12] = GetBitWithIndex(ctrlDI[4], 1)
      funcDI[13] = GetBitWithIndex(ctrlDI[4], 2)
      funcDI[14] = GetBitWithIndex(ctrlDI[4], 3)
      funcDI[15] = GetBitWithIndex(ctrlDI[4], 4)
      funcDI[16] = GetBitWithIndex(ctrlDI[4], 5)
      SetRobotFuncDIState(funcDI)
      local stopFlag = GetOpenLUAStopFlag(id)
      if(stopFlag ~= 0) then 
         UnloadFieldBusSlave()
         break
      end
      sleep_ms(10)
   end

(3) Clique no botão "Carregar" para carregar o modo escravo do robô.
   
.. image:: custom_protocol_slave/040.png
   :width: 6in
   :align: center

.. note:: Após o modo escravo do robô ser carregado com sucesso, ele suporta a inicialização automática ao ligar. Se precisar usar o modo remoto, descarregue o modo escravo primeiro.

(4) Clique no botão da barra de status da placa à direita para monitorar as informações de interação DI, DO, AI e AO. Os parâmetros são introduzidos a seguir:

- CtrlDO: Valor de entrada do sinal DO/CO do gabinete de controle enviado pelo mestre externo;
- DI: Valor de entrada do sinal de controle do mestre externo;
- Aux_DI: DI estendido da placa de comunicação;
- DO: Valor de saída do sinal de feedback do escravo do robô;
- Aux_DO: DO estendido da placa de comunicação;
- AI: Valor de entrada do mestre externo;
- AI0~AI15: tipo int16;
- AI16~AI31: tipo float;
- AO: Valor de saída do escravo do robô;
- AO0~AO15: tipo int16;
- AO16~AO31: tipo float.

.. note:: Para informações detalhadas sobre os parâmetros DI, DO, AI, AO, consulte "RD36-Tabela de Comparação de Endereços do Modo Escravo do Robô-V1.0-20260605".
   
.. image:: custom_protocol_slave/041.png
   :width: 4in
   :align: center

(5) Após o carregamento, você pode gerar instruções lua da placa através de Programa de Ensino -> Instruções de Comunicação -> Placa para definir DO, AO do escravo, obter DI, AI do escravo e aguardar DI, AI do escravo.
   
.. image:: custom_protocol_slave/042.png
   :width: 6in
   :align: center

Atualização de Firmware da Placa e Configuração do Ciclo de Comunicação
--------------------------------------------------------------------------

Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ao alternar protocolos, a placa requer uma atualização de firmware. Use o computador host para atualizar o firmware da placa FRJ-PCIeN-EIP/CC/PN-RJ-V10. As etapas são as seguintes:

(1) Abra WinPcap_4_1_3.exe e instale o pacote de driver da placa de rede.

(2) Conecte diretamente a porta de rede do PC (sistema Win11) à porta de rede da placa. Abra Device Assistant v1.1.0.exe, clique duas vezes em "Ethernet" e clique no botão "Atualizar" no canto superior esquerdo para escanear o dispositivo da placa atualmente conectado.
   
.. image:: custom_protocol_slave/043.png
   :width: 6in
   :align: center
      
.. image:: custom_protocol_slave/044.png
   :width: 6in
   :align: center

(3) Clique duas vezes no dispositivo da placa escaneado para entrar na interface de atualização de firmware. Configure o PC e o IP da placa obtido na mesma sub-rede. Clique no botão "..." no lado direito da barra de menu "Atualização de Firmware" para carregar o firmware a ser atualizado. Clique no botão "Atualizar" e uma mensagem "Atualização bem-sucedida" aparecerá na caixa de texto no canto inferior esquerdo.
      
.. image:: custom_protocol_slave/045.png
   :width: 6in
   :align: center

(4) Após uma atualização bem-sucedida da placa, uma operação de reinicialização será executada. Aguarde a conclusão da reinicialização da placa (5s), insira o ciclo de comunicação necessário (suporta 1~100ms), clique no botão "Definir" e, após a mensagem "Configuração de ciclo bem-sucedida" aparecer no canto inferior esquerdo, reinicie o gabinete de controle.
      
.. image:: custom_protocol_slave/046.png
   :width: 6in
   :align: center

Placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ao alternar protocolos, a placa requer uma atualização de firmware. Faça login na interface do robô para atualizar o firmware da placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20. As etapas são as seguintes:

(1) Digite o URL 192.168.58.2 para acessar a interface do robô. Clique na interface "Configurações Iniciais" -> "Periféricos" -> "Comunicação da Placa" para obter o número da versão do firmware da placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20. Selecione o arquivo bin a ser atualizado, clique em "Carregar", aguarde a atualização do firmware ser bem-sucedida e reinicie o gabinete de controle.
      
.. image:: custom_protocol_slave/047.png
   :width: 6in   
   :align: center

.. note:: Para atualizar o firmware da placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20, você precisa descarregar o protocolo aberto em execução.

(2) Digite o URL 192.168.58.2 para acessar a interface do robô. Clique na interface "Configurações Iniciais" -> "Periféricos" -> "Comunicação da Placa" para obter o ciclo de comunicação da placa. Digite o ciclo de comunicação necessário (1~100ms), clique no botão "Configurar", aguarde a configuração ser bem-sucedida e reinicie o gabinete de controle.
      
.. image:: custom_protocol_slave/048.png
   :width: 6in
   :align: center

.. note:: Para configurar o ciclo de comunicação da placa FRJ-PCIeN-EC/PN/EIP/CC-RJ-V20, você precisa descarregar o protocolo aberto em execução.

:download:`Firmware da placa de comunicação e arquivos de configuração <../_static/_doc/Board communication firmware and configuration files.zip>`

:download:`Resumo dos programas de teste PLC para cada protocolo <../_static/_doc/Summary of PLC Test Programs for Each Protocol.zip>`   