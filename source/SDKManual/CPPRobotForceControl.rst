Controle de Força do Robô
====================================

.. toctree:: 
    :maxdepth: 5

Configuração do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
	 * @brief  Configura o sensor de força
	 * @param  [in] company  Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa Aeroespacial 11, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin, 23-NBIT, 24-Xinjingcheng (XJC), 26-NSR
	 * @param  [in] device  Número do dispositivo, Kunwei(0-KWR75B), Instituto Aeroespacial 11(0-MCS6A-200-4), ATI(0-AXIA80-M8), Zhongke Midian(0-MST2010), Weihang Minxin(0-WHC6L-YB-10A), NBIT(0-XLH93003ACS), Xinjingcheng XJC(0-XJC-6F-D82), NSR(0-NSR-FTSensorA)
	 * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
	 * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
	 * @return  Código de erro
	 */
    errno_t FT_SetConfig(int company, int device, int softvesion, int bus);

Obter Configuração do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a configuração do sensor de força
    * @param  [in] company  Fabricante do sensor de força, a definir
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    errno_t  FT_GetConfig(int *company, int *device, int *softvesion, int *bus);

Ativação do Sensor de Força
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Ativa o sensor de força
    * @param  [in] act  0-reset, 1-ativar
    * @return  Código de erro
    */
    errno_t  FT_Activate(uint8_t act);

Zeragem do Sensor de Força
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Zera o sensor de força
    * @param  [in] act  0-remover zero, 1-correção de zero
    * @return  Código de erro
    */
    errno_t  FT_SetZero(uint8_t act);   

Definir Sistema de Coordenadas de Referência do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o sistema de coordenadas de referência do sensor de força
    * @param  [in] ref  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @return  Código de erro
    */
    errno_t  FT_SetRCS(uint8_t ref); 

Definir Peso da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o peso da carga sob o sensor de força
     * @param [in] weight Peso da carga kg
     * @return Código de erro
     */
    errno_t SetForceSensorPayload(double weight);

Definir Centro de Gravidade da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o centro de gravidade da carga sob o sensor de força
     * @param [in] x Centro de gravidade da carga x mm
     * @param [in] y Centro de gravidade da carga y mm
     * @param [in] z Centro de gravidade da carga z mm
     * @return Código de erro
     */
    errno_t SetForceSensorPayloadCog(double x, double y, double z);

Obter Peso da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
     * @brief Obtém o peso da carga sob o sensor de força
     * @param [in] weight Peso da carga kg
     * @return Código de erro
     */
    errno_t GetForceSensorPayload(double& weight);

Obter Centro de Gravidade da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém o centro de gravidade da carga sob o sensor de força
     * @param [out] x Centro de gravidade da carga x mm
     * @param [out] y Centro de gravidade da carga y mm
     * @param [out] z Centro de gravidade da carga z mm
     * @return Código de erro
     */
    errno_t GetForceSensorPayloadCog(double& x, double& y, double& z);

Autozero do Sensor de Força
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Autozero do sensor de força
     * @param [out] weight Massa do sensor kg
     * @param [out] pos Centro de gravidade do sensor mm
     * @return Código de erro
     */
    errno_t ForceSensorAutoComputeLoad(double& weight, DescTran& pos);

Obter Dados de Força/Torque no Sistema de Coordenadas de Referência
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém dados de força/torque no sistema de coordenadas de referência
    * @param  [out] ft  Força/torque, fx, fy, fz, tx, ty, tz
    * @return  Código de erro
    */   
    errno_t  FT_GetForceTorqueRCS(ForceTorque *ft); 

Obter Dados Brutos de Força/Torque do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém dados brutos de força/torque do sensor de força
    * @param  [out] ft  Força/torque, fx, fy, fz, tx, ty, tz
    * @return  Código de erro
    */   
    errno_t  FT_GetForceTorqueOrigin(ForceTorque *ft); 

