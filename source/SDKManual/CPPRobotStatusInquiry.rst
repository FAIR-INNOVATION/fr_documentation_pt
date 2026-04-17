Consulta de Estado do Robô
==============================

.. toctree::
    :maxdepth: 5

Obter Posição Articular Atual (graus)
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a posição articular atual (graus)
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] jPos Posições das seis juntas, em graus
    * @return  Código de erro
    */
    errno_t GetActualJointPosDegree(uint8_t flag, JointPos *jPos);

Obter Velocidade de Feedback Articular
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade de feedback articular - graus/s
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] speed Velocidades das seis juntas
     * @return  Código de erro
     */
    errno_t GetActualJointSpeedsDegree(uint8_t flag, float speed[6]);

Obter Aceleração de Feedback Articular
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a aceleração de feedback articular - graus/s^2
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] acc Acelerações das seis juntas
     * @return  Código de erro
     */
    errno_t GetActualJointAccDegree(uint8_t flag, float acc[6]);

Obter Velocidade de Comando TCP - Velocidade Resultante
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade de comando TCP - velocidade resultante
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] tcp_speed Velocidade linear
     * @param  [out] ori_speed Velocidade de orientação
     * @return  Código de erro
     */
    errno_t GetTargetTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

Obter Velocidade de Feedback TCP - Velocidade Resultante
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade de feedback TCP - velocidade resultante
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] tcp_speed Velocidade linear
     * @param  [out] ori_speed Velocidade de orientação
     * @return  Código de erro
     */
    errno_t GetActualTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

Obter Velocidade de Comando TCP - Velocidades Componentes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade de comando TCP - velocidades componentes
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] speed Velocidades [x, y, z, rx, ry, rz]
     * @return  Código de erro
     */
    errno_t GetTargetTCPSpeed(uint8_t flag, float speed[6]);

Obter Velocidade de Feedback TCP - Velocidades Componentes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade de feedback TCP - velocidades componentes
     * @param  [in] flag 0-bloqueante, 1-não bloqueante
     * @param  [out] speed Velocidades [x, y, z, rx, ry, rz]
     * @return  Código de erro
     */
    errno_t GetActualTCPSpeed(uint8_t flag, float speed[6]);

Obter Pose da Ferramenta Atual
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a pose da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose da ferramenta
    * @return  Código de erro
    */
    errno_t GetActualTCPPose(uint8_t flag, DescPose *desc_pos);

Obter Número do Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o número do sistema de coordenadas da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] id Número do sistema de coordenadas da ferramenta
    * @return  Código de erro
    */
    errno_t GetActualTCPNum(uint8_t flag, int *id);

Obter Número do Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o número do sistema de coordenadas da peça atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] id Número do sistema de coordenadas da peça
    * @return  Código de erro
    */
    errno_t GetActualWObjNum(uint8_t flag, int *id);

Obter Pose do Flange da Extremidade Atual
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a pose do flange da extremidade atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do flange
    * @return  Código de erro
    */
    errno_t GetActualToolFlangePose(uint8_t flag, DescPose *desc_pos);

Obter Torque Articular Atual
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o torque articular atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] torques Torques das juntas
    * @return Código de erro
    */
    errno_t GetJointTorques(uint8_t flag, float torques[6]);

Obter Tempo do Sistema
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o tempo do sistema
    * @param [out] t_ms em ms
    * @return Código de erro
    */
    errno_t GetSystemClock(float *t_ms);

Verificar se o Movimento do Robô está Concluído
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Verifica se o movimento do robô está concluído
    * @param [out] state 0-não concluído, 1-concluído
    * @return Código de erro
    */
    errno_t GetRobotMotionDone(uint8_t *state);

Consultar o Comprimento da Fila de Cache de Movimento do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Consulta o comprimento da fila de cache de movimento do robô
     * @param [out] len Comprimento da cache
     * @return Código de erro
     */
    errno_t GetMotionQueueLength(int *len);

Obter Estado de Parada de Emergência do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado de parada de emergência do robô
    * @param [out] state Estado de parada de emergência, 0-não em parada de emergência, 1-em parada de emergência
    * @return Código de erro
    */
    errno_t GetRobotEmergencyStopState(uint8_t *state);

