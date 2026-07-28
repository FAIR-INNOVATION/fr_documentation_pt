Periféricos do Robô
========================

.. toctree:: 
    :maxdepth: 5

Configurar Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Configura a garra
    * @param  [in] config .company   Fabricante da garra, 1-Robotiq, 2-Huiling, 3-Tianji, 4-Dahuan, 5-Zhixing
    * @param  [in] config .device   Número do dispositivo, Robotiq(0-2F-85 series), Huiling(0-NK series,1-Z-EFG-100), Tianji(0-TEG-110), Dahuan(0-PGI-140), Zhixing(0-CTPM2F20)
    * @param  [in] config .softvesion   Número da versão do software, não usado no momento, padrão 0
    * @param  [in] config .bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    int SetGripperConfig(DeviceConfig config);

Obter Configuração da Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a configuração da garra
    * @param  [out] config .company   Fabricante da garra, 1-Robotiq, 2-Huiling, 3-Tianji, 4-Dahuan, 5-Zhixing
    * @param  [out] config .device   Número do dispositivo, Robotiq(0-2F-85 series), Huiling(0-NK series,1-Z-EFG-100), Tianji(0-TEG-110), Dahuan(0-PGI-140), Zhixing(0-CTPM2F20)
    * @param  [out] config .softvesion   Número da versão do software, não usado no momento, padrão 0
    * @param  [out] config .bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    int GetGripperConfig(DeviceConfig config);

Ativar Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Ativa a garra
    * @param  [in] index   Número da garra
    * @param  [in] act  0-reset, 1-ativar
    * @return  Código de erro
    */
    int ActGripper(int index, int act); 

Controlar Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Controla a garra
    * @param  [in] index   Número da garra
    * @param  [in] pos   Porcentagem de posição, faixa [0~100]
    * @param  [in] vel   Porcentagem de velocidade, faixa [0~100]
    * @param  [in] force   Porcentagem de torque, faixa [0~100]
    * @param  [in] max_time   Tempo máximo de espera, faixa [0~30000], unidade ms
    * @param  [in] block  0-bloqueado, 1-não bloqueado
    * @param  [in] type  Tipo de garra, 0-garra paralela; 1-garra rotativa
    * @param  [in] rotNum  Número de rotações
    * @param  [in] rotVel  Porcentagem de velocidade de rotação [0-100]
    * @param  [in] rotTorque  Porcentagem de torque de rotação [0-100]
    * @return Código de erro
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, int block, int type, double rotNum, int rotVel, int rotTorque); 

Obter Estado de Movimento da Garra
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado de movimento da garra
    * @return List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]: status  0-movimento não concluído, 1-movimento concluído
    */
    List<Integer> GetGripperMotionDone(); 

Obter Estado de Ativação da Garra
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado de ativação da garra
    * @return  List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]: status  bit0~bit15 correspondem aos números das garras 0~15, bit=0 não ativado, bit=1 ativado
    */
    List<Number> GetGripperActivateStatus()

Obter Posição da Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a posição da garra
    * @return  List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]: position   Porcentagem de posição, faixa 0~100%
    */
    List<Number> GetGripperCurPosition()

Obter Velocidade da Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a velocidade da garra
    * @return  List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]: speed   Porcentagem de velocidade, faixa 0~100%
    */
    List<Number> GetGripperCurSpeed()

Obter Corrente da Garra
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a corrente da garra
    * @return  List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]: current   Porcentagem de corrente, faixa 0~100%
    */
    List<Number> GetGripperCurCurrent()

Obter Tensão da Garra
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a tensão da garra
    * @return List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]:voltage   Tensão, unidade 0.1V
    */
    List<Number> GetGripperVoltage()

Obter Temperatura da Garra
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a temperatura da garra
    * @return List[0]: Código de erro; List[1] : fault  0-sem erro, 1-com erro; List[2]:temp   Temperatura, unidade ℃
    */
    List<Number> GetGripperTemp()

Calcular Ponto de Pré-Captura - Visão
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Calcula o ponto de pré-captura - Visão 
    * @param [in] desc_pos   Pose cartesiana do ponto de captura
    * @param [in] zlength   Deslocamento no eixo Z
    * @param [in] zangle    Deslocamento de rotação em torno do eixo Z
    * @param [out] pre_pos  Ponto de pré-captura
    * @return Código de erro 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, DescPose pre_pos);

Calcular Ponto de Retirada - Visão
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Calcula o ponto de retirada - Visão 
    * @param [in] desc_pos   Pose cartesiana do ponto de captura
    * @param [in] zlength   Deslocamento no eixo Z 
    * @param [in] zangle    Deslocamento de rotação em torno do eixo Z
    * @param [out] post_poss  Ponto de retirada
    * @return Código de erro 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, DescPose post_pos);

Exemplo de Código para Operações com a Garra do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGripper(Robot robot)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        int act = 0;
        int max_time = 30000;
        int block = 0;

        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        DeviceConfig cnn=new DeviceConfig(company,device,softversion,bus);
        robot.SetGripperConfig(cnn);
        robot.GetGripperConfig(cnn);

        robot.ActGripper(index, act);
        robot.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        robot.Sleep(1000);

        robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
        robot.Sleep(1000);
        robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);

        List<Integer> stat=new ArrayList<>();
        stat=robot.GetGripperMotionDone();

        List<Number> list=new ArrayList<>();
        list=robot.GetGripperActivateStatus();

        list=robot.GetGripperCurPosition();

        list=robot.GetGripperCurCurrent();

        list=robot.GetGripperVoltage();

        list=robot.GetGripperTemp();

        list=robot.GetGripperCurSpeed();

        int retval = 0;
        DescPose prepick_pose = new DescPose(){};
        DescPose postpick_pose = new DescPose(){};

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        retval = robot.ComputePrePick(p1Desc, 10, 0, prepick_pose);

        retval = robot.ComputePostPick(p2Desc, -10, 0, postpick_pose);
        return 0;
    }

Obter Número de Rotações da Garra Rotativa
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o número de rotações da garra rotativa
    * @return List[0]: Código de erro List[1]: 0-sem erro, 1-com erro List[2]: Número de rotações
    */
    List<Number> GetGripperRotNum(); 

Obter Porcentagem de Velocidade de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a porcentagem de velocidade de rotação da garra rotativa
    * @return List[0]: Código de erro List[1]: 0-sem erro, 1-com erro List[2]: Porcentagem de velocidade de rotação
    */
    List<Number> GetGripperRotSpeed(); 

Obter Porcentagem de Torque de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a porcentagem de torque de rotação da garra rotativa
    * @return List[0]: Código de erro List[1]: 0-sem erro, 1-com erro List[2]: Porcentagem de torque de rotação
    */
    List<Number> GetGripperRotTorque(); 

