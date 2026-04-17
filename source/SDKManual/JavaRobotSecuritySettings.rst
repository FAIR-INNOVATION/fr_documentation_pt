Configurações de Segurança do Robô
===================================================

.. toctree::
    :maxdepth: 5

Definir Nível de Colisão
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o nível de colisão
    * @param [in] mode 0-nível, 1-percentagem
    * @param [in] level Limiar de colisão, intervalo do nível [1 - 10 corresponde ao nível 1-10, 100-desativado], intervalo da percentagem [0~10 corresponde a 0% - 100%]
    * @param [in] config 0-não atualizar arquivo de configuração, 1-atualizar arquivo de configuração
    * @return Código de erro
    */
    int SetAnticollision(int mode, Object[] level, int config);

Definir Estratégia Pós-Colisão
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a estratégia pós-colisão
    * @param [in] strategy 0-parar com erro, 1-continuar execução
    * @param [in] safeTime Tempo de paragem segura [1000 - 2000]ms
    * @param [in] safeDistance Distância de paragem segura [1-150]mm
    * @param [in] safetyMargin Fator de segurança para j1-j6 [1-10]
    * @return Código de erro
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]);

Iniciar Função de Limiar de Deteção de Colisão Personalizada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief Inicia a função de limiar de deteção de colisão personalizada, define os limiares de deteção de colisão na extremidade da junta e na extremidade do TCP
    * @param [in] flag 1-apenas deteção da junta ativada; 2-apenas deteção do TCP ativada; 3-deteção da junta e do TCP ativadas simultaneamente
    * @param [in] jointDetectionThreshould Limiar de deteção de colisão da junta j1-j6
    * @param [in] tcpDetectionThreshould Limiar de deteção de colisão do TCP, xyzabc
    * @param [in] block 0-não bloqueante; 1-bloqueante
    * @return Código de erro
    */
    public int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

Desativar Função de Limiar de Deteção de Colisão Personalizada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief Desativa a função de limiar de deteção de colisão personalizada
    * @return Código de erro
    */
    public int CustomCollisionDetectionEnd();

