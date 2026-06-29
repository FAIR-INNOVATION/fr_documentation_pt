Configurações Comuns do Robô
=====================================

.. toctree:: 
    :maxdepth: 5

Definir Ponto de Referência da Ferramenta - Método dos Seis Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir ponto de referência da ferramenta - método dos seis pontos
    * @param [in] point_num Número do ponto, intervalo [1~6]
    * @return Código de erro
    */ 
    int SetToolPoint(int point_num); 

Calcular Sistema de Coordenadas da Ferramenta - Método dos Seis Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Calcular sistema de coordenadas da ferramenta
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta
    * @return Código de erro
    */ 
    int ComputeTool(ref DescPose tcp_pose); 

Definir Ponto de Referência da Ferramenta - Método dos Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir ponto de referência da ferramenta - método dos quatro pontos
    * @param [in] point_num Número do ponto, intervalo [1~4]
    * @return Código de erro
    */ 
    int SetTcp4RefPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta - Método dos Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Calcular sistema de coordenadas da ferramenta
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta
    * @return Código de erro
    */ 
    int ComputeTcp4(ref DescPose tcp_pose);

Definir Sistema de Coordenadas da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir sistema de coordenadas da ferramenta
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] coord  Pose do ponto central da ferramenta em relação ao centro da flange da extremidade
    * @param  [in] type  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
    * @param  [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    * param   [in] toolID ID da ferramenta
    * @param  [in] loadNum Número da carga
    * @return  Código de erro
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);

Calcular Sistema de Coordenadas da Ferramenta com Base em Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Calcular sistema de coordenadas da ferramenta com base em pontos
    * @param [in] method Método de cálculo; 0-método dos quatro pontos; 1-método dos seis pontos
    * @param [in] pos Grupo de posições de junta, comprimento do array é 4 para o método dos quatro pontos e 6 para o método dos seis pontos
    * @return Código de erro
    */

    int ComputeToolCoordWithPoints(int method, JointPos[] pos, ref DescPose coordRtn)  

