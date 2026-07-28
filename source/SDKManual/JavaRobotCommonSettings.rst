Configurações Comuns do Robô
=======================================

.. toctree::
    :maxdepth: 5

Definir Ponto de Referência da Ferramenta - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência da ferramenta - método dos seis pontos
    * @param [in] point_num Número do ponto, intervalo [1~6]
    * @return Código de erro
    */
    int SetToolPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da ferramenta
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta
    * @return Código de erro
    */
    int ComputeTool(DescPose tcp_pose);

Definir Ponto de Referência da Ferramenta - Método dos Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência da ferramenta - método dos quatro pontos
    * @param [in] point_num Número do ponto, intervalo [1~4]
    * @return Código de erro
    */
    int SetTcp4RefPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta - Método dos Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da ferramenta
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta
    * @return Código de erro
    */
    int ComputeTcp4(DescPose tcp_pose);

Calcular Sistema de Coordenadas da Ferramenta com Base em Informações de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da ferramenta com base em informações de pontos
    * @param [in] method Método de cálculo; 0-método dos quatro pontos; 1-método dos seis pontos
    * @param [in] pos Grupo de posições das juntas, comprimento do array é 4 para o método dos quatro pontos e 6 para o método dos seis pontos
    * @param [out] tool_pose Sistema de coordenadas da ferramenta de saída
    * @return Código de erro
    */
    int ComputeToolCoordWithPoints(int method, JointPos[] pos, DescPose tool_pose);

Definir Sistema de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o sistema de coordenadas da ferramenta
    * @param [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param [in] coord Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param [in] type 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
    * @param [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    * @param [in] toolID ID da ferramenta
    * @param [in] loadNum Número da carga
    * @return Código de erro
    */
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);

Definir Lista de Sistemas de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a lista de sistemas de coordenadas da ferramenta
    * @param [in] id Número do sistema de coordenadas, intervalo [0~14]
    * @param [in] coord Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param [in] type 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor
    * @param [in] install Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    * @param [in] loadNum Número da carga
    * @return Código de erro
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);

Obter Sistema de Coordenadas da Ferramenta Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da ferramenta atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] desc_pos Pose do sistema de coordenadas da ferramenta
    * @return Código de erro
    */
    int GetTCPOffset(int flag, DescPose desc_pos);

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTCPCompute(Robot robot)
    {
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint=new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);

        DescPose p2Desc=new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint=new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);

        DescPose p3Desc=new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint=new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);

        DescPose p4Desc=new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint=new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);

        DescPose p5Desc=new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint=new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);

        DescPose p6Desc=new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint=new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
        DescPose coordRtn =new DescPose() {};
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(4);
        robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(5);
        robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(6);
        rtn = robot.ComputeTool(coordRtn);
        robot.SetToolList(3, coordRtn, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(coordRtn);

        robot.SetToolCoord(4, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose(){};
        rtn = robot.GetTCPOffset(0, getCoord);
        return 0;
    }

Definir Ponto de Referência da Coordenada da Ferramenta Externa - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência da ferramenta externa - método dos três pontos
    * @param [in] point_num Número do ponto, intervalo [1~3]
    * @return Código de erro
    */
    int SetExTCPPoint(int point_num);

Calcular Sistema de Coordenadas da Ferramenta Externa - Método dos Seis Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da ferramenta externa - método dos três pontos
    * @param [out] tcp_pose Sistema de coordenadas da ferramenta externa
    * @return Código de erro
    */
    int ComputeExTCF(DescPose tcp_pose);

Definir Sistema de Coordenadas da Ferramenta Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o sistema de coordenadas da ferramenta externa
    * @param [in] id Número do sistema de coordenadas, 20-39 correspondem aos sistemas de coordenadas de ferramentas externas 0-19
    * @param [in] etcp Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param [in] etool Pendente
    * @return Código de erro
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool);

Definir Lista de Sistemas de Coordenadas da Ferramenta Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a lista de sistemas de coordenadas da ferramenta externa
    * @param [in] id Número do sistema de coordenadas, 20-39 correspondem aos sistemas de coordenadas de ferramentas externas 0-19
    * @param [in] etcp Pose do ponto central da ferramenta em relação ao centro do flange da extremidade
    * @param [in] etool Pendente
    * @return Código de erro
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool);

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta Externa do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExtCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = { p1Desc , p2Desc , p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(coordRtn);

        robot.SetExToolCoord(1, coordRtn, offdese);
        robot.SetExToolList(1, coordRtn, offdese);
        return 0;
    }

