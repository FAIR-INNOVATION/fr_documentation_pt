Configurações de Segurança do Robô
===================================================

.. toctree::
    :maxdepth: 5

Definir Nível de Colisão
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define o nível de colisão
    * @param  [in]  mode  0-nível, 1-percentagem
    * @param  [in]  level  Limiar de colisão, o nível corresponde ao intervalo[], a percentagem corresponde ao intervalo[0~1]
    * @param  [in]  config 0-não atualizar ficheiro de configuração, 1-atualizar ficheiro de configuração
    * @return   Código de erro
    */
    int SetAnticollision(int mode, double[] level, int config);

Definir Estratégia Pós-Colisão
+++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define a estratégia pós-colisão
    * @param  [in] strategy  0-parar com erro; 1-continuar execução; 2-parar com erro; 3-modo de torque gravitacional; 4-modo de resposta oscilatória; 5-modo de recuo elástico
    * @param  [in] safeTime  Tempo de paragem segura [1000 - 2000]ms
    * @param  [in] safeDistance  Distância de paragem segura [1-150]mm
    * @param  [in] safeVel  Velocidade segura do TCP [50-250]mm/s
    * @param  [in] safetyMargin  Fator de segurança para j1-j6 [1-10]
    * @return   Código de erro
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel,int[] safetyMargin);

Iniciar Função de Limiar de Deteção de Colisão Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Inicia a função de limiar de deteção de colisão personalizada, define os limiares de deteção de colisão na extremidade da junta e na extremidade do TCP
    * @param  [in] flag 1-apenas deteção da junta ativada; 2-apenas deteção do TCP ativada; 3-deteção da junta e do TCP ativadas simultaneamente
    * @param  [in] jointDetectionThreshould  Limiar de deteção de colisão da junta j1-j6
    * @param  [in] tcpDetectionThreshould  Limiar de deteção de colisão do TCP, xyzabc
    * @param  [in] block 0-não bloqueante; 1-bloqueante
    * @return   Código de erro
    */
    int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

Desativar Função de Limiar de Deteção de Colisão Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Desativa a função de limiar de deteção de colisão personalizada
    * @return   Código de erro
    */
    int CustomCollisionDetectionEnd()

Exemplo de Código para Definição do Nível de Colisão do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button24_Click(object sender, EventArgs e)
    {
        int mode = 0;
        int config = 1;
        double[] level1 = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f };
        double[] level2 = { 50.0f, 20.0f, 30.0f, 40.0f, 50.0f, 60.0f };

        int rtn = robot.SetAnticollision(mode, level1, config);
        Console.WriteLine($"SetAnticollision mode 0 rtn is {rtn}");
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        Console.WriteLine($"SetAnticollision mode 1 rtn is {rtn}");

        JointPos p1Joint = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos p2Joint = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0.0f, 0.0f, 0.0f, 0.0f);
        DescPose offdese = new DescPose(0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, 2,  exaxisPos, 0, 0,  offdese);
        robot.ResetAllError();
        int[] safety = { 5, 5, 5, 5, 5, 5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        Console.WriteLine($"SetCollisionStrategy rtn is {rtn}");

        double[] jointDetectionThreshould = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould = { 60, 60, 60, 60, 60, 60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        Console.WriteLine($"CustomCollisionDetectionStart rtn is {rtn}");

        robot.MoveL( p1Joint,  p1Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        rtn = robot.CustomCollisionDetectionEnd();
        Console.WriteLine($"CustomCollisionDetectionEnd rtn is {rtn}");
    }

Definir Limite Positivo
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o limite positivo
    * @param  [in] limit  Posições das seis juntas, em graus
    * @return   Código de erro
    */
    int SetLimitPositive(double[] limit);

Definir Limite Negativo
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o limite negativo
    * @param  [in] limit  Posições das seis juntas, em graus
    * @return   Código de erro
    */
    int SetLimitNegative(double[] limit);

Obter Ângulo do Limite Flexível das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o ângulo do limite flexível das juntas
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] negative  Ângulo do limite negativo, em graus
    * @param  [out] positive  Ângulo do limite positivo, em graus
    * @return   Código de erro
    */
    int GetJointSoftLimitDeg(byte flag, ref double[] negative, ref double[] positive);

Exemplo de Código para Definição de Limites do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] plimit = { 170.0f, 80.0f, 150.0f, 80.0f, 170.0f, 160.0f };
        robot.SetLimitPositive(plimit);
        double[] nlimit = { -170.0f, -260.0f, -150.0f, -260.0f, -170.0f, -160.0f };
        robot.SetLimitNegative(nlimit);

        double[] neg_deg = new double[6] {0,0,0,0,0,0 };
        double[] pos_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        robot.GetJointSoftLimitDeg(0, ref neg_deg,ref pos_deg);
        Console.WriteLine($"neg limit deg:{neg_deg[0]},{neg_deg[1]},{neg_deg[2]},{neg_deg[3]},{neg_deg[4]},{neg_deg[5]}");
        Console.WriteLine($"pos limit deg:{pos_deg[0]},{pos_deg[1]},{pos_deg[2]},{pos_deg[3]},{pos_deg[4]},{pos_deg[5]}");
    }