Exemplo de Código para Configuração e Autozero do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTInit(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      robot.FT_GetForceTorqueOrigin(0, &ft);
      printf("ft origin:%f,%f,%f,%f,%f,%f\n", ft.fx, ft.fy, ft.fz, ft.tx, ft.ty, ft.tz);
      robot.FT_SetZero(1);
      robot.Sleep(1000);
      DescPose ftCoord = {};
      robot.FT_SetRCS(0, ftCoord);
      robot.SetForceSensorPayload(0.824);
      robot.SetForceSensorPayloadCog(0.778, 2.554, 48.765);
      double weight = 0;
      double x = 0, y = 0, z = 0;
      robot.GetForceSensorPayload(weight);
      robot.GetForceSensorPayloadCog(x, y, z);
      printf("the FT load is %lf, %lf %lf %lf\n", weight, x, y, z);
      robot.SetForceSensorPayload(0);
      robot.SetForceSensorPayloadCog(0, 0, 0);
      double computeWeight = 0;
      DescTran tran = {};
      robot.ForceSensorAutoComputeLoad(weight, tran);
      cout << "the result is weight " << weight << " pos is " << tran.x << " " << tran.y << " " << tran.z << endl;
      robot.CloseRPC();
      return 0;
    }


Registro da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Registro da identificação do peso da carga
    * @param  [in] id  Número do sistema de coordenadas do sensor, faixa [1~14]
    * @return  Código de erro
    */
    errno_t  FT_PdIdenRecord(int id);   

Cálculo da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Cálculo da identificação do peso da carga
    * @param  [out] weight  Peso da carga, unidade kg
    * @return  Código de erro
    */   
    errno_t  FT_PdIdenCompute(float *weight);

Registro da Identificação do Centro de Gravidade da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Registro da identificação do centro de gravidade da carga
    * @param  [in] id  Número do sistema de coordenadas do sensor, faixa [1~14]
    * @param  [in] index Número do ponto, faixa [1~3]
    * @return  Código de erro
    */
    errno_t  FT_PdCogIdenRecord(int id, int index);    

Cálculo da Identificação do Centro de Gravidade da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Cálculo da identificação do centro de gravidade da carga
    * @param  [out] cog  Centro de gravidade da carga, unidade mm
    * @return  Código de erro
    */   
    errno_t  FT_PdCogIdenCompute(DescTran *cog); 

Exemplo de Código para Identificação da Carga do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTLoadCompute(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      robot.FT_GetForceTorqueOrigin(0, &ft);
      printf("ft origin:%f,%f,%f,%f,%f,%f\n", ft.fx, ft.fy, ft.fz, ft.tx, ft.ty, ft.tz);
      robot.FT_SetZero(1);
      robot.Sleep(1000);
      DescPose tcoord = {};
      tcoord.tran.z = 35.0;
      robot.SetToolCoord(10, &tcoord, 1, 0, 0, 0);
      robot.FT_PdIdenRecord(10);
      robot.Sleep(1000);
      float weight = 0.0;
      robot.FT_PdIdenCompute(&weight);
      printf("payload weight:%f\n", weight);
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_p3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      robot.MoveCart(&desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 1);
      robot.MoveCart(&desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 2);
      robot.MoveCart(&desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 3);
      robot.Sleep(1000);
      DescTran cog;
      memset(&cog, 0, sizeof(DescTran));
      robot.FT_PdCogIdenCompute(&cog);
      printf("cog:%f,%f,%f\n", cog.x, cog.y, cog.z);
      robot.CloseRPC();
      return 0;
    }

Proteção Contra Colisão
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Proteção contra colisão
    * @param  [in] flag 0-desativar proteção contra colisão, 1-ativar proteção contra colisão
    * @param  [in] sensor_id Número do sensor de força
    * @param  [in] select  Seleciona se os seis graus de liberdade são detectados para colisão, 0-não detectar, 1-detectar
    * @param  [in] ft  Força/torque de colisão, fx, fy, fz, tx, ty, tz
    * @param  [in] max_threshold Limite máximo
    * @param  [in] min_threshold Limite mínimo
    * @note   Faixa de detecção de força/torque: (ft-min_threshold, ft+max_threshold)
    * @return  Código de erro
    */   
    errno_t  FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]); 

Exemplo de Código para Proteção Contra Colisão
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTGuard(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t sensor_id = 1;
      uint8_t select[6] = { 1,1,1,1,1,1 };
      float max_threshold[6] = { 10.0,10.0,10.0,10.0,10.0,10.0 };
      float min_threshold[6] = { 5.0,5.0,5.0,5.0,5.0,5.0 };
      ForceTorque ft;
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_p3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      robot.FT_Guard(1, sensor_id, select, &ft, max_threshold, min_threshold);
      robot.MoveCart(&desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.MoveCart(&desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.MoveCart(&desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.FT_Guard(0, sensor_id, select, &ft, max_threshold, min_threshold);
      robot.CloseRPC();
      return 0;
    }

Controle de Força Constante
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Controle de força constante
    * @param [in] flag 0-desativar controle de força constante, 1-ativar controle de força constante
    * @param [in] sensor_id Número do sensor de força
    * @param [in] select  Seleciona se os seis graus de liberdade são detectados para colisão, 0-não detectar, 1-detectar
    * @param [in] ft  Força/torque de colisão, fx, fy, fz, tx, ty, tz
    * @param [in] ft_pid Parâmetros PID de força, parâmetros PID de torque
    * @param [in] adj_sign Controle de ativação/desativação adaptativa, 0-desativar, 1-ativar
    * @param [in] ILC_sign Controle de ativação/desativação ILC, 0-parar, 1-treinar, 2-operação real
    * @param [in] max_dis Distância máxima de ajuste, unidade mm
    * @param [in] max_ang Ângulo máximo de ajuste, unidade graus
    * @param [in] M Parâmetros de massa rx, ry [0.1-10], padrão 2
    * @param [in] B Parâmetros de amortecimento rx, ry [0.1-50], padrão 8
    * @param [in] threshold Limite de ativação rx, ry [0-10], padrão 0.2
    * @param [in] adjustCoeff Coeficiente de ajuste de torque rx, ry [0-1], padrão 1
    * @param [in] polishRadio Raio de lixamento, unidade mm
    * @param [in] filter_Sign Flag de ativação do filtro 0-desativar; 1-ativar, padrão desativado
    * @param [in] posAdapt_sign Flag de ativação da conformidade de postura 0-desativar; 1-ativar, padrão desativado
    * @param [in] isNoBlock Flag de bloqueio, 0-bloqueado; 1-não bloqueado
    * @return Código de erro
    */
    errno_t FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque* ft, float ft_pid[6], uint8_t adj_sign, 
    uint8_t ILC_sign, float max_dis, float max_ang, double M[2], double B[2], double threshold[2], double adjustCoeff[2], double polishRadio = 0.0, int filter_Sign = 0, int posAdapt_sign = 0, int isNoBlock = 0);

Exemplo de Código para Controle de Força Constante com Amortecimento
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTControlWithAdjustCoeff(void)
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
      uint8_t sensor_id = 10;
      uint8_t select[6] = { 0,0,1,0,0,0 };
      float ft_pid[6] = { 0.0008, 0.0, 0.0, 0.0, 0.0, 0.0 };
      uint8_t adj_sign = 0;
      uint8_t ILC_sign = 0;
      float max_dis = 1000.0;
      float max_ang = 20;
      ForceTorque ft = {0.0};
      ExaxisPos epos(0, 0, 0, 0);
      JointPos j1(80.765, -98.795, 106.548, -97.734, -89.999, 94.842);
      JointPos j2(43.067, -84.429, 92.620, -98.175, -90.011, 57.144);
      DescPose desc_p1(5.009, -547.463, 262.053, -179.999, -0.019, 75.923);
      DescPose desc_p2(-347.966, -547.463, 262.048, -180.000, -0.019, 75.923);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      double M[2] = { 2.0, 2.0 };
      double B[2] = { 15.0, 15.0 };
      double threshold[2] = {1.0, 1.0};
      double adjustCoeff[2] = {1.0, 0.8};
      double polishRadio = 0.0;
      int filter_Sign = 0;
      int posAdapt_sign = 1;
      int isNoBlock;
      ft.fz = -10.0;
      while(true)
      { 
        rtn = robot.FT_Control(1, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
        printf("FT_Control start rtn is %d\n", rtn);
        robot.MoveL(&j1, &desc_p1, 1, 0, 100, 100, 100, -1, 0, &epos, 0, 0, &offset_pos, 200.0, 0);
        robot.MoveL(&j2, &desc_p2, 1, 0, 100, 100, 100, -1, 0, &epos, 0, 0, &offset_pos, 200.0, 0);
        rtn = robot.FT_Control(0, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
        printf("FT_Control end rtn is %d\n", rtn);
      }
      robot.CloseRPC();
      return 0;
    }

Busca em Espiral
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Busca em espiral
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param  [in] dr Avanço do raio por volta
    * @param  [in] ft Limite de força/torque, fx, fy, fz, tx, ty, tz, faixa [0~100]
    * @param  [in] max_t_ms Tempo máximo de busca, unidade ms
    * @param  [in] max_vel Velocidade linear máxima, unidade mm/s
    * @return  Código de erro
    */   
    errno_t  FT_SpiralSearch(int rcs, float dr, float ft, float max_t_ms, float max_vel);  

Inserção Rotativa
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Inserção rotativa
    * @param [in] rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param [in] angVelRot Velocidade angular de rotação, unidade deg/s
    * @param [in] ft  Limite de força/torque, fx, fy, fz, tx, ty, tz, faixa [0~100]
    * @param [in] max_angle Ângulo máximo de rotação, unidade deg
    * @param [in] orn Direção da força/torque, 1-ao longo do eixo z, 2-em torno do eixo z
    * @param [in] max_angAcc Aceleração angular máxima de rotação, unidade deg/s^2, não usado no momento, padrão 0
    * @param [in] rotorn  Direção de rotação, 1-sentido horário, 2-sentido anti-horário
    * @param [in] strategy Estratégia de tratamento quando nenhuma força/torque é detectada, 0-erro; 1-aviso, continuar movimento
    * @return Código de erro
    */
    errno_t FT_RotInsertion(int rcs, float angVelRot, float ft, float max_angle, uint8_t orn, float max_angAcc, uint8_t rotorn, int strategy = 0);

Exemplo de Código para Inserção Rotativa com Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMove(void)
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
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float oacc = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, oacc, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&j3, &desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &j4, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, oacc, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&j3, &desc_pos3, tool, user, vel, acc, &epos, &j1, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(&desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, -1, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, -1, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&desc_pos3, tool, user, vel, acc, &epos, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, blendR, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        robot.CloseRPC();
        return 0;
    }

Inserção Linear
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Inserção linear
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param  [in] ft  Limite de força/torque, fx, fy, fz, tx, ty, tz, faixa [0~100]
    * @param  [in] lin_v Velocidade linear, unidade mm/s
    * @param  [in] lin_a Aceleração linear, unidade mm/s^2, não usado no momento
    * @param  [in] max_dis Distância máxima de inserção, unidade mm
    * @param  [in] linorn  Direção de inserção, 0-direção negativa, 1-direção positiva
    * @return  Código de erro
    */   
    errno_t  FT_LinInsertion(int rcs, float ft, float lin_v, float lin_a, float max_dis, uint8_t linorn);    

Exemplo de Código para Busca em Espiral, Inserção Linear, etc.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTSearch(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t status = 1; 
      int sensor_num = 1; 
      float gain[6] = { 0.0001,0.0,0.0,0.0,0.0,0.0 }; 
      uint8_t adj_sign = 0; 
      uint8_t ILC_sign = 0; 
      float max_dis = 100.0; 
      float max_ang = 5.0; 
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      int rcs = 0; 
      float dr = 0.7; 
      float fFinish = 1.0; 
      float t = 60000.0;
      float vmax = 3.0;
      float force_goal = 20.0; 
      float lin_v = 0.0;
      float lin_a = 0.0;
      float disMax = 100.0;
      uint8_t linorn = 1; 
      float angVelRot = 2.0; 
      float forceInsertion = 1.0; 
      int angleMax = 45; 
      uint8_t orn = 1;
      float angAccmax = 0.0; 
      uint8_t rotorn = 1; 
      uint8_t select1[6] = { 0,0,1,1,1,0 }; 
      ft.fz = -10.0;
      robot.FT_Control(status, sensor_num, select1, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_SpiralSearch(rcs, dr, fFinish, t, vmax);
      printf("FT_SpiralSearch rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select1, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select2[6] = { 1,1,1,0,0,0 }; 
      gain[0] = 0.00005;
      ft.fz = -30.0;
      status = 1;
      robot.FT_Control(status, sensor_num, select2, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn);
      printf("FT_LinInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select2, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select3[6] = { 0,0,1,1,1,0 }; 
      ft.fz = -10.0;
      gain[0] = 0.0001;
      status = 1;
      robot.FT_Control(status, sensor_num, select3, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn);
      printf("FT_RotInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select3, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select4[6] = { 1,1,1,0,0,0 }; 
      ft.fz = -30.0;
      status = 1;
      robot.FT_Control(status, sensor_num, select4, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn);
      printf("FT_LinInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select4, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      robot.CloseRPC();
      return 0;
    }

Localização de Superfície
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Localização de superfície
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param  [in] dir  Direção de movimento, 1-direção positiva, 2-direção negativa 
    * @param  [in] axis Eixo de movimento, 1-eixo x, 2-eixo y, 3-eixo z
    * @param  [in] lin_v Velocidade linear de busca, unidade mm/s
    * @param  [in] lin_a Aceleração linear de busca, unidade mm/s^2, não usado no momento, padrão 0
    * @param  [in] max_dis Distância máxima de busca, unidade mm
    * @param  [in] ft  Limite de força/torque de término da ação, fx, fy, fz, tx, ty, tz  
    * @return  Código de erro
    */   
    errno_t  FT_FindSurface(int rcs, uint8_t dir, uint8_t axis, float lin_v, float lin_a, float max_dis, float ft);   

Início do Cálculo da Posição do Plano Médio
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Início do cálculo da posição do plano médio
    * @return  Código de erro
    */   
    errno_t  FT_CalCenterStart();

Fim do Cálculo da Posição do Plano Médio
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Fim do cálculo da posição do plano médio
    * @param  [out] pos Pose do plano médio
    * @return  Código de erro
    */      
    errno_t  FT_CalCenterEnd(DescPose *pos);

Exemplo de Código para Localização de Superfície
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSurface(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      int rcs = 0;
      uint8_t dir = 1;
      uint8_t axis = 1;
      float lin_v = 3.0;
      float lin_a = 0.0;
      float maxdis = 50.0;
      float ft_goal = 2.0;
      DescPose desc_pos(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose xcenter(0, 0, 0, 0, 0, 0);
      DescPose ycenter(0, 0, 0, 0, 0, 0);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      ft.fx = -2.0;
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.FT_CalCenterStart();
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.WaitMs(1000);
      dir = 2;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.FT_CalCenterEnd(&xcenter);
      printf("xcenter:%f,%f,%f,%f,%f,%f\n", xcenter.tran.x, xcenter.tran.y, xcenter.tran.z, xcenter.rpy.rx, xcenter.rpy.ry, xcenter.rpy.rz);
      robot.MoveCart(&xcenter, 9, 0, 60.0, 50.0, 50.0, -1.0, -1);
      robot.FT_CalCenterStart();
      dir = 1;
      axis = 2;
      lin_v = 6.0;
      maxdis = 150.0;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.WaitMs(1000);
      dir = 2;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.FT_CalCenterEnd(&ycenter);
      printf("ycenter:%f,%f,%f,%f,%f,%f\n", ycenter.tran.x, ycenter.tran.y, ycenter.tran.z, ycenter.rpy.rx, ycenter.rpy.ry, ycenter.rpy.rz);
      robot.MoveCart(&ycenter, 9, 0, 60.0, 50.0, 50.0, 0.0, -1);
      robot.CloseRPC();
      return 0;
    }

Ativação do Controle de Complacência
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Ativa o controle de complacência
    * @param  [in] p Coeficiente de ajuste de posição ou coeficiente de complacência
    * @param  [in] force Limite de força para ativação da complacência, unidade N
    * @return  Código de erro
    */   
    errno_t  FT_ComplianceStart(float p, float force); 

Desativação do Controle de Complacência
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Desativa o controle de complacência
    * @return  Código de erro
    */   
    errno_t  FT_ComplianceStop(); 

Exemplo de Código para Controle de Complacência
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestCompliance(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t flag = 1;
      int sensor_id = 1;
      uint8_t select[6] = { 1,1,1,0,0,0 };
      float ft_pid[6] = { 0.0005,0.0,0.0,0.0,0.0,0.0 };
      uint8_t adj_sign = 0;
      uint8_t ILC_sign = 0;
      float max_dis = 100.0;
      float max_ang = 0.0;
      ForceTorque ft;
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      memset(&ft, 0, sizeof(ForceTorque));
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      ft.fx = -10.0;
      ft.fy = -10.0;
      ft.fz = -10.0;
      robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      float p = 0.00005;
      float force = 30.0;
      rtn = robot.FT_ComplianceStart(p, force);
      printf("FT_ComplianceStart rtn is %d\n", rtn);
      int count = 15;
      while (count)
      {
        robot.MoveL(&j1, &desc_p1, 0, 0, 100.0, 180.0, 100.0, -1.0, &epos, 0, 1, &offset_pos);
        robot.MoveL(&j2, &desc_p2, 0, 0, 100.0, 180.0, 100.0, -1.0, &epos, 0, 0, &offset_pos);
        count -= 1;
      }
      robot.FT_ComplianceStop();
      printf("FT_ComplianceStop rtn is %d\n", rtn);
      flag = 0;
      robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      robot.CloseRPC();
      return 0;
    }

Inicialização da Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Inicialização da identificação da carga
    * @return Código de erro
    */
    errno_t LoadIdentifyDynFilterInit();

Inicialização das Variáveis de Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Inicialização das variáveis de identificação da carga
    * @return Código de erro
    */
    errno_t LoadIdentifyDynVarInit();

Programa Principal de Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Programa principal de identificação da carga
    * @param [in] joint_torque Torque das juntas
    * @param [in] joint_pos Posição das juntas
    * @param [in] t Período de amostragem
    * @return Código de erro
    */
    errno_t LoadIdentifyMain(double joint_torque[6], double joint_pos[6], double t);

Obter Resultado da Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o resultado da identificação da carga
    * @param [in] gain 
    * @param [out] weight Peso da carga
    * @param [out] cog Centro de gravidade da carga
    * @return Código de erro
    */
    errno_t LoadIdentifyGetResult(double gain[12], double *weight, DescTran *cog);

Exemplo de Código para Identificação da Carga do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestIdentify(void)
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
      retval = robot.LoadIdentifyDynFilterInit();
      printf("LoadIdentifyDynFilterInit retval is: %d \n", retval);
      retval = robot.LoadIdentifyDynVarInit();
      printf("LoadIdentifyDynVarInit retval is: %d \n", retval);
      JointPos posJ = {};
      DescPose posDec = {};
      float joint_toq[6] = { 0.0 };
      robot.GetActualJointPosDegree(0, &posJ);
      posJ.jPos[1] = posJ.jPos[1] + 10;
      robot.GetJointTorques(0, joint_toq);
      joint_toq[1] = joint_toq[1] + 2;
      double tmpTorque[6] = { 0.0 };
      for (int i = 0; i < 6; i++)
      {
        tmpTorque[i] = joint_toq[i];
      }
      retval = robot.LoadIdentifyMain(tmpTorque, posJ.jPos, 1);
      printf("LoadIdentifyMain retval is: %d \n", retval);
      double gain[12] = { 0,0.05,0,0,0,0,0,0.02,0,0,0,0 };
      double weight = 0;
      DescTran load_pos;
      memset(&load_pos, 0, sizeof(DescTran));
      retval = robot.LoadIdentifyGetResult(gain, &weight, &load_pos);
      printf("LoadIdentifyGetResult retval is: %d ; weight is %f cog is %f %f %f \n", retval, weight, load_pos.x, load_pos.y, load_pos.z);
      robot.CloseRPC();
      return 0;
    }

Arrastagem Assistida por Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.0-3.8.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  Arrastagem assistida por sensor de força
    * @param  [in] status Estado de controle, 0-desativar; 1-ativar
    * @param  [in] asaptiveFlag Flag de ativação adaptativa, 0-desativar; 1-ativar
    * @param  [in] interfereDragFlag Flag de arrastagem em área de interferência, 0-desativar; 1-ativar
    * @param  [in] ingularityConstraintsFlag Estratégia para pontos singulares, 0-evitar; 1-atravessar
    * @param  [in] forceCollisionFlag Flag de detecção de colisão durante arrastagem assistida; 0-desativar; 1-ativar
    * @param  [in] M Coeficiente de inércia
    * @param  [in] B Coeficiente de amortecimento
    * @param  [in] K Coeficiente de rigidez
    * @param  [in] F Limite de força de arrastagem de 6 eixos
    * @param  [in] Fmax Limite máximo de força de arrastagem
    * @param  [in] Vmax Limite máximo de velocidade das juntas
    * @return  Código de erro
    */
    errno_t EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, int ingularityConstraintsFlag, int forceCollisionFlag, std::vector<double> M, std::vector<double> B, std::vector<double> K, std::vector<double> F, double Fmax, double Vmax);

Obter Estado da Chave de Arrastagem do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém o estado da chave de arrastagem do sensor de força
     * @param [out] dragState Estado de controle da arrastagem assistida por sensor de força, 0-desativar; 1-ativar
     * @param [out] sixDimensionalDragState Estado de controle da arrastagem assistida por força de 6 eixos, 0-desativar; 1-ativar
     * @return Código de erro
     */
    errno_t GetForceAndTorqueDragState(int& dragState, int& sixDimensionalDragState);

Ativação Automática do Sensor de Força Após Limpeza de Erro
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Ativação automática do sensor de força após limpeza de erro
     * @param [in] status Estado de controle, 0-desativar; 1-ativar
     * @return Código de erro
     */
    errno_t SetForceSensorDragAutoFlag(int status);

Exemplo de Código para Arrastagem Assistida por Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestEndForceDragCtrl(void)
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
         robot.SetForceSensorDragAutoFlag(1);
         vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
         vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
         vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
         vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
         robot.EndForceDragControl(1, 0, 0, 0, 1, M, B, K, F, 50, 100);
         robot.Sleep(5000);
         int dragState = 0;
         int sixDimensionalDragState = 0;
         robot.GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
         printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);
         robot.EndForceDragControl(0, 0, 0, 0, 1, M, B, K, F, 50, 100);
         robot.CloseRPC();
         return 0;
     }

Definir Chave e Parâmetros para Arrastagem Híbrida com Força de 6 Eixos e Impedância de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Define a chave e parâmetros para arrastagem híbrida com força de 6 eixos e impedância de junta
     * @param [in] status Estado de controle, 0-desativar; 1-ativar
     * @param [in] impedanceFlag Flag de ativação da impedância, 0-desativar; 1-ativar
     * @param [in] lamdeDain Ganho de arrastagem
     * @param [in] KGain Ganho de rigidez
     * @param [in] BGain Ganho de amortecimento
     * @param [in] dragMaxTcpVel Limite máximo de velocidade linear da extremidade durante arrastagem
     * @param [in] dragMaxTcpOriVel Limite máximo de velocidade angular da extremidade durante arrastagem
     * @return Código de erro
     */
    errno_t ForceAndJointImpedanceStartStop(int status, int impedanceFlag, std::vector<double> lamdeDain, std::vector<double> KGain, std::vector<double> BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

Exemplo de Código para Arrastagem Híbrida com Força de 6 Eixos e Impedância de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestForceAndJointImpedance(void)
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
      vector <double> lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
      vector <double> KGain = { 0, 0, 0, 0, 0, 0 };
      vector <double> BGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
      rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000, 180);
      printf("ForceAndJointImpedanceStartStop rtn is %d\n", rtn);
      robot.Sleep(5000);
      robot.DragTeachSwitch(0);
      rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000, 180);
      printf("ForceAndJointImpedanceStartStop rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Controle de Ativação/Desativação da Impedância
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Controle de ativação/desativação da impedância
    * @param [in] status 0-desativar; 1-ativar
    * @param [in] workSpace 0-espaço articular; 1-espaço cartesiano
    * @param [in] forceThreshold Limite de força de disparo (N)
    * @param [in] m Parâmetro de massa
    * @param [in] b Parâmetro de amortecimento
    * @param [in] k Parâmetro de rigidez
    * @param [in] maxV Velocidade linear máxima (mm/s)
    * @param [in] maxVA Aceleração linear máxima (mm/s2)
    * @param [in] maxW Velocidade angular máxima (°/s)
    * @param [in] maxWA Aceleração angular máxima (°/s2)
    * @return Código de erro
    */
    errno_t ImpedanceControlStartStop(int status, int workSpace, double forceThreshold[6], double m[6], double b[6], double k[6], double maxV, double maxVA, double maxW, double maxWA);

Exemplo de Código para Controle de Ativação/Desativação da Impedância do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    int TestImpedanceControl()
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
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      JointPos j1(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
      JointPos j2(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
      DescPose desc_pos1(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
      DescPose desc_pos2(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 200.0;
      float ovl = 100.0;
      float blendT = -1.0;
      float blendR = -1.0;
      uint8_t flag = 0;
      uint8_t search = 0;
      robot.SetSpeed(20);
      int company = 17;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
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
      double forceThreshold[6] = { 30,30,30,5,5,5 };
      double m[6] = { 0.1,0.1,0.1,0.02,0.02,0.02 };
      double b[6] = { 1,1,1,0.08,0.08,0.08 };
      double k[6] = { 0,0,0,0,0,0 };
      rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
      printf("ImpedanceControlStartStop errcode:%d\n", rtn);
      rtn = robot.MoveL(&desc_pos1, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos1, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      printf("movel errcode:%d\n", rtn);
      robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);    
      robot.CloseRPC();
      return 0;
    }

Ativação da Função de Compensação de Torque e Coeficiente de Compensação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Ativação da função de compensação de torque e coeficiente de compensação
    * @param [in] status Interruptor, 0-desativar; 1-ativar
    * @param [in] torqueCoeff Coeficiente de compensação de torque J1-J6 [0-1]
    * @return Código de erro
    */
    errno_t SetCoderCompenParams(int status, double torqueCoeff[6]);