Exemplo de Código para Obter Estado da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRotGripperState(Robot robot)
    {
        int fault = 0;
        List<Number> rotNum=new ArrayList<>();
        List<Number> rotSpeed=new ArrayList<>();
        List<Number> rotTorque=new ArrayList<>();

        rotNum=robot.GetGripperRotNum();
        rotSpeed=robot.GetGripperRotSpeed();
        rotTorque=robot.GetGripperRotTorque();
        System.out.println("gripper rot num :"+rotNum.get(2)+ ", gripper rotSpeed :"+rotSpeed.get(2)+",gripper rotTorque : "+rotTorque.get(2));

        return 0;
    }

Iniciar/Parar Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Inicia/para a esteira transportadora
    * @param  [in] status Estado, 1-iniciar, 0-parar
    * @return  Código de erro
    */
    int ConveyorStartEnd(int status);

Registrar Ponto de Detecção IO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Registra o ponto de detecção IO
    * @return  Código de erro
    */
    int ConveyorPointIORecord();

Registrar Ponto A
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Registra o ponto A
    * @return  Código de erro
    */
    int ConveyorPointARecord(); 

Registrar Ponto de Referência
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Registra o ponto de referência
    * @return  Código de erro
    */
    int ConveyorRefPointRecord();

Registrar Ponto B
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Registra o ponto B
    * @return Código de erro
    */
    int ConveyorPointBRecord(); 

Detecção IO de Peça na Esteira
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Detecção IO de peça na esteira
    * @param [in] max_t Tempo máximo de detecção, unidade ms
    * @return Código de erro 
    */ 
    int ConveyorIODetect(int max_t);

Obter Posição Atual do Objeto
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a posição atual do objeto
    * @param [in] mode 1-captura com rastreamento, 2-movimento com rastreamento, 3-rastreamento TPD
    * @return Código de erro 
    */ 
    int ConveyorGetTrackData(int mode);

Iniciar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Inicia o rastreamento da esteira
    * @param [in] status Estado, 1-iniciar, 0-parar
    * @return Código de erro 
    */ 
    int ConveyorTrackStart(int status);

Parar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Para o rastreamento da esteira
    * @return Código de erro 
    */ 
    int ConveyorTrackEnd();

Configurar Parâmetros da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief  Configura os parâmetros da esteira
    * @param [in] encChannel Canal do encoder 1~2
    * @param [in] resolution Número de pulsos do encoder por rotação
    * @param [in] lead Distância percorrida pela esteira por rotação do encoder
    * @param [in] wpAxis Número do sistema de coordenadas da peça (para movimento de rastreamento, escolha o número do sistema de coordenadas; para captura com rastreamento e rastreamento TPD, defina como 0)
    * @param [in] vision Se usa visão  0-não usa  1-usa
    * @param [in] speedRadio Relação de velocidade (para a opção de captura com rastreamento da esteira [1-100]; para outras opções, padrão 1)
    * @return Código de erro
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis, int endDis); 

Definir Compensação do Ponto de Captura da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a compensação do ponto de captura da esteira
    * @param [in] cmp Compensação de posição double[3]{x, y, z}
    * @return Código de erro 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

Movimento Linear com Rastreamento da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Movimento linear com rastreamento da esteira
    * @param [in] name Nome do ponto de movimento
    * @param [in] tool Número da ferramenta, faixa [0~14]
    * @param [in] wobj Número da peça, faixa [0~14]
    * @param [in] vel Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @return Código de erro 
    */ 
    int ConveyorTrackMoveL(String name, int tool, int wobj, double vel, double acc, double ovl, double blendR);   

Detecção de Entrada de Comunicação da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief Detecção de entrada de comunicação da esteira
    * @param [in] timeout Tempo limite de espera ms
    * @return Código de erro
    */
    int ConveyorComDetect(int timeout);

Acionamento da Detecção de Entrada de Comunicação da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief Acionamento da detecção de entrada de comunicação da esteira
    * @param [in] timeout Tempo limite de espera ms
    * @return Código de erro
    */
    int ConveyorComDetectTrigger();

Exemplo de Programa de Operação da Esteira do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestConveyor(Robot robot)
    {
        int retval = 0;

        retval = robot.ConveyorStartEnd(1);

        retval = robot.ConveyorPointIORecord();

        retval = robot.ConveyorPointARecord();

        retval = robot.ConveyorRefPointRecord();

        retval = robot.ConveyorPointBRecord();

        retval = robot.ConveyorStartEnd(0);

        retval = 0;

        retval = robot.ConveyorSetParam(1,10000,200,0,0,20,0,0,100);

        Object[] cmp = new Object[]{ 0.0, 0.0, 0.0 };
        retval = robot.ConveyorCatchPointComp(cmp);

        int index = 1;
        int max_time = 30000;
        int block = 0;
        retval = 0;

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);


        retval = robot.MoveCart(p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.WaitMs(1);

        retval = robot.ConveyorTrackStart(1);

        retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);

        retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.ConveyorTrackEnd();

        robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);

        return 0;
    }

Configuração de Parâmetros de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Configura os parâmetros de rastreamento em posição da esteira transportadora
    * @param  [in] trackMode 0-tempo; 1-distância; 2-tempo e distância, qualquer condição satisfeita
    * @param  [in] trackTime Tempo de rastreamento, unidade s
    * @param  [in] trackDis Distância de rastreamento
    * @return  Código de erro
    */
    public int SetStationaryTrackPara(int trackMode, double trackTime, int trackDis)

