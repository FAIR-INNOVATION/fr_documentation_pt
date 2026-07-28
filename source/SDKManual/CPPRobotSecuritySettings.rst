Configurações de Segurança do Robô
=================================================

.. toctree:: 
    :maxdepth: 5

Definir Nível de Colisão
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o nível de colisão
    * @param  [in]  mode  0-nível, 1-porcentagem
    * @param  [in]  level Limiar de colisão, faixa do nível [], faixa da porcentagem [0~1]
    * @param  [in]  config 0-não atualizar arquivo de configuração, 1-atualizar arquivo de configuração
    * @return  Código de erro
    */
    errno_t  SetAnticollision(int mode, float level[6], int config);

Definir Estratégia Pós-Colisão
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  Define a estratégia pós-colisão
	 * @param  [in] strategy  0-reportar erro e pausar; 1-continuar executando; 2-reportar erro e parar; 3-modo de torque gravitacional; 4-modo de resposta oscilatória; 5-modo de ricochete pós-colisão 
	 * @param  [in] safeTime  Tempo de parada segura [1000 - 2000] ms
	 * @param  [in] safeDistance  Distância de parada segura [1-150] mm
	 * @param  [in] safetyMargin  Fator de segurança j1-j6 [1-10]
	 * @return  Código de erro
	 */
	errno_t SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]);

Início da Função de Limite de Detecção de Colisão Personalizado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

	 /**
	 * @brief  Início da função de limite de detecção de colisão personalizado. Define os limites de detecção de colisão para as juntas e o TCP.
	 * @param  [in] flag 1-ativa apenas detecção de juntas; 2-ativa apenas detecção de TCP; 3-ativa detecção de juntas e TCP simultaneamente
	 * @param  [in] jointDetectionThreshould Limiares de detecção de colisão das juntas j1-j6
	 * @param  [in] tcpDetectionThreshould Limiares de detecção de colisão do TCP, xyzabc
	 * @param  [in] block 0-não bloqueante; 1-bloqueante
	 * @return  Código de erro
	 */
	errno_t CustomCollisionDetectionStart(int flag, double jointDetectionThreshould[6], double tcpDetectionThreshould[6], int block);

Fim da Função de Limite de Detecção de Colisão Personalizado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  Desativa a função de limite de detecção de colisão personalizado
	 * @return  Código de erro
	 */
	errno_t CustomCollisionDetectionEnd();

