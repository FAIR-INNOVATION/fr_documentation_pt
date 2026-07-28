Descrição das Estruturas de Dados
================================================

.. toctree::
    :maxdepth: 5

Tipo de Dados de Posição Articular
+++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++
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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Tipo de estrutura de feedback de estado do robô
    */
    public class ROBOT_STATE_PKG {
        public int frame_head;                      // Cabeçalho do quadro
        public int frame_cnt;                       // Contagem de quadros
        public int data_len;                        // Comprimento dos dados
        public int program_state;                   // Estado do programa - 1-parado; 2-em execução; 3-pausado
        public int robot_state;                     // Estado de movimento do robô - 1-parado; 2-em movimento; 3-pausado; 4-arrastando
        public int main_code;                       // Código de falha principal
        public int sub_code;                        // Código de falha secundário
        public int robot_mode;                      // Modo do robô - 1-manual; 0-automático
        public double[] jt_cur_pos = new double[6]; // Posições atuais das juntas de 6 eixos, unidade deg
        public double[] tl_cur_pos = new double[6]; // Posição atual da ferramenta - [x,y,z,rx,ry,rz]
        public double[] flange_cur_pos = new double[6]; // Posição atual da flange final - [x,y,z,rx,ry,rz]
        public double[] actual_qd = new double[6];  // Velocidades atuais de 6 juntas, unidade deg/s
        public double[] actual_qdd = new double[6]; // Acelerações atuais de 6 juntas, unidade deg/s^2
        public double[] target_TCP_CmpSpeed = new double[2]; // Velocidade de comando composta TCP - [posição mm/s, orientação deg/s]
        public double[] target_TCP_Speed = new double[6]; // Velocidade de comando TCP - [vx,vy,vz,wx,wy,wz]
        public double[] actual_TCP_CmpSpeed = new double[2]; // Velocidade efetiva composta TCP - [posição mm/s, orientação deg/s]
        public double[] actual_TCP_Speed = new double[6]; // Velocidade efetiva TCP - [vx,vy,vz,wx,wy,wz]
        public double[] jt_cur_tor = new double[6]; // Torque atual da junta
        public int tool;                            // ID da ferramenta
        public int user;                            // ID da peça
        public int cl_dgt_output_h;                 // Byte alto da saída digital do armário de controle
        public int cl_dgt_output_l;                 // Byte baixo da saída digital do armário de controle
        public int tl_dgt_output_l;                 // Byte baixo da saída digital da ferramenta
        public int cl_dgt_input_h;                  // Byte alto da entrada digital do armário de controle
        public int cl_dgt_input_l;                  // Byte baixo da entrada digital do armário de controle
        public int tl_dgt_input_l;                  // Byte baixo da entrada digital da ferramenta
        public int[] cl_analog_input = new int[2];  // Entrada analógica do armário de controle
        public int tl_anglog_input;                 // Entrada analógica da ferramenta
        public double[] ft_sensor_raw_data = new double[6]; // Dados brutos do sensor de força
        public double[] ft_sensor_data = new double[6]; // Dados do sensor de força
        public int ft_sensor_active;                // Estado de ativação do sensor de força
        public int EmergencyStop;                   // Estado de parada de emergência
        public int motion_done;                     // Movimento concluído
        public int gripper_motiondone;              // Sinal de conclusão de movimento da garra, 0-não concluído, 1-concluído (nenhum objeto detectado), 2-movimento concluído (objeto detectado)
        public int mc_queue_len;                    // Comprimento da fila de movimentos
        public int collisionState;                  // Estado de colisão
        public int trajectory_pnum;                 // Número de sequência do ponto de trajetória
        public int safety_stop0_state;              // Estado de parada de segurança 0
        public int safety_stop1_state;              // Estado de parada de segurança 1
        public int gripper_fault_id;                // ID de falha da garra
        public int gripper_fault;                   // Falha da garra
        public int gripper_active;                  // Ativação da garra
        public int gripper_position;                // Posição da garra
        public int gripper_speed;                   // Velocidade da garra
        public int gripper_current;                 // Corrente da garra
        public int gripper_temp;                    // Temperatura da garra
        public int gripper_voltage;                 // Tensão da garra
        public AuxState aux_state = new AuxState(); // Estado dos eixos auxiliares internos
        public EXT_AXIS_STATUS[] extAxisStatus = new EXT_AXIS_STATUS[4]; // Matriz de estado dos eixos de extensão
        public short[] extDIState = new short[8];   // I/O estendidos
        public short[] extDOState = new short[8];   // I/O estendidos
        public short[] extAIState = new short[4];   // I/O estendidos
        public short[] extAOState = new short[4];   // I/O estendidos
        public int rbtEnableState;                  // Estado de habilitação do robô
        public double[] jointDriverTorque = new double[6]; // Torque do driver da junta
        public double[] jointDriverTemperature = new double[6]; // Temperatura do driver da junta
        public ROBOT_TIME robotTime = new ROBOT_TIME(); // Objeto de tempo do robô
        public int softwareUpgradeState;            // Estado de atualização do software
        public int endLuaErrCode;                   // Código de erro Lua da extremidade
        public int[] cl_analog_output = new int[2]; // Saída analógica do armário de controle
        public int tl_analog_output;                // Saída analógica da ferramenta
        public float gripperRotNum;                 // Número de rotações da garra rotativa
        public int gripperRotSpeed;                 // Velocidade da garra rotativa
        public int gripperRotTorque;                // Torque da garra rotativa
        public WELDING_BREAKOFF_STATE weldingBreakOffState = new WELDING_BREAKOFF_STATE(); // Estado de interrupção da soldagem
        public double[] jt_tgt_tor = new double[6]; // Torque da junta alvo
        public int smartToolState;                  // Estado da ferramenta inteligente
        public float wideVoltageCtrlBoxTemp;        // Temperatura do armário de controle de ampla tensão
        public int wideVoltageCtrlBoxFanCurrent;    // Corrente do ventilador do armário de controle de ampla tensão
        public double[] toolCoord = new double[6];  // Sistema de coordenadas da ferramenta
        public double[] wobjCoord = new double[6];  // Sistema de coordenadas da peça
        public double[] extoolCoord = new double[6]; // Sistema de coordenadas da ferramenta externa
        public double[] exAxisCoord = new double[6]; // Sistema de coordenadas do eixo de extensão
        public double load;                         // Carga
        public double[] loadCog = new double[3];    // Centro de gravidade da carga
        public double[] lastServoTarget = new double[6]; // Última posição alvo servo J
        public int servoJCmdNum;                    // Número de comandos servo J
        public double[] targetJointPos = new double[6]; // Posição da junta alvo
        public double[] targetJointVel = new double[6]; // Velocidade da junta alvo
        public double[] targetJointAcc = new double[6]; // Aceleração da junta alvo
        public double[] targetJointCurrent = new double[6]; // Corrente da junta alvo
        public double[] actualJointCurrent = new double[6]; // Corrente efetiva da junta
        public double[] actualTCPForce = new double[6]; // Força TCP efetiva
        public double[] targetTCPPos = new double[6]; // Posição TCP alvo
        public int[] collisionLevel = new int[6];   // Nível de colisão
        public double speedScaleManual;              // Escala de velocidade manual
        public double speedScaleAuto;                // Escala de velocidade automática
        public int luaLineNum;                       // Número da linha Lua
        public int abnomalStop;                      // Parada anormal
        public String currentLuaFileName;            // Nome do arquivo Lua atual
        public int programTotalLine;                 // Linhas totais do programa
        public int[] safetyBoxSingal = new int[6];   // Sinal da caixa de segurança
        public double weldVoltage;                   // Tensão de soldagem
        public double weldCurrent;                   // Corrente de soldagem
        public double weldTrackVel;                  // Velocidade de rastreamento de soldagem
        public int tpdException;                     // Exceção TPD
        public int alarmRebootRobot;                 // Reinicialização do robô por alarme
        public int modbusMasterConnect;              // Conexão master Modbus
        public int modbusSlaveConnect;               // Conexão slave Modbus
        public int btnBoxStopSignal;                 // Sinal de parada da caixa de botões
        public int dragAlarm;                        // Alarme de arrasto
        public int safetyDoorAlarm;                  // Alarme de porta de segurança
        public int safetyPlaneAlarm;                 // Alarme de plano de segurança
        public int motonAlarm;                       // Alarme de movimento
        public int interfaceAlarm;                   // Alarme de interferência
        public int udpCmdState;                      // Estado do comando UDP
        public int weldReadyState;                   // Estado de prontidão da soldagem
        public int alarmCheckEmergStopBtn;           // Botão de parada de emergência de verificação de alarme
        public int tsTmCmdComError;                  // Erro de comunicação de comando
        public int tsTmStateComError;                // Erro de comunicação de estado
        public int ctrlBoxError;                     // Erro do armário de controle
        public int safetyDataState;                  // Estado dos dados de segurança
        public int forceSensorErrState;              // Estado de erro do sensor de força
        public int[] ctrlOpenLuaErrCode = new int[4]; // Código de erro Lua de controle aberto
        public int strangePosFlag;                   // Flag de posição singular
        public int alarm;                            // Alarme
        public int driverAlarm;                      // Alarme do driver
        public int aliveSlaveNumError;               // Erro de número de escravos ativos
        public int[] slaveComError = new int[8];     // Erro de comunicação do escravo
        public int cmdPointError;                    // Erro de ponto de comando
        public int IOError;                          // Erro de IO
        public int gripperError;                     // Erro da garra
        public int fileError;                        // Erro de arquivo
        public int paraError;                        // Erro de parâmetro
        public int exaxisOutLimitError;              // Erro de limite suave do eixo de extensão excedido
        public int[] driverComError = new int[6];    // Erro de comunicação do driver
        public int driverError;                      // Erro do driver
        public int outSoftLimitError;                // Erro de limite suave excedido
        public byte[] axleGenComData = new byte[130]; // Dados de comunicação do eixo geral
        public int check_sum;                        // Checksum
        public int socketConnTimeout;                // Tempo limite de conexão do socket
        public int socketReadTimeout;                // Tempo limite de leitura do socket
        public int tsWebStateComErr;                 // Erro de comunicação de estado TS Web
        public int exaxisCoordID;                  //ID do sistema de coordenadas do eixo estendido
        public int programRunState;                //Status de execução do programa LUA 0-programa não em execução; 1-programa em execução (incluindo programa pausado)
    }

