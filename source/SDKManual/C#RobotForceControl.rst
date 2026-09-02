Controle de Força do Robô
====================================

.. toctree:: 
    :maxdepth: 5

Configuração do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Configura o sensor de força
    * @param  [in] company  Fabricante do sensor de força, 17-Kunwei Technology
    * @param  [in] device  Número do dispositivo, não usado no momento, padrão 0
    * @param  [in] softvesion  Número da versão do software, não usado no momento, padrão 0
    * @param  [in] bus  Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0
    * @return  Código de erro
    */
    int FT_SetConfig(int company, int device, int softvesion, int bus); 

Obter Configuração do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém a configuração do sensor de força
    * @param [out] deviceID Número do sensor de força
    * @param [out] company Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa Aeroespacial 11, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin
    * @param [out] device  Número do dispositivo, Kunwei(0-KWR75B), Instituto Aeroespacial 11(0-MCS6A-200-4), ATI (0-AXIA80 -M8), Zhongke Midian(0-MST2010), Weihang Minxin(0-WHC6L-YB-10A) 
    * @param [out] softvesion Número da versão do software, não usado no momento, padrão 0
    * @return Código de erro
    */ 
    int FT_GetConfig(ref int deviceID, ref int company, ref int device, ref int softvesion); 

Ativação do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Ativa o sensor de força
    * @param  [in] act  0-reset, 1-ativar
    * @return  Código de erro
    */
    int FT_Activate(byte act); 

Zeragem do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Zera o sensor de força
    * @param  [in] act  0-remover zero, 1-correção de zero
    * @return  Código de erro
    */
    int FT_SetZero(byte act); 

Definir Sistema de Coordenadas de Referência do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o sistema de coordenadas de referência do sensor de força
    * @param  [in] ref  0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @return  Código de erro
    */
    int FT_SetRCS(byte type); 

Definir Peso da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o peso da carga sob o sensor de força
    * @param  [in] weight Peso da carga kg
    * @return  Código de erro
    */
    int SetForceSensorPayLoad(double weight);

Definir Centro de Gravidade da Carga Sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o centro de gravidade da carga sob o sensor de força
    * @param  [in] x Centro de gravidade da carga x mm 
    * @param  [in] y Centro de gravidade da carga y mm
    * @param  [in] z Centro de gravidade da carga z mm
    * @return  Código de erro
    */
    int SetForceSensorPayLoadCog(double x, double y, double z);

Obter Peso da Carga Sob o Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o peso da carga sob o sensor de força
    * @param  [in] weight Peso da carga kg
    * @return  Código de erro
    */
    int GetForceSensorPayLoad(ref double weight);

Obter Centro de Gravidade da Carga Sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o centro de gravidade da carga sob o sensor de força
    * @param  [out] x Centro de gravidade da carga x mm 
    * @param  [out] y Centro de gravidade da carga y mm
    * @param  [out] z Centro de gravidade da carga z mm
    * @return  Código de erro
    */
    int GetForceSensorPayLoadCog(ref double x, ref double y, ref double z);

Autozero do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Autozero do sensor de força
    * @param  [out] weight Massa do sensor kg 
    * @param  [out] pos Centro de gravidade do sensor mm
    * @return  Código de erro
    */
    int ForceSensorAutoComputeLoad(ref double weight, ref DescTran pos);

Obter Dados de Força/Torque no Sistema de Coordenadas de Referência
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém dados de força/torque no sistema de coordenadas de referência
    * @param  [out] ft  Força/torque, fx, fy, fz, tx, ty, tz
    * @return  Código de erro
    */   
    int FT_GetForceTorqueRCS(byte flag, ref ForceTorque ft); 

Obter Dados Brutos de Força/Torque do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém dados brutos de força/torque do sensor de força
    * @param  [out] ft  Força/torque, fx, fy, fz, tx, ty, tz
    * @return  Código de erro
    */   
    int FT_GetForceTorqueOrigin(byte flag, ref ForceTorque ft); 