Exemplo de Código para Configuração do Nível de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestCollision(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         int mode = 0;
         int config = 1;
         float level1[6] = { 1.0,2.0,3.0,4.0,5.0,6.0 };
         float level2[6] = { 50.0,20.0,30.0,40.0,50.0,60.0 };
         rtn = robot.SetAnticollision(mode, level1, config);
         printf("SetAnticollision mode 0 rtn is %d\n", rtn);
         mode = 1;
         rtn = robot.SetAnticollision(mode, level2, config);
         printf("SetAnticollision mode 1 rtn is %d\n", rtn);
         JointPos p1Joint(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos p2Joint(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0.0, 0.0, 0.0, 0.0);
         DescPose offdese(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
         robot.MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, 2, &exaxisPos, 0, 0, &offdese);
         robot.ResetAllError();
         int safety[6] = { 5,5,5,5,5,5 };
         rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
         printf("SetCollisionStrategy rtn is %d\n", rtn);
         double jointDetectionThreshould[6] = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
         double tcpDetectionThreshould[6] = { 60,60,60,60,60,60 };
         rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
         cout << "CustomCollisionDetectionStart rtn is " << rtn << endl;
         robot.MoveL(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
         robot.MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
         rtn = robot.CustomCollisionDetectionEnd();
         cout << "CustomCollisionDetectionEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

Definir Limite Positivo
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o limite positivo
    * @param  [in] limit Posições das seis juntas, unidade deg
    * @return  Código de erro
    */
    errno_t  SetLimitPositive(float limit[6]);

Definir Limite Negativo
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o limite negativo
    * @param  [in] limit Posições das seis juntas, unidade deg
    * @return  Código de erro
    */
    errno_t  SetLimitNegative(float limit[6]);   

Obter Ângulos dos Limites Flexíveis das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém os ângulos dos limites flexíveis das juntas
    * @param  [in] flag 0-bloqueante, 1-não bloqueante    
    * @param  [out] negative  Ângulo do limite negativo, unidade deg
    * @param  [out] positive  Ângulo do limite positivo, unidade deg
    * @return  Código de erro
    */
    errno_t  GetJointSoftLimitDeg(uint8_t flag, float negative[6], float positive[6]);
    
Exemplo de Código para Configuração de Limites do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLimit(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      float plimit[6] = { 170.0,80.0,150.0,80.0,170.0,160.0 };
      robot.SetLimitPositive(plimit);
      float nlimit[6] = { -170.0,-260.0,-150.0,-260.0,-170.0,-160.0 };
      robot.SetLimitNegative(nlimit);
      float neg_deg[6] = { 0.0 }, pos_deg[6] = { 0.0 };
      robot.GetJointSoftLimitDeg(0, neg_deg, pos_deg);
      printf("neg limit deg:%f,%f,%f,%f,%f,%f\n", neg_deg[0], neg_deg[1], neg_deg[2], neg_deg[3], neg_deg[4], neg_deg[5]);
      printf("pos limit deg:%f,%f,%f,%f,%f,%f\n", pos_deg[0], pos_deg[1], pos_deg[2], pos_deg[3], pos_deg[4], pos_deg[5]);
      robot.CloseRPC();
      return 0;
    }

Definir Método de Detecção de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o método de detecção de colisão do robô
    * @param [in] method Método de detecção de colisão: 0-modo corrente; 1-duplo encoder; 2-corrente e duplo encoder simultaneamente
    * @param [in] thresholdMode Modo de limiar do nível de colisão; 0-modo de limiar fixo do nível de colisão; 1-limite de detecção de colisão personalizado
    * @return  Código de erro
    */
    errno_t SetCollisionDetectionMethod(int method, int thresholdMode = 0);

Ativar/Desativar Detecção de Colisão Estática
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Ativa/desativa a detecção de colisão estática
     * @param [in] status 0-desativar; 1-ativar
     * @return Código de erro
     */
    errno_t SetStaticCollisionOnOff(int status);

Exemplo de Código para Definir Método de Detecção de Colisão do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestCollisionMethod(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      rtn = robot.SetCollisionDetectionMethod(0, 0);
      printf("SetCollisionDetectionMethod rtn is %d\n", rtn);
      rtn = robot.SetStaticCollisionOnOff(1);
      printf("SetStaticCollisionOnOff On rtn is %d\n", rtn);
      rtn = robot.Sleep(5000);
      rtn = robot.SetStaticCollisionOnOff(0);
      printf("SetStaticCollisionOnOff Off rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Detecção de Potência do Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Detecção de potência do torque das juntas
     * @param [in] status 0-desativar; 1-ativar
     * @param [in] power Potência máxima definida (W);
     * @return Código de erro
     */
    errno_t SetPowerLimit(int status, double power);

Exemplo de Código para Detecção de Potência do Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestPowerLimit(void)
    {
       ROBOT_STATE_PKG pkg = {};
       FRRobot robot;
       robot.LoggerInit();
       robot.SetLoggerLevel(1);
       int rtn = robot.RPC("192.168.58.2");
       if (rtn != 0)
       {
          return -1;
       }
       robot.SetReConnectParam(true, 30000, 500);
       robot.DragTeachSwitch(1);
       robot.SetPowerLimit(1, 200);
       float torques[] = { 0, 0, 0, 0, 0, 0 };
       robot.GetJointTorques(1, torques);
       int count = 100;
       robot.ServoJTStart(); 
       int error = 0;
       while (count > 0)
       {
          error = robot.ServoJT(torques, 0.001);
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
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros de velocidade de segurança
    * @param [in] enable 0-desabilitado; 1-habilitado no modo manual; 2-habilitado em todos os modos
    * @param [in] maxTCPVel Limite máximo de velocidade TCP; [0-1000] mm/s
    * @param [in] strategy Estratégia pós-excesso de velocidade; 0-parar e alarmar; 1-limitação automática de velocidade; 2-parar e alarmar com desabilitação
    * @param [in] maxJointVel Velocidade máxima para 6 juntas (°/s), padrão 45°/s
    * @return Código de erro
    */
    errno_t SetVelReducePara(int enable, double maxTCPVel, int strategy, std::vector<double> maxJointVel = {45.0, 45.0, 45.0, 45.0, 45.0, 45.0});
        
Exemplo de Código SDK para Definir Parâmetros de Velocidade Segura
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSetVelReducePara()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        JointPos j1(0, -90, 90, 0, 0, 0);
        JointPos j2(90, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        robot.SetSpeed(80);
        rtn = robot.SetVelReducePara(2, 30, 1);
        printf("SetVelReducePara param error rtn is %d\n", rtn);
        rtn = robot.SetVelReducePara(0, 30, 1);
        printf("SetVelReducePara disable reduce vel rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        rtn = robot.SetVelReducePara(1, 30, 1);
        printf("SetVelReducePara reduce vel rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        rtn = robot.SetVelReducePara(2, 30, 2);
        printf("SetVelReducePara disable robot rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(2000);
        robot.ResetAllError();
        robot.RobotEnable(1);
        robot.Sleep(1000);
        rtn = robot.SetVelReducePara(2, 30, 0);
        printf("SetVelReducePara report error rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

Exemplo de Código para Definir a Velocidade de Segurança das Juntas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:    

    int TestSetJointVelReducePara()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        JointPos j1(10.220, -11.121, -118.086, -46.739, 82.036, 131.503);
        JointPos j2(89.782, -11.122, -118.086, -46.740, 82.036, 131.504);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        robot.SetSpeed(20);

        std::vector<double> maxJointVelA = {100.0, 100.0, 100.0, 100.0, 100.0, 100.0 };
        rtn = robot.SetVelReducePara(2, 200, 0, maxJointVelA);
        printf("SetVelReducePara param error rtn is %d\n", rtn);
        robot.MoveJ(&j1, 1, 2, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 1, 2, 100, 100, 100, &epos, -1, 0, &offset_pos);
        std::vector<double> maxJointVelB = { 20.0, 20.0, 20.0, 20.0, 20.0, 20.0 };
        rtn = robot.SetVelReducePara(2, 200, 0, maxJointVelB);
        printf("SetVelReducePara reduce vel rtn is %d\n", rtn);
        robot.MoveJ(&j1, 1, 2, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 1, 2, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(2000);
        robot.CloseRPC();
        return 0;
    }    