Exemplo de Código de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestStationaryTrack(Robot robot)
    {
        System.out.println("\n========== Teste de Rastreamento Estacionário da Esteira ==========");

        int rtn;

        JointPos j1 = new JointPos(-35.146, -102.684, 120.805, -100.401, -90.295, 150.105);
        DescPose d1 = new DescPose(-121.814, -348.341, 209.978, -173.152, -3.585, -5.446);

        ExaxisPos ex = new ExaxisPos(0, 0, 0, 0);
        DescPose zeroOff = new DescPose(0, 0, 0, 0, 0, 0);

        int tool = 1;
        int workpiece = 1;

        rtn = robot.ConveyorSetParam(0, 10000, 200, 0, 0, 10,0,0,0);


        robot.MoveJ(j1, d1, tool, workpiece, 100, 100, 100, ex, -1, 0, zeroOff);

        // Step 1: Sinal de controle SetDO
        System.out.println("--- Step 1: SetDO(6,1) ---");
        rtn = robot.SetDO(6, 1, 0, 0);
        System.out.println("  SetDO(6,1) rtn=" + rtn);

        // Step 2: Início do rastreamento da esteira
        System.out.println("--- Step 2: ConveyorTrackStart(2) ---");
        rtn = robot.ConveyorTrackStart(2);
        System.out.println("  ConveyorTrackStart(2) rtn=" + rtn);

        // Step 3: Detecção IO da peça
        System.out.println("--- Step 3: ConveyorIODetect(10000) ---");
        rtn = robot.ConveyorIODetect(10000);
        System.out.println("  ConveyorIODetect(10000) rtn=" + rtn);

        // Step 4: Obter dados de rastreamento
        System.out.println("--- Step 4: ConveyorGetTrackData(2) ---");
        rtn = robot.ConveyorGetTrackData(2);
        System.out.println("  ConveyorGetTrackData(2) rtn=" + rtn);

        // Step 5: Configuração de parâmetros de rastreamento estacionário (modo tempo, 200s, distância 5)
        System.out.println("--- Step 5: SetStationaryTrackPara(0,200,5) ---");
        rtn = robot.SetStationaryTrackPara(0, 5, 5);
        System.out.println("  SetStationaryTrackPara(0,200,5) rtn=" + rtn);

        // Step 6: Executar movimento estacionário
        System.out.println("--- Step 6: MoveStationary() ---");
        rtn = robot.MoveStationary();
        robot.WaitStationaryMotionDone();
        System.out.println("  MoveStationary() rtn=" + rtn);

        // Step 7: Fim do rastreamento da esteira
        System.out.println("--- Step 7: ConveyorTrackEnd() ---");
        rtn = robot.ConveyorTrackEnd();
        System.out.println("  ConveyorTrackEnd() rtn=" + rtn);

        // Step 8: Sinal de desligamento SetDO
        System.out.println("--- Step 8: SetDO(6,0) ---");
        rtn = robot.SetDO(6, 0, 0, 0);
        System.out.println("  SetDO(6,0) rtn=" + rtn);

        System.out.println("\n========== Teste de Rastreamento Estacionário Concluído ==========");
        return 0;
    }

Configurar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Configura o sensor de extremidade
    * @param [in] config idCompany Fabricante, 18-JUNKONG；25-HUIDE
    * @param [in] config idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware Versão do software, 0-J1.0/HuiDe1.0 (temporariamente não disponível)
    * @param [in] config idBus Posição de montagem, 1-porta 1 da extremidade; 2-porta 2 da extremidade...8-porta 8 da extremidade (temporariamente não disponível)
    * @return Código de erro
    */
    int AxleSensorConfig(DeviceConfig config);

Obter Configuração do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a configuração do sensor de extremidade
    * @param [out] config idCompany Fabricante, 18-JUNKONG；25-HUIDE
    * @param [out] config idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
    * @return Código de erro
    */
    int AxleSensorConfigGet(DeviceConfig config);

Ativar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Ativa o sensor de extremidade
    * @param [in] actFlag 0-reset; 1-ativar
    * @return Código de erro
    */
    int AxleSensorActivate(int actFlag);

Escrita no Registrador do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Escrita no registrador do sensor de extremidade
    * @param [in] devAddr  Endereço do dispositivo 0-255
    * @param [in] regHAddr 8 bits altos do endereço do registrador
    * @param [in] regLAddr 8 bits baixos do endereço do registrador
    * @param [in] regNum  Número de registradores 0-255
    * @param [in] data1 Valor 1 a ser escrito no registrador
    * @param [in] data2 Valor 2 a ser escrito no registrador
    * @param [in] isNoBlock 0-bloqueado; 1-não bloqueado
    * @return Código de erro
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

Exemplo de Código do Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleSensor(Robot robot)
    {
        DeviceConfig con=new DeviceConfig(18,0,0,1);
        robot.AxleSensorConfig(con);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(con);

        int rtn = robot.AxleSensorActivate(1);

        robot.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        return 0;
    }

Obter Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém o protocolo de periféricos do robô
    * @return List[0]: Código de erro; List[1] : int protocol  Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

Definir Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o protocolo de periféricos do robô
    * @param [in] protocol Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster
    * @return Código de erro 
    */
    int SetExDevProtocol(int protocol);

Exemplo de Programa para Definir Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExDevProtocol(Robot robot)
    {
        int protocol = 4096;
        int rtn = robot.SetExDevProtocol(protocol);
        List<Integer> integer=new ArrayList<>();
        integer = robot.GetExDevProtocol();

        return 0;
    }

Obter Parâmetros de Comunicação da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém os parâmetros de comunicação da extremidade
    * @param [out] param Parâmetros de comunicação da extremidade
    * @return Código de erro 
    */
    int GetAxleCommunicationParam(AxleComParam param)

Definir Parâmetros de Comunicação da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define os parâmetros de comunicação da extremidade
    * @param [in] param Parâmetros de comunicação da extremidade
    * @return Código de erro 
    */
    int SetAxleCommunicationParam(AxleComParam param)

Definir Tipo de Transferência de Arquivo da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o tipo de transferência de arquivo da extremidade
    * @param [in] type 1-arquivo de atualização MCU; 2-arquivo LUA
    * @return  Código de erro
    */
    public int SetAxleFileType(int type)

Ativar Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa a execução LUA na extremidade
    * @param [in] enable 0-desativar; 1-ativar
    * @return  Código de erro
    */
    public int SetAxleLuaEnable(int enable)

Recuperação de Erro de Arquivo LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Recuperação de erro de arquivo LUA na extremidade
    * @param [in] status 0-não recuperar; 1-recuperar
    * @return  Código de erro
    */
    public int SetRecoverAxleLuaErr(int status)

Obter Estado de Ativação da Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado de ativação da execução LUA na extremidade
    * @param [out] status[0]: 0-desativado; 1-ativado
    * @return  Código de erro
    */
    int GetAxleLuaEnableStatus(int[] status)

Definir os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os tipos de dispositivo de extremidade habilitados para o LUA
    * @param forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    * @param gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
    * @param IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    * @param dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
    * @return  Código de erro
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable, int dexhandEnable)

Obter os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém os tipos de dispositivo de extremidade habilitados para o LUA
     * @param enable enable[0]:forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
     * @param enable enable[1]:gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
     * @param enable enable[2]:IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
     * @param enable enable[3]:dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
     * @return  Código de erro
     */
    public int GetAxleLuaEnableDeviceType(int[] enable)

