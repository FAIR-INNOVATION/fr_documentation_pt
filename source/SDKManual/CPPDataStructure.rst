Descrição das Estruturas de Dados
================================================

.. toctree::
    :maxdepth: 5

Tipo de Valor de Retorno da Chamada de Interface
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    typedef int errno_t;

Tipo de Dados de Posição Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Tipo de dados de posição articular
    */
    typedef struct
    {
        double jPos[6];   /* Posições das seis juntas, em graus */
    } JointPos;

Tipo de Dados de Posição no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Tipo de dados de posição no espaço cartesiano
    */
    typedef struct
    {
        double x;    /* Coordenada do eixo X, em mm */
        double y;    /* Coordenada do eixo Y, em mm */
        double z;    /* Coordenada do eixo Z, em mm */
    } DescTran;

Tipo de Dados de Atitude de Ângulos de Euler
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Tipo de dados de atitude de ângulos de Euler
    */
    typedef struct
    {
        double rx;   /* Ângulo de rotação em torno do eixo X fixo, em graus */
        double ry;   /* Ângulo de rotação em torno do eixo Y fixo, em graus */
        double rz;   /* Ângulo de rotação em torno do eixo Z fixo, em graus */
    } Rpy;

Tipo de Dados de Pose no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    *@brief Tipo de pose no espaço cartesiano
    */
    typedef struct
    {
        DescTran tran;      /* Posição no espaço cartesiano */
        Rpy rpy;            /* Atitude no espaço cartesiano */
    } DescPose;

Tipo de Dados de Posição do Eixo Estendido
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Tipo de dados de posição do eixo estendido
    */
    typedef struct
    {
        double ePos[4];   /* Posições dos quatro eixos estendidos, em mm */
    } ExaxisPos;

Tipo de Dados do Sensor de Torque
+++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Componentes de força e torque do sensor de força
    */
    typedef struct
    {
        double fx;  /* Componente de força ao longo do eixo X, em N */
        double fy;  /* Componente de força ao longo do eixo Y, em N */
        double fz;  /* Componente de força ao longo do eixo Z, em N */
        double tx;  /* Componente de torque em torno do eixo X, em Nm */
        double ty;  /* Componente de torque em torno do eixo Y, em Nm */
        double tz;  /* Componente de torque em torno do eixo Z, em Nm */
    } ForceTorque;

Tipo de Dados de Parâmetros da Espiral
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Tipo de dados de parâmetros da espiral
    */
    typedef struct
    {
        int    circle_num;           /* Número de voltas da espiral */
        float  circle_angle;         /* Ângulo de inclinação da espiral */
        float  rad_init;             /* Raio inicial da espiral, em mm */
        float  rad_add;              /* Incremento do raio */
        float  rotaxis_add;          /* Incremento na direção do eixo de rotação */
        int    rot_direction;        /* Direção de rotação, 0-horário, 1-anti-horário */
        int    velAccMode;           /* Modo de parâmetro de velocidade/aceleração: 0-velocidade angular constante; 1-velocidade linear constante */
    } SpiralParam;

Pacote de feedback do estado do controlador
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionchanged:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Pacote de feedback do estado do controlador
     */
    typedef struct _ROBOT_STATE_PKG
    {
      uint16_t frame_head;   // Cabeçalho do quadro, definido como 0x5A5A
      uint8_t frame_cnt;     // Contagem do quadro, contagem cíclica 0-255
      uint16_t data_len;     // Comprimento do conteúdo dos dados
      uint8_t program_state;   // Estado de execução do programa, 1-parado; 2-em execução; 3-pausado;
      uint8_t robot_state;    // Estado de movimento do robô, 1-parado; 2-em execução; 3-pausado; 4-arrasto
      int   main_code;     // Código de falha principal
      int   sub_code;      // Código de falha secundário
      uint8_t robot_mode;    // Modo do robô, 1-modo manual; 0-modo automático;
      double  jt_cur_pos[6];   // Posição atual das 6 juntas, unidade deg
      double  tl_cur_pos[6];   // Posição atual da ferramenta (TCP)
            // tl_cur_pos[0], posição ao longo do eixo x, unidade mm,
            // tl_cur_pos[1], posição ao longo do eixo y, unidade mm,
            // tl_cur_pos[2], posição ao longo do eixo z, unidade mm,
            // tl_cur_pos[3], ângulo de rotação em torno do eixo X fixo, unidade deg
            // tl_cur_pos[4], ângulo de rotação em torno do eixo Y fixo, unidade deg
            // tl_cur_pos[5], ângulo de rotação em torno do eixo Z fixo, unidade deg
      double  flange_cur_pos[6]; // Posição atual da flange final
            // flange_cur_pos[0], posição ao longo do eixo x, unidade mm,
            // flange_cur_pos[1], posição ao longo do eixo y, unidade mm,
            // flange_cur_pos[2], posição ao longo do eixo z, unidade mm,
            // flange_cur_pos[3], ângulo de rotação em torno do eixo X fixo, unidade deg
            // flange_cur_pos[4], ângulo de rotação em torno do eixo Y fixo, unidade deg
            // flange_cur_pos[5], ângulo de rotação em torno do eixo Z fixo, unidade deg
      double  actual_qd[6];    // Velocidade atual das 6 juntas, unidade deg/s
      double  actual_qdd[6];    // Aceleração atual das 6 juntas, unidade deg/s^2
      double  target_TCP_CmpSpeed[2];
            // target_TCP_CmpSpeed[0], Velocidade de instrução composta TCP (posição), unidade mm/s
            // target_TCP_CmpSpeed[1], Velocidade de instrução composta TCP (orientação), unidade deg/s */
      double  target_TCP_Speed[6];  // Velocidade de instrução TCP
              // target_TCP_Speed[0], velocidade ao longo do eixo x, unidade mm/s,
              // target_TCP_Speed[1], velocidade ao longo do eixo y, unidade mm/s,
              // target_TCP_Speed[2], velocidade ao longo do eixo z, unidade mm/s,
              // target_TCP_Speed[3], velocidade angular em torno do eixo X fixo, unidade deg/s
              // target_TCP_Speed[4], velocidade angular em torno do eixo Y fixo, unidade deg/s
              // target_TCP_Speed[5], velocidade angular em torno do eixo Z fixo, unidade deg/s */
      double  actual_TCP_CmpSpeed[2];
              // actual_TCP_CmpSpeed[0], Velocidade real composta TCP (posição), unidade mm/s
              // actual_TCP_CmpSpeed[1], Velocidade real composta TCP (orientação), unidade deg/s */
      double  actual_TCP_Speed[6];  // Velocidade real TCP
              // actual_TCP_Speed[0], velocidade ao longo do eixo x, unidade mm/s,
              // actual_TCP_Speed[1], velocidade ao longo do eixo y, unidade mm/s,
              // actual_TCP_Speed[2], velocidade ao longo do eixo z, unidade mm/s,
              // actual_TCP_Speed[3], velocidade angular em torno do eixo X fixo, unidade deg/s
              // actual_TCP_Speed[4], velocidade angular em torno do eixo Y fixo, unidade deg/s
              // actual_TCP_Speed[5], velocidade angular em torno do eixo Z fixo, unidade deg/s
      double  jt_cur_tor[6];    // Torque atual das 6 juntas, unidade N·m
      int   tool;         // Número do sistema de coordenada da ferramenta aplicado
      int   user;         // Número do sistema de coordenada da peça aplicado
      uint8_t cl_dgt_output_h;   // Saída IO digital da caixa de controle 15-8
      uint8_t cl_dgt_output_l;   // Saída IO digital da caixa de controle 7-0
      uint8_t tl_dgt_output_l;   // Saída IO digital da ferramenta 7-0, apenas bits 0-1 válidos
      uint8_t cl_dgt_input_h;    // Entrada IO digital da caixa de controle 15-8
      uint8_t cl_dgt_input_l;    // Entrada IO digital da caixa de controle 7-0
      uint8_t tl_dgt_input_l;    // Entrada IO digital da ferramenta 7-0, apenas bits 0-1 válidos
      uint16_t cl_analog_input[2]; // cl_analog_input[0], Entrada analógica da caixa de controle 0
                    // cl_analog_input[1], Entrada analógica da caixa de controle 1
      uint16_t tl_anglog_input;   // Entrada analógica da ferramenta
      double  ft_sensor_raw_data[6]; // Dados brutos do sensor de força
              // ft_sensor_raw_data[0], força ao longo do eixo x, unidade N
              // ft_sensor_raw_data[1], força ao longo do eixo y, unidade N
              // ft_sensor_raw_data[2], força ao longo do eixo z, unidade N
              // ft_sensor_raw_data[3], torque em torno do eixo x, unidade Nm
              // ft_sensor_raw_data[4], torque em torno do eixo y, unidade Nm
              // ft_sensor_raw_data[5], torque em torno do eixo z, unidade Nm
      double  ft_sensor_data[6];    // Dados do sensor de força
              // ft_sensor_data[0], força ao longo do eixo x, unidade N
              // ft_sensor_data[1], força ao longo do eixo y, unidade N
              // ft_sensor_data[2], força ao longo do eixo z, unidade N
              // ft_sensor_data[3], torque em torno do eixo x, unidade Nm
              // ft_sensor_data[4], torque em torno do eixo y, unidade Nm
              // ft_sensor_data[5], torque em torno do eixo z, unidade Nm
      uint8_t ft_sensor_active;   // Estado de ativação do sensor de força, 0-reset, 1-ativado
      uint8_t EmergencyStop;    // Flag de parada de emergência, 0-parada de emergência não acionada, 1-parada de emergência acionada
      int   motion_done;     // Sinal de movimento concluído, 1-concluído, 0-não concluído
      uint8_t gripper_motiondone; // Sinal de conclusão do movimento da garra, 1-concluído, 0-não concluído
      int   mc_queue_len;     // Comprimento da fila de instruções de movimento
      uint8_t collisionState;    // Detecção de colisão, 1-colisão, 0-sem colisão
      int   trajectory_pnum;   // Número do ponto da trajetória
      uint8_t safety_stop0_state; // Sinal de parada de segurança SI0
      uint8_t safety_stop1_state; // Sinal de parada de segurança SI1
      uint8_t gripper_fault_id;   // ID da garra com erro
      uint16_t gripper_fault;    // Falha da garra
      uint16_t gripper_active;    // Estado de ativação da garra
      uint8_t gripper_position;   // Posição da garra
      int8_t  gripper_speed;    // Velocidade da garra
      int8_t  gripper_current;   // Corrente da garra
      int   gripper_temp;     // Temperatura da garra
      int   gripper_voltage;   // Tensão da garra
      robot_aux_state aux_state;   // Estado do eixo de extensão 485
      EXT_AXIS_STATUS extAxisStatus[4]; // Estado do eixo de extensão UDP
      uint16_t extDIState[8];     // Entrada DI estendida
      uint16_t extDOState[8];     // Saída DO estendida
      uint16_t extAIState[4];     // Entrada AI estendida
      uint16_t extAOState[4];     // Saída AO estendida
      int rbtEnableState;       // Estado de habilitação do robô
      double  jointDriverTorque[6];    // Torque do driver da junta do robô
      double  jointDriverTemperature[6];  // Temperatura do driver da junta do robô
      RobotTime robotTime;       // Tempo do sistema do robô
      int softwareUpgradeState;    // Estado de atualização de software do robô
      uint16_t endLuaErrCode;     // Estado de execução LUA da extremidade
      uint16_t cl_analog_output[2]; // Saída analógica da caixa de controle
      uint16_t tl_analog_output;    // Saída analógica da ferramenta
      float gripperRotNum;       // Número atual de rotações da garra rotativa
      uint8_t gripperRotSpeed;     // Percentual de velocidade atual da garra rotativa
      uint8_t gripperRotTorque;    // Percentual de torque atual da garra rotativa
      WELDING_BREAKOFF_STATE weldingBreakOffState; // Estado de interrupção da soldagem
      double jt_tgt_tor[6];         // Torque de instrução da junta
      int smartToolState;          // Estado do botão da SmartTool
      float wideVoltageCtrlBoxTemp;     // Temperatura da caixa de controle de ampla tensão
      uint16_t wideVoltageCtrlBoxFanCurrent;// Corrente do ventilador da caixa de controle de ampla tensão (mA)
      double toolCoord[6];    // Valores atuais do sistema de coordenada da ferramenta; x,y,z,rx,ry,rz
      double wobjCoord[6];    // Valores atuais do sistema de coordenada da peça; x,y,z,rx,ry,rz
      double extoolCoord[6];   // Valores atuais do sistema de coordenada da ferramenta externa; x,y,z,rx,ry,rz
      double exAxisCoord[6];   // Valores atuais do sistema de coordenada do eixo de extensão; x,y,z,rx,ry,rz
      double load;        // Massa da carga
      double loadCog[3];     // Centro de gravidade da carga
      double lastServoTarget[6]; // Posição alvo do último ServoJ na fila
      int servoJCmdNum;      // Contagem de instruções servoJ
      double targetJointPos[6];  // Posição de instrução das 6 juntas, unidade °
      double targetJointVel[6];  // Velocidade de instrução das 6 juntas, unidade °/s
      double targetJointAcc[6];  // Aceleração de instrução das 6 juntas, unidade °/s2
      double targetJointCurrent[6]; // Corrente de instrução das 6 juntas, unidade A
      double actualJointCurrent[6]; // Corrente atual das 6 juntas, unidade A
      double actualTCPForce[6];  // Torque da extremidade do robô Nm; x,y,z,rx,ry,rz
      double targetTCPPos[6];    // Posição de instrução TCP do robô mm; x,y,z,rx,ry,rz
      uint8_t collisionLevel[6]; // Nível de colisão do robô
      double speedScaleManual;   // Percentual de velocidade global no modo manual
      double speedScaleAuto;    // Percentual de velocidade global no modo automático
      int luaLineNum;       // Número da linha do programa lua atualmente em execução
      uint8_t abnomalStop;     // 0-sem anormalidade; 1-com anormalidade
      char currentLuaFileName[256]; // Nome do programa lua atualmente em execução
      uint8_t programTotalLine;   // Número total de linhas do programa lua
      uint8_t safetyBoxSingal[6]; // Estado dos botões da caixa de segurança do robô
      double weldVoltage;     // Tensão de soldagem V
      double weldCurrent;     // Corrente de soldagem
      double weldTrackVel;    // Velocidade de rastreamento da solda mm/s
      uint8_t tpdException;    // Excedeu o limite de carregamento da trajetória TPD, 0-não excedeu, 1-excedeu
      uint8_t alarmRebootRobot;  // Aviso, 1-soltar botão de parada de emergência e reiniciar a caixa de controle, 2-anomalia de comunicação da junta reiniciar a caixa de controle
      uint8_t modbusMasterConnect; // bits 0-7 correspondem ao estado de conexão do mestre 0-7 ModbusTCP 0-não conectado 1-conectado
      uint8_t modbusSlaveConnect;  // Estado de conexão do escravo ModbusTCP 0-não conectado; 1-conectado
      uint8_t btnBoxStopSignal;    // Sinal de parada de emergência da botoeira, 0-parada de emergência solta; 1-parada de emergência pressionada
      uint8_t dragAlarm;      // Aviso de arrasto, atualmente em modo automático, 0-sem aviso, 1-com aviso, 2-anomalia de feedback de posição sem comutação
      uint8_t safetyDoorAlarm;    // Aviso de porta de segurança; 0-porta de segurança fechada; 1-porta de segurança aberta
      uint8_t safetyPlaneAlarm;    // Aviso de entrada no safety wall; 0-sem entrada no safety wall; 1-entrada no safety wall
      uint8_t motonAlarm;      // Aviso de movimento
      uint8_t interfaceAlarm;    // Aviso de entrada em área de interferência
      int udpCmdState;       // Estado de conexão de comunicação UDP na porta 20007
      uint8_t weldReadyState;    // Estado de preparação da soldadora concluído
      uint8_t alarmCheckEmergStopBtn; // 0-normal; 1-anomalia de comunicação, verificar se o botão de parada de emergência está solto
      uint8_t tsTmCmdComError;    // 0-normal; 1-falha de comunicação da instrução de torque
      uint8_t tsTmStateComError;   // 0-normal; 1-falha de comunicação do estado de torque
      int ctrlBoxError;       // Erro da caixa de controle
      uint8_t safetyDataState;    // Flag de estado dos dados de segurança, 0-normal, 1-anômalo
      uint8_t forceSensorErrState; // Falha de tempo limite de conexão do sensor de força; bits 0-1 correspondem aos IDs do sensor de força ID1-ID2
      uint8_t ctrlOpenLuaErrCode[4]; // Códigos de erro do protocolo do periférico do controlador 4 (código de erro 500)
      uint8_t strangePosFlag; // Flag de posição singular atual; 0-normal; 1-posição singular
      uint8_t alarm;      // Aviso
      uint8_t driverAlarm;    // Número do eixo com alarme do driver
      uint8_t aliveSlaveNumError; // Erro no número de escravos ativos, 0: normal; 1: erro no número
      uint8_t slaveComError[8];   // Erro do escravo, 0: normal; 1: escravo offline; 2: estado do escravo inconsistente com o valor definido; 3: escravo não configurado; 4: erro de configuração do escravo; 5: erro de inicialização do escravo; 6: erro de inicialização da comunicação da caixa postal do escravo
      uint8_t cmdPointError;    // Erro no ponto de instrução
      uint8_t IOError;      // Erro de IO
      uint8_t gripperError;    // Erro da garra
      uint8_t fileError;     // Erro de arquivo
      uint8_t paraError;     // Erro de parâmetro
      uint8_t exaxisOutLimitError;  // Erro de limite suave do eixo externo excedido
      uint8_t driverComError[6];    // Falha de comunicação com o driver
      uint8_t driverError;      // Número do eixo com falha de comunicação do driver
      uint8_t outSoftLimitError;   // Falha de limite suave excedido
      char axleGenComData[130];    // Dados de feedback de transmissão transparente da extremidade do robô
      uint8_t socketConnTimeout;   // Tempo limite de conexão do socket, bits 0-4: socketID 1-4
      uint8_t socketReadTimeout;   // Tempo limite de leitura do socket, bits 0-4: socketID 1-4
      uint8_t tsWebStateComErr;   // Falha de comunicação web-torque; 0-normal; 1-falha
      uint8_t exaxisCoordID;     //ID do sistema de coordenadas do eixo estendido
      uint16_t check_sum;     // Checksum
    }ROBOT_STATE_PKG;