Obter Estado de Comunicação entre SDK e o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado de comunicação entre SDK e o robô
    * @param [out] state Estado de comunicação, 0-comunicação normal, 1-comunicação anormal
    */
    errno_t GetSDKComState(int *state);

Obter Sinal de Parada de Segurança
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sinal de parada de segurança
    * @param [out] si0_state Sinal de parada de segurança SI0, 0-inválido, 1-válido
    * @param [out] si1_state Sinal de parada de segurança SI1, 0-inválido, 1-válido
    */
    errno_t GetSafetyStopState(uint8_t *si0_state, uint8_t *si1_state);

Obter Temperatura do Driver Articular do Robô (°C)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a temperatura do driver articular do robô (°C)
    * @return Código de erro
    */
    errno_t GetJointDriverTemperature(double temperature[]);

Obter Torque do Driver Articular do Robô (Nm)
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o torque do driver articular do robô (Nm)
    * @return Código de erro
    */
    errno_t GetJointDriverTorque(double torque[]);

Obter Estrutura de Estado em Tempo Real do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a estrutura de estado em tempo real do robô
    * @param [out] pkg Estrutura de estado em tempo real do robô
    * @return Código de erro
    */
    errno_t GetRobotRealTimeState(ROBOT_STATE_PKG *pkg);

Exemplo de Código de Consulta de Estado do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestGetStatus(void)
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
      float yangle, zangle;
      robot.GetRobotInstallAngle(&yangle, &zangle);
      printf("yangle:%f,zangle:%f\n", yangle, zangle);
      JointPos j_deg = {};
      robot.GetActualJointPosDegree(0, &j_deg);
      printf("joint pos deg:%f,%f,%f,%f,%f,%f\n", j_deg.jPos[0], j_deg.jPos[1], j_deg.jPos[2], j_deg.jPos[3], j_deg.jPos[4], j_deg.jPos[5]);
      float jointSpeed[6] = { 0.0 };
      robot.GetActualJointSpeedsDegree(0, jointSpeed);
      printf("joint speeds deg:%f,%f,%f,%f,%f,%f\n", jointSpeed[0], jointSpeed[1], jointSpeed[2], jointSpeed[3], jointSpeed[4], jointSpeed[5]);
      float jointAcc[6] = { 0.0 };
      robot.GetActualJointAccDegree(0, jointAcc);
      printf("joint acc deg:%f,%f,%f,%f,%f,%f\n", jointAcc[0], jointAcc[1], jointAcc[2], jointAcc[3], jointAcc[4], jointAcc[5]);
      float tcp_speed = 0.0;
      float ori_speed = 0.0;
      robot.GetTargetTCPCompositeSpeed(0, &tcp_speed, &ori_speed);
      printf("GetTargetTCPCompositeSpeed tcp %f; ori %f\n", tcp_speed, ori_speed);
      robot.GetActualTCPCompositeSpeed(0, &tcp_speed, &ori_speed);
      printf("GetActualTCPCompositeSpeed tcp %f; ori %f\n", tcp_speed, ori_speed);
      float targetSpeed[6] = { 0.0 };
      robot.GetTargetTCPSpeed(0, targetSpeed);
      printf("GetTargetTCPSpeed %f,%f,%f,%f,%f,%f\n", targetSpeed[0], targetSpeed[1], targetSpeed[2], targetSpeed[3], targetSpeed[4], targetSpeed[5]);
      float actualSpeed[6] = { 0.0 };
      robot.GetActualTCPSpeed(0, actualSpeed);
      printf("GetTargetTCPSpeed %f,%f,%f,%f,%f,%f\n", actualSpeed[0], actualSpeed[1], actualSpeed[2], actualSpeed[3], actualSpeed[4], actualSpeed[5]);
      DescPose tcp = {};
      robot.GetActualTCPPose(0, &tcp);
      printf("tcp pose:%f,%f,%f,%f,%f,%f\n", tcp.tran.x, tcp.tran.y, tcp.tran.z, tcp.rpy.rx, tcp.rpy.ry, tcp.rpy.rz);
      DescPose flange = {};
      robot.GetActualToolFlangePose(0, &flange);
      printf("flange pose:%f,%f,%f,%f,%f,%f\n", flange.tran.x, flange.tran.y, flange.tran.z, flange.rpy.rx, flange.rpy.ry, flange.rpy.rz);
      int id = 0;
      robot.GetActualTCPNum(0, &id);
      printf("tcp num:%d\n", id);
      robot.GetActualWObjNum(0, &id);
      printf("wobj num:%d\n", id);
      float jtorque[6] = { 0.0 };
      robot.GetJointTorques(0, jtorque);
      printf("torques:%f,%f,%f,%f,%f,%f\n", jtorque[0], jtorque[1], jtorque[2], jtorque[3], jtorque[4], jtorque[5]);
      float t_ms = 0.0;
      robot.GetSystemClock(&t_ms);
      printf("system clock:%f\n", t_ms);
      int config = 0;
      robot.GetRobotCurJointsConfig(&config);
      printf("joint config:%d\n", config);
      uint8_t motionDone = 0;
      robot.GetRobotMotionDone(&motionDone);
      printf("GetRobotMotionDone :%d\n", motionDone);
      int len = 0;
      robot.GetMotionQueueLength(&len);
      printf("GetMotionQueueLength :%d\n", len);
      uint8_t emergState = 0;
      robot.GetRobotEmergencyStopState(&emergState);
      printf("GetRobotEmergencyStopState :%d\n", emergState);
      int comstate = 0;
      robot.GetSDKComState(&comstate);
      printf("GetSDKComState :%d\n", comstate);
      uint8_t si0_state, si1_state;
      robot.GetSafetyStopState(&si0_state, &si1_state);
      printf("GetSafetyStopState :%d %d\n", si0_state, si1_state);
      double temp[6] = { 0.0 };
      robot.GetJointDriverTemperature(temp);
      printf("Temperature:%f,%f,%f,%f,%f,%f\n", temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]);
      double torque[6] = { 0.0 };
      robot.GetJointDriverTorque(torque);
      printf("torque:%f,%f,%f,%f,%f,%f\n", torque[0], torque[1], torque[2], torque[3], torque[4], torque[5]);
      robot.GetRobotRealTimeState(&pkg);
      robot.CloseRPC();
      return 0;
    }

