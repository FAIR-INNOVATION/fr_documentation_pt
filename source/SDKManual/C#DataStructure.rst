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

Tipo de estrutura de feedback do estado do robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief  Tipo de estrutura de feedback do estado do robô
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public class ROBOT_STATE_PKG
    {
        public UInt16 frame_head;           // Cabeçalho do quadro 0x5A5A
        public byte frame_cnt;              // Contagem do quadro
        public UInt16 data_len;             // Comprimento dos dados 5
        public byte program_state;          // Estado de execução do programa, 1-parado; 2-em execução; 3-pausado;
        public byte robot_state;            // Estado de movimento do robô, 1-parado; 2-em execução; 3-pausado; 4-arrasto
        public int main_code;               // Código de falha principal
        public int sub_code;                // Código de falha secundário
        public byte robot_mode;             // Modo do robô, 1-modo manual; 0-modo automático;

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_pos;         // Posições atuais das 6 juntas, unidade deg
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] tl_cur_pos;         // Posição atual da ferramenta (TCP)
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] flange_cur_pos;     // Posição atual da flange final
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qd;          // Velocidades atuais das 6 juntas, unidade deg/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qdd;         // Acelerações atuais das 6 juntas, unidade deg/s^2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] target_TCP_CmpSpeed;// Velocidade de instrução composta TCP (posição, orientação)
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] target_TCP_Speed;   // Velocidade de instrução TCP
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] actual_TCP_CmpSpeed;// Velocidade real composta TCP
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_TCP_Speed;   // Velocidade real TCP
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_tor;         // Torques atuais das 6 juntas, unidade N·m

        public int tool;                    // Número do sistema de coordenada da ferramenta aplicado
        public int user;                    // Número do sistema de coordenada da peça aplicado
        public byte cl_dgt_output_h;        // Saída IO digital da caixa de controle 15-8
        public byte cl_dgt_output_l;        // Saída IO digital da caixa de controle 7-0
        public byte tl_dgt_output_l;        // Saída IO digital da ferramenta 7-0, apenas bits 0-1 válidos
        public byte cl_dgt_input_h;         // Entrada IO digital da caixa de controle 15-8
        public byte cl_dgt_input_l;         // Entrada IO digital da caixa de controle 7-0
        public byte tl_dgt_input_l;         // Entrada IO digital da ferramenta 7-0, apenas bits 0-1 válidos

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public UInt16[] cl_analog_input;        // Entradas analógicas da caixa de controle
        public UInt16 tl_anglog_input;          // Entrada analógica da ferramenta

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_raw_data; // Dados brutos do sensor de torque
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_data;     // Dados do sensor de torque
        public byte ft_sensor_active;       // Estado de ativação do sensor de torque, 0-reset, 1-ativado

        public byte EmergencyStop;          // Flag de parada de emergência, 0-não pressionado, 1-pressionado
        public int motion_done;             // Sinal de movimento concluído, 1-concluído, 0-não concluído
        public byte gripper_motiondone;     // Sinal de conclusão do movimento da garra, 1-concluído, 0-não concluído
        public int mc_queue_len;            // Comprimento da fila de comandos de movimento
        public byte collisionState;         // Detecção de colisão, 1-colisão, 0-sem colisão
        public int trajectory_pnum;         // Número do ponto da trajetória
        public byte safety_stop0_state;     // Sinal de parada de segurança SI0
        public byte safety_stop1_state;     // Sinal de parada de segurança SI1
        public byte gripper_fault_id;       // ID da garra com erro
        public UInt16 gripper_fault;     /* Falha da garra */
        public UInt16 gripper_active;    /* Estado de ativação da garra */
        public byte gripper_position;       // Posição da garra
        public byte gripper_speed;       /* Velocidade da garra */
        public byte gripper_current;     /* Corrente da garra */
        public int gripper_temp;            // Temperatura da garra
        public int gripper_voltage;         // Tensão da garra

        public ROBOT_AUX_STATE auxState;   // Estado do eixo de extensão 485

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public EXT_AXIS_STATUS[] extAxisStatus; // Estado do eixo de extensão UDP

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDIState;        // Entradas DI estendidas
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDOState;        // Saídas DO estendidas
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAIState;        // Entradas AI estendidas
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAOState;        // Saídas AO estendidas

        public int rbtEnableState;          // Estado de habilitação do robô

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTorque;      // Torques do driver da junta do robô
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTemperature; // Temperaturas do driver da junta do robô

        public ROBOT_TIME robotTime;        // Tempo do sistema do robô
        public int softwareUpgradeState;    // Estado de atualização de software do robô
        public UInt16 endLuaErrCode;    // Estado de execução LUA da extremidade

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public  UInt16[] cl_analog_output;  // Saídas analógicas da caixa de controle
        public UInt16 tl_analog_output;     // Saída analógica da ferramenta

        public float gripperRotNum;         // Número atual de rotações da garra rotativa
        public byte gripperRotSpeed;        // Percentual de velocidade atual da garra rotativa
        public byte gripperRotTorque;       // Percentual de torque atual da garra rotativa

        public WELDING_BREAKOFF_STATE weldingBreakOffState; // Estado de interrupção da soldagem

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_tgt_tor;         // Torques de instrução da junta
        public int smartToolState;          // Estado do botão do punho SmartTool
        public float wideVoltageCtrlBoxTemp; // Temperatura da caixa de controle de ampla tensão
        public UInt16 wideVoltageCtrlBoxFanVel;   // Corrente do ventilador da caixa de controle de ampla tensão (mA)

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] toolCoord;          // Valores atuais do sistema de coordenada da ferramenta; x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] wobjCoord;          // Valores atuais do sistema de coordenada da peça; x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] extoolCoord;        // Valores atuais do sistema de coordenada da ferramenta externa; x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] exAxisCoord;        // Valores atuais do sistema de coordenada do eixo de extensão; x,y,z,rx,ry,rz

        public double load;                 // Massa da carga
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public double[] loadCog;            // Centro de gravidade da carga
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] lastServoTarget;    // Última posição alvo do ServoJ na fila
        public int servoJCmdNum;            // Contagem de comandos servoJ

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointPos;     // Posições de instrução das 6 juntas, unidade °
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointVel;     // Velocidades de instrução das 6 juntas, unidade °/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointAcc;     // Acelerações de instrução das 6 juntas, unidade °/s²
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointCurrent; // Correntes de instrução das 6 juntas, unidade A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualJointCurrent; // Correntes atuais das 6 juntas, unidade A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualTCPForce;     // Torque da extremidade do robô Nm; x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetTCPPos;       // Posição de instrução TCP do robô mm; x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] collisionLevel;       // Níveis de colisão do robô

        public double speedScaleManual;     // Percentual de velocidade global no modo manual
        public double speedScaleAuto;       // Percentual de velocidade global no modo automático
        public int luaLineNum;              // Número da linha do programa lua atualmente em execução
        public byte abnomalStop;            // 0-sem anormalidade; 1-com anormalidade

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        public byte[] currentLuaFileName;   // Nome do programa lua atualmente em execução
        public byte programTotalLine;       // Total de linhas do programa lua
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] safetyBoxSingal;      // Estado dos botões da caixa de botões do robô

        public double weldVoltage;          // Tensão de soldagem V
        public double weldCurrent;          // Corrente de soldagem
        public double weldTrackVel;         // Velocidade de rastreamento da solda mm/s

        public byte tpdException;           // Excesso de limite de carregamento de trajetórias TPD, 0-não excedido, 1-excedido
        public byte alarmRebootRobot;       // Aviso, 1-soltar botão de parada de emergência e reiniciar caixa de controle, 2-anomalia de comunicação da junta reiniciar caixa de controle
        public byte modbusMasterConnect;    // bits 0-7 correspondem ao estado de conexão do mestre 0-7 ModbusTCP 0-não conectado 1-conectado
        public byte modbusSlaveConnect;     // Estado de conexão do escravo ModbusTCP 0-não conectado; 1-conectado
        public byte btnBoxStopSignal;       // Sinal de parada de emergência da botoeira, 0-parada de emergência solta; 1-parada de emergência pressionada
        public byte dragAlarm;              // Aviso de arrasto, atualmente em modo automático, 0-sem alarme, 1-alarme, 2-anomalia de feedback de posição sem comutação
        public byte safetyDoorAlarm;        // Aviso de porta de segurança; 0-porta de segurança fechada; 1-porta de segurança aberta
        public byte safetyPlaneAlarm;       // Aviso de entrada no safety wall; 0-sem entrada no safety wall; 1-entrada no safety wall
        public byte motonAlarm;             // Aviso de movimento
        public byte interfaceAlarm;         // Aviso de entrada em área de interferência
        public int udpCmdState;             // Estado de conexão de comunicação UDP na porta 20007
        public byte weldReadyState;         // Estado de preparação da soldadora concluído
        public byte alarmCheckEmergStopBtn; // 0-normal; 1-anomalia de comunicação, verificar se o botão de parada de emergência está solto
        public byte tsTmCmdComError;        // 0-normal; 1-falha de comunicação do comando de torque
        public byte tsTmStateComError;      // 0-normal; 1-falha de comunicação do estado de torque
        public int ctrlBoxError;            // Erro da caixa de controle
        public byte safetyDataState;        // Flag de estado dos dados de segurança, 0-normal, 1-anômalo
        public byte forceSensorErrState;    // Falha de timeout de conexão do sensor de força; bits 0-1 correspondem aos IDs do sensor de força ID1-ID2

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] ctrlOpenLuaErrCode;   // 4 códigos de erro de protocolo do periférico do controlador (código de erro 500)

        public byte strangePosFlag;         // Flag de posição singular atual; 0-normal; 1-posição singular
        public byte alarm;                  // Aviso
        public byte driverAlarm;            // Número do eixo com alarme do driver
        public byte aliveSlaveNumError;     // Erro no número de escravos ativos, 0: normal; 1: erro no número

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public byte[] slaveComError;        // Erro do escravo, 0: normal; 1: escravo offline; 2: estado do escravo inconsistente com o valor definido; 3: escravo não configurado; 4: erro de configuração do escravo; 5: erro de inicialização do escravo; 6: erro de inicialização da comunicação da caixa postal do escravo

        public byte cmdPointError;          // Erro no ponto de comando
        public byte IOError;                // Erro de IO
        public byte gripperError;           // Erro da garra
        public byte fileError;              // Erro de arquivo
        public byte paraError;              // Erro de parâmetro
        public byte exaxisOutLimitError;    // Erro de limite suave do eixo externo excedido

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] driverComError;       // Falha de comunicação com o driver
        public byte driverError;            // Número do eixo com falha de comunicação do driver
        public byte outSoftLimitError;      // Falha de limite suave excedido

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 130)]
        public byte[] axleGenComData;       // Dados de feedback de transmissão transparente da extremidade do robô

        public byte socketConnTimeout;     // Flag de timeout de conexão do socket
        public byte socketReadTimeout;     // Flag de timeout de leitura do socket
        public byte tsWebStateComErr;      // ts_web_state_com_err

        public UInt16 check_sum;         /* Checksum */

        // Construtor: inicializa todos os campos de array
        public ROBOT_STATE_PKG()
        {
            jt_cur_pos = new double[6];
            tl_cur_pos = new double[6];
            flange_cur_pos = new double[6];
            actual_qd = new double[6];
            actual_qdd = new double[6];
            target_TCP_CmpSpeed = new double[2];
            target_TCP_Speed = new double[6];
            actual_TCP_CmpSpeed = new double[2];
            actual_TCP_Speed = new double[6];
            jt_cur_tor = new double[6];
            cl_analog_input = new ushort[2];
            ft_sensor_raw_data = new double[6];
            ft_sensor_data = new double[6];
            extAxisStatus = new EXT_AXIS_STATUS[4];
            extDIState = new ushort[8];
            extDOState = new ushort[8];
            extAIState = new ushort[4];
            extAOState = new ushort[4];
            jointDriverTorque = new double[6];
            jointDriverTemperature = new double[6];
            cl_analog_output = new ushort[2];
            jt_tgt_tor = new double[6];
            toolCoord = new double[6];
            wobjCoord = new double[6];
            extoolCoord = new double[6];
            exAxisCoord = new double[6];
            loadCog = new double[3];
            lastServoTarget = new double[6];
            targetJointPos = new double[6];
            targetJointVel = new double[6];
            targetJointAcc = new double[6];
            targetJointCurrent = new double[6];
            actualJointCurrent = new double[6];
            actualTCPForce = new double[6];
            targetTCPPos = new double[6];
            collisionLevel = new byte[6];
            currentLuaFileName = new byte[256];
            safetyBoxSingal = new byte[6];
            ctrlOpenLuaErrCode = new byte[4];
            slaveComError = new byte[8];
            driverComError = new byte[6];
            axleGenComData = new byte[130];
        }
    }

