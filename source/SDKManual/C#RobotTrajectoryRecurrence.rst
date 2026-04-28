Reprodução de Trajetória do Robô
==================================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros de Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define os parâmetros de gravação de trajetória TPD
    * @param  [in] type  Tipo de dados de gravação, 1-posição articular
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] period_ms  Período de amostragem de dados, valores fixos 2ms, 4ms ou 8ms
    * @param  [in] di_choose  Seleção DI, bit0~bit7 correspondem aos DI0~DI7 do painel de controle, bit8~bit9 correspondem aos DI0~DI1 da extremidade, 0-não selecionar, 1-selecionar
    * @param  [in] do_choose  Seleção DO, bit0~bit7 correspondem aos DO0~DO7 do painel de controle, bit8~bit9 correspondem aos DO0~DO1 da extremidade, 0-não selecionar, 1-selecionar
    * @return  Código de erro
    */
    int SetTPDParam(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose);

Iniciar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Inicia a gravação de trajetória TPD
    * @param  [in] type  Tipo de dados de gravação, 1-posição articular
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] period_ms  Período de amostragem de dados, valores fixos 2ms, 4ms ou 8ms
    * @param  [in] di_choose  Seleção DI, bit0~bit7 correspondem aos DI0~DI7 do painel de controle, bit8~bit9 correspondem aos DI0~DI1 da extremidade, 0-não selecionar, 1-selecionar
    * @param  [in] do_choose  Seleção DO, bit0~bit7 correspondem aos DO0~DO7 do painel de controle, bit8~bit9 correspondem aos DO0~DO1 da extremidade, 0-não selecionar, 1-selecionar
    * @return  Código de erro
    */
    int SetTPDStart(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose); 

Parar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Para a gravação de trajetória TPD
    * @return  Código de erro
    */
    int SetWebTPDStop(); 

Excluir Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Exclui a gravação de trajetória TPD
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */   
    int SetTPDDelete(string name); 

Pré-carregar Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Pré-carrega a trajetória
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */      
    int LoadTPD(string name);

Obter Pose Inicial da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém a pose inicial da trajetória 
    * @param [in] name  Nome do arquivo de trajetória
    * @param [out] desc_pose Pose inicial da trajetória 
    * @return Código de erro 
    */ 
    int GetTPDStartPose(string name, ref DescPose desc_pose); 

Reproduzir Trajetória TPD
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Reproduz a trajetória
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] blend 0-não suave, 1-suave
    * @param  [in] ovl  Porcentagem de escala de velocidade, faixa [0~100]
    * @return  Código de erro
    */
    int MoveTPD(string name, byte blend, float ovl); 

Exemplo de Código de Gravação de Trajetória TPD do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnTPDMove_Click(object sender, EventArgs e)
    {
        int type = 1;
        string name = "tpd2025";
        int period_ms = 4;
        ushort di_choose = 0;
        ushort do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        Thread.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        float ovl = 100.0f;
        byte blend = 0;

        DescPose start_pose = new DescPose();

        int rtn = robot.LoadTPD(name);
        Console.WriteLine("LoadTPD rtn is: {0}\n", rtn);

        robot.GetTPDStartPose(name, ref start_pose);
        Console.WriteLine("start pose, xyz is: {0} {1} {2}. rpy is: {3} {4} {5} \n",
            start_pose.tran.x, start_pose.tran.y, start_pose.tran.z,
            start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        robot.MoveCart(start_pose, 0, 0, 100, 100, ovl, -1, -1);
        Thread.Sleep(1000);

        rtn = robot.MoveTPD(name, blend, ovl);
        Console.WriteLine("MoveTPD rtn is: {0}\n", rtn);
        Thread.Sleep(5000);

        robot.SetTPDDelete(name);
    }

Pré-processamento de Arquivo de Trajetória Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Pré-processamento de arquivo de trajetória externa 
    * @param [in] name Nome do arquivo de trajetória  
    * @param [in] ovl Porcentagem de escala de velocidade, faixa [0~100] 
    * @param [in] opt 1-ponto de controle, padrão 1 
    * @return Código de erro 
    */ 
    int LoadTrajectoryJ(string name, float ovl, int opt); 

Reprodução de Trajetória de Arquivo de Trajetória Externa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Reprodução de trajetória de arquivo de trajetória externa  
    * @return Código de erro 
    */
    int MoveTrajectoryJ();

Obter Posição Inicial da Trajetória do Arquivo de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém a posição inicial da trajetória do arquivo de trajetória 
    * @param [in] name Nome do arquivo de trajetória  
    * @param [out] desc_pose Pose inicial da trajetória  
    * @return Código de erro 
    */ 
    int GetTrajectoryStartPose(string name, ref DescPose desc_pose); 

Obter Número do Ponto da Trajetória do Arquivo de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obtém o número do ponto da trajetória   
    * @param [out] pnum Número do ponto da trajetória  
    * @return Código de erro 
    */  
    int GetTrajectoryPointNum(ref int pnum);

Definir Velocidade Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Definir a velocidade durante a execução da trajetória
    * @param [in] ovl Percentual de velocidade [0-100.0]
    * @param [in] mode Modo; 0-modo de redução de velocidade; 1-comutação direta
    * @return Código de erro
    */
    errno_t SetTrajectoryJSpeed(float ovl, int mode = 0);

Exemplo de Código para Definir a Velocidade do Robô Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSetTrajectoryJSpeed() 
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 30000, 500);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        
        rtn = robot.TrajectoryJUpLoad("D://zUP/trajHelix_aima_1.txt");
        printf("Upload TrajectoryJ A %d\n", rtn);
        char traj_file_name[90] = "/fruser/traj/trajHelix_aima_1.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        printf("LoadTrajectoryJ %s, rtn is: %d\n", traj_file_name, rtn);
        DescPose traj_start_pose;
        memset(&traj_start_pose, 0, sizeof(DescPose));
        rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
        printf("GetTrajectoryStartPose is: %d\n", rtn);
        printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
        std::this_thread::sleep_for(std::chrono::seconds(1));
        robot.SetSpeed(50);
        robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(&traj_num);
        printf("GetTrajectoryStartPose rtn is: %d, traj num is: %d\n", rtn, traj_num);
        rtn = robot.MoveTrajectoryJ();
        printf("MoveTrajectoryJ rtn is: %d\n", rtn);
        robot.Sleep(1000);
        robot.GetRobotRealTimeState(&pkg);
        int trajspeedMode = 1;
        while (pkg.motion_done == 0)
        {
            robot.GetRobotRealTimeState(&pkg);
            rtn = robot.SetTrajectoryJSpeed(10.0, trajspeedMode);
            printf("SetTrajectoryJSpeed is: %d\n", rtn);
            robot.Sleep(1000);
            rtn = robot.SetTrajectoryJSpeed(80.0, trajspeedMode);
            printf("SetTrajectoryJSpeed is: %d\n", rtn);
            robot.Sleep(1000);
        }
        robot.CloseRPC();
        robot.Sleep(1000000);
        return 0;
    }

Definir Força e Torque Durante a Execução da Trajetória do Arquivo de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define a força e o torque durante a execução da trajetória do arquivo de trajetória  
    * @param [in] ft Força em três direções e torque, unidade N e Nm
    * @return Código de erro 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

Definir Força na Direção X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define a força na direção X durante a execução da trajetória  
    * @param [in] fx  Força na direção X, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFx(double fx);

Definir Força na Direção Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define a força na direção Y durante a execução da trajetória  
    * @param [in] fy  Força na direção Y, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFy(double fy);

Definir Força na Direção Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define a força na direção Z durante a execução da trajetória  
    * @param [in] fz  Força na direção Z, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFz(double fz);

Definir Torque em Torno do Eixo X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo X durante a execução da trajetória  
    * @param [in] tx  Torque em torno do eixo X, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTx(double tx);

Definir Torque em Torno do Eixo Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo Y durante a execução da trajetória  
    * @param [in] ty  Torque em torno do eixo Y, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTy(double ty);

Definir Torque em Torno do Eixo Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo Z durante a execução da trajetória  
    * @param [in] tz  Torque em torno do eixo Z, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTz(double tz);

Enviar Arquivo de Trajetória J
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Envia arquivo de trajetória J
    * @param [in] filePath Caminho completo do arquivo de trajetória a ser enviado   C://test/testJ.txt
    * @return Código de erro
    */
    int TrajectoryJUpLoad(string filePath);

Excluir Arquivo de Trajetória J
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Exclui arquivo de trajetória J
    * @param [in] fileName Nome do arquivo testJ.txt
    * @return Código de erro
    */
    int TrajectoryJDelete(string fileName);

Exemplo de Código de Reprodução de Arquivo de Trajetória J do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button33_Click(object sender, EventArgs e)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/spray_traj1.txt");
        Console.WriteLine("Upload TrajectoryJ A {0}\n", rtn);

        string traj_file_name = "/fruser/traj/spray_traj1.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        Console.WriteLine("LoadTrajectoryJ {0}, rtn is: {1}\n", traj_file_name, rtn);

        DescPose traj_start_pose = new DescPose();
        rtn = robot.GetTrajectoryStartPose(traj_file_name, ref traj_start_pose);
        Console.WriteLine("GetTrajectoryStartPose is: {0}\n", rtn);
        Console.WriteLine("desc_pos:{0},{1},{2},{3},{4},{5}\n",
            traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z,
            traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);

        Thread.Sleep(1000);

        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(ref traj_num);
        Console.WriteLine("GetTrajectoryStartPose rtn is: {0}, traj num is: {1}\n", rtn, traj_num);

        rtn = robot.SetTrajectoryJSpeed(50.0f);
        Console.WriteLine("SetTrajectoryJSpeed is: {0}\n", rtn);

        ForceTorque traj_force = new ForceTorque();
        traj_force.fx = 10;
        rtn = robot.SetTrajectoryJForceTorque(traj_force);
        Console.WriteLine("SetTrajectoryJForceTorque rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFx(10.0f);
        Console.WriteLine("SetTrajectoryJForceFx rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFy(0.0f);
        Console.WriteLine("SetTrajectoryJForceFy rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFz(0.0f);
        Console.WriteLine("SetTrajectoryJForceFz rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTx(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTx rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTy(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTy rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTz(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTz rtn is: {0}\n", rtn);

        rtn = robot.MoveTrajectoryJ();
        Console.WriteLine("MoveTrajectoryJ rtn is: {0}\n", rtn);
    }

Pré-processamento de Trajetória (Antecedência de Trajetória)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Pré-processamento de trajetória (Antecedência de trajetória)
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] mode Modo de amostragem, 0-sem amostragem; 1-amostragem por intervalo de dados igual; 2-amostragem por limite de erro igual
    * @param  [in] errorLim Limite de erro, usado quando a amostragem por limite de erro igual é ativada
    * @param  [in] type Método de suavização, 0-suavização Bezier
    * @param  [in] precision Precisão da suavização, usada quando a suavização Bezier é ativada
    * @param  [in] vamx Velocidade máxima definida, mm/s
    * @param  [in] amax Aceleração máxima definida, mm/s2
    * @param  [in] jmax Jerk máximo definido, mm/s3
    * @return  Código de erro   
    */
    int LoadTrajectoryLA(string name, int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax);

Reprodução de Trajetória (Antecedência de Trajetória)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Reprodução de trajetória (Antecedência de trajetória)
    * @return  Código de erro   
    */
    int MoveTrajectoryLA();

Exemplo de Código de Reprodução de Trajetória (Antecedência de Trajetória)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button8_Click(object sender, EventArgs e)
    {
        int rtn = 0;

        string nameA = "/fruser/traj/A.txt";
        string nameB = "/fruser/traj/B.txt";

        rtn = robot.LoadTrajectoryLA(nameB, 0, 0, 0, 1, 100.0, 100.0, 1000.0);    // Ajuste linear
        Console.WriteLine($"LoadTrajectoryLA rtn is {rtn}");

        DescPose startPos = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetTrajectoryStartPose(nameA, ref startPos);

        //
        robot.MoveCart(startPos, 1, 0, (float)100.0, (float)100.0, (float)100.0, -1, -1);

        rtn = robot.MoveTrajectoryLA();
        Console.WriteLine($"MoveTrajectoryLA rtn is {rtn}");
    }

Mover para o Início da Gravação da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Move para o início da gravação da trajetória TPD
    * @param [in] name Nome do arquivo de trajetória
    * @param [in] moveType Tipo de movimento; 0-PTP; 1-LIN
    * @param [in] ovl Porcentagem de escala de velocidade, faixa [0~100]
    * @return Código de erro
    */
    public int MoveToTPDStart(string name, int moveType, double ovl)

Exemplo de Código SDK para Mover para o Início da Gravação da Trajetória TPD
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void testTPDmove()
    {
        string name = "tpd2025";
        int type = 1;
        int period_ms = 4;
        int rtn = 0;
        UInt16 di_choose = 0;
        UInt16 do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        Thread.Sleep(3000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        Thread.Sleep(3000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        Thread.Sleep(1000);
        float ovl = 100.0f;
        byte blend = 0;
        DescPose start_pose = new DescPose();
        rtn = robot.LoadTPD(name);
        Console.WriteLine($"LoadTPD rtn is:{rtn}\n");

        robot.GetTPDStartPose(name, ref start_pose);
        Console.WriteLine($"start pose, xyz is: %f %f %f. rpy is: {start_pose.tran.x},{start_pose.tran.y}, {start_pose.tran.z}, {start_pose.rpy.rx}, {start_pose.rpy.ry}, {start_pose.rpy.rz}");

        rtn = robot.MoveToTPDStart(name, 0, 100.0);

        rtn = robot.MoveTPD(name, blend, ovl);
        Thread.Sleep(5000*5);

        robot.SetTPDDelete(name);
    }