Definir Lista de Sistemas de Coordenadas da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir lista de sistemas de coordenadas da ferramenta
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] coord  Pose do ponto central da ferramenta em relação ao centro da flange da extremidade
    * @param  [in] type  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
    * @param  [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    * @param  [in] loadNum Número da carga
    * @return  Código de erro
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

Obter Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter sistema de coordenadas da ferramenta atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do sistema de coordenadas da ferramenta
    * @return  Código de erro
    */
    int GetTCPOffset(byte flag, ref DescPose desc_pos); 

Exemplo de Código de Operações do Sistema de Coordenadas da Ferramenta do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button18_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(186.331f, 487.913f, 209.850f, 149.030f, 0.688f, -114.347f);
        JointPos p1Joint = new JointPos(-127.876f, -75.341f, 115.417f, -122.741f, -59.820f, 74.300f);

        DescPose p2Desc = new DescPose(69.721f, 535.073f, 202.882f, -144.406f, -14.775f, -89.012f);
        JointPos p2Joint = new JointPos(-101.780f, -69.828f, 110.917f, -125.740f, -127.841f, 74.300f);

        DescPose p3Desc = new DescPose(146.861f, 578.426f, 205.598f, 175.997f, -36.178f, -93.437f);
        JointPos p3Joint = new JointPos(-112.851f, -60.191f, 86.566f, -80.676f, -97.463f, 74.300f);

        DescPose p4Desc = new DescPose(136.284f, 509.876f, 225.613f, 178.987f, 1.372f, -100.696f);
        JointPos p4Joint = new JointPos(-116.397f, -76.281f, 113.845f, -128.611f, -88.654f, 74.299f);

        DescPose p5Desc = new DescPose(138.395f, 505.972f, 298.016f, 179.134f, 2.147f, -101.110f);
        JointPos p5Joint = new JointPos(-116.814f, -82.333f, 109.162f, -118.662f, -88.585f, 74.302f);

        DescPose p6Desc = new DescPose(105.553f, 454.325f, 232.017f, -179.426f, 0.444f, -99.952f);
        JointPos p6Joint = new JointPos(-115.649f, -84.367f, 122.447f, -128.663f, -90.432f, 74.303f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = new JointPos[] { p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, ref coordRtn);
        Console.WriteLine($"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(4);
        robot.MoveJ( p5Joint,  p5Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(5);
        robot.MoveJ( p6Joint,  p6Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(6);
        rtn = robot.ComputeTool(ref coordRtn);
        Console.WriteLine($"6 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
        robot.SetToolList(1,  coordRtn, 0, 0, 0);

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose();
        rtn = robot.GetTCPOffset(0, ref getCoord);
        Console.WriteLine($"GetTCPOffset    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
    }

Definir Ponto de Referência da Ferramenta Externa - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir ponto de referência da ferramenta externa - método dos três pontos
    * @param [in] point_num Número do ponto, intervalo [1~3]
    * @return Código de erro
    */ 
    int SetExTCPPoint(int point_num); 

Calcular Sistema de Coordenadas da Ferramenta Externa - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief Calcular sistema de coordenadas da ferramenta externa - método dos três pontos
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta externa
    * @return Código de erro
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

Definir Sistema de Coordenadas da Ferramenta Externa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir sistema de coordenadas da ferramenta externa
    * @param [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param [in] etcp Pose do ponto central da ferramenta em relação ao centro da flange da extremidade
    * @param [in] etool A definir
    * @return Código de erro
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

Definir Lista de Sistemas de Coordenadas da Ferramenta Externa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir lista de sistemas de coordenadas da ferramenta externa
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] etcp  Pose do ponto central da ferramenta em relação ao centro da flange da extremidade
    * @param  [in] etool  A definir
    * @return  Código de erro
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

Calcular Sistema de Coordenadas da Peça com Base em Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Calcular sistema de coordenadas da peça com base em pontos
    * @param [in] method Método de cálculo; 0: origem-eixo X-eixo Z  1: origem-eixo X-plano XY
    * @param [in] pos Três posições TCP
    * @param [in] refFrame Sistema de coordenadas de referência
    * @return Código de erro
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, ref DescPose coordRtn)

Exemplo de Código de Operações do Sistema de Coordenadas da Ferramenta Externa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button20_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606f, 779.517f, 193.516f, 178.000f, 0.476f, -92.484f);
        JointPos p1Joint = new JointPos(-108.145f, -50.137f, 85.818f, -125.599f, -87.946f, 74.329f);

        DescPose p2Desc = new DescPose(-24.656f, 850.384f, 191.361f, 177.079f, -2.058f, -95.355f);
        JointPos p2Joint = new JointPos(-111.024f, -41.538f, 69.222f, -114.913f, -87.743f, 74.329f);

        DescPose p3Desc = new DescPose(-99.813f, 766.661f, 241.878f, -176.817f, 1.917f, -91.604f);
        JointPos p3Joint = new JointPos(-107.266f, -56.116f, 85.971f, -122.560f, -92.548f, 74.331f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(ref coordRtn);
        Console.WriteLine($"ComputeExTCF                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetExToolCoord(1,  coordRtn,  offdese);
        robot.SetExToolList(1,  coordRtn,  offdese);
    }

Definir Ponto de Referência do Sistema de Coordenadas da Peça - Método dos Três Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir ponto de referência da peça - método dos três pontos
    * @param [in] point_num Número do ponto, intervalo [1~3]  
    * @return Código de erro
    */ 
    int SetWObjCoordPoint(int point_num); 

Calcular Sistema de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Calcular sistema de coordenadas da peça
    * @param [in] method Método de cálculo 0: origem-eixo X-eixo Z  1: origem-eixo X-plano XY
    * @param [in] refFrame Sistema de coordenadas de referência
    * @param [out] wobj_pose Sistema de coordenadas da peça
    * @return Código de erro
    */
    int ComputeWObjCoord(int method, int refFrame, ref DescPose wobj_pose); 

Definir Sistema de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir sistema de coordenadas da peça
    * @param  [in] id Número do sistema de coordenadas, intervalo [1~15]
    * @param  [in] coord  Pose do sistema de coordenadas da peça em relação ao centro da flange da extremidade
    * @param  [in] refFrame Sistema de coordenadas de referência
    * @return  Código de erro
    */
    int SetWObjCoord(int id, DescPose coord, int refFrame);

Definir Lista de Sistemas de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir lista de sistemas de coordenadas da peça
    * @param  [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param  [in] coord  Pose do sistema de coordenadas da peça em relação ao centro da flange da extremidade
    * @param  [in] refFrame Sistema de coordenadas de referência
    * @return  Código de erro
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter sistema de coordenadas da peça atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] desc_pos Pose do sistema de coordenadas da peça
    * @return  Código de erro
    */   
    int GetWObjOffset(byte flag, ref DescPose desc_pos); 

Exemplo de Código de Operações do Sistema de Coordenadas da Peça do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button19_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint = new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc = new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint = new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc = new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint = new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint,ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoord                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetWObjCoord(1,  coordRtn, 0);
        robot.SetWObjList(1,  coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, ref getWobjDesc);
        Console.WriteLine($"GetWObjOffset                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");   
    } 

Definir Velocidade Global
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir velocidade global
    * @param  [in]  vel  Percentual de velocidade, intervalo [0~100]
    * @return  Código de erro
    */
    int SetSpeed(int vel); 

Definir Aceleração do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir aceleração do robô
    * @param [in] acc Percentual de aceleração do robô
    * @return Código de erro
    */
    int SetOaccScale(double acc)

Obter Velocidade Padrão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter velocidade padrão do robô
    * @param  [out]  vel  Velocidade, unidade mm/s
    * @return  Código de erro
    */   
    int GetDefaultTransVel(ref double vel); 

Definir Peso da Carga na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir peso da carga na extremidade
    * @param  [in] loadNum Número da carga
    * @param  [in] weight  Peso da carga, unidade kg
    * @return  Código de erro
    */
    int SetLoadWeight(int loadNum, float weight)

Definir Coordenadas do Centro de Massa da Carga na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir coordenadas do centro de massa da carga na extremidade
    * @param  [in] coord Coordenadas do centro de massa, unidade mm
    * @return  Código de erro
    */
    int SetLoadCoord(DescTran coord); 

Obter Peso da Carga Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter peso da carga atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] weight Peso da carga, unidade kg
    * @return  Código de erro
    */
    int GetTargetPayload(byte flag, ref double weight); 

Obter Centro de Massa da Carga Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter centro de massa da carga atual
    * @param  [in] flag 0-bloqueante, 1-não bloqueante
    * @param  [out] cog Centro de massa da carga, unidade mm
    * @return  Código de erro
    */   
    int GetTargetPayloadCog(byte flag, ref DescTran cog);

Definir Método de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir método de instalação do robô
    * @param  [in] install  Método de instalação, 0-montagem padrão (chão), 1-montagem na parede, 2-montagem invertida (teto)
    * @return  Código de erro
    */
    int SetRobotInstallPos(byte install); 

Definir Ângulo de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir ângulo de instalação do robô (instalação livre)
    * @param  [in] yangle  Ângulo de inclinação
    * @param  [in] zangle  Ângulo de rotação
    * @return  Código de erro
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

Obter Ângulo de Instalação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter ângulo de instalação do robô
    * @param  [out] yangle Ângulo de inclinação
    * @param  [out] zangle Ângulo de rotação
    * @return  Código de erro
    */
    int GetRobotInstallAngle(ref double yangle, ref double zangle); 

Definir Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir valor de variável do sistema
    * @param  [in]  id  Número da variável, intervalo [1~20]
    * @param  [in]  value Valor da variável
    * @return  Código de erro
    */
    int SetSysVarValue(int id, double value); 

Obter Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter valor de variável do sistema
    * @param  [in] id Número da variável do sistema, intervalo [1~20]
    * @param  [out] value  Valor da variável do sistema
    * @return  Código de erro
    */
    int GetSysVarValue(int id, ref double value); 

Exemplo de Código de Configurações Comuns do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button21_Click(object sender, EventArgs e)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            Thread.Sleep(30);
        }

        double defaultVel = 0.0f;
        robot.GetDefaultTransVel(ref defaultVel);
        Console.WriteLine($"GetDefaultTransVel is {defaultVel}");

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5f);
            Thread.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            double value = 0;
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value  {i} is :{value}");
            Thread.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5f);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0f;
        loadCoord.y = 4.0f;
        loadCoord.z = 5.0f;
        robot.SetLoadCoord( loadCoord);

        Thread.Sleep(1000);

        double getLoad = 0.0f;
        robot.GetTargetPayload(0, ref getLoad);

        DescTran getLoadTran = new DescTran();
        robot.GetTargetPayloadCog(0, ref getLoadTran);
        Console.WriteLine($"get load is {getLoad}; get load cog is {getLoadTran.x} {getLoadTran.y} {getLoadTran.z}");

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0f, 25.0f);

        double anglex = 0.0f;
        double angley = 0.0f;
        robot.GetRobotInstallAngle(ref anglex, ref angley);
        Console.WriteLine($"GetRobotInstallAngle x:  {anglex};  y:  {angley}");
    }

