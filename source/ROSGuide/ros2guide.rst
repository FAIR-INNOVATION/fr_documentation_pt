Prefácio
++++++++++
O fairino_hardware é uma API desenvolvida para robôs colaborativos FAIRINO baseada em ROS2, projetada para permitir que usuários iniciantes utilizem o SDK da FAIRINO de forma mais conveniente. Através da configuração de parâmetros padrão em arquivos de configuração, é possível atender a diferentes requisitos dos clientes.

fairino_hardware
++++++++++++++++++++++++++++
Esta seção explica como configurar o ambiente de execução do aplicativo.

Instalação do Ambiente Básico
----------------------------------------

Recomenda-se o uso no Ubuntu 22.04 LTS (Jammy). Após a instalação do sistema, é necessário instalar o ROS2. Recomenda-se o ros2-humble. Para a instalação completa do ROS2, consulte o tutorial: https://docs.ros.org/en/humble/index.html.
Antes de compilar oficialmente o fairino_hardware, também é necessário instalar o pacote oficial ros2_control. Para a instalação completa do ros2_control, consulte o tutorial: https://control.ros.org/humble/index.html. O site oficial oferece duas maneiras de instalar o ros2_control: instalação por comando e instalação por compilação do código fonte. Como a instalação por comando pode resultar em pacotes de funcionalidades incompletos, recomenda-se o uso da compilação do código fonte.

O processo de instalação do ROS2 (humble) é detalhado abaixo:

1. Abra uma janela de terminal

.. code-block:: shell
    :linenos:

    locale  # check for UTF-8

    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    locale  # verify settings

2. Configure as fontes de repositório

.. code-block:: shell
    :linenos:
    
    sudo apt install software-properties-common
    sudo add-apt-repository universe

    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

3. Instale o ROS2

.. code-block:: shell
    :linenos:

    sudo apt update
    sudo apt upgrade
    sudo apt install ros-humble-desktop

4. Por fim, instale as ferramentas de desenvolvimento

.. code-block:: shell
    :linenos:

    sudo apt install ros-dev-tools

O processo de instalação do ros2_control é detalhado abaixo:

1. Primeiro, faça o source dos recursos do ROS2

.. code-block:: shell
    :linenos:

    source /opt/ros/humble/setup.bash

2. Crie o espaço de trabalho do ros2_control e baixe os recursos

.. code-block:: shell
    :linenos:

    mkdir -p ~/ros2_control_ws/src
    cd ~/ros2_control_ws/
    wget https://raw.githubusercontent.com/ros-controls/ros2_control_ci/master/ros_controls.$ROS_DISTRO.repos
    vcs import src < ros_controls.$ROS_DISTRO.repos

3. Instale os pacotes de dependência

.. code-block:: shell
    :linenos:

    rosdep update --rosdistro=$ROS_DISTRO
    sudo apt-get update
    rosdep install --from-paths src --ignore-src -r -y

4. Compile o ros2_control

.. code-block:: shell
    :linenos:

    . /opt/ros/${ROS_DISTRO}/setup.sh
    colcon build --symlink-install

Compilação e Construção do fairino_hardware
-------------------------------------------------------
1. Crie um espaço de trabalho colcon
O fairino_hardware é composto por dois pacotes de funcionalidades: um é o pacote de funcionalidades de estrutura de dados personalizada `fairino_msgs`, e o outro é o pacote de funcionalidades principal `fairino_hardware`. Após instalar o ambiente básico, primeiro crie um espaço de trabalho colcon, por exemplo:

Primeiro, é necessário fazer o source dos recursos do ROS2 e do ros2_control

.. code-block:: shell
    :linenos:

    source /opt/ros/humble/setup.bash
    source ~/ros2_control_ws/install/setup.bash

Em seguida, crie o espaço de trabalho

.. code-block:: shell
    :linenos:

    cd ~/
    mkdir -p ros2_ws/src

2. Compile os pacotes de funcionalidades
Copie o código do pacote de instalação para o diretório `ros2_ws/src`. No diretório `ros2_ws`, execute o seguinte comando:

