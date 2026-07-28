Periféricos do Robô
========================

.. toctree:: 
    :maxdepth: 5

Configurar Garra
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Configura a garra
    * @param  [in] company  Fabricante da garra, a definir
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    errno_t  SetGripperConfig(int company, int device, int softvesion, int bus);

Obter Configuração da Garra
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a configuração da garra
    * @param  [in] company  Fabricante da garra, a definir
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    errno_t  GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

Ativar Garra
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Ativa a garra
    * @param  [in] index  Número da garra
    * @param  [in] act  0-reset, 1-ativar
    * @return  Código de erro
    */
    errno_t  ActGripper(int index, uint8_t act);

Controlar Garra
++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
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
	errno_t MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block, int type, double rotNum, int rotVel, int rotTorque);



Obter Estado de Movimento da Garra
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém o estado de movimento da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] staus  0-movimento não concluído, 1-movimento concluído
     * @return  Código de erro
     */
    errno_t  GetGripperMotionDone(uint16_t *fault, uint8_t *status);

Obter Estado de Ativação da Garra
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém o estado de ativação da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] status  bit0~bit15 correspondem aos números das garras 0~15, bit=0 não ativado, bit=1 ativado
     * @return  Código de erro
     */
    errno_t  GetGripperActivateStatus(uint16_t *fault, uint16_t *status);

Obter Posição da Garra
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a posição da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] position  Porcentagem de posição, faixa 0~100%
     * @return  Código de erro
     */
    errno_t  GetGripperCurPosition(uint16_t *fault, uint8_t *position);

Obter Velocidade da Garra
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a velocidade da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] speed  Porcentagem de velocidade, faixa 0~100%
     * @return  Código de erro
     */
    errno_t  GetGripperCurSpeed(uint16_t *fault, int8_t *speed);

Obter Corrente da Garra
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a corrente da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] current  Porcentagem de corrente, faixa 0~100%
     * @return  Código de erro
     */
    errno_t  GetGripperCurCurrent(uint16_t *fault, int8_t *current);

Obter Tensão da Garra
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a tensão da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] voltage  Tensão, unidade 0.1V
     * @return  Código de erro
     */
    errno_t  GetGripperVoltage(uint16_t *fault, int *voltage);

Obter Temperatura da Garra
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Obtém a temperatura da garra
     * @param  [out] fault  0-sem erro, 1-com erro
     * @param  [out] temp  Temperatura, unidade ℃
     * @return  Código de erro
     */
    errno_t  GetGripperTemp(uint16_t *fault, int *temp);

Calcular Ponto de Pré-Captura - Visão
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o ponto de pré-captura - Visão
     * @param  [in] desc_pos  Pose cartesiana do ponto de captura
     * @param  [in] zlength  Deslocamento no eixo Z
     * @param  [in] zangle   Deslocamento de rotação em torno do eixo Z
     * @return  Código de erro 
     */
    errno_t  ComputePrePick(DescPose *desc_pos, double zlength, double zangle, DescPose *pre_pos);

Calcular Ponto de Retirada - Visão
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o ponto de retirada - Visão
     * @param  [in] desc_pos  Pose cartesiana do ponto de captura
     * @param  [in] zlength  Deslocamento no eixo Z
     * @param  [in] zangle   Deslocamento de rotação em torno do eixo Z
     * @return  Código de erro 
     */
    errno_t  ComputePostPick(DescPose *desc_pos, double zlength, double zangle, DescPose *post_pos);

Exemplo de Código para Operações com a Garra do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGripper(void)
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
      int company = 4;
      int device = 0;
      int softversion = 0;
      int bus = 2;
      int index = 2;
      int act = 0;
      int max_time = 30000;
      uint8_t block = 0;
      uint8_t status;
      uint16_t fault;
      uint16_t active_status = 0;
      uint8_t current_pos = 0;
      int8_t current = 0;
      int voltage = 0;
      int temp = 0;
      int8_t speed = 0;
      robot.SetGripperConfig(company, device, softversion, bus);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.GetGripperConfig(&company, &device, &softversion, &bus);
      printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      act = 1;
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);
      robot.GetGripperMotionDone(&fault, &status);
      printf("motion status:%u,%u\n", fault, status);
      robot.GetGripperActivateStatus(&fault, &active_status);
      printf("gripper active fault is: %u, status is: %u\n", fault, active_status);
      robot.GetGripperCurPosition(&fault, &current_pos);
      printf("fault is:%u, current position is: %u\n", fault, current_pos);
      robot.GetGripperCurCurrent(&fault, &current);
      printf("fault is:%u, current current is: %d\n", fault, current);
      robot.GetGripperVoltage(&fault, &voltage);
      printf("fault is:%u, current voltage is: %d \n", fault, voltage);
      robot.GetGripperTemp(&fault, &temp);
      printf("fault is:%u, current temperature is: %d\n", fault, temp);
      robot.GetGripperCurSpeed(&fault, &speed);
      printf("fault is:%u, current speed is: %d\n", fault, speed);
      int retval = 0;
      DescPose prepick_pose = {};
      DescPose postpick_pose = {};
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.ComputePrePick(&p1Desc, 10, 0, &prepick_pose);
      printf("ComputePrePick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z, prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);
      retval = robot.ComputePostPick(&p2Desc, -10, 0, &postpick_pose);
      printf("ComputePostPick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z, postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);
      robot.CloseRPC();
      return 0;
    }

Obter Número de Rotações da Garra Rotativa
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: Versão 3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  Obtém o número de rotações da garra rotativa
	 * @param  [out] fault  0-sem erro, 1-com erro
	 * @param  [out] num  Número de rotações
	 * @return  Código de erro
	 */
	errno_t GetGripperRotNum(uint16_t* fault, double* num);

Obter Velocidade de Rotação da Garra Rotativa
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  Obtém a velocidade de rotação da garra rotativa
	 * @param  [out] fault  0-sem erro, 1-com erro
	 * @param  [out] speed  Porcentagem de velocidade de rotação
	 * @return  Código de erro
	 */
	errno_t GetGripperRotSpeed(uint16_t* fault, int* speed);

Obter Torque de Rotação da Garra Rotativa
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  Obtém o torque de rotação da garra rotativa
	 * @param  [out] fault  0-sem erro, 1-com erro
	 * @param  [out] torque  Porcentagem de torque de rotação
	 * @return  Código de erro
	 */
	errno_t GetGripperRotTorque(uint16_t* fault, int* torque);

Exemplo de Código para Obter Estado da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestRotGripperState(void)
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
      uint16_t fault = 0;
      double rotNum = 0.0;
      int rotSpeed = 0;
      int rotTorque = 0;
      robot.GetGripperRotNum(&fault, &rotNum);
      robot.GetGripperRotSpeed(&fault, &rotSpeed);
      robot.GetGripperRotTorque(&fault, &rotTorque);
      printf("gripper rot num : %lf, gripper rotSpeed : %d, gripper rotTorque : %d\n", rotNum, rotSpeed, rotTorque);
      robot.CloseRPC();
      return 0;
    }