Interruptor de Compensação de Atrito das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Interruptor de compensação de atrito das juntas
    * @param [in] state 0-desligado, 1-ligado
    * @return Código de erro
    */ 
    int FrictionCompensationOnOff(byte state); 

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Padrão (Chão)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir coeficiente de compensação de atrito das juntas - montagem padrão (chão)
    * @param  [in]  coeff Coeficientes de compensação para as seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    int SetFrictionValue_level(double[] coeff);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem na Parede
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir coeficiente de compensação de atrito das juntas - montagem na parede
    * @param  [in]  coeff Coeficientes de compensação para as seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    int SetFrictionValue_wall(double[] coeff); 

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Invertida (Teto)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir coeficiente de compensação de atrito das juntas - montagem invertida (teto)
    * @param  [in]  coeff Coeficientes de compensação para as seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    int SetFrictionValue_ceiling(double[] coeff);

Definir Coeficiente de Compensação de Atrito das Juntas - Instalação Livre
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir coeficiente de compensação de atrito das juntas - instalação livre
    * @param  [in]  coeff Coeficientes de compensação para as seis juntas, intervalo [0~1]
    * @return  Código de erro
    */
    int SetFrictionValue_freedom(double[] coeff);

Exemplo de Código de Configuração de Compensação de Atrito das Juntas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] lcoeff = { 0.9f, 0.9f, 0.9f, 0.9f, 0.9f, 0.9f };
        double[] wcoeff = { 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f };
        double[] ccoeff = { 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f };
        double[] fcoeff = { 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f };

        int rtn = robot.FrictionCompensationOnOff(1);
        Console.WriteLine($"FrictionCompensationOnOff rtn is{rtn}");

        rtn = robot.SetFrictionValue_level(lcoeff);
        Console.WriteLine($"SetFrictionValue_level rtn is {rtn}");

        rtn = robot.SetFrictionValue_wall(wcoeff);
        Console.WriteLine($"SetFrictionValue_wall rtn is{rtn}");

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        Console.WriteLine($"SetFrictionValue_ceiling rtn is {rtn}");

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        Console.WriteLine($"SetFrictionValue_freedom rtn is {rtn}");
    }

