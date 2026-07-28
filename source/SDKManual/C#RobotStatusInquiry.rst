Consulta de Estado do Robô
==============================

.. toctree::
    :maxdepth: 5

Obter Posição Articular Atual (graus)
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a posição articular atual (graus)
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] jPos Posições das seis juntas, em graus
    * @return  Código de erro
    */
    int GetActualJointPosDegree(byte flag, ref JointPos jPos);

Obter Posição Articular Atual (radianos)
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a posição articular atual (radianos)
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] jPos Posições das seis juntas, em radianos
    * @return  Código de erro
    */
    int GetActualJointPosRadian(byte flag, ref JointPos jPos);

Obter Velocidade de Feedback Articular
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback articular - graus/s
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] speed Velocidades das seis juntas
    * @return Código de erro
    */
    int GetActualJointSpeedsDegree(byte flag, ref double[] speed);

Obter Aceleração de Feedback Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a aceleração de feedback articular - graus/s^2
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] acc Acelerações das seis juntas
    * @return Código de erro
    */
    int GetActualJointAccDegree(byte flag, ref double[] acc);

Obter Velocidade de Comando TCP - Velocidade Resultante
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a velocidade de comando TCP - velocidade resultante
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] tcp_speed Velocidade linear
    * @param [out] ori_speed Velocidade de orientação
    * @return Código de erro
    */
    int GetTargetTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed);

Obter Velocidade de Feedback TCP - Velocidade Resultante
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback TCP - velocidade resultante
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] tcp_speed Velocidade linear
    * @param [out] ori_speed Velocidade de orientação
    * @return Código de erro
    */
    int GetActualTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed);

Obter Velocidade de Comando TCP - Velocidades Componentes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a velocidade de comando TCP - velocidades componentes
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] speed Velocidades [x, y, z, rx, ry, rz]
    * @return Código de erro
    */
    int GetTargetTCPSpeed(byte flag, ref double[] speed);

Obter Velocidade de Feedback TCP - Velocidades Componentes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback TCP - velocidades componentes
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] speed Velocidades [x, y, z, rx, ry, rz]
    * @return Código de erro
    */
    int GetActualTCPSpeed(byte flag, ref double[] speed);

Obter Pose da Ferramenta Atual
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a pose da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose da ferramenta
    * @return  Código de erro
    */
    int GetActualTCPPose(byte flag, ref DescPose desc_pos);

Obter Número do Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o número do sistema de coordenadas da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] id Número do sistema de coordenadas da ferramenta
    * @return  Código de erro
    */
    int GetActualTCPNum(byte flag, ref int id);

Obter Número do Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o número do sistema de coordenadas da peça atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] id Número do sistema de coordenadas da peça
    * @return  Código de erro
    */
    int GetActualWObjNum(byte flag, ref int id);

Obter Pose do Flange da Extremidade Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém a pose do flange da extremidade atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do flange
    * @return  Código de erro
    */
    int GetActualToolFlangePose(byte flag, ref DescPose desc_pos);

Obter Torque Articular Atual
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o torque articular atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] torques Torques das juntas
    * @return Código de erro
    */
    int GetJointTorques(byte flag, float[] torques);

Obter a Hora do Sistema
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter a hora do sistema
    * @param  [out] t_ms Unidade ms, pode ser convertida de acordo com o tempo UTC. Quando o robô está em estado de falha, GetSystemClock retorna 0 e retorna um código de erro.
    * @return  Código de erro
    */
    public int GetSystemClock(ref double t_ms)

Verificar se o Movimento do Robô está Concluído
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Verifica se o movimento do robô está concluído
    * @param [out] state 0-não concluído, 1-concluído
    * @return Código de erro
    */
    int GetRobotMotionDone(ref byte state);

Consultar o Comprimento da Fila de Cache de Movimento do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Consulta o comprimento da fila de cache de movimento do robô
    * @param [out] len Comprimento da cache
    * @return Código de erro
    */
    int GetMotionQueueLength(ref int len);

Obter Estado de Parada de Emergência do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado de parada de emergência do robô
    * @param [out] state Estado de parada de emergência, 0-não em parada de emergência, 1-em parada de emergência
    * @return Código de erro
    */
    int GetRobotEmergencyStopState(ref byte state);

Obter Estado de Comunicação entre SDK e o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado de comunicação entre SDK e o robô
    * @param [out] state Estado de comunicação, 0-comunicação normal, 1-comunicação anormal
    */
    int GetSDKComState(ref int state);