Definir Método de Deteção de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define o método de deteção de colisão do robô
    * @param  [in] method  Método de deteção de colisão: 0-modo de corrente; 1-duplo encoder; 2-corrente e duplo encoder ativados simultaneamente
    * @param [in] thresholdMode Modo do limiar de nível de colisão; 0-modo de limiar fixo do nível de colisão; 1-limiar de deteção de colisão personalizado
    * @return   Código de erro
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode=0);

Ativar/Desativar Deteção de Colisão em Estática
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativa ou desativa a deteção de colisão em estática
    * @param  [in] status 0-desativar; 1-ativar
    * @return   Código de erro
    */
    int SetStaticCollisionOnOff(int status);

Exemplo de Código para Definição do Método de Deteção de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        int rtn = robot.SetCollisionDetectionMethod(0, 0);

        rtn = robot.SetStaticCollisionOnOff(1);
        Console.WriteLine($"SetStaticCollisionOnOff On rtn is {rtn}");
        Thread.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        Console.WriteLine($"SetStaticCollisionOnOff Off rtn is {rtn}");
    }

Deteção de Torque e Potência das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Deteção de torque e potência das juntas
    * @param  [in] status 0-desativar; 1-ativar
    * @param  [in] power  Potência máxima definida (W)
    * @return   Código de erro
    */
    int SetPowerLimit(int status, double power);

Exemplo de Código para Deteção de Torque e Potência das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }

Definir Parâmetros de Velocidade Segura
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define os parâmetros de velocidade segura
    * @param [in] enable 0-desativar; 1-ativar no modo manual; 2-ativar em todos os modos (limitação automática de velocidade não suportada)
    * @param [in] maxTCPVel  Limitar a velocidade máxima do TCP;[0-1000]mm/s
    * @param [in] strategy  Estratégia após excesso de velocidade; 0-parar com alarme; 1-limitação automática de velocidade; 2-parar com alarme e desativar
    * @return  Código de erro
    */
    public int SetVelReducePara(int enable, double maxTCPVel, int strategy)

Exemplo de Código SDK para Definir Parâmetros de Velocidade Segura
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int TestSetVelReducePara()
    {
        int rtn = 0;
        JointPos j1 = new JointPos(0, -90, 90, 0, 0, 0);
        JointPos j2 = new JointPos(90, -90, 90, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        robot.SetSpeed(80);

        // Testar parâmetro inválido
        rtn = robot.SetVelReducePara(2, 30, 1);
        Console.WriteLine($"SetVelReducePara param error rtn is {rtn}");

        // Desativar redução de velocidade
        rtn = robot.SetVelReducePara(0, 30, 1);
        Console.WriteLine($"SetVelReducePara disable reduce vel rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // Ativar redução de velocidade (modo manual)
        rtn = robot.SetVelReducePara(1, 30, 1);
        Console.WriteLine($"SetVelReducePara reduce vel rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // Ativar em todos os modos, estratégia de parar com alarme e desativar
        rtn = robot.SetVelReducePara(2, 30, 2);
        Console.WriteLine($"SetVelReducePara disable robot rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        Thread.Sleep(2000);
        robot.ResetAllError();
        robot.RobotEnable(1);
        Thread.Sleep(1000);

        // Ativar em todos os modos, estratégia de parar com alarme (parâmetros normais)
        rtn = robot.SetVelReducePara(2, 30, 0);
        Console.WriteLine($"SetVelReducePara report error rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        Thread.Sleep(1000);
        return 0;
    }