Iniciar/Parar Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Inicia/para a esteira transportadora
    * @param [in] status Estado, 1-iniciar, 0-parar 
    * @return Código de erro
    */
    errno_t ConveyorStartEnd(uint8_t status);

Registrar Ponto de Detecção IO
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Registra o ponto de detecção IO
    * @return Código de erro
    */
    errno_t ConveyorPointIORecord();

Registrar Ponto A
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Registra o ponto A
    * @return Código de erro
    */
    errno_t ConveyorPointARecord();

Registrar Ponto de Referência
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Registra o ponto de referência
    * @return Código de erro
    */
    errno_t ConveyorRefPointRecord();

Registrar Ponto B
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Registra o ponto B
    * @return Código de erro
    */
    errno_t ConveyorPointBRecord();

Detecção IO de Peça na Esteira
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Detecção IO de peça na esteira
    * @param [in] max_t Tempo máximo de detecção, unidade ms
    * @return Código de erro
    */
    errno_t ConveyorIODetect(int max_t);

Obter Posição Atual do Objeto
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a posição atual do objeto
    * @param [in] mode 
    * @return Código de erro
    */
    errno_t ConveyorGetTrackData(int mode);

Iniciar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Inicia o rastreamento da esteira
    * @param [in] status Estado, 1-iniciar, 0-parar 
    * @return Código de erro
    */
    errno_t ConveyorTrackStart(uint8_t status);

Parar Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Para o rastreamento da esteira
    * @return Código de erro
    */
    errno_t ConveyorTrackEnd();

Configurar Parâmetros da Esteira
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Configura os parâmetros da esteira
    * @param [in] para[0] Canal do encoder 1~2
    * @param [in] para[1] Número de pulsos do encoder por rotação
    * @param [in] para[2] Distância percorrida pela esteira por rotação do encoder
    * @param [in] para[3] Número do sistema de coordenadas da peça (para movimento de rastreamento, escolha o número do sistema de coordenadas; para captura com rastreamento e rastreamento TPD, defina como 0)
    * @param [in] para[4] Se usa visão 0-não usa 1-usa
    * @param [in] para[5] Relação de velocidade (para a opção de captura com rastreamento da esteira [1-100]; para outras opções, padrão 1)
    * @return Código de erro
    */
    errno_t ConveyorSetParam(float para[6], int followType = 0, int startDis = 0, int endDis = 100);

Compensação do Ponto de Captura da Esteira
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief Compensação do ponto de captura da esteira
	 * @param [in] cmp Compensação de posição double[3]{x, y, z}
	 * @return Código de erro
	 */
    errno_t ConveyorCatchPointComp(double cmp[3]);

Movimento Linear com Rastreamento da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento linear com rastreamento da esteira
    * @param [in] status Estado, 1-iniciar, 0-parar 
    * @return Código de erro
    */
    errno_t TrackMoveL(char name[32], int tool, int wobj, float vel, float acc, float ovl, float blendR, uint8_t flag, uint8_t type);

Detecção de Entrada de Comunicação da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Detecção de entrada de comunicação da esteira
    * @param [in] timeout Tempo limite de espera ms
    * @return Código de erro
    */
    errno_t ConveyorComDetect(int timeout);

Acionamento da Detecção de Entrada de Comunicação da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Acionamento da detecção de entrada de comunicação da esteira
    * @return Código de erro
    */
    errno_t ConveyorComDetectTrigger();

Exemplo de Programa de Operação da Esteira do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestConveyor(void)
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
      int retval = 0;
      retval = robot.ConveyorStartEnd(1);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = robot.ConveyorPointIORecord();
      printf("ConveyorPointIORecord retval is: %d\n", retval);
      retval = robot.ConveyorPointARecord();
      printf("ConveyorPointARecord retval is: %d\n", retval);
      retval = robot.ConveyorRefPointRecord();
      printf("ConveyorRefPointRecord retval is: %d\n", retval);
      retval = robot.ConveyorPointBRecord();
      printf("ConveyorPointBRecord retval is: %d\n", retval);
      retval = robot.ConveyorStartEnd(0);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = 0;
      float param[6] = { 1,10000,200,0,0,20 };
      retval = robot.ConveyorSetParam(param);
      printf("ConveyorSetParam retval is: %d\n", retval);
      double cmp[3] = { 0.0, 0.0, 0.0 };
      retval = robot.ConveyorCatchPointComp(cmp);
      printf("ConveyorCatchPointComp retval is: %d\n", retval);
      int index = 1;
      int max_time = 30000;
      uint8_t block = 0;
      retval = 0;
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.MoveCart(&p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      printf("MoveCart retval is: %d\n", retval);
      retval = robot.WaitMs(1);
      printf("WaitMs retval is: %d\n", retval);
      retval = robot.ConveyorIODetect(10000);
      printf("ConveyorIODetect retval is: %d\n", retval);
      retval = robot.ConveyorGetTrackData(1);
      printf("ConveyorGetTrackData retval is: %d\n", retval);
      retval = robot.ConveyorTrackStart(1);
      printf("ConveyorTrackStart retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.ConveyorTrackEnd();
      printf("ConveyorTrackEnd retval is: %d\n", retval);
      robot.MoveCart(&p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      rtn = robot->ConveyorComDetect(1000 * 10);
      printf("ConveyorComDetect rtn is: %d\n", rtn);
      robot.Sleep(2000);
      rtn = robot->ConveyorComDetectTrigger();
      printf("ConveyorComDetectTrigger rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Configuração de Parâmetros de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.9.8
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Configura os parâmetros de rastreamento em posição da esteira transportadora
    * @param [in] trackMode 0-tempo; 1-distância; 2-tempo e distância, qualquer condição satisfeita
    * @param [in] trackTime Tempo de rastreamento, unidade s
    * @param [in] trackDis Distância de rastreamento, unidade mm
    * @return Código de erro
    */
    int SetStationaryTrackPara(int trackMode, double trackTime, int trackDis);
    
Exemplo de Código de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.9.8
    
.. code-block:: c++
    :linenos:

    int TestStationaryTrack()
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
        printf("\n========== Teste de Rastreamento Estacionário da Esteira ==========");
        JointPos j1(-35.146, -102.684, 120.805, -100.401, -90.295, 150.105);
        DescPose d1(-121.814, -348.341, 209.978, -173.152, -3.585, -5.446);
        ExaxisPos ex(0, 0, 0, 0);
        DescPose zeroOff(0, 0, 0, 0, 0, 0);
        int tool = 1;
        int workpiece = 1;
        float conveyorParam[6] = { 0, 10000, 200, 0, 0, 10 };
        rtn = robot.ConveyorSetParam(conveyorParam);
        robot.MoveJ(&j1, &d1, tool, workpiece, 100, 100, 100, &ex, -1, 0, &zeroOff);
        // Step 1: Sinal de controle SetDO
        printf("--- Step 1: SetDO(6,1) ---\n");
        rtn = robot.SetDO(6, 1, 0, 0);
        printf("  SetDO(6,1) rtn={0}\n", rtn);
        // Step 2: Início do rastreamento da esteira
        printf("--- Step 2: ConveyorTrackStart(2) ---\n");
        rtn = robot.ConveyorTrackStart(2);
        printf("  ConveyorTrackStart(2) rtn={0}\n", rtn);
        // Step 3: Detecção IO da peça
        printf("--- Step 3: ConveyorIODetect(10000) ---\n");
        rtn = robot.ConveyorIODetect(10000);
        printf("  ConveyorIODetect(10000) rtn={0}\n", rtn);
        // Step 4: Obter dados de rastreamento
        printf("--- Step 4: ConveyorGetTrackData(2) ---\n");
        rtn = robot.ConveyorGetTrackData(2);
        printf("  ConveyorGetTrackData(2) rtn={0}\n", rtn);
        // Step 5: Configuração de parâmetros de rastreamento estacionário (modo tempo, 200s, distância 5)
        printf("--- Step 5: SetStationaryTrackPara(0,200,5) ---\n");
        rtn = robot.SetStationaryTrackPara(0, 5, 5);
        printf("  SetStationaryTrackPara(0,200,5) rtn={0}\n", rtn);
        // Step 6: Executar movimento de rastreamento estacionário
        printf("--- Step 6: MoveStationary() ---\n");
        rtn = robot.MoveStationary();
        rtn = robot.WaitStationaryMotionDone();
        printf("  MoveStationary() rtn={0}\n", rtn);
        // Step 7: Fim do rastreamento da esteira
        printf("--- Step 7: ConveyorTrackEnd() ---\n");
        rtn = robot.ConveyorTrackEnd();
        printf("  ConveyorTrackEnd() rtn={0}\n", rtn);
        // Step 8: Sinal de desligamento SetDO
        printf("--- Step 8: SetDO(6,0) ---\n");
        rtn = robot.SetDO(6, 0, 0, 0);
        printf("  SetDO(6,0) rtn={0}\n", rtn);
        printf("\n========== Teste de Rastreamento Estacionário Concluído ==========\n");
        return 0;
    }

Configurar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Configura o sensor de extremidade
    * @param [in] idCompany Fabricante, 18-JUNKONG；25-HUIDE
    * @param [in] idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
    * @param [in] idSoftware Versão do software, 0-J1.0/HuiDe1.0 (temporariamente não disponível)
    * @param [in] idBus Posição de montagem, 1-porta 1 da extremidade; 2-porta 2 da extremidade...8-porta 8 da extremidade (temporariamente não disponível)
    * @return Código de erro
    */
    errno_t AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

Obter Configuração do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém a configuração do sensor de extremidade
     * @param [out] idCompany Fabricante, 18-JUNKONG；25-HUIDE
     * @param [out] idDevice Tipo, 0-JUNKONG/RYR6T.V1.0
     * @return Código de erro
     */
    errno_t AxleSensorConfigGet(int& idCompany, int& idDevice);

Ativar Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Ativa o sensor de extremidade
     * @param [in] actFlag 0-reset; 1-ativar
     * @return Código de erro
     */
    errno_t AxleSensorActivate(int actFlag);

Escrita no Registrador do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Escrita no registrador do sensor de extremidade
     * @param [in] devAddr Endereço do dispositivo 0-255
     * @param [in] regHAddr 8 bits altos do endereço do registrador
     * @param [in] regLAddr 8 bits baixos do endereço do registrador
     * @param [in] regNum Número de registradores 0-255
     * @param [in] data1 Valor 1 a ser escrito no registrador
     * @param [in] data2 Valor 2 a ser escrito no registrador
     * @param [in] isNoBlock 0-bloqueado; 1-não bloqueado
     * @return Código de erro
     */
    errno_t AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

Exemplo de Código do Sensor de Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestAxleSensor(void)
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
      robot.AxleSensorConfig(18, 0, 0, 1);
      int company = -1;
      int type = -1;
      robot.AxleSensorConfigGet(company, type);
      printf("company is %d, type is %d\n", company, type);
      rtn = robot.AxleSensorActivate(1);
      printf("AxleSensorActivate rtn is %d\n", rtn);
      robot.Sleep(1000);
      rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
      printf("AxleSensorRegWrite rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }
        
Obter Protocolo de Periféricos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o protocolo de periféricos do robô
    * @param [out] protocol Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster
    * @return Código de erro
    */
    errno_t GetExDevProtocol(int *protocol);

Definir Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o protocolo de periféricos do robô
    * @param [in] protocol Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster
    * @return Código de erro
    */
    errno_t SetExDevProtocol(int protocol);

Exemplo de Programa para Definir Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    int TestExDevProtocol(void)
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
      int protocol = 4096;
      rtn = robot.SetExDevProtocol(protocol);
      std::cout << "SetExDevProtocol rtn " << rtn << std::endl;
      rtn = robot.GetExDevProtocol(&protocol);
      std::cout << "GetExDevProtocol rtn " << rtn << " protocol is: " << protocol << std::endl;
      robot.CloseRPC();
      return 0;
    }

Obter Parâmetros de Comunicação da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os parâmetros de comunicação da extremidade
    * @param param Parâmetros de comunicação da extremidade
    * @return  Código de erro
    */
    errno_t GetAxleCommunicationParam(AxleComParam* param);

Definir Parâmetros de Comunicação da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros de comunicação da extremidade
    * @param param  Parâmetros de comunicação da extremidade
    * @return  Código de erro
    */
    errno_t SetAxleCommunicationParam(AxleComParam param);

Definir Tipo de Transferência de Arquivo da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o tipo de transferência de arquivo da extremidade
    * @param type 1-arquivo de atualização MCU; 2-arquivo LUA
    * @return  Código de erro
    */
    errno_t SetAxleFileType(int type);

Ativar Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Ativa a execução LUA na extremidade
    * @param enable 0-desativar; 1-ativar
    * @return  Código de erro
    */
    errno_t SetAxleLuaEnable(int enable);

Recuperação de Erro de Arquivo LUA na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Recuperação de erro de arquivo LUA na extremidade
    * @param status 0-não recuperar; 1-recuperar
    * @return  Código de erro
    */
    errno_t SetRecoverAxleLuaErr(int status);

Recuperação de Erro de Arquivo LUA na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado de ativação da execução LUA na extremidade
    * @param status status[0]: 0-desativado; 1-ativado
    * @return  Código de erro
    */
    errno_t GetAxleLuaEnableStatus(int status[]);

Definir os tipos de dispositivo de extremidade habilitados para LUA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os tipos de dispositivo de extremidade habilitados para o LUA
    * @param forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    * @param gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
    * @param IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    * @param dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
    * @return  Código de erro
    */
    errno_t SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable, int dexhandEnable);

Obter os tipos de dispositivo de extremidade habilitados para LUA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:
        
    /**
    * @brief Obtém os tipos de dispositivo de extremidade habilitados para o LUA
    * @param enable enable[0]:forceSensorEnable Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    * @param enable enable[1]:gripperEnable Status de habilitação da garra, 0-desabilitado; 1-habilitado
    * @param enable enable[2]:IOEnable Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    * @param enable enable[3]:dexhandEnable Status de habilitação da mão destra, 0-desabilitado; 1-habilitado
    * @return Código de erro
    */
    errno_t GetAxleLuaEnableDeviceType(int* forceSensorEnable, int* gripperEnable, int* IOEnable, int* dexhandEnable);

Obter os dispositivos de extremidade atualmente configurados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os dispositivos de extremidade atualmente configurados
    * @param [out] forceSensorEnable Número do dispositivo de sensor de força habilitado, 0-desabilitado; 1-habilitado
    * @param [out] gripperEnable Número do dispositivo de garra habilitado, 0-desabilitado; 1-habilitado
    * @param [out] IODeviceEnable Número do dispositivo IO habilitado, 0-desabilitado; 1-habilitado
    * @param [out] decHandEnable Número do dispositivo de mão destra habilitado, 0-desabilitado; 1-habilitado
    * @return Código de erro
    */
    errno_t GetAxleLuaEnableDevice(int forceSensorEnable[], int gripperEnable[], int IODeviceEnable[], int decHandEnable[]);

Definir as funções de controle de ação da garra habilitadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
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
    errno_t SetAxleLuaGripperFunc(int id, int func[32]);

Obter as funções de controle de ação da garra habilitadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
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
    errno_t GetAxleLuaGripperFunc(int id, int func[32]);

Escrita de Arquivo no Escravo Ethercat do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Escrita de arquivo no escravo Ethercat do robô
    * @param type Tipo de arquivo do escravo, 1-arquivo de atualização do escravo; 2-arquivo de configuração do escravo
    * @param slaveID Número do escravo
    * @param fileName Nome do arquivo a ser enviado
    * @return  Código de erro
    */
    errno_t SlaveFileWrite(int type, int slaveID, std::string fileName);

Enviar Arquivo de Protocolo Aberto LUA da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Envia arquivo de protocolo aberto LUA da extremidade
    * @param filePath Caminho do arquivo lua local ".../AXLE_LUA_End_DaHuan.lua"
    * @return Código de erro
    */
    errno_t AxleLuaUpload(std::string filePath);

Entrar no Modo Boot do Escravo Ethercat do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Entrar no modo boot do escravo Ethercat do robô
    * @return  Código de erro
    */
    errno_t SetSysServoBootMode();

Exemplo de Código para Operações com Arquivos LUA da Extremidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAxleLua(void)
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
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");
        AxleComParam param(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);
        AxleComParam getParam;
        robot.GetAxleCommunicationParam(&getParam);
        printf("GetAxleCommunicationParam param is %d %d %d %d %d %d %d\n", getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify, getParam.timeout, getParam.timeoutTimes, getParam.period);
        robot.SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot.GetAxleLuaEnableStatus(&luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0, 0);
        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int dexhandEnable = 0;
        robot.GetAxleLuaEnableDeviceType(&forceEnable, &gripperEnable, &ioEnable, &dexhandEnable);
        printf("GetAxleLuaEnableDeviceType param is %d %d %d %d\n", forceEnable, gripperEnable, ioEnable, dexhandEnable);
        int func[32] = { 0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
        rtn = robot.SetAxleLuaGripperFunc(2, func);
        printf("SetAxleLuaGripperFunc rtn is %d\n", rtn);
        int getFunc[32] = { 0 };
        rtn = robot.GetAxleLuaGripperFunc(2, getFunc);
        printf("GetAxleLuaGripperFunc rtn is %d\n", rtn);
        int getforceEnable[16] = { 0 };
        int getgripperEnable[16] = { 0 };
        int getioEnable[16] = { 0 };
        int dexhandEnable1[16] = { 0 };
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable, dexhandEnable1);
        printf("\ngetforceEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getforceEnable[i]);
        }
        printf("\ngetgripperEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getgripperEnable[i]);
        }
        printf("\ngetioEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getioEnable[i]);
        }
        printf("\n");
        robot.ActGripper(2, 0);
        robot.Sleep(2000);
        robot.ActGripper(2, 1);
        robot.Sleep(2000);
        robot.MoveGripper(2, 1, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            robot.GetRobotRealTimeState(&pkg);
            printf("gripper pos is %u\n", pkg.gripper_position);
            robot.Sleep(100);
        }
        robot.CloseRPC();
        return 0;
    }

Obter Estado dos Botões do SmartTool
++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado dos botões do SmartTool
    * @param [out] state Estado dos botões do SmartTool; (bit0:0-comunicação normal; 1-comunicação perdida; bit1-operação de desfazer; bit2-limpar programa;
    bit3-tecla A; bit4-tecla B; bit5-tecla C; bit6-tecla D; bit7-tecla E; bit8-tecla IO; bit9-manual/automático; bit10-iniciar)
    * @return Código de erro
    */
    errno_t GetSmarttoolBtnState(int& state);
    
Exemplo de Código do Botão SmartTool
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int main(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;

      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      robot.SetReConnectParam(true, 30000, 500);

      while (true)
      {
        int btn = 0;
        robot.GetSmarttoolBtnState(btn);
        cout << "smarttool " << std::bitset<sizeof(btn) * 8>(btn) << endl;

        Sleep(100);
      }
    }

Controlar Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Controla a matriz de ventosas
    * @param [in] slaveID Número do escravo
    * @param [in] len Comprimento
    * @param [in] ctrlValue Valor de controle
    * @return Código de erro
    */
    errno_t FRRobot::SetSuckerCtrl(uint8_t slaveID, uint8_t len, uint8_t ctrlValue[20]);

Obter Estado da Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado da matriz de ventosas
    * @param [in] slaveID Número do escravo
    * @param [out] state Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    * @param [out] pressValue Vácuo atual unidade kPa 
    * @param [out] error Código de erro atual da ventosa
    * @return Código de erro
    */
	errno_t FRRobot::GetSuckerState(uint8_t slaveID, uint8_t* state, int* pressValue, int* error);

Aguardar Estado da Ventosa
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda o estado da ventosa
    * @param [in] slaveID Número do escravo
    * @param [in] state Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    * @param [in] ms Tempo máximo de espera
    * @return Código de erro
    */
    errno_t FRRobot::WaitSuckerState(uint8_t slaveID, uint8_t state, int ms);

Exemplo de Código para Instruções de Controle da Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testSucker()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("E://openlua/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(1, "CtrlDev_sucker.lua");
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);

        //Controlar ventosa em modo broadcast com capacidade máxima de sucção
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);

        //Monitorar estados da ventosa 1 e ventosa 12 em loop
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, &state, &pressVlaue, &error);
            printf("sucker1 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.GetSuckerState(12, &state, &pressVlaue, &error);
            printf("sucker12 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.Sleep(100);
        }

        //Aguardar ventosa 1 atingir estado de objeto aderido, tempo de espera 100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        printf("WaitSuckerState result is  %d\n", ret);

        //Modo unicast para desligar ventosas 1 e 12
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);

        robot.CloseRPC();
    }

Enviar Arquivo LUA de Protocolo Aberto de Periférico
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

	/**
	 * @brief Envia arquivo Lua
	 * @param [in] filePath Caminho do arquivo lua local
	 * @return Código de erro
	 */
    errno_t OpenLuaUpload(std::string filePath);

Obter Parâmetros da Placa Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém os parâmetros da placa escrava
    * @param  [out] type  0-Ethercat, 1-CClink, 3-Ethercat, 4-EIP
    * @param  [out] version  Versão do protocolo
    * @param  [out] connState  0-desconectado 1-conectado
    * @return  Código de erro
    */
    errno_t GetFieldBusConfig(uint8_t* type, uint8_t* version, uint8_t* connState);

Escrever DO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Escreve DO no escravo
    * @param  [in] DOIndex  Número do DO
    * @param  [in] wirteNum  Número a ser escrito
    * @param  [in] status[8] Valor a ser escrito, máximo de 8
    * @return  Código de erro
    */
    errno_t FieldBusSlaveWriteDO(uint8_t DOIndex, uint8_t wirteNum, uint8_t status[8]);

Escrever AO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Escreve AO no escravo
    * @param  [in] AOIndex  Número do AO
    * @param  [in] wirteNum  Número a ser escrito
    * @param  [in] status[8] Valor a ser escrito, máximo de 8
    * @return  Código de erro
    */
    errno_t FieldBusSlaveWriteAO(uint8_t AOIndex, uint8_t wirteNum, double status[8]);