Obter Sinal de Parada de Segurança
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o sinal de parada de segurança
    * @param [out] si0_state Sinal de parada de segurança SI0, 0-inválido, 1-válido
    * @param [out] si1_state Sinal de parada de segurança SI1, 0-inválido, 1-válido
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state);

Obter Temperatura do Driver Articular do Robô (°C)
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a temperatura do driver articular do robô (°C)
    * @return Código de erro
    */
    int GetJointDriverTemperature(double[] temperature);

Obter Torque do Driver Articular do Robô (Nm)
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o torque do driver articular do robô (Nm)
    * @return Código de erro
    */
    int GetJointDriverTorque(double torque[]);

Obter o Último Quadro dos Dados de Estado em Tempo Real do Robô (Alteração no Mecanismo Interno)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obter o último quadro dos dados de estado em tempo real do robô (thread interno atualiza continuamente, esta interface retorna diretamente os dados em cache)
    * @param [out] pkg Parâmetro de referência para receber os dados de estado do robô (estrutura ROBOT_STATE_PKG)
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha (ex. erro de comunicação de rede)
    */
    public int GetRobotRealTimeState(ref ROBOT_STATE_PKG pkg)

Exemplo de Código de Consulta de Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button29_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        double yangle = 0, zangle = 0;
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle:{yangle},zangle:{zangle}");

        JointPos j_deg = new JointPos(0,0,0,0,0,0);
        robot.GetActualJointPosDegree(0, ref j_deg);
        Console.WriteLine($"joint pos deg:{j_deg.jPos[0]},{j_deg.jPos[1]},{j_deg.jPos[2]},{j_deg.jPos[3]},{j_deg.jPos[4]},{j_deg.jPos[5]}");

        double[] jointSpeed = new double[6];
        robot.GetActualJointSpeedsDegree(0, ref jointSpeed);
        Console.WriteLine($"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}");

        double[] jointAcc = new double[6];
        robot.GetActualJointAccDegree(0, ref jointAcc);
        Console.WriteLine($"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}");

        double tcp_speed = 0, ori_speed = 0;
        robot.GetTargetTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        robot.GetActualTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        double[] targetSpeed = new double[6];
        robot.GetTargetTCPSpeed(0,ref targetSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}");

        double[] actualSpeed = new double[6];
        robot.GetActualTCPSpeed(0, ref actualSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}");

        DescPose tcp = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualTCPPose(0, ref tcp);
        Console.WriteLine($"tcp pose:{tcp.tran.x},{tcp.tran.y},{tcp.tran.z},{tcp.rpy.rx},{tcp.rpy.ry},{tcp.rpy.rz}");

        DescPose flange = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualToolFlangePose(0, ref flange);
        Console.WriteLine($"flange pose:{flange.tran.x},{flange.tran.y},{flange.tran.z},{flange.rpy.rx},{flange.rpy.ry},{flange.rpy.rz}");

        int id = 0;
        robot.GetActualTCPNum(0, ref id);
        Console.WriteLine($"tcp num:{id}");

        robot.GetActualWObjNum(0, ref id);
        Console.WriteLine($"wobj num:{id}");

        double[] jtorque = new double[6];
        robot.GetJointTorques(0, jtorque);
        Console.WriteLine($"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}");

        double t_ms = 0;
        robot.GetSystemClock(ref t_ms);
        Console.WriteLine($"system clock:{t_ms}");

        int config = 0;
        robot.GetRobotCurJointsConfig(ref config);
        Console.WriteLine($"joint config:{config}");

        byte motionDone = 0;
        robot.GetRobotMotionDone(ref motionDone);
        Console.WriteLine($"GetRobotMotionDone :{motionDone}");

        int len = 0;
        robot.GetMotionQueueLength(ref len);
        Console.WriteLine($"GetMotionQueueLength :{len}");

        byte emergState = 0;
        robot.GetRobotEmergencyStopState(ref emergState);
        Console.WriteLine($"GetRobotEmergencyStopState :{emergState}");

        int comstate = 0;
        robot.GetSDKComState(ref comstate);
        Console.WriteLine($"GetSDKComState :{comstate}");

        byte si0_state = 0, si1_state = 0;
        robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState :{si0_state} {si1_state}");

        double[] temp = new double[6];
        robot.GetJointDriverTemperature(temp);
        Console.WriteLine($"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}");

        double[] torque = new double[6];
        robot.GetJointDriverTorque(torque);
        Console.WriteLine($"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}");

        robot.GetRobotRealTimeState(ref pkg);
    }

