Periféricos do Robô
========================

.. toctree:: 
    :maxdepth: 5

Configurar Garra
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Configura a garra
    * @param  [in] company  Fabricante da garra, a definir
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    int SetGripperConfig(int company, int device, int softvesion, int bus);

Obter Configuração da Garra
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a configuração da garra
    * @param  [in] company  Fabricante da garra, a definir
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    int GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

Ativar Garra
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Ativa a garra
    * @param  [in] index  Número da garra
    * @param  [in] act  0-reset, 1-ativar
    * @return  Código de erro
    */
    int ActGripper(int index, byte act); 

Controlar Garra
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Controla a garra
    * @param  [in] index  Número da garra
    * @param  [in] pos  Porcentagem de posição, faixa [0~100]
    * @param  [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param  [in] force  Porcentagem de torque, faixa [0~100]
    * @param  [in] max_time  Tempo máximo de espera, faixa [0~30000], unidade ms
    * @param  [in] block  0-bloqueado, 1-não bloqueado
    * @param  [in] type  Tipo de garra, 0-garra paralela; 1-garra rotativa
    * @param  [in] rotNum  Número de rotações
    * @param  [in] rotVel  Porcentagem de velocidade de rotação [0-100]
    * @param  [in] rotTorque  Porcentagem de torque de rotação [0-100]
    * @return  Código de erro
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, byte block, int type, double rotNum, int rotVel, int rotTorque);

Obter Estado de Movimento da Garra
++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o estado de movimento da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] status  0-movimento não concluído, 1-movimento concluído
    * @return  Código de erro
    */
    int GetGripperMotionDone(ref int fault, ref int status); 

Obter Estado de Ativação da Garra
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o estado de ativação da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] status  bit0~bit15 correspondem aos números das garras 0~15, bit=0 não ativado, bit=1 ativado
    * @return  Código de erro
    */
    int GetGripperActivateStatus(ref int fault, ref int status);

Obter Posição da Garra
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a posição da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] position  Porcentagem de posição, faixa 0~100%
    * @return  Código de erro
    */
    int GetGripperCurPosition(ref int fault, ref int position);

Obter Velocidade da Garra
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a velocidade da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] speed  Porcentagem de velocidade, faixa 0~100%
    * @return  Código de erro
    */
    int GetGripperCurSpeed(ref int fault, ref int speed);
     
Obter Corrente da Garra
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a corrente da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] current  Porcentagem de corrente, faixa 0~100%
    * @return  Código de erro
    */
    int GetGripperCurCurrent(ref int fault, ref int current);

Obter Tensão da Garra
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a tensão da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] voltage  Tensão, unidade 0.1V
    * @return  Código de erro
    */
    int GetGripperVoltage(ref int fault, ref int voltage);

Obter Temperatura da Garra
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a temperatura da garra
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] temp  Temperatura, unidade ℃
    * @return  Código de erro
    */
    int GetGripperTemp(ref int fault, ref int temp);

Calcular Ponto de Pré-Captura - Visão
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Calcula o ponto de pré-captura - Visão 
    * @param [in] desc_pos Pose cartesiana do ponto de captura 
    * @param [in] zlength Deslocamento no eixo Z 
    * @param [in] zangle Deslocamento de rotação em torno do eixo Z
    * @param [out] pre_pos Ponto de pré-captura
    * @return Código de erro 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, ref DescPose pre_pos);

Calcular Ponto de Retirada - Visão
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Calcula o ponto de retirada - Visão 
    * @param [in] desc_pos Pose cartesiana do ponto de retirada 
    * @param [in] zlength Deslocamento no eixo Z 
    * @param [in] zangle Deslocamento de rotação em torno do eixo Z
    * @param [out] post_pos Ponto de retirada
    * @return Código de erro 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, ref DescPose post_pos);

Exemplo de Código para Operações com a Garra do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button36_Click(object sender, EventArgs e)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status=0;
        int fault=0;
        int active_status = 0;
        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        robot.SetGripperConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.GetGripperConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine("gripper config:{0},{1},{2},{3}\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        Thread.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        Thread.Sleep(1000);

        robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0);
        Thread.Sleep(1000);
        robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0);

        robot.GetGripperMotionDone(ref fault, ref status);
        Console.WriteLine("motion status:{0},{1}\n", fault, status);

        robot.GetGripperActivateStatus(ref fault, ref active_status);
        Console.WriteLine("gripper active fault is: {0}, status is: {1}\n", fault, active_status);

        robot.GetGripperCurPosition(ref fault, ref current_pos);
        Console.WriteLine("fault is:{0}, current position is: {1}\n", fault, current_pos);

        robot.GetGripperCurCurrent(ref fault, ref current);
        Console.WriteLine("fault is:{0}, current current is: {1}\n", fault, current);

        robot.GetGripperVoltage(ref fault, ref voltage);
        Console.WriteLine("fault is:{0}, current voltage is: {1} \n", fault, voltage);

        robot.GetGripperTemp(ref fault, ref temp);
        Console.WriteLine("fault is:{0}, current temperature is: {1}\n", fault, temp);

        robot.GetGripperCurSpeed(ref fault, ref speed);
        Console.WriteLine("fault is:{0}, current speed is: {1}\n", fault, speed);

        int retval = 0;
        DescPose prepick_pose = new DescPose();
        DescPose postpick_pose = new DescPose();

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        retval = robot.ComputePrePick(p1Desc, 10, 0, ref prepick_pose);
        Console.WriteLine("ComputePrePick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z,
            prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);

        retval = robot.ComputePostPick( p2Desc, -10, 0, ref postpick_pose);
        Console.WriteLine("ComputePostPick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z,
            postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);

    }

Obter Número de Rotações da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o número de rotações da garra rotativa
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] num  Número de rotações
    * @return  Código de erro
    */
    int GetGripperRotNum(ref UInt16 fault, ref double num);

Obter Porcentagem de Velocidade de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a porcentagem de velocidade de rotação da garra rotativa
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] speed  Porcentagem de velocidade de rotação
    * @return  Código de erro
    */
    int GetGripperRotSpeed(ref UInt16 fault, ref int speed);