Consultar Código de Erro do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Consultar código de erro do robô
    * @param [out] maincode   Código de erro principal
    * @param [out] subcode    Código de erro secundário
    * @return Código de erro
    */ 
    int GetRobotErrorCode(ref int maincode, ref int subcode);

Limpar Estado de Erro
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Limpar estado de erro
    * @return  Código de erro
    */
    int ResetAllError(); 

Exemplo de Código de Obtenção de Estado de Falha e Limpeza de Erro do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        int maincode=0, subcode=0;
        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is {subcode}" );

        robot.ResetAllError();

        Thread.Sleep(1000);

        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is{subcode}");
    }

Definir Parâmetros de Monitoramento de Temperatura e Velocidade do Ventilador para Painel de Controle de Tensão Ampla
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir parâmetros de monitoramento de temperatura e velocidade do ventilador para painel de controle de tensão ampla
    * @param [in] enable 0-desabilitar monitoramento; 1-habilitar monitoramento
    * @param [in] period Período de monitoramento (s), intervalo 1-100
    * @return Código de erro
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

Obter Parâmetros de Monitoramento de Temperatura e Velocidade do Ventilador para Painel de Controle de Tensão Ampla
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter parâmetros de monitoramento de temperatura e velocidade do ventilador para painel de controle de tensão ampla
    * @param [out] enable 0-desabilitar monitoramento; 1-habilitar monitoramento
    * @param [out] period Período de monitoramento (s), intervalo 1-100
    * @return Código de erro
    */
    int GetWideBoxTempFanMonitorParam(ref int enable, ref int period);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        var pkg = new ROBOT_STATE_PKG(); 
        robot.SetWideBoxTempFanMonitorParam(1, 2);    
        int enable = 0;
        int period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }       
        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
        Console.WriteLine($"SetWideBoxTempFanMonitorParam rtn is {rtn}");       
        enable = 0;
        period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($" robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }
    }

