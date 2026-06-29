Configurações Comuns do Robô
===================================

.. toctree::
    :maxdepth: 5

Definir Ponto de Referência da Ferramenta - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o ponto de referência da ferramenta - método dos seis pontos
     * @param [in] point_num Número do ponto, intervalo [1~6]
     * @return Código de erro
     */
    errno_t SetToolPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o sistema de coordenadas da ferramenta
     * @param [out] tcp_pose Sistema de coordenadas da ferramenta
     * @return Código de erro
     */
    errno_t ComputeTool(DescPose *tcp_pose);

Definir Ponto de Referência da Ferramenta - Método dos Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o ponto de referência da ferramenta - método dos quatro pontos
     * @param [in] point_num Número do ponto, intervalo [1~4]
     * @return Código de erro
     */
    errno_t SetTcp4RefPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o sistema de coordenadas da ferramenta
     * @param [out] tcp_pose Sistema de coordenadas da ferramenta
     * @return Código de erro
     */
    errno_t ComputeTcp4(DescPose *tcp_pose);

Calcular Sistema de Coordenadas da Ferramenta com Base em Informações de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Calcula o sistema de coordenadas da ferramenta com base em informações de pontos
     * @param [in] method Método de cálculo; 0-método dos quatro pontos; 1-método dos seis pontos
     * @param [in] pos Grupo de posições das juntas, comprimento do array é 4 para o método dos quatro pontos e 6 para o método dos seis pontos
     * @param [out] coord Resultado do sistema de coordenadas da ferramenta
     * @return Código de erro
    */
    errno_t ComputeToolCoordWithPoints(int method, JointPos pos[], DescPose& coord);

Definir Sistema de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Define o sistema de coordenadas da ferramenta
     * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
     * @param  [in] coord  Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
     * @param  [in] type  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
     * @param  [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
     * @param  [in] toolID ID da ferramenta
     * @param  [in] loadNum Número da carga
     * @return  Código de erro
     */
    errno_t SetToolCoord(int id, DescPose *coord, int type, int install, int toolID, int loadNum);

Definir Lista de Sistemas de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Define a lista de sistemas de coordenadas da ferramenta
     * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
     * @param  [in] coord  Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
     * @param  [in] type  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
     * @param  [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
     * @param  [in] loadNum Número da carga
     * @return  Código de erro
     */
    errno_t SetToolList(int id, DescPose *coord, int type, int install, int loadNum);

Obter Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o sistema de coordenadas da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do sistema de coordenadas da ferramenta
    * @return  Código de erro
    */
    errno_t  GetTCPOffset(uint8_t flag, DescPose *desc_pos);

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestTCPCompute(void)
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
         DescPose p1Desc(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
         JointPos p1Joint(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);
         DescPose p2Desc(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
         JointPos p2Joint(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);
         DescPose p3Desc(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
         JointPos p3Joint(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);
         DescPose p4Desc(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
         JointPos p4Joint(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);
         DescPose p5Desc(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
         JointPos p5Joint(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);
         DescPose p6Desc(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
         JointPos p6Joint(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         JointPos posJ[6] = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
         DescPose coordRtn = {};
         rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);
         printf("ComputeToolCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(3);
         robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(4);
         robot.MoveJ(&p5Joint, &p5Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(5);
         robot.MoveJ(&p6Joint, &p6Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(6);
         rtn = robot.ComputeTool(&coordRtn);
         printf("6 Point ComputeTool        %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetToolList(1, &coordRtn, 0, 0, 0);
         robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(3);
         robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(4);
         rtn = robot.ComputeTcp4(&coordRtn);
         printf("4 Point ComputeTool        %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetToolCoord(2, &coordRtn, 0, 0, 1, 0);
         DescPose getCoord = {};
         rtn = robot.GetTCPOffset(0, &getCoord);
         printf("GetTCPOffset    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.CloseRPC();
         return 0;
     }

Definir Ponto de Referência da Ferramenta Externa - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o ponto de referência da ferramenta externa - método dos seis pontos
     * @param [in] point_num Número do ponto, intervalo [1~4]
     * @return Código de erro
     */
    errno_t SetExTCPPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o sistema de coordenadas da ferramenta externa
     * @param [out] tcp_pose Sistema de coordenadas da ferramenta externa
     * @return Código de erro
     */
    errno_t ComputeExTCF(DescPose *tcp_pose);

Definir Sistema de Coordenadas da Ferramenta Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o sistema de coordenadas da ferramenta externa
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] etcp  Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param  [in] etool  Pendente
    * @return  Código de erro
    */
    errno_t  SetExToolCoord(int id, DescPose *etcp, DescPose *etool);

Definir Lista de Sistemas de Coordenadas da Ferramenta Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a lista de sistemas de coordenadas da ferramenta externa
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] etcp  Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param  [in] etool  Pendente
    * @return  Código de erro
    */
    errno_t  SetExToolList(int id, DescPose *etcp, DescPose *etool);

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta Externa do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestExtCoord(void)
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
       DescPose p1Desc(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
       JointPos p1Joint(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);
       DescPose p2Desc(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
       JointPos p2Joint(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);
       DescPose p3Desc(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
       JointPos p3Joint(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);
       ExaxisPos exaxisPos(0, 0, 0, 0);
       DescPose offdese(0, 0, 0, 0, 0, 0);
       DescPose posTCP[3] = { p1Desc , p2Desc , p3Desc };
       DescPose coordRtn = {};
       robot.MoveJ(&p1Joint, &p1Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(1);
       robot.MoveJ(&p2Joint, &p2Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(2);
       robot.MoveJ(&p3Joint, &p3Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(3);
       rtn = robot.ComputeExTCF(&coordRtn);
       printf("ComputeExTCF          %d coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
       robot.SetExToolCoord(1, &coordRtn, &offdese);
       robot.SetExToolList(1, &coordRtn, &offdese);
       robot.CloseRPC();
       return 0;
    }

Definir Ponto de Referência da Peça - Método dos Três Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Define o ponto de referência da peça - método dos três pontos
     * @param [in] point_num Número do ponto, intervalo [1~3]
     * @return Código de erro
     */
    errno_t SetWObjCoordPoint(int point_num);

Calcular Sistema de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Calcula o sistema de coordenadas da peça
     * @param [in] method Método de cálculo 0: origem-eixo x-eixo z  1: origem-eixo x-plano xy
     * @param [in] refFrame Sistema de coordenadas de referência
     * @param [out] wobj_pose Sistema de coordenadas da peça
     * @return Código de erro
     */
    errno_t ComputeWObjCoord(int method, int refFrame, DescPose *wobj_pose);

Definir Sistema de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Define o sistema de coordenadas da peça
     * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
     * @param  [in] coord  Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade
     * @param  [in] refFrame Sistema de coordenadas de referência
     * @return  Código de erro
     */
    errno_t SetWObjCoord(int id, DescPose *coord, int refFrame);

Definir Lista de Sistemas de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Define a lista de sistemas de coordenadas da peça
     * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
     * @param  [in] coord  Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade
     * @param  [in] refFrame Sistema de coordenadas de referência
     * @return  Código de erro
     */
    errno_t SetWObjList(int id, DescPose *coord, int refFrame);

Calcular Sistema de Coordenadas da Peça com Base em Informações de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Calcula o sistema de coordenadas da peça com base em informações de pontos
     * @param [in] method Método de cálculo; 0: origem-eixo x-eixo z  1: origem-eixo x-plano xy
     * @param [in] pos Grupo de três posições TCP
     * @param [in] refFrame Sistema de coordenadas de referência
     * @param [out] coord Resultado do sistema de coordenadas da ferramenta
     * @return Código de erro
    */
    errno_t ComputeWObjCoordWithPoints(int method, DescPose pos[], int refFrame, DescPose& coord);

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o sistema de coordenadas da peça atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do sistema de coordenadas da peça
    * @return  Código de erro
    */
    errno_t  GetWObjOffset(uint8_t flag, DescPose *desc_pos);

Exemplo de Código para Operações do Sistema de Coordenadas da Peça do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestWobjCoord(void)
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
         DescPose p1Desc(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
         JointPos p1Joint(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);
         DescPose p2Desc(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
         JointPos p2Joint(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);
         DescPose p3Desc(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
         JointPos p3Joint(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         DescPose posTCP[3] = { p1Desc , p2Desc , p3Desc };
         DescPose coordRtn = {};
         rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);
         printf("ComputeWObjCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.MoveJ(&p1Joint, &p1Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(3);
         rtn = robot.ComputeWObjCoord(1, 0, &coordRtn);
         printf("ComputeWObjCoord                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetWObjCoord(1, &coordRtn, 0);
         robot.SetWObjList(1, &coordRtn, 0);
         DescPose getWobjDesc = {};
         rtn = robot.GetWObjOffset(0, &getWobjDesc);
         printf("GetWObjOffset                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.CloseRPC();
         return 0;
     }

Definir Velocidade Global
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a velocidade global
    * @param  [in]  vel  Percentagem de velocidade, intervalo [0~100]
    * @return  Código de erro
    */
    errno_t  SetSpeed(int vel);

Definir Aceleração do Robô
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Define a aceleração do robô
     * @param [in] acc Percentagem de aceleração do robô
     * @return Código de erro
     */
    errno_t SetOaccScale(double acc);

Obter Velocidade Padrão do Robô
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a velocidade padrão do robô
    * @param  [out]  vel  Velocidade, em mm/s
    * @return  Código de erro
    */
    errno_t  GetDefaultTransVel(float *vel);

Definir Peso da Carga na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief  Define o peso da carga na extremidade
     * @param  [in] loadNum Número da carga
     * @param  [in] weight  Peso da carga, em kg
     * @return  Código de erro
    */
    errno_t SetLoadWeight(int loadNum = 0, float weight);

Definir Coordenadas do Centro de Massa da Carga na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Define as coordenadas do centro de massa da carga na extremidade
    * @param [in] loadNum Número da carga
    * @param [in] coord Coordenadas do centro de massa, em mm
    * @return Código de erro
    */
    errno_t SetLoadCoord(int loadNum, DescTran* coord);

Obter Peso da Carga Atual
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o peso da carga atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] weight Peso da carga, em kg
    * @return  Código de erro
    */
    errno_t  GetTargetPayload(uint8_t flag, float *weight);

Obter Centro de Massa da Carga Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o centro de massa da carga atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] cog Centro de massa da carga, em mm
    * @return  Código de erro
    */
    errno_t  GetTargetPayloadCog(uint8_t flag, DescTran *cog);

Definir Modo de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o modo de instalação do robô
    * @param  [in] install  Modo de instalação, 0-montagem normal, 1-montagem lateral, 2-montagem invertida
    * @return  Código de erro
    */
    errno_t  SetRobotInstallPos(uint8_t install);

Definir Ângulo de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o ângulo de instalação do robô, instalação livre
    * @param  [in] yangle  Ângulo de inclinação
    * @param  [in] zangle  Ângulo de rotação
    * @return  Código de erro
    */
    errno_t  SetRobotInstallAngle(double yangle, double zangle);

Obter Ângulo de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o ângulo de instalação do robô
    * @param  [out] yangle Ângulo de inclinação
    * @param  [out] zangle Ângulo de rotação
    * @return  Código de erro
    */
    errno_t  GetRobotInstallAngle(float *yangle, float *zangle);

Definir Valor de Variável do Sistema
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o valor da variável do sistema
    * @param  [in]  id  Número da variável, intervalo [1~20]
    * @param  [in]  value Valor da variável
    * @return  Código de erro
    */
    errno_t  SetSysVarValue(int id, float value);

Obter Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o valor da variável do sistema
    * @param  [in] id Número da variável do sistema, intervalo [1~20]
    * @param  [out] value  Valor da variável do sistema
    * @return  Código de erro
    */
    errno_t  GetSysVarValue(int id, float *value);

Exemplo de Código para Configurações Comuns do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestLoadInstall(void)
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
         for (int i = 1; i < 100; i++)
         {
             robot.SetSpeed(i);
             robot.SetOaccScale(i);
             robot.Sleep(30);
         }
         float defaultVel = 0.0;
         robot.GetDefaultTransVel(&defaultVel);
         printf("GetDefaultTransVel is %f\n", defaultVel);
         for (int i = 1; i < 21; i++)
         {
             robot.SetSysVarValue(i, i + 0.5);
             robot.Sleep(100);
         }
         for (int i = 1; i < 21; i++)
         {
             float value = 0;
             robot.GetSysVarValue(i, &value);
             printf("sys value  %d is :%f\n", i, value);
             robot.Sleep(100);
         }
         robot.SetLoadWeight(0, 2.5);
         DescTran loadCoord = {};
         loadCoord.x = 3.0;
         loadCoord.y = 4.0;
         loadCoord.z = 5.0;
         robot.SetLoadCoord(&loadCoord);
         robot.Sleep(1000);
         float getLoad = 0.0;
         robot.GetTargetPayload(0, &getLoad);
         DescTran getLoadTran = {};
         robot.GetTargetPayloadCog(0, &getLoadTran);
         printf("get load is %f; get load cog is %f %f %f\n", getLoad, getLoadTran.x, getLoadTran.y, getLoadTran.z);
         robot.SetRobotInstallPos(0);
         robot.SetRobotInstallAngle(15.0, 25.0);
         float anglex = 0.0;
         float angley = 0.0;
         robot.GetRobotInstallAngle(&anglex, &angley);
         printf("GetRobotInstallAngle x:  %f;  y:  %f\n", anglex, angley);
         robot.CloseRPC();
         return 0;
     }

Chave de Compensação de Atrito das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Chave de compensação de atrito das juntas
    * @param  [in]  state  0-desligar, 1-ligar
    * @return  Código de erro
    */
    errno_t  FrictionCompensationOnOff(uint8_t state);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Normal
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o coeficiente de compensação de atrito das juntas - montagem normal
    * @param  [in]  coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    errno_t  SetFrictionValue_level(float coeff[6]);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Lateral
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o coeficiente de compensação de atrito das juntas - montagem lateral
    * @param  [in]  coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    errno_t  SetFrictionValue_wall(float coeff[6]);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Invertida
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o coeficiente de compensação de atrito das juntas - montagem invertida
    * @param  [in]  coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    errno_t  SetFrictionValue_ceiling(float coeff[6]);

Definir Coeficiente de Compensação de Atrito das Juntas - Instalação Livre
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o coeficiente de compensação de atrito das juntas - instalação livre
    * @param  [in]  coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    errno_t  SetFrictionValue_freedom(float coeff[6]);

Exemplo de Código para Configuração de Compensação de Atrito das Juntas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFriction(void)
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
       float lcoeff[6] = { 0.9,0.9,0.9,0.9,0.9,0.9 };
       float wcoeff[6] = { 0.4,0.4,0.4,0.4,0.4,0.4 };
       float ccoeff[6] = { 0.6,0.6,0.6,0.6,0.6,0.6 };
       float fcoeff[6] = { 0.5,0.5,0.5,0.5,0.5,0.5 };
       rtn = robot.FrictionCompensationOnOff(1);
       printf("FrictionCompensationOnOff rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_level(lcoeff);
       printf("SetFrictionValue_level rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_wall(wcoeff);
       printf("SetFrictionValue_wall rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_ceiling(ccoeff);
       printf("SetFrictionValue_ceiling rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_freedom(fcoeff);
       printf("SetFrictionValue_freedom rtn is %d\n", rtn);
       robot.CloseRPC();
       return 0;
    }

Consultar Código de Erro do Robô
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  Consulta o código de erro do robô
     * @param  [out]  maincode  Código de erro principal
     * @param  [out]  subcode   Código de erro secundário
     * @return  Código de erro
     */
    errno_t  GetRobotErrorCode(int *maincode, int *subcode);

Limpar Estado de Erro
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Limpa o estado de erro
    * @return  Código de erro
    */
    errno_t  ResetAllError();

Exemplo de Código para Obter Estado de Falha e Limpar Erro do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGetError(void)
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
       int maincode, subcode;
       robot.GetRobotErrorCode(&maincode, &subcode);
       printf("robot maincode is %d; subcode is %d\n", maincode, subcode);
       robot.ResetAllError();
       robot.Sleep(1000);
       robot.GetRobotErrorCode(&maincode, &subcode);
       printf("robot maincode is %d; subcode is %d\n", maincode, subcode);
       robot.CloseRPC();
       return 0;
    }

Definir Parâmetros de Monitoramento de Temperatura e Corrente da Ventoinha da Caixa de Controle de Larga Tensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros de monitoramento de temperatura e corrente da ventoinha da caixa de controle de larga tensão
    * @param [in] enable 0-desativar monitoramento; 1-ativar monitoramento
    * @param [in] period Período de monitoramento (s), intervalo 1-100
    * @return Código de erro
    */
    errno_t SetWideBoxTempFanMonitorParam(int enable, int period);

Obter Parâmetros de Monitoramento de Temperatura e Corrente da Ventoinha da Caixa de Controle de Larga Tensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os parâmetros de monitoramento de temperatura e corrente da ventoinha da caixa de controle de larga tensão
    * @param [out] enable 0-desativar monitoramento; 1-ativar monitoramento
    * @param [out] period Período de monitoramento (s), intervalo 1-100
    * @return Código de erro
    */
    errno_t GetWideBoxTempFanMonitorParam(int &enable, int &period);

Exemplo de Código para Obter Estado de Temperatura e Corrente da Ventoinha da Caixa de Controle de Larga Tensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestWideVoltageCtrlBoxtemp(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         printf("robot rpc rtn is %d\n", rtn);
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         robot.SetWideBoxTempFanMonitorParam(1, 2);
         int enable = 0;
         int period = 0;
         robot.GetWideBoxTempFanMonitorParam(enable, period);
         printf("GetWideBoxTempFanMonitorParam enable is %d   period is %d\n", enable, period);
         for (int i = 0; i < 100; i++)
         {
             robot.GetRobotRealTimeState(&pkg);
             printf("robot ctrl box temp is %f,  fan current is %d\n", pkg.wideVoltageCtrlBoxTemp, pkg.wideVoltageCtrlBoxFanCurrent);
             robot.Sleep(100);
         }
         rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
         printf("SetWideBoxTempFanMonitorParam rtn is %d\n", rtn);
         enable = 0;
         period = 0;
         robot.GetWideBoxTempFanMonitorParam(enable, period);
         printf("GetWideBoxTempFanMonitorParam enable is %d   period is %d\n", enable, period);
         for (int i = 0; i < 100; i++)
         {
             robot.GetRobotRealTimeState(&pkg);
             printf("robot ctrl box temp is %f,  fan current is %d\n", pkg.wideVoltageCtrlBoxTemp, pkg.wideVoltageCtrlBoxFanCurrent);
             robot.Sleep(100);
         }
         robot.CloseRPC();
         robot.Sleep(2000);
         return 0;
     }

Calcular Resultado da Calibração do Foco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calcula o resultado da calibração do foco
    * @param [in] pointNum Número de pontos de calibração
    * @param [out] resultPos Resultado da calibração XYZ
    * @param [out] accuracy Erro de precisão da calibração
    * @return Código de erro
    */
    errno_t ComputeFocusCalib(int pointNum, DescTran& resultPos, float& accuracy);

Definir Coordenadas do Foco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define as coordenadas do foco
    * @param [in] pos Coordenadas do foco XYZ
    * @return Código de erro
    */
    errno_t SetFocusPosition(DescTran pos);

Iniciar Rastreamento do Foco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Inicia o rastreamento do foco
    * @param [in] kp Parâmetro proporcional, padrão 50.0
    * @param [in] kpredict Parâmetro feedforward, padrão 19.0
    * @param [in] aMax Limite máximo de aceleração angular, padrão 1440°/s^2
    * @param [in] vMax Limite máximo de velocidade angular, padrão 180°/s
    * @param [in] type Travar a direção do eixo X (0-vetor de entrada de referência; 1-horizontal; 2-vertical)
    * @return Código de erro
    */
    errno_t FocusStart(double kp, double kpredict, double aMax, double vMax, int type);

Parar Rastreamento do Foco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Para o rastreamento do foco
    * @return Código de erro
    */
    errno_t FocusEnd();

Exemplo de Código de Rastreamento do Foco do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestFocus()
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
      DescPose p1Desc(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
      JointPos p1Joint(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);
      DescPose p2Desc(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
      JointPos p2Joint(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);
      DescPose p3Desc(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
      JointPos p3Joint(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);
      DescPose p4Desc(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
      JointPos p4Joint(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);
      DescPose p5Desc(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
      JointPos p5Joint(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);
      DescPose p6Desc(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
      JointPos p6Joint(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 100, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(1);
      robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(2);
      robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(3);
      robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(4);
      DescPose coordRtn = {};
      rtn = robot.ComputeTcp4(&coordRtn);
      printf("4 Point ComputeTool    %d coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
      robot.SetToolCoord(1, &coordRtn, 0, 0, 1, 0);
      robot.GetForwardKin(&p1Joint, &p1Desc);
      robot.GetForwardKin(&p2Joint, &p2Desc);
      robot.GetForwardKin(&p3Joint, &p3Desc);
      robot.SetFocusCalibPoint(1, p1Desc);
      robot.SetFocusCalibPoint(2, p2Desc);
      robot.SetFocusCalibPoint(3, p3Desc);
      DescTran resultPos = {};
      float accuracy = 0.0;
      rtn = robot.ComputeFocusCalib(3, resultPos, accuracy);
      printf("ComputeFocusCalib coord is %d %f %f %f accuracy is %f\n", rtn, resultPos.x, resultPos.y, resultPos.z, accuracy);
      rtn = robot.SetFocusPosition(resultPos);
      robot.GetForwardKin(&p5Joint, &p5Desc);
      robot.GetForwardKin(&p6Joint, &p6Desc);
      robot.MoveL(&p5Joint, &p5Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.MoveL(&p6Joint, &p6Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.FocusStart(50, 19, 710, 90, 0);
      robot.MoveL(&p5Joint, &p5Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.MoveL(&p6Joint, &p6Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.FocusEnd();
      robot.CloseRPC();
      return 0;
    }

Ativar Função de Calibração de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Ativa a função de calibração de sensibilidade do sensor de torque das juntas
    * @param [in] status 0-desativar; 1-ativar
    * @return  Código de erro
    */
    errno_t JointSensitivityEnable(int status);

Coleta de Dados de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Coleta de dados de sensibilidade do sensor de torque das juntas
    * @return Código de erro
    */
    errno_t JointSensitivityCollect();

Obter Resultado da Calibração de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o resultado da calibração de sensibilidade do sensor de torque das juntas
    * @param [out] calibResult Sensibilidade das juntas j1~j6 [0-1]
    * @param [out] linearityn Linearidade das juntas j1~j6 [0-1]
    * @return Código de erro
    */
    errno_t JointSensitivityCalibration(double calibResult[6], double linearity[6]);

Obter Erro de Histerese do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o erro de histerese do sensor de torque das juntas
    * @param [out] hysteresisError Erro de histerese das juntas j1~j6
    * @return Código de erro
    */
    errno_t JointHysteresisError(double hysteresisError[6]);

Obter Repetibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a repetibilidade do sensor de torque das juntas
    * @param [out] repeatability Repetibilidade do sensor de torque das juntas j1~j6
    * @return Código de erro
    */
    errno_t JointRepeatability(double repeatability[6]);

Definir Parâmetros do Sensor de Força das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros do sensor de força das juntas
    * @param [in] M Coeficiente de massa J1-J6 [0.001 ~ 10]
    * @param [in] B Coeficiente de amortecimento J1-J6 [0.001 ~ 10]
    * @param [in] K Coeficiente de rigidez J1-J6 [0.001 ~ 10]
    * @param [in] threshold Limiar de controle de força, Nm
    * @param [in] sensitivity Sensibilidade, Nm/V, [0 ~ 10]
    * @param [in] setZeroFlag Flag de ativação da função; 0-desativar; 1-ativar; 2-registrar ponto zero na posição 1; 3-registrar ponto zero na posição 2
    * @return Código de erro
    */
    errno_t SetAdmittanceParams(double M[6], double B[6], double K[6], double threshold[6], double sensitivity[6], int setZeroFlag);

Exemplo de Código para Calibração Automática de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSensitivityCalib()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 30000, 500);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return 0;
        }
        rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        printf("JointSensitivityEnable rtn is %d\n", rtn);
        JointPos curJPos = {};
        robot.GetActualJointPosDegree(0, &curJPos);
        ExaxisPos epos = { 0,0,0,0 };
        DescPose offset_pos = { 0,0,0,0,0,0 };
        JointPos jointPos1 = { curJPos.jPos[0], 0, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos1 = {};
        robot.GetForwardKin(&jointPos1, &descPos1);
        robot.MoveJ(&jointPos1, &descPos1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 1 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos2 = { curJPos.jPos[0], -30, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos2 = {};
        robot.GetForwardKin(&jointPos2, &descPos2);
        robot.MoveJ(&jointPos2, &descPos2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 2 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos3 = { curJPos.jPos[0], -60, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos3 = {};
        robot.GetForwardKin(&jointPos3, &descPos3);
        robot.MoveJ(&jointPos3, &descPos3, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 3 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos4 = { curJPos.jPos[0], -90, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos4 = {};
        robot.GetForwardKin(&jointPos4, &descPos4);
        robot.MoveJ(&jointPos4, &descPos4, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 4 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos5 = { curJPos.jPos[0], -120, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos5 = {};
        robot.GetForwardKin(&jointPos5, &descPos5);
        robot.MoveJ(&jointPos5, &descPos5, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 5 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos6 = { curJPos.jPos[0], -150, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos6 = {};
        robot.GetForwardKin(&jointPos6, &descPos6);
        robot.MoveJ(&jointPos6, &descPos6, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 6 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos7 = { curJPos.jPos[0], -180, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos7 = {};
        robot.GetForwardKin(&jointPos7, &descPos7);
        robot.MoveJ(&jointPos7, &descPos7, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 7 rtn is %d\n", rtn);
        robot.Sleep(100);
        //-------------------
        robot.MoveJ(&jointPos6, &descPos6, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 8 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos5, &descPos5, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 9 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos4, &descPos4, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 10 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos3, &descPos3, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 11 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos2, &descPos2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 12 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos1, &descPos1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 13 rtn is %d\n", rtn);
        robot.Sleep(100);
        double calibResult[6] = { 0.0 };
        double linearity[6] = { 0.0 };
        rtn = robot.JointSensitivityCalibration(calibResult, linearity);
        printf("JointSensitivityCalibration rtn is %d\n", rtn);
        rtn = robot.JointSensitivityEnable(0);
        printf("JointSensitivityEnable rtn is %d\n", rtn);
        printf("jointSensor Calib result is %f %f %f %f %f %f\njointSensor linearity is %f %f %f %f %f %f\n",
            calibResult[0], calibResult[1], calibResult[2],
            calibResult[3], calibResult[4], calibResult[5],
            linearity[0], linearity[1], linearity[2],
            linearity[3], linearity[4], linearity[5]);
        double hysteresisError[6] = { 0.0 };
        rtn = robot.JointHysteresisError(hysteresisError);
        printf("JointHysteresisError result is %f %f %f %f %f %f\n",
            hysteresisError[0], hysteresisError[1], hysteresisError[2],
            hysteresisError[3], hysteresisError[4], hysteresisError[5]);
        double repeatability[6] = { 0.0 };
        rtn = robot.JointRepeatability(repeatability);
        printf("JointRepeatability result is %f %f %f %f %f %f\n",
            repeatability[0], repeatability[1], repeatability[2],
            repeatability[3], repeatability[4], repeatability[5]);
        double M[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double B[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double K[6] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double threshold[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        printf("SetAdmittanceParams rtn is %d\n", rtn);
        robot.CloseRPC();
    }

Obter Número de Quadros com Erro nas 8 Portas Escravas do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o número de quadros com erro nas 8 portas escravas do robô
    * @param [out] inRecvErr Número de quadros com erro de receção de entrada
    * @param [out] inCRCErr Número de quadros com erro CRC de entrada
    * @param [out] inTransmitErr Número de quadros com erro de transmissão de entrada
    * @param [out] inLinkErr Número de quadros com erro de ligação de entrada
    * @param [out] outRecvErr Número de quadros com erro de receção de saída
    * @param [out] outCRCErr Número de quadros com erro CRC de saída
    * @param [out] outTransmitErr Número de quadros com erro de transmissão de saída
    * @param [out] outLinkErr Número de quadros com erro de ligação de saída
    * @return Código de erro
    */
    errno_t GetSlavePortErrCounter(int inRecvErr[8], int inCRCErr[8], int inTransmitErr[8], int inLinkErr[8], int outRecvErr[8], int outCRCErr[8], int outTransmitErr[8], int outLinkErr[8]);

Limpar Quadros com Erro nas Portas Escravas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Limpa os quadros com erro nas portas escravas
    * @param [in] slaveID ID da escrava 0~7
    * @return Código de erro
    */
    errno_t SlavePortErrCounterClear(int slaveID);

Exemplo de Código para Obter Quadros com Erro nas Portas Escravas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSlavePortErr()
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
        int inRecvErr[8] = {0.0};
        int inCRCErr[8] = { 0.0 };
        int inTransmitErr[8] = { 0.0 };
        int inLinkErr[8] = { 0.0 };
        int outRecvErr[8] = { 0.0 };
        int outCRCErr[8] = { 0.0 };
        int outTransmitErr[8] = { 0.0 };
        int outLinkErr[8] = { 0.0 };
        robot.GetSlavePortErrCounter(inRecvErr,  inCRCErr, inTransmitErr, inLinkErr,
            outRecvErr, outCRCErr, outTransmitErr, outLinkErr);
        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inRecvErr[i]);
            }
            if (inCRCErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inCRCErr[i]);
            }
            if (inTransmitErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inTransmitErr[i]);
            }
            if (inLinkErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inLinkErr[i]);
            }
            if (outRecvErr[i] != 0)
            {
                printf("outRecvErr %d is %d\n", i, outRecvErr[i]);
            }
            if (outCRCErr[i] != 0)
            {
                printf("outCRCErr %d is %d\n", i, outCRCErr[i]);
            }
            if (outTransmitErr[i] != 0)
            {
                printf("outTransmitErr %d is %d\n", i, outTransmitErr[i]);
            }
            if (outLinkErr[i] != 0)
            {
                printf("outLinkErr %d is %d\n", i, outLinkErr[i]);
            }
        }
        printf("others has no err!\n");
        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }
        robot.CloseRPC();
        return 0;
    }

Definir Coeficiente de Feedforward de Velocidade por Eixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o coeficiente de feedforward de velocidade por eixo
    * @param [in] radio Coeficiente de feedforward de velocidade por eixo
    * @return Código de erro
    */
    errno_t SetVelFeedForwardRatio(double radio[6]);

Obter Coeficiente de Feedforward de Velocidade por Eixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o coeficiente de feedforward de velocidade por eixo
    * @param [out] radio Coeficiente de feedforward de velocidade por eixo
    * @return Código de erro
    */
    errno_t GetVelFeedForwardRatio(double radio[6]);

Exemplo de Código do Coeficiente de Feedforward de Velocidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestVelFeedForwardRatio()
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
        double setRadio[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double getRadio[6] = { 0.0 };
        robot.GetVelFeedForwardRatio(getRadio);
        printf(" %f %f %f %f %f %f\n", getRadio[0], getRadio[1], getRadio[2], getRadio[3], getRadio[4], getRadio[5]);
        robot.CloseRPC();
        return 0;
    }

Calibração TCP do Sensor Fotoelétrico - Calcular RPY da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - calcular RPY da ferramenta
    * @param [in] Btool Posição cartesiana do robô
    * @param [in] Etool Valor atual do sistema de coordenadas da ferramenta
    * @param [in] senser Valor atual do sistema de coordenadas do sensor (não disponível no momento)
    * @param [in] radius Raio do movimento circular mm (não disponível no momento)
    * @param [in] dz Distância de movimento na direção negativa do eixo z do sistema de coordenadas base; quando dz = 10000, a função retorna diretamente o RPY da ferramenta
    * @param [out] TCPRPY Valor RPY da ferramenta
    * @return Código de erro
    */
    errno_t TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, Rpy& TCPRPY);

Calibração TCP do Sensor Fotoelétrico - Calcular XYZ da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - calcular XYZ da ferramenta
    * @param [in] select 0-calcular TCP da ferramenta; 1-calcular origem do sensor; 2-calcular postura do sensor; 3-retornar diretamente o TCP da ferramenta; 4-registrar o sistema de coordenadas atual da peça e da ferramenta
    * @param [in] originDirection 0-Direção X; 1-Direção Y; 2-Direção Z
    * @param [in] pos1 Posição cartesiana do robô 1
    * @param [in] pos2 Posição cartesiana do robô 2
    * @param [in] pos3 Posição cartesiana do robô 3
    * @param [in] pos4 Posição cartesiana do robô 4
    * @param [out] TCP Valor XYZ da ferramenta
    * @return Código de erro
    */
    errno_t TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2, DescTran pos3, DescTran pos4, DescTran& TCP);

Calibração TCP do Sensor Fotoelétrico - Iniciar Gravação da Posição do Centro do Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - iniciar gravação da posição do centro do flange da extremidade
    * @return Código de erro
    */
    errno_t TCPRecordFlangePosStart();

Calibração TCP do Sensor Fotoelétrico - Parar Gravação da Posição do Centro do Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - parar gravação da posição do centro do flange da extremidade
    * @return Código de erro
    */
    errno_t TCPRecordFlangePosEnd();

Calibração TCP do Sensor Fotoelétrico - Obter Posição do Centro da Ponta da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - obter posição do centro da ponta da ferramenta
    * @param [out] TCP Posição do centro da ponta da ferramenta (x, y, z)
    * @return Código de erro
    */
    errno_t TCPGetRecordFlangePos(DescTran& TCP);

Calibração TCP do Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico
    * @param [in] luaPath Caminho do programa lua para calibração automática:  "FR_CalibrateTheToolTcp.lua"
    * @param [in] offsetX Deslocamento do ponto de ensino (x, y, z) mm
    * @param [out] TCP Sistema de coordenadas da ferramenta calibrado (x, y, z, rx, ry, rz)
    * @return Código de erro
    */
    errno_t PhotoelectricSensorTCPCalibration(std::string luaPath, DescTran offset, DescPose& TCP);

Exemplo de Código para Calibração TCP do Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestPhotoelectricSensorTCPCalib(void)
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
        DescTran offset = { 10.0, 10.0, 3.0 };
        DescPose TCP = {};
        rtn = robot.PhotoelectricSensorTCPCalibration("FR_CalibrateTheToolTcp.lua", offset, TCP);
        printf("PhotoelectricSensorTCPCalibration rtn is  %d %f %f %f %f %f %f \n", rtn, TCP.tran.x, TCP.tran.y, TCP.tran.z, TCP.rpy.rx, TCP.rpy.ry, TCP.rpy.rz);
        robot.CloseRPC();
        robot.Sleep(9999999);
        return 0;
    }
    
Definir Velocidade Global em Tempo Real
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir velocidade global em tempo real
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @return Código de erro
    */
    errno_t SetSpeedInstant(int vel);   