Obter Porcentagem de Torque de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a porcentagem de torque de rotação da garra rotativa
    * @param  [out] fault  0-sem erro, 1-com erro
    * @param  [out] torque  Porcentagem de torque de rotação
    * @return  Código de erro
    */
    int GetGripperRotTorque(ref UInt16 fault, ref int torque);

Exemplo de Código para Obter Estado da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    int MoveRotGripper(int pos, double rotPos)
    {
        robot.ResetAllError();
        robot.ActGripper(1, 1);
        Thread.Sleep(1000);
        int rtn = robot.MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
        Console.WriteLine($"move gripper rtn is {rtn}" );
        UInt16 fault = 0;
        double rotNum = 0.0;
        int rotSpeed = 0;
        int rotTorque = 0;
        robot.GetGripperRotNum(ref fault, ref rotNum);
        robot.GetGripperRotSpeed(ref fault, ref rotSpeed);
        robot.GetGripperRotTorque(ref fault, ref rotTorque);
        Console.WriteLine($"gripper rot num :{ rotNum}, gripper rotSpeed :{rotSpeed}, gripper rotTorque : { rotTorque}");
        return 0;
    }

Iniciar/Parar Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Inicia/para a esteira transportadora 
    * @param [in] status Estado, 1-iniciar, 0-parar
    * @return Código de erro 
    */ 
    int ConveyorStartEnd(byte status); 

Registrar Ponto de Detecção IO
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Registra o ponto de detecção IO 
    * @return Código de erro 
    */ 
    int ConveyorPointIORecord(); 

Registrar Ponto A
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Registra o ponto A 
    * @return Código de erro 
    */ 
    int ConveyorPointARecord();

Registrar Ponto de Referência
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Registra o ponto de referência 
    * @return Código de erro 
    */ 
    int ConveyorRefPointRecord(); 

Registrar Ponto B
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Registra o ponto B 
    * @return Código de erro 
    */ 
    int ConveyorPointBRecord();

Detecção IO de Peça na Esteira
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Detecção IO de peça na esteira 
    * @param [in] max_t Tempo máximo de detecção, unidade ms
    * @return Código de erro 
    */ 
    int ConveyorIODetect(int max_t);

Obter Posição Atual do Objeto
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém a posição atual do objeto 
    * @param [in] mode 1-captura com rastreamento, 2-movimento com rastreamento, 3-rastreamento TPD
    * @return Código de erro 
    */ 
    int ConveyorGetTrackData(int mode);

Iniciar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Inicia o rastreamento da esteira 
    * @param [in] status Estado, 1-iniciar, 0-parar
    * @return Código de erro 
    */
    int ConveyorTrackStart(byte status);

Parar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Para o rastreamento da esteira 
    * @return Código de erro 
    */
    int ConveyorTrackEnd();

Configurar Parâmetros da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Configura os parâmetros da esteira
    * @param [in] para[0] Canal do encoder 1~2
    * @param [in] para[1] Número de pulsos do encoder por rotação
    * @param [in] para[2] Distância percorrida pela esteira por rotação do encoder
    * @param [in] para[3] Número do sistema de coordenadas da peça (para movimento de rastreamento, escolha o número do sistema de coordenadas; para captura com rastreamento e rastreamento TPD, defina como 0)
    * @param [in] para[4] Se usa visão 0-não usa 1-usa
    * @param [in] para[5] Relação de velocidade (para a opção de captura com rastreamento da esteira [1-100]; para outras opções, padrão 1)
    * @param [in] followType Tipo de movimento de rastreamento, 0-movimento de rastreamento; 1-movimento de verificação
    * @param [in] startDis Necessário para captura com verificação, distância inicial de rastreamento, -1: cálculo automático (a verificação começa automaticamente quando a peça chega abaixo do robô), unidade mm, valor padrão 0
    * @param [in] endDis Necessário para captura com verificação, distância final de rastreamento, unidade mm, valor padrão 100
    * @return Código de erro
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis=0, int endDis=100);

Definir Compensação do Ponto de Captura da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define a compensação do ponto de captura da esteira 
    * @param [in] cmp Compensação de posição double[3]{x, y, z}
    * @return Código de erro 
    */
    int ConveyorCatchPointComp(double[] cmp);

Movimento Linear com Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int ConveyorTrackMoveL(string name, int tool, int wobj, float vel, float acc, float ovl, float blendR);

Detecção de Entrada de Comunicação da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Detecção de entrada de comunicação da esteira
    * @param [in] timeout Tempo limite de espera ms
    * @return Código de erro
    */
    public int ConveyorComDetect(int timeout)

Acionamento da Detecção de Entrada de Comunicação da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Acionamento da detecção de entrada de comunicação da esteira
    * @return Código de erro
    */
    int ConveyorComDetectTrigger();