Definir Ponto de Calibração de Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir ponto de calibração de foco
    * @param [in] pointNum Número do ponto de calibração de foco 1-8
    * @param [in] point Coordenadas do ponto de calibração
    * @return Código de erro
    */
    int SetFocusCalibPoint(int pointNum, DescPose point);

Definir Posição do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir posição do foco
    * @param [in] pos Coordenadas XYZ do foco
    * @return Código de erro
    */
    int SetFocusPosition(DescTran pos);

Iniciar Rastreamento de Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Iniciar rastreamento de foco
    * @param [in] kp Parâmetro proporcional, padrão 50.0
    * @param [in] kpredict Parâmetro de feedforward, padrão 19.0
    * @param [in] aMax Limite máximo de aceleração angular, padrão 1440°/s^2
    * @param [in] vMax Limite máximo de velocidade angular, padrão 180°/s
    * @param [in] type Direção de apontamento do eixo X bloqueado (0-vetor de entrada de referência; 1-horizontal; 2-vertical)
    * @return Código de erro
    */
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type);

Parar Rastreamento de Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Parar rastreamento de foco
    * @return Código de erro
    */
    int FocusEnd();

Exemplo de Código de Rastreamento de Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    private void button81_Click(object sender, EventArgs e)
    {
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint = new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);
        DescPose p2Desc = new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint = new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);
        DescPose p3Desc = new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint = new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);
        DescPose p4Desc = new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint = new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);
        DescPose p5Desc = new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint = new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);
        DescPose p6Desc = new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint = new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 100, 0, 0, 0);
        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.GetForwardKin(p4Joint, ref p4Desc);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool      {rtn} coord is {coordRtn.tran.x} ,{coordRtn.tran.y} ,{coordRtn.tran.z} ,{coordRtn.rpy.rx} ,{coordRtn.rpy.ry} ,{coordRtn.rpy.rz} ");
        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);
        robot.GetForwardKin(p1Joint, ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);
        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double accuracy = 0.0;
        rtn = robot.ComputeFocusCalib(3, ref resultPos, ref accuracy);
        Console.WriteLine($"ComputeFocusCalib coord is  {rtn},{ resultPos.x} ,{ resultPos.y}, { resultPos.z}, accuracy is {accuracy} ");
        rtn = robot.SetFocusPosition(resultPos);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusEnd();
    }

Ativação da Função de Calibração de Sensibilidade do Sensor de Torque de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação da função de calibração de sensibilidade do sensor de torque de junta
    * @param [in] status 0-desligado; 1-ligado
    * @return   Código de erro
    */
    public int JointSensitivityEnable(int status);

Coleta de Dados de Sensibilidade do Sensor de Torque de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Coleta de dados de sensibilidade do sensor de torque de junta
    * @return Código de erro
    */
    public int JointSensitivityCollect();