Obter os dispositivos de extremidade atualmente configurados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém os dispositivos de extremidade atualmente configurados
     * @param forceSensorEnable Número do dispositivo de sensor de força habilitado, 0-desabilitado; 1-habilitado
     * @param gripperEnable Número do dispositivo de garra habilitado, 0-desabilitado; 1-habilitado
     * @param IODeviceEnable Número do dispositivo IO habilitado, 0-desabilitado; 1-habilitado
     * @param dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
     * @return  Código de erro
     */
    public int GetAxleLuaEnableDevice(int[] forceSensorEnable, int[] gripperEnable, int[] IODeviceEnable, int[] dexhandEnable)


Definir as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Define as funções de controle de ação da garra habilitadas
     * @param id Número do dispositivo da garra
     * @param func func[0]-habilitação da garra; func[1]-inicialização da garra; func[2]-definição de posição; func[3]-definição de velocidade; func[4]-definição de torque; func[6]-leitura do estado da garra;
        func[7]-leitura do estado de inicialização; func[8]-leitura do código de falha; func[9]-leitura da posição; func[10]-leitura da velocidade; func[11]-leitura do torque; func[12]-definição do número de rotações para garra rotativa;
        func[13]-definição da velocidade de rotação para garra rotativa; func[14]-definição do torque de rotação para garra rotativa; func[15]-leitura do estado da garra rotativa; func[16]-leitura do estado de inicialização da garra rotativa;
        func[17]-leitura do número de rotações da garra rotativa; func[18]-leitura da velocidade da garra rotativa; func[19]-leitura do torque da garra rotativa; func[20]-definição de movimento síncrono multi-eixo; func[21]-comando de limpeza de falhas;
        func[22]-estado de operação de eixo único; func[23]-estado de operação de todos os eixos;
     * @return  Código de erro
     */
    public int SetAxleLuaGripperFunc(int id, int[] func)

Obter as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém as funções de controle de ação da garra habilitadas
     * @param id Número do dispositivo da garra
     * @param func func[0]-habilitação da garra; func[1]-inicialização da garra; func[2]-definição de posição; func[3]-definição de velocidade; func[4]-definição de torque; func[6]-leitura do estado da garra;
        func[7]-leitura do estado de inicialização; func[8]-leitura do código de falha; func[9]-leitura da posição; func[10]-leitura da velocidade; func[11]-leitura do torque; func[12]-definição do número de rotações para garra rotativa;
        func[13]-definição da velocidade de rotação para garra rotativa; func[14]-definição do torque de rotação para garra rotativa; func[15]-leitura do estado da garra rotativa; func[16]-leitura do estado de inicialização da garra rotativa;
        func[17]-leitura do número de rotações da garra rotativa; func[18]-leitura da velocidade da garra rotativa; func[19]-leitura do torque da garra rotativa; func[20]-definição de movimento síncrono multi-eixo; func[21]-comando de limpeza de falhas;
        func[22]-estado de operação de eixo único; func[23]-estado de operação de todos os eixos;
     * @return  Código de erro
     */
    public int GetAxleLuaGripperFunc(int id, int[] func)

Escrita de Arquivo no Escravo Ethercat do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Escrita de arquivo no escravo Ethercat do robô
     * @param type Tipo de arquivo do escravo, 1-arquivo de atualização do escravo; 2-arquivo de configuração do escravo
     * @param slaveID Número do escravo
     * @param fileName Nome do arquivo a ser enviado
     * @return  Código de erro
     */
    public int SlaveFileWrite(int type, int slaveID, String fileName)

Enviar Arquivo de Protocolo Aberto LUA da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Envia arquivo de protocolo aberto LUA da extremidade
     * @param filePath Caminho do arquivo lua local ".../AXLE_LUA_End_DaHuan.lua"
     * @return Código de erro
     */
    public int AxleLuaUpload(String filePath)

Entrar no Modo Boot do Escravo Ethercat do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Entrar no modo boot do escravo Ethercat do robô
     * @return  Código de erro
     */
    public int SetSysServoBootMode()

Exemplo de Código para Operações com Arquivos LUA da Extremidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleLua(Robot robot)
    {
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");

        AxleComParam param=new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        robot.GetAxleCommunicationParam(param);

        robot.SetAxleLuaEnable(1);
        int[] luaEnableStatus = new int[]{0};
        robot.GetAxleLuaEnableStatus(luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int [] enable=new int[]{0,0,0};
        robot.GetAxleLuaEnableDeviceType(enable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        robot.GetAxleLuaGripperFunc(1, getFunc);
        int[] getforceEnable = { 0,0,0,0,0,0,0,0};
        int[] getgripperEnable = { 0,0,0,0,0,0,0,0};
        int[] getioEnable = { 0,0,0,0,0,0,0,0};
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getforceEnable[i]);
        }
        System.out.println("getgripperEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getgripperEnable[i]);
        }
        System.out.println("getioEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getioEnable[i]);
        }
        robot.ActGripper(1, 0);
        robot.Sleep(2000);
        robot.ActGripper(1, 1);
        robot.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
            pkg=robot.GetRobotRealTimeState();
            System.out.println("gripper pos is:"+pkg.gripper_position);
            robot.Sleep(100);
        }

    }

Obter Estado dos Botões do SmartTool
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado dos botões do SmartTool
    * @param [out] state Estado dos botões do SmartTool; (bit0:0-comunicação normal; 1-comunicação perdida; bit1-operação de desfazer; bit2-limpar programa; bit3-tecla A; bit4-tecla B; bit5-tecla C; bit6-tecla D; bit7-tecla E; bit8-tecla IO; bit9-manual/automático; bit10-iniciar)
    * @return Código de erro
    */
    int GetSmarttoolBtnState(int[] state)

Exemplo de Código do Botão SmartTool
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args) 
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 500);//Definir número de tentativas de reconexão, intervalo
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn == 0) {
            System.out.println("Conexão RPC bem-sucedida");
        } else {
            System.out.println("Falha na conexão RPC");
            return;
        }

        int[] state = {0};
        while (true)
        {
            robot.GetSmarttoolBtnState(state);

            String binaryString = String.format("%32s", Integer.toBinaryString(state[0])).replace(' ', '0');
            System.out.println("GetSmarttoolBtnState:"+binaryString);
            robot.Sleep(100);
        }
    }

Enviar Arquivo Lua de Protocolo Aberto
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Envia arquivo Lua de protocolo aberto
    * @param  filePath Caminho do arquivo lua de protocolo aberto local
    * @return Código de erro
    */
    public int OpenLuaUpload(String filePath)

Obter Parâmetros da Placa Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém os parâmetros da placa escrava
    * @param  type  0-Ethercat, 1-CClink, 3-Ethercat, 4-EIP
    * @param  version  Versão do protocolo
    * @param  connState  0-desconectado 1-conectado
    * @return  Código de erro
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

Escrever DO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Escreve DO no escravo
    * @param   DOIndex  Número do DO
    * @param   wirteNum  Número a ser escrito
    * @param   status Valor a ser escrito, máximo de 8
    * @return  Código de erro
    */
    public int FieldBusSlaveWriteDO(int DOIndex, int wirteNum, int[] status)

Escrever AO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /*
    * @brief  Escrever AO no Escravo
    * @param  AOIndex Número AO
    * @param  writeNum Número de valores a escrever
    * @param  status Matriz de valores a escrever (máximo 8), AO0~AO15 são do tipo inteiro, AO16~AO31 são do tipo ponto flutuante
    * @return  Código de erro
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int writeNum, double[] status)

Ler DI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Lê DI do escravo
    * @param  DOIndex  Número do DI
    * @param  readNum  Número a ser lido
    * @param  status Valor lido, máximo de 8
    * @return  Código de erro
    */
    public int FieldBusSlaveReadDI(int DOIndex, int readNum, int[] status)

Ler AI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Lê AI do escravo
    * @param  AIIndex  Número do AI
    * @param  readNum  Número a ser lido
    * @param  status Valor lido, máximo de 8
    * @return  Código de erro
    */
    public int FieldBusSlaveReadAI(int AIIndex, int readNum, double[] status)

Aguardar Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda entrada DI de extensão
    * @param  DIIndex Número do DI
    * @param  status 0-nível baixo; 1-nível alto
    * @param  waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda entrada AI de extensão
    * @param  AIIndex Número do AI
    * @param  waitType 0-maior que; 1-menor que
    * @param  value Valor do AI
    * @param  waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

Exemplo de Código para Interfaces de Instrução do Modo Escravo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testFieldBusBoard(Robot robot)
    {
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("D://zUP/1111/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);
        int[] type=new int[1];
        int[] version=new int[1];
        int[] connState=new int[1];
        //Obter tipo de protocolo da placa escrava, versão do software, status de conexão com CLP
        robot.GetFieldBusConfig(type, version, connState);
        System.out.println("type is: "+type[0]+", version is : "+version[0]+", connState is : "+connState[0]);
        //Escrever DO0 = 1, DO1 = 0, DO2 = 1
        int[] ctrl =new int[8];
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
        //Escrever AO2 = 0x1000
        int[] ctrlAO =new int[8];
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);
        int[] DI=new int[4];
        double[] AI=new double[3];
        //Monitorar DI0~DI3 AI0~AI2 em loop
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            System.out.println("DI0 is: "+DI[0]+", DI1 is: "+DI[1]+",DI2 is: "+DI[2]+",DI3 is: "+DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            System.out.println("AI0 is: "+AI[0]+ ",AI1 is: "+AI[1]+",AI2 is: "+AI[2]);
            robot.Sleep(10);
        }
        //Aguardar DI0 ser igual a 1, tempo de espera 100ms, imprimir resultado
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        System.out.println("FieldBusSlaveWaitDI result is: "+ ret);
        //Aguardar AI0 ser maior que 400, tempo de espera 100ms, imprimir resultado
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        System.out.println("FieldBusSlaveWaitAI result is: "+ ret);
        robot.CloseRPC();
    }

Controlar Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Controla a matriz de ventosas
    * @param  slaveID Número do escravo
    * @param  len Comprimento
    * @param  ctrlValue Valor de controle 1-sucção com vácuo máximo 2-sucção com vácuo definido 3-parar sucção
    * @return Código de erro
    */
    public int SetSuckerCtrl(int slaveID, int len, int[] ctrlValue)

Obter Estado da Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado da matriz de ventosas
    * @param  slaveID Número do escravo
    * @param  state Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    * @param  pressValue Vácuo atual unidade kPa
    * @param  error Código de erro atual da ventosa
    * @return Código de erro
    */
    public int GetSuckerState(int slaveID, int[] state, int[] pressValue, int[] error)

Aguardar Estado da Ventosa
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda o estado da ventosa
    * @param  slaveID Número do escravo
    * @param  state Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    * @param  ms Tempo máximo de espera
    * @return Código de erro
    */
    public int WaitSuckerState(int slaveID, int state, int ms)

Exemplo de Código para Instruções de Controle da Matriz de Ventosas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testSucker(Robot robot)
    {
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("C：//openlua/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);
        //Controlar ventosa em modo broadcast com capacidade máxima de sucção
        int[] ctrl = {1};
        robot.SetSuckerCtrl(0, 1, ctrl);
        int[] state=new int[1];
        int[] pressVlaue=new int[1];
        int[] error=new int[1];
        //Monitorar estados da ventosa 1 e ventosa 12 em loop
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, state,pressVlaue, error);
            System.out.println("sucker1 state is:"+state[0]+",pressVlaue is:"+pressVlaue[0]+",error num is"+error[0]);
            robot.GetSuckerState(12, state, pressVlaue, error);
            System.out.println("sucker12 state is :"+state[0]+", pressVlaue is:"+pressVlaue[0]+",error num is:"+error[0]);
            robot.Sleep(100);
        }
        //Aguardar ventosa 1 atingir estado de objeto aderido, tempo de espera 100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        System.out.println("WaitSuckerState result is:"+ ret);
        //Modo unicast para desligar ventosas 1 e 12
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
        robot.CloseRPC();
    }

Função de Ligar/Desligar Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Função para ligar/desligar periférico laser
     * @param [in] OnOff 0-desligar 1-ligar
     * @param [in] weldId ID da solda, padrão 0
     * @return Código de erro
     */
    public int LaserTrackingLaserOnOff(int OnOff, int weldId)
    
Função de Iniciar/Parar Rastreamento a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:
    
    /**
     * @brief Função para iniciar/parar rastreamento a laser
     * @param [in] OnOff 0-parar 1-iniciar
     * @param [in] coordId Número do sistema de coordenadas da ferramenta do periférico laser
     * @return Código de erro
     */
    public int LaserTrackingTrackOnOff(int OnOff, int coordId)

Busca de Posição a Laser - Direção Fixa
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Busca de posição a laser - Direção fixa
     * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
     * @param [in] vel Velocidade unidade %
     * @param [in] distance Distância máxima de busca unidade mm
     * @param [in] timeout Tempo limite de busca unidade ms
     * @param [in] posSensorNum Número do sistema de coordenadas da ferramenta calibrado para o laser
     * @return Código de erro
     */
    public int LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum)
    