Exemplo de Código para Configuração e Autozero do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button54_Click(object sender, EventArgs e)
    {
        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin:{ft.fx},{ft.fy},{ft.fz},{ft.tx},{ft.ty},{ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose ftCoord = new DescPose(0, 0, 0, 0, 0, 0);
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayLoad(0.824);
        robot.SetForceSensorPayLoadCog(0.778, 2.554, 48.765);
        double weight = 0;
        double x = 0, y = 0, z = 0;
        robot.GetForceSensorPayLoad(ref weight);
        robot.GetForceSensorPayLoadCog(ref x, ref y, ref z);
        Console.WriteLine($"the FT load is {weight}, {x} {y} {z}");

        robot.SetForceSensorPayLoad(0);
        robot.SetForceSensorPayLoadCog(0, 0, 0);

        double computeWeight = 0;
        DescTran tran = new DescTran(0, 0, 0);
        robot.ForceSensorAutoComputeLoad(ref weight, ref tran);
        Console.WriteLine($"the result is weight {weight} pos is {tran.x} {tran.y} {tran.z}");

    } 

Registro da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Registro da identificação do peso da carga
    * @param  [in] id  Número do sistema de coordenadas do sensor, faixa [1~14]
    * @return  Código de erro
    */
    int FT_PdIdenRecord(int id);

Cálculo da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Cálculo da identificação do peso da carga
    * @param  [out] weight  Peso da carga, unidade kg
    * @return  Código de erro
    */   
    int FT_PdIdenCompute(ref double weight);

Registro da Identificação do Centro de Gravidade da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Registro da identificação do centro de gravidade da carga
    * @param  [in] id  Número do sistema de coordenadas do sensor, faixa [1~14]
    * @param  [in] index Número do ponto, faixa [1~3]
    * @return  Código de erro
    */
    int FT_PdCogIdenRecord(int id, int index); 

Cálculo da Identificação do Centro de Gravidade da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Cálculo da identificação do centro de gravidade da carga
    * @param  [out] cog  Centro de gravidade da carga, unidade mm
    * @return  Código de erro
    */   
    int FT_PdCogIdenCompute(ref DescTran cog);

Exemplo de Código para Identificação da Carga do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTPdCog_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin: {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose tcoord = new DescPose(0, 0, 35.0, 0, 0, 0);
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        Thread.Sleep(1000);

        double weight = 0.0f;
        robot.FT_PdIdenCompute(ref weight);
        Console.WriteLine($"payload weight: {weight}");

        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);

        DescTran cog = new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(ref cog);
        Console.WriteLine($"cog: {cog.x}, {cog.y}, {cog.z}");
    }

Proteção Contra Colisão
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int FT_Guard(int flag, int sensor_id, int[] select, ForceTorque ft, double[] max_threshold, double[] min_threshold); 

Exemplo de Código para Proteção Contra Colisão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTGuard_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte sensor_id = 1;
        int[] select = { 1, 1, 1, 1, 1, 1 };
        double[] max_threshold = { 10.0f, 10.0f, 10.0f, 10.0f, 10.0f, 10.0f };
        double[] min_threshold = { 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f };

        ForceTorque ft = new ForceTorque();
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.FT_Guard(1, sensor_id, select,  ft, max_threshold, min_threshold);
        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);

        robot.FT_Guard(0, sensor_id, select, ft, max_threshold, min_threshold);
    }

Controle de Força Constante
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Controle de força constante
    * @param  [in] flag 0-desativar controle de força constante, 1-ativar controle de força constante
    * @param  [in] sensor_id Número do sensor de força
    * @param  [in] select  Seleciona se os seis graus de liberdade são detectados para colisão, 0-não detectar, 1-detectar
    * @param  [in] ft  Força/torque de colisão, fx, fy, fz, tx, ty, tz
    * @param  [in] ft_pid Parâmetros PID de força, parâmetros PID de torque
    * @param  [in] adj_sign Controle de ativação/desativação adaptativa, 0-desativar, 1-ativar
    * @param  [in] ILC_sign Controle de ativação/desativação ILC, 0-parar, 1-treinar, 2-operação real
    * @param  [in] max_dis Distância máxima de ajuste, unidade mm
    * @param  [in] max_ang Ângulo máximo de ajuste, unidade graus
    * @param  [in] M Parâmetros de massa rx, ry [0.1-10], padrão 2
    * @param  [in] B Parâmetros de amortecimento rx, ry [0.1-50], padrão 8
    * @param  [in] threshold Limite de ativação rx, ry [0-10], padrão 0.2
    * @param  [in] adjustCoeff Coeficiente de ajuste de torque rx, ry [0-1], padrão 1
    * @param  [in] polishRadio Raio de lixamento, unidade mm
    * @param  [in] filter_Sign Flag de ativação do filtro 0-desativar; 1-ativar, padrão desativado
    * @param  [in] posAdapt_sign Flag de ativação da conformidade de postura 0-desativar; 1-ativar, padrão desativado
    * @param  [in] isNoBlock Flag de bloqueio, 0-bloqueado; 1-não bloqueado
    * @return  Código de erro
    */
    public int FT_Control(byte flag, int sensor_id, byte[] select, ForceTorque ft, float[] ft_pid,byte adj_sign, byte ILC_sign, float max_dis, float max_ang,double[] M, double[] B, double[] threshold, double[] adjustCoeff,double polishRadio, int filter_Sign, int posAdapt_sign, int isNoBlock)

Exemplo de Código para Controle de Força Constante com Amortecimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public void TestFTControlWithAdjustCoeff()
    {
        int rtn;
        int sensor_id = 10;
        byte[] select = new byte[6] { 0, 0, 1, 0, 0, 0 };
        float[] ft_pid = new float[6] { 0.0008f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 1000.0f;
        float max_ang = 20.0f;
        ForceTorque ft = new ForceTorque();
        ft.fz = -10.0f;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        JointPos j1 = new JointPos(80.765f, -98.795f, 106.548f, -97.734f, -89.999f, 94.842f);
        JointPos j2 = new JointPos(43.067f, -84.429f, 92.620f, -98.175f, -90.011f, 57.144f);
        DescPose desc_p1 = new DescPose(5.009f, -547.463f, 262.053f, -179.999f, -0.019f, 75.923f);
        DescPose desc_p2 = new DescPose(-347.966f, -547.463f, 262.048f, -180.000f, -0.019f, 75.923f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        double[] M = new double[2] { 2.0, 2.0 };
        double[] B = new double[2] { 15.0, 15.0 };
        double[] threshold = new double[2] { 1.0, 1.0 };
        double[] adjustCoeff = new double[2] { 1.0, 0.8 };
        double polishRadio = 0.0;
        int filter_Sign = 0;
        int posAdapt_sign = 1;
        int isNoBlock = 0;
        while (true)
        {
            rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            Console.WriteLine($"FT_Control start rtn is {rtn}");
            robot.MoveL(j1, desc_p1, 1, 0, 100, 100, 100, -1, 0, epos, 0, 0, offset_pos, 0, 0, 10);
            robot.MoveL(j2, desc_p2, 1, 0, 100, 100, 100, -1, 0, epos, 0, 0, offset_pos, 0, 0, 10);
            rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            Console.WriteLine($"FT_Control end rtn is {rtn}");
        }
    }

Inserção Rotativa
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Inserção rotativa
    * @param [in] rcs Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    * @param [in] angVelRot Velocidade angular de rotação, unidade deg/s
    * @param [in] ft Limite de força/torque, fx, fy, fz, tx, ty, tz, faixa [0~100]
    * @param [in] max_angle Ângulo máximo de rotação, unidade deg
    * @param [in] orn Direção da força/torque, 1-ao longo do eixo z, 2-em torno do eixo z
    * @param [in] max_angAcc Aceleração angular máxima de rotação, unidade deg/s^2, não usado no momento, padrão 0
    * @param [in] rotorn Direção de rotação, 1-sentido horário, 2-sentido anti-horário
    * @param [in] strategy Estratégia de tratamento quando nenhuma força/torque é detectada, 0-erro; 1-aviso, continuar movimento
    * @return Código de erro
    */
    public int FT_RotInsertion(int rcs, double angVelRot, double ft, double max_angle, int orn, double max_angAcc, int rotorn, int strategy)

Busca em Espiral
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Busca em espiral
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema da ferramenta, 1-sistema base
    * @param  [in] dr Avanço do raio por volta
    * @param  [in] ft Limiar de força/torque, fx,fy,fz,tx,ty,tz, intervalo [0~100]
    * @param  [in] max_t_ms Tempo máximo de busca, unidade ms
    * @param  [in] max_vel Velocidade linear máxima, unidade mm/s
    * @param  [in] strategy Estratégia de tratamento quando nenhuma força/torque é detectado, 0-erro; 1-aviso, continuar movimento
    * @return  Código de erro
    */
    public int FT_SpiralSearch(int rcs, float dr, float ft, float max_t_ms, float max_vel, int strategy = 0)

Inserção Linear
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Inserção linear
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema da ferramenta, 1-sistema base
    * @param  [in] ft  Limiar de força/torque, fx,fy,fz,tx,ty,tz, intervalo [0~100]
    * @param  [in] lin_v Velocidade linear, unidade mm/s
    * @param  [in] lin_a Aceleração linear, unidade mm/s^2, não utilizada temporariamente
    * @param  [in] max_dis Distância máxima de inserção, unidade mm
    * @param  [in] linorn  Direção de inserção, 0-direção negativa, 1-direção positiva
    * @param  [in] strategy Estratégia de tratamento quando nenhuma força/torque é detectado, 0-erro; 1-aviso, continuar movimento
    * @return  Código de erro
    */
    public int FT_LinInsertion(int rcs, float ft, float lin_v, float lin_a, float max_dis, byte linorn, int strategy=0)

Exemplo de Código de Inserção Rotacional com Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public void TestRotInsert()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        int rtn;

        float forceInsertion = 5.0f; // Limiar de força ou torque (0~100), unidade N ou Nm
        int angleMax = 300; // Ângulo máximo de rotação, unidade °
        byte orn = 1; // Direção da força, 1-fz, 2-mz
        float angAccmax = 0; // Aceleração angular máxima, unidade °/s^2, não utilizada temporariamente
        byte status = 1;  // Sinalizador de controle de força constante, 0-desligado, 1-ligado
        int sensor_num = 11; // Número do sensor de força
        float[] gain = { 0.0001f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };  // Limiar máximo
        byte adj_sign = 0;  // Status de início/parada adaptativo, 0-desligado, 1-ligado
        byte ILC_sign = 0;  // Status de início/parada do controle ILC, 0-parado, 1-treinamento, 2-operacional
        float max_dis = 1000.0f;  // Distância máxima de ajuste
        float max_ang = 20.0f;  // Ângulo máximo de ajuste
        ForceTorque ft = new ForceTorque();
        int rcs = 0;  // Sistema de coordenadas de referência, 0-sistema da ferramenta, 1-sistema base
        float angVelRot = 1.0f;  // Velocidade angular rotacional, unidade °/s
        byte rotorn = 1; // Direção de rotação, 1-horário, 2-anti-horário
        JointPos j1 = new JointPos(100.968, -108.678, 126.166, -106.630, -93.253, 19.584);
        DescPose desc_p1 = new DescPose(159.473, -316.570, 334.560, -179.718, -3.352, 171.400);
        ExaxisPos epos = new ExaxisPos(0.0f, 0.0f, 0.0f, 0.0f);
        DescPose offset_pos = new DescPose(0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f);

        robot.MoveL(j1, desc_p1, 2, 0, 100.0f, 180.0f, 100.0f, -1.0f, 0, epos, (byte)0, (byte)1, offset_pos);

        byte[] select3 = { 0, 0, 1, 0, 0, 0 };
        ft.fz = -5.0f;
        gain[0] = 0.0001f;
        status = 1;
        robot.FT_Control(status, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        rtn = robot.FT_LinInsertion(rcs, 10, 1, 1, 100, 1);
        Console.WriteLine("FT_LinInsertion rtn is " + rtn);
        robot.FT_Control(0, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);

        ft.fz = -30.0f;
        robot.FT_Control(1, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn, 0);
        Console.WriteLine("FT_RotInsertion rtn is " + rtn);
        robot.FT_Control(0, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);

        rtn = robot.FT_LinInsertion(0, 40, 3, 0, 100, 1);
        Console.WriteLine("FT_LinInsertion retract rtn is " + rtn);

        Thread.Sleep(1000);
        robot.GetRobotRealTimeState(ref pkg);
        Console.WriteLine("robot errcode " + pkg.main_code + "  " + pkg.sub_code);
    }
    
Exemplo de Código para Inserção Rotativa com Sensor de Força do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public void TestMove()
    {
        int rtn;
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos j2 = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos j3 = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);
        JointPos j4 = new JointPos(-31.154f, -95.317f, 94.276f, -88.079f, -89.740f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose desc_pos2 = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose desc_pos3 = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);
        DescPose desc_pos4 = new DescPose(-443.165f, 147.881f, 480.951f, 179.511f, -0.775f, -15.409f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float oacc = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos,j1, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        Console.WriteLine($"MoveCart errcode:{rtn}");
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,desc_pos4, tool, user, vel, acc, epos, flag, offset_pos,ovl, blendR, -1, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
    }

Ativação do Controle de Complacência
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Ativa o controle de complacência
    * @param  [in] p Coeficiente de ajuste de posição ou coeficiente de complacência
    * @param  [in] force Limite de força para ativação da complacência, unidade N
    * @return  Código de erro
    */   
    int FT_ComplianceStart(float p, float force);

Desativação do Controle de Complacência
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Desativa o controle de complacência
    * @return  Código de erro
    */   
    int FT_ComplianceStop(); 

Exemplo de Código para Controle de Complacência
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnComplience_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte flag = 1;
        int sensor_id = 1;
        int[] select = { 1, 1, 1, 0, 0, 0 };
        double[] ft_pid = { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0, ILC_sign = 0;
        float max_dis = 100.0f, max_ang = 0.0f;

        ForceTorque ft = new ForceTorque { fx = -10.0, fy = -10.0, fz = -10.0 };
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        float p = 0.00005f;
        float force = 30.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        Console.WriteLine($"FT_ComplianceStart rtn is {rtn}");

        int count = 5;
        while (count-- > 0)
        {
        robot.MoveL(j1, desc_p1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 1, offset_pos);
        robot.MoveL(j2, desc_p2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 0, offset_pos);
        }

        robot.FT_ComplianceStop();
        Console.WriteLine($"FT_ComplianceStop rtn is {rtn}");

        flag = 0;
        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
    }

Inicialização da Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Inicialização da identificação da carga
    * @return Código de erro
    */
    int LoadIdentifyDynFilterInit();

Inicialização das Variáveis de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Inicialização das variáveis de identificação da carga
    * @return Código de erro
    */
    int LoadIdentifyDynVarInit();

Programa Principal de Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Programa principal de identificação da carga
    * @param [in] joint_torque Torque das juntas
    * @param [in] joint_pos Posição das juntas
    * @param [in] t Período de amostragem
    * @return Código de erro
    */
    int LoadIdentifyMain(double[] joint_torque, double[] joint_pos, double t);

Obter Resultado da Identificação da Carga
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o resultado da identificação da carga
    * @param [in] gain  Coeficiente do termo gravitacional double[6], coeficiente do termo centrífugo double[6]
    * @param [out] weight Peso da carga
    * @param [out] cog Centro de gravidade da carga
    * @return Código de erro
    */
    int LoadIdentifyGetResult(double[] gain, ref double weight, ref DescTran cog);

Exemplo de Código para Identificação da Carga do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button74_Click(object sender, EventArgs e)
    {
        int rtn;
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();
        Console.WriteLine("LoadIdentifyDynFilterInit retval is: " + retval);

        retval = robot.LoadIdentifyDynVarInit();
        Console.WriteLine("LoadIdentifyDynVarInit retval is: " + retval);

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0, 0, 0, 0, 0, 0);
        double[] joint_toq = new double[6] { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        robot.GetActualJointPosDegree(0, ref posJ);
        posJ.jPos[1] = posJ.jPos[1] + 10;
        robot.GetJointTorques(0, joint_toq);
        joint_toq[1] = joint_toq[1] + 2;

        double[] tmpTorque = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        for (int i = 0; i < 6; i++)
        {
            tmpTorque[i] = joint_toq[i];
        }

        retval = robot.LoadIdentifyMain(tmpTorque, posJ.jPos, 1);
        Console.WriteLine("LoadIdentifyMain retval is: " + retval);

        double[] gain = new double[12] { 0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0 };
        double weight = 0;
        DescTran load_pos = new DescTran(0, 0, 0);
        retval = robot.LoadIdentifyGetResult(gain, ref weight, ref load_pos);
        Console.WriteLine("LoadIdentifyGetResult retval is: {0}; weight is {1} cog is {2} {3} {4}", retval, weight, load_pos.x, load_pos.y, load_pos.z);
    }

Arrastagem Assistida por Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
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
    * @param  [in] Fmax Limite máximo de força de arrastagem Nm
    * @param  [in] Vmax Limite máximo de velocidade das juntas °/s
    * @return  Código de erro
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag,int forceCollisionFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);
    
Obter Estado da Chave de Arrastagem do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o estado da chave de arrastagem do sensor de força
    * @param  [out] dragState Estado de controle da arrastagem assistida por sensor de força, 0-desativar; 1-ativar
    * @param  [out] sixDimensionalDragState Estado de controle da arrastagem assistida por força de 6 eixos, 0-desativar; 1-ativar
    * @return  Código de erro
    */
    int GetForceAndTorqueDragState(ref int dragState, ref int sixDimensionalDragState);

Ativação Automática do Sensor de Força Após Limpeza de Erro
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Ativação automática do sensor de força após limpeza de erro
    * @param  [in] status Estado de controle, 0-desativar; 1-ativar
    * @return  Código de erro
    */
    int SetForceSensorDragAutoFlag(int status);

Exemplo de Código para Arrastagem Assistida por Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button61_Click(object sender, EventArgs e)
    {
        robot.SetForceSensorDragAutoFlag(1);
        double[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        double[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        double[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };

        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);
        robot.WaitMs(5000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        robot.GetForceAndTorqueDragState(ref dragState, ref sixDimensionalDragState);
        Console.WriteLine($"the drag state is {dragState} {sixDimensionalDragState}");

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
    }

Definir Chave e Parâmetros para Arrastagem Híbrida com Força de 6 Eixos e Impedância de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  Define a chave e parâmetros para arrastagem híbrida com força de 6 eixos e impedância de junta
    * @param  [in] status Estado de controle, 0-desativar; 1-ativar
    * @param  [in] impedanceFlag Flag de ativação da impedância, 0-desativar; 1-ativar
    * @param  [in] lamdeDain Ganho de arrastagem
    * @param  [in] KGain Ganho de rigidez
    * @param  [in] BGain Ganho de amortecimento
    * @param  [in] dragMaxTcpVel Limite máximo de velocidade linear da extremidade durante arrastagem
    * @param  [in] dragMaxTcpOriVel Limite máximo de velocidade angular da extremidade durante arrastagem
    * @return  Código de erro
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, double[] lamdeDain, double[] KGain, double[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

Exemplo de Código para Arrastagem Assistida por Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button62_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        double[] lambdaGain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        double[] kGain = { 0, 0, 0, 0, 0, 0 };
        double[] bGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
        Thread.Sleep(5000); 
        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
    }

Controle de Ativação/Desativação da Impedância
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
    public int ImpedanceControlStartStop(int status, int workSpace, double[] forceThreshold, double[] m, double[] b, double[] k, double maxV, double maxVA, double maxW, double maxWA)

Exemplo de Código para Controle de Ativação/Desativação da Impedância do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestImpedanceControl()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        int rtn;
        JointPos j1 = new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2 = new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1 = new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2 = new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
    
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
    
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 200.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendR = -1.0f;
    
        byte flag = 0;
    
        byte search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);
    
        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);
        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);
        robot.FT_SetZero(1);
        Thread.Sleep(1000);
    
        double[] forceThreshold = new double[] { 30, 30, 30, 5, 5, 5 };
        double[] m = new double[] { 0.1, 0.1, 0.1, 0.02, 0.02, 0.02 };
        double[] b = new double[] { 1, 1, 1, 0.08, 0.08, 0.08 };
        double[] k = new double[] { 0, 0, 0, 0, 0, 0 };
        rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        Console.WriteLine($"ImpedanceControlStartStop errcode:{rtn}");
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        Console.WriteLine($"movel errcode:{rtn}");
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
    }

Ativação da Função de Compensação de Torque e Coeficiente de Compensação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação da função de compensação de torque e coeficiente de compensação
    * @param [in] status Interruptor, 0-desativar; 1-ativar
    * @param [in] torqueCoeff Coeficiente de compensação de torque J1-J6 [0-1]
    * @return Código de erro
    */
    public int SetCoderCompenParams(int status, double[] torqueCoeff)

Posicionamento de Superfície
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Posicionamento de superfície
    * @param  [in] rcs Sistema de coordenadas de referência, 0-sistema da ferramenta, 1-sistema base
    * @param  [in] dir  Direção de movimento, 1-direção positiva, 2-direção negativa
    * @param  [in] axis Eixo de movimento, 1-eixo x, 2-eixo y, 3-eixo z
    * @param  [in] lin_v Velocidade linear de busca, unidade mm/s
    * @param  [in] lin_a Aceleração linear de busca, unidade mm/s^2, não utilizada temporariamente, padrão 0
    * @param  [in] max_dis Distância máxima de busca, unidade mm
    * @param  [in] ft  Limiar de força/torque de término de movimento, fx,fy,fz,tx,ty,tz
    * @param  [in] strategy Estratégia de tratamento quando nenhuma força/torque é detectado, 0-erro; 1-aviso, continuar movimento
    * @return  Código de erro
    */
    public int FT_FindSurface(int rcs, byte dir, byte axis, float lin_v, float lin_a, float max_dis, float ft, int stragety = 0)

Início do Cálculo da Posição do Plano Médio
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início do cálculo da posição do plano médio
    * @return  Código de erro
    */
    public int FT_CalCenterStart()

Fim do Cálculo da Posição do Plano Médio
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim do cálculo da posição do plano médio
    * @param  [out] pos Posição do plano médio
    * @return  Código de erro
    */
    public int FT_CalCenterEnd(ref DescPose pos)

Exemplo de Código de Posicionamento de Superfície
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    private void button59_Click(object sender, EventArgs e)
    {
        int company = 22;
        int device = 0;
        int softversion = 0;
        int bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine("FT config:" + company + "," + device + "," + softversion + "," + bus);
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        int rcs = 0;
        byte dir = 1;
        byte axis = 1;
        float lin_v = 15.0f;
        float lin_a = 0.0f;
        float maxdis = 500.0f;
        float ft_goal = 2.0f;
        DescPose desc_pos = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose xcenter = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose ycenter = new DescPose(0, 0, 0, 0, 0, 0);

        ForceTorque ft = new ForceTorque();

        ft.fx = -2.0f;

        robot.MoveCart(desc_pos, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);

        robot.FT_CalCenterStart();
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.MoveCart(desc_pos, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.WaitMs(1000);

        dir = 2;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.FT_CalCenterEnd(ref xcenter);
        Console.WriteLine("xcenter:" + xcenter.tran.x + "," + xcenter.tran.y + "," + xcenter.tran.z + "," + xcenter.rpy.rx + "," + xcenter.rpy.ry + "," + xcenter.rpy.rz);
        robot.MoveCart(xcenter, 1, 0, 60.0f, 50.0f, 50.0f, -1.0f, -1);

        robot.FT_CalCenterStart();
        dir = 1;
        axis = 2;
        lin_v = 6.0f;
        maxdis = 150.0f;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.MoveCart(desc_pos, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.WaitMs(1000);

        dir = 2;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.FT_CalCenterEnd(ref ycenter);
        Console.WriteLine("ycenter:" + ycenter.tran.x + "," + ycenter.tran.y + "," + ycenter.tran.z + "," + ycenter.rpy.rx + "," + ycenter.rpy.ry + "," + ycenter.rpy.rz);
        robot.MoveCart(ycenter, 1, 0, 60.0f, 50.0f, 50.0f, 0.0f, -1);

    }

Definir Deslocamento em Tempo Real da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir deslocamento em tempo real da oscilação
    * @param [in] offset Deslocamento em tempo real [mm, °]
    * @return  Código de erro
    */
    public int SetWeaveOffsetRT(DescPose offset)

Exemplo de Código de Velocidade e Deslocamento em Tempo Real da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:   

    public void TestWeaveSpeedAndOffset()
    {
        Console.WriteLine("============================================================");
        Console.WriteLine("  Weave Speed and Offset Test");
        Console.WriteLine("============================================================");

        if (robot == null)
        {
            Console.WriteLine("ERROR: Robot not connected!");
            return;
        }

        int rtn;
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos j1 = new JointPos(5.027, -84.331, -75.139, -103.690, 86.379, 20.794);
        DescPose d1 = new DescPose(324.752, -83.339, 366.314, -172.321, -0.936, -106.047);

        JointPos j2 = new JointPos(-35.335, -117.598, -57.174, -95.234, 90.001, -19.560);
        DescPose d2 = new DescPose(324.999, -355.439, 260.000, 179.995, 0.003, -105.775);

        JointPos j3 = new JointPos(59.787, -117.594, -57.183, -95.222, 90.006, 75.562);
        DescPose d3 = new DescPose(324.998, 355.441, 260.002, 179.995, 0.003, -105.775);

        // ---- Step 1: MoveJ to start point ----
        Console.WriteLine("\nStep 1: MoveJ to start point");
        rtn = robot.MoveJ(j1, d1, 1, 0, 100, 100, 50, epos, -1, 0, offset_pos);
        Console.WriteLine("  MoveJ(j1) rtn={0}", rtn);
        Thread.Sleep(500);

        // ---- Step 2: MoveJ to weave entry ----
        Console.WriteLine("\nStep 2: MoveJ to weave entry point");
        rtn = robot.MoveJ(j2, d2, 1, 0, 100, 100, 50, epos, -1, 0, offset_pos);
        Console.WriteLine("  MoveJ(j2) rtn={0}", rtn);
        Thread.Sleep(500);

        // ---- Step 3: WeaveStart, launch weave MoveL thread ----
        Console.WriteLine("\nStep 3: WeaveStart + MoveL in background thread");
        robot.WeaveStart(0);

        bool weaveRunning = true;
        Thread weaveThread = new Thread(() =>
        {
            rtn = robot.MoveL(j3, d3, 1, 0, 100, 100, 5, -1, 0, epos, 0, 0, offset_pos, 5, 0, 0, 10);
            Console.WriteLine("  MoveL(weave) thread finished, rtn={0}", rtn);
            weaveRunning = false;
        });
        weaveThread.IsBackground = true;
        weaveThread.Start();
        Thread.Sleep(500);  // Wait for motion to start

        // ---- Step 4: Speed test (main thread, weave MoveL in background) ----
        Console.WriteLine("\nStep 4: SetSpeed test during weaving");
        int[] speedValues = { 20, 50, 80, 30, 60, 10 };
        foreach (int speed in speedValues)
        {
            if (!weaveRunning) break;
            rtn = robot.SetSpeedInstant(speed);
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("  SetSpeed({0}) -> rtn={1}, TCP_CmpSpeed={2}", speed, rtn, pkg.target_TCP_CmpSpeed);
            Thread.Sleep(5000);
        }


        Thread.Sleep(5000);
        // ---- Step 5: SetWeaveOffsetRT offset test (main thread, weave MoveL in background) ----
        Console.WriteLine("\nStep 5: SetWeaveOffsetRT test (50 iterations, delta=0.1)");
        double accumOffset = 0.0;
        for (int i = 0; i < 50 && weaveRunning; i++)
        {
            accumOffset += 0.1;
            DescPose weaveOffset = new DescPose(0, 0, accumOffset, 0, 0, 0);
            rtn = robot.SetWeaveOffsetRT(weaveOffset);
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("  [{0}/50] SetWeaveOffsetRT(x={1:F1}) -> rtn={2}, TCP_pos=({3:F2},{4:F2},{5:F2})",
                i + 1, accumOffset, rtn,
                pkg.tl_cur_pos[0], pkg.tl_cur_pos[1], pkg.tl_cur_pos[2]);
            Thread.Sleep(100);
        }

        // ---- Step 6: Wait for weave MoveL, then WeaveEnd ----
        Console.WriteLine("\nStep 6: Wait for weave MoveL, then WeaveEnd");
        weaveThread.Join();
        robot.WeaveEnd(0);
        Thread.Sleep(500);

        // ---- Step 7: MoveL back to start ----
        Console.WriteLine("\nStep 7: MoveL back to start");
        rtn = robot.MoveL(j1, d1, 1, 0, 100, 100, 50, -1, 0, epos, 0, 0, offset_pos, 50, 0, 0, 10);
        Console.WriteLine("  MoveL(back) rtn={0}", rtn);

        robot.GetRobotRealTimeState(ref pkg);
        Console.WriteLine("\n  Final robot state: main_code={0}, sub_code={1}", pkg.main_code, pkg.sub_code);
        Console.WriteLine("============================================================");
        Console.WriteLine("  Weave Speed and Offset Test Complete");
        Console.WriteLine("============================================================");
    }