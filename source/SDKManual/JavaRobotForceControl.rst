Controle de Força do Robô
====================================

.. toctree::
    :maxdepth: 5

Configurar Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configura o sensor de força
    * @param config company: Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa 11 da Aeroespacial, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin, 23-NBIT, 24-Xin Jingcheng (XJC), 26-NSR
    * @param config device: Número do dispositivo, Kunwei (0-KWR75B), Instituto de Pesquisa 11 (0-MCS6A-200-4), ATI (0-AXIA80-M8), Zhongke Midian (0-MST2010), Weihang Minxin (0-WHC6L-YB-10A), NBIT (0-XLH93003ACS), Xin Jingcheng XJC (0-XJC-6F-D82), NSR (0-NSR-FTSensorA)
    * @param config softversion: Número da versão do software, não utilizado no momento, padrão 0
    * @param config bus: Posição do barramento onde o dispositivo está conectado, não utilizado no momento, padrão 0
    * @return Código de erro
    */
    int FT_SetConfig(DeviceConfig config);

Obter Configuração do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a configuração do sensor de força
    * @param [out] config company: Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa 11 da Aeroespacial, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin
    * @param [out] config device: Número do dispositivo, Kunwei (0-KWR75B), Instituto de Pesquisa 11 (0-MCS6A-200-4), ATI (0-AXIA80-M8), Zhongke Midian (0-MST2010), Weihang Minxin (0-WHC6L-YB-10A)
    * @param [out] config softversion: Número da versão do software, não utilizado no momento, padrão 0
    * @param [out] config bus: Posição do barramento onde o dispositivo está conectado, não utilizado no momento, padrão 0
    * @return Código de erro
    */
    int FT_GetConfig(DeviceConfig config);

Ativar Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa o sensor de força
    * @param [in] act 0-reset, 1-ativar
    * @return Código de erro
    */
    int FT_Activate(int act);

Calibrar Zero do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibra o zero do sensor de força
    * @param [in] act 0-remover zero, 1-corrigir zero
    * @return Código de erro
    */
    int FT_SetZero(int act);

Definir Sistema de Coordenadas de Referência do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o sistema de coordenadas de referência do sensor de força
    * @param [in] type 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base, 2-sistema de coordenadas livre
    * @param [in] coord Valor do sistema de coordenadas livre
    * @return Código de erro
    */
    int FT_SetRCS(int type, DescPose coord);

Definir Peso da Carga sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o peso da carga sob o sensor de força
    * @param [in] weight Peso da carga em kg
    * @return Código de erro
    */
    int SetForceSensorPayLoad(double weight);

Definir Centro de Massa da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o centro de massa da carga sob o sensor de força
    * @param [in] cog Centro de massa da carga em mm
    * @return Código de erro
    */
    int SetForceSensorPayLoadCog(DescTran cog);

Obter Peso da Carga sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o peso da carga sob o sensor de força
    * @return List[0]: código de erro; List[1]: weight Peso da carga em kg
    */
    List<Number> GetForceSensorPayLoad();

Obter Centro de Massa da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o centro de massa da carga sob o sensor de força
    * @param [out] cog Centro de massa da carga em mm
    * @return Código de erro
    */
    int GetForceSensorPayLoadCog(DescTran cog);

Calibração Automática do Zero do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração automática do zero do sensor de força
    * @param [in] massCenter Massa do sensor (kg) e centro de massa (mm)
    * @return Código de erro
    */
    int ForceSensorAutoComputeLoad(MassCenter massCenter);

Obter Dados de Força/Torque no Sistema de Coordenadas de Referência
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém dados de força/torque no sistema de coordenadas de referência
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] ft Força/torque, fx, fy, fz, tx, ty, tz
    * @return Código de erro
    */
    int FT_GetForceTorqueRCS(int flag, ForceTorque ft);

Obter Dados Brutos de Força/Torque do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém dados brutos de força/torque do sensor de força
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] ft Força/torque, fx, fy, fz, tx, ty, tz
    * @return Código de erro
    */
    int FT_GetForceTorqueOrigin(int flag, ForceTorque ft);