Busca de Posição a Laser - Direção Arbitrária
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Busca de posição a laser - Direção arbitrária
     * @param [in] directionPoint Coordenadas xyz do ponto de entrada da busca
     * @param [in] vel Velocidade unidade %
     * @param [in] distance Distância máxima de busca unidade mm
     * @param [in] timeout Tempo limite de busca unidade ms
     * @param [in] posSensorNum Número do sistema de coordenadas da ferramenta calibrado para o laser
     * @return Código de erro
     */
    public int LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum)
   
Fim da Busca de Posição a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
   :linenos:

   /**
    * @brief  Fim da busca de posição a laser
    * @return Código de erro
    */
    public int LaserTrackingSearchStop()

Configuração de IP do Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
   :linenos:

    /**
     * @brief Configuração de IP do laser
     * @param [in] ip Endereço IP do periférico laser
     * @param [in] port Número da porta do periférico laser
     * @return Código de erro
     */
    public int LaserTrackingSensorConfig(String ip, int port)

Configuração do Período de Amostragem do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Configuração do período de amostragem do periférico laser
     * @param [in] period Período de amostragem do periférico laser unidade ms
     * @return Código de erro
     */
    public int LaserTrackingSensorSamplePeriod(int period)

Carregar Driver do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Carregar driver do periférico laser
     * @param [in] type Tipo de protocolo do driver do periférico laser 101-Ruiniu 102-Chuangxiang 103-Quanshi 104-Tongzhou 105-Aotai
     * @return Código de erro
     */
    public int LoadPosSensorDriver(int type)

Descarregar Driver do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Descarregar driver do periférico laser
     * @return Código de erro
     */
    public int UnLoadPosSensorDriver()

Gravação da Trajetória da Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Gravação da trajetória da solda a laser
     * @param [in] status 0-parar gravação 1-rastreamento em tempo real 2-iniciar gravação
     * @param [in] delayTime Tempo de atraso unidade ms
     * @return Código de erro
     */
    public int LaserSensorRecord1(int status, int delayTime)

Reprodução da Trajetória da Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Reprodução da trajetória da solda a laser
     * @param [in] delayTime Tempo de atraso unidade ms
     * @param [in] speed Velocidade unidade %
     * @return Código de erro
     */
    public int LaserSensorReplay(int delayTime, double speed)

Reprodução do Rastreamento a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Reprodução do rastreamento a laser
     * @return Código de erro
     */
    public int MoveLTR()

Reprodução da Trajetória da Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief Reprodução da trajetória da solda a laser
    * @param delayMode Modo de atraso 0-tempo de atraso 1-distância de atraso
    * @param delayTime Tempo de atraso unidade ms
    * @param delayDisExAxisNum Número do eixo de extensão
    * @param delayDis Distância de atraso unidade mm
    * @param sensitivePara Coeficiente de sensibilidade de compensação
    * @param trackMode Tipo de rastreamento pontual. 0-movimento assíncrono do eixo de extensão; 1-robô
    * @param triggerMode Modo de acionamento do rastreamento pontual. 0-duração do rastreamento; 1-IO
    * @param runTime Duração do rastreamento pontual do robô (s)
    * @param speed Velocidade unidade %
    * @return Código de erro
    */
    public int LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum, double delayDis, double sensitivePara, int trackMode, int triggerMode, double runTime, double speed)
    
Mover para o Início da Gravação da Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Mover para o início da gravação da solda
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl Velocidade unidade %
     * @return Código de erro
     */
    public int MoveToLaserRecordStart(int moveType, double ovl)

Mover para o Fim da Gravação da Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Mover para o fim da gravação da solda
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl Velocidade unidade %
     * @return Código de erro
     */
    public int MoveToLaserRecordEnd(int moveType, double ovl)

Mover para o Ponto de Busca do Sensor a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Mover para o ponto de busca do sensor a laser
     * @param [in] moveFlag Tipo de movimento: 0-PTP; 1-LIN
     * @param [in] ovl Fator de escala de velocidade, 0-100
     * @param [in] dataFlag Seleção de dados de cache da solda: 0-executar dados planejados; 1-executar dados gravados
     * @param [in] plateType Tipo de placa: 0-placa ondulada; 1-placa corrugada; 2-placa de cerca; 3-barril de óleo; 4-aço de casco ondulado
     * @param [in] trackOffectType Tipo de deslocamento do sensor a laser: 0-sem deslocamento; 1-deslocamento no sistema de coordenadas base; 2-deslocamento no sistema de coordenadas da ferramenta; 3-deslocamento com base nos dados brutos do sensor a laser
     * @param [in] offset Valor de deslocamento
     * @return Código de erro
     */
    public int MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset)
    
Obter Informações de Coordenadas do Ponto de Busca do Sensor a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obter informações de coordenadas do ponto de busca do sensor a laser
     * @param [in] trackOffectType Tipo de deslocamento do sensor a laser: 0-sem deslocamento; 1-deslocamento no sistema de coordenadas base; 2-deslocamento no sistema de coordenadas da ferramenta; 3-deslocamento com base nos dados brutos do sensor a laser
     * @param [in] offset Valor de deslocamento
     * @param [out] jPos Posição articular [°]
     * @param [out] descPos Posição cartesiana [mm]
     * @param [out] tool Sistema de coordenadas da ferramenta
     * @param [out] user Sistema de coordenadas da peça
     * @param [out] exaxis Posição do eixo de extensão [mm]
     * @return Código de erro
     */
    public int GetLaserSeamPos(int trackOffectType, DescPose offset, JointPos jPos, DescPose descPos, int[] tool, int[] user, ExaxisPos exaxis)

Exemplo de Código para Configuração e Depuração de Parâmetros do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLaserConfig(Robot robot)
    {
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);

        robot.LaserTrackingSensorSamplePeriod(20);

        robot.LoadPosSensorDriver(101);
        robot.LaserTrackingLaserOnOff(0,0);

        robot.Sleep(3000);

        robot.LaserTrackingLaserOnOff(1, 0);

        robot.CloseRPC();
    }

Exemplo de Código para Digitalização e Reprodução de Trajetória a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLaserRecordAndReplay(Robot robot)
    {
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);

        for (int i=0;i<10;++i){
            JointPos startjointPos=new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose=new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
            DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserSensorRecord1(2, 10);

            JointPos endjointPos=new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose=new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 50, 100, 100, -1,0, exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserSensorRecord1(0, 10);

            robot.MoveToLaserRecordStart(1, 30);

            robot.LaserSensorReplay(10, 100);

            robot.MoveLTR();

            robot.LaserSensorRecord1(0, 10);
        }

        robot.CloseRPC();
    }