.. code-block:: shell
    :linenos:

    source ~/ros2_control_ws/install/setup.bash

Após a conclusão do comando, execute o seguinte comando:

.. code-block:: shell
    :linenos:

    colcon build --packages-select fairino_msgs

Após aguardar a conclusão da compilação do comando anterior, use o seguinte comando para compilar o `fairino_hardware`:

.. code-block::  shell
    :linenos:

    colcon build --packages-select fairino_hardware

Início Rápido
++++++++++++++

Processo de Inicialização
-------------------------------------------
No Ubuntu, abra um terminal e digite:

.. code-block::  shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    ros2 run fairino_hardware ros2_cmd_server

.. image:: img/fr_ros2_001.png
    :width: 6in
    :align: center

Processo para Visualizar o Feedback de Estado do Braço Robótico
------------------------------------------------------------------------------
O feedback de estado do braço robótico é publicado através de tópicos. Os usuários podem observar a atualização dos dados de estado usando comandos nativos do ROS2 ou escrever programas para obter esses dados. Abaixo, mostramos como observar os dados de estado do braço robótico usando comandos ROS2.

No Ubuntu, abra um terminal e digite:

.. code-block:: shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    ros2 topic echo /nonrt_state_data

Você verá os dados de estado sendo atualizados continuamente na janela do terminal, conforme mostrado na figura abaixo.

.. image:: img/fr_ros2_002.png
    :width: 6in
    :align: center

Processo para Enviar Comandos
---------------------------------------
No Ubuntu, abra um terminal e digite:

.. code-block:: shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    rqt

Após a execução do comando acima, uma interface GUI do rqt será exibida, conforme mostrado na figura abaixo.

.. image:: img/fr_ros2_003.png
    :width: 6in
    :align: center

Na interface GUI, selecione plugins -> service -> service caller. A interface a seguir será exibida. Selecione o serviço `/fairino_remote_command_service`. Na caixa de texto `expression`, insira a string de comando e clique em `call`. Você verá a mensagem de resposta na caixa de diálogo abaixo.

.. image:: img/fr_ros2_004.png
    :width: 6in
    :align: center

.. important:: 

   - Explicação das regras da string de entrada:

    O programa filtra internamente a forma da string de entrada. O formato da função de entrada deve ser `[Nome da função]()`. A string de parâmetros entre parênteses deve conter apenas letras, números, vírgulas e o sinal de menos. A presença de outros caracteres ou espaços resultará em erro.

   - Explicação do valor de retorno do comando:

    Exceto pelos comandos GET, que retornam uma string, os valores de retorno das outras funções são do tipo int. Geralmente, 0 indica um erro, 1 indica execução correta. Se outros valores aparecerem, consulte os códigos de erro definidos no SDK xmlrpc.

Processo para Modificar Parâmetros
----------------------------------------------------
Como o SDK simplificado é uma melhoria da interface SDK nativa, a simplificação é possível porque alguns parâmetros recebem valores padrão. No entanto, durante o uso real, pode haver situações em que os parâmetros padrão não atendam aos requisitos. Nesses casos, é possível modificar os valores dos parâmetros padrão correspondentes e, em seguida, carregá-los no nó.

No código fonte, existe um arquivo de parâmetros `fairino_remotecmdinterface_para.yaml`. Os parâmetros neste arquivo são os valores padrão predefinidos, usados para simplificar os parâmetros de entrada do comando. Eles podem ser modificados de acordo com suas necessidades específicas. Em seguida, use o comando para carregar os parâmetros dinamicamente: `ros2 param load fr_command_server ~/ros2_ws/src/fairino_hardware/fairino_remotecmdinterface_para.yaml`.