Definir Ponto de Referência do Sistema de Coordenadas da Peça - Método dos Três Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência da peça - método dos três pontos
    * @param [in] point_num Número do ponto, intervalo [1~3]
    * @return Código de erro
    */
    int SetWObjCoordPoint(int point_num);

Calcular Sistema de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da peça
    * @param [in] method Método de cálculo 0: origem-eixo x-eixo z  1: origem-eixo x-plano xy
    * @param [in] refFrame Sistema de coordenadas de referência
    * @param [out] wobj_pose Sistema de coordenadas da peça
    * @return Código de erro
    */
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose);

Definir Sistema de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o sistema de coordenadas da peça
    * @param [in] id Número do sistema de coordenadas, intervalo [1~15]
    * @param [in] coord Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade
    * @param [in] refFrame Sistema de coordenadas de referência
    * @return Código de erro
    */
    int SetWObjCoord(int id, DescPose coord, int refFrame);

Definir Lista de Sistemas de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a lista de sistemas de coordenadas da peça
    * @param [in] id Número do sistema de coordenadas, intervalo [1~15]
    * @param [in] coord Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade
    * @param [in] refFrame Sistema de coordenadas de referência
    * @return Código de erro
    */
    int SetWObjList(int id, DescPose coord, int refFrame);

Calcular Sistema de Coordenadas da Peça com Base em Informações de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas da peça com base em informações de pontos
    * @param [in] method Método de cálculo; 0: origem-eixo x-eixo z  1: origem-eixo x-plano xy
    * @param [in] pos Grupo de três posições TCP
    * @param [in] refFrame Sistema de coordenadas de referência
    * @param [in] tcp_pose Sistema de coordenadas da peça de saída
    * @return Código de erro
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, DescPose tcp_pose);

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas da peça atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] desc_pos Pose do sistema de coordenadas da peça
    * @return Código de erro
    */
    int GetWObjOffset(int flag, DescPose desc_pos);

Exemplo de Código para Operações do Sistema de Coordenadas da Peça do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWobjCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP =new DescPose[]{p1Desc , p2Desc , p3Desc };
        DescPose coordRtn =new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, coordRtn);

        robot.SetWObjCoord(1, coordRtn, 0);
        robot.SetWObjList(1, coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, getWobjDesc);
        return 0;
    }

Definir Velocidade Global
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a velocidade global
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @return Código de erro
    */
    int SetSpeed(int vel);

Definir Aceleração do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a aceleração do robô
    * @param [in] acc Percentagem de aceleração do robô
    * @return Código de erro
    */
    int SetOaccScale(double acc);

Obter Velocidade Padrão do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a velocidade padrão do robô
    * @return List[0]:int código de erro; List[1]: double vel Velocidade, em mm/s
    */
    List<Number> GetDefaultTransVel();

Definir Peso da Carga na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o peso da carga na extremidade
    * @param [in] loadNum Número da carga
    * @param [in] weight Peso da carga, em kg
    * @return Código de erro
    */
    int SetLoadWeight(int loadNum, double weight);

Definir Coordenadas do Centro de Massa da Carga na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define as coordenadas do centro de massa da carga na extremidade
    * @param [in] coord Coordenadas do centro de massa, em mm
    * @return Código de erro
    */
    int SetLoadCoord(DescTran coord);

Definir Coordenadas do Centro de Massa da Carga na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Define as coordenadas do centro de massa da carga na extremidade
     * @param [in] loadNum Número da carga
     * @param [in] coord Coordenadas do centro de massa, em mm
     * @return Código de erro
     */
    public int SetLoadCoord(int loadNum, DescTran coord)

Obter Peso da Carga Atual
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o peso da carga atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @return List[0]:int código de erro; List[1]: double weight Peso da carga, em kg
    */
    List<Number> GetTargetPayload(int flag);