Solução de Cinemática Inversa
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Solução de cinemática inversa
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] config Configuração do espaço articular, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @param [out] joint_pos Posição articular
    * @return Código de erro
    */
    errno_t GetInverseKin(int type, DescPose *desc_pos, int config, JointPos *joint_pos);

Solução de Cinemática Inversa (com posição de referência)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Solução de cinemática inversa, resolve com base na posição articular de referência especificada
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @param [out] joint_pos Posição articular
    * @return Código de erro
    */
    errno_t GetInverseKinRef(int type, DescPose *desc_pos, JointPos *joint_pos_ref, JointPos *joint_pos);

Solução de Cinemática Inversa incluindo posição do eixo estendido no espaço cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, JointPos& joint_pos);

Exemplo de Código de Solução de Cinemática Inversa incluindo posição do eixo estendido
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestInverseKinExaxis()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return 0;
        }
        robot.SetReConnectParam(true, 30000, 500);
        DescPose desc(99.957, -0.002, 29.994, -176.569, -6.757, -167.462);
        ExaxisPos exaxis(100.0, 0.0, 0.0, 0.0);
        JointPos jointPos = {};
        DescPose offsetPos = {};
        robot.GetRobotRealTimeState(&pkg);
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;
        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, jointPos);
        printf("GetInverseKinExaxis joint is %f, %f, %f, %f, %f, %f\n", jointPos.jPos[0], jointPos.jPos[1], jointPos.jPos[2], jointPos.jPos[3], jointPos.jPos[4], jointPos.jPos[5]);
        robot.ExtAxisMove(exaxis, 100, -1);
        robot.MoveJ(&jointPos, &desc, toolnum, workPcsNum, 100.0, 100.0, 100.0, &exaxis, -1, 0, &offsetPos);
        robot.CloseRPC();
        robot.Sleep(9999999);
        return 0;
    }

Verificar se a Solução de Cinemática Inversa Existe
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Solução de cinemática inversa, verifica se há solução com base na posição articular de referência especificada
    * @param [in] type 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana
    * @param [in] joint_pos_ref Posição articular de referência
    * @param [out] result 0-sem solução, 1-com solução
    * @return Código de erro
    */
    errno_t GetInverseKinHasSolution(int type, DescPose *desc_pos, JointPos *joint_pos_ref, uint8_t *result);

