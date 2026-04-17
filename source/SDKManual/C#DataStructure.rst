Descrição das Estruturas de Dados
================================================

.. toctree:: 
    :maxdepth: 5

Tipo de Dados para Posição das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Tipo de dados para posição das juntas
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* Posições das seis juntas, unidade deg */
    }

Tipo de Dados para Posição no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Tipo de dados para posição no espaço cartesiano
    */
    struct DescTran
    {
        public double x;    /* Coordenada do eixo X, unidade mm  */
        public double y;    /* Coordenada do eixo Y, unidade mm  */
        public double z;    /* Coordenada do eixo Z, unidade mm  */
    }

Tipo de Dados para Postura em Ângulos de Euler
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Tipo de dados para postura em ângulos de Euler
    */
    struct Rpy
    {
    public double rx;   /* Ângulo de rotação em torno do eixo X fixo, unidade: deg  */
    public double ry;   /* Ângulo de rotação em torno do eixo Y fixo, unidade: deg  */
    public double rz;   /* Ângulo de rotação em torno do eixo Z fixo, unidade: deg  */
    }

Tipo de Dados para Pose no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief Tipo de dados para pose no espaço cartesiano
    */
    struct DescPose
    {
        public DescTran tran;     /* Posição no espaço cartesiano  */
        public Rpy rpy;			/* Postura no espaço cartesiano  */
    }

Tipo de Dados para Posição dos Eixos Extensores
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Tipo de dados para posição dos eixos extensores
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* Posições dos quatro eixos extensores, unidade mm */
    }

Tipo de Dados para o Sensor de Força/Torque
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Componentes de força e torque do sensor de força
    */
    struct ForceTorque
    {
        public double fx;  /* Componente de força ao longo do eixo X, unidade N  */
        public double fy;  /* Componente de força ao longo do eixo Y, unidade N  */
        public double fz;  /* Componente de força ao longo do eixo Z, unidade N  */
        public double tx;  /* Componente de torque em torno do eixo X, unidade Nm */
        public double ty;  /* Componente de torque em torno do eixo Y, unidade Nm */
        public double tz;  /* Componente de torque em torno do eixo Z, unidade Nm */
    }

Tipo de Dados para Parâmetros da Espiral
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public struct SpiralParam
    {
        public int circle_num;           /* Número de voltas da espiral  */
        public float circle_angle;         /* Ângulo de inclinação da espiral  */
        public float rad_init;             /* Raio inicial da espiral, unidade mm  */
        public float rad_add;              /* Incremento do raio  */
        public float rotaxis_add;          /* Incremento na direção do eixo de rotação  */
        public uint rot_direction;  /* Direção de rotação, 0-horário, 1-anti-horário  */
        public int velAccMode;      // Modo do parâmetro de velocidade/aceleração: 0-velocidade angular constante; 1-velocidade linear constante
        public SpiralParam(int num, float angle, float initRad, float addRad, float axisAdd, uint direction, int mode)
        {
            circle_num = num;
            circle_angle = angle;
            rad_init = initRad;
            rad_add = addRad;
            rotaxis_add = axisAdd;
            rot_direction = direction;
            velAccMode = mode;
        }
    }

