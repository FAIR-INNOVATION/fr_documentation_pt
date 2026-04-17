Outras Interfaces
========================

.. toctree:: 
    :maxdepth: 5

Obter Chave Pública SSH
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter chave pública SSH
    * @param [out] keygen Chave pública
    * @return Código de erro
    */
    int GetSSHKeygen(ref string keygen);

Enviar Comando SCP
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief Enviar comando SCP
    * @param [in] mode 0-upload (PC -> controlador), 1-download (controlador -> PC)
    * @param [in] sshname Nome de usuário do PC
    * @param [in] sship Endereço IP do PC
    * @param [in] usr_file_url Caminho do arquivo no PC
    * @param [in] robot_file_url Caminho do arquivo no controlador do robô
    * @return Código de erro
    */
    int SetSSHScpCmd(int mode, string sshname, string sship, string usr_file_url, string robot_file_url);

Calcular o Valor MD5 de um Arquivo em um Caminho Especificado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Calcular o valor MD5 de um arquivo em um caminho especificado
    * @param [in] file_path Caminho do arquivo incluindo o nome do arquivo. O caminho padrão da pasta Traj é: "/fruser/traj/", ex: "/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 Valor MD5 do arquivo
    * @return Código de erro
    */
    int ComputeFileMD5(string file_path, ref string md5);

Exemplo de Código de Comandos SSH e MD5 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        string file_path = "/fruser/airlab.lua";
        string md5 = "";
        byte emerg_state = 0;
        byte si0_state = 0;
        byte si1_state = 0;
        int sdk_com_state = 0;

        string ssh_keygen = "";
        int retval = robot.GetSSHKeygen(ref ssh_keygen);
        Console.WriteLine("GetSSHKeygen retval is: {0}", retval);
        Console.WriteLine("ssh key is: {0}", ssh_keygen);

        string ssh_name = "fr";
        string ssh_ip = "192.168.58.45";
        string ssh_route = "/home/fr";
        string ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        Console.WriteLine("SetSSHScpCmd retval is: {0}", retval);
        Console.WriteLine("robot url is: {0}", ssh_robot_url);

        robot.ComputeFileMD5(file_path, ref md5);
        Console.WriteLine("md5 is: {0}", md5);
    }

Definir o Período de Feedback da Porta 20004 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir o período de feedback da porta 20004 do robô
    * @param [in] period Período de feedback da porta 20004 do robô (ms)
    * @return Código de erro
    */
    int SetRobotRealtimeStateSamplePeriod(int period);

Obter o Período de Feedback da Porta 20004 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obter o período de feedback da porta 20004 do robô
    * @param [out] period Período de feedback da porta 20004 do robô (ms)
    * @return Código de erro
    */
    int GetRobotRealtimeStateSamplePeriod(ref int period);

Exemplo de Código de Configuração do Período de Feedback de Estado da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button47_Click(object sender, EventArgs e)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        int getPeriod = 0;
        robot.GetRobotRealtimeStateSamplePeriod(ref getPeriod);
        Console.WriteLine("period is {0}", getPeriod);
        Thread.Sleep(1000);
    }

Atualização de Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Atualização de software do robô
    * @param [in] filePath Caminho completo do pacote de atualização de software
    * @param [in] block Bloquear até a conclusão da atualização? true: bloqueante; false: não bloqueante
    * @return  Código de erro
    */
    int SoftwareUpgrade(string filePath, bool block);

Obter o Status da Atualização de Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter o status da atualização de software do robô
    * @param [out] state Status da atualização do pacote de software do robô: 0-ocioso ou enviando pacote de atualização; 1~100: porcentagem de conclusão da atualização; -1: falha na atualização do software; -2: falha na verificação; -3: falha na verificação de versão; -4: falha na descompactação; -5: falha na atualização da configuração do usuário; -6: falha na atualização da configuração do periférico; -7: falha na atualização da configuração do eixo extensor; -8: falha na atualização da configuração do robô; -9: falha na atualização da configuração dos parâmetros DH
    * @return  Código de erro
    */
    int GetSoftwareUpgradeState(ref int state);

Exemplo de Código de Atualização de Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button48_Click(object sender, EventArgs e)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            int curState = -1;
            robot.GetSoftwareUpgradeState(ref curState);
            Console.WriteLine("upgrade state is {0}", curState);
            Thread.Sleep(300);
        }
    }