Exemplo de Programa de Acionamento da Detecção de Entrada de Comunicação da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button3_Click(object sender, EventArgs e)
    {

        // Desabilita o botão para evitar cliques repetidos
        button3.Enabled = false;

        // Executa a operação demorada em uma thread em segundo plano
        Thread conveyorThread = new Thread(ConveyorTest);
        conveyorThread.IsBackground = true;
        conveyorThread.Start();
    }

    private void button4_Click(object sender, EventArgs e)
    {
        // Obtém a entrada do usuário
        string input = texBox.Text;
        Console.WriteLine($"please input a number to trigger:{input}");
    
        int rtn = robot.ConveyorComDetectTrigger();
        Console.WriteLine($"ConveyorComDetectTrigger 返回值: {rtn}");
        
    }

    private void ConveyorTest()
    {
        // Usa Invoke para atualizar os controles na thread da UI
        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("开始传送带测试...");
        });

        int retval = 0;
        int index = 1;
        int max_time = 30000;
        bool block = false;
        retval = 0;

        /* 传送带抓取流程 */
        DescPose startdescPose = new DescPose(139.176f, 4.717f, 9.088f, -179.999f, -0.004f, -179.990f);
        JointPos startjointPos = new JointPos(-34.129f, -88.062f, 97.839f, -99.780f, -90.003f, -34.140f);

        DescPose homePose = new DescPose(139.177f, 4.717f, 69.084f, -180.000f, -0.004f, -179.989f);
        JointPos homejointPos = new JointPos(-34.129f, -88.618f, 84.039f, -85.423f, -90.003f, -34.140f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        // Move para posição segura
        retval = robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        Console.WriteLine($"MoveL 到安全位置返回值: {retval}");

        // Detecção da esteira
        retval = robot.ConveryComDetect(1000 * 10);
        Console.WriteLine($"ConveyorComDetect 返回值: {retval}");

        // Obtém dados de rastreamento
        retval = robot.ConveyorGetTrackData(2);
        Console.WriteLine($"ConveyorGetTrackData 返回值: {retval}");

        // Inicia rastreamento
        retval = robot.ConveyorTrackStart(2);
        Console.WriteLine($"ConveyorTrackStart 返回值: {retval}");

        // Move para posição inicial
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        // Encerra rastreamento
        retval = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd 返回值: {retval}");

        // Retorna à posição segura
        robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("传送带测试完成!");
            button3.Enabled = true;
        });
    }

Exemplo de Programa de Operação da Esteira do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnConvert_Click(object sender, EventArgs e)
    {
        // Conveyor belt tracking
        DescPose pos1 = new DescPose(-354.549, 63.914, 270.176, -179.679, -0.134, 2.468);
        DescPose pos2 = new DescPose(-351.203, -213.393, 351.054, -179.932, -0.508, 2.472);

        double[] cmp = { 0.0, 0.0, 0.0 };
        int rtn = robot.ConveyorCatchPointComp(cmp); // Set conveyor pick-up point compensation
        if (rtn != 0)
        {
            return;
        }
        Console.WriteLine("ConveyorCatchPointComp: rtn  " + rtn);

        rtn = robot.MoveCart(pos1, 1, 0, (float)30.0, (float)180.0, (float)100.0, (float)-1.0, -1);
        Console.WriteLine("MoveCart: rtn  " + rtn);

        rtn = robot.ConveyorIODetect(10000); // Conveyor workpiece I/O detection
        Console.WriteLine("ConveyorIODetect: rtn   " + rtn);

        robot.ConveyorGetTrackData(1); // Configure conveyor tracking for picking
        rtn = robot.ConveyorTrackStart(1); // Start tracking
        Console.WriteLine("ConveyorTrackStart: rtn  " + rtn);

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, (float)100.0, (float)0.0, (float)100.0, (float)-1.0, 0, 0);
        Console.WriteLine("ConveyorTrackMoveL: rtn  " + rtn);

        rtn = robot.MoveGripper(2, 30, 60, 30, 30000, 0, 0, 0, 50, 50);
        Console.WriteLine("ConveyorTrackMoveL: rtn  " + rtn);
            

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, (float)100.0, (float)0.0, (float)100.0, (float)-1.0, 0, 0);
        Console.WriteLine("ConveyorTrackMoveL: rtn   " + rtn);

        rtn = robot.ConveyorTrackEnd(); // Stop conveyor tracking
        Console.WriteLine("ConveyorTrackEnd: rtn  " + rtn);

        rtn = robot.MoveCart(pos2, 1, 0, (float)30.0, (float)180.0, (float)100.0, (float)-1.0, -1);
        Console.WriteLine("MoveCart: rtn  " + rtn);

        rtn = robot.MoveGripper(2, 100, 60, 30, 30000, 0,0,0,50,50);
        Console.WriteLine("MoveGripper: rtn  " + rtn);

    }

Configurar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Configura o sensor de extremidade
    * @param  [in] idCompany Fabricante, 18-JUNKONG；25-HUIDE
    * @param  [in] idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
    * @param  [in] idSoftware Versão do software, 0-J1.0/HuiDe1.0 (temporariamente não disponível)
    * @param  [in] idBus Posição de montagem, 1-porta 1 da extremidade; 2-porta 2 da extremidade...8-porta 8 da extremidade (temporariamente não disponível)
    * @return  Código de erro
    */
    int AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

Obter Configuração do Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a configuração do sensor de extremidade
    * @param  [out] idCompany Fabricante, 18-JUNKONG；25-HUIDE
    * @param  [out] idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
    * @return  Código de erro
    */
    int AxleSensorConfigGet(ref int idCompany, ref int idDevice);

Ativar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Ativa o sensor de extremidade
    * @param  [in] actFlag 0-reset; 1-ativar
    * @return  Código de erro
    */
    int AxleSensorActivate(int actFlag);

Escrita no Registrador do Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Escrita no registrador do sensor de extremidade
    * @param  [in] devAddr  Endereço do dispositivo 0-255
    * @param  [in] regHAddr 8 bits altos do endereço do registrador
    * @param  [in] regLAddr 8 bits baixos do endereço do registrador
    * @param  [in] regNum  Número de registradores 0-255
    * @param  [in] data1 Valor 1 a ser escrito no registrador
    * @param  [in] data2 Valor 2 a ser escrito no registrador
    * @param  [in] isNoBlock 0-bloqueado; 1-não bloqueado
    * @return  Código de erro
    */
     int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

Exemplo de Código do Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button2_Click_1(object sender, EventArgs e)
    {
        robot.AxleSensorConfig(18, 0, 0, 1);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(ref company, ref type);
        Console.WriteLine("company is " + company + ", type is " + type);

        int rtn = robot.AxleSensorActivate(1);
        Console.WriteLine("AxleSensorActivate rtn is " + rtn);

        Thread.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        Console.WriteLine("AxleSensorRegWrite rtn is " + rtn);   
    }

Obter Protocolo de Periféricos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém o protocolo de periféricos do robô
    * @param [out] protocol Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster
    * @return Código de erro 
    */
    int GetExDevProtocol(ref int protocol);