Tipo de Enumeração para Configuração de Feedback de Estado do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    enum class RobotState
    {
        ProgramState = 3,           // Estado de execução do programa, 1-parado; 2-em execução; 3-pausado
        RobotState = 4,             // Estado de movimento do robô, 1-parado; 2-em movimento; 3-pausado; 4-arrastando
        MainCode = 5,               // Código de falha principal
        SubCode = 6,                // Código de falha secundário
        RobotMode = 7,              // Modo do robô, 1-manual; 0-automático
        JointCurPos = 8,            // Posições atuais das juntas de 6 eixos, unidade deg
        ToolCurPos = 9,             // Posição atual da ferramenta: [0] ao longo x (mm), [1] ao longo y (mm), [2] ao longo z (mm), [3] rotação em torno X fixo (deg), [4] em torno Y fixo (deg), [5] em torno Z fixo (deg)
        FlangeCurPos = 10,          // Posição atual da flange final: [0] ao longo x (mm), [1] ao longo y (mm), [2] ao longo z (mm), [3] rotação em torno X fixo (deg), [4] em torno Y fixo (deg), [5] em torno Z fixo (deg)
        ActualJointVel = 11,        // Velocidades atuais de 6 juntas, unidade deg/s
        ActualJointAcc = 12,        // Acelerações atuais de 6 juntas, unidade deg/s^2
        TargetTCPCmpSpeed = 13,     // Velocidade de comando composta TCP: [0] posição (mm/s), [1] orientação (deg/s)
        TargetTCPSpeed = 14,        // Velocidade de comando TCP: [0] ao longo x (mm/s), [1] ao longo y (mm/s), [2] ao longo z (mm/s), [3] velocidade angular em torno X (deg/s), [4] em torno Y (deg/s), [5] em torno Z (deg/s)
        ActualTCPCmpSpeed = 15,     // Velocidade efetiva composta TCP: [0] posição (mm/s), [1] orientação (deg/s)
        ActualTCPSpeed = 16,        // Velocidade efetiva TCP: [0] ao longo x (mm/s), [1] ao longo y (mm/s), [2] ao longo z (mm/s), [3] velocidade angular em torno X (deg/s), [4] em torno Y (deg/s), [5] em torno Z (deg/s)
        ActualJointTorque = 17,     // Torques atuais de 6 eixos, unidade N·m
        Tool = 18,                  // Número do sistema de coordenadas da ferramenta aplicado
        User = 19,                  // Número do sistema de coordenadas da peça aplicado
        ClDgtOutputH = 20,          // Saída IO digital da caixa de controle 15-8
        ClDgtOutputL = 21,          // Saída IO digital da caixa de controle 7-0
        TlDgtOutputL = 22,          // Saída IO digital da ferramenta 7-0, apenas bit0-bit1 válidos
        ClDgtInputH = 23,           // Entrada IO digital da caixa de controle 15-8
        ClDgtInputL = 24,           // Entrada IO digital da caixa de controle 7-0
        TlDgtInputL = 25,           // Entrada IO digital da ferramenta 7-0, apenas bit0-bit1 válidos
        ClAnalogInput = 26,         // Entrada analógica da caixa de controle: [0] canal 0, [1] canal 1
        TlAnalogInput = 27,         // Entrada analógica da ferramenta
        FtSensorRawData = 28,       // Dados brutos do sensor de força/torque: [0] força ao longo x (N), [1] ao longo y (N), [2] ao longo z (N), [3] torque em torno x (Nm), [4] em torno y (Nm), [5] em torno z (Nm)
        FtSensorData = 29,          // Dados do sensor de força/torque (processados): [0] força ao longo x (N), [1] ao longo y (N), [2] ao longo z (N), [3] torque em torno x (Nm), [4] em torno y (Nm), [5] em torno z (Nm)
        FtSensorActive = 30,        // Estado de ativação do sensor de força/torque, 0-reiniciado, 1-ativado
        EmergencyStop = 31,         // Flag de parada de emergência, 0-não pressionada, 1-pressionada
        MotionDone = 32,            // Sinal de movimento concluído, 1-concluído, 0-não concluído
        GripperMotiondone = 33,     // Sinal de movimento da garra concluído, 1-concluído, 0-não concluído
        McQueueLen = 34,            // Comprimento da fila de comandos de movimento
        CollisionState = 35,        // Detecção de colisão, 1-colisão, 0-sem colisão
        TrajectoryPnum = 36,        // Número do ponto de trajetória
        SafetyStop0State = 37,      // Sinal de parada de segurança SI0
        SafetyStop1State = 38,      // Sinal de parada de segurança SI1
        GripperFaultId = 39,        // Número da garra com falha
        GripperFault = 40,          // Falha da garra
        GripperActive = 41,         // Estado de ativação da garra
        GripperPosition = 42,       // Posição da garra
        GripperSpeed = 43,          // Velocidade da garra
        GripperCurrent = 44,        // Corrente da garra
        GripperTemp = 45,           // Temperatura da garra
        GripperVoltage = 46,        // Tensão da garra
        AuxState = 47,              // Estado dos eixos de extensão 485
        ExtAxisStatus = 48,         // Estado dos eixos de extensão UDP (4 eixos)
        ExtDIState = 49,            // Entrada DI estendida (8)
        ExtDOState = 50,            // Saída DO estendida (8)
        ExtAIState = 51,            // Entrada AI estendida (4)
        ExtAOState = 52,            // Saída AO estendida (4)
        RbtEnableState = 53,        // Estado de habilitação do robô
        JointDriverTorque = 54,     // Torque do driver das juntas do robô (6 juntas)
        JointDriverTemperature = 55,// Temperatura do driver das juntas do robô (6 juntas)
        RobotTime = 56,             // Tempo do sistema do robô
        SoftwareUpgradeState = 57,  // Estado de atualização do software do robô
        EndLuaErrCode = 58,         // Estado de execução Lua da extremidade
        ClAnalogOutput = 59,        // Saída analógica da caixa de controle (2)
        TlAnalogOutput = 60,        // Saída analógica da ferramenta
        GripperRotNum = 61,         // Número de rotações atual da garra rotativa
        GripperRotSpeed = 62,       // Porcentagem de velocidade de rotação atual da garra rotativa
        GripperRotTorque = 63,      // Porcentagem de torque de rotação atual da garra rotativa
        WeldingBreakOffState = 64,  // Estado de interrupção da soldagem
        TargetJointTorque = 65,     // Torque de comando da junta (6 juntas)
        SmartToolState = 66,        // Estado do botão da manopla SmartTool
        WideVoltageCtrlBoxTemp = 67,// Temperatura da caixa de controle de ampla tensão
        WideVoltageCtrlBoxFanCurrent = 68, // Corrente do ventilador da caixa de controle de ampla tensão (mA)
        ToolCoord = 69,             // Valores atuais do sistema de coordenadas da ferramenta: x,y,z,rx,ry,rz
        WobjCoord = 70,             // Valores atuais do sistema de coordenadas da peça: x,y,z,rx,ry,rz
        ExtoolCoord = 71,           // Valores atuais do sistema de coordenadas da ferramenta externa: x,y,z,rx,ry,rz
        ExAxisCoord = 72,           // Valores atuais do sistema de coordenadas dos eixos de extensão: x,y,z,rx,ry,rz
        Load = 73,                  // Massa da carga
        LoadCog = 74,               // Centro de gravidade da carga: x,y,z
        LastServoTarget = 75,       // Última posição alvo ServoJ na fila (6 juntas)
        ServoJCmdNum = 76,          // Contagem de comandos ServoJ
        TargetJointPos = 77,        // Posição de comando de 6 juntas, unidade °
        TargetJointVel = 78,        // Velocidade de comando de 6 juntas, unidade °/s
        TargetJointAcc = 79,        // Aceleração de comando de 6 juntas, unidade °/s²
        TargetJointCurrent = 80,    // Corrente de comando de 6 juntas, unidade A
        ActualJointCurrent = 81,    // Corrente atual de 6 juntas, unidade A
        ActualTCPForce = 82,        // Torque do end-effector do robô: x,y,z,rx,ry,rz, unidade Nm
        TargetTCPPos = 83,          // Posição de comando TCP do robô: x,y,z,rx,ry,rz, unidade mm
        CollisionLevel = 84,        // Nível de colisão do robô (6)
        SpeedScaleManual = 85,      // Porcentagem de velocidade global no modo manual
        SpeedScaleAuto = 86,        // Porcentagem de velocidade global no modo automático
        LuaLineNum = 87,            // Número da linha atual do programa Lua em execução
        AbnomalStop = 88,           // 0-sem anormalidade; 1-anormalidade presente
        CurrentLuaFileName = 89,    // Nome do programa Lua atualmente em execução
        ProgramTotalLine = 90,      // Número total de linhas do programa Lua
        SafetyBoxSingal = 91,       // Estado dos botões da caixa de botões do robô (6)
        WeldVoltage = 92,           // Tensão de soldagem V
        WeldCurrent = 93,           // Corrente de soldagem
        WeldTrackVel = 94,          // Velocidade de rastreamento da junta de solda mm/s
        TpdException = 95,          // Contagem de carregamento de trajetória TPD excedida, 0-não excedida, 1-excedida
        AlarmRebootRobot = 96,      // Aviso: 1-solte a parada de emergência e reinicie, 2-anomalia de comunicação da junta, reinicie
        ModbusMasterConnect = 97,   // bit0-7 correspondem ao estado de conexão dos mestres ModbusTCP 0-7, 0-não conectado, 1-conectado
        ModbusSlaveConnect = 98,    // Estado de conexão escrava ModbusTCP, 0-não conectado, 1-conectado
        BtnBoxStopSignal = 99,      // Sinal de parada de emergência da caixa de botões, 0-liberado, 1-pressionado
        DragAlarm = 100,            // Aviso de arrasto: 0-sem aviso, 1-aviso, 2-anomalia feedback posição, sem comutação
        SafetyDoorAlarm = 101,      // Aviso de porta de segurança: 0-fechada, 1-aberta
        SafetyPlaneAlarm = 102,     // Aviso de parede de segurança: 0-não entrou, 1-entrou
        MotonAlarm = 103,           // Aviso de movimento
        InterfaceAlarm = 104,       // Aviso de entrada na área de interferência
        UdpCmdState = 105,          // Estado de conexão de comunicação UDP da porta 20007
        WeldReadyState = 106,       // Estado de prontidão da máquina de solda
        AlarmCheckEmergStopBtn = 107, // 0-normal; 1-anomalia de comunicação, verificar botão de parada de emergência
        TsTmCmdComError = 108,      // 0-normal; 1-falha de comunicação do comando de torque
        TsTmStateComError = 109,    // 0-normal; 1-falha de comunicação do estado de torque
        CtrlBoxError = 110,         // Erro da caixa de controle
        SafetyDataState = 111,      // Estado dos dados de segurança, 0-normal, 1-anormal
        ForceSensorErrState = 112,  // Timeout de conexão do sensor de força, bit0-bit1 correspondem a ID1-ID2
        CtrlOpenLuaErrCode = 113,   // Códigos de erro do protocolo aberto do controlador periférico (4 erros código 500)
        StrangePosFlag = 114,       // Flag de postura singular: 0-normal, 1-postura singular
        Alarm = 115,                // Aviso
        DriverAlarm = 116,          // Número do eixo com alarme do driver
        AliveSlaveNumError = 117,   // Erro de contagem de escravos ativos: 0-normal, 1-erro de contagem
        SlaveComError = 118,        // Erro de escravo: 0-normal, 1-offline, 2-estado inconsistente, 3-não configurado, 4-erro de configuração, 5-erro de inicialização, 6-erro de inicialização da comunicação da caixa de correio
        CmdPointError = 119,        // Erro de ponto de comando
        IOError = 120,              // Erro de IO
        GripperError = 121,         // Erro da garra
        FileError = 122,            // Erro de arquivo
        ParaError = 123,            // Erro de parâmetro
        ExaxisOutLimitError = 124,  // Erro de limite suave do eixo externo excedido
        DriverComError = 125,       // Falha de comunicação com o driver (6 eixos)
        DriverError = 126,          // Número do eixo com falha de comunicação do driver
        OutSoftLimitError = 127,    // Falha de limite suave excedido
        AxleGenComData = 128,       // Dados de feedback de transmissão transparente do end-effector do robô
        SocketConnTimeout = 129,    // Timeout de conexão socket, bit0-bit4 correspondem a socketID 1-4
        SocketReadTimeout = 130,    // Timeout de leitura socket, bit0-bit4 correspondem a socketID 1-4
        TsWebStateComErr = 131,     // Falha de comunicação web-torque: 0-normal, 1-falha
        ExaxisCoordID = 132          //ID do sistema de coordenadas do eixo estendido
    };