Obter Resultado da Calibração de Sensibilidade do Sensor de Torque de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter resultado da calibração de sensibilidade do sensor de torque de junta
    * @param [out] calibResult Sensibilidade das juntas j1~j6 [0-1]
    * @param [out] linearityn Linearidade das juntas j1~j6 [0-1]
    * @return Código de erro
    */
    public int JointSensitivityCalibration(double calibResult[6], double linearity[6]);

Obter Erro de Histerese do Sensor de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter erro de histerese do sensor de torque de junta
    * @param [out] hysteresisError Erro de histerese das juntas j1~j6
    * @return Código de erro
    */
    public int JointHysteresisError(ref double[] hysteresisError);

Obter Repetibilidade do Sensor de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:
    
    /**
    * @brief Obter repetibilidade do sensor de torque de junta
    * @param [out] repeatability Repetibilidade do sensor de torque de junta para j1~j6
    * @return Código de erro
    */
    public int JointRepeatability(ref double[] repeatability);

Definir Parâmetros do Sensor de Força de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir parâmetros do sensor de força de junta
    * @param [in] M Coeficientes de massa J1-J6 [0.001 ~ 10]
    * @param [in] B Coeficientes de amortecimento J1-J6 [0.001 ~ 10]
    * @param [in] K Coeficientes de rigidez J1-J6 [0.001 ~ 10]
    * @param [in] threshold Limite de controle de força, Nm
    * @param [in] sensitivity Sensibilidade, Nm/V, [0 ~ 10]
    * @param [in] setZeroFlag Flag de ativação da função; 0-desligado; 1-ligado; 2-registrar ponto zero na posição 1; 3-registrar ponto zero na posição 2
    * @return Código de erro
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

Exemplo de Código de Calibração Automática de Sensibilidade do Sensor de Torque de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    public int TestSensitivityCalib()
    {
        int rtn; 
        rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");

        JointPos curJPos = new JointPos(0, 0, 0, 0, 0, 0);
        robot.GetActualJointPosDegree(0, ref curJPos);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        JointPos[] jointPoses = new JointPos[]
        {
            new JointPos(curJPos.jPos[0], 0, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -30, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -60, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -90, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -120, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -150, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -180, 0, -90, 0.02, curJPos.jPos[5])
        };
        for (int i = 0; i < jointPoses.Length; i++)
        {
            DescPose descPos = new DescPose(0, 0, 0, 0, 0, 0);
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            Thread.Sleep(i == 0 ? 200 : 100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {i + 1} rtn is {rtn}");
            Thread.Sleep(100);
        }

        for (int i = jointPoses.Length - 2; i >= 0; i--)
        {
            DescPose descPos = new DescPose();
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            Thread.Sleep(100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {jointPoses.Length + (jointPoses.Length - 1 - i)} rtn is {rtn}");
            Thread.Sleep(100);
        }
        double[] calibResult = new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(ref calibResult, ref linearity);
        Console.WriteLine($"JointSensitivityCalibration rtn is {rtn}");
        rtn = robot.JointSensitivityEnable(0);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");
        Console.WriteLine($"jointSensor Calib result is {calibResult[0]:F6} {calibResult[1]:F6} {calibResult[2]:F6} {calibResult[3]:F6} {calibResult[4]:F6} {calibResult[5]:F6}");
        Console.WriteLine($"jointSensor linearity is {linearity[0]:F6} {linearity[1]:F6} {linearity[2]:F6} {linearity[3]:F6} {linearity[4]:F6} {linearity[5]:F6}"); 
        double[] hysteresisError = new double[6];
        rtn = robot.JointHysteresisError(ref hysteresisError);
        Console.WriteLine($"JointHysteresisError result is {hysteresisError[0]:F6} {hysteresisError[1]:F6} {hysteresisError[2]:F6} {hysteresisError[3]:F6} {hysteresisError[4]:F6} {hysteresisError[5]:F6}");   
        double[] repeatability = new double[6];
        rtn = robot.JointRepeatability(ref repeatability);
        Console.WriteLine($"JointRepeatability result is {repeatability[0]:F6} {repeatability[1]:F6} {repeatability[2]:F6} {repeatability[3]:F6} {repeatability[4]:F6} {repeatability[5]:F6}");
        double[] M = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] B = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] K = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] threshold = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        Console.WriteLine($"SetAdmittanceParams rtn is {rtn}");
        robot.CloseRPC();
        return 0;
    }