Definir Protocolo de Periféricos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Define o protocolo de periféricos do robô
    * @param [in] protocol Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster
    * @return Código de erro 
    */
    int SetExDevProtocol(int protocol);

Exemplo de Programa para Definir Protocolo de Periféricos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
      int protocol = 4096;
      int rtn = robot.SetExDevProtocol(protocol);
      Console.WriteLine("SetExDevProtocol rtn " + rtn);
      rtn = robot.GetExDevProtocol(ref protocol);
      Console.WriteLine("GetExDevProtocol rtn " + rtn + " protocol is: " + protocol);
    }

Obter Parâmetros de Comunicação da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os parâmetros de comunicação da extremidade
    * @param param Parâmetros de comunicação da extremidade
    * @return  Código de erro
    */
    int GetAxleCommunicationParam(ref AxleComParam getParam);

Definir Parâmetros de Comunicação da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define os parâmetros de comunicação da extremidade
    * @param param  Parâmetros de comunicação da extremidade
    * @return  Código de erro
    */
    int SetAxleCommunicationParam(AxleComParam param);

Definir Tipo de Transferência de Arquivo da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define o tipo de transferência de arquivo da extremidade
    * @param type 1-arquivo de atualização MCU; 2-arquivo LUA
    * @return  Código de erro
    */
    int SetAxleFileType(int type);

Ativar Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativa a execução LUA na extremidade
    * @param enable 0-desativar; 1-ativar
    * @return  Código de erro
    */
    int SetAxleLuaEnable(int enable);

Recuperação de Erro de Arquivo LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Recuperação de erro de arquivo LUA na extremidade
    * @param status 0-não recuperar; 1-recuperar
    * @return  Código de erro
    */
    int SetRecoverAxleLuaErr(int status);

Obter Estado de Ativação da Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado de ativação da execução LUA na extremidade
    * @param [out] status 0-desativado; 1-ativado
    * @return  Código de erro
    */
    int GetAxleLuaEnableStatus(ref int status);

Definir os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define os tipos de dispositivo de extremidade habilitados para o LUA
    * @param [in] forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    * @param [in] gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
    * @param [in] IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    * @param [in] dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
    * @return  Código de erro
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable, int dexhandEnable)

Obter os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os tipos de dispositivo de extremidade habilitados para o LUA
    * @param [out] forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    * @param [out] gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
    * @param [out] IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    * @param [out] dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
    * @return  Código de erro
    */
    public int GetAxleLuaEnableDeviceType(ref int forceSensorEnable, ref int gripperEnable, ref int IOEnable, ref int dexhandEnable)

Obter os dispositivos de extremidade atualmente configurados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os dispositivos de extremidade atualmente configurados
    * @param [out] forceSensorEnable Número do dispositivo de sensor de força habilitado, 0-desabilitado; 1-habilitado
    * @param [out] gripperEnable Número do dispositivo de garra habilitado, 0-desabilitado; 1-habilitado
    * @param [out] IODeviceEnable Número do dispositivo IO habilitado, 0-desabilitado; 1-habilitado
    * @param [out] decHandEnable Número do dispositivo de mão destra habilitado, 0-desabilitado; 1-habilitado
    * @return  Código de erro
    */
    public int GetAxleLuaEnableDevice(ref int[] forceSensorEnable, ref int[] gripperEnable, ref int[] IODeviceEnable, ref int[] decHandEnable)

Definir as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define as funções de controle de ação da garra habilitadas
    * @param [in] id Número do dispositivo da garra
    * @param [in] func func[0]-habilitação da garra; func[1]-inicialização da garra; func[2]-definição de posição; func[3]-definição de velocidade; func[4]-definição de torque; func[6]-leitura do estado da garra;
        func[7]-leitura do estado de inicialização; func[8]-leitura do código de falha; func[9]-leitura da posição; func[10]-leitura da velocidade; func[11]-leitura do torque; func[12]-definição do número de rotações para garra rotativa;
        func[13]-definição da velocidade de rotação para garra rotativa; func[14]-definição do torque de rotação para garra rotativa; func[15]-leitura do estado da garra rotativa; func[16]-leitura do estado de inicialização da garra rotativa;
        func[17]-leitura do número de rotações da garra rotativa; func[18]-leitura da velocidade da garra rotativa; func[19]-leitura do torque da garra rotativa; func[20]-definição de movimento síncrono multi-eixo; func[21]-comando de limpeza de falhas;
        func[22]-estado de operação de eixo único; func[23]-estado de operação de todos os eixos;
    * @return  Código de erro
    */
    public int SetAxleLuaGripperFunc(int id, int[] func)

Obter as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém as funções de controle de ação da garra habilitadas
    * @param [in] id Número do dispositivo da garra
    * @param [out] func func[0]-habilitação da garra; func[1]-inicialização da garra; func[2]-definição de posição; func[3]-definição de velocidade; func[4]-definição de torque; func[6]-leitura do estado da garra;
        func[7]-leitura do estado de inicialização; func[8]-leitura do código de falha; func[9]-leitura da posição; func[10]-leitura da velocidade; func[11]-leitura do torque; func[12]-definição do número de rotações para garra rotativa;
        func[13]-definição da velocidade de rotação para garra rotativa; func[14]-definição do torque de rotação para garra rotativa; func[15]-leitura do estado da garra rotativa; func[16]-leitura do estado de inicialização da garra rotativa;
        func[17]-leitura do número de rotações da garra rotativa; func[18]-leitura da velocidade da garra rotativa; func[19]-leitura do torque da garra rotativa; func[20]-definição de movimento síncrono multi-eixo; func[21]-comando de limpeza de falhas;
        func[22]-estado de operação de eixo único; func[23]-estado de operação de todos os eixos;
    * @return  Código de erro
    */
    public int GetAxleLuaGripperFunc(int id, ref int[] func)