Obter Centro de Massa da Carga Atual
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o centro de massa da carga atual
    * @param [in] flag 0-bloqueante, 1-não bloqueante
    * @param [out] cog Centro de massa da carga, em mm
    * @return Código de erro
    */
    int GetTargetPayloadCog(int flag, DescTran cog);

Definir Modo de Instalação do Robô
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o modo de instalação do robô
    * @param [in] install Modo de instalação, 0-montagem normal, 1-montagem lateral, 2-montagem invertida
    * @return Código de erro
    */
    int SetRobotInstallPos(int install);

Definir Ângulo de Instalação do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ângulo de instalação do robô, instalação livre
    * @param [in] yangle Ângulo de inclinação
    * @param [in] zangle Ângulo de rotação
    * @return Código de erro
    */
    int SetRobotInstallAngle(double yangle, double zangle);

Obter Ângulo de Instalação do Robô
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o ângulo de instalação do robô
    * @return List[0]:código de erro; List[1]:double yangle Ângulo de inclinação; List[2]:double zangle Ângulo de rotação
    */
    public List<Number> GetRobotInstallAngle()

Definir Valor de Variável do Sistema
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o valor da variável do sistema
    * @param [in] id Número da variável, intervalo [1~20]
    * @param [in] value Valor da variável
    * @return Código de erro
    */
    int SetSysVarValue(int id, double value);

Obter Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o valor da variável do sistema
    * @param [in] id Número da variável do sistema, intervalo [1~20]
    * @return List[0]:código de erro; List[1]:double value Valor da variável do sistema
    */
    List<Number> GetSysVarValue(int id);

Exemplo de Código para Configurações Comuns do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadInstall(Robot robot)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            robot.Sleep(30);
        }

        List<Number> defaultVel=new ArrayList<>();

        defaultVel=robot.GetDefaultTransVel();
        System.out.println("GetDefaultTransVel is:"+ defaultVel.get(1));

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5);
            robot.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            float value = 0;
            defaultVel=robot.GetSysVarValue(i);
            System.out.println("sys value :"+i+", is :"+defaultVel.get(1));
            robot.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0;
        loadCoord.y = 4.0;
        loadCoord.z = 5.0;
        robot.SetLoadCoord(loadCoord);

        robot.Sleep(1000);

        List<Number> getLoad = new ArrayList<>();

        getLoad=robot.GetTargetPayload(0);

        DescTran getLoadTran =new DescTran();
        robot.GetTargetPayloadCog(0, getLoadTran);
        System.out.println("get load is:"+getLoad.get(1)+", get load cog is: "+getLoadTran.x+","+getLoadTran.y+","+getLoadTran.z);

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0, 25.0);

        List<Number> angle=new ArrayList<>();
        angle=robot.GetRobotInstallAngle();
        System.out.println("GetRobotInstallAngle x:"+angle.get(1)+";  y:"+angle.get(2));

        robot.CloseRPC();
        return 0;
    }

Chave de Compensação de Atrito das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Chave de compensação de atrito das juntas
    * @param [in] state 0-desligar, 1-ligar
    * @return Código de erro
    */
    int FrictionCompensationOnOff(int state);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Normal
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o coeficiente de compensação de atrito das juntas - montagem normal
    * @param [in] coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return Código de erro
    */
    int SetFrictionValue_level(Object[] coeff);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Lateral
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o coeficiente de compensação de atrito das juntas - montagem lateral
    * @param [in] coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return Código de erro
    */
    int SetFrictionValue_wall(Object[] coeff);

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Invertida
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o coeficiente de compensação de atrito das juntas - montagem invertida
    * @param [in] coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return Código de erro
    */
    int SetFrictionValue_ceiling(Object[] coeff);

Definir Coeficiente de Compensação de Atrito das Juntas - Instalação Livre
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o coeficiente de compensação de atrito das juntas - instalação livre
    * @param [in] coeff Coeficientes de compensação das seis juntas, intervalo [0~1]
    * @return Código de erro
    */
    int SetFrictionValue_freedom(Object[] coeff);