Obter Número de Quadros de Erro nas 8 Portas Escravas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter número de quadros de erro nas 8 portas escravas do robô
    * @param [out] inRecvErr Número de erros de recepção de entrada 
    * @param [out] inCRCErr Número de erros CRC de entrada 
    * @param [out] inTransmitErr Número de erros de transmissão de entrada 
    * @param [out] inLinkErr Número de erros de link de entrada 
    * @param [out] outRecvErr Número de erros de recepção de saída
    * @param [out] outCRCErr Número de erros CRC de saída
    * @param [out] outTransmitErr Número de erros de transmissão de saída
    * @param [out] outLinkErr Número de erros de link de saída
    * @return Código de erro
    */
    public int GetSlavePortErrCounter(ref int[] inRecvErr,ref int[] inCRCErr,ref int[] inTransmitErr,ref int[] inLinkErr,ref int[] outRecvErr,ref int[] outCRCErr,ref int[] outTransmitErr,ref int[] outLinkErr);

Limpar Contadores de Erro de Porta Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Limpar contadores de erro de porta escrava
    * @param [in] slaveID Número do escravo 0~7
    * @return Código de erro
    */
    public int SlavePortErrCounterClear(int slaveID);

Exemplo de Código de Obtenção de Quadros de Erro de Porta Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    public void TestSlavePortErr()
    {
        int[] inRecvErr = new int[8];
        int[] inCRCErr = new int[8];
        int[] inTransmitErr = new int[8];
        int[] inLinkErr = new int[8];
        int[] outRecvErr = new int[8];
        int[] outCRCErr = new int[8];
        int[] outTransmitErr = new int[8];
        int[] outLinkErr = new int[8];

        robot.GetSlavePortErrCounter(ref inRecvErr, ref inCRCErr, ref inTransmitErr, ref inLinkErr,
            ref outRecvErr, ref outCRCErr, ref outTransmitErr, ref outLinkErr);

        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                Console.WriteLine($"inRecvErr {i} is {inRecvErr[i]}");
            }

            if (inCRCErr[i] != 0)
            {
                Console.WriteLine($"inCRCErr {i} is {inCRCErr[i]}");
            }

            if (inTransmitErr[i] != 0)
            {
                Console.WriteLine($"inTransmitErr {i} is {inTransmitErr[i]}");
            }

            if (inLinkErr[i] != 0)
            {
                Console.WriteLine($"inLinkErr {i} is {inLinkErr[i]}");
            }

            if (outRecvErr[i] != 0)
            {
                Console.WriteLine($"outRecvErr {i} is {outRecvErr[i]}");
            }

            if (outCRCErr[i] != 0)
            {
                Console.WriteLine($"outCRCErr {i} is {outCRCErr[i]}");
            }

            if (outTransmitErr[i] != 0)
            {
                Console.WriteLine($"outTransmitErr {i} is {outTransmitErr[i]}");
            }

            if (outLinkErr[i] != 0)
            {
                Console.WriteLine($"outLinkErr {i} is {outLinkErr[i]}");
            }
        }
        Console.WriteLine("others has no err!");

        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }

        robot.CloseRPC();
    }

Definir Coeficiente de Feedforward de Velocidade para Cada Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir coeficiente de feedforward de velocidade para cada eixo
    * @param [in] radio Coeficientes de feedforward de velocidade para cada eixo
    * @return Código de erro
    */
    public int SetVelFeedForwardRatio(double radio[6]);

Obter Coeficiente de Feedforward de Velocidade para Cada Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter coeficiente de feedforward de velocidade para cada eixo
    * @param [out] radio Coeficientes de feedforward de velocidade para cada eixo
    * @return Código de erro
    */
    public int GetVelFeedForwardRatio(ref double radio[6]);

Exemplo de código para definir o feedforward de velocidade do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestVelFeedForwardRatio()
    {

        double[] setRadio = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        robot.GetVelFeedForwardRatio(ref getRadio);
        Console.WriteLine($" {getRadio[0]:F6} {getRadio[1]:F6} {getRadio[2]:F6} {getRadio[3]:F6} {getRadio[4]:F6} {getRadio[5]:F6}");
    }