Tipo de Dados para Estado do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /**
    * @brief  Tipo de dados para estado do eixo extensor
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_AUX_STATE
    {
        public byte servoId;           // Número de ID do servo driver
        public int servoErrCode;       // Código de falha do servo driver
        public int servoState;         // Estado do servo driver
        public double servoPos;        // Posição atual do servo
        public float servoVel;         // Velocidade atual do servo
        public float servoTorque;      // Torque atual do servo
    }

Estado de Interrupção da Soldagem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct WELDING_BREAKOFF_STATE
    {
        public byte breakOffState;  // Estado de interrupção da soldagem
        public byte weldArcState;   // Estado de interrupção do arco de soldagem
    }

Tipo de Estrutura de Feedback de Estado do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief  Tipo de estrutura de feedback de estado do robô
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_STATE_PKG
    {
        public UInt16 frame_head;           // Cabeçalho do quadro 0x5A5A
        public byte frame_cnt;              // Contagem do quadro
        public UInt16 data_len;             // Comprimento dos dados  5
        public byte program_state;          // Estado de execução do programa, 1-parado; 2-executando; 3-pausado
        public byte robot_state;            // Estado de movimento do robô, 1-parado; 2-executando; 3-pausado; 4-arrastando  7
        public int main_code;               // Código de falha principal
        public int sub_code;                // Código de falha secundário
        public byte robot_mode;             // Modo do robô, 0-modo automático; 1-modo manual 16

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_pos;                             // Posição atual das juntas
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] tl_cur_pos;                             // Pose atual da ferramenta
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] flange_cur_pos;                         // Pose atual da flange da extremidade
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qd;                              // Velocidade atual das juntas do robô
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qdd;                             // Aceleração atual das juntas do robô  16 + 8 * 6 * 5 = 256
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] target_TCP_CmpSpeed;                    // Velocidade linear combinada do TCP do robô (comando)                        
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] target_TCP_Speed;                       // Velocidade do TCP do robô (comando)                        
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] actual_TCP_CmpSpeed;                    // Velocidade linear combinada real do TCP do robô                     
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_TCP_Speed;                       // Velocidade real do TCP do robô                     
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_tor;                             // Torque atual       
        public int tool;                        // Número da ferramenta
        public int user;                        // Número da peça
        public byte cl_dgt_output_h;            // Saída digital 15-8
        public byte cl_dgt_output_l;            // Saída digital 7-0
        public byte tl_dgt_output_l;            // Saída digital da ferramenta 7-0 (apenas bits 0-1 são válidos)
        public byte cl_dgt_input_h;             // Entrada digital 15-8
        public byte cl_dgt_input_l;             // Entrada digital 7-0
        public byte tl_dgt_input_l;             // Entrada digital da ferramenta 7-0 (apenas bits 0-1 são válidos)                  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public UInt16[] cl_analog_input;        // Entrada analógica do painel de controle
        public UInt16 tl_anglog_input;          // Entrada analógica da ferramenta                            
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_raw_data;     // Dados brutos do sensor de força/torque
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_data;         // Dados do sensor de força/torque                          
        public byte ft_sensor_active;           // Estado de ativação do sensor de força/torque, 0-reset, 1-ativado
        public byte EmergencyStop;              // Flag de parada de emergência
        public int motion_done;                 // Sinal de movimento concluído
        public byte gripper_motiondone;         // Sinal de movimento da garra concluído
        public int mc_queue_len;                // Comprimento da fila de movimento
        public byte collisionState;             // Detecção de colisão, 1-colisão; 0-sem colisão
        public int trajectory_pnum;             // Número do ponto da trajetória
        public byte safety_stop0_state;  /* Sinal de parada de segurança SI0 */
        public byte safety_stop1_state;  /* Sinal de parada de segurança SI1 */
        public byte gripper_fault_id;    /* Número da garra com falha */             
        public UInt16 gripper_fault;     /* Falha da garra */
        public UInt16 gripper_active;    /* Estado de ativação da garra */
        public byte gripper_position;    /* Posição da garra */
        public byte gripper_speed;       /* Velocidade da garra */
        public byte gripper_current;     /* Corrente da garra */
        public int gripper_tmp;          /* Temperatura da garra */
        public int gripper_voltage;      /* Tensão da garra */                 
        public ROBOT_AUX_STATE auxState; /* Estado do eixo extensor 485 */          
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public EXT_AXIS_STATUS[] extAxisStatus;  /* Estado do eixo extensor UDP */
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDIState;        // Entrada DI de extensão
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDOState;        // Saída DO de extensão
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAIState;        // Entrada AI de extensão
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAOState;        // Saída AO de extensão
        public int rbtEnableState;       // Estado de habilitação do robô
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTorque;               // Torque do driver da junta
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTemperature;          // Temperatura do driver da junta
        public ROBOT_TIME robotTime;     // Tempo do sistema do robô
        public int softwareUpgradeState; // Estado da atualização de software  0-ocioso ou enviando pacote de atualização; 1~100: porcentagem de conclusão da atualização; -1: falha na atualização do software; -2: falha na verificação; -3: falha na verificação de versão; -4: falha na descompactação; -5: falha na atualização da configuração do usuário; -6: falha na atualização da configuração do periférico; -7: falha na atualização da configuração do eixo extensor; -8: falha na atualização da configuração do robô; -9: falha na atualização da configuração dos parâmetros DH
        public UInt16 endLuaErrCode;    // Estado de execução do LUA da extremidade 
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public  UInt16[] cl_analog_output;  // Saída analógica do painel de controle
        public UInt16 tl_analog_output;     // Saída analógica da ferramenta
        public float gripperRotNum;           // Número atual de rotações da garra rotativa
        public byte gripperRotSpeed;       // Percentual atual da velocidade de rotação da garra rotativa
        public byte gripperRotTorque;	   // Percentual atual do torque de rotação da garra rotativa
        public WELDING_BREAKOFF_STATE weldingBreakOffState;// Estado de interrupção da soldagem

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_tgt_tor;// Torque de comando da junta
        public int smartToolState; // Estado do botão da SmartTool
        public float wideVoltageCtrlBoxTemp;        // Temperatura do painel de controle de tensão ampla
        public UInt16 wideVoltageCtrlBoxFanVel;   // Corrente do ventilador do painel de controle de tensão ampla (mA)

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] toolCoord;         // Sistema de coordenadas da ferramenta
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] wobjCoord;         // Sistema de coordenadas da peça
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] extoolCoord;        // Sistema de coordenadas da ferramenta externa
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] exAxisCoord;          // Sistema de coordenadas do eixo extensor
        public double load;                   // Massa da carga

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public double[] loadCog;           // Centro de massa da carga
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] lastServoTarget;// Última posição alvo do servoJ na fila

        public int servoJCmdNum;// Contagem de comandos servoJ
        public UInt16 check_sum;         /* Checksum */                     
    }