Escrita de Arquivo no Escravo Ethercat do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Escrita de arquivo no escravo Ethercat do robô
    * @param [in] type Tipo de arquivo do escravo, 1-arquivo de atualização do escravo; 2-arquivo de configuração do escravo
    * @param [in] slaveID Número do escravo
    * @param [in] fileName Nome do arquivo a ser enviado
    * @return  Código de erro
    */
    int SlaveFileWrite(int type, int slaveID, string fileName);

Enviar Arquivo de Protocolo Aberto LUA da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Envia arquivo de protocolo aberto LUA da extremidade
    * @param filePath Caminho do arquivo lua local ".../AXLE_LUA_End_DaHuan.lua"
    * @return Código de erro 
    */
    int AxleLuaUpload(string filePath);

Entrar no Modo Boot do Escravo Ethercat do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Entrar no modo boot do escravo Ethercat do robô
    * @return  Código de erro
    */
    int SetSysServoBootMode();

Exemplo de Código para Operações com Arquivos LUA da Extremidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button41_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_JunDuo_V0.4_20260602.lua");

        AxleComParam param = new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        AxleComParam getParam = new AxleComParam();
        robot.GetAxleCommunicationParam(ref getParam);
        Console.WriteLine("GetAxleCommunicationParam param is {0} {1} {2} {3} {4} {5} {6}",
            getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify,
            getParam.timeout, getParam.timeoutTimes, getParam.period);

        robot.SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot.GetAxleLuaEnableStatus(ref luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int dexhandEnable = 0;
        robot.GetAxleLuaEnableDeviceType(ref forceEnable, ref gripperEnable, ref ioEnable, ref dexhandEnable);
        Console.WriteLine("GetAxleLuaEnableDeviceType param is {0} {1} {2}", forceEnable, gripperEnable, ioEnable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        robot.SetAxleLuaGripperFunc(1, func);

        int[] getFunc = new int[32];
        robot.GetAxleLuaGripperFunc(1, ref getFunc);
        int[] getforceEnable = new int[16];
        int[] getgripperEnable = new int[16];
        int[] getioEnable = new int[16];
        int[] dexhandEnable1 = new int[16];
        robot.GetAxleLuaEnableDevice(ref getforceEnable, ref getgripperEnable, ref getioEnable,ref dexhandEnable1);
        Console.WriteLine("\ngetforceEnable status : ");
        foreach (int i in getforceEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetgripperEnable status : ");
        foreach (int i in getgripperEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetioEnable status : ");
        foreach (int i in getioEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine();
        robot.ActGripper(1, 0);
        Thread.Sleep(3000);
        robot.ActGripper(1, 1);
        Thread.Sleep(4000);
        robot.MoveGripper(1, 50, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("gripper pos is " + pkg.gripper_position);
            Thread.Sleep(100);
        }
    } 

Obter Estado dos Botões do SmartTool
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado dos botões do SmartTool
    * @param [out] state Estado dos botões do SmartTool; (bit0:0-comunicação normal; 1-comunicação perdida; bit1-operação de desfazer; bit2-limpar programa;
        bit3-tecla A；bit4-tecla B；bit5-tecla C；bit6-tecla D；bit7-tecla E；bit8-tecla IO；bit9-manual/automático；bit10-iniciar)
    * @return Código de erro
    */
    int GetSmarttoolBtnState(ref int state);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button11_Click(object sender, EventArgs e)
    {

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        int state = 0;
        while (true)
        {
            int rtn = robot.GetSmarttoolBtnState(ref state);
            string binaryString = Convert.ToString(state, 2).PadLeft(32, '0');
            Console.WriteLine($"GetSmarttoolBtnState rtn (binary): {binaryString}");
            Thread.Sleep(100);
        }

    }

Enviar Arquivo Lua de Protocolo Aberto
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Envia arquivo Lua de protocolo aberto
    * @param  filePath Caminho do arquivo lua de protocolo aberto local
    * @return Código de erro
    */
    public int OpenLuaUpload(string filePath)

Obter Parâmetros da Placa Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém os parâmetros da placa escrava
    * @param  type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  version  Versão do protocolo
    * @param  connState  0-desconectado 1-conectado
    * @return  Código de erro
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

Escrever DO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Escrever AO da estação escrava
    * @param [in] AOIndex Número AO
    * @param [in] writeNum Número de valores a escrever
    * @param [in] status Matriz de valores a escrever (máximo 8), AO0~AO15 são do tipo inteiro, AO16~AO31 são do tipo ponto flutuante
    * @return Código de erro
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int writeNum, double[] status)

Ler DI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Aguarda entrada DI de extensão
    * @param  DIIndex Número do DI
    * @param  status 0-nível baixo；1-nível alto
    * @param  waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Aguarda entrada AI de extensão
    * @param  AIIndex Número do AI
    * @param  waitType 0-maior que；1-menor que
    * @param  value Valor do AI
    * @param  waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

Exemplo de Código para Interfaces de Instrução do Modo Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button101_Click(object sender, EventArgs e)
    {
        int rtn = 0;
    
        int type = 0, version = 0, connState = 0;
        int[] ctrl = new int[8];
        double[] ctrlAO = new double[8];
        int[] DI = new int[8];
        double[] AI = new double[8];
        if (rtn != 0)
        {
            return;
        }
        // Upload and load open protocol file
        robot.OpenLuaUpload("E://temp/CtrlDev_field.lua");
        Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        Thread.Sleep(8000);
    
        // Get protocol type, software version, and connection status with PLC
        robot.GetFieldBusConfig(ref type, ref version, ref connState);
        Console.WriteLine($"type is {type}, version is {version}, connState is {connState}");
    
        // Write DO0 = 1, DO1 = 0, DO2 = 1
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
    
        // Write AO2 = 0x1000
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, ref DI);
            Console.WriteLine($"DI0 is {DI[0]}, DI1 is {DI[1]}, DI2 is {DI[2]}, DI3 is {DI[3]}");
            robot.FieldBusSlaveReadAI(0, 3, ref AI);
            Console.WriteLine($"AI0 is {AI[0]}, AI1 is {AI[1]}, AI2 is {AI[2]}");
            Thread.Sleep(10);
        }
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        Console.WriteLine($"FieldBusSlaveWaitDI result is {ret}");

        ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00f, 100);
        Console.WriteLine($"FieldBusSlaveWaitAI result is {ret}"); 
    }

