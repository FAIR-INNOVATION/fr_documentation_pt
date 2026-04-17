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

Pacote de Dados de Retroalimentação de Estado do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Pacote de dados de retroalimentação de estado do controlador
     */
    typedef struct _ROBOT_STATE_PKG
    {
        uint16_t frame_head;      // Cabeçalho do quadro, definido como 0x5A5A
        uint8_t  frame_cnt;       // Contagem do quadro, contagem cíclica 0-255
        uint16_t data_len;        // Comprimento do conteúdo dos dados
        uint8_t  program_state;   // Estado de execução do programa, 1-parado; 2-em execução; 3-pausado;
        uint8_t  robot_state;     // Estado de movimento do robô, 1-parado; 2-em movimento; 3-pausado; 4-arrasto
        int      main_code;       // Código de falha principal
        int      sub_code;        // Código de falha secundário
        uint8_t  robot_mode;      // Modo do robô, 1-modo manual; 0-modo automático;
        double   jt_cur_pos[6];   // Posições atuais das 6 juntas, em graus
        double   tl_cur_pos[6];   // Posição atual da ferramenta
                                  // tl_cur_pos[0], posição ao longo do eixo X, em mm,
                                  // tl_cur_pos[1], posição ao longo do eixo Y, em mm,
                                  // tl_cur_pos[2], posição ao longo do eixo Z, em mm,
                                  // tl_cur_pos[3], ângulo de rotação em torno do eixo X fixo, em graus
                                  // tl_cur_pos[4], ângulo de rotação em torno do eixo Y fixo, em graus
                                  // tl_cur_pos[5], ângulo de rotação em torno do eixo Z fixo, em graus
        double   flange_cur_pos[6]; // Posição atual do flange da extremidade
                                    // flange_cur_pos[0], posição ao longo do eixo X, em mm,
                                    // flange_cur_pos[1], posição ao longo do eixo Y, em mm,
                                    // flange_cur_pos[2], posição ao longo do eixo Z, em mm,
                                    // flange_cur_pos[3], ângulo de rotação em torno do eixo X fixo, em graus
                                    // flange_cur_pos[4], ângulo de rotação em torno do eixo Y fixo, em graus
                                    // flange_cur_pos[5], ângulo de rotação em torno do eixo Z fixo, em graus
        double   actual_qd[6];      // Velocidades atuais das 6 juntas, em graus/s
        double   actual_qdd[6];     // Acelerações atuais das 6 juntas, em graus/s^2
        double   target_TCP_CmpSpeed[2];
    // target_TCP_CmpSpeed[0], velocidade de comando sintética do TCP (posição), em mm/s
                     // target_TCP_CmpSpeed[1], velocidade de comando sintética do TCP (atitude), em graus/s */
        double   target_TCP_Speed[6];    // Velocidade de comando do TCP
                         // target_TCP_Speed[0], velocidade ao longo do eixo X, em mm/s,
                         // target_TCP_Speed[1], velocidade ao longo do eixo Y, em mm/s,
                         // target_TCP_Speed[2], velocidade ao longo do eixo Z, em mm/s,
                         // target_TCP_Speed[3], velocidade angular em torno do eixo X fixo, em graus/s
                         // target_TCP_Speed[4], velocidade angular em torno do eixo Y fixo, em graus/s
                         // target_TCP_Speed[5], velocidade angular em torno do eixo Z fixo, em graus/s */
        double   actual_TCP_CmpSpeed[2];
    // actual_TCP_CmpSpeed[0], velocidade real sintética do TCP (posição), em mm/s
                  // actual_TCP_CmpSpeed[1], velocidade real sintética do TCP (atitude), em graus/s
        double   actual_TCP_Speed[6];    // Velocidade real do TCP
                        // actual_TCP_Speed[0], velocidade ao longo do eixo X, em mm/s,
                        // actual_TCP_Speed[1], velocidade ao longo do eixo Y, em mm/s,
                        // actual_TCP_Speed[2], velocidade ao longo do eixo Z, em mm/s,
                        // actual_TCP_Speed[3], velocidade angular em torno do eixo X fixo, em graus/s
                        // actual_TCP_Speed[4], velocidade angular em torno do eixo Y fixo, em graus/s
                        // actual_TCP_Speed[5], velocidade angular em torno do eixo Z fixo, em graus/s
        double   jt_cur_tor[6];      // Torques atuais das 6 juntas, em N·m
        int      tool;               // Número do sistema de coordenadas da ferramenta aplicado
        int      user;               // Número do sistema de coordenadas da peça aplicado
        uint8_t  cl_dgt_output_h;    // Saída digital da caixa de controle 15-8
        uint8_t  cl_dgt_output_l;    // Saída digital da caixa de controle 7-0
        uint8_t  tl_dgt_output_l;    // Saída digital da ferramenta 7-0, apenas bits 0-1 são válidos
        uint8_t  cl_dgt_input_h;     // Entrada digital da caixa de controle 15-8
        uint8_t  cl_dgt_input_l;     // Entrada digital da caixa de controle 7-0
        uint8_t  tl_dgt_input_l;     // Entrada digital da ferramenta 7-0, apenas bits 0-1 são válidos
        uint16_t cl_analog_input[2]; // cl_analog_input[0], entrada analógica 0 da caixa de controle
                                     // cl_analog_input[1], entrada analógica 1 da caixa de controle
        uint16_t tl_anglog_input;    // Entrada analógica da ferramenta
        double   ft_sensor_raw_data[6]; // Dados brutos do sensor de torque
                                      // ft_sensor_raw_data[0], força ao longo do eixo X, em N
                                      // ft_sensor_raw_data[1], força ao longo do eixo Y, em N
                                      // ft_sensor_raw_data[2], força ao longo do eixo Z, em N
                                      // ft_sensor_raw_data[3], torque em torno do eixo X, em Nm
                                      // ft_sensor_raw_data[4], torque em torno do eixo Y, em Nm
                                      // ft_sensor_raw_data[5], torque em torno do eixo Z, em Nm
        double   ft_sensor_data[6];     // Dados do sensor de torque,
                                        // ft_sensor_data[0], força ao longo do eixo X, em N
                                        // ft_sensor_data[1], força ao longo do eixo Y, em N
                                        // ft_sensor_data[2], força ao longo do eixo Z, em N
                                        // ft_sensor_data[3], torque em torno do eixo X, em Nm
                                        // ft_sensor_data[4], torque em torno do eixo Y, em Nm
                                        // ft_sensor_data[5], torque em torno do eixo Z, em Nm
        uint8_t  ft_sensor_active;   // Estado de ativação do sensor de torque, 0-reset, 1-ativado
        uint8_t  EmergencyStop;      // Sinalizador de parada de emergência, 0-parada de emergência não pressionada, 1-parada de emergência pressionada
        int      motion_done;        // Sinal de movimento concluído, 1-concluído, 0-não concluído
        uint8_t  gripper_motiondone; // Sinal de movimento concluído da garra, 1-concluído, 0-não concluído
        int      mc_queue_len;       // Comprimento da fila de instruções de movimento
        uint8_t  collisionState;     // Detecção de colisão, 1-colisão, 0-sem colisão
        int      trajectory_pnum;    // Número do ponto de trajetória
        uint8_t  safety_stop0_state; // Sinal de parada de segurança SI0
        uint8_t  safety_stop1_state; // Sinal de parada de segurança SI1
        uint8_t  gripper_fault_id;   // Número da garra com falha
        uint16_t gripper_fault;      // Falha da garra
        uint16_t gripper_active;     // Estado de ativação da garra
        uint8_t  gripper_position;   // Posição da garra
        int8_t   gripper_speed;      // Velocidade da garra
        int8_t   gripper_current;    // Corrente da garra
        int      gripper_temp;       // Temperatura da garra
        int      gripper_voltage;    // Tensão da garra
        robot_aux_state aux_state;   // Estado do eixo estendido 485
        EXT_AXIS_STATUS extAxisStatus[4];  // Estado do eixo estendido UDP
        uint16_t extDIState[8];        // Entrada DI estendida
        uint16_t extDOState[8];        // Saída DO estendida
        uint16_t extAIState[4];        // Entrada AI estendida
        uint16_t extAOState[4];        // Saída AO estendida
        int rbtEnableState;            // Estado de habilitação do robô
        double   jointDriverTorque[6];        // Torque do driver articular do robô
        double   jointDriverTemperature[6];   // Temperatura do driver articular do robô
        RobotTime robotTime;           // Tempo do sistema do robô
        int softwareUpgradeState;      // Estado de atualização de software do robô
        uint16_t endLuaErrCode;        // Estado de execução do LUA da extremidade
        uint16_t cl_analog_output[2];  // Saída analógica da caixa de controle
        uint16_t tl_analog_output;     // Saída analógica da ferramenta
        float gripperRotNum;           // Número atual de rotações da garra rotativa
        uint8_t gripperRotSpeed;       // Percentagem da velocidade atual de rotação da garra rotativa
        uint8_t gripperRotTorque;      // Percentagem do torque atual de rotação da garra rotativa
        WELDING_BREAKOFF_STATE weldingBreakOffState;  // Estado de interrupção da soldagem
        double jt_tgt_tor[6];                 // Torque de comando das juntas
        int smartToolState;                   // Estado do botão do SmartTool
        float wideVoltageCtrlBoxTemp;         // Temperatura da caixa de controle de larga tensão
        uint16_t wideVoltageCtrlBoxFanCurrent; // Corrente da ventoinha da caixa de controle de larga tensão (mA)
        double toolCoord[6];        // Sistema de coordenadas da ferramenta
        double wobjCoord[6];        // Sistema de coordenadas da peça
        double extoolCoord[6];      // Sistema de coordenadas da ferramenta externa
        double exAxisCoord[6];      // Sistema de coordenadas do eixo estendido
        double load;                // Massa da carga
        double loadCog[3];          // Centro de massa da carga
        double lastServoTarget[6];  // Última posição alvo do ServoJ na fila
        int servoJCmdNum;           // Contagem de instruções servoJ
        uint16_t check_sum;         // Soma de verificação
    } ROBOT_STATE_PKG;