Exemplo de Código para Configuração de Compensação de Atrito das Juntas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFriction(Robot robot)
    {

        Object[] lcoeff = { 0.9,0.9,0.9,0.9,0.9,0.9 };
        Object[] wcoeff = { 0.4,0.4,0.4,0.4,0.4,0.4 };
        Object[] ccoeff = { 0.6,0.6,0.6,0.6,0.6,0.6 };
        Object[] fcoeff = { 0.5,0.5,0.5,0.5,0.5,0.5 };

        int rtn = robot.FrictionCompensationOnOff(1);
        System.out.println("FrictionCompensationOnOff rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_level(lcoeff);
        System.out.println("SetFrictionValue_level rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_wall(wcoeff);
        System.out.println("SetFrictionValue_wall rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        System.out.println("SetFrictionValue_ceiling rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        System.out.println("SetFrictionValue_freedom rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

Consultar Código de Erro do Robô
++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Consulta o código de erro do robô
     * @param [out] maincode Código de erro principal
     * @param [out] subcode Código de erro secundário
     * @return Código de erro
     */
    int GetRobotErrorCode(int[] maincode, int[] subcode);

Limpar Estado de Erro
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Limpa o estado de erro
    * @return Código de erro
    */
    int ResetAllError();

Exemplo de Código para Obter Estado de Falha e Limpar Erro do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetError(Robot robot)
    {
        int[] maincode={0}, subcode={0};
        robot.GetRobotErrorCode(maincode, subcode);

        robot.ResetAllError();

        robot.Sleep(1000);

        robot.GetRobotErrorCode(maincode, subcode);
        return 0;
    }

Definir Parâmetros de Monitoramento de Temperatura e Velocidade da Ventoinha da Caixa de Controle de Larga Tensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros de monitoramento de temperatura e velocidade da ventoinha da caixa de controle de larga tensão
    * @param [in] enable 0-desativar monitoramento; 1-ativar monitoramento
    * @param [in] period Período de monitoramento (s), intervalo 1-100
    * @return Código de erro
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

Obter Parâmetros de Monitoramento de Temperatura e Velocidade da Ventoinha da Caixa de Controle de Larga Tensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros de monitoramento de temperatura e velocidade da ventoinha da caixa de controle de larga tensão
    * @return List[0]-código de erro, List[1]-enable 0-desativar monitoramento; 1-ativar monitoramento, List[2]-period Período de monitoramento (s), intervalo 1-100
    */
    List<Number> GetWideBoxTempFanMonitorParam()

Exemplo de Código para Obter Estado de Temperatura e Corrente da Ventoinha da Caixa de Controle de Larga Tensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestWideVoltageCtrlBoxtemp(Robot robot)
    {
        robot.SetWideBoxTempFanMonitorParam(1, 2);
        List<Number> list=robot.GetWideBoxTempFanMonitorParam();
        System.out.println("GetWideBoxTempFanMonitorParam enable is:"+list.get(1)+", period is:"+list.get(2));
        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+",fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);

        list=robot.GetWideBoxTempFanMonitorParam();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+" ,fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        robot.CloseRPC();
        robot.Sleep(2000);
        return 0;
    }

Definir Ponto de Calibração do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de calibração do foco
    * @param [in] pointNum Número do ponto de calibração do foco 1-8
    * @param [in] point Coordenadas do ponto de calibração
    * @return Código de erro
    */
    int SetFocusCalibPoint(int pointNum, DescPose point)

Calcular Resultado da Calibração do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o resultado da calibração do foco
    * @param [in] pointNum Número de pontos de calibração
    * @param [in] resultPos Resultado da calibração XYZ
    * @param [out] accuracy Erro de precisão da calibração
    * @return Código de erro
    */
    int ComputeFocusCalib(int pointNum, DescTran resultPos, double[] accuracy)

Iniciar Rastreamento do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
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
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type)

Parar Rastreamento do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Para o rastreamento do foco
    * @return Código de erro
    */
    int FocusEnd()

Definir Coordenadas do Foco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define as coordenadas do foco
    * @param pos Coordenadas do foco XYZ
    * @return Código de erro
    */
    public int SetFocusPosition(DescTran pos)

Exemplo de Código de Rastreamento do Foco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFocus(Robot robot){
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

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint,  p2Desc);
        robot.GetForwardKin(p3Joint,  p3Desc);
        robot.GetForwardKin(p4Joint,  p4Desc);
        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);

        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4( coordRtn);

        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint, p2Desc);
        robot.GetForwardKin(p3Joint, p3Desc);

        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);

        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double[] accuracy = {0.0};
        rtn = robot.ComputeFocusCalib(3,  resultPos,  accuracy);
        rtn = robot.SetFocusPosition(resultPos);

        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);

        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.FocusEnd();
    }