Exemplo de Código para Busca de Posição e Rastreamento em Tempo Real a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLasertrack(Robot robot)
    {
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        for(int i=0;i<10;++i){
            JointPos startjointPos=new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose=new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
            DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
            DescTran directionPoint=new DescTran();
            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3);
            robot.LaserTrackingSearchStop();

            //robot.GetRobotTeachingPoint(name, data);
            robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);
            //printf("%f, %f, %f,%f, %f, %f,%f, %f, %f,%f, %f, %f\n", data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]);

            robot.LaserTrackingTrackOnOff(1, 3);
            //robot.LaserTrackingTrackOn(3);
            JointPos endjointPos=new JointPos(68.809,-87.100,121.120,-127.233,-95.038,-109.555);
            DescPose enddescPose=new DescPose(-103.555,-464.234,13.076,174.179,-1.344,-91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserTrackingTrackOnOff(0, 3);
            System.out.println("Execução atual: "+(i+1));
        }
        robot.CloseRPC();
    }

Exemplo de Código para Rastreamento a Laser Síncrono com Eixo de Extensão e Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLasertrackandExitAxis(Robot robot)
    {
        ExaxisPos startexaxisPos =new ExaxisPos( 0,0,0,0 );
        ExaxisPos seamexaxisPos = new ExaxisPos(-10,0,0,0 );
        ExaxisPos endexaxisPos = new ExaxisPos(-30, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0 );
        JointPos seamjointPos=new JointPos(0, 0, 0, 0, 0, 0);
        DescPose seamdescPose=new DescPose(0, 0, 0, 0, 0, 0);

        for(int i =0;i<10;++i) {
            //Mover para o ponto inicial da busca de posição
            JointPos startjointPos = new JointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose = new DescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);

            System.out.println("11111");
            //Iniciar busca de posição ao longo da direção -y
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            System.out.println("2222");
            int[] tool = new int[1];
            int[] user = new int[1];
            robot.GetLaserSeamPos(0, offdese, seamjointPos, seamdescPose, tool, user, startexaxisPos);
            System.out.println(seamjointPos.J1 + ", " + seamjointPos.J2 + ", " +
                    seamjointPos.J3 + ", " + seamjointPos.J4 + ", " +
                    seamjointPos.J5 + ", " + seamjointPos.J6 + ", " +
                    seamdescPose.tran.x + ", " + seamdescPose.tran.y + ", " +
                    seamdescPose.tran.z + ", " + seamdescPose.rpy.rx + ", " +
                    seamdescPose.rpy.ry + ", " + seamdescPose.rpy.rz);
            //Se a busca de posição for bem-sucedida
            if (ret == 0) {
                //Robô e eixo de extensão se movem sincronizadamente para o ponto de busca
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);

                //Iniciar rastreamento a laser ao longo do ponto de busca e movimento síncrono com o eixo de extensão
                System.out.println("3333");
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos = new JointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose = new DescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);
                ;
                //Parar rastreamento
                robot.LaserTrackingTrackOnOff(0, 2);
                System.out.println("44444");
            }
            System.out.println("Número de execuções: "+i);
        }
        robot.CloseRPC();
    }

Interface SDK para Ativar/Desativar Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa/desativa a função de passagem direta na extremidade
    * @param  enable, 0-desativar, 1-ativar
    * @return Código de erro
    */
    public int SetAxleGenComEnable(int mode)

Interface SDK para Transmissão e Recepção de Dados Aperiódicos na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Envia dados aperiódicos na extremidade e aguarda resposta
    * @param lenSnd Comprimento do envio
    * @param sndBuff Dados a serem enviados
    * @param lenRcv Comprimento da recepção selecionada
    * @param [out] rcvData Dados de resposta
    * @return Código de erro
    */
    public int SndRcvAxleGenComCmdData(int lenSnd, int[] sndBuff, int lenRcv, int[] rcvData)
    
Exemplo de Código para Comunicação de Dados Aperiódicos do Cabeçote de Moxabustão Beiyikang Baseado na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testAxleGenCom(Robot robot) {
    int[] led_on = {0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79};
    int[] led_off = {0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78};
    int[] version = {0xAB, 0xBA, 0x11, 0x00, 0x76};
    int[] state = {0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B};

    int[] rcvdata = new int[16];
    int ret = 0;
    int cnt = 1;

    JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
    DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

    JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
    DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

    ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
    DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

    // Ativar função de passagem direta na extremidade
    robot.SetAxleGenComEnable(1);
    robot.SetAxleLuaEnable(1);

    while (cnt <= 10000) {
        // Ler número da versão
        ret = robot.SndRcvAxleGenComCmdData(5, version, 10, rcvdata);
        if (ret == 0) {
            System.out.printf(" hard version : %d,hard code:%d, soft version:%d %d, soft code:%d \n",
                    rcvdata[4], rcvdata[5], rcvdata[6], rcvdata[7], rcvdata[8]);
        } else {
            System.out.println("Falha no SndRcvAxleGenComCmdData version: " + ret);
            break;
        }
        robot.Sleep(1000);

        // Ler estado de presença do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, state, 6, rcvdata);
        if (ret == 0) {
            System.out.printf(" state : %d \n", rcvdata[4]);
        }
        robot.Sleep(1000);

        // Ativar laser do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, rcvdata);
        if (ret == 0) {
            System.out.printf("led on rcv data is: %d, %d, %d, %d, %d, %d\n",
                    rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        }
        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100.0, 100.0, 100.0, exaxisPos, -1.0, 0, offdese);
        robot.Sleep(4000);

        // Desativar laser do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, rcvdata);
        if (ret == 0) {
            System.out.printf("led off rcv data is: %d, %d, %d, %d, %d, %d \n",
                    rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        }
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100.0, 100.0, 100.0, exaxisPos, -1.0, 0, offdese);
        robot.Sleep(1000);

        System.out.println("***********************complete No. " + cnt + " SDK test*****************************");
        cnt++;
    }
    }  
    
Download do Arquivo Lua de Protocolo Aberto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Download do arquivo Lua de protocolo aberto
    * @param fileName Nome do arquivo de protocolo aberto "CtrlDev_XXX.lua"
    * @param savePath Caminho para salvar o arquivo de protocolo aberto
    * @return Código de erro
    */
    public int OpenLuaDownload(string fileName, string savePath)

Excluir Arquivo Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Excluir arquivo Lua de protocolo aberto
    * @param [in] fileName Nome do arquivo lua de protocolo aberto a ser excluído "CtrlDev_XXX.lua"
    * @return Código de erro
    */
    public int OpenLuaDelete(string fileName)
        
Excluir Todos os Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Excluir todos os arquivos Lua de protocolo aberto
    * @return Código de erro
    */
    public int AllOpenLuaDelete()