Baixar Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Baixar tabela de pontos do controlador do robô para o computador local
    * @param [in] pointTableName Nome da tabela de pontos no controlador: pointTable1.db
    * @param [in] saveFilePath Caminho para onde a tabela de pontos será baixada no computador C://test/
    * @return Código de erro
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

Enviar Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Enviar tabela de pontos do computador local para o controlador do robô
    * @param [in] pointTableFilePath Caminho absoluto da tabela de pontos no computador local C://test/pointTable1.db
    * @return Código de erro
    */
    int PointTableUpLoad(string pointTableFilePath);

Atualizar Programa Lua com a Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Atualizar pontos em um programa Lua usando a tabela de pontos fornecida
    * @param [in] pointTableName Nome da tabela de pontos no controlador: "pointTable1.db". Quando a tabela de pontos está vazia, ou seja, "", indica que o programa Lua deve ser atualizado para o programa inicial sem a aplicação da tabela de pontos.
    * @param [in] luaFileName Nome do arquivo Lua a ser atualizado: "test.lua"
    * @param [out] errorStr Mensagem de erro da atualização do programa Lua com a tabela de pontos
    * @return Código de erro
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

Alternar e Aplicar Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Alternar e aplicar tabela de pontos
    * @param [in] pointTableName Nome da tabela de pontos para alternar: "pointTable1.db"
    * @param [out] errorStr Mensagem de erro da alternância da tabela de pontos
    * @return Código de erro
    */
    int PointTableSwitch(string pointTableName, ref string errorStr);

Exemplo de Código de Operações com Tabela de Pontos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        string save_path = "D://zDOWN/";
        string point_table_name = "test_point_A.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);
        Console.WriteLine("download : {0} fail: {1}", point_table_name, rtn);

        string upload_path = "D://zUP/test_point_A.db";
        rtn = robot.PointTableUpLoad(upload_path);
        Console.WriteLine("retval is: {0}", rtn);

        string point_tablename = "test_point_A.db";
        string lua_name = "Text1.lua";

        string errorStr = "";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name, ref errorStr);
        Console.WriteLine("retval is: {0}", rtn);
    }

Baixar Log do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Baixar log do controlador
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return  Código de erro
    */
    int RbLogDownload(string savePath);

Baixar Todas as Fontes de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Baixar todas as fontes de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return  Código de erro
    */
    int AllDataSourceDownload(string savePath);

Baixar Pacote de Backup de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Baixar pacote de backup de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return  Código de erro
    */
    int DataPackageDownload(string savePath);

Exemplo de Código para Baixar Dados do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button50_Click(object sender, EventArgs e)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");
        Console.WriteLine("RbLogDownload rtn is {0}", rtn);

        rtn = robot.AllDataSourceDownload("D://zDOWN/");
        Console.WriteLine("AllDataSourceDownload rtn is {0}", rtn);

        rtn = robot.DataPackageDownload("D://zDOWN/");
        Console.WriteLine("DataPackageDownload rtn is {0}", rtn);
    }