Calibração TCP com Sensor Fotoelétrico - Calcular RPY da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico - Calcular RPY da ferramenta
    * @param [in] Btool Posição cartesiana do robô
    * @param [in] Etool Valor atual do sistema de coordenadas da ferramenta
    * @param [in] senser Valor atual do sistema de coordenadas do sensor (temporariamente não disponível)
    * @param [in] radius Raio do movimento circular mm (temporariamente não disponível)
    * @param [in] dz Distância de movimento na direção negativa do eixo Z do sistema de coordenadas base; quando dz = 10000, a função retorna diretamente o RPY da ferramenta
    * @param [out] TCPRPY Valores RPY da ferramenta
    * @return Código de erro
    */
    public int TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, out Rpy TCPRPY);

Calibração TCP com Sensor Fotoelétrico - Calcular XYZ da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico - Calcular XYZ da ferramenta
    * @param [in] select 0-calcular TCP da ferramenta; 1-calcular origem do sensor; 2-calcular postura do sensor; 3-retornar diretamente o TCP da ferramenta; 4-registrar o sistema de coordenadas da peça e da ferramenta atuais
    * @param [in] originDirection 0-Direção X; 1-Direção Y; 2-Direção Z
    * @param [in] pos1 Posição cartesiana do robô 1
    * @param [in] pos2 Posição cartesiana do robô 2
    * @param [in] pos3 Posição cartesiana do robô 3
    * @param [in] pos4 Posição cartesiana do robô 4
    * @param [out] TCP Valores XYZ da ferramenta
    * @return Código de erro
    */
    public int TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2,DescTran pos3, DescTran pos4, out DescTran TCP);

Calibração TCP com Sensor Fotoelétrico - Iniciar Registro da Posição do Centro da Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico - Iniciar registro da posição do centro da flange da extremidade
    * @return Código de erro
    */
    errno_t TCPRecordFlangePosStart();

Calibração TCP com Sensor Fotoelétrico - Parar Registro da Posição do Centro da Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico - Parar registro da posição do centro da flange da extremidade
    * @return Código de erro
    */
    public int TCPRecordFlangePosEnd();

Calibração TCP com Sensor Fotoelétrico - Obter Posição do Ponto Central da Ferramenta na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico - Obter posição do ponto central da ferramenta na extremidade
    * @param [out] TCP Posição do ponto central da ferramenta (x, y, z)
    * @return Código de erro
    */
    public int TCPGetRecordFlangePos(out DescTran TCP);

Calibração TCP com Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Calibração TCP com sensor fotoelétrico
    * @param [in] luaPath Caminho do programa lua de calibração automática: "FR_CalibrateTheToolTcp.lua"
    * @param [in] offsetX Deslocamento do ponto de ensinamento (x, y, z) mm
    * @param [out] TCP Sistema de coordenadas da ferramenta calibrado (x, y, z, rx, ry, rz)
    * @return Código de erro
    */
    public int PhotoelectricSensorTCPCalibration(string luaPath, DescTran offset, out DescPose TCP);

Exemplo de Código de Calibração TCP com Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestPhotoelectricSensorTCPCalib()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        DescTran offset = new DescTran(10.0, 10.0, 3.0);
        DescPose TCP = new DescPose();
        int rtn = robot.PhotoelectricSensorTCPCalibration("FR_CalibrateTheToolTcp.lua", offset, out TCP);
        Console.WriteLine($"PhotoelectricSensorTCPCalibration: {rtn}");
        Console.WriteLine($"Coordenadas TCP da ferramenta: X={TCP.tran.x:F3}, Y={TCP.tran.y:F3}, Z={TCP.tran.z:F3}");
        Console.WriteLine($"Postura RPY da ferramenta: RX={TCP.rpy.rx:F3}, RY={TCP.rpy.ry:F3}, RZ={TCP.rpy.rz:F3}");
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
    public int SetWeaveOffsetRT(DescPose offset)