Controlar Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void TestSucker(Robot robot)
    {
    
        int[] ctrl = new int[20];
        int state=0;
        int pressValue=0;
        int error=0;
        int rtn;
    
    
        // Upload and load open protocol file
        robot.OpenLuaUpload(@"C:\SDK\CtrlDev_sucker.lua");
        Thread.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        Thread.Sleep(1000);
    
        // Control sucker in broadcast mode with maximum adsorption capacity
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);
    
        // Monitor states of sucker 1 and sucker 12 in a loop
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker1 state is {state}, pressValue is {pressValue}, error num is {error}");
            robot.GetSuckerState(12, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker12 state is {state}, pressValue is {pressValue}, error num is {error}");
            Thread.Sleep(100);
        }
        // Wait for sucker 1 to reach adsorbed state, timeout 100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        Console.WriteLine($"WaitSuckerState result is {ret}");
    
        // Unicast mode to turn off sucker 1 and 12
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
    
        robot.CloseRPC();
    }

Função de Ligar/Desligar Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Função de ligar/desligar periférico laser
     * @param [in] OnOff 0-desligar 1-ligar
     * @param [in] weldId ID da solda, padrão 0
     * @return Código de erro
     */
    public int LaserTrackingLaserOnOff(int OnOff, int weldId)
    
Função de Iniciar/Parar Rastreamento a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    
    /**
     * @brief Função de iniciar/parar rastreamento a laser
     * @param [in] OnOff 0-parar 1-iniciar
     * @param [in] coordId Número do sistema de coordenadas da ferramenta do periférico laser
     * @return Código de erro
     */
    public int LaserTrackingTrackOnOff(int OnOff, int coordId)

Busca de Posição a Laser - Direção Fixa
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Busca de posição a laser - Direção Fixa
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Busca de posição a laser - Direção Arbitrária
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
    * @brief  Fim da busca de posição a laser
    * @return Código de erro
    */
    public int LaserTrackingSearchStop()

Configuração de IP do Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Configuração de IP do laser
     * @param [in] ip Endereço IP do periférico laser
     * @param [in] port Número da porta do periférico laser
     * @return Código de erro
     */
    public int LaserTrackingSensorConfig(string ip, int port)

Configuração do Período de Amostragem do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Configuração do período de amostragem do periférico laser
     * @param [in] period Período de amostragem do periférico laser unidade ms
     * @return Código de erro
     */
    public int LaserTrackingSensorSamplePeriod(int period)

Carregar Driver do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Carregar driver do periférico laser
     * @param [in] type Tipo de protocolo do driver do periférico laser 101-Ruiniu 102-Chuangxiang 103-Quanshi 104-Tongzhou 105-Aotai
     * @return Código de erro
     */
    public int LoadPosSensorDriver(int type)

Descarregar Driver do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Descarregar driver do periférico laser
     * @return Código de erro
     */
    public int UnLoadPosSensorDriver()

Gravação da Trajetória da Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Reprodução do rastreamento a laser
     * @return Código de erro
     */
    public int MoveLTR()

Gravação e Reprodução da Trajetória da Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Gravação e reprodução da trajetória da solda a laser
    * @param [in] delayMode Modo de atraso 0-tempo de atraso 1-distância de atraso
    * @param [in] delayTime Tempo de atraso unidade ms
    * @param [in] delayDisExAxisNum Número do eixo de extensão
    * @param [in] delayDis Distância de atraso unidade mm
    * @param [in] sensitivePara Coeficiente de sensibilidade de compensação
    * @param [in] trackMode Tipo de rastreamento pontual. 0-movimento assíncrono do eixo de extensão；1-robô
    * @param [in] triggerMode Modo de acionamento do rastreamento pontual. 0-duração do rastreamento；1-IO
    * @param [in] runTime Duração do rastreamento pontual do robô (s)
    * @param [in] speed Velocidade unidade %
    * @return Código de erro
    */
    public int LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum,double delayDis, double sensitivePara, int trackMode, int triggerMode,double runTime, double speed)
    
Mover para o Início da Gravação da Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Mover para o ponto de busca do sensor a laser
     * @param [in] moveFlag Tipo de movimento: 0-PTP；1-LIN
     * @param [in] ovl Fator de escala de velocidade, 0-100
     * @param [in] dataFlag Seleção de dados de cache da solda: 0-executar dados planejados；1-executar dados gravados
     * @param [in] plateType Tipo de placa: 0-placa ondulada；1-placa corrugada；2-placa de cerca；3-barril de óleo；4-aço de casco ondulado
     * @param [in] trackOffectType Tipo de deslocamento do sensor a laser: 0-sem deslocamento；1-deslocamento no sistema de coordenadas base；2-deslocamento no sistema de coordenadas da ferramenta；3-deslocamento com base nos dados brutos do sensor a laser
     * @param [in] offset Valor de deslocamento
     * @return Código de erro
     */
    public int MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset)
    
Obter Informações de Coordenadas do Ponto de Busca do Sensor a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief Obter informações de coordenadas do ponto de busca do sensor a laser
     * @param [in] trackOffectType Tipo de deslocamento do sensor a laser: 0-sem deslocamento；1-deslocamento no sistema de coordenadas base；2-deslocamento no sistema de coordenadas da ferramenta；3-deslocamento com base nos dados brutos do sensor a laser
     * @param [in] offset Valor de deslocamento
     * @param [out] jPos Posição articular [°]
     * @param [out] descPos Posição cartesiana [mm]
     * @param [out] tool Sistema de coordenadas da ferramenta
     * @param [out] user Sistema de coordenadas da peça
     * @param [out] exaxis Posição do eixo de extensão [mm]
     * @return Código de erro
     */
    public int GetLaserSeamPos(int trackOffectType, DescPose offset, ref JointPos jPos, ref DescPose descPos, ref int tool, ref int user, ref ExaxisPos exaxis)