Ativar Função de Calibração de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativa a função de calibração de sensibilidade do sensor de torque das juntas
    * @param status 0-desativar; 1-ativar
    * @return Código de erro
    */
    public int JointSensitivityEnable(int status)

Coleta de Dados de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Coleta de dados de sensibilidade do sensor de torque das juntas
    * @return Código de erro
    */
    public int JointSensitivityCollect()

Obter Resultado da Calibração de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o resultado da calibração de sensibilidade do sensor de torque das juntas
    * @param calibResult Sensibilidade das juntas j1~j6 [0-1]
    * @param linearityn Linearidade das juntas j1~j6 [0-1]
    * @return Código de erro
    */
    public int JointSensitivityCalibration(double calibResult[6], double linearity[6])

Obter Erro de Histerese do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o erro de histerese do sensor de torque das juntas
    * @param hysteresisError Erro de histerese das juntas j1~j6
    * @return Código de erro
    */
    public int JointHysteresisError(double[] hysteresisError);

Obter Repetibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a repetibilidade do sensor de torque das juntas
    * @param repeatability Repetibilidade do sensor de torque das juntas j1~j6
    * @return Código de erro
    */
    public int JointRepeatability(double[] repeatability);

Definir Parâmetros do Sensor de Força das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros do sensor de força das juntas
    * @param Parâmetro obrigatório M Coeficientes de massa J1-J6[]
    * @param Parâmetro obrigatório B Coeficientes de amortecimento J1-J6[]
    * @param Parâmetro obrigatório K Coeficientes de rigidez J1-J6[]
    * @param Parâmetro padrão threshold Limiar de controle de força, Nm
    * @param Parâmetro padrão sensitivity Sensibilidade, Nm/V,[]
    * @param Parâmetro padrão setZeroFlag Flag de ativação da função; 0-desativar; 1-ativar; 2-registrar ponto zero na posição 1; 3-registrar ponto zero na posição 2
    * @return Código de erro
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