Ler DI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Lê DI do escravo
    * @param  [in] DOIndex  Número do DI
    * @param  [in] readeNum  Número a ser lido
    * @param  [out] status[8] Valor lido, máximo de 8
    * @return  Código de erro
    */
    errno_t FieldBusSlaveReadDI(uint8_t DOIndex, uint8_t readNum, uint8_t status[8]);

Ler AI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Lê AI do escravo
    * @param  [in] AOIndex  Número do AI
    * @param  [in] readeNum  Número a ser lido
    * @param  [out] status[8] Valor lido, máximo de 8
    * @return  Código de erro
    */
    errno_t FieldBusSlaveReadAI(uint8_t AIIndex, uint8_t readNum, double status[8]);

Aguardar Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda entrada DI de extensão
    * @param [in] DIIndex Número do DI
    * @param [in] status 0-nível baixo; 1-nível alto
    * @param [in] waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    errno_t FRRobot::FieldBusSlaveWaitDI(uint8_t DIIndex, bool status, int waitMs);

Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda entrada AI de extensão
    * @param [in] AIIndex Número do AI
    * @param [in] waitType 0-maior que; 1-menor que
    * @param [in] value Valor do AI
    * @param [in] waitMs Tempo máximo de espera (ms)
    * @return Código de erro
    */
    errno_t FRRobot::FieldBusSlaveWaitAI(uint8_t AIIndex, uint8_t waitType, double value, int waitMs);

Exemplo de Código para Interfaces de Instrução do Modo Escravo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testFieldBusBoard()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t type = 0, version = 0, connState = 0;
        uint8_t ctrl[8];
        double ctrlAO[8];
        static uint8_t DI[8];
        static double AI[8];

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("E://openlua/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);

        //Obter tipo de protocolo da placa escrava, versão do software, status de conexão com CLP
        robot.GetFieldBusConfig(&type, &version, &connState);
        printf("type is %d, version is %d,connState is %d\n", type, version, connState);

        //Escrever DO0 = 1, DO1 = 0, DO2 = 1
        ctrl[0] = 0;
        ctrl[1] = 1;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);

        //Escrever AO2 = 0x1000
        ctrlAO[0] = 0x1005;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        //Monitorar DI0~DI3 AI0~AI2 em loop
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            printf("DI0 is %d, DI1 is %d,DI2 is %d,DI3 is %d\n", DI[0], DI[1], DI[2], DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            printf("AI0 is %d, AI1 is %d,AI2 is %d\n", AI[0], AI[1], AI[2]);
            robot.Sleep(10);
        }

        //Aguardar DI0 ser igual a 1, tempo de espera 100ms, imprimir resultado
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        printf("FieldBusSlaveWaitDI result is  %d\n", ret);

        //Aguardar AI0 ser maior que 400, tempo de espera 100ms, imprimir resultado
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        printf("FieldBusSlaveWaitAI result is  %d\n", ret);

        robot.CloseRPC();
    }

Ligar/Desligar Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Função para ligar/desligar periférico laser
	 * @param [in] OnOff 0-desligar 1-ligar
	 * @param [in] weldId ID da solda, padrão 0
	 * @return Código de erro
	 */
	errno_t LaserTrackingLaserOnOff(int OnOff,int weldId);
        
Iniciar/Parar Rastreamento a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Função para iniciar/parar rastreamento a laser
	 * @param [in] OnOff 0-parar 1-iniciar
	 * @param [in] coordId Número do sistema de coordenadas da ferramenta do periférico laser
	 * @return Código de erro
	 */
 	errno_t LaserTrackingTrackOnOff(int OnOff, int coordId); 
            
Início da Busca de Posição a Laser - Direção Fixa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Busca de posição a laser - Direção fixa
    * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    * @param [in] vel Velocidade unidade %
    * @param [in] distance Distância máxima de busca unidade mm
    * @param [in] distance Tempo limite de busca unidade ms
    * @param [in] posSensorNum Número do sistema de coordenadas da ferramenta calibrado para o laser
    * @return Código de erro
    */
    errno_t LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum);
                
Início da Busca de Posição a Laser - Direção Arbitrária
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Busca de posição a laser - Direção arbitrária
	 * @param [in] directionPoint Coordenadas xyz do ponto de entrada da busca
	 * @param [in] vel Velocidade unidade %
	 * @param [in] distance Distância máxima de busca unidade mm
	 * @param [in] distance Tempo limite de busca unidade ms
	 * @param [in] posSensorNum Número do sistema de coordenadas da ferramenta calibrado para o laser
	 * @return Código de erro
	 */
    errno_t LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum);
                    
Fim da Busca de Posição a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Fim da busca de posição a laser
	 * @return Código de erro
	 */
    errno_t LaserTrackingSearchStop();

Configuração de Rede do Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Configuração de rede do laser
	 * @param [in] ip Endereço IP do periférico laser
	 * @param [in] port Número da porta do periférico laser
	 * @return Código de erro
	 */
    errno_t LaserTrackingSensorConfig(std::string ip, int port);
    
Configuração do Período de Amostragem do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Configuração do período de amostragem do periférico laser
    * @param [in] period Período de amostragem do periférico laser unidade ms
    * @return Código de erro
    */
    errno_t LaserTrackingSensorSamplePeriod(int period);
        
Carregar Driver do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Carregar driver do periférico laser
	 * @param [in] type Tipo de protocolo do driver do periférico laser 101-Ruiniu 102-Chuangxiang 103-Quanshi 104-Tongzhou 105-Aotai
	 * @return Código de erro
	 */
    errno_t LoadPosSensorDriver(int type);
            
Descarregar Driver do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Descarregar driver do periférico laser
	 * @return Código de erro
	 */
    errno_t UnLoadPosSensorDriver();
                
Gravação da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Gravação da trajetória da solda a laser
    * @param [in] status 0-parar gravação 1-rastreamento em tempo real 2-iniciar gravação
    * @param [in] delayTime Tempo de atraso unidade ms
    * @return Código de erro
    */
    errno_t LaserSensorRecord1(int status, int delayTime); 
                    
Reprodução da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Reprodução da trajetória da solda a laser
	 * @param [in] delayTime Tempo de atraso unidade ms
	 * @param [in] speed Velocidade unidade %
	 * @return Código de erro
	 */
    errno_t LaserSensorReplay(int delayTime, double speed);
                        
Reprodução do Rastreamento a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief Reprodução do rastreamento a laser
	 * @return Código de erro
	 */
    errno_t MoveLTR();
                            
Gravação e Reprodução da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Gravação e reprodução da trajetória da solda a laser
    * @param [in] delayMode Modo de atraso 0-tempo de atraso 1-distância de atraso
    * @param [in] delayTime Tempo de atraso unidade ms
    * @param [in] delayDisExAxisNum Número do eixo de extensão
    * @param [in] delayDis Distância de atraso unidade mm
    * @param [in] sensitivePara Coeficiente de sensibilidade de compensação
    * @param [in] trackMode Tipo de rastreamento pontual. 0-movimento assíncrono do eixo de extensão; 1-robô
    * @param [in] triggerMode Modo de acionamento do rastreamento pontual. 0-duração do rastreamento; 1-IO
    * @param [in] runTime Duração do rastreamento pontual do robô (s)
    * @param [in] speed Velocidade unidade %
    * @return Código de erro
    */
    errno_t LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum, double delayDis, double sensitivePara, int trackMode, int triggerMode, double runTime, double speed);
                                
Mover para o Início da Gravação da Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Mover para o início da gravação da solda
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl Velocidade unidade %
    * @return Código de erro
    */
    errno_t MoveToLaserRecordStart(int moveType, double ovl);
                                    
Mover para o Fim da Gravação da Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Mover para o fim da gravação da solda
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl Velocidade unidade %
    * @return Código de erro
    */
    errno_t MoveToLaserRecordEnd(int moveType, double ovl);
                                        
Mover para o Ponto de Busca do Sensor a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
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
    errno_t MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset);
                                            
Obter Coordenadas do Ponto de Busca do Sensor a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
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
    errno_t GetLaserSeamPos(int trackOffectType, DescPose offset, JointPos& jPos, DescPose& descPos, int& tool, int& user, ExaxisPos& exaxis); 
                                                
Exemplo de Código para Configuração e Depuração de Parâmetros do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserConfig()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //Definir endereço IP e número da porta
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        //Definir período de amostragem
        robot.LaserTrackingSensorSamplePeriod(20);
        //Carregar driver
        robot.LoadPosSensorDriver(101);
        //Desligar periférico laser
        robot.LaserTrackingLaserOnOff(0,0);
        robot.Sleep(3000);
        //Ligar periférico laser
        robot.LaserTrackingLaserOnOff(1, 0);
        robot.CloseRPC();
    }
                                                    
Exemplo de Código para Digitalização e Reprodução de Trajetória a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserRecordAndReplay()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while(cnt<31)
        { 
            //Mover para o ponto inicial da digitalização
            JointPos startjointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //Iniciar gravação da trajetória
            robot.LaserSensorRecord1(2, 10);
            //Mover para o ponto final a ser gravado
            JointPos endjointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(&endjointPos, &enddescPose, 1, 0, 30, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //Parar gravação
            robot.LaserSensorRecord1(0, 10);
            //Mover para o ponto inicial da solda gravada
            robot.MoveToLaserRecordStart(1, 30);
            //Iniciar reprodução da trajetória
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            //Parar reprodução da trajetória
            robot.LaserSensorRecord1(0, 10);
            printf("Teste de estabilidade de digitalização a laser + reprodução de trajetória %d\n", cnt);
            cnt++;
        }
        robot.CloseRPC();
    }
                                                        