Exemplo de Código de Configuração e Calibração Automática do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTInit(Robot robot)
    {
        DescTran tr1 = new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con = new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose ftCoord = new DescPose();
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayload(0.824);

        DescTran tr = new DescTran(0.778, 2.554, 48.765);
        robot.SetForceSensorPayloadCog(tr);
        List<Number> weight = new ArrayList<>();
        double x = 0, y = 0, z = 0;
        weight = robot.GetForceSensorPayload();
        robot.GetForceSensorPayloadCog(tr);
        tr.x = 0;
        tr.y = 0;
        tr.z = 0;
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr);

        double computeWeight = 0;
        DescTran tran = new DescTran();
        MassCenter mass = new MassCenter();
        mass.weight = weight.get(1).doubleValue();
        mass.cog = tran;
        robot.ForceSensorAutoComputeLoad(mass);
        return 0;
    }

Registro de Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Registro de identificação do peso da carga
    * @param [in] id Número do sistema de coordenadas do sensor, intervalo [1~14]
    * @return Código de erro
    */
    int FT_PdIdenRecord(int id);

Cálculo da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Cálculo da identificação do peso da carga
    * @return List[0]: código de erro; List[1]: double weight Peso da carga, em kg
    */
    List<Number> FT_PdIdenCompute();

Registro de Identificação do Centro de Massa da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Registro de identificação do centro de massa da carga
    * @param [in] id Número do sistema de coordenadas do sensor, intervalo [1~14]
    * @param [in] index Número do ponto, intervalo [1~3]
    * @return Código de erro
    */
    int FT_PdCogIdenRecord(int id, int index);

Cálculo da Identificação do Centro de Massa da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Cálculo da identificação do centro de massa da carga
    * @param [out] cog Centro de massa da carga, em mm
    * @return Código de erro
    */
    int FT_PdCogIdenCompute(DescTran cog);

Exemplo de Código de Identificação da Carga do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTLoadCompute(Robot robot)
    {
        DescTran tr1 = new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con = new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose tcoord = new DescPose();
        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        robot.Sleep(1000);

        List<Number> weight = new ArrayList<>();
        weight = robot.FT_PdIdenCompute();

        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart(desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);
        robot.Sleep(1000);
        DescTran cog = new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(cog);

        robot.CloseRPC();
        return 0;
    }

Proteção contra Colisão
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Proteção contra colisão
    * @param [in] flag 0-desativar proteção contra colisão, 1-ativar proteção contra colisão
    * @param [in] sensor_id Número do sensor de força
    * @param [in] select Seleciona quais dos seis graus de liberdade detectam colisão, 0-não detectar, 1-detectar
    * @param [in] ft Força/torque de colisão, fx, fy, fz, tx, ty, tz
    * @param [in] max_threshold Limiar máximo
    * @param [in] min_threshold Limiar mínimo
    * @note Faixa de detecção de força/torque: (ft - min_threshold, ft + max_threshold)
    * @return Código de erro
    */
    int FT_Guard(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] max_threshold, Object[] min_threshold);

Exemplo de Código de Proteção contra Colisão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500); // Define parâmetros de reconexão
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("Conexão RPC bem-sucedida");
        }
        else
        {
            System.out.println("Falha na conexão RPC");
            return;
        }
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 1, 0, 0, 0, 0, 0 }; // Ativa apenas a proteção contra colisão no eixo X
        Object[] max_threshold = { 5.0, 0.01, 0.01, 0.01, 0.01, 0.01 };
        Object[] min_threshold = { 3.0, 0.01, 0.01, 0.01, 0.01, 0.01 };

        ForceTorque ft = new ForceTorque(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        DescPose desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(-14.404, -455.283, 319.847, -172.935, 25.141, -68.097);
        desc_p2 = new DescPose(-107.999, -599.174, 285.939, 153.472, 12.686, -71.284);
        desc_p3 = new DescPose(6.586, -704.897, 309.638, 178.909, -27.759, -70.479);

        int rtn = robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        System.out.println("FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
    }

Controle de Força Constante
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Controle de força constante
    * @param flag 0-desativar controle de força constante, 1-ativar controle de força constante
    * @param sensor_id Número do sensor de força
    * @param select Seleciona quais dos seis graus de liberdade detectam colisão, 0-não detectar, 1-detectar
    * @param ft Força/torque de colisão, fx, fy, fz, tx, ty, tz
    * @param ft_pid Parâmetros PID de força, parâmetros PID de torque
    * @param adj_sign Controle de adaptação liga/desliga, 0-desativar, 1-ativar
    * @param ILC_sign Controle ILC liga/desliga, 0-parar, 1-treinar, 2-praticar
    * @param max_dis Distância máxima de ajuste, em mm
    * @param max_ang Ângulo máximo de ajuste, em graus
    * @param M Parâmetros de massa rx, ry [0.1-10], padrão 2
    * @param B Parâmetros de amortecimento rx, ry [0.1-50], padrão 8
    * @param threshold Limiares de ativação rx, ry [0-10], padrão 0.2
    * @param adjustCoeff Coeficientes de ajuste de torque rx, ry [0-1], padrão 1
    * @param polishRadio Raio de polimento, em mm
    * @param filter_Sign Flag de ativação de filtro 0-desativar; 1-ativar, padrão desativado
    * @param posAdapt_sign Flag de ativação de adaptação de postura 0-desativar; 1-ativar, padrão desativado
    * @param isNoBlock Flag de bloqueio, 0-bloqueante; 1-não bloqueante
    * @return Código de erro
    */
    public int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang, double[] M, double[] B, double[] threshold, double[] adjustCoeff, double polishRadio, int filter_Sign, int posAdapt_sign, int isNoBlock)