Exemplo de Código para Definição do Nível de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollision(Robot robot)
    {
        int mode = 0;
        int config = 1;
        Object[] level1 = new Object[]{ 1.0,2.0,3.0,4.0,5.0,6.0 };
        Object[] level2 = new Object[]{ 50.0,20.0,30.0,40.0,50.0,60.0 };

        int rtn = robot.SetAnticollision(mode, level1, config);
        System.out.println("SetAnticollision mode 0 rtn is: "+ rtn);
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        System.out.println("SetAnticollision mode 1 rtn is :"+ rtn);

        JointPos p1Joint = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos p2Joint = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose p1Desc = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, 2,0, exaxisPos, 0, 0, offdese,0,10);
        robot.ResetAllError();
        int[] safety = new int[]{ 5,5,5,5,5,5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        System.out.println("SetCollisionStrategy rtn is:"+ rtn);

        double[] jointDetectionThreshould = new double[]{ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould = new double[] { 60,60,60,60,60,60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        System.out.println("CustomCollisionDetectionStart rtn is :"+ rtn);

        robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        rtn = robot.CustomCollisionDetectionEnd();
        System.out.println("CustomCollisionDetectionEnd rtn is: "+ rtn);
        return 0;
    }

Definir Limite Positivo
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o limite positivo
    * @param [in] limit Posições das seis juntas, em graus
    * @return Código de erro
    */
    int SetLimitPositive(Object[] limit);

Definir Limite Negativo
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o limite negativo
    * @param [in] limit Posições das seis juntas, em graus
    * @return Código de erro
    */
    int SetLimitNegative(Object[] limit);

Obter Ângulo do Limite Flexível das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o ângulo do limite flexível das juntas
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] negative Ângulo do limite negativo, em graus
    * @param [out] positive Ângulo do limite positivo, em graus
    * @return Código de erro
    */
    int GetJointSoftLimitDeg(int flag, Object[] negative, Object[] positive);

Exemplo de Código para Definição de Limites do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLimit(Robot robot)
    {
        Object[] plimit = new Object[] { 170.0,80.0,150.0,80.0,170.0,160.0 };
        robot.SetLimitPositive(plimit);
        Object[] nlimit = new Object[] { -170.0,-260.0,-150.0,-260.0,-170.0,-160.0 };
        robot.SetLimitNegative(nlimit);

        Object[] neg_deg = new Object[] {0, 0 , 0, 0, 0, 0}, pos_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        robot.GetJointSoftLimitDeg(1, neg_deg, pos_deg);
        System.out.println("neg limit deg:"+ neg_deg[0]+","+ neg_deg[1]+","+ neg_deg[2]+","+ neg_deg[3]+","+ neg_deg[4]+","+ neg_deg[5]);
        System.out.println("pos limit deg:"+pos_deg[0]+","+ pos_deg[1]+","+ pos_deg[2]+","+ pos_deg[3]+","+ pos_deg[4]+","+pos_deg[5]);
        return 0;
    }

Definir Método de Deteção de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Define o método de deteção de colisão do robô
    * @param [in] method Método de deteção de colisão: 0-modo de corrente; 1-duplo encoder; 2-corrente e duplo encoder ativados simultaneamente
    * @param [in] thresholdMode Modo do limiar de nível de colisão; 0-modo de limiar fixo do nível de colisão; 1-limiar de deteção de colisão personalizado
    * @return Código de erro
    */
    int SetCollisionDetectionMethod(int method, int thresholdMode)

Definir Ativação/Desativação de Deteção de Colisão em Estática
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a ativação/desativação de deteção de colisão em estática
    * @param [in] status 0-desativar; 1-ativar
    * @return Código de erro
    */
    public int SetStaticCollisionOnOff(int status)

Exemplo de Código para Definição do Método de Deteção de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollisionMethod(Robot robot)
    {
        int rtn = robot.SetCollisionDetectionMethod(0);

        rtn = robot.SetStaticCollisionOnOff(1);
        System.out.println("SetStaticCollisionOnOff On rtn is:"+ rtn);
        robot.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        System.out.println("SetStaticCollisionOnOff Off rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

Deteção de Torque e Potência das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Deteção de torque e potência das juntas
    * @param [in] status 0-desativar; 1-ativar
    * @param [in] power Potência máxima definida (W)
    * @return Código de erro
    */
    public int SetPowerLimit(int status, double power)

Exemplo de Código para Deteção de Torque e Potência das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPowerLimit(Robot robot)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        List<Number> joint_toq = new ArrayList<>();
        joint_toq = robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); // # início do ServoJT
        int error = 0;
        while (count > 0)
        {
            count = count - 1;
            robot.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);

        robot.CloseRPC();
        return 0;
    }

Definir Parâmetros de Velocidade Segura
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros de velocidade segura
    * @param enable 0-desativar; 1-ativar no modo manual; 2-ativar em todos os modos (limitação automática de velocidade não suportada)
    * @param maxTCPVel Limitar a velocidade máxima do TCP;[0-1000]mm/s
    * @param strategy Estratégia após excesso de velocidade; 0-parar com alarme; 1-limitação automática de velocidade; 2-parar com alarme e desativar
    * @return Código de erro
    */
    public int SetVelReducePara(int enable, double maxTCPVel, int strategy)

Exemplo de Código SDK para Definir Parâmetros de Velocidade Segura
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSetVelReducePara(Robot robot) {
        int rtn = 0;

        JointPos j1 = new JointPos(0, -90, 90, 0, 0, 0);
        JointPos j2 = new JointPos(90, -90, 90, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        robot.SetSpeed(80);
        rtn = robot.SetVelReducePara(2, 30, 1);
        System.out.printf("SetVelReducePara param error rtn is %d\n", rtn);

        rtn = robot.SetVelReducePara(0, 30, 1);
        System.out.printf("SetVelReducePara disable reduce vel rtn is %d\n", rtn);
        robot.MoveJ(j1, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);

        rtn = robot.SetVelReducePara(1, 30, 1);
        System.out.printf("SetVelReducePara reduce vel rtn is %d\n", rtn);
        robot.MoveJ(j1, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);

        rtn = robot.SetVelReducePara(2, 30, 2);
        System.out.printf("SetVelReducePara disable robot rtn is %d\n", rtn);
        robot.MoveJ(j1, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);

        robot.Sleep(2000);
        robot.ResetAllError();
        robot.RobotEnable(1);
        robot.Sleep(1000);

        rtn = robot.SetVelReducePara(2, 30, 0);
        System.out.printf("SetVelReducePara report error rtn is %d\n", rtn);
        robot.MoveJ(j1, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);

        robot.Sleep(1000);
        return 0;
    }