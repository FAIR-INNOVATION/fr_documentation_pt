Descrição das Estruturas de Dados
================

.. toctree::
    :maxdepth: 5

Tipo de Dados de Posição Articular
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de dados de posição articular
    */
    public class JointPos
    {
      double J1;
      double J2;
      double J3;
      double J4;
      double J5;
      double J6;

      public JointPos(double j1, double j2, double j3, double j4, double j5, double j6)
      {
        J1 = j1;
        J2 = j2;
        J3 = j3;
        J4 = j4;
        J5 = j5;
        J6 = j6;
      }

      public JointPos()
      {

      }
    }

Tipo de Dados de Posição no Espaço Cartesiano
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de dados de posição no espaço cartesiano
    */
    public class DescTran
    {
      public double x = 0.0;    /* Coordenada do eixo X, em mm */
      public double y = 0.0;    /* Coordenada do eixo Y, em mm */
      public double z = 0.0;    /* Coordenada do eixo Z, em mm */
      public DescTran(double posX, double posY, double posZ)
      {
        x = posX;
        y = posY;
        z = posZ;
      }

      public DescTran()
      {

      }

    }

Tipo de Dados de Atitude de Ângulos de Euler
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de dados de atitude de ângulos de Euler
    */
    public class Rpy
    {
      public double rx = 0.0;   /* Ângulo de rotação em torno do eixo X fixo, em graus */
      public double ry = 0.0;   /* Ângulo de rotação em torno do eixo Y fixo, em graus */
      public double rz = 0.0;   /* Ângulo de rotação em torno do eixo Z fixo, em graus */
      public Rpy(double rotateX, double rotateY, double rotateZ)
      {
        rx = rotateX;
        ry = rotateY;
        rz = rotateZ;
      }
    }

Tipo de Dados de Pose no Espaço Cartesiano
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief Tipo de pose no espaço cartesiano
    */
    public class DescPose
    {
      public DescTran tran = new DescTran(0.0, 0.0, 0.0);      /* Posição no espaço cartesiano */
      public Rpy rpy = new Rpy(0.0, 0.0, 0.0);                 /* Atitude no espaço cartesiano */

      public DescPose()
      {

      }

      public DescPose(DescTran descTran, Rpy rotateRpy)
      {
        tran = descTran;
        rpy = rotateRpy;
      }

      public DescPose(double tranX, double tranY, double tranZ, double rX, double ry, double rz)
      {
        tran.x = tranX;
        tran.y = tranY;
        tran.z = tranZ;
        rpy.rx = rX;
        rpy.ry = ry;
        rpy.rz = rz;
      }

      public String toString()
      {
        return String.valueOf(tran.x) + "," + String.valueOf(tran.y) + "," + String.valueOf(tran.z) + "," + String.valueOf(rpy.rx) + "," + String.valueOf(rpy.ry) + "," + String.valueOf(rpy.rz);
      }
    }

Tipo de Dados de Posição do Eixo Estendido
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de dados de posição do eixo estendido
    */
    public class ExaxisPos
    {
      public double axis1 = 0.0;
      public double axis2 = 0.0;
      public double axis3 = 0.0;
      public double axis4 = 0.0;

      public ExaxisPos()
      {

      }
      public ExaxisPos(double[] exaxisPos)
      {
        axis1 = exaxisPos[0];
        axis2 = exaxisPos[1];
        axis3 = exaxisPos[2];
        axis4 = exaxisPos[3];
      }

      public ExaxisPos(double pos1, double pos2, double pos3, double pos4)
      {
        axis1 = pos1;
        axis2 = pos2;
        axis3 = pos3;
        axis4 = pos4;
      }
    }

Tipo de Dados do Sensor de Torque
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Componentes de força e torque do sensor de força
    */
    public class ForceTorque
    {
      public double fx;  /* Componente de força ao longo do eixo X, em N */
      public double fy;  /* Componente de força ao longo do eixo Y, em N */
      public double fz;  /* Componente de força ao longo do eixo Z, em N */
      public double tx;  /* Componente de torque em torno do eixo X, em Nm */
      public double ty;  /* Componente de torque em torno do eixo Y, em Nm */
      public double tz;  /* Componente de torque em torno do eixo Z, em Nm */
      public ForceTorque(double fX, double fY, double fZ, double tX, double tY, double tZ)
      {
        fx = fX;
        fy = fY;
        fz = fZ;
        tx = tX;
        ty = tY;
        tz = tZ;
      }
    }

Tipo de Dados de Parâmetros da Espiral
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de dados de parâmetros da espiral
    */
    public class SpiralParam
    {
        public int circle_num;           /* Número de voltas da espiral */
        public double circle_angle;      /* Ângulo de inclinação da espiral */
        public double rad_init;          /* Raio inicial da espiral, em mm */
        public double rad_add;           /* Incremento do raio */
        public double rotaxis_add;       /* Incremento na direção do eixo de rotação */
        public int rot_direction;        /* Direção de rotação, 0-horário, 1-anti-horário */
        public int velAccMode;           /* Modo de parâmetro de velocidade/aceleração: 0-velocidade angular constante; 1-velocidade linear constante */
        public SpiralParam(int circleNum, double circleAngle, double radInit, double radAdd, double rotaxisAdd, int rotDirection, int vel_AccMode)
        {
            circle_num = circleNum;
            circle_angle = circleAngle;
            rad_init = radInit;
            rad_add = radAdd;
            rotaxis_add = rotaxisAdd;
            rot_direction = rotDirection;
            velAccMode = vel_AccMode;
        }
    }

Tipo de Estado do Eixo Estendido
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de estado do eixo estendido
    */
    public class EXT_AXIS_STATUS
    {
     public double pos = 0;        // Posição do eixo estendido
     public double vel = 0;        // Velocidade do eixo estendido
     public int errorCode = 0;     // Código de falha do eixo estendido
     public int ready = 0;         // Servo pronto
     public int inPos = 0;         // Servo no lugar
     public int alarm = 0;         // Alarme do servo
     public int flerr = 0;         // Erro de seguimento
     public int nlimit = 0;        // Limite negativo atingido
     public int pLimit = 0;        // Limite positivo atingido
     public int mdbsOffLine = 0;   // Driver offline no barramento 485
     public int mdbsTimeout = 0;   // Tempo limite de comunicação 485 entre placa de controle e caixa de controle
     public int homingStatus = 0;  // Status de retorno à origem do eixo estendido
    }

Tipo de Sensor
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de sensor
    */
    public class DeviceConfig
    {
      int company = 0;          // Fabricante
      int device = 0;           // Tipo/número do dispositivo
      int softwareVersion = 0;  // Versão do software
      int bus = 0;              // Local de montagem

      public DeviceConfig()
      {

      }

      public DeviceConfig(int company, int device, int softwareVersion, int bus)
      {
        this.company = company;
        this.device = device;
        this.softwareVersion = softwareVersion;
        this.bus = bus;
      }
    }

Configuração do Eixo Estendido 485
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configuração do eixo estendido 485
    */
    public class Axis485Param
    {
      int servoCompany;           // Fabricante do servo driver, 1-Dynatec
      int servoModel;             // Modelo do servo driver, 1-FD100-750C
      int servoSoftVersion;       // Versão do software do servo driver, 1-V1.0
      int servoResolution;        // Resolução do codificador
      double axisMechTransRatio;  // Relação de transmissão mecânica

      public Axis485Param(int company, int model, int softVersion, int resolution, double mechTransRatio)
      {
        servoCompany = company;
        servoModel = model;
        servoSoftVersion = softVersion;
        servoResolution = resolution;
        axisMechTransRatio = mechTransRatio;
      }

      public Axis485Param()
      {

      }
    }

Estado do Controlador Servo
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Estado do controlador servo
    */
    public class ROBOT_AUX_STATE
    {
      public int servoId = 0;           // Número de ID do servo driver
      public int servoErrCode = 0;      // Código de falha do servo driver
      public int servoState = 0;        // Estado do servo driver
      public double servoPos = 0;       // Posição atual do servo
      public float servoVel = 0;        // Velocidade atual do servo
      public float servoTorque = 0;     // Torque atual do servo
    }

Estado de Interrupção da Soldagem
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Estado de interrupção da soldagem
    */
    public class WELDING_BREAKOFF_STATE
    {
      public int breakOffState = 0;  // Estado de interrupção da soldagem
      public int weldArcState = 0;   // Estado de interrupção do arco de soldagem
    }

Parâmetros de Comunicação UDP do Eixo Estendido
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parâmetros de comunicação UDP do eixo estendido
    */
    public class UDPComParam
    {
      public String ip = "192.168.58.88"; // Endereço IP
      public int port = 2021;            // Número da porta
      public int period = 2;             // Período de comunicação (ms, padrão 2, não modifique este parâmetro)
      public int lossPkgTime = 50;       // Tempo de detecção de perda de pacote (ms)
      public int lossPkgNum = 2;         // Número de perdas de pacote
      public int disconnectTime = 100;   // Duração para confirmação de desconexão da comunicação
      public int reconnectEnable = 0;    // Ativação da reconexão automática em caso de desconexão 0-desativar 1-ativar
      public int reconnectPeriod = 100;  // Intervalo do período de reconexão (ms)
      public int reconnectNum = 3;       // Número de tentativas de reconexão
      public int selfConnect = 0;        // Estabelecer conexão automaticamente após reinicialização com perda de energia; 0-não estabelecer; 1-estabelecer
    }

Tipo de Estrutura de Retroalimentação de Estado do Robô
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Tipo de estrutura de retroalimentação de estado do robô
    */
    public class ROBOT_STATE_PKG
    {
      public short frame_head = 0;            // Cabeçalho do quadro 0x5A5A
      public byte frame_cnt = 0;              // Contagem do quadro
      public short data_len = 0;              // Comprimento dos dados
      public int program_state = 0;           // Estado de execução do programa, 1-parado; 2-em execução; 3-pausado
      public int robot_state = 0;             // Estado de movimento do robô, 1-parado; 2-em movimento; 3-pausado; 4-arrasto
      public int main_code = 0;               // Código de falha principal
      public int sub_code = 0;                // Código de falha secundário
      public int robot_mode = 0;              // Modo do robô, 0-modo automático; 1-modo manual
      public double[] jt_cur_pos = new double[6];                  // Posições atuais das juntas
      public double[] tl_cur_pos = new double[6];                  // Pose atual da ferramenta
      public double[] flange_cur_pos = new double[6];              // Pose atual do flange da extremidade
      public double[] actual_qd = new double[6];                   // Velocidades atuais das juntas do robô
      public double[] actual_qdd = new double[6];                  // Acelerações atuais das juntas do robô
      public double[] target_TCP_CmpSpeed = new double[2];         // Velocidade de comando sintética do TCP do robô
      public double[] target_TCP_Speed = new double[6];            // Velocidade de comando do TCP do robô
      public double[] actual_TCP_CmpSpeed = new double[2];         // Velocidade real sintética do TCP do robô
      public double[] actual_TCP_Speed = new double[6];            // Velocidade real do TCP do robô
      public double[] jt_cur_tor = new double[6];                  // Torques atuais
      public int tool = 0;                        // Número da ferramenta
      public int user = 0;                        // Número da peça
      public int cl_dgt_output_h = 0;             // Saída digital 15-8
      public int cl_dgt_output_l = 0;             // Saída digital 7-0
      public int tl_dgt_output_l = 0;             // Saída digital da ferramenta 7-0 (apenas bits 0-1 válidos)
      public int cl_dgt_input_h = 0;              // Entrada digital 15-8
      public int cl_dgt_input_l = 0;              // Entrada digital 7-0
      public int tl_dgt_input_l = 0;              // Entrada digital da ferramenta 7-0 (apenas bits 0-1 válidos)
      public short[] cl_analog_input = new short[2];          // Entrada analógica da caixa de controle
      public short tl_anglog_input = 0;                       // Entrada analógica da ferramenta
      public double[] ft_sensor_raw_data = new double[6];     // Dados brutos do sensor de força/torque
      public double[] ft_sensor_data = new double[6];         // Dados do sensor de força/torque no sistema de coordenadas de referência
      public int ft_sensor_active = 0;           // Estado de ativação do sensor de força/torque, 0-reset, 1-ativado
      public int EmergencyStop = 0;              // Sinalizador de parada de emergência
      public int motion_done = 0;                // Sinal de movimento concluído
      public int gripper_motiondone = 0;         // Sinal de movimento concluído da garra
      public int mc_queue_len = 0;               // Comprimento da fila de movimento
      public int collisionState = 0;             // Detecção de colisão, 1-colisão; 0-sem colisão
      public int trajectory_pnum = 0;            // Número do ponto de trajetória
      public int safety_stop0_state = 0;         /* Sinal de parada de segurança SI0 */
      public int safety_stop1_state = 0;         /* Sinal de parada de segurança SI1 */
      public int gripper_fault_id = 0;           /* Número da garra com falha */
      public short gripper_fault = 0;            /* Falha da garra */
      public short gripper_active = 0;           /* Estado de ativação da garra */
      public int gripper_position = 0;           /* Posição da garra */
      public int gripper_speed = 0;              /* Velocidade da garra */
      public int gripper_current = 0;            /* Corrente da garra */
      public int gripper_tmp = 0;                /* Temperatura da garra */
      public int gripper_voltage = 0;            /* Tensão da garra */
      public ROBOT_AUX_STATE auxState = new ROBOT_AUX_STATE(); /* Estado do eixo estendido 485 */
      public EXT_AXIS_STATUS extAxisStatus0 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus1 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus2 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus3 = new EXT_AXIS_STATUS();
      public short[] extDIState = new short[8];        // Entrada DI estendida
      public short[] extDOState = new short[8];        // Saída DO estendida
      public short[] extAIState = new short[4];        // Entrada AI estendida
      public short[] extAOState = new short[4];        // Saída AO estendida
      public int rbtEnableState = 0;                   // Estado de habilitação do robô
      public double[] jointDriverTorque = new double[6];       // Torque atual do driver articular
      public double[] jointDriverTemperature = new double[6];  // Temperatura atual do driver articular
      public ROBOT_TIME robotTime = new ROBOT_TIME();
      public int softwareUpgradeState = 0;   // Estado de atualização de software do robô 0-ocioso ou enviando pacote de atualização; 1~100: percentagem de conclusão da atualização; -1: falha na atualização do software; -2: falha na verificação; -3: falha na verificação da versão; -4: falha na descompactação; -5: falha na atualização da configuração do usuário; -6: falha na atualização da configuração do periférico; -7: falha na atualização da configuração do eixo estendido; -8: falha na atualização da configuração do robô; -9: falha na atualização da configuração dos parâmetros DH
      public int endLuaErrCode;              // Estado de execução do LUA da extremidade

      public int[] cl_analog_output = new int[2];  // Saída analógica da caixa de controle
      public int tl_analog_output;                // Saída analógica da ferramenta
      public float gripperRotNum;                 // Número atual de rotações da garra rotativa
      public int gripperRotSpeed;                 // Percentagem da velocidade atual de rotação da garra rotativa
      public int gripperRotTorque;                // Percentagem do torque atual de rotação da garra rotativa

      public WELDING_BREAKOFF_STATE weldingBreakOffstate = new WELDING_BREAKOFF_STATE(); // Estado de interrupção da soldagem

      public double[] jt_tgt_tor = new double[6];    // Torque de comando das juntas
      public int smartToolState;                     // Estado do botão do SmartTool

      public float wideVoltageCtrlBoxTemp;           // Temperatura da caixa de controle de larga tensão
      public int wideVoltageCtrlBoxFanVel;           // Velocidade da ventoinha da caixa de controle de larga tensão (mA)

      public double[] toolCoord = new double[6];           // Sistema de coordenadas da ferramenta
      public double[] wobjCoord = new double[6];           // Sistema de coordenadas da peça
      public double[] extoolCoord = new double[6];         // Sistema de coordenadas da ferramenta externa
      public double[] exAxisCoord = new double[6];         // Sistema de coordenadas do eixo estendido
      public double load;                   // Massa da carga
      public double[] loadCog = new double[3];             // Centro de massa da carga

      public double[] lastServoTarget = new double[6];      // Última posição alvo do servoJ na fila
      public int servoJCmdNum;                            // Contagem de instruções servoJ

      public short check_sum = 0;          /* Soma de verificação */

      public ROBOT_STATE_PKG()
      {

      }
    }