Explicação da API
++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /*
    Descrição da função: Armazena informações de um ponto de junta
    id - Número de identificação do ponto a ser armazenado, começando em 1. Observe que este ID é independente do ID do ponto CARTPoint.
    double j1-j6 - 6 posições das juntas, unidade em graus
    */
    int JNTPoint(int id, double j1, double j2, double j3, double j4, double j5, double j6)
    // Exemplo
    JNTPoint(1,10,11,12,13,14,15)

    /*
    Descrição da função: Armazena informações de um ponto cartesiano
    id - Número de identificação do ponto a ser armazenado, começando em 1. Observe que este ID é independente do ID do ponto JNTPoint.
    double x,y,z,rx,ry,rz - Informações do ponto cartesiano, posição em mm, ângulo em graus
    */
    int CARTPoint(int id, double x,y,z,rx,ry,rz)//Armazena um ponto no espaço cartesiano
    // Exemplo
    CARTPoint(1,100,110,200,0,0,0)

    /*
    Descrição da função: Obtém a posição do ponto da junta ou cartesiano para o ponto com o número de sequência especificado
    string name - 'JNT' ou 'CART'. 'JNT' representa obter informações do ponto de junta, 'CART' representa obter informações do ponto cartesiano.
    int id - Número de identificação do ponto, começando em 1
    */
    string GET(string name, int id)//Obtém o conteúdo do ponto com o ID correspondente. name pode ser JNT ou CART.
    // Exemplo
    GET(JNT,1)

    /*
    Descrição da função: Alterna o modo de arrastagem
    uint8_t state - 1-ativar modo de arrastagem, 0-desativar modo de arrastagem
    */
    int DragTeachSwitch(uint8_t state)
    // Exemplo
    DragTeachSwitch(0)

    /*
    Descrição da função: Alterna a habilitação do braço robótico
    uint8_t state - 1-habilitar braço robótico, 0-desabilitar braço robótico
    */
    int RobotEnable(uint8_t state)
    // Exemplo
    RobotEnable(1)

    /*
    Descrição da função: Alterna o modo
    uint8_t state - 1-modo manual, 0-modo automático
    */
    int Mode(uint8_t state)
    // Exemplo
    Mode(1)

    /*
    Descrição da função: Define a velocidade do braço robótico no modo atual
    float vel - Porcentagem de velocidade, faixa de 1 a 100
    */
    int SetSpeed(float vel)
    // Exemplo
    SetSpeed(10)

    /*
    Descrição da função: Define e carrega o sistema de coordenadas da ferramenta com o número de sequência especificado
    int id - Número do sistema de coordenadas da ferramenta, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da ferramenta
    */
    int SetToolCoord(int id, float x,float y, float z,float rx,float ry,float rz)
    // Exemplo
    SetToolCoord(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define a lista de sistemas de coordenadas da ferramenta
    int id - Número do sistema de coordenadas da ferramenta, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da ferramenta
    */
    int SetToolList(int id, float x,float y, float z,float rx,float ry,float rz );
    // Exemplo
    SetToolList(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define o sistema de coordenadas da ferramenta externa
    int id - Número do sistema de coordenadas da ferramenta, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da ferramenta externa
    */
    int SetExToolCoord(int id, float x,float y, float z,float rx,float ry,float rz);	
    // Exemplo
    SetExToolCoord(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define a lista de sistemas de coordenadas da ferramenta externa
    int id - Número do sistema de coordenadas da ferramenta, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da ferramenta externa
    */
    int SetExToolList(int id, float x,float y, float z,float rx,float ry,float rz);
    // Exemplo
    SetExToolList(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define o sistema de coordenadas da peça
    int id - Número do sistema de coordenadas da peça, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da peça
    */
    int SetWObjCoord(int id, float x,float y, float z,float rx,float ry,float rz);
    // Exemplo
    SetWObjCoord(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define a lista de sistemas de coordenadas da peça
    int id - Número do sistema de coordenadas da peça, faixa 1-15
    float x,y,z,rx,ry,rz - Informações de deslocamento do sistema de coordenadas da peça
    */
    int SetWObjList(int id, float x,float y, float z,float rx,float ry,float rz);
    // Exemplo
    SetWObjList(1,0,0,0,0,0,0)

    /*
    Descrição da função: Define o peso da carga de extremidade
    float weight - Peso da carga, unidade kg
    */
    int SetLoadWeight(float weight);
    // Exemplo
    SetLoadWeight(3.5)

    /*
    Descrição da função: Define as coordenadas do centro de gravidade da carga de extremidade
    float x,y,z - Coordenadas do centro de gravidade, unidade mm
    */
    int SetLoadCoord(float x,float y,float z);
    // Exemplo
    SetLoadCoord(10,20,30)

    /*
    Descrição da função: Define o modo de instalação do robô
    uint8_t install - Modo de instalação, 0-montagem normal, 1-montagem lateral, 2-montagem invertida
    */
    int SetRobotInstallPos(uint8_t install);
    // Exemplo
    SetRobotInstallPos(0)

    /*
    Descrição da função: Define o ângulo de instalação do robô, instalação livre
    double yangle - Ângulo de inclinação
    double zangle - Ângulo de rotação
    */
    int SetRobotInstallAngle(double yangle,double zangle);
    // Exemplo
    SetRobotInstallAngle(90,0)


    //Configurações de segurança
    /*
    Descrição da função: Define o nível de colisão do robô
    float level1-level6 - Níveis de colisão para os eixos 1-6, faixa de 1 a 10
    */
    int SetAnticollision(float level1, float level2, float level3, float level4, float level5, folat level6);
    // Exemplo
    SetAnticollision(1,1,1,1,1,1)

    /*
	 * @brief  Define a estratégia pós-colisão
	 * @param  [in] strategy  0-parar com erro, 1-continuar executando
	 * @param  [in] safeTime  Tempo de parada segura [1000 - 2000] ms
	 * @param  [in] safeDistance  Distância de parada segura [1-150] mm
	 * @param  [in] safeVel Velocidade segura [50-250] mm/s
	 * @param  [in] safetyMargin  Fator de segurança j1-j6 [1-10]
	 * @return  Código de erro
    */
	int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel, int safetyMargin[])
    // Exemplo
    SetCollisionStrategy(1)

    /*
	 * @brief Define o método de detecção de colisão do robô
	 * @param [in] method Método de detecção de colisão: 0-modo corrente; 1-duplo encoder; 2-corrente e duplo encoder simultaneamente
     * @param [in] thresholdMode Modo de limite do nível de colisão; 0-modo de limite fixo do nível de colisão; 1-limite de detecção de colisão personalizado
	 * @return  Código de erro
    */
	int SetCollisionDetectionMethod(int method, int thresholdMode);
    // Exemplo
    SetCollisionDetectionMethod(0,0)


    /*
	 * @brief Ativa/desativa a detecção de colisão estática
	 * @param  [in] status 0-desativar; 1-ativar
	 * @return  Código de erro
    */
	int SetStaticCollisionOnOff(int status);
    // Exemplo
    SetStaticCollisionOnOff(1)



    /*
	 * @brief Detecção de potência do torque das juntas
	 * @param  [in] status 0-desativar; 1-ativar
	 * @param  [in] power Potência máxima definida (W);
	 * @return  Código de erro
    */
	int SetPowerLimit(int status, double power);
    //Exemplo
    SetPowerLimit(1,100)

    /*
	 * @brief  Configura o sensor de força
	 * @param  [in] company  Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa Aeroespacial 11, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin, 23-NBIT, 24-Xinjingcheng (XJC), 26-NSR
	 * @param  [in] device  Número do dispositivo, Kunwei(0-KWR75B), Instituto Aeroespacial 11(0-MCS6A-200-4), ATI(0-AXIA80-M8), Zhongke Midian(0-MST2010), Weihang Minxin(0-WHC6L-YB-10A), NBIT(0-XLH93003ACS), Xinjingcheng XJC(0-XJC-6F-D82), NSR(0-NSR-FTSensorA)
	 * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
	 * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
	 * @return  Código de erro
    */
	int FT_SetConfig(int company, int device, int softvesion, int bus);
    // Exemplo
    FT_SetConfig(0,1,0,0)



    /*
	 * @brief  Obtém a configuração do sensor de força
	 * @param  [out] company  Fabricante do sensor de força, a definir
	 * @param  [out] device  Número do dispositivo, não usado no momento, padrão 0
	 * @param  [out] softvesion  Número da versão do software, não usado no momento, padrão 0
	 * @param  [out] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
	 * @return  Código de erro
    */
	int FT_GetConfig(int *company, int *device, int *softvesion, int *bus);
    // Exemplo
    FT_GetConfig()


    /*
	 * @brief  Ativa o sensor de força
	 * @param  [in] act  0-reset, 1-ativar
	 * @return  Código de erro
    */
	int FT_Activate(uint8_t act);
    // Exemplo
    FT_Activate(1)


    /*
	 * @brief  Zera o sensor de força
	 * @param  [in] act  0-remover zero, 1-correção de zero
	 * @return  Código de erro
    */
	int FT_SetZero(uint8_t act);
    // Exemplo
    FT_SetZero(1)

    /*
	 * @brief  Proteção contra colisão
	 * @param  [in] flag 0-desativar proteção contra colisão, 1-ativar proteção contra colisão
	 * @param  [in] sensor_id  Número do sensor de força
	 * @param  [in] select  Seleciona se os seis graus de liberdade são detectados para colisão, 0-não detectar, 1-detectar
	 * @param  [in] ft  Força/torque de colisão, fx, fy, fz, tx, ty, tz
	 * @param  [in] max_threshold  Limite máximo
	 * @param  [in] min_threshold  Limite mínimo
	 * @note   Faixa de detecção de força/torque: (ft-min_threshold, ft+max_threshold)
	 * @return  Código de erro
    */
	int FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]);
    // Exemplo
    FT_Guard(1,1,0,0,1,0,0,0,0,0,100,0,0,0,0,0,200,0,0,0,0,0,50,0,0,0)


    /*
	 * @brief  Controle de força constante
	 * @param  [in] flag 0-desativar controle de força constante, 1-ativar controle de força constante
	 * @param  [in] sensor_id  Número do sensor de força
	 * @param  [in] select  Seleciona se os seis graus de liberdade são detectados para colisão, 0-não detectar, 1-detectar
	 * @param  [in] ft  Força/torque de colisão, fx, fy, fz, tx, ty, tz
	 * @param  [in] ft_pid  Parâmetros PID de força, parâmetros PID de torque
	 * @param  [in] adj_sign  Controle de ativação/desativação adaptativa, 0-desativar, 1-ativar
	 * @param  [in] ILC_sign  Controle de ativação/desativação ILC, 0-parar, 1-treinar, 2-operação real
	 * @param  [in] max_dis  Distância máxima de ajuste, unidade mm
	 * @param  [in] max_ang  Ângulo máximo de ajuste, unidade graus
	 * @param  [in] filter_Sign  Flag de ativação do filtro 0-desativar; 1-ativar, padrão desativado
     * @param  [in] posAdapt_sign  Flag de ativação da conformidade de postura 0-desativar; 1-ativar, padrão desativado
     * @param  [in] isNoBlock  Flag de bloqueio, 0-bloqueado; 1-não bloqueado
	 * @return  Código de erro
    */
	int FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float ft_pid[6], uint8_t adj_sign, uint8_t ILC_sign, float max_dis, float max_ang, int filter_Sign = 0, int posAdapt_sign = 0, int isNoBlock = 0);
    // Exemplo
    FT_Control(1,1,0,0,1,0,0,0,0,0,-10,0,0,0,0.0005,0,0,0,0,0,0,0,100,10,0,0,0) 


    /*
	 * @brief  Ativa o controle de complacência
	 * @param  [in] p  Coeficiente de ajuste de posição ou coeficiente de complacência
	 * @param  [in] force  Limite de força para ativação da complacência, unidade N
	 * @return  Código de erro
    */
	int FT_ComplianceStart(float p, float force);
    // Exemplo
    FT_ComplianceStart(0.005,20)


    /**
	 * @brief  Desativa o controle de complacência
	 * @return  Código de erro
    */
	int FT_ComplianceStop();
    // Exemplo
    FT_ComplianceStop()

    /*
    Descrição da função: Define o limite positivo. Observe que o valor definido deve estar dentro do limite rígido.
    float limit1-limit6 - Valores de limite para as 6 juntas
    */
    int SetLimitPositive(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
    // Exemplo
    SetLimitPositve(100,90,90,90,90,90)

    /*
    Descrição da função: Define o limite negativo. Observe que o valor definido deve estar dentro do limite rígido.
    float limit1-limit6 - Valores de limite para as 6 juntas
    */
    int SetLimitNegative(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
    // Exemplo
    SetLimitNegative(-100,-90,-90,-90,-90,-90)

    /*
    Descrição da função: Limpa o estado de erro
    */
    int ResetAllError();

    /*
    Descrição da função: Alterna a compensação de fricção das juntas
    uint8_t state - 0-desativar, 1-ativar
    */
    int FrictionCompensationOnOff(uint8_t state);
    // Exemplo
    FrictionCompensationOnOff(1)

    /*
    Descrição da função: Define os coeficientes de compensação de fricção das juntas - montagem normal
    float coeff1-coeff6 - 6 coeficientes de compensação das juntas, faixa de 0 a 1
    */
    int SetFrictionValue_level(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // Exemplo
    SetFrictionValue_level(1,1,1,1,1,1)

    /*
    Descrição da função: Define os coeficientes de compensação de fricção das juntas - montagem lateral
    float coeff1-coeff6 - 6 coeficientes de compensação das juntas, faixa de 0 a 1
    */
    int SetFrictionValue_wall(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // Exemplo
    SetFrictionValue_wall(0.5,0.5,0.5,0.5,0.5,0.5)

    /*
    Descrição da função: Define os coeficientes de compensação de fricção das juntas - montagem invertida
    float coeff1-coeff6 - 6 coeficientes de compensação das juntas, faixa de 0 a 1
    */
    int SetFrictionValue_ceiling(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // Exemplo
    SetFrictionValue_ceiling(0.5,0.5,0.5,0.5,0.5,0.5)


    //Controle de periféricos
    /*
    Descrição da função: Ativa a garra
    int index - Número da garra
    uint8_t act - 0-reset, 1-ativar
    */
    int ActGripper(int index,uint8_t act);
    // Exemplo
    ActGripper(1,1)

    /*
    Descrição da função: Controla a garra
    int index - Número da garra
    int pos - Porcentagem de posição, faixa de 0 a 100
    */
    int MoveGripper(int index,int pos);
    // Exemplo
    MoveGripper(1,10)


    //Controle de IO
    /*
    Descrição da função: Define a saída digital do painel de controle
    int id - Número do IO, faixa 0-15
    uint_t status - 0-desativar, 1-ativar
    */
    int SetDO(int id,uint8_t status);
    // Exemplo
    SetDO(1,1)

    /*
    Descrição da função: Define a saída digital da ferramenta
    int id - Número do IO, faixa 0-1
    uint_t status - 0-desativar, 1-ativar
    */
    int SetToolDO(int id,uint8_t status);
    // Exemplo
    SetToolDO(0,1)

    /*
    Descrição da função: Define a saída analógica do painel de controle
    int id - Número do IO, faixa 0-1
    float value - Porcentagem do valor de corrente ou tensão, faixa 0-100
    */
    int SetAO(int id,float value);
    // Exemplo
    SetAO(1,100)

    /*
    Descrição da função: Define a saída analógica da ferramenta
    int id - Número do IO, faixa 0
    float value - Porcentagem do valor de corrente ou tensão, faixa 0-100
    */
    int SetToolAO(int id,float value);
    // Exemplo
    SetToolAO(0,100)


    //Instruções de movimento
    /*
    Descrição da função: Movimento incremental do robô (JOG)
    uint8_t ref - 0-JOG de junta, 2-JOG no sistema de coordenadas base, 4-JOG no sistema de coordenadas da ferramenta, 8-JOG no sistema de coordenadas da peça
    uint8_t nb - 1-junta 1 (ou eixo x), 2-junta 2 (ou eixo y), 3-junta 3 (ou eixo z), 4-junta 4 (ou rotação em torno do eixo x), 5-junta 5 (ou rotação em torno do eixo y), 6-junta 6 (ou rotação em torno do eixo z)
    uint8_t dir - 0-direção negativa, 1-direção positiva
    float vel - Porcentagem de velocidade, faixa de 0 a 100
    */
    int StartJOG(uint8_t ref, uin8_t nb, uint8_t dir, float vel);
    // Exemplo
    StartJOG(1,1,1,10)

    /*
    Descrição da função: Para o movimento incremental do robô
    uint8_t ref - 0-parar JOG de junta, 2-parar JOG no sistema de coordenadas base, 4-parar JOG no sistema de coordenadas da ferramenta, 8-parar JOG no sistema de coordenadas da peça
    */
    int StopJOG(uint8_t ref);
    // Exemplo
    StopJOG(1)

    /*
    Descrição da função: Para o movimento incremental do robô imediatamente
    */
    int ImmStopJOG();

    /*
    Descrição da função: Movimento no espaço articular
    string point_name - Nome do ponto pré-armazenado, por exemplo, JNT1 é o ponto de junta com número de sequência 1, CART1 é o ponto cartesiano com número de sequência 1. O comando MoveJ suporta a entrada de pontos de junta ou pontos cartesianos. Observe que, como o comando MoveJ tem sistemas de coordenadas de ferramenta e peça especificados nos parâmetros padrão, se os números desses sistemas de coordenadas não corresponderem aos atualmente carregados, o comando resultará em um erro. É necessário modificar os parâmetros do sistema de coordenadas nos parâmetros padrão e carregar os parâmetros novamente antes de executar esta instrução de movimento.
    float vel - Porcentagem de velocidade do comando, faixa 0-100
    int tool - Número do sistema de coordenadas da ferramenta
    int user - Número do sistema de coordenadas da peça
    double expos1 - Posição do eixo externo 1
    double expos2 - Posição do eixo externo 2
    double expos3 - Posição do eixo externo 3
    double expos4 - Posição do eixo externo 4
    */
    int MoveJ(string point_name, float vel,int tool, int user,double expos1,double expos2,double expos3,double expos4);//point_name é o nome do ponto pré-armazenado
    // Exemplo
    MoveJ(JNT1,10,1,1,0,0,0,0)

    /*
    Descrição da função: Movimento linear no espaço cartesiano
    string point_name - Nome do ponto pré-armazenado, por exemplo, JNT1 é o ponto de junta com número de sequência 1, CART1 é o ponto cartesiano com número de sequência 1. O comando MoveL suporta a entrada de pontos de junta ou pontos cartesianos. Observe que, como o comando MoveL tem sistemas de coordenadas de ferramenta e peça especificados nos parâmetros padrão, se os números desses sistemas de coordenadas não corresponderem aos atualmente carregados, o comando resultará em um erro. É necessário modificar os parâmetros do sistema de coordenadas nos parâmetros padrão e carregar os parâmetros novamente antes de executar esta instrução de movimento.
    float vel - Porcentagem de velocidade do comando, faixa 0-100
    int tool - Número do sistema de coordenadas da ferramenta
    int user - Número do sistema de coordenadas da peça
    double expos1 - Posição do eixo externo 1
    double expos2 - Posição do eixo externo 2
    double expos3 - Posição do eixo externo 3
    double expos4 - Posição do eixo externo 4
    */
    int MoveL(string point_name,float vel,int tool,int user,double expos1,double expos2,double expos3,double expos4);
    // Exemplo
    MoveL(CART1,10,1,1,0,0,0,0)

    /*
    Descrição da função: Movimento de arco no espaço cartesiano
    string point1_name point2_name - Nomes dos pontos pré-armazenados, por exemplo, JNT1 é o ponto de junta com número de sequência 1, CART1 é o ponto cartesiano com número de sequência 1. O comando MoveC suporta a entrada de pontos de junta ou pontos cartesianos, mas os dois pontos devem ser do mesmo tipo, ou seja, não suporta o primeiro ponto como ponto de junta e o segundo como ponto cartesiano. Observe que, como o comando MoveC tem sistemas de coordenadas de ferramenta e peça especificados nos parâmetros padrão, se os números desses sistemas de coordenadas não corresponderem aos atualmente carregados, o comando resultará em um erro. É necessário modificar os parâmetros do sistema de coordenadas nos parâmetros padrão e carregar os parâmetros novamente antes de executar esta instrução de movimento.
    float vel - Porcentagem de velocidade do comando, faixa 0-100
    int tool - Número do sistema de coordenadas da ferramenta
    int user - Número do sistema de coordenadas da peça
    double expos1 - Posição do eixo externo 1 do ponto 1
    double expos2 - Posição do eixo externo 2 do ponto 1
    double expos3 - Posição do eixo externo 3 do ponto 1
    double expos4 - Posição do eixo externo 4 do ponto 1
    double expos1 - Posição do eixo externo 1 do ponto 2
    double expos2 - Posição do eixo externo 2 do ponto 2
    double expos3 - Posição do eixo externo 3 do ponto 2
    double expos4 - Posição do eixo externo 4 do ponto 2
    */
    int MoveC(string point1_name,string point2_name, float vel, int tool,int user,double expos1,double expos2,double expos3,double expos4,double expos1,double expos2,double expos3,double expos4);
    // Exemplo
    MoveC(JNT1,JNT2,10,1,1,0,0,0,0,0,0,0,0)

    /*
    Descrição da função: Início do movimento spline
    */
    int SplineStart();

    /*
    Descrição da função: Movimento spline no espaço articular. Esta instrução só suporta a entrada de dados de junta como JNT1. A entrada de pontos cartesianos resultará em erro.
    string point_name - Nome do ponto pré-armazenado, por exemplo, JNT1 é o ponto de junta com número de sequência 1.
    float vel - Porcentagem de velocidade, faixa 0-100
    */
    int SplinePTP(string point_name, float vel);
    // Exemplo
    SplinePTP(JNT2,10)

    /*
    Descrição da função: Fim do movimento spline
    */
    int SplineEnd();

    /*
    Descrição da função: Início do movimento spline no espaço cartesiano
    uint8_t ctlpoint - 0-trajetória passa pelos pontos de caminho, 1-trajetória não passa pelos pontos de controle. Pelo menos 4 pontos são necessários.
    */
    int NewSplineStart(uint8_t ctlpoint);
    // Exemplo
    NewSplineStart(1)

    /*
    Descrição da função: Movimento spline no espaço cartesiano. Só é possível inserir pontos cartesianos como CART1. A entrada de pontos de junta resultará em erro.
    string point_name - Nome do ponto pré-armazenado, por exemplo, CART1 é o ponto cartesiano com número de sequência 1.
    float vel - Porcentagem de velocidade, faixa 0-100
    int lastflag - 0-não é o último ponto, 1-é o último ponto
    */
    int NewSplinePoint(string point_name, float vel, int lastflag);
    // Exemplo
    NewSplinePoint(JNT2,20,0)

    /*
    Descrição da função: Fim do movimento spline no espaço cartesiano
    */
    int NewSplineEnd();

    /*
    Descrição da função: Para o movimento
    */
    int StopMotion();

    /*
    Descrição da função: Inicia o deslocamento geral de pontos
    int flag - 0-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    double x,y,z,rx,ry,rz - Valores de deslocamento da pose
    */
    int PointsOffsetEnable(int flag,double x,double y,double z,double rx,double ry,double rz);
    // Exemplo
    PointsOffsetEnable(1,10,10,10,0,0,0)

    /*
    Descrição da função: Termina o deslocamento geral de pontos
    */
    int PointsOffsetDisable();