Classe de Resultado da Configuração de Feedback de Estado do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * Classe de resultado da configuração de feedback de estado do robô, contendo lista de estados e período
    */
    public static class StateConfigResult {
      public final List<RobotState> stateList;
      public final int period;
    }

Tipo de Enumeração da Configuração de Feedback de Estado do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * Tipo de enumeração de estado do robô
    * Usado para configuração de feedback de estado em tempo real
    */
    enum class RobotState
    {
        ProgramState,           // Estado de execução do programa, 1-parado; 2-em execução; 3-em pausa
        RobotState,             // Estado de movimento do robô, 1-parado; 2-em movimento; 3-em pausa; 4-arrasto
        MainCode,               // Código de falha principal
        SubCode,                // Código de falha secundário
        RobotMode,              // Modo do robô, 1-modo manual; 0-modo automático
        JointCurPos,            // Posições atuais das juntas de 6 eixos, unidade deg
        ToolCurPos,             // Posição atual da ferramenta: [0]posição ao longo do eixo x(mm), [1]ao longo do eixo y(mm), [2]ao longo do eixo z(mm), [3]rotação em torno do X fixo(deg), [4]em torno do Y fixo(deg), [5]em torno do Z fixo(deg)
        FlangeCurPos,           // Posição atual da flange final: [0]ao longo do eixo x(mm), [1]ao longo do eixo y(mm), [2]ao longo do eixo z(mm), [3]rotação em torno do X fixo(deg), [4]em torno do Y fixo(deg), [5]em torno do Z fixo(deg)
        ActualJointVel,         // Velocidades atuais de 6 juntas, unidade deg/s
        ActualJointAcc,         // Acelerações atuais de 6 juntas, unidade deg/s²
        TargetTCPCmpSpeed,      // Velocidade composta de comando TCP: [0]posição(mm/s), [1]orientação(deg/s)
        TargetTCPSpeed,         // Velocidade de comando TCP: [0]ao longo do eixo x(mm/s), [1]ao longo do eixo y(mm/s), [2]ao longo do eixo z(mm/s), [3]velocidade angular em torno do X(deg/s), [4]em torno do Y(deg/s), [5]em torno do Z(deg/s)
        ActualTCPCmpSpeed,      // Velocidade composta real TCP: [0]posição(mm/s), [1]orientação(deg/s)
        ActualTCPSpeed,         // Velocidade real TCP: [0]ao longo do eixo x(mm/s), [1]ao longo do eixo y(mm/s), [2]ao longo do eixo z(mm/s), [3]velocidade angular em torno do X(deg/s), [4]em torno do Y(deg/s), [5]em torno do Z(deg/s)
        ActualJointTorque,      // Torques atuais de 6 juntas, unidade N·m
        Tool,                   // Número do sistema de coordenadas da ferramenta aplicado
        User,                   // Número do sistema de coordenadas da peça aplicado
        ClDgtOutputH,           // Saída IO digital da caixa de controle 15-8
        ClDgtOutputL,           // Saída IO digital da caixa de controle 7-0
        TlDgtOutputL,           // Saída IO digital da ferramenta 7-0, apenas bit0-bit1 válidos
        ClDgtInputH,            // Entrada IO digital da caixa de controle 15-8
        ClDgtInputL,            // Entrada IO digital da caixa de controle 7-0
        TlDgtInputL,            // Entrada IO digital da ferramenta 7-0, apenas bit0-bit1 válidos
        ClAnalogInput,          // Entrada analógica da caixa de controle: [0]canal 0, [1]canal 1
        TlAnalogInput,          // Entrada analógica da ferramenta
        FtSensorRawData,        // Dados brutos do sensor de força/torque: [0]força ao longo do eixo x(N), [1]ao longo do eixo y(N), [2]ao longo do eixo z(N), [3]torque em torno do eixo x(Nm), [4]em torno do eixo y(Nm), [5]em torno do eixo z(Nm)
        FtSensorData,           // Dados do sensor de força/torque (processados): [0]força ao longo do eixo x(N), [1]ao longo do eixo y(N), [2]ao longo do eixo z(N), [3]torque em torno do eixo x(Nm), [4]em torno do eixo y(Nm), [5]em torno do eixo z(Nm)
        FtSensorActive,         // Estado de ativação do sensor de força/torque, 0-reset, 1-ativo
        EmergencyStop,          // Flag de parada de emergência, 0-parada de emergência não pressionada, 1-parada de emergência pressionada
        MotionDone,             // Sinal de movimento concluído, 1-concluído, 0-não concluído
        GripperMotiondone,      // Sinal de movimento da garra concluído, 1-concluído, 0-não concluído
        McQueueLen,             // Comprimento da fila de comandos de movimento
        CollisionState,         // Detecção de colisão, 1-colisão, 0-sem colisão
        TrajectoryPnum,         // Número do ponto de trajetória
        SafetyStop0State,       // Sinal de parada de segurança SI0
        SafetyStop1State,       // Sinal de parada de segurança SI1
        GripperFaultId,         // Número da garra com falha
        GripperFault,           // Falha da garra
        GripperActive,          // Estado de ativação da garra
        GripperPosition,        // Posição da garra
        GripperSpeed,           // Velocidade da garra
        GripperCurrent,         // Corrente da garra
        GripperTemp,            // Temperatura da garra
        GripperVoltage,         // Tensão da garra
        AuxState,               // Estado do eixo estendido 485
        ExtAxisStatus,          // Estado do eixo estendido UDP (4 eixos)
        ExtDIState,             // Entrada DI estendida (8)
        ExtDOState,             // Saída DO estendida (8)
        ExtAIState,             // Entrada AI estendida (4)
        ExtAOState,             // Saída AO estendida (4)
        RbtEnableState,         // Estado de habilitação do robô
        JointDriverTorque,      // Torque do driver da junta do robô (6 juntas)
        JointDriverTemperature, // Temperatura do driver da junta do robô (6 juntas)
        RobotTime,              // Tempo do sistema do robô
        SoftwareUpgradeState,   // Estado de atualização de software do robô
        EndLuaErrCode,          // Estado de execução LUA da extremidade
        ClAnalogOutput,         // Saída analógica da caixa de controle (2)
        TlAnalogOutput,         // Saída analógica da ferramenta
        GripperRotNum,          // Número atual de rotações da garra rotativa
        GripperRotSpeed,        // Percentual de velocidade atual da garra rotativa
        GripperRotTorque,       // Percentual de torque atual da garra rotativa
        WeldingBreakOffState,   // Estado de interrupção da soldagem
        TargetJointTorque,      // Torque de comando da junta (6 juntas)
        SmartToolState,         // Estado do botão da alça SmartTool
        WideVoltageCtrlBoxTemp, // Temperatura da caixa de controle de ampla tensão
        WideVoltageCtrlBoxFanCurrent, // Corrente do ventilador da caixa de controle de ampla tensão (mA)
        ToolCoord,              // Valores atuais das coordenadas da ferramenta: x,y,z,rx,ry,rz
        WobjCoord,              // Valores atuais das coordenadas da peça: x,y,z,rx,ry,rz
        ExtoolCoord,            // Valores atuais das coordenadas da ferramenta externa: x,y,z,rx,ry,rz
        ExAxisCoord,            // Valores atuais das coordenadas do eixo estendido: x,y,z,rx,ry,rz
        Load,                   // Massa da carga
        LoadCog,                // Centro de gravidade da carga: x,y,z
        LastServoTarget,        // Última posição alvo do ServoJ na fila (6 juntas)
        ServoJCmdNum,           // Contagem de comandos servoJ
        TargetJointPos,         // Posições de comando de 6 juntas, unidade °
        TargetJointVel,         // Velocidades de comando de 6 juntas, unidade °/s
        TargetJointAcc,         // Acelerações de comando de 6 juntas, unidade °/s²
        TargetJointCurrent,     // Correntes de comando de 6 juntas, unidade A
        ActualJointCurrent,     // Correntes atuais de 6 juntas, unidade A
        ActualTCPForce,         // Torque da extremidade do robô: x,y,z,rx,ry,rz, unidade Nm
        TargetTCPPos,           // Posição de comando TCP do robô: x,y,z,rx,ry,rz, unidade mm
        CollisionLevel,         // Nível de colisão do robô (6)
        SpeedScaleManual,       // Percentual global de velocidade no modo manual
        SpeedScaleAuto,         // Percentual global de velocidade no modo automático
        LuaLineNum,             // Número da linha atual do programa lua em execução
        AbnomalStop,            // 0-sem anormalidade; 1-com anormalidade
        CurrentLuaFileName,     // Nome do programa lua atualmente em execução
        ProgramTotalLine,       // Linhas totais do programa lua
        SafetyBoxSingal,        // Estado dos botões da caixa de botões do robô (6)
        WeldVoltage,            // Tensão de soldagem V
        WeldCurrent,            // Corrente de soldagem
        WeldTrackVel,           // Velocidade de rastreamento da solda mm/s
        TpdException,           // Limite de carregamento de trajetórias TPD excedido, 0-não excedido, 1-excedido
        AlarmRebootRobot,       // Aviso: 1-ciclo de energia necessário após liberar parada de emergência, 2-anormalidade de comunicação da junta requer ciclo de energia
        ModbusMasterConnect,    // bit0-7 correspondem ao status de conexão do mestre ModbusTCP 0-7, 0-não conectado, 1-conectado
        ModbusSlaveConnect,     // Status de conexão do escravo ModbusTCP, 0-não conectado, 1-conectado
        BtnBoxStopSignal,       // Sinal de parada de emergência da caixa de botões, 0-parada de emergência liberada, 1-parada de emergência pressionada
        DragAlarm,              // Aviso de arrasto: 0-sem alarme, 1-alarme, 2-anormalidade de feedback de posição sem troca
        SafetyDoorAlarm,        // Aviso de porta de segurança: 0-fechada, 1-aberta
        SafetyPlaneAlarm,       // Aviso de parede de segurança: 0-não entrou, 1-entrou
        MotonAlarm,             // Aviso de movimento
        InterfaceAlarm,         // Aviso de entrada em zona de interferência
        UdpCmdState,            // Status da conexão de comunicação UDP da porta 20007
        WeldReadyState,         // Estado de prontidão da soldadora
        AlarmCheckEmergStopBtn, // 0-normal; 1-anormalidade de comunicação, verificar botão de parada de emergência
        TsTmCmdComError,        // 0-normal; 1-falha de comunicação do comando de torque
        TsTmStateComError,      // 0-normal; 1-falha de comunicação do estado de torque
        CtrlBoxError,           // Erro da caixa de controle
        SafetyDataState,        // Estado dos dados de segurança, 0-normal, 1-anormal
        ForceSensorErrState,    // Tempo limite de conexão do sensor de força, bit0-bit1 correspondem ao ID1-ID2
        CtrlOpenLuaErrCode,     // Códigos de erro de protocolo de periféricos do controlador (código de erro 500)
        StrangePosFlag,         // Flag de pose singular: 0-normal, 1-pose singular
        Alarm,                  // Alarme
        DriverAlarm,            // Número do eixo com alarme do driver
        AliveSlaveNumError,     // Erro de contagem de escravos ativos: 0-normal, 1-erro de contagem
        SlaveComError,          // Erro de escravo: 0-normal, 1-offline, 2-inconsistência de estado, 3-não configurado, 4-erro de configuração, 5-erro de inicialização, 6-erro de inicialização de comunicação de caixa postal
        CmdPointError,          // Erro de ponto de comando
        IOError,                // Erro de IO
        GripperError,           // Erro da garra
        FileError,              // Erro de arquivo
        ParaError,              // Erro de parâmetro
        ExaxisOutLimitError,    // Erro de limite suave excedido no eixo externo
        DriverComError,         // Falha de comunicação com o driver (6 eixos)
        DriverError,            // Número do eixo com falha de comunicação do driver
        OutSoftLimitError,      // Falha de limite suave excedido
        AxleGenComData,         // Dados de feedback transparente da extremidade do robô
        SocketConnTimeout,      // Tempo limite de conexão socket, bit0-bit4 correspondem ao socketID 1-4
        SocketReadTimeout,      // Tempo limite de leitura socket, bit0-bit4 correspondem ao socketID 1-4
        TsWebStateComErr,       // Falha de comunicação web-torque: 0-normal, 1-falha
        ExaxisCoordID           // ID do sistema de coordenadas do eixo estendido
        programRunState         //Status de execução do programa LUA 0-programa não em execução; 1-programa em execução (incluindo programa pausado)
    };