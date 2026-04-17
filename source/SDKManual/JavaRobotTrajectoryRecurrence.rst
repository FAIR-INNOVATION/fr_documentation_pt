Reprodução de Trajetória do Robô
===================================================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros de Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDParam(int type, String name, int period_ms, int di_choose, int do_choose);

Iniciar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDStart(int type, String name, int period_ms, int di_choose, int do_choose);

Parar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: java
    :linenos:

    /**
    * @brief  Para a gravação de trajetória TPD
    * @return  Código de erro
    */
    int SetWebTPDStop(); 

Excluir Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Exclui a gravação de trajetória TPD
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */   
    int SetTPDDelete(string name); 

Pré-carregar Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Pré-carrega a trajetória
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */      
    int LoadTPD(String name);

Reproduzir Trajetória TPD
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Reproduz a trajetória
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] blend 0-não suave, 1-suave
    * @param  [in] ovl  Porcentagem de escala de velocidade, faixa [0~100]
    * @return  Código de erro
    */
    int MoveTPD(String name, int blend, double ovl); 

Obter Pose Inicial da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a pose inicial da trajetória 
    * @param [in] name  Nome do arquivo de trajetória, sem extensão
    * @param [out] desc_pose Pose inicial da trajetória obtida
    * @return Código de erro 
    */ 
    int GetTPDStartPose(String name, DescPose desc_pose); 

Exemplo de Código de Gravação de Trajetória TPD do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTPD(Robot robot)
    {
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        double ovl = 100.0;
        int blend = 0;

        DescPose start_pose =new DescPose() {};

        int rtn = robot.LoadTPD(name);
        System.out.println("LoadTPD rtn is:"+ rtn);

        robot.GetTPDStartPose(name, start_pose);
        robot.MoveCart(start_pose, 0, 0, 100, 100, ovl, -1, -1);
        robot.Sleep(1000);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.println("MoveTPD rtn is: "+ rtn);
        robot.Sleep(5000);

        robot.SetTPDDelete(name);
        return 0;
    }

Pré-processamento de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Pré-processamento de arquivo de trajetória externa 
    * @param [in] name Nome do arquivo de trajetória  
    * @param [in] ovl Porcentagem de escala de velocidade, faixa [0~100]
    * @param [in] opt 1-ponto de controle, padrão 1 
    * @return Código de erro 
    */ 
    int LoadTrajectoryJ(String name, double ovl, int opt); 

Reprodução de Trajetória
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Reprodução de trajetória de arquivo de trajetória externa  
    * @return Código de erro 
    */
    int MoveTrajectoryJ();

Obter Pose Inicial da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a pose inicial da trajetória 
    * @param [in] name Nome do arquivo de trajetória  
    * @param [out] desc_pose Pose inicial da trajetória obtida
    * @return Código de erro 
    */ 
    int GetTrajectoryStartPose(String name, DescPose desc_pose);

Obter Número do Ponto da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o número do ponto da trajetória
    * @return  Código de erro
    */
    public int GetTrajectoryPointNum(int pnum)

Definir Velocidade Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a velocidade durante a execução da trajetória
    * @param  [in] ovl Porcentagem de velocidade
    * @return  Código de erro
    */
    public int SetTrajectoryJSpeed(double ovl)

Definir Força e Torque Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a força e o torque durante a execução da trajetória
    * @param  [in] ft Força em três direções e torque, unidade N e Nm
    * @return  Código de erro
    */
    public int SetTrajectoryJForceTorque(ForceTorque ft)

Definir Força na Direção X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a força na direção X durante a execução da trajetória  
    * @param [in] fx Força na direção X, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFx(double fx);

Definir Força na Direção Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a força na direção Y durante a execução da trajetória
    * @param [in] fy Força na direção Y, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFy(double fy);

Definir Força na Direção Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a força na direção Z durante a execução da trajetória  
    * @param [in] fz  Força na direção Z, unidade N
    * @return Código de erro 
    */
    int SetTrajectoryJForceFz(double fz);

Definir Torque em Torno do Eixo X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo X durante a execução da trajetória  
    * @param [in] tx Torque em torno do eixo X, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTx(double tx);

Definir Torque em Torno do Eixo Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo Y durante a execução da trajetória  
    * @param [in] ty Torque em torno do eixo Y, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTy(double ty);

Definir Torque em Torno do Eixo Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o torque em torno do eixo Z durante a execução da trajetória  
    * @param [in] tz Torque em torno do eixo Z, unidade Nm
    * @return Código de erro 
    */
    int SetTrajectoryJTorqueTz(double tz);

Enviar Arquivo de Trajetória J
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Envia arquivo de trajetória J  
    * @param [in] filePath Caminho completo do arquivo de trajetória a ser enviado   C://test/testJ.txt
    * @return Código de erro 
    */
    int TrajectoryJUpLoad(String filePath);

Excluir Arquivo de Trajetória J
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Exclui arquivo de trajetória J  
    * @param [in] fileName Nome do arquivo testJ.txt
    * @return Código de erro 
    */
    int TrajectoryJDelete(String fileName);

Exemplo de Código de Reprodução de Arquivo de Trajetória J do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTraj(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");
        System.out.println("Upload TrajectoryJ A :"+ rtn);

        String traj_file_name = "/fruser/traj/traj.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        System.out.println("LoadTrajectoryJ:"+traj_file_name+", rtn is:"+ rtn);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);


        ExaxisPos epos=new ExaxisPos(0,0,0,0);
        DescPose po=new DescPose(0,0,0,0,0,0);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(traj_num);

        rtn = robot.SetTrajectoryJSpeed(50.0);
        System.out.println("SetTrajectoryJSpeed is:"+ rtn);

        ForceTorque traj_force=new ForceTorque(0,0,0,0,0,0);
        traj_force.fx = 10;
        rtn = robot.SetTrajectoryJForceTorque(traj_force);
        System.out.println("SetTrajectoryJForceTorque rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJForceFx(10.0);
        System.out.println("SetTrajectoryJForceFx rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFy(0.0);
        System.out.println("SetTrajectoryJForceFy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFz(0.0);
        System.out.println("SetTrajectoryJForceFz rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTx(10.0);
        System.out.println("SetTrajectoryJTorqueTx rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTy(10.0);
        System.out.println("SetTrajectoryJTorqueTy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJTorqueTz(10.0);
        System.out.println("SetTrajectoryJTorqueTz rtn is:"+ rtn);

        rtn = robot.MoveTrajectoryJ();
        System.out.println("MoveTrajectoryJ rtn is: "+ rtn);

        return 0;
    }

Pré-processamento de Trajetória (Antecedência de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief Pré-processamento de trajetória (Antecedência de trajetória) 
    * @param [in] name  Nome do arquivo de trajetória
    * @param [in] mode Modo de amostragem, 0-sem amostragem; 1-amostragem por intervalo de dados igual; 2-amostragem por limite de erro igual
    * @param [in] errorLim Limite de erro, usado quando a amostragem por limite de erro igual é ativada
    * @param [in] type Método de suavização, 0-suavização Bezier
    * @param [in] precision Precisão da suavização, usada quando a suavização Bezier é ativada
    * @param [in] vamx Velocidade máxima definida, mm/s
    * @param [in] amax Aceleração máxima definida, mm/s2
    * @param [in] jmax Jerk máximo definido, mm/s3
    * @return Código de erro 
    */ 
    int LoadTrajectoryLA(String name, int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax); 

Reprodução de Trajetória (Antecedência de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief Reprodução de trajetória (Antecedência de trajetória)  
    * @return Código de erro 
    */
    int MoveTrajectoryLA();

Exemplo de Código de Reprodução de Trajetória (Antecedência de Trajetória)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadTrajLA(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");

        String traj_file_name = "/fruser/traj/traj.txt";
        rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        rtn = robot.MoveTrajectoryLA();

        robot.CloseRPC();
        return 0;
    }

Mover para o Início da Gravação da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Move para o início da gravação da trajetória TPD
    * @param name Nome do arquivo de trajetória
    * @param moveType Tipo de movimento; 0-PTP; 1-LIN
    * @param ovl Porcentagem de escala de velocidade, faixa [0~100]
    * @return Código de erro
    */
    public int MoveToTPDStart(string name, int moveType, double ovl)

Exemplo de Código SDK para Mover para o Início da Gravação da Trajetória TPD
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testTPDmove (Robot robot)
    {
        int rtn = 0;
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(3000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        robot.Sleep(1000);
        double ovl = 100.0;
        int blend = 0;
        DescPose start_pose = new DescPose();
        rtn = robot.LoadTPD(name);
        System.out.printf("LoadTPD rtn is: %d\n", rtn);

        robot.GetTPDStartPose(name, start_pose);
        System.out.printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        //robot.MoveCart(&start_pose, 0, 0, 100, 100, ovl, -1, -1);
        //robot.Sleep(1000);

        rtn = robot.MoveToTPDStart(name, 0, 100);
        System.out.printf("MoveToTPDStart rtn is: %d\n", rtn);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.printf("MoveTPD rtn is: %d\n", rtn);

        robot.Sleep(5000);

        robot.SetTPDDelete(name);

        return ;
    }