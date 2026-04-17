Consulta de Estado do Robô
==============================

.. toctree::
    :maxdepth: 5

Obter Posição Articular Atual (graus)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a posição articular atual (graus)
    * @param [out] jPos Posições das seis juntas obtidas, em graus
    * @return Código de erro
    */
    int GetActualJointPosDegree(JointPos jPos);

Obter Velocidade de Feedback Articular - graus/s
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback articular - graus/s
    * @param [out] speed Velocidades das seis juntas
    * @return Código de erro
    */
    int GetActualJointSpeedsDegree(Object[] speed);

Obter Aceleração de Feedback Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a aceleração de feedback articular - graus/s²
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] acc Acelerações das seis juntas
    * @return Código de erro
    */
    public int GetActualJointAccDegree(int flag, Object[] acc)

Obter Velocidade de Comando TCP - Velocidade Resultante
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade de comando TCP - velocidade resultante
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] tcp_speed Velocidade linear
    * @param [out] ori_speed Velocidade de orientação
    * @return Código de erro
    */
    public int GetTargetTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

Obter Velocidade de Feedback TCP - Velocidade Resultante
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback TCP - velocidade resultante
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] tcp_speed Velocidade linear
    * @param [out] ori_speed Velocidade de orientação
    * @return Código de erro
    */
    public int GetActualTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

Obter Velocidade de Comando TCP - Velocidades Componentes
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade de comando TCP - velocidades componentes
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] speed Velocidades [x, y, z, rx, ry, rz]
    * @return Código de erro
    */
    public int GetTargetTCPSpeed(int flag, Object[] speed)

Obter Velocidade de Feedback TCP - Velocidades Componentes
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade de feedback TCP - velocidades componentes
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] speed Velocidades [x, y, z, rx, ry, rz]
    * @return Código de erro
    */
    public int GetActualTCPSpeed(int flag, Object[] speed)

Obter Pose da Ferramenta Atual
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a pose da ferramenta atual
    * @param [out] desc_pos Pose da ferramenta
    * @return Código de erro
    */
    int GetActualTCPPose(DescPose desc_pos);

Obter Número do Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o número do sistema de coordenadas da ferramenta atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] id Número do sistema de coordenadas da ferramenta
    * @return Código de erro
    */
    int GetActualTCPNum(int flag, int[] id)

Obter Número do Sistema de Coordenadas da Peça Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o número do sistema de coordenadas da peça atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] id Número do sistema de coordenadas da peça
    * @return Código de erro
    */
    public int GetActualWObjNum(int flag, int[] id)

Obter Pose do Flange da Extremidade Atual
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a pose do flange da extremidade atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] desc_pos Pose do flange
    * @return Código de erro
    */
    public int GetActualToolFlangePose(int flag, DescPose desc_pos)

Obter Torque Articular Atual
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o torque articular atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] torques Torques das juntas
    * @return Código de erro
    */
    int GetJointTorques(int flag, Object[] torques);

Obter Tempo do Sistema
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o tempo do sistema
    * @return List[0]:int código de erro; List[1]:double t_ms em ms
    */
    List<Number> GetSystemClock();

Verificar se o Movimento do Robô está Concluído
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Verifica se o movimento do robô está concluído
    * @param [out] state 0-não concluído, 1-concluído
    * @return Código de erro
    */
    public int GetRobotMotionDone(int[] state)

Consultar o Comprimento da Fila de Cache de Movimento do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Consulta o comprimento da fila de cache de movimento do robô
    * @param [out] len Comprimento da cache
    * @return Código de erro
    */
    public int GetMotionQueueLength(int[] len)

Obter Estado de Parada de Emergência do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado de parada de emergência do robô
    * @param [out] state Estado de parada de emergência, 0-não em parada de emergência, 1-em parada de emergência
    * @return Código de erro
    */
    public int GetRobotEmergencyStopState(int[] state)

Obter Estado de Comunicação entre SDK e o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado de comunicação entre SDK e o robô
    * @return state Estado de comunicação, 0-comunicação normal, 1-comunicação anormal
    */
    public int GetSDKComState()

Obter Sinal de Parada de Segurança
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sinal de parada de segurança
    * @param [out] si0_state Sinal de parada de segurança SI0, 0-inválido, 1-válido
    * @param [out] si1_state Sinal de parada de segurança SI1, 0-inválido, 1-válido
    * @return Código de erro
    */
    public int GetSafetyStopState(int[] si0_state, int[] si1_state)