Solução de Cinemática Direta
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Solução de cinemática direta
    * @param [in] joint_pos Posição articular
    * @param [out] desc_pos Pose cartesiana
    * @return Código de erro
    */
    errno_t GetForwardKin(JointPos *joint_pos, DescPose *desc_pos);

Exemplo de Código de Cálculo de Cinemática Direta e Inversa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestInverseKin(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      JointPos inverseRtn = {};
      robot.GetInverseKin(0, &desc_pos1, -1, &inverseRtn);
      printf("dcs1 GetInverseKin rtn is %f %f %f %f %f %f \n", inverseRtn.jPos[0], inverseRtn.jPos[1], inverseRtn.jPos[2], inverseRtn.jPos[3], inverseRtn.jPos[4], inverseRtn.jPos[5]);
      robot.GetInverseKinRef(0, &desc_pos1, &j1, &inverseRtn);
      printf("dcs1 GetInverseKinRef rtn is %f %f %f %f %f %f \n", inverseRtn.jPos[0], inverseRtn.jPos[1], inverseRtn.jPos[2], inverseRtn.jPos[3], inverseRtn.jPos[4], inverseRtn.jPos[5]);
      uint8_t hasResut = 0;
      robot.GetInverseKinHasSolution(0, &desc_pos1, &j1, &hasResut);
      printf("dcs1 GetInverseKinRef result %d\n", hasResut);
      DescPose forwordResult = {};
      robot.GetForwardKin(&j1, &forwordResult);
      printf("jpos1 forwordResult rtn is %f %f %f %f %f %f \n", forwordResult.tran.x, forwordResult.tran.y, forwordResult.tran.z, forwordResult.rpy.rx, forwordResult.rpy.ry, forwordResult.rpy.rz);
      robot.CloseRPC();
      return 0;
    }

Consultar Dados do Ponto de Gerenciamento de Ensino do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Consulta os dados do ponto de gerenciamento de ensino do robô
     * @param [in] name Nome do ponto
     * @param [out] data Dados do ponto
     * @return Código de erro
     */
    errno_t GetRobotTeachingPoint(char name[64], float data[20]);

Obter Valores de Compensação dos Parâmetros DH do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os valores de compensação dos parâmetros DH do robô
    * @param [out] dhCompensation Valores de compensação dos parâmetros DH do robô (mm) [cmpstD1, cmpstA2, cmpstA3, cmpstD4, cmpstD5, cmpstD6]
    * @return Código de erro
    */
    errno_t GetDHCompensation(double dhCompensation[6]);

Obter Número de Série da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o número de série da caixa de controle
    * @param [out] SNCode Número de série da caixa de controle
    * @return Código de erro
    */
    errno_t GetRobotSN(std::string& SNCode);

Exemplo de Código de Consulta de Dados do Ponto de Gerenciamento de Ensino do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestGetTeachPoint(void)
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
      char name[64] = "P1";
      float data[20] = { 0 };
      rtn = robot.GetRobotTeachingPoint(name, data);
      printf(" %d name is: %s \n", rtn, name);
      for (int i = 0; i < 20; i++)
      {
        printf("data is: %f \n", data[i]);
      }
      int que_len = 0;
      rtn = robot.GetMotionQueueLength(&que_len);
      printf("GetMotionQueueLength rtn is: %d, queue length is: %d \n", rtn, que_len);
      double dh[6] = { 0 };
      int retval = 0;
      retval = robot.GetDHCompensation(dh);
      cout << "retval is: " << retval << endl;
      cout << "dh is: " << dh[0] << " " << dh[1] << " " << dh[2] << " " << dh[3] << " " << dh[4] << " " << dh[5] << endl;
      string SN = "";
      robot.GetRobotSN(SN);
      cout << "robot SN is " << SN << endl;
      robot.CloseRPC();
      return 0;
    }

Obter Sistema de Coordenadas da Ferramenta por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetToolCoordWithID(int id, DescPose& coord);

Obter Sistema de Coordenadas da Peça por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da peça por ID
    * @param [in] id Número do sistema de coordenadas da peça
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetWObjCoordWithID(int id, DescPose& coord);