Exemplo de Código para Calibração Automática de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSensitivityCalib(Robot robot)
    {
        int rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        JointPos curJPos = new JointPos();
        robot.GetActualJointPosDegree(curJPos);
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos =new DescPose(0,0,0,0,0,0 );
        JointPos jointPos1 = new JointPos(curJPos.J1, 0, 0, -90, 0.02, curJPos.J6);
        DescPose descPos1 = new DescPose();
        robot.GetForwardKin(jointPos1, descPos1);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 1 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos2 =new JointPos( curJPos.J1, -30, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos2 =new DescPose();
        robot.GetForwardKin(jointPos2, descPos2);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 2 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos3 = new JointPos( curJPos.J1, -60, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos3 =new DescPose();
        robot.GetForwardKin(jointPos3, descPos3);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 3 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos4 = new JointPos(curJPos.J1, -90, 0, -90, 0.02, curJPos.J6);
        DescPose descPos4 = new DescPose();
        robot.GetForwardKin(jointPos4, descPos4);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 4 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos5 = new JointPos(curJPos.J1, -120, 0, -90, 0.02, curJPos.J6);
        DescPose descPos5 = new DescPose();
        robot.GetForwardKin(jointPos5, descPos5);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 5 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos6 = new JointPos(curJPos.J1, -150, 0, -90, 0.02, curJPos.J6);
        DescPose descPos6 = new DescPose();
        robot.GetForwardKin(jointPos6, descPos6);
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 6 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos7 = new JointPos(curJPos.J1, -180, 0, -90, 0.02, curJPos.J6);
        DescPose descPos7 = new DescPose();
        robot.GetForwardKin(jointPos7, descPos7);
        robot.MoveJ(jointPos7, descPos7, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 7 rtn is %d\n", rtn);
        robot.Sleep(100);
        // Curso reverso
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 8 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 9 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 10 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 11 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 12 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 13 rtn is %d\n", rtn);
        robot.Sleep(100);
        double[] calibResult =new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(calibResult, linearity);
        System.out.printf("JointSensitivityCalibration rtn is %d\n", rtn);
        rtn = robot.JointSensitivityEnable(0);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        System.out.printf("jointSensor Calib result is %f %f %f %f %f %f\njointSensor linearity is %f %f %f %f %f %f\n",
                calibResult[0], calibResult[1], calibResult[2],
                calibResult[3], calibResult[4], calibResult[5],
                linearity[0], linearity[1], linearity[2],
                linearity[3], linearity[4], linearity[5]);
        double[] hysteresisError = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointHysteresisError(hysteresisError);
        System.out.printf("JointHysteresisError result is %f %f %f %f %f %f\n",
                hysteresisError[0], hysteresisError[1], hysteresisError[2],
                hysteresisError[3], hysteresisError[4], hysteresisError[5]);
        double[] repeatability = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointRepeatability(repeatability);
        System.out.printf("JointRepeatability result is %f %f %f %f %f %f\n",
                repeatability[0], repeatability[1], repeatability[2],
                repeatability[3], repeatability[4], repeatability[5]);
        double[] M = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] B = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] K = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double[] threshold = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        System.out.printf("SetAdmittanceParams rtn is %d\n", rtn);
    }

Obter Número de Quadros com Erro nas 8 Portas Escravas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o número de quadros com erro nas 8 portas escravas do robô
    * @param inRecvErr Número de quadros com erro de receção de entrada
    * @param inCRCErr Número de quadros com erro CRC de entrada
    * @param inTransmitErr Número de quadros com erro de transmissão de entrada
    * @param inLinkErr Número de quadros com erro de ligação de entrada
    * @param outRecvErr Número de quadros com erro de receção de saída
    * @param outCRCErr Número de quadros com erro CRC de saída
    * @param outTransmitErr Número de quadros com erro de transmissão de saída
    * @param outLinkErr Número de quadros com erro de ligação de saída
    * @return Código de erro
    */
    public int GetSlavePortErrCounter(int[] inRecvErr, int[] inCRCErr, int[] inTransmitErr, int[] inLinkErr, int[] outRecvErr, int[] outCRCErr, int[] outTransmitErr, int[] outLinkErr)

Limpar Quadros com Erro nas Portas Escravas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Limpa os quadros com erro nas portas escravas
    * @param slaveID ID da escrava 0~7
    * @return Código de erro
    */
    public int SlavePortErrCounterClear(int slaveID)

Exemplo de Código para Obter Quadros com Erro nas Portas Escravas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSlavePortErr(Robot robot)
    {
        ROBOT_STATE_PKG pkg =new ROBOT_STATE_PKG();
        int[] inRecvErr =new int[8];
        int[] inCRCErr =new int[8];
        int[] inTransmitErr =new int[8];
        int[] inLinkErr =new int[8];
        int[] outRecvErr =new int[8];
        int[] outCRCErr =new int[8];
        int[] outTransmitErr =new int[8];
        int[] outLinkErr =new int[8];
        robot.GetSlavePortErrCounter(inRecvErr,  inCRCErr, inTransmitErr, inLinkErr,
                outRecvErr, outCRCErr, outTransmitErr, outLinkErr);
        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inRecvErr[i]);
            }
            if (inCRCErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inCRCErr[i]);
            }
            if (inTransmitErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inTransmitErr[i]);
            }
            if (inLinkErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inLinkErr[i]);
            }
            if (outRecvErr[i] != 0)
            {
                System.out.printf("outRecvErr %d is %d\n", i, outRecvErr[i]);
            }
            if (outCRCErr[i] != 0)
            {
                System.out.printf("outCRCErr %d is %d\n", i, outCRCErr[i]);
            }
            if (outTransmitErr[i] != 0)
            {
                System.out.printf("outTransmitErr %d is %d\n", i, outTransmitErr[i]);
            }
            if (outLinkErr[i] != 0)
            {
                System.out.printf("outLinkErr %d is %d\n", i, outLinkErr[i]);
            }
        }
        System.out.printf("others has no err!\n");
        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }
        robot.CloseRPC();
    }

Definir Coeficiente de Feedforward de Velocidade por Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o coeficiente de feedforward de velocidade por eixo
    * @param radio Coeficiente de feedforward de velocidade por eixo
    * @return Código de erro
    */
    public int SetVelFeedForwardRatio(double[] radio)