Solução de Cinemática Inversa
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Solução de cinemática inversa
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] config Configuração do espaço articular, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @param [out] joint_pos Posição articular
    * @return  Código de erro
    */
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos);

Solução de Cinemática Inversa (com posição de referência)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Solução de cinemática inversa, verifica se há solução com base na posição articular de referência especificada
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @param [out] result 0-sem solução, 1-com solução
    * @return  Código de erro
    */
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref JointPos joint_pos);

Solução de Cinemática Inversa incluindo posição do eixo estendido no espaço cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Solução de cinemática inversa incluindo posição do eixo estendido no espaço cartesiano
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] exaxis Posição do eixo estendido
    * @param [in] tool Número da ferramenta
    * @param [in] workPiece Número da peça
    * @param [out] joint_pos Posição articular
    * @return Código de erro
    */
    public int GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, ref JointPos joint_pos);

Exemplo de Código de Solução de Cinemática Inversa incluindo posição do eixo estendido
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestInverseKinExaxis()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        DescPose desc = new DescPose(99.957f, -0.002f, 29.994f, -176.569f, -6.757f, -167.462f);
        ExaxisPos exaxis = new ExaxisPos(100.0f, 0.0f, 0.0f, 0.0f);
        JointPos jointPos = new JointPos(0,0,0,0,0,0);
        DescPose offsetPos = new DescPose(0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f);
        int rtn;
        robot.GetRobotRealTimeState(ref pkg);
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;

        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, ref jointPos);
        Console.WriteLine($"GetInverseKinExaxis joint is {jointPos.jPos[0]}, {jointPos.jPos[1]}, {jointPos.jPos[2]}, {jointPos.jPos[3]}, {jointPos.jPos[4]}, {jointPos.jPos[5]}");

        robot.ExtAxisMove(exaxis, 100, -1);

        int blendMode = 0;
        int velAccMode = 0;
        float oacc = 100.0f;
        byte flag = 0;
        robot.MoveJ(jointPos, desc, toolnum, workPcsNum, (float)100.0, (float)100.0, (float)100.0, exaxis, -1, 0, offsetPos);
    }

Verificar se a Solução de Cinemática Inversa Existe
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Solução de cinemática inversa, verifica se há solução com base na posição articular de referência especificada
    * @param [in] posMode 0-pose absoluta, 1-pose relativa - sistema de coordenadas base, 2-pose relativa - sistema de coordenadas da ferramenta
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @param [out] hasResult 0-sem solução, 1-com solução
    * @return Código de erro
    */
    int GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref bool hasResult);

Solução de Cinemática Direta
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Solução de cinemática direta
    * @param [in] joint_pos Posição articular
    * @param [out] desc_pos Pose cartesiana
    * @return  Código de erro
    */
    int GetForwardKin(JointPos joint_pos, ref DescPose desc_pos);

Exemplo de Código de Cálculo de Cinemática Direta e Inversa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button30_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);

        JointPos inverseRtn = new JointPos(0, 0, 0, 0, 0, 0);

        robot.GetInverseKin(0, desc_pos1, -1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKin rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");
        robot.GetInverseKinRef(0, desc_pos1, j1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKinRef rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");

        bool hasResut = false;
        robot.GetInverseKinHasSolution(0, desc_pos1, j1, ref hasResut);
        Console.WriteLine($"dcs1 GetInverseKinRef result {hasResut}");

        DescPose forwordResult = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(j1, ref forwordResult);
        Console.WriteLine($"jpos1 forwordResult rtn is {forwordResult.tran.x} {forwordResult.tran.y} {forwordResult.tran.z} {forwordResult.rpy.rx} {forwordResult.rpy.ry} {forwordResult.rpy.rz}");
    }

Consultar Dados do Ponto de Gerenciamento de Ensino do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Consulta os dados do ponto de gerenciamento de ensino do robô
    * @param [in] name Nome do ponto
    * @param [out] data Dados do ponto double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4}
    * @return Código de erro
    */
    int GetRobotTeachingPoint(string name, ref double[] data);

Obter Valores de Compensação dos Parâmetros DH do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os valores de compensação dos parâmetros DH do robô
    * @param [out] dhCompensation Valores de compensação dos parâmetros DH do robô (mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return Código de erro
    */
    int GetDHCompensation(ref double[] dhCompensation);

Obter Número de Série da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o número de série da caixa de controle
    * @param [out] SNCode Número de série da caixa de controle
    * @return Código de erro
    */
    int GetRobotSN(ref string SNCode);

Exemplo de Código de Consulta de Dados do Ponto de Gerenciamento de Ensino do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button31_Click(object sender, EventArgs e)
    {
        string name = "A0";
        double[] data = new double[20];
        int rtn = robot.GetRobotTeachingPoint(name, ref data);
        Console.WriteLine(" {0} name is: {1} \n", rtn, name);
        for (int i = 0; i < 20; i++)
        {
            Console.WriteLine("data is: {0} \n", data[i]);
        }

        int que_len = 0;
        rtn = robot.GetMotionQueueLength(ref que_len);
        Console.WriteLine("GetMotionQueueLength rtn is: {0}, queue length is: {1} \n", rtn, que_len);

        double[] dh = { 0, 0, 0, 0, 0, 0 };
        int retval = 0;
        retval = robot.GetDHCompensation(ref dh);
        Console.WriteLine($"retval is  {retval}");
        Console.WriteLine($"dh is {dh[0]}, {dh[1]}, {dh[2]}, {dh[3]}, {dh[4]}, {dh[5]}");
        string SN = "";
        robot.GetRobotSN(ref SN);
        Console.WriteLine($"robot SN is  {SN}");
    }

Obter Sistema de Coordenadas da Ferramenta por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta
    * @param [out] coord Valores do sistema de coordenadas
    * @param [out] type Tipo de ferramenta: 0-ferramenta; 1-sensor
    * @param [out] install Posição de instalação: 0-extremidade do robô; 1-externa ao robô
    * @param [out] toolID ID da ferramenta
    * @param [out] loadNo Número de carga
    * @return Código de erro
    */
    int GetToolCoordWithID(int id, ref DescPose coord, ref int type, ref int install, ref int toolID, ref int loadNo)

Obter Sistema de Coordenadas da Peça por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da peça por ID
    * @param [in] id Número do sistema de coordenadas da peça
    * @param [out] coord Valores do sistema de coordenadas
    * @param [out] refFrame Sistema de coordenadas de referência
    * @return Código de erro
    */
    public int GetWObjCoordWithID(int id, ref DescPose coord, ref int refFrame)

Obter Sistema de Coordenadas da Ferramenta Externa por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta externa por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa, 20-39 correspondem aos sistemas de coordenadas de ferramentas externas 0-19
    * @param [out] coord Pose TCP da ferramenta externa fixa no robô
    * @param [out] tcoord Pose do sistema de coordenadas da peça montado na extremidade do robô
    * @return Código de erro
    */
    public int GetExToolCoordWithID(int id, ref DescPose coord, ref DescPose tcoord)

Obter Sistema de Coordenadas do Eixo Estendido por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas do eixo estendido por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa
    * @param [out] coord Valores do sistema de coordenadas
    * @param [out] axisCoordNum Número do eixo estendido; bit0-bit3 correspondem aos eixos estendidos 1-4; por exemplo, valor axisCoordNum 3 corresponde aos eixos estendidos [1, 2]
    * @param [out] calibFlag Flag de calibração; 0-não calibrado; 1-calibrado
    * @return Código de erro
    */
    public int GetExAxisCoordWithID(int id, ref DescPose coord, ref int axisCoordNum, ref int calibFlag)

Obter Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da ferramenta atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurToolCoord(ref DescPose coord)

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da peça atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurWObjCoord(ref DescPose coord)

Obter Sistema de Coordenadas da Ferramenta Externa Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da ferramenta externa atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurExToolCoord(ref DescPose coord)

Obter Sistema de Coordenadas do Eixo Estendido Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas do eixo estendido atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurExAxisCoord(ref DescPose coord)

Exemplo de Código para Obter Coordenadas por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    public int TestCoord()
    {
        int rtn;
        int id = 1;

        // GetToolCoordWithID
        DescPose toolCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int type = 0, install = 0, toolID = 0, loadNo = 0;
        rtn = robot.GetToolCoordWithID(id, ref toolCoord, ref type, ref install, ref toolID, ref loadNo);
        Console.WriteLine("GetToolCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, type={7}, install={8}, toolID={9}, loadNo={10}",
            id, toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz, type, install, toolID, loadNo);

        // GetWObjCoordWithID
        DescPose wobjCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int refFrame = 0;
        rtn = robot.GetWObjCoordWithID(id, ref wobjCoord, ref refFrame);
        Console.WriteLine("GetWObjCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, refFrame={7}",
            id, wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz, refFrame);

        // GetExToolCoordWithID
        DescPose extoolCoord = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose exworkpieceCoord = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.GetExToolCoordWithID(21, ref extoolCoord, ref exworkpieceCoord);
        Console.WriteLine("GetExToolCoordWithID 21, {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);
        Console.WriteLine("  tcoord: {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            exworkpieceCoord.tran.x, exworkpieceCoord.tran.y, exworkpieceCoord.tran.z,
            exworkpieceCoord.rpy.rx, exworkpieceCoord.rpy.ry, exworkpieceCoord.rpy.rz);

        // GetExAxisCoordWithID
        DescPose exAxisCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int axisCoordNum = 0, calibFlag = 0;
        rtn = robot.GetExAxisCoordWithID(id, ref exAxisCoord, ref axisCoordNum, ref calibFlag);
        Console.WriteLine("GetExAxisCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, axisCoordNum={7}, calibFlag={8}",
            id, exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz, axisCoordNum, calibFlag);

        // GetTargetPayloadWithID
        double weight = 0.0;
        DescTran cog = new DescTran(0, 0, 0);
        rtn = robot.GetTargetPayloadWithID(id, ref weight, ref cog);
        Console.WriteLine("GetTargetPayloadWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3}",
            id, weight, cog.x, cog.y, cog.z);

        // GetCurToolCoord
        rtn = robot.GetCurToolCoord(ref toolCoord);
        Console.WriteLine("GetCurToolCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz);

        // GetCurWObjCoord
        rtn = robot.GetCurWObjCoord(ref wobjCoord);
        Console.WriteLine("GetCurWObjCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz);

        // GetCurExToolCoord
        rtn = robot.GetCurExToolCoord(ref extoolCoord);
        Console.WriteLine("GetCurExToolCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);

        // GetCurExAxisCoord
        rtn = robot.GetCurExAxisCoord(ref exAxisCoord);
        Console.WriteLine("GetCurExAxisCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz);

        // GetTargetPayload / GetTargetPayloadCog
        double weightT = 0.0;
        DescTran cogT = new DescTran(0, 0, 0);
        robot.GetTargetPayload(0, ref weightT);
        robot.GetTargetPayloadCog(0, ref cogT);
        Console.WriteLine("GetTargetPayload {0:F3} {1:F3} {2:F3} {3:F3}",
            weightT, cogT.x, cogT.y, cogT.z);

        // SetToolCoord
        DescPose coordSet = new DescPose(0, 1, 2, 3, 4, 5);
        rtn = robot.SetToolCoord(1, coordSet, 0, 0, 1, 0);
        Console.WriteLine("SetToolCoord(1) rtn={0}", rtn);

        // SetWObjCoord
        rtn = robot.SetWObjCoord(1, coordSet, 0);
        Console.WriteLine("SetWObjCoord(1) rtn={0}", rtn);

        // SetLoadWeight + SetLoadCoord
        rtn = robot.SetLoadWeight(1, 1.3f);
        Console.WriteLine("SetLoadWeight(1,1.3) rtn={0}", rtn);

        DescTran loadCog = new DescTran(10, 20, 30);
        rtn = robot.SetLoadCoord(1, loadCog);
        Console.WriteLine("SetLoadCoord(1,10,20,30) rtn={0}", rtn);

        // SetExToolCoord
        DescPose etcp = new DescPose(0, 0, 100, 0, 0, 0);
        DescPose etool = new DescPose(0, 0, 50, 0, 0, 0);
        rtn = robot.SetExToolCoord(21, etcp, etool);
        Console.WriteLine("SetExToolCoord(21) rtn={0}", rtn);
        // SetExToolList
        rtn = robot.SetExToolList(21, etcp, etool);
        Console.WriteLine("SetExToolList(21) rtn={0}", rtn);

        // ExtAxisActiveECoordSys
        rtn = robot.ExtAxisActiveECoordSys(1, 1, coordSet, 1);
        Console.WriteLine("ExtAxisActiveECoordSys(1,1,..,1) rtn={0}", rtn);

        return 0;
    }