Obter Sistema de Coordenadas da Ferramenta Externa por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta externa por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetExToolCoordWithID(int id, DescPose& coord);

Obter Sistema de Coordenadas do Eixo Estendido por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas do eixo estendido por ID
    * @param [in] id Número do sistema de coordenadas da ferramenta externa
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetExAxisCoordWithID(int id, DescPose& coord);

Obter Massa e Centro de Massa da Carga por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a massa e o centro de massa da carga por ID
    * @param [in] id Número da carga
    * @param [out] weight Massa da carga
    * @param [out] cog Centro de massa da carga
    * @return Código de erro
    */
    errno_t GetTargetPayloadWithID(int id, double& weight, DescTran& cog);

Obter Sistema de Coordenadas da Ferramenta Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta atual
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetCurToolCoord(DescPose& coord);

Obter Sistema de Coordenadas da Peça Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da peça atual
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetCurWObjCoord(DescPose& coord);

Obter Sistema de Coordenadas da Ferramenta Externa Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta externa atual
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetCurExToolCoord(DescPose& coord);

Obter Sistema de Coordenadas do Eixo Estendido Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas do eixo estendido atual
    * @param [out] coord Valores do sistema de coordenadas
    * @return Código de erro
    */
    errno_t GetCurExAxisCoord(DescPose& coord);

Exemplo de Código de Sistemas de Coordenadas e Carga do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    int TestCoord()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      int id = 1;
      DescPose toolCoord = {};
      DescPose extoolCoord = {};
      DescPose wobjCoord = {};
      DescPose exAxisCoord = {};
      robot.GetToolCoordWithID(id, toolCoord);
      printf("GetToolCoordWithID %d, %f %f %f %f %f %f\n", id,
        toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
        toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz);
      robot.GetWObjCoordWithID(id, wobjCoord);
      printf("GetWObjCoordWithID %d, %f %f %f %f %f %f\n", id,
        wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
        wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz);

      robot.GetExToolCoordWithID(id, extoolCoord);
      printf("GetExToolCoordWithID %d, %f %f %f %f %f %f\n", id,
        extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
        extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);

      robot.GetExAxisCoordWithID(id, exAxisCoord);
      printf("GetExAxisCoordWithID %d, %f %f %f %f %f %f\n", id,
        exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
        exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz);
      double weight = 0.0;
      DescTran cog = {};
      robot.GetTargetPayloadWithID(id, weight, cog);
      printf("GetTargetPayloadWithID %d, %f %f %f %f\n", id, weight,
        cog.x, cog.y, cog.z);
      robot.GetCurToolCoord(toolCoord);
      printf("GetCurToolCoord %f %f %f %f %f %f\n",
        toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
        toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz);
      robot.GetCurWObjCoord(wobjCoord);
      printf("GetCurWObjCoord %f %f %f %f %f %f\n",
        wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
        wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz);
      robot.GetCurExToolCoord(extoolCoord);
      printf("GetExToolCoordWithID %f %f %f %f %f %f\n",
        extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
        extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);
      robot.GetCurExAxisCoord(exAxisCoord);
      printf("GetCurExAxisCoord %f %f %f %f %f %f\n",
        exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
        exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz);
      float weightT = 0.0;
      DescTran cogT = {};
      robot.GetTargetPayload(0, &weightT);
      robot.GetTargetPayloadCog(0, &cogT);
      printf("GetTargetPayload %f %f %f %f\n", weightT,
        cogT.x, cogT.y, cogT.z);
      DescPose coordSet(0,1,2,3,4,5);
      robot.SetToolCoord(1, &coordSet, 0, 0, 1, 0);
      robot.SetWObjCoord(1, &coordSet, 0);
      robot.SetLoadWeight(1, 1.3);
      DescTran cog = {};
      cog.x = 10;
      cog.y = 20;
      cog.z = 30;
      robot.SetLoadCoord(1, &cog);
      DescPose etcp(0, 0, 100, 0, 0, 0);
      DescPose etool(0, 0, 50, 0, 0, 0);
      rtn = robot.SetExToolCoord(1, &etcp, &etool);
      printf("SetExToolCoord rtn is %d\n", rtn);
      robot.ExtAxisActiveECoordSys(1, 1, coordSet, 1);
      robot.CloseRPC();
      return 0;
    }