Obter Temperatura do Driver Articular do Robô (°C)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a temperatura do driver articular do robô (°C)
    * @param [out] temperature Temperatura
    * @return Código de erro
    */
    public int GetJointDriverTemperature(double[] temperature)

Obter Torque do Driver Articular do Robô (Nm)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o torque do driver articular do robô (Nm)
    * @param [out] torque Torque
    * @return Código de erro
    */
    public int GetJointDriverTorque(double[] torque)

Obter Estrutura de Estado em Tempo Real do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a estrutura de estado em tempo real do robô
    * @return Estrutura de estado em tempo real
    */
    public ROBOT_STATE_PKG GetRobotRealTimeState()

Exemplo de Código de Consulta de Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetStatus(Robot robot)
    {
        List<Number> angle = new ArrayList<>();
        angle = robot.GetRobotInstallAngle();
        System.out.println("yangle:"+angle.get(1)+",zangle:"+angle.get(2));

        JointPos j_deg = new JointPos(){};
        robot.GetActualJointPosDegree(j_deg);

        Object[] jointSpeed = new Object[] { 0,0,0,0,0,0 };
        robot.GetActualJointSpeedsDegree(jointSpeed);

        Object[] jointAcc = new Object[]{0,0,0,0,0,0 };
        robot.GetActualJointAccDegree(0, jointAcc);

        double tcp_speed = 0.0;
        double ori_speed = 0.0;
        robot.GetTargetTCPCompositeSpeed(0, tcp_speed, ori_speed);

        robot.GetActualTCPCompositeSpeed(0, tcp_speed, ori_speed);

        Object[] targetSpeed = new Object[] { 0,0,0,0,0,0 };
        robot.GetTargetTCPSpeed(0, targetSpeed);

        Object[] actualSpeed = new Object[] {0,0,0,0,0,0 };
        robot.GetActualTCPSpeed(0, actualSpeed);

        DescPose tcp = new DescPose(){};
        robot.GetActualTCPPose(tcp);

        DescPose flange = new DescPose(){};
        robot.GetActualToolFlangePose(0, flange);

        int[] id = {};
        robot.GetActualTCPNum(0, id);

        robot.GetActualWObjNum(0, id);

        List<Number> jtorque = new ArrayList<>();
        jtorque = robot.GetJointTorques(0);

        List<Number> t_ms = new ArrayList<>();
        t_ms = robot.GetSystemClock();

        List<Integer> config = new ArrayList<>();
        config = robot.GetRobotCurJointsConfig();

        int motionDone = 0;
        robot.GetRobotMotionDone(motionDone);

        int[] len = {0 };
        robot.GetMotionQueueLength(len);

        int[] emergState = {0};
        robot.GetRobotEmergencyStopState(emergState);

        int comstate = 0;
        comstate = robot.GetSDKComState();

        int[] si0_state = new int[]{0}, si1_state = new int[]{0};
        robot.GetSafetyStopState(si0_state, si1_state);

        double[] temp = new double[] { 0,0,0,0,0,0 };
        robot.GetJointDriverTemperature(temp);

        double[] torque = new double[]{ 0,0,0,0,0,0 };
        robot.GetJointDriverTorque(torque);

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        pkg = robot.GetRobotRealTimeState();

        return 0;
    }

Solução de Cinemática Inversa
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Solução de cinemática inversa
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] config Configuração do espaço articular, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @param [out] joint_pos Posição articular
    * @return Código de erro
    */
    int GetInverseKin(int type, DescPose desc_pos, int config, JointPos joint_pos);

Solução de Cinemática Inversa (com posição de referência)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Solução de cinemática inversa, resolve com base na posição articular de referência especificada
    * @param [in] posMode 0-pose absoluta, 1-pose relativa - sistema de coordenadas base, 2-pose relativa - sistema de coordenadas da ferramenta
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @param [out] joint_pos Posição articular
    * @return Código de erro
    */
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, JointPos joint_pos);

Solução de Cinemática Inversa incluindo posição do eixo estendido no espaço cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Solução de cinemática inversa incluindo posição do eixo estendido no espaço cartesiano
    * @param type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param desc_pos Pose cartesiana
    * @param exaxis Posição do eixo estendido
    * @param tool Número da ferramenta
    * @param workPiece Número da peça
    * @param joint_pos Posição articular
    * @return Código de erro
    */
    public int GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, JointPos joint_pos)

Exemplo de Código de Solução de Cinemática Inversa incluindo posição do eixo estendido
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestInverseKinExaxis(Robot robot)
    {
        DescPose desc = new DescPose(99.957, -0.002, 29.994, -176.569, -6.757, -167.462);
        ExaxisPos exaxis = new ExaxisPos(100.0, 0.0, 0.0, 0.0);
        JointPos jointPos = new JointPos();
        DescPose offsetPos = new DescPose();
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;
        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, jointPos);
        System.out.printf("GetInverseKinExaxis joint is %f, %f, %f, %f, %f, %f\n", jointPos.J1, jointPos.J2, jointPos.J3, jointPos.J4, jointPos.J5, jointPos.J6);
        robot.ExtAxisMove(exaxis, 100, -1);
        robot.MoveJ(jointPos, desc, toolnum, workPcsNum, 100.0, 100.0, 100.0, exaxis, -1, 0, offsetPos);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }

Verificar se a Solução de Cinemática Inversa Existe
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Solução de cinemática inversa, verifica se há solução com base na posição articular de referência especificada
    * @param [in] posMode 0-pose absoluta, 1-pose relativa - sistema de coordenadas base, 2-pose relativa - sistema de coordenadas da ferramenta
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @return Código de erro List[0]:código de erro; List[1]: int hasResult 0-sem solução, 1-com solução
    */
    List<Integer> GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref);

Solução de Cinemática Direta
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Solução de cinemática direta
    * @param [in] joint_pos Posição articular
    * @param [out] desc_pos Pose cartesiana
    * @return Código de erro
    */
    int GetForwardKin(JointPos joint_pos, DescPose desc_pos);

Exemplo de Código de Cálculo de Cinemática Direta e Inversa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestInverseKin(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        JointPos inverseRtn = new JointPos(){};

        robot.GetInverseKin(0, desc_pos1, -1, inverseRtn);
        robot.GetInverseKinRef(0, desc_pos1, j1, inverseRtn);

        int hasResut = 0;
        robot.GetInverseKinHasSolution(0, desc_pos1, j1);

        DescPose forwordResult = new DescPose(){};
        robot.GetForwardKin(j1, forwordResult);

        return 0;
    }

Consultar Dados do Ponto de Gerenciamento de Ensino do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Consulta os dados do ponto de gerenciamento de ensino do robô
    * @param [in] name Nome do ponto
    * @return List[0]:código de erro; List[1] - List[20]: dados do ponto double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4}
    */
    List<Number> GetRobotTeachingPoint(String name);

Obter Valores de Compensação dos Parâmetros DH do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os valores de compensação dos parâmetros DH do robô
    * @param dhCompensation Valores de compensação dos parâmetros DH do robô (mm) [cmpstD1, cmpstA2, cmpstA3, cmpstD4, cmpstD5, cmpstD6]
    * @return Código de erro
    */
    public int GetDHCompensation(Object[] dhCompensation)

Obter Número de Série da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o número de série da caixa de controle
    * @param [out] SNCode Número de série da caixa de controle
    * @return Código de erro
    */
    int GetRobotSN(String[] SNCode);

Exemplo de Código de Consulta de Dados do Ponto de Gerenciamento de Ensino do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetTeachPoint(Robot robot)
    {
        String name = "P1";
        List<Number> data = new ArrayList<>();
        data = robot.GetRobotTeachingPoint(name);
        System.out.println(name+" name is: "+data.get(0));
        for (int i = 0; i < 20; i++)
        {
            System.out.println("data is: "+ data.get(i+1));
        }

        int[] que_len = {0};
        int rtn = robot.GetMotionQueueLength(que_len);
        System.out.println("GetMotionQueueLength rtn is:"+rtn+", queue length is:"+ que_len[0]);

        Object[] dh = new Object[]{ 0,0,0,0,0,0 };
        int retval = 0;
        retval = robot.GetDHCompensation(dh);
        System.out.println("retval is: "+retval);

        String[] SN = new String[]{""};
        robot.GetRobotSN(SN);
        System.out.println("robot SN is "+SN[0]);
        return 0;
    }

Obter Sistema de Coordenadas da Ferramenta por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    int GetToolCoordWithID(int id, DescPose coord)

Obter Sistema de Coordenadas da Peça por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da peça por ID
    * @param [in] id Número do sistema de coordenadas da peça
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    public int GetWObjCoordWithID(int id, DescPose coord)

Obter Sistema de Coordenadas da Ferramenta Externa por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta externa por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    public int GetExToolCoordWithID(int id, DescPose coord)

Obter Sistema de Coordenadas do Eixo Estendido por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas do eixo estendido por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    public int GetExAxisCoordWithID(int id, DescPose coord)

Obter Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da ferramenta atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurToolCoord(DescPose coord)

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da peça atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurWObjCoord(DescPose coord)

Obter Sistema de Coordenadas da Ferramenta Externa Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas da ferramenta externa atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurExToolCoord(DescPose coord)

Obter Sistema de Coordenadas do Eixo Estendido Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém o sistema de coordenadas do eixo estendido atual
     * @param [out] coord Valores do sistema de coordenadas
     * @return Código de erro
     */
    public int GetCurExAxisCoord(DescPose coord)

Exemplo de Código de Sistemas de Coordenadas e Carga do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestCoord(Robot robot)
    {
        int id = 1;
        int rtn = 0;
        DescPose toolCoord = new DescPose();
        DescPose extoolCoord = new DescPose();
        DescPose wobjCoord = new DescPose();
        DescPose exAxisCoord = new DescPose();

        robot.GetCurToolCoord(toolCoord); // ferramenta
        System.out.println("GetToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetCurWObjCoord(toolCoord); // peça
        System.out.println("GetCurWObjCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetCurExToolCoord(toolCoord); // ferramenta externa
        System.out.println("GetCurExToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetCurExAxisCoord(toolCoord); // eixo estendido
        System.out.println("GetCurExToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        List<Number> weightT = new ArrayList<>(); // centro de massa
        DescTran cogT = new DescTran();
        weightT = robot.GetTargetPayload(0);
        robot.GetTargetPayloadCog(0, cogT);
        System.out.println("GetTargetPayload :"+weightT.get(1).doubleValue()+", "+
                cogT.x+", "+cogT.y+", "+cogT.z);

        robot.GetToolCoordWithID(id, toolCoord);
        System.out.println("GetToolCoordWithID:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetWObjCoordWithID(id, wobjCoord);
        System.out.println("GetWObjCoordWithID "+id+", "+
                wobjCoord.tran.x+","+ wobjCoord.tran.y+","+ wobjCoord.tran.z+","+
                wobjCoord.rpy.rx+","+ wobjCoord.rpy.ry+","+ wobjCoord.rpy.rz);

        robot.GetExToolCoordWithID(id, extoolCoord); // ferramenta externa
        System.out.println("GetExToolCoordWithID :"+ id+","+
                extoolCoord.tran.x+","+ extoolCoord.tran.y+","+ extoolCoord.tran.z+","+
                extoolCoord.rpy.rx+","+ extoolCoord.rpy.ry+","+ extoolCoord.rpy.rz);

        robot.GetExAxisCoordWithID(id, exAxisCoord); // eixo estendido
        System.out.println("GetExAxisCoordWithID "+id+","+
                exAxisCoord.tran.x+","+ exAxisCoord.tran.y+","+ exAxisCoord.tran.z+","+
                exAxisCoord.rpy.rx+","+ exAxisCoord.rpy.ry+","+ exAxisCoord.rpy.rz);

        double[] weight = new double[1]; // carga e centro de massa
        DescTran getCog = new DescTran();
        robot.GetTargetPayloadWithID(id, weight, getCog);
        System.out.println("GetTargetPayloadWithID :"+ id+","+ weight[0]+","+
                getCog.x+","+ getCog.y+","+ getCog.z);

        DescPose coordSet0 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose coordSet = new DescPose(1, 2, 3, 4, 5, 6);
        DescPose etcp = new DescPose(10, 20, 30, 40, 50, 60);
        DescPose etool = new DescPose(0.1, 0.2, 0.3, 0.4, 0.5, 0.6);
        DescTran cog = new DescTran(1, 2, 3);

        robot.SetToolCoord(id, coordSet, 0, 0, 1, 0);
        robot.Sleep(100);
        robot.SetWObjCoord(id, coordSet, 0);
        robot.Sleep(100);
        robot.ExtAxisActiveECoordSys(id, 1, coordSet, 1); // Aplica o resultado da calibração ao sistema de coordenadas do eixo estendido
        robot.Sleep(100);
        rtn = robot.SetExToolCoord(id, etcp, etool);
        robot.Sleep(100);
        rtn = robot.SetLoadWeight(id, 1.5);
        robot.Sleep(500);
        rtn = robot.SetLoadCoord(id, cog);
        robot.Sleep(100);
    }