Exemplo de Código de Controle de Força Constante com Amortecimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTControlWithAdjustCoeff(Robot robot)
    {
        int sensor_id = 10;
        int[] select = { 0,0,1,0,0,0 };
        double[] ft_pid = { 0.0008, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 1000.0;
        double max_ang = 20;
        ForceTorque ft = new ForceTorque(0.0,0,0,0,0,0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        JointPos j1 = new JointPos(80.765, -98.795, 106.548, -97.734, -89.999, 94.842);
        JointPos j2 = new JointPos(43.067, -84.429, 92.620, -98.175, -90.011, 57.144);
        DescPose desc_p1 = new DescPose(5.009, -547.463, 262.053, -179.999, -0.019, 75.923);
        DescPose desc_p2 = new DescPose(-347.966, -547.463, 262.048, -180.000, -0.019, 75.923);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        double[] M = { 2.0, 2.0 };
        double[] B = { 15.0, 15.0 };
        double[] threshold = {1.0, 1.0};
        double[] adjustCoeff = {1.0, 0.8};
        double polishRadio = 0.0;
        int filter_Sign = 0;
        int posAdapt_sign = 1;
        int isNoBlock;
        ft.fz = -10.0;
        while(true)
        {
            int rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control start rtn is %d\n", rtn);
            robot.MoveL(j1, desc_p1, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            robot.MoveL(j2, desc_p2, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control end rtn is %d\n", rtn);
        }
    }

Inserção Rotativa
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Inserção rotativa
    * @param rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param angVelRot Velocidade angular de rotação, em graus/s
    * @param ft Limiar de força/torque, fx, fy, fz, tx, ty, tz, intervalo [0~100]
    * @param max_angle Ângulo máximo de rotação, em graus
    * @param orn Direção da força/torque, 1-ao longo do eixo Z, 2-em torno do eixo Z
    * @param max_angAcc Aceleração angular máxima, em graus/s^2, não utilizado no momento, padrão 0
    * @param rotorn Direção de rotação, 1-horário, 2-anti-horário
    * @param strategy Estratégia de tratamento quando força/torque não são detectados, 0-reportar erro; 1-avisar, continuar movimento
    * @return Código de erro
    */
    public int FT_RotInsertion(int rcs, double angVelRot, double ft, double max_angle, int orn, double max_angAcc, int rotorn, int strategy)

Exemplo de Código de Inserção Rotativa com Sensor de Força do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn = -1;
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4 = new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4 = new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

Ativar Controle de Compliance
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa o controle de compliance
    * @param [in] p Coeficiente de ajuste de posição ou coeficiente de compliance
    * @param [in] force Limiar de força para ativação do compliance, em N
    * @return Código de erro
    */
    int FT_ComplianceStart(double p, double force);

Desativar Controle de Compliance
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Desativa o controle de compliance
    * @return Código de erro
    */
    int FT_ComplianceStop();

Exemplo de Código de Controle de Compliance
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCompliance(Robot robot)
    {
        DescTran tr1 = new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con = new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);

        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        int flag = 1;
        int sensor_id = 1;
        Object[] select = new Object[] { 1,1,1,0,0,0 };
        Object[] ft_pid = new Object[] { 0.0005,0.0,0.0,0.0,0.0,0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 100.0;
        double max_ang = 0.0;

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        double p = 0.00005;
        double force = 30.0;
        int rtn = robot.FT_ComplianceStart(p, force);

        int count = 15;
        while (count > 0)
        {
            robot.MoveL(j1, desc_p1, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 1, offset_pos,0,10);
            robot.MoveL(j2, desc_p2, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 0, offset_pos,0,10);
            count -= 1;
        }
        robot.FT_ComplianceStop();
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);

        robot.CloseRPC();
        return 0;
    }

Inicialização da Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Inicialização da identificação da carga
    * @return Código de erro
    */
    int LoadIdentifyDynFilterInit();

Inicialização das Variáveis de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Inicialização das variáveis de identificação da carga
    * @return Código de erro
    */
    int LoadIdentifyDynVarInit();

Programa Principal de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Programa principal de identificação da carga
    * @param [in] joint_torque Torque das juntas
    * @param [in] joint_pos Posição das juntas
    * @param [in] t Período de amostragem
    * @return Código de erro
    */
    int LoadIdentifyMain(Object[] joint_torque, Object[] joint_pos, double t);

Obter Resultado da Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o resultado da identificação da carga
    * @param [in] gain
    * @return List[0]: código de erro; List[1]: double weight Peso da carga; List[2]: x Centro de massa X mm; List[3]: y Centro de massa Y mm; List[4]: z Centro de massa Z mm
    */
    List<Number> LoadIdentifyGetResult(Object[] gain);

Exemplo de Código de Identificação da Carga do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestIdentify(Robot robot)
    {
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();

        retval = robot.LoadIdentifyDynVarInit();

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0,0,0,0,0,0);
        List<Number> joint_toq = new ArrayList<>();
        robot.GetActualJointPosDegree(posJ);
        posJ.J2 = posJ.J2 + 10;
        joint_toq = robot.GetJointTorques(0);

        Object[] gain = new Object[] { 0,0.05,0,0,0,0,0,0.02,0,0,0,0 };
        double weight = 0;
        DescTran load_pos = new DescTran(0,0,0);
        List<Number> num = new ArrayList<>();
        num = robot.LoadIdentifyGetResult(gain);

        robot.CloseRPC();
        return 0;

    }

Arrasto Assistido por Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief Arrasto assistido por sensor de força
    * @param [in] status Estado de controle, 0-desativar; 1-ativar
    * @param [in] asaptiveFlag Flag de ativação de adaptação, 0-desativar; 1-ativar
    * @param [in] interfereDragFlag Flag de arrasto em zona de interferência, 0-desativar; 1-ativar
    * @param [in] ingularityConstraintsFlag Estratégia de ponto singular, 0-evitar; 1-atravessar
    * @param [in] forceCollisionFlag Flag de detecção de colisão do robô durante arrasto assistido; 0-desativar; 1-ativar
    * @param [in] M Coeficiente de inércia
    * @param [in] B Coeficiente de amortecimento
    * @param [in] K Coeficiente de rigidez
    * @param [in] F Limiar de força de arrasto 6D
    * @param [in] Fmax Limite máximo de força de arrasto Nm
    * @param [in] Vmax Limite máximo de velocidade das juntas °/s
    * @return Código de erro
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, int ingularityConstraintsFlag, int forceCollisionFlag, Object[] M, Object[] B, Object[] K, Object[] F, double Fmax, double Vmax)

Obter Estado do Interruptor de Arrasto do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado do interruptor de arrasto do sensor de força
    * @return List[0]: código de erro; List[1]: dragState Estado de controle de arrasto assistido por sensor de força, 0-desativar; 1-ativar; List[2]: sixDimensionalDragState Estado de controle de arrasto assistido por força 6D, 0-desativar; 1-ativar
    */
    List<Integer> GetForceAndTorqueDragState();

Ativação Automática do Sensor de Força Após Limpeza de Erro
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativação automática do sensor de força após limpeza de erro
    * @param [in] status Estado de controle, 0-desativar; 1-ativar
    * @return Código de erro
    */
    int SetForceSensorDragAutoFlag(int status)

Exemplo de Código de Arrasto Assistido por Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestEndForceDragCtrl(Robot robot)
    {
        DescTran tr1 = new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        robot.SetForceSensorDragAutoFlag(1);

        Object[] M = new Object[] { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        Object[] B = new Object[] { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        Object[] K = new Object[] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] F = new Object[] { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);

        robot.Sleep(10000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        List<Integer> state = new ArrayList<>();
        state = robot.GetForceAndTorqueDragState();

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
        return 0;
    }

Definir Interruptor e Parâmetros do Arrasto Híbrido de Força 6D e Impedância Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o interruptor e parâmetros do arrasto híbrido de força 6D e impedância articular
    * @param [in] status Estado de controle, 0-desativar; 1-ativar
    * @param [in] impedanceFlag Flag de ativação de impedância, 0-desativar; 1-ativar
    * @param [in] lamdeGain Ganho de arrasto
    * @param [in] KGain Ganho de rigidez
    * @param [in] BGain Ganho de amortecimento
    * @param [in] dragMaxTcpVel Velocidade linear máxima do TCP durante arrasto
    * @param [in] dragMaxTcpOriVel Velocidade angular máxima do TCP durante arrasto
    * @return Código de erro
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, Object[] lamdeGain, Object[] KGain, Object[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

Exemplo de Código de Arrasto Híbrido de Força 6D e Impedância Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestForceAndJointImpedance(Robot robot)
    {
        robot.DragTeachSwitch(1);
        Object[] lamdeDain = new Object[] { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        Object[] KGain = new Object[]{ 0, 0, 0, 0, 0, 0 };
        Object[] BGain = new Object[] { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.Sleep(10000);

        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.CloseRPC();
        return 0;
    }

Controle de Ativação/Desativação de Impedância
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Controle de ativação/desativação de impedância
    * @param [in] status 0: desativar; 1-ativar
    * @param [in] workSpace 0-espaço articular; 1-espaço cartesiano
    * @param [in] forceThreshold Limiar de força de ativação (N)
    * @param [in] m Parâmetro de massa
    * @param [in] b Parâmetro de amortecimento
    * @param [in] k Parâmetro de rigidez
    * @param [in] maxV Velocidade linear máxima (mm/s)
    * @param [in] maxVA Aceleração linear máxima (mm/s²)
    * @param [in] maxW Velocidade angular máxima (°/s)
    * @param [in] maxWA Aceleração angular máxima (°/s²)
    * @return Código de erro
    */
    public int ImpedanceControlStartStop(int status, int workSpace, double[] forceThreshold, double[] m, double[] b, double[] k, double maxV, double maxVA, double maxW, double maxWA)

Exemplo de Código de Controle de Ativação/Desativação de Impedância do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestImpedanceControl(Robot robot)
    {
        JointPos j1 = new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2 = new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1 = new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2 = new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 200.0;
        double ovl = 100.0;
        double blendT = -1.0;
        double blendR = -1.0;
        int flag = 0;
        int search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        DeviceConfig con = new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        System.out.println("FT config:"+con.company+","+con.device+","+con.softwareVersion+"con"+ con.bus);
        robot.Sleep(1000);
        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);
        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);
        robot.FT_SetZero(1);
        robot.Sleep(1000);
        double[] forceThreshold = { 30,30,30,5,5,5 };
        double[] m = { 0.1,0.1,0.1,0.02,0.02,0.02 };
        double[] b = { 1,1,1,0.08,0.08,0.08 };
        double[] k = { 0,0,0,0,0,0 };
        int rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        System.out.println("ImpedanceControlStartStop errcode:"+ rtn);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        System.out.println("movel errcode:"+ rtn);
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        robot.CloseRPC();
        return 0;
    }

Ativar Função de Compensação de Torque e Coeficientes de Compensação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa a função de compensação de torque e coeficientes de compensação
    * @param status Interruptor, 0-desativar; 1-ativar
    * @param torqueCoeff Coeficientes de compensação de torque J1-J6 [0-1]
    * @return Código de erro
    */
    public int SetCoderCompenParams(int status, double[] torqueCoeff)