Atualização do Sistema Operacional do Robô (Painel de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Atualização do sistema operacional do robô (Painel de Controle LA)
     * @param [in] filePath Caminho completo do pacote de atualização do sistema operacional
     * @return  Código de erro
     */
    public int KernelUpgrade(string filePath)

Obter o Resultado da Atualização do Sistema Operacional do Robô (Painel de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obter o resultado da atualização do sistema operacional do robô (Painel de Controle LA)
     * @param [out] result Resultado da atualização: 0: sucesso; -1: falha
     * @return  Código de erro
     */
    public int GetKernelUpgradeResult(ref int[] result)

Definir Atualização do Codificador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir atualização do codificador
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int SetEncoderUpgrade(string path);

Definir Atualização de Firmware da Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir atualização de firmware da junta
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int SetJointFirmwareUpgrade(int type, string path);

Definir Atualização de Firmware do Painel de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir atualização de firmware do painel de controle
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int SetCtrlFirmwareUpgrade(int type, string path);

Definir Atualização de Firmware da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir atualização de firmware da extremidade
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int SetEndFirmwareUpgrade(int type, string path);

Atualização do Arquivo de Configuração de Parâmetros Completos da Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Atualização do arquivo de configuração de parâmetros completos da junta
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int JointAllParamUpgrade(string path);

Exemplo de Código de Atualização de Firmware do Escravo do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: c#
    :linenos:

    private void button83_Click(object sender, EventArgs e)
    {
        robot.RobotEnable(0);
        Thread.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/jointallparameters.db");
        Console.WriteLine($"robot JointAllParamUpgrade rtn is{rtn}");
        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/upgrade/FR_CTRL_PRIMCU_FV201212_MAIN_U4_T01_20250428(MT).bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/upgrade/FR_END_FV201009_MAIN_U1_T01_20250428.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/upgrade/FR_SERVO_FV504214_MAIN_U7_T07_20250519.bin");
        Console.WriteLine($"robot SetJointFirmwareUpgrade rtn is{rtn}");
    }

Geração de Log do MCU do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Geração de log do MCU do robô
    * @return Código de erro
    */
    public int RobotMCULogCollect();

Definir Parada do Robô ao Desconectar a Comunicação da Porta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir parada do robô ao desconectar a comunicação da porta
    * @param [in] portID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param [in] enable 0-desabilitar; 1-habilitar
    * @param [in] confirmTime Duração para confirmar a interrupção da comunicação (ms)[0-5000]
    * @return  Código de erro
    */
    public int SetRobotStopOnComDisc(int portID, bool enable, int confirmTime)

Obter Parâmetros de Parada do Robô ao Desconectar a Comunicação da Porta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter parâmetros de parada do robô ao desconectar a comunicação da porta
    * @param [in] portID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param [out] enable 0-desabilitar; 1-habilitar
    * @param [out] confirmTime Duração para confirmar a interrupção da comunicação (ms)[0-5000]
    * @return  Código de erro
    */
    public int GetRobotStopOnComDisc(int portID, ref bool enable, ref int confirmTime)

Exemplo de Código dos Parâmetros de Parada do Robô ao Desconectar a Comunicação da Porta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestRobotStopOnComDisc()
    {
        int rtn = 0;

        // Definir parâmetros para as quatro portas
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        Console.WriteLine($"SetRobotStopOnComDisc {rtn}");

        bool enable = false;
        int confirmTime = 0;

        // Obter e imprimir a configuração de cada porta
        robot.GetRobotStopOnComDisc(0, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(1, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8083 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(2, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(3, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

    }

Enviar Quadro de Instrução UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Enviar quadro de instrução UDP
    * @param [in] Quadro de instrução
    * @return Código de erro
    */
    public int SendUDPFrame(string frame)

Exemplo de Código SDK Baseado em Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestRobotUDP()
    {
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[Resposta UDP] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };


        // Enviar quadro
        string frameToSend = "/f/bIII52III236III7IIIMode(1)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII52III236III7IIIMode(0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII41III201III153IIIMoveJ(53.857,-89.441,119.453,-22.664,61.059,3.369,-54.249,-491.930,375.396,96.474,-6.896,-7.783,0,0,100,100,100,0.000,0.000,0.000,0.000,-1,0,0,0,0,0,0,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII42III203III163IIIMoveL(81.736,-85.284,114.974,-23.261,88.746,6.799,125.744,-506.570,375.396,96.474,-6.896,-7.783,0,0,100,100,100,-1,0,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,0,100,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII47III400III15IIIGetMCVersion(1)III/b/f/f/bIII48III424III21IIIGetSlaveFirmVersion()III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);

    }

Definir Cor do LED da Extremidade do Robô Personalizada pelo Usuário
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir cor do LED da extremidade do robô personalizada pelo usuário
    * @param [in] r Controle do LED vermelho da extremidade; 0-apagado; 1-aceso
    * @param [in] g Controle do LED verde da extremidade; 0-apagado; 1-aceso
    * @param [in] b Controle do LED azul da extremidade; 0-apagado; 1-aceso
    * @return Código de erro
    */
    public int SetUserLEDColor(bool r, bool g, bool b)

Exemplo de Código SDK para Definir Cor do LED da Extremidade do Robô Personalizada pelo Usuário
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void testled()
    {
        robot.SetUserLEDColor(true, true, true);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(true, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, true, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, true);
    }