Enum de estado configurável do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Enum de estado configurável do robô, intervalo 3~131
    */
    public enum RobotState
    {
        ProgramState = 3,
        RobotState = 4,
        MainCode = 5,
        SubCode = 6,
        RobotMode = 7,
        JointCurPos = 8,
        ToolCurPos = 9,
        FlangeCurPos = 10,
        ActualJointVel = 11,
        ActualJointAcc = 12,
        TargetTCPCmpSpeed = 13,
        TargetTCPSpeed = 14,
        ActualTCPCmpSpeed = 15,
        ActualTCPSpeed = 16,
        ActualJointTorque = 17,
        Tool = 18,
        User = 19,
        ClDgtOutputH = 20,
        ClDgtOutputL = 21,
        TlDgtOutputL = 22,
        ClDgtInputH = 23,
        ClDgtInputL = 24,
        TlDgtInputL = 25,
        ClAnalogInput = 26,
        TlAnglogInput = 27,
        FtSensorRawData = 28,
        FtSensorData = 29,
        FtSensorActive = 30,
        EmergencyStop = 31,
        MotionDone = 32,
        GripperMotiondone = 33,
        McQueueLen = 34,
        CollisionState = 35,
        TrajectoryPnum = 36,
        SafetyStop0State = 37,
        SafetyStop1State = 38,
        GripperFaultId = 39,
        GripperFault = 40,
        GripperActive = 41,
        GripperPosition = 42,
        GripperSpeed = 43,
        GripperCurrent = 44,
        GripperTemp = 45,
        GripperVoltage = 46,
        AuxState = 47,
        ExtAxisStatus = 48,
        ExtDIState = 49,
        ExtDOState = 50,
        ExtAIState = 51,
        ExtAOState = 52,
        RbtEnableState = 53,
        JointDriverTorque = 54,
        JointDriverTemperature = 55,
        RobotTime = 56,
        SoftwareUpgradeState = 57,
        EndLuaErrCode = 58,
        ClAnalogOutput = 59,
        TlAnalogOutput = 60,
        GripperRotNum = 61,
        GripperRotSpeed = 62,
        GripperRotTorque = 63,
        WeldingBreakOffState = 64,
        TargetJointTorque = 65,
        SmartToolState = 66,
        WideVoltageCtrlBoxTemp = 67,
        WideVoltageCtrlBoxFanCurrent = 68,
        ToolCoord = 69,
        WobjCoord = 70,
        ExtoolCoord = 71,
        ExAxisCoord = 72,
        Load = 73,
        LoadCog = 74,
        LastServoTarget = 75,
        ServoJCmdNum = 76,
        TargetJointPos = 77,
        TargetJointVel = 78,
        TargetJointAcc = 79,
        TargetJointCurrent = 80,
        ActualJointCurrent = 81,
        ActualTCPForce = 82,
        TargetTCPPos = 83,
        CollisionLevel = 84,
        SpeedScaleManual = 85,
        SpeedScaleAuto = 86,
        LuaLineNum = 87,
        AbnomalStop = 88,
        CurrentLuaFileName = 89,
        ProgramTotalLine = 90,
        SafetyBoxSingal = 91,
        WeldVoltage = 92,
        WeldCurrent = 93,
        WeldTrackVel = 94,
        TpdException = 95,
        AlarmRebootRobot = 96,
        ModbusMasterConnect = 97,
        ModbusSlaveConnect = 98,
        BtnBoxStopSignal = 99,
        DragAlarm = 100,
        SafetyDoorAlarm = 101,
        SafetyPlaneAlarm = 102,
        MotonAlarm = 103,
        InterfaceAlarm = 104,
        UdpCmdState = 105,
        WeldReadyState = 106,
        AlarmCheckEmergStopBtn = 107,
        TsTmCmdComError = 108,
        TsTmStateComError = 109,
        CtrlBoxError = 110,
        SafetyDataState = 111,
        ForceSensorErrState = 112,
        CtrlOpenLuaErrCode = 113,
        StrangePosFlag = 114,
        Alarm = 115,
        DriverAlarm = 116,
        AliveSlaveNumError = 117,
        SlaveComError = 118,
        CmdPointError = 119,
        IOError = 120,
        GripperError = 121,
        FileError = 122,
        ParaError = 123,
        ExaxisOutLimitError = 124,
        DriverComError = 125,
        DriverError = 126,
        OutSoftLimitError = 127,
        AxleGenComData = 128,
        SocketConnTimeout = 129,     // timeout de conexão do socket, bits 0-4: socketID 1-4
        SocketReadTimeout = 130,     // timeout de leitura do socket, bits 0-4: socketID 1-4
        TsWebStateComErr = 131     // falha de comunicação web-torque; 0-normal; 1-falha
    }