Exemplo de Código para Upload, Download e Exclusão de Protocolo Aberto de Periférico do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    public static int TestCtrlOpenLuaOperate(Robot robot) {
        int rtn;
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        System.out.println("OpenLuaUpload rtn is " + rtn);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        System.out.println("OpenLuaUpload rtn is " + rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        System.out.println("OpenLuaDownload rtn is " + rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        System.out.println("OpenLuaDownload rtn is " + rtn);

        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        System.out.println("SetCtrlOpenLUAName rtn is " + rtn);
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        System.out.println("SetCtrlOpenLUAName rtn is " + rtn);

        String[] names = new String[4];
        rtn = robot.GetCtrlOpenLUAName(names);
        System.out.println("GetCtrlOpenLUAName rtn is " + rtn + ", names: " +
                names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3]);

        rtn = robot.LoadCtrlOpenLUA(1);
        System.out.println("LoadCtrlOpenLUA rtn is " + rtn);
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        System.out.println("UnloadCtrlOpenLUA rtn is " + rtn);

        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        System.out.println("OpenLuaDelete rtn is " + rtn);
        rtn = robot.AllOpenLuaDelete();
        System.out.println("AllOpenLuaDelete rtn is " + rtn);

        robot.Sleep(1000);
        return 0;
    }

Controlar o Movimento da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Controlar o movimento da mão destra
    * @param idstart Número da estação escrava inicial
    * @param slaveNum Número de escravos
    * @param pos Array de posições, comprimento 16, intervalo (-360~360)
    * @param speed Array de percentuais de velocidade, comprimento 16, intervalo [0~100]
    * @param force Array de percentuais de torque, comprimento 16, intervalo [0~100]
    * @param max_time Tempo máximo de espera, intervalo [0~30000], unidade ms
    * @return Código de erro
    */
    public int SetDexterousHandsMove(int idstart, int slaveNum, double[] pos, int[] speed, int[] force, int max_time) 
        
Controlar o Reset e Ativação da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Controlar o reset e ativação da mão destra
    * @param id Número da estação escrava
    * @param act 0-reset 1-ativação
    * @return Código de erro
    */
    public int SetDexterousHandsAct(int id, int act)
            
Limpar Erro da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Limpar erro da mão destra
    * @return Código de erro
    */
    public int ClearDexterousHandsError()
                
Definir as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define as funções de controle de ação da mão destra habilitadas
    * @param id Número da estação escrava da mão destra
    * @param func Array de funções, comprimento 32, Bit0-acionamento de aperto, Bit1-inicialização da garra, Bit2-definição de posição, Bit3-definição de velocidade, Bit4-definição de torque, Bit6-leitura do estado da garra, Bit7-leitura do estado de inicialização, Bit8-leitura do código de falha, Bit9-leitura da posição, Bit10-leitura da velocidade, Bit11-leitura do torque, Bit12-definição do número de rotações, Bit13-definição da velocidade de rotação, Bit14-definição do torque de rotação, Bit15-leitura do estado da garra rotativa, Bit16-leitura do estado de inicialização da rotação, Bit17-leitura do número de rotações, Bit18-leitura da velocidade de rotação, Bit19-leitura do torque de rotação, Bit20-definição de movimento síncrono multi-eixo, Bit21-comando de limpeza de falhas, Bit22-estado de operação de eixo único, Bit23-estado de operação de todos os eixos
    * @return Código de erro
    */
    public int SetDexterousHandsFunc(int id, int[] func)
                    
Obter as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém as funções de controle de ação da mão destra habilitadas
    * @param id Número do dispositivo da mão destra
    * @param func Array de parâmetros de saída, comprimento 32, Bit0-acionamento de aperto, Bit1-inicialização da garra, Bit2-definição de posição, Bit3-definição de velocidade, Bit4-definição de torque, Bit6-leitura do estado da garra, Bit7-leitura do estado de inicialização, Bit8-leitura do código de falha, Bit9-leitura da posição, Bit10-leitura da velocidade, Bit11-leitura do torque, Bit12-definição do número de rotações, Bit13-definição da velocidade de rotação, Bit14-definição do torque de rotação, Bit15-leitura do estado da garra rotativa, Bit16-leitura do estado de inicialização da rotação, Bit17-leitura do número de rotações, Bit18-leitura da velocidade de rotação, Bit19-leitura do torque de rotação, Bit20-definição de movimento síncrono multi-eixo, Bit21-comando de limpeza de falhas, Bit22-estado de operação de eixo único, Bit23-estado de operação de todos os eixos
    * @return Código de erro
    */
    public int GetDexterousHandsFunc(int id, int[] func)
                    
Exemplo de Código de Configuração e Movimento da Mão Destra no Efetuador Final
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    public static int TestDexterousHands(Robot robot) {
        int id = 1;
        int slaveNum = 4;
        int max_time = 8000;
        int[] speed = new int[16]; 
        int[] force = new int[16]; 

        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        for (int i = 0; i < 16; i++) {
            force[i] = (i < 4) ? 50 : 0;
        }

        final double[] pos = new double[16];

        JointPos j1 = new JointPos(-91.876, -85.920, 109.279, -86.239, -96.664, -28.563);
        JointPos j2 = new JointPos(-40.954, -85.920, 109.279, -86.239, -96.664, -28.563);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        int ret = robot.ClearDexterousHandsError();
        System.out.println("ClearDexterousHandsError -> " + ret);

        int[] setFunc = new int[32];
        setFunc[2] = 1;
        setFunc[4] = 1;
        setFunc[9] = 1;
        setFunc[10] = 1;
        setFunc[11] = 1;
        setFunc[22] = 1;

        ret = robot.SetDexterousHandsFunc(id, setFunc);

        int[] getFunc = new int[32];
        ret = robot.GetDexterousHandsFunc(id, getFunc);
        System.out.println("GetDexterousHandsFunc -> " + ret);
        if (ret == 0) {
            for (int i = 0; i < getFunc.length; i++) {
                System.out.print("  [" + i + "]=" + getFunc[i]);
                if ((i + 1) % 8 == 0) {
                    System.out.println();
                } else if (i < getFunc.length - 1) {
                    System.out.print(", ");
                }
            }
            if (getFunc.length % 8 != 0) {
                System.out.println();
            }
        }

        ret = robot.SetDexterousHandsAct(id, 1);
        if (ret != 0) {
            return ret;
        }

        setPositions(pos, 20, 20, 20, 20);
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        robot.Sleep(5000);
        
        for (int iteration = 1; iteration <= 10; iteration++) {
            robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            setPositions(pos, 10, 10, 10, 10);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            robot.Sleep(1000);

            robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            setPositions(pos, 50, 50, 50, 50);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            robot.Sleep(1000);
        }
        return 0;
    }    