Exemplo de Código para Busca de Posição e Rastreamento em Tempo Real a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrack()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //Carregar e enviar arquivo de protocolo aberto
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while (cnt < 2)
        {
            //Mover para o ponto inicial da busca de posição
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            DescTran directionPoint;
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);

            //Iniciar busca de posição ao longo da direção -y
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            //Se a busca de posição for bem-sucedida
            if (ret == 0)
            {
                //Mover para o ponto de busca
                robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);
                //Iniciar rastreamento a laser ao longo do ponto de busca
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.MoveL(&endjointPos, &enddescPose, 1, 0, 20, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
                //Parar rastreamento
                robot.LaserTrackingTrackOnOff(0, 2);

            }
            cnt++;
        }
        robot.CloseRPC();
    }
                                                            
Exemplo de Código para Rastreamento a Laser Síncrono com Eixo de Extensão e Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrackandExitAxis()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        ExaxisPos startexaxisPos = { 0,0,0,0 };
        ExaxisPos seamexaxisPos = { -10,0,0,0 };
        ExaxisPos endexaxisPos = { -30, 0, 0, 0 };
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        JointPos seamjointPos(0, 0, 0, 0, 0, 0);
        DescPose seamdescPose(0, 0, 0, 0, 0, 0);
        
        int cnt = 1;
        while (cnt < 31)
        {
            //Mover para o ponto inicial da busca de posição
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);

            //Iniciar busca de posição ao longo da direção -y
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            int tool = 0;
            int user = 0;
            robot.GetLaserSeamPos(0, offdese, seamjointPos, seamdescPose, tool, user, startexaxisPos);
            printf("%f, %f, %f,%f, %f, %f,%f, %f, %f,%f, %f, %f\n", seamjointPos.jPos[0], seamjointPos.jPos[1], seamjointPos.jPos[2], seamjointPos.jPos[3], seamjointPos.jPos[4], seamjointPos.jPos[5], seamdescPose.tran.x, seamdescPose.tran.y, seamdescPose.tran.z, seamdescPose.rpy.rx, seamdescPose.rpy.ry, seamdescPose.rpy.rz);

            //Se a busca de posição for bem-sucedida
            if (ret == 0)
            {
                //Robô e eixo de extensão se movem sincronizadamente para o ponto de busca
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);

                //Iniciar rastreamento a laser ao longo do ponto de busca e movimento síncrono com o eixo de extensão
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);;
                //Parar rastreamento
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            cnt++;
            printf("Rastreamento a laser síncrono com eixo de extensão e robô %d\n", cnt);
        }
        robot.CloseRPC();
    } 
                                                            
Ativar/Desativar Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Ativa/desativa a função de passagem direta na extremidade
    * @param [in] enable, 0-desativar, 1-ativar
    * @return Código de erro
    */
    errno_t SetAxleGenComEnable(int mode);
                                                            
Transmissão e Recepção de Dados Aperiódicos na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:
    
    /**
    * @brief Transmissão e recepção de dados aperiódicos na função de passagem direta na extremidade
    * @param [in] lenSnd Comprimento do envio
    * @param [in] sndBuff Dados a serem enviados
    * @param [in] lenRcv Comprimento da recepção selecionada
    * @param [out] rcvBuff Dados de resposta
    * @return Código de erro
    */
    errno_t SndRcvAxleGenComCmdData(int lenSnd, int sndBuff[130], int lenRcv, int rcvData[130]);
                                                                