Exemplo de Código para Configuração e Depuração de Parâmetros do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserConfig()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);
        robot.LaserTrackingLaserOnOff(0, 0);
        System.Threading.Thread.Sleep(3000);
        robot.LaserTrackingLaserOnOff(1, 0);
    }

Exemplo de Código para Digitalização e Reprodução de Trajetória a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserRecordAndReplay()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i=0;i<10;++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserSensorRecord1(2, 10);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);

            robot.LaserSensorRecord1(0, 10);
            robot.MoveToLaserRecordStart(1, 30);
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            robot.LaserSensorRecord1(0, 10);
            Console.WriteLine($"Number of completions : {i+1} ");
        }
                
    }

Exemplo de Código para Busca de Posição e Rastreamento em Tempo Real a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public static void testLasertrack()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i = 0; i < 10; ++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
            DescTran directionPoint = new DescTran();

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3);
            robot.LaserTrackingSearchStop();
            robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);

            robot.LaserTrackingTrackOnOff(1, 3);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingTrackOnOff(0, 3);
            Console.WriteLine($"Number of completions : {i + 1} ");
        }
    }

Exemplo de Código para Rastreamento a Laser Síncrono com Eixo de Extensão e Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public void TestLaserTrackAndExitAxis()
    {   
        ExaxisPos startexaxisPos = new ExaxisPos(0, 0, 0, 0);
        ExaxisPos seamexaxisPos = new ExaxisPos(-10, 0, 0, 0);
        ExaxisPos endexaxisPos = new ExaxisPos(-30, 0, 0, 0);      
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);     
        JointPos startjointPos = new JointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
        DescPose startdescPose = new DescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
        for (int i=0;i<10;++i)
        {
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);
            Console.WriteLine("11111");
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            Console.WriteLine("2222");
            int tool = 0;
            int user = 0;
            JointPos seamjointPos = new JointPos();
            DescPose seamdescPose = new DescPose();
            robot.GetLaserSeamPos(0, offdese, ref seamjointPos, ref seamdescPose, ref tool, ref user, ref startexaxisPos);
            Console.WriteLine($"{seamjointPos.jPos[0]}, {seamjointPos.jPos[1]}, {seamjointPos.jPos[2]}, " +
                            $"{seamjointPos.jPos[3]}, {seamjointPos.jPos[4]}, {seamjointPos.jPos[5]}, " +
                            $"{seamdescPose.tran.x}, {seamdescPose.tran.y}, {seamdescPose.tran.z}, " +
                            $"{seamdescPose.rpy.rx}, {seamdescPose.rpy.ry}, {seamdescPose.rpy.rz}");
            if (ret == 0)
            {
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);
                Console.WriteLine("3333");
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos = new JointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose = new DescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            Console.WriteLine($"Number of completions : {i + 1} ");
        }     
    }

Ativar/Desativar Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Ativa/desativa a função de passagem direta na extremidade
    * @param [in] enable, 0-desativar, 1-ativar
    * @return Código de erro
    */
    public int SetAxleGenComEnable(int mode)

Transmissão e Recepção de Dados Aperiódicos na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Envia dados aperiódicos na extremidade e aguarda resposta
    * @param [in] len_snd, comprimento do envio
    * @param [in] sndBuff[], dados a serem enviados
    * @param [in] len_rcv, comprimento da recepção selecionada
    * @param [out] rcvBuff[], dados de resposta
    * @return Código de erro
    */
    public int SndRcvAxleGenComCmdData(int len_snd, int[] sndBuff, int len_rcv, ref int[] rcvdata)