Obter Coeficiente de Feedforward de Velocidade por Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o coeficiente de feedforward de velocidade por eixo
    * @param radio Coeficiente de feedforward de velocidade por eixo
    * @return Código de erro
    */
    public int GetVelFeedForwardRatio(double[] radio)

Exemplo de Código do Coeficiente de Feedforward de Velocidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestVelFeedForwardRatio(Robot robot)
    {
        double[] setRadio =new double[] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[]{ 0.0 };
        robot.GetVelFeedForwardRatio(getRadio);
        System.out.printf(" %f %f %f %f %f %f\n", getRadio[0], getRadio[1], getRadio[2], getRadio[3], getRadio[4], getRadio[5]);
        robot.CloseRPC();
    }

Calibração TCP do Sensor Fotoelétrico - Calcular RPY da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - calcular RPY da ferramenta
    * @param Btool Posição cartesiana do robô
    * @param Etool Valor atual do sistema de coordenadas da ferramenta
    * @param sensor Valor atual do sistema de coordenadas do sensor (não disponível no momento)
    * @param radius Raio do movimento circular mm (não disponível no momento)
    * @param dz Distância de movimento na direção negativa do eixo z do sistema de coordenadas base; quando dz = 10000, a função retorna diretamente o RPY da ferramenta
    * @param TCPRPY Valor RPY da ferramenta
    * @return Código de erro
    */
    public int TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, Rpy TCPRPY)

Calibração TCP do Sensor Fotoelétrico - Calcular XYZ da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - calcular XYZ da ferramenta
    * @param select 0-calcular TCP da ferramenta; 1-calcular origem do sensor; 2-calcular postura do sensor; 3-retornar diretamente o TCP da ferramenta; 4-registrar o sistema de coordenadas atual da peça e da ferramenta
    * @param originDirection 0-Direção X; 1-Direção Y; 2-Direção Z
    * @param pos1 Posição cartesiana do robô 1
    * @param pos2 Posição cartesiana do robô 2
    * @param pos3 Posição cartesiana do robô 3
    * @param pos4 Posição cartesiana do robô 4
    * @param TCP Valor XYZ da ferramenta
    * @return Código de erro
    */
    public int TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2, DescTran pos3, DescTran pos4, DescTran TCP)

Calibração TCP do Sensor Fotoelétrico - Iniciar Gravação da Posição do Centro do Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - iniciar gravação da posição do centro do flange da extremidade
    * @return Código de erro
    */
    public int TCPRecordFlangePosStart()

Calibração TCP do Sensor Fotoelétrico - Parar Gravação da Posição do Centro do Flange da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - parar gravação da posição do centro do flange da extremidade
    * @return Código de erro
    */
    public int TCPRecordFlangePosEnd()

Calibração TCP do Sensor Fotoelétrico - Obter Posição do Centro da Ponta da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico - obter posição do centro da ponta da ferramenta
    * @param TCP Posição do centro da ponta da ferramenta (x, y, z)
    * @return Código de erro
    */
    public int TCPGetRecordFlangePos(DescTran TCP)

Calibração TCP do Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calibração TCP do sensor fotoelétrico
    * @param luaPath Caminho do programa lua para calibração automática: "FR_CalibrateTheToolTcp.lua"
    * @param offset Deslocamento do ponto de ensino (x, y, z) mm
    * @param TCP Sistema de coordenadas da ferramenta calibrado (x, y, z, rx, ry, rz)
    * @return Código de erro
    */
    public int PhotoelectricSensorTCPCalibration(String luaPath, DescTran offset, DescPose TCP)

Exemplo de Código para Calibração TCP do Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestPhotoelectricSensorTCPCalib(Robot robot)
    {
        DescTran offset = new DescTran(10.0, 10.0, 3.0 );
        DescPose TCP = new DescPose();
        int rtn = robot.PhotoelectricSensorTCPCalibration("FR_CalibrateTheToolTcp.lua", offset, TCP);
        System.out.printf("PhotoelectricSensorTCPCalibration rtn is %d %f %f %f %f %f %f \n", rtn, TCP.tran.x, TCP.tran.y, TCP.tran.z, TCP.rpy.rx, TCP.rpy.ry, TCP.rpy.rz);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }