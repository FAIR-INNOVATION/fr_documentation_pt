Reprodução de Trajetória do Robô
===================================================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros de Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  SetTPDParam(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose);

Iniciar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  SetTPDStart(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose); 

Parar Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Para a gravação de trajetória TPD
    * @return  Código de erro
    */
    errno_t  SetWebTPDStop();

Excluir Gravação de Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Exclui a gravação de trajetória TPD
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */   
    errno_t  SetTPDDelete(char name[30]);

Pré-carregar Trajetória TPD
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Pré-carrega a trajetória TPD
    * @param  [in] name  Nome do arquivo de trajetória
    * @return  Código de erro
    */      
    errno_t  LoadTPD(char name[30]);

Reproduzir Trajetória TPD
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Reproduz a trajetória TPD
    * @param  [in] name  Nome do arquivo de trajetória
    * @param  [in] blend 0-não suave, 1-suave
    * @param  [in] ovl  Porcentagem de escala de velocidade, faixa [0~100]
    * @return  Código de erro
    */
    errno_t  MoveTPD(char name[30], uint8_t blend, float ovl);

Obter Pose Inicial da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a pose inicial da trajetória TPD
    * @param [in] name Nome do arquivo TPD, sem extensão
    * @return Código de erro
    */   
    errno_t GetTPDStartPose(char name[30], DescPose *desc_pose);

Mover para o Início da Gravação da Trajetória TPD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Move para o início da gravação da trajetória TPD
    * @param [in] name Nome do arquivo de trajetória
    * @param [in] moveType Tipo de movimento; 0-PTP; 1-LIN
    * @param [in] ovl Porcentagem de escala de velocidade, faixa [0~100]
    * @return Código de erro
    */
    errno_t MoveToTPDStart(char name[30], uint8_t moveType, float ovl);
    
Exemplo de Código de Gravação de Trajetória TPD do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTPD(void)
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
    int type = 1;
    char name[30] = "tpd2025";
    int period_ms = 4;
    uint16_t di_choose = 0;
    uint16_t do_choose = 0;
    robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);
    robot.Mode(1);
    robot.Sleep(1000);
    robot.DragTeachSwitch(1);
    robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
    robot.Sleep(3000);
    robot.SetWebTPDStop();
    robot.DragTeachSwitch(0);
    robot.Sleep(1000);
    float ovl = 100.0;
    uint8_t blend = 0;
    DescPose start_pose = {};
    rtn = robot.LoadTPD(name);
    printf("LoadTPD rtn is: %d\n", rtn);
    robot.GetTPDStartPose(name, &start_pose);
    printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
    rtn = robot.MoveToTPDStart(name, 0, 100);
    printf("MoveToTPDStart rtn is: %d\n", rtn);
    rtn = robot.MoveTPD(name, blend, ovl);
    printf("MoveTPD rtn is: %d\n", rtn);
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    robot.SetTPDDelete(name);
    robot.CloseRPC();
    return 0;
    }

Pré-processamento de Trajetória
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Pré-processamento de trajetória
    * @param [in] name Nome do arquivo de trajetória
    * @param [in] ovl Porcentagem de escala de velocidade, faixa [0~100]
    * @param [in] opt 1-ponto de controle, padrão 1
    * @return Código de erro
    */   
    errno_t LoadTrajectoryJ(char name[30], float ovl, int opt);

Reprodução de Trajetória
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Reprodução de trajetória
    * @return Código de erro
    */   
    errno_t MoveTrajectoryJ();

Obter Pose Inicial da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a pose inicial da trajetória
    * @param [in] name Nome do arquivo de trajetória
    * @return Código de erro
    */   
    errno_t GetTrajectoryStartPose(char name[30], DescPose *desc_pose);

Obter Número do Ponto da Trajetória
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o número do ponto da trajetória
    * @return Código de erro
    */   
    errno_t GetTrajectoryPointNum(int *pnum);

Definir Velocidade Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

Definir Força e Torque Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a força e o torque durante a execução da trajetória
    * @param [in] ft Força em três direções e torque, unidade N e Nm
    * @return Código de erro
    */   
    errno_t SetTrajectoryJForceTorque(ForceTorque *ft);

Definir Força na Direção X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a força na direção X durante a execução da trajetória
    * @param [in] fx Força na direção X, unidade N
    * @return Código de erro
    */   
    errno_t SetTrajectoryJForceFx(double fx);

Definir Força na Direção Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a força na direção Y durante a execução da trajetória
    * @param [in] fy Força na direção Y, unidade N
    * @return Código de erro
    */   
    errno_t SetTrajectoryJForceFy(double fy);

Definir Força na Direção Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a força na direção Z durante a execução da trajetória
    * @param [in] fz Força na direção X, unidade N
    * @return Código de erro
    */   
    errno_t SetTrajectoryJForceFz(double fz);

Definir Torque em Torno do Eixo X Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o torque em torno do eixo X durante a execução da trajetória
    * @param [in] tx Torque em torno do eixo X, unidade Nm
    * @return Código de erro
    */   
    errno_t SetTrajectoryJTorqueTx(double tx);

Definir Torque em Torno do Eixo Y Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o torque em torno do eixo Y durante a execução da trajetória
    * @param [in] ty Torque em torno do eixo Y, unidade Nm
    * @return Código de erro
    */   
    errno_t SetTrajectoryJTorqueTy(double ty);

Definir Torque em Torno do Eixo Z Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o torque em torno do eixo Z durante a execução da trajetória
    * @param [in] tz Torque em torno do eixo Z, unidade Nm
    * @return Código de erro
    */   
    errno_t SetTrajectoryJTorqueTz(double tz);

Enviar Arquivo de Trajetória J
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief Envia arquivo de trajetória J
	 * @param [in] filePath Caminho completo do arquivo de trajetória a ser enviado   C://test/testJ.txt
	 * @return Código de erro
	 */
	errno_t TrajectoryJUpLoad(const std::string& filePath);

Excluir Arquivo de Trajetória J
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief Exclui arquivo de trajetória J
	 * @param [in] fileName Nome do arquivo testJ.txt
	 * @return Código de erro
	 */
	errno_t TrajectoryJDelete(const std::string& fileName);

Exemplo de Código de Reprodução de Arquivo de Trajetória J do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTraj(void)
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
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj1.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj1.txt";
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
      rtn = robot.SetTrajectoryJSpeed(50.0);
      printf("SetTrajectoryJSpeed is: %d\n", rtn);
      ForceTorque traj_force;
      memset(&traj_force, 0, sizeof(ForceTorque));
      traj_force.fx = 10;
      rtn = robot.SetTrajectoryJForceTorque(&traj_force);
      printf("SetTrajectoryJForceTorque rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFx(10.0);
      printf("SetTrajectoryJForceFx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFy(0.0);
      printf("SetTrajectoryJForceFy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFz(0.0);
      printf("SetTrajectoryJForceFz rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTx(10.0);
      printf("SetTrajectoryJTorqueTx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTy(10.0);
      printf("SetTrajectoryJTorqueTy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTz(10.0);
      printf("SetTrajectoryJTorqueTz rtn is: %d\n", rtn);
      rtn = robot.MoveTrajectoryJ();
      printf("MoveTrajectoryJ rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Pré-processamento de Trajetória (Antecedência de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Pré-processamento de trajetória (Antecedência de trajetória)
    * @param [in] name Nome do arquivo de trajetória
    * @param [in] mode Modo de amostragem, 0-sem amostragem; 1-amostragem por intervalo de dados igual; 2-amostragem por limite de erro igual
    * @param [in] errorLim Limite de erro, usado quando a amostragem por limite de erro igual é ativada
    * @param [in] type Método de suavização, 0-suavização Bezier
    * @param [in] precision Precisão da suavização, usada quando a suavização Bezier é ativada
    * @param [in] vamx Velocidade máxima definida, mm/s
    * @param [in] amax Aceleração máxima definida, mm/s2
    * @param [in] jmax Jerk máximo definido, mm/s3
    * @param [in] flag Interruptor de antecipação de velocidade constante 0-desativar; 1-ativar
    * @return Código de erro
    */
    errno_t LoadTrajectoryLA(char name[30], int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax, int flag = 0);

Reprodução de Trajetória (Antecedência de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  Reprodução de trajetória (Antecedência de trajetória)
    * @return  Código de erro
    */
    errno_t MoveTrajectoryLA();

Exemplo de Código de Reprodução de Trajetória (Antecedência de Trajetória)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLoadTrajLA(void)
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
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj.txt";
      rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);
      printf("LoadTrajectoryLA %s, rtn is: %d\n", traj_file_name, rtn);
      DescPose traj_start_pose;
      memset(&traj_start_pose, 0, sizeof(DescPose));
      rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
      printf("GetTrajectoryStartPose is: %d\n", rtn);
      printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
      std::this_thread::sleep_for(std::chrono::seconds(1));
      robot.SetSpeed(50);
      robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
      rtn = robot.MoveTrajectoryLA();
      printf("MoveTrajectoryLA rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }