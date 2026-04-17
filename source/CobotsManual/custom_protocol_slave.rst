Instruções do Escravo de Protocolo Personalizado
============================================================

.. toctree:: 
   :maxdepth: 6

Visão Geral
-------------------

Para facilitar o controle de movimento do robô por um CLP através de diferentes protocolos de barramento industrial (CC-Link IEF Basic, Profinet, Ethernet/IP e EtherCAT), as placas FRH-PCIeN-EC/EIP/CC/PN-RJ-V10, FRJ-PCIeN-EIP/CC/PN-RJ-V10 e FRJ-PCIeN-EC-RJ-V10 foram adicionadas ao mini painel de controle integrado.

Configuração do Ambiente
--------------------------

Os modelos das placas e as versões de software são descritos abaixo:

.. list-table:: 
   :widths: 20 50 30
   :header-rows: 1
   :align: center

   * - **Tipo de Protocolo**
     - **Modelo da Placa**
     - **Versão do Software do Robô**

   * - CC-Link IEF Basic
     - Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10, Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.0 ou superior

   * - Profinet
     - Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10, Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.0 ou superior

   * - Ethernet/IP
     - Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10, Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10
     - V3.8.0 ou superior

   * - EtherCAT
     - Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10, Placa FRJ-PCIeN-EC-RJ-V10
     - V3.8.4.1 ou superior

Configuração do Ambiente de Hardware para a Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Instale a placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10 no mini painel de controle integrado, conforme mostrado.

.. image:: custom_protocol_slave/001.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-1 Instalação da Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10

.. image:: custom_protocol_slave/002.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-2 Porta Ethernet da Placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10

2. A fiação entre o painel de controle do robô e o CLP é mostrada nas figuras abaixo.

.. image:: custom_protocol_slave/003.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-3 Diagrama de Fiação do Painel de Controle & CLP Mitsubishi

.. image:: custom_protocol_slave/004.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-4 Diagrama de Fiação do Painel de Controle & CLP Siemens

.. image:: custom_protocol_slave/005.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-5 Diagrama de Fiação do Painel de Controle & CLP Omron

.. image:: custom_protocol_slave/006.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-6 Diagrama de Fiação do Painel de Controle & CLP Omron

.. note:: 
    1: Painel de controle do robô (porta Ethernet da placa);
    2: Switch;
    3: Notebook PC;
    4: CLP Mitsubishi (porta Ethernet CC-Link IEF Basic);
    5: CLP Siemens (porta Ethernet Profinet);
    6: CLP Omron (porta Ethernet Ethernet/IP);
    7: CLP Omron (porta Ethernet EtherCAT);

.. important:: Quando o protocolo é alterado para o barramento EtherCAT, as portas Ethernet da placa precisam ser diferenciadas em EtherCAT_IN e EtherCAT_OUT. Neste caso, a porta Ethernet EtherCAT do CLP Omron deve ser diretamente conectada à porta EtherCAT_IN da placa com um cabo Ethernet.

Configuração do Ambiente de Hardware para a Placa FRJ-PCIeN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Instale a placa no mini painel de controle integrado, conforme mostrado.

.. image:: custom_protocol_slave/044.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-7 Portas Ethernet da Placa FRJ-PCIeN

2. A fiação entre o painel de controle do robô e o CLP é mostrada nas figuras abaixo.

.. image:: custom_protocol_slave/003.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-8 Diagrama de Fiação do Painel de Controle & CLP Mitsubishi

.. image:: custom_protocol_slave/004.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-9 Diagrama de Fiação do Painel de Controle & CLP Siemens

.. image:: custom_protocol_slave/005.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-10 Diagrama de Fiação do Painel de Controle & CLP Inovance

.. note:: 
    1: Painel de controle do robô (porta Ethernet da placa);
    2: Switch;
    3: Notebook PC;
    4: CLP Mitsubishi (porta Ethernet CC-Link IEF Basic);
    5: CLP Siemens (porta Ethernet Profinet);
    6: CLP Inovance (Ethernet/IP);

3. Ao alternar o protocolo na placa FRJ-PCIeN, é necessária uma atualização de firmware. Durante a atualização de firmware, o endereço IP do PC conectado à placa deve ser alterado para “192.168.0.xxx”. Em seguida, abra o software “Gateway Tool Set” -> selecione o dispositivo de placa de rede do PC a ser conectado -> clique no botão “Iniciar” no canto inferior direito -> clique no botão “Pesquisar” no canto superior direito para procurar o dispositivo da placa.

.. image:: custom_protocol_slave/045.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-11 Conectando ao Dispositivo da Placa

4. Clique no botão “Atualizar” no canto inferior esquerdo -> selecione o dispositivo da placa -> clique no botão “…” no canto superior direito para selecionar o firmware do protocolo desejado -> clique no botão “Atualizar” e aguarde a conclusão da atualização do firmware.

.. image:: custom_protocol_slave/046.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-12 Alternância de Protocolo da Placa

.. note:: Após a alternância do protocolo, o endereço IP da placa será alterado, conforme mostrado na tabela abaixo.

.. centered:: Tabela 17.2-1 Endereços IP da Placa

.. list-table:: 
   :widths: 20 80
   :header-rows: 1
   :align: center

   * - **Protocolo**
     - **Endereço IP**

   * - CC-Link IEF Basic
     - 192.168.0.113

   * - Ethernet/IP
     - 192.168.0.112

   * - Profinet
     - 192.168.0.2

Quando o protocolo é configurado como CC-Link IEF Basic, o controlador alterará o IP da placa para “192.168.0.113”.

Quando o protocolo é configurado como Ethernet/IP, o controlador alterará o IP da placa para “192.168.0.112”.

Quando o protocolo é alterado para Profinet e o nome do dispositivo escravo corresponde ao do mestre, o mestre configurará automaticamente o endereço IP do escravo.

5. Atualização de Firmware da Placa FRJ-PCIeN-EC-RJ-V10

Insira o URL 192.169.58.2 para acessar a interface do robô. Clique em “Configurações Iniciais” -> “Periféricos” -> “Comunicação com Placa” para obter o número da versão do firmware da placa FRJ-PCIeN-EC-RJ-V10. Selecione o arquivo .bin a ser atualizado, clique em “Enviar” e, após a conclusão bem-sucedida da atualização do firmware, reinicie o painel de controle.

.. image:: custom_protocol_slave/064.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-13 Atualização de Firmware da Placa

.. note:: 1. Apenas as versões V3.9.2 e superiores suportam a atualização de firmware do protocolo Ethercat; 2. Para atualizar o firmware do protocolo Ethercat, é necessário descarregar o protocolo aberto em execução.

Configuração do Ambiente de Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Insira o IP 192.168.58.2 no navegador, o nome de usuário é admin e a senha é 123. Clique em “Login” para acessar a interface web do painel de controle do robô.

.. image:: teaching_pendant_software/001.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-14 Interface de Login Web

2. Clique em Configurações do Sistema -> Sobre e, em seguida, clique no botão “Atualização de Software”. Selecione o arquivo software.tar.gz e faça o upload do pacote de atualização.

.. image:: custom_protocol_slave/008.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-15 Atualização de Software

.. note:: A versão web do painel de controle QX precisa ser 3.8.0 ou superior, e a versão web do painel de controle LA precisa ser 3.8.0 ou superior.

3. Clique no botão de expansão no canto superior direito para alternar de “Modo Local” para “Modo Remoto”.

.. image:: custom_protocol_slave/010.png
   :width: 4in
   :align: center

.. centered:: Figura 17.2-16 Alternar para Modo Remoto

4. Selecione o protocolo escravo do controlador e a necessidade da função de autoinicialização. Clique no botão “Definir”. Observe: para alternar entre diferentes protocolos, é necessário primeiro clicar no botão “Descarregar” antes de configurar outro protocolo.

.. image:: custom_protocol_slave/011.png
   :width: 6in
   :align: center

.. centered:: Figura 17.2-17 Configurar Protocolo de Comunicação

.. note:: Para alternar entre diferentes protocolos, é necessário reiniciar o painel de controle antes de configurar o protocolo.

Configuração do Ambiente do CLP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O ambiente de teste para implementar as instruções escravas de cada protocolo é mostrado na tabela abaixo, incluindo os modelos de CLP usados, a versão do firmware e o software de teste.

.. list-table:: 
   :widths: 100 100 100 100 100
   :header-rows: 1
   :align: center

   * - Protocolo
     - Marca
     - Modelo
     - Firmware
     - Software
  
   * - Profinet
     - Siemens
     - CPU 1515-2 PN
     - 6ES75152AM020AB0
     - TIA Portal V17
  
   * - CC-Link IEF Basic
     - Mitsubishi
     - FX5S-30TR/DS
     - 30MR/ES V1.3
     - GX Works3 V1.097B
  
   * - Ethernet/IP
     - Omron
     - MX102-1100
     - V1.3
     - Sysmac Studio V1.50
  
   * - EtherCAT
     - Inovance
     - Easy521-0808TN
     - /
     - AutoShop 4.10.2.4

Siemens Profinet
++++++++++++++++++++++++++++++++++

1. Importação do Arquivo GSD (Arquivo XML)

Abra o software de programação Siemens TIA Portal V17, crie um novo projeto CLP e selecione “Dispositivos e Redes”. No “Catálogo de Hardware” à direita, clique duas vezes em 6ES7 515-2AM02-0AB0 para adicionar o módulo CLP.

.. image:: custom_protocol_slave/012.png
   :width: 6in
   :align: center

Na barra de menu do software TIA PORTAL, selecione “Opções” -> “Gerenciar arquivos de descrição de estação geral (GSD)” para instalar ou remover arquivos GSD já instalados.

.. image:: custom_protocol_slave/013.png
   :width: 6in
   :align: center

Usando a instalação do arquivo GSD da placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10 como exemplo, selecione “Gerenciar arquivos de descrição de estação geral (GSD)” conforme acima. A janela “Gerenciar arquivos de descrição de estação geral” será exibida.

Selecione a pasta onde o arquivo GSD a ser instalado está localizado em “Caminho de origem”. Na lista de arquivos GSD exibida, selecione um ou mais arquivos para instalar e clique no botão “Instalar”, conforme mostrado abaixo.

.. image:: custom_protocol_slave/014.png
   :width: 6in
   :align: center

Após a instalação bem-sucedida, o dispositivo do arquivo GSD instalado pode ser encontrado em “Outros dispositivos de campo” no catálogo de hardware, conforme mostrado abaixo.

.. image:: custom_protocol_slave/015.png
   :width: 4in
   :align: center

2. Executar Programa

Abra o projeto “QNXtest”.

.. image:: custom_protocol_slave/016.png
   :width: 6in
   :align: center

Compilar o programa: na árvore do projeto à esquerda, clique duas vezes para entrar em “Dispositivos e Redes”. Clique com o botão direito no módulo “PLC_1”, selecione “Compilar” no menu suspenso e escolha “Hardware e Software (somente alterações)”. Após a compilação, a mensagem “Compilação concluída” será exibida na parte inferior da visualização do software.

.. image:: custom_protocol_slave/017.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/018.png
   :width: 6in
   :align: center

Baixar o programa para o dispositivo: na árvore do projeto à esquerda, clique duas vezes para entrar em “Dispositivos e Redes”. Clique com o botão direito no módulo “PLC_1”, selecione “Baixar para dispositivo” no menu suspenso e escolha “Hardware e Software (somente alterações)”.

.. image:: custom_protocol_slave/019.png
   :width: 6in
   :align: center

Pesquisar e baixar o dispositivo: após a janela pop-up, configure o tipo de interface PG/PC conforme mostrado, clique em “Iniciar pesquisa”, selecione o dispositivo para o qual o programa será baixado e clique em “Baixar”.

.. image:: custom_protocol_slave/020.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/021.png
   :width: 6in
   :align: center

Mitsubishi CC-Link IEF Basic
++++++++++++++++++++++++++++++++++

1. Configuração CC-Link IEF Basic

Habilitar o uso do CC-Link IEF Basic: no menu de navegação à esquerda, selecione “Porta Ethernet”. Defina o endereço IP do CLP, garantindo que esteja no mesmo segmento de rede que o endereço da placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10. Clique em “Usar CC-Link IEF Basic” e selecione “Usar”.

.. image:: custom_protocol_slave/022.png
   :width: 6in
   :align: center

Configuração da rede CC-Link IEF Basic: ainda nas configurações do CC-Link IEF Basic, selecione “Configuração de Rede”. Selecione o módulo CIFX Digital I/O da placa FRH-PCIeN-EC/EIP/CC/PN-RJ-V10. Arraste-o para o canto inferior esquerdo da visualização para concluir a configuração de hardware.

.. image:: custom_protocol_slave/023.png
   :width: 6in
   :align: center

Configuração de atualização CC-Link IEF Basic: ainda nas configurações do CC-Link IEF Basic, clique em “Configuração de Atualização”. Defina as configurações de transferência personalizadas: 256 bytes de recepção, 256 bytes de transmissão.

.. image:: custom_protocol_slave/024.png
   :width: 6in
   :align: center

2. Download do Programa

Após abrir o programa de teste, clique em “Online” → “Gravar no controlador programável” para entrar na interface de download.

.. image:: custom_protocol_slave/025.png
   :width: 6in
   :align: center

Após abrir a interface de download, clique em “Parâmetros + Programa” no canto superior esquerdo e, em seguida, clique em “Executar” no canto inferior direito para iniciar o download. Aguarde a conclusão.

.. image:: custom_protocol_slave/026.png
   :width: 6in
   :align: center

Inovance EtherCAT
++++++++++++++++++++++++++++++++++

1. Importação do Arquivo XML

Abra o software de programação Inovance AutoShop, crie um novo projeto CLP e, na barra de ferramentas à direita, selecione “EtheCATDevices”:

.. image:: custom_protocol_slave/052.png
   :width: 6in
   :align: center

Clique com o botão esquerdo em “EtheCATDevices” e, em seguida, com o botão direito para abrir a caixa de diálogo “Importar XML do dispositivo”. Clique em “OK”, encontre a pasta onde o arquivo XML da placa está localizado e selecione-o.

Após a importação bem-sucedida, o nome da placa aparecerá no diretório “EtherCAT Devices”. Feche o projeto e reabra-o para concluir o processo de importação do arquivo XML.

.. image:: custom_protocol_slave/053.png
   :width: 6in
   :align: center

2. Configuração do Mapeamento de E/S

Na barra de ferramentas à esquerda, clique duas vezes em “Tabela de Variáveis”. Crie uma nova matriz de entrada de 256 bytes com o endereço do dispositivo D0. Crie uma nova matriz de saída de 256 bytes com o endereço do dispositivo D200.

.. image:: custom_protocol_slave/054.png
   :width: 6in
   :align: center

Na barra de ferramentas à esquerda, em “EtherCAT”, clique duas vezes em “Xone-PCIe-ECATs”. Na caixa de diálogo pop-up, clique em “Mapeamento de Funções de E/S”. Clique na caixa para vincular o endereço da variável. Na caixa de diálogo pop-up, clique em “Tabela de Variáveis”, selecione a entrada/saída correspondente desejada e clique em “OK”. Repita a operação para vincular outros endereços em ordem.

.. image:: custom_protocol_slave/055.png
   :width: 6in
   :align: center

3. Download do Programa

Abra o programa de teste. Altere o endereço IP do CLP para “192.168.0.88” (o padrão é “192.168.1.88”).

.. image:: custom_protocol_slave/056.png
   :width: 6in
   :align: center

Clique em “Modificar IP/Nome do Dispositivo” para entrar na interface de configuração de modificação de IP. Altere o endereço IP e o gateway para “192.168.0.88”:

.. image:: custom_protocol_slave/057.png
   :width: 6in
   :align: center

Clique em “Modificar IP”. Após a caixa de diálogo pop-up, clique em “Sim” para confirmar. O endereço IP será modificado com sucesso.

.. image:: custom_protocol_slave/058.png
   :width: 6in
   :align: center

Após a comunicação bem-sucedida, baixe o programa CLP.

.. image:: custom_protocol_slave/059.png
   :width: 6in
   :align: center

Configuração da IHM (Simulação CC-Link IEF Basic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Após fazer login na interface da IHM, habilite “Enable Task” para estabelecer a conexão de comunicação entre o CLP e o controlador.

.. image:: custom_protocol_slave/027.png
   :width: 6in
   :align: center

2. Clique na interface 01_MC_EnableRobot e, em seguida, clique em “EnableRobot” para habilitar o robô. Se houver algum erro durante o uso, clique em “Reset” para reiniciar.

.. image:: custom_protocol_slave/028.png
   :width: 6in
   :align: center

3. Clique em “02_MC_ToolData” para entrar na interface de informações da ferramenta. Insira os parâmetros à esquerda e clique em WriteToolData para gravar as informações da ferramenta; à direita, clique em ReadToolData para ler as informações da ferramenta existentes.
   
.. image:: custom_protocol_slave/029.png
   :width: 6in
   :align: center

4. Clique em “03_MC_FrameData” para entrar na interface de informações da peça. Insira os parâmetros à esquerda e clique em WriteFrameData para gravar as informações da peça; à direita, clique em ReadFrameData para ler as informações da peça existentes.
   
.. image:: custom_protocol_slave/030.png
   :width: 6in
   :align: center

5. Clique em “04_MC_LoadData” para entrar na interface de informações de carga. Insira os parâmetros à esquerda e clique em WriteLoadData para gravar as informações de carga; à direita, clique em ReadLoadData para ler as informações de carga existentes.
   
.. image:: custom_protocol_slave/031.png
   :width: 6in
   :align: center

6. Clique em “05_MC_RobotReferenceDynamics” para entrar na interface de velocidade máxima e aceleração máxima do robô. Insira os parâmetros à esquerda e clique em WriteRobotRefD para gravar as informações de velocidade máxima e aceleração máxima; à direita, clique em ReadRobotRefD para ler as informações de velocidade máxima e aceleração máxima.
   
.. image:: custom_protocol_slave/032.png
   :width: 6in
   :align: center

7. Clique em “06_MC_Robot DefaultDynamics” para entrar na interface de velocidade padrão e aceleração padrão do robô. Insira os parâmetros à esquerda e clique em WriteRobotDefD para gravar as informações de velocidade padrão e aceleração padrão; à direita, clique em ReadRobotDefD para ler as informações de velocidade padrão e aceleração padrão.
   
.. image:: custom_protocol_slave/033.png
   :width: 6in
   :align: center

8. Clique em “07_MC_RobotSwLimits” para entrar na interface de limites de coordenadas. Insira os valores máximos e mínimos de limite à esquerda e clique em WriteRobotSwLimits para gravar as informações dos parâmetros de limite; à direita, clique em ReadRobotSwLimits para ler as informações dos parâmetros de limite existentes.
   
.. image:: custom_protocol_slave/034.png
   :width: 6in
   :align: center

9. Clique em “08_MC_ReadActualPosition” para entrar na interface de leitura de posição real. Clique em ReadPosition para ler as informações de posição existentes.
   
.. image:: custom_protocol_slave/035.png
   :width: 6in
   :align: center

10. Clique em “09_MC_MoveLinearAbsolute” para entrar na interface de movimento linear. Insira os parâmetros de coordenadas e clique em MoveLinearAbsolute para mover o robô linearmente para a posição alvo.
   
.. image:: custom_protocol_slave/036.png
   :width: 6in
   :align: center

11. Clique em “10_MC_MoveAxesAbsolute” para entrar na interface de movimento de coordenadas de eixo. Insira os parâmetros de coordenadas e clique em MoveAxesAbsolute para mover o robô para a posição alvo usando as coordenadas de eixo inseridas como ponto final.
   
.. image:: custom_protocol_slave/037.png
   :width: 6in
   :align: center

12. Clique em “11_MC_MoveDirectAbsolute” para entrar na interface de movimento direto. Insira os parâmetros de coordenadas e clique em MoveDirectAbsolute para mover o robô diretamente para a posição alvo usando os parâmetros inseridos como ponto final.
   
.. image:: custom_protocol_slave/038.png
   :width: 6in
   :align: center

13. Clique em “12_MC_Groups” para entrar na interface de operação de movimento direto. Aqui, clicar em GroupInterrupt pode interromper o movimento do robô durante o processo; clicar em GroupContinue faz o robô continuar a se mover para a posição alvo. Clique em GroupStop para parar (finalizar) a ação de movimento de posição em andamento. Se um alarme ou erro for acionado durante o processo, clique em GroupReset para reiniciar o erro do robô.
   
.. image:: custom_protocol_slave/039.png
   :width: 6in
   :align: center

14. Clique em “13_MC_PositionConversion” para entrar na interface de conversão de posição. XtoJ1 pode converter pose cartesiana para ângulos de junta; J1toX pode converter ângulos de junta para pose cartesiana.
   
.. image:: custom_protocol_slave/040.png
   :width: 6in
   :align: center

15. Clique em “14_MC_GroupJog” para entrar na interface de controle ponto a ponto do robô. Após a configuração, selecione o eixo a ser movido no menu suspenso e, em seguida, a direção de rotação do eixo. Clique em JogMove para realizar o movimento ponto a ponto. À direita, MC_ChangeSpeedOverride pode ajustar a velocidade de movimento do braço robótico.
   
.. image:: custom_protocol_slave/041.png
   :width: 6in
   :align: center

Configuração da IHM (Simulação Profinet)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Após abrir o programa, clique para selecionar “HMI_1[ktp700 Basic PN]” na árvore do projeto. Em seguida, na barra de menu, clique em “Online” → “Simulação” → “Iniciar”. Aguarde o software compilar e simular.

2. Após a simulação, as funções são as mesmas da tela Weintek (CC-Link IEF Basic). Consulte as instruções acima para a configuração.
   
.. image:: custom_protocol_slave/042.png
   :width: 6in
   :align: center   

.. image:: custom_protocol_slave/043.png
   :width: 6in
   :align: center

Instruções de Operação Relacionadas ao Modo Escravo do Robô
-----------------------------------------------------------------------

Carregar o Modo Escravo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Passo 1**: Abra o WebApp e vá para Configurações Iniciais -> Periféricos -> Comunicação com Placa -> Configuração Manual.

.. image:: custom_protocol_slave/047.png
   :width: 6in
   :align: center

.. centered:: Figura 17.3-1 Configuração Manual da Comunicação com a Placa

Primeiro, configure o endereço IP da placa FRJ-PCIeN. Se não for preenchido, a placa será iniciada com o IP padrão: 192.168.0.100. Atualmente, a configuração de IP se aplica apenas aos protocolos EIP e CC-Link IEF Basic. Para o protocolo PN, o IP é atribuído pelo mestre CLP ao escanear o dispositivo escravo.

.. note:: Após alterar o endereço IP na página, é necessário carregar o modo escravo para que a alteração entre em vigor.

Selecione sequencialmente as funções de mapeamento necessárias para DI, DO, AO (consulte o Apêndice I). O significado de cada parâmetro é o seguinte:

- DI é o controle do robô: o escravo do robô recebe sinais de entrada externos e executa as funções mapeadas;
  
- DO é a saída de status do robô: o escravo do robô envia sinais de status de volta ao mestre;
  
- AO é o feedback de status do robô: o escravo do robô envia dados de status de volta ao mestre. AO0 a AO15 são inteiros com sinal (int16), AO16 a AO31 são números de ponto flutuante de precisão simples (float).

**Passo 2**: Clique no botão “Configurar” para gerar o arquivo lua de protocolo aberto.

.. image:: custom_protocol_slave/048.png
   :width: 6in
   :align: center

.. centered:: Figura 17.3-2 Operação e Status do Dispositivo

.. note:: O arquivo lua de protocolo aberto suporta download. O arquivo lua de protocolo aberto pode ser importado na interface de configuração automática.

Um exemplo do programa gerado é mostrado abaixo:

.. code-block:: console
   :linenos:

   local id = 3 
   local ctrlDI = {0, 0, 0, 0, 0, 0}
   local funcDI = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
   local DOState = {0, 0, 0, 0, 0, 0, 0, 0}
   local AOState = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
   -- Launch the board communication process
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

**Passo 3**: Clique no botão “Carregar” para carregar o modo escravo do robô.

.. image:: custom_protocol_slave/049.png
   :width: 6in
   :align: center

.. centered:: Figura 17.3-3 Carregar Modo Escravo

.. note:: Após carregar com sucesso o modo escravo do robô, a função de autoinicialização é suportada. Se o modo remoto for necessário, descarregue o modo escravo primeiro.

**Passo 4**: Clique no botão da barra de status à direita para monitorar as informações de interação de DI, DO, AI e AO. As introduções dos parâmetros são as seguintes:

- CtrlDO é o valor de entrada do sinal de controle do DO do painel de controle do robô pelo dispositivo mestre;
  
- DI é o valor de entrada do sinal de controle do mestre externo;
  
- DO é o valor de saída do sinal de feedback do escravo do robô;
  
- AI é o valor de entrada do mestre externo. AI0 a AI15 são do tipo int16, AI16 a AI31 são do tipo float;
  
- AO é o valor de saída do escravo do robô. AO0 a AO15 são do tipo int16, AO16 a AO31 são do tipo float.

.. image:: custom_protocol_slave/050.png
   :width: 6in
   :align: center

.. centered:: Figura 17.3-4 Informações de Interação DI, DO, AI, AO

**Passo 5**: Após o carregamento, as instruções lua da placa podem ser geradas através de Programas de Ensinamento -> Instruções de Comunicação -> Placa, para implementar a configuração de DO, AO do escravo, obtenção de DI, AI do escravo e espera por DI, AI do escravo.

.. image:: custom_protocol_slave/051.png
   :width: 6in
   :align: center

.. centered:: Figura 17.3-5 Gerar Instruções Lua da Placa

:download:`Apêndice I: Tabela de Mapeamento de Endereços do Modo Escravo <../_static/_doc/Control box slave mode address comparison table.xlsx>`

Configuração do Ciclo de Comunicação da Placa
---------------------------------------------------------

O ciclo de comunicação da placa pode ser configurado através do host. Atualmente, apenas o firmware do protocolo PN é fornecido. A compatibilidade com os protocolos EIP, CClink ie basic e ECAT será adicionada posteriormente.

(1) Conecte diretamente a porta Ethernet do PC (sistema Win11) à porta Ethernet da placa. Abra o Device Assistant v1.1.0. Clique duas vezes em “Ethernet” e, em seguida, clique no botão “Atualizar” no canto superior esquerdo para escanear os dispositivos da placa atualmente conectados.

.. image:: custom_protocol_slave/060.png
   :width: 6in
   :align: center

.. image:: custom_protocol_slave/061.png
   :width: 6in
   :align: center

(2) Na interface de atualização de firmware, faça o upload da nova versão do firmware PN, clique no botão “Atualizar”. A mensagem “Atualização bem-sucedida” será exibida no canto inferior esquerdo.

.. image:: custom_protocol_slave/062.png
   :width: 6in
   :align: center

(3) Insira o ciclo de comunicação desejado (suporta 1~100ms), clique no botão “Definir”. A mensagem “Configuração do ciclo bem-sucedida” será exibida no canto inferior esquerdo.

.. image:: custom_protocol_slave/063.png
   :width: 6in
   :align: center

Apêndice
-------------------

Lista de Instruções
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
   :widths: 20 80
   :header-rows: 1
   :align: center

   * - Código do Comando
     - Descrição da Instrução

   * - 0x1000
     - Habilitar robô

   * - 0x1001
     - Redefinir todos os erros

   * - 0x1002
     - Parar movimento do robô

   * - 0x1003
     - Ler posição real

   * - 0x1004
     - Definir velocidade do robô

   * - 0x1005
     - Continuar movimento do robô

   * - 0x1006
     - Pausar movimento do robô

   * - 0x1007
     - Calcular posição cartesiana a partir da posição da junta

   * - 0x1008
     - Calcular posição da junta a partir da posição cartesiana

   * - 0x2000
     - Gravar informações da ferramenta

   * - 0x2001
     - Ler informações da ferramenta

   * - 0x2002
     - Gravar informações da peça

   * - 0x2003
     - Ler informações da peça

   * - 0x2004
     - Gravar informações de carga

   * - 0x2005
     - Ler informações de carga

   * - 0x2006
     - Gravar informações de dinâmica de referência

   * - 0x2007
     - Ler informações de dinâmica de referência

   * - 0x2008
     - Gravar informações de dinâmica padrão

   * - 0x2009
     - Ler informações de dinâmica padrão

   * - 0x2010
     - Gravar informações de limites suaves

   * - 0x2011
     - Ler informações de limites suaves

   * - 0x3000
     - MoveAxes (com base no ângulo da junta)

   * - 0x3001
     - MoveLinear

   * - 0x3002
     - MoveDirect (com base no sistema de coordenadas cartesiano)

   * - 0x3003
     - Movimento Jog

   * - 0x3004
     - Parar movimento Jog