Exemplo de Código para Comunicação de Dados Aperiódicos do Cabeçote de Moxabustão Beiyikang Baseado na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

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

        while(cnt<=10)
        { 
            // Ler número da versão
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            // Ler estado de presença do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            // Ativar laser do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            // Desativar laser do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }

Download do Arquivo Lua de Protocolo Aberto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Download do arquivo Lua de protocolo aberto
    * @param [in] fileName Nome do arquivo de protocolo aberto "CtrlDev_XXX.lua"
    * @param [in] savePath Caminho para salvar o arquivo de protocolo aberto
    * @return Código de erro
    */
    public int OpenLuaDownload(string fileName, string savePath)
    
Excluir Arquivo Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Excluir arquivo Lua de protocolo aberto
    * @param [in] fileName Nome do arquivo lua de protocolo aberto a ser excluído "CtrlDev_XXX.lua"
    * @return Código de erro
    */
    public int OpenLuaDelete(string fileName)
        
Excluir Todos os Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Excluir todos os arquivos Lua de protocolo aberto
    * @return Código de erro
    */
    public int AllOpenLuaDelete()

Exemplo de Código SDK para Operações com Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public int TestCtrlOpenLuaOperate()
    {
        int rtn;

        // Upload do arquivo Lua para o robô
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");

        // Download do arquivo Lua do robô
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");

        // Definir nome do Lua de protocolo aberto de controle
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");

        // Obter nome do Lua de protocolo aberto de controle
        string[] name = new string[4];
        rtn = robot.GetCtrlOpenLUAName(ref name);
        Console.WriteLine($"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}");

        // Carregar e descarregar protocolo aberto Lua
        rtn = robot.LoadCtrlOpenLUA(1);
        Console.WriteLine($"LoadCtrlOpenLUA rtn is {rtn}");
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        Console.WriteLine($"UnloadCtrlOpenLUA rtn is {rtn}");

        // Excluir arquivo Lua específico e todos os arquivos Lua
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaDelete rtn is {rtn}");
        rtn = robot.AllOpenLuaDelete();
        Console.WriteLine($"AllOpenLuaDelete rtn is {rtn}");

        return 0;
    }

Controlar o movimento da mão destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:    

    /**
    * @brief  Controlar o movimento da mão destra
    * @param  [in] idstart  Número da estação escrava inicial
    * @param  [in] slaveNum  Número de escravos
    * @param  [in] pos[16]  Posição (-360~360) 
    * @param  [in] speed[16]  Percentual de velocidade, intervalo [0~100]
    * @param  [in] force[16]  Percentual de torque, intervalo [0~100]
    * @param  [in] max_time  Tempo máximo de espera, intervalo [0~30000], unidade ms
    * @return  Código de erro
    */
    public int SetDexterousHandsMove(int idstart, int slaveNum, double[] pos, int[] speed, int[] force, int max_time)
    
Controlar o reset e ativação da mão destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief  Controlar o reset e ativação da mão destra
    * @param  [in] id  Número da estação escrava
    * @param  [in] act  0-reset 1-ativação
    * @return  Código de erro
    */
    public int SetDexterousHandsAct(int id, int act)

Limpar erro da mão destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief  Limpar erro da mão destra
    * @return  Código de erro
    */
    public int ClearDexterousHandsError()
    
Definir as funções de controle de ação da mão destra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief Define as funções de controle de ação da mão destra habilitadas
    * @param [in] id Número da estação escrava da mão destra
    * @param [in] func 0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque, 6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade, 11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação, 15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação, 19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único, 23-estado de operação de todos os eixos
    * @return  Código de erro
    */
    public int SetDexterousHandsFunc(int id, int[] func)
    
Obter as funções de controle de ação da mão destra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief Obtém as funções de controle de ação da mão destra habilitadas
    * @param [in] id Número do dispositivo da mão destra
    * @param [out] func 0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque, 6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade, 11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação, 15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação, 19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único, 23-estado de operação de todos os eixos
    * @return  Código de erro
    */
    public int GetDexterousHandsFunc(int id, ref int[] func)

Exemplo de código de configuração e movimento da mão destra no efetuador final
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    private void button105_Click(object sender, EventArgs e)
    {
        int id = 1;               // Número da estação escrava
        int slaveNum = 4;         // Controla 4 dedos
        int max_time = 8000;      // Tempo máximo de espera 8 segundos
        int[] speed = new int[16]; // Array de velocidade, todos 0 significa usar velocidade padrão
        int[] force = new int[16]; // Array de torque

        // Inicializar array de torque: primeiros 4 dedos definidos como 50%, o resto 0 (valores enviados via comando Move)
        for (int i = 0; i < 16; i++)
            force[i] = (i < 4) ? 50 : 0;

        // Função auxiliar: definir array de posição (apenas os primeiros 4 dedos são efetivos)
        double[] pos = new double[16];
        void SetPositions(double v1, double v2, double v3, double v4)
        {
            for (int i = 0; i < 16; i++)
                pos[i] = 0;
            pos[0] = v1;
            pos[1] = v2;
            pos[2] = v3;
            pos[3] = v4;
        }

        JointPos j1 = new JointPos(-91.876, -85.920, 109.279, -86.239, -96.664, -28.563);
        JointPos j2 = new JointPos(-40.954, -85.920, 109.279, -86.239, -96.664, -28.563);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        Console.WriteLine("===== Teste de Função Completa da Mão Destra Iniciado =====");

        // 1. Limpar erro
        int ret = robot.ClearDexterousHandsError();
        Console.WriteLine($"ClearDexterousHandsError -> {ret}");

        // ========== 2. Definir chaves de função ==========
        int[] setFunc = new int[32];
        setFunc[2] = 1;   // Habilitar função de definição de posição
        setFunc[4] = 1;   // Habilitar função de definição de torque
        setFunc[9] = 1;   // Ler posição
        setFunc[10] = 1;  // Ler torque
        setFunc[11] = 1;  // Ler status
        setFunc[22] = 1;  // Status de movimento de eixo único

        ret = robot.SetDexterousHandsFunc(id, setFunc);
        Console.WriteLine($"SetDexterousHandsFunc(init + funções de posição/torque habilitadas) -> {ret}");

        // ========== 3. Ler status da função (verificar se as configurações foram aplicadas) ==========
        int[] getFunc = new int[32];  // GetDexterousHandsFunc retorna 32 inteiros
        ret = robot.GetDexterousHandsFunc(id, ref getFunc);
        Console.WriteLine($"GetDexterousHandsFunc -> {ret}");
        if (ret == 0)
        {
            // Imprimir todos os 32 valores
            Console.WriteLine("Todos os 32 valores retornados por GetDexterousHandsFunc:");
            for (int i = 0; i < getFunc.Length; i++)
            {
                Console.Write($"  [{i}]={getFunc[i]}");
                if ((i + 1) % 8 == 0)
                    Console.WriteLine();          // Nova linha a cada 8 itens
                else if (i < getFunc.Length - 1)
                    Console.Write(", ");
            }
            if (getFunc.Length % 8 != 0)
                Console.WriteLine();              // Adicionar nova linha se a última linha tiver menos de 8 itens
        }

        // ========== 4. Ativar mão destra ==========
        ret = robot.SetDexterousHandsAct(id, 1);
        Console.WriteLine($"SetDexterousHandsAct(ativar) -> {ret}");
        if (ret != 0)
        {
            Console.WriteLine("Falha na ativação, teste abortado");
            return;
        }

        // ========== 5. Movimento inicial para 20° (enviar valores de posição e torque via comando Move) ==========
        SetPositions(20, 20, 20, 20);
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        Console.WriteLine($"Movimento inicial para 20° -> {ret}");
        robot.Sleep(5000);

        // ========== 6. Movimento alternado 10 vezes (10° ↔ 50°) ==========
        Console.WriteLine("Iniciando 10 movimentos alternados...");
        for (int iteration = 1; iteration <= 10; iteration++)
        {
            robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            SetPositions(10, 10, 10, 10);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            Console.WriteLine($"[{iteration}] Movimento para 10° -> {ret}");
            robot.Sleep(1000);

            robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            SetPositions(50, 50, 50, 50);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            Console.WriteLine($"[{iteration}] Movimento para 50° -> {ret}");
            robot.Sleep(1000);
        }

        Console.WriteLine("Teste concluído (definição/leitura de chaves de função + ativação + 10 movimentos alternados).");
    }    