Exemplo de Código para Comunicação de Dados Aperiódicos do Cabeçote de Moxabustão Beiyikang Baseado na Função de Passagem Direta na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int testAxleGenCom()
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
      int led_on[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
      int led_off[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int version[5] = { 0xAB, 0xBA, 0x11, 0x00, 0x76 };
      int state[6] = { 0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B };
      int cycleState[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int rcvdata[16] = {0};
      int ret = 0;
      int cnt = 1;
      JointPos p1Joint(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
      DescPose p1Desc(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);
      JointPos p2Joint(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
      DescPose p2Desc(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      //Ativar função de passagem direta na extremidade
      robot.SetAxleGenComEnable(1);
      robot.SetAxleLuaEnable(1);
      while (cnt <= 10000)
      {
        //Ler número da versão
        ret = robot.SndRcvAxleGenComCmdData(5, version, 10, rcvdata);
        printf(" hard version : %d,hard code:%d, soft version:%d %d, soft code:%d \n", rcvdata[4], rcvdata[5], rcvdata[6] ,rcvdata[7], rcvdata[8]);
        if (ret != 0)
        {
          break;
        }
        robot.Sleep(1000);
        //Ler estado de presença do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, state, 6, rcvdata);
        printf(" state : %d \n", rcvdata[4]);
        robot.Sleep(1000);
        //Ativar laser do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, rcvdata);
        printf("led on rcv data is: %d, %d, %d, %d, %d, %d  \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(4000);
        //Desativar laser do cabeçote de moxabustão
        ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, rcvdata);
        printf("led off rcv data is: %d, %d, %d, %d, %d, %d \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(1000);
        printf("***********************complate No. %d SDK test*****************************\n", cnt);
        cnt++;
      }
      robot.CloseRPC();
    }

Download do Arquivo Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Download do arquivo Lua de protocolo aberto
    * @param [in] fileName Nome do arquivo de protocolo aberto "CtrlDev_XXX.lua"
    * @param [in] savePath Caminho para salvar o arquivo de protocolo aberto
    * @return Código de erro
    */
    errno_t OpenLuaDownload(std::string fileName, std::string savePath);
    
Excluir Arquivo Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Excluir arquivo Lua de protocolo aberto
    * @param [in] fileName Nome do arquivo lua de protocolo aberto a ser excluído "CtrlDev_XXX.lua"
    * @return Código de erro
    */
    errno_t OpenLuaDelete(std::string fileName);
        
Excluir Todos os Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Excluir todos os arquivos Lua de protocolo aberto
    * @return Código de erro
    */
    errno_t AllOpenLuaDelete();

Exemplo de Código para Upload, Download e Exclusão de Protocolo Aberto de Periférico do Controlador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestCtrlOpenLuaOperate()
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
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        std::string name[4] = {};
        rtn = robot.GetCtrlOpenLUAName(name);
        printf("ctrl open lua names : %s, %s, %s, %s\n", name[0].c_str(), name[1].c_str(), name[2].c_str(), name[3].c_str());
        rtn = robot.LoadCtrlOpenLUA(1);
        printf("LoadCtrlOpenLUA rtn is %d\n", rtn);
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        printf("UnloadCtrlOpenLUA rtn is %d\n", rtn);
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        printf("OpenLuaDelete rtn is %d\n", rtn);
        rtn = robot.AllOpenLuaDelete();
        printf("AllOpenLuaDelete rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

Controlar o Movimento da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Controlar o movimento da mão destra
    * @param [in] idstart Número da estação escrava inicial
    * @param [in] slaveNum Número de escravos
    * @param [in] pos Array de posições, comprimento 16, intervalo (-360~360)
    * @param [in] speed Array de percentuais de velocidade, comprimento 16, intervalo [0~100]
    * @param [in] force Array de percentuais de torque, comprimento 16, intervalo [0~100]
    * @param [in] max_time Tempo máximo de espera, intervalo [0~30000], unidade ms
    * @return Código de erro, 0 em caso de sucesso
    */
    errno_t SetDexterousHandsMove(int idstart, int slaveNum, double pos[16], int speed[16], int force[16], int max_time);
        
Controlar o Reset e Ativação da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Controlar o reset e ativação da mão destra
    * @param [in] id Número da estação escrava
    * @param [in] act 0-reset 1-ativação
    * @return Código de erro, 0 em caso de sucesso
    */
    errno_t SetDexterousHandsAct(int id, int act);
            
Limpar Erro da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Limpar erro da mão destra
    * @return Código de erro, 0 em caso de sucesso
    */
    errno_t ClearDexterousHandsError();
                
Definir as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define as funções de controle de ação da mão destra habilitadas
    * @param [in] id Número do dispositivo da mão destra
    * @param [in] func 0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque, 6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade, 11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação, 15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação, 19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único, 23-estado de operação de todos os eixos
    * @return Código de erro
    */
    errno_t SetDexterousHandsFunc(int id, int func[32]);
                    
Obter as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém as funções de controle de ação da mão destra habilitadas
    * @param [in] id Número do dispositivo da mão destra
    * @param [out] func 0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque, 6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade, 11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação, 15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação, 19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único, 23-estado de operação de todos os eixos
    * @return Código de erro
    */
    errno_t GetDexterousHandsFunc(int id, int func[32]);
                        
Exemplo de Código de Configuração e Movimento da Mão Destra no Efetuador Final
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestDexterousHands()
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
    int id = 1;        // Número da estação escrava
    int slaveNum = 4;     // Controla 4 dedos
    int max_time = 8000;   // Tempo máximo de espera 8 segundos
    int speed[16] = {0};   // Array de velocidade, todos 0 significa usar velocidade padrão
    int force[16] = {0};   // Array de torque
    // Inicializar array de torque: primeiros 4 dedos definidos como 50%, o resto 0 (valores enviados via comando Move)
    for (int i = 0; i < 16; i++)
    {
        force[i] = (i < 4) ? 50 : 0;
    }
    // Função auxiliar: definir array de posição (apenas os primeiros 4 dedos são efetivos)
    double pos[16] = {0.0};
    JointPos j1(-91.876, -85.920, 109.279, -86.239, -96.664, -28.563);
    JointPos j2(-40.954, -85.920, 109.279, -86.239, -96.664, -28.563);
    ExaxisPos epos(0, 0, 0, 0);
    DescPose offset_pos(0, 0, 0, 0, 0, 0);
    printf("===== Teste de Função Completa da Mão Destra Iniciado =====\n");
    // 1. Limpar erro
    int ret = robot.ClearDexterousHandsError();
    printf("ClearDexterousHandsError rtn %d\n", ret);
    // ========== 2. Definir chaves de função ==========
    int setFunc[32] = {0};
    setFunc[2] = 1;  // Habilitar função de definição de posição
    setFunc[4] = 1;  // Habilitar função de definição de torque
    setFunc[9] = 1;  // Ler posição
    setFunc[10] = 1;  // Ler torque
    setFunc[11] = 1;  // Ler status
    setFunc[22] = 1;  // Status de movimento de eixo único
    ret = robot.SetDexterousHandsFunc(id, setFunc);
    printf("SetDexterousHandsFunc(init + funções de posição/torque habilitadas) rtn %d\n", ret);
    // ========== 3. Ler status da função (verificar se as configurações foram aplicadas) ==========
    int getFunc[32] = {0}; // GetDexterousHandsFunc retorna 32 inteiros
    ret = robot.GetDexterousHandsFunc(id, getFunc);
    printf("GetDexterousHandsFunc rtn %d\n", ret);
    if (ret == 0)
    {
        // Imprimir todos os 32 valores
        printf("Todos os 32 valores retornados por GetDexterousHandsFunc:");
        for (int i = 0; i < 32; i++)
        {
        printf(" [%d]={%d}", i, getFunc[i]);
        if ((i + 1) % 8 == 0)
        {
            printf("\n");
        } 
        else if (i < 31)
        {
            printf(", ");
        }
        }
    }
    // ========== 4. Ativar mão destra ==========
    ret = robot.SetDexterousHandsAct(id, 1);
    printf("SetDexterousHandsAct(ativar) rtn %d\n", ret);
    if (ret != 0)
    {
        printf("Falha na ativação, teste abortado");
        return -1;
    }
    // ========== 5. Movimento inicial para 20° (enviar valores de posição e torque via comando Move) ==========
    memset(pos, 0, sizeof(pos));
    pos[0] = 20;
    pos[1] = 20;
    pos[2] = 20;
    pos[3] = 20;
    ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
    printf("Movimento inicial para 20° -> %d\n", ret);
    robot.Sleep(5000);
    // ========== 6. Movimento alternado 10 vezes (10° ↔ 50°) ==========
    printf("Iniciando 10 movimentos alternados...");
    for (int iteration = 1; iteration <= 10; iteration++)
    {
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        memset(pos, 0, sizeof(pos));
        pos[0] = 10;
        pos[1] = 10;
        pos[2] = 10;
        pos[3] = 10;
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        printf("Movimento para 10° -> %d\n", ret);
        robot.Sleep(1000);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        memset(pos, 0, sizeof(pos));
        pos[0] = 50;
        pos[1] = 50;
        pos[2] = 50;
        pos[3] = 50;
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        printf("Movimento para 50° -> %d\n", ret);
        robot.Sleep(1000);
    }
    printf("Teste concluído (definição/leitura de chaves de função + ativação + 10 movimentos alternados).");
    return 0;
    }    