Outras Interfaces
=====================

.. toctree:: 
    :maxdepth: 5

Obter Chave Pública SSH
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a chave pública SSH
    * @param [out] keygen Chave pública
    * @return Código de erro
    */
    int GetSSHKeygen(String[] keygen)

Enviar Comando SCP
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /** 
    * @brief Envia comando SCP
    * @param [in] mode 0-upload (PC -> controlador), 1-download (controlador -> PC)
    * @param [in] sshname Nome de usuário do PC
    * @param [in] sship Endereço IP do PC
    * @param [in] usr_file_url Caminho do arquivo no PC
    * @param [in] robot_file_url Caminho do arquivo no controlador do robô
    * @return Código de erro
    */
    int SetSSHScpCmd(int mode, String sshname, String sship, String usr_file_url, String robot_file_url)

Calcular o Valor MD5 de um Arquivo em um Caminho Especificado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o valor MD5 de um arquivo em um caminho especificado
    * @param [in] file_path Caminho do arquivo incluindo o nome do arquivo. O caminho padrão da pasta Traj é: "/fruser/traj/", ex: "/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 Valor MD5 do arquivo
    * @return Código de erro
    */
    int ComputeFileMD5(String file_path, String[] md5)

Exemplo de Código para Comandos SSH e MD5 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSSHMd5(Robot robot)
    {
        String file_path= "/fruser/airlab.lua";
        String[] md5 =new String[]{""};

        String[] ssh_keygen=new String[]{""};
        int retval = robot.GetSSHKeygen(ssh_keygen);
        System.out.println(ssh_keygen[0]);

        String ssh_name = "fr";
        String ssh_ip = "192.168.58.45";
        String ssh_route = "/home/fr";
        String ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        System.out.println("SetSSHScpCmd retval is:"+ retval);
        System.out.println("robot url is:"+ ssh_robot_url);

        robot.ComputeFileMD5(file_path, md5);
        System.out.println("md5 is:+"+ md5[0]);
        return 0;
    }

Definir o Período de Feedback da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o período de feedback da porta 20004 do robô
    * @param [in] period Período de feedback da porta 20004 do robô (ms)
    * @return  Código de erro
    */
    public int SetRobotRealtimeStateSamplePeriod(int period)

Obter o Período de Feedback da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o período de feedback da porta 20004 do robô
    * @return  List[0]: Código de erro; List[1]: Período de feedback da porta 20004 do robô (ms)
    */
    public List<Integer> GetRobotRealtimeStateSamplePeriod()

Exemplo de Código para Configuração do Período de Feedback de Estado da Porta 20004 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRealtimePeriod(Robot robot)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        List<Integer> getPeriod = new ArrayList<>();
        getPeriod=robot.GetRobotRealtimeStateSamplePeriod();
        robot.Sleep(1000);

        return 0;
    }

Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Atualização de software do robô
     * @param [in] filePath Caminho completo do pacote de atualização de software
     * @param [in] block Se bloqueia até que a atualização seja concluída true: bloqueia; false: não bloqueia
     * @return  Código de erro
     */
    public int SoftwareUpgrade(String filePath, boolean block)

Obter Estado da Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado da atualização de software do robô
    * @return  List[0]: Código de erro; List[1]: Estado da atualização de software do robô 0-ocioso ou enviando pacote de atualização; 1~100: porcentagem de conclusão da atualização; -1: falha na atualização do software; -2: falha na verificação; -3: falha na verificação de versão; -4: falha na descompactação; -5: falha na atualização da configuração do usuário; -6: falha na atualização da configuração do periférico; -7: falha na atualização da configuração do eixo de extensão; -8: falha na atualização da configuração do robô; -9: falha na atualização da configuração do parâmetro DH
    */
    public List<Integer> GetSoftwareUpgradeState()

Exemplo de Código para Atualização de Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUpgrade(Robot robot)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            List<Integer> inter=new ArrayList<>();
            inter=robot.GetSoftwareUpgradeState();
            System.out.println("upgrade state is:"+ inter.get(1));
            robot.Sleep(300);
        }
    }

Download do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Download do banco de dados da tabela de pontos 
    * @param [in] pointTableName Nome da tabela de pontos a ser baixada    pointTable1.db
    * @param [in] saveFilePath Caminho para salvar a tabela de pontos baixada   C://test/
    * @return Código de erro 
    */
    int PointTableDownLoad(String pointTableName, String saveFilePath);

Upload do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Upload do banco de dados da tabela de pontos 
    * @param [in] pointTableFilePath Caminho completo do arquivo da tabela de pontos a ser enviado   C://test/pointTable1.db
    * @return Código de erro 
    */
    int PointTableUpLoad(String pointTableFilePath);

Atualizar Arquivo Lua com a Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Atualizar o arquivo Lua com a tabela de pontos
    * @param [in] pointTableName Nome da tabela de pontos a ser alternada   "pointTable1.db". Quando a tabela de pontos estiver vazia, ou seja, "", indica que o programa Lua deve ser atualizado para o programa inicial sem a tabela de pontos aplicada
    * @param [in] luaFileName Nome do arquivo Lua a ser atualizado   "testPointTable.lua"
    * @param [out] errorStr Mensagem de erro ao alternar a tabela de pontos
    * @return Código de erro 
    */
    int PointTableUpdateLua(String pointTableName, String luaFileName, String errorStr);

Exemplo de Código para Operações com Tabela de Pontos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPointTable(Robot robot)
    {
        String save_path = "D://zDOWN/";
        String point_table_name = "point_table_FR5.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);

        String upload_path = "D://zUP/point_table_FR5.db";
        rtn = robot.PointTableUpLoad(upload_path);

        String point_tablename = "point_table_FR5.db";
        String lua_name = "airlab.lua";
        String err="";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name,err);

        robot.CloseRPC();
        return 0;
    }

Download de Log do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief Download de log do controlador
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    int RbLogDownload(String savePath);

Download de Todas as Fontes de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief Download de todas as fontes de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    int AllDataSourceDownload(String savePath);

Download do Pacote de Backup de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief Download do pacote de backup de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    int DataPackageDownload(String savePath);

Exemplo de Código para Download de Dados do Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestDownLoadRobotData(Robot robot)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");

        rtn = robot.AllDataSourceDownload("D://zDOWN/");

        rtn = robot.DataPackageDownload("D://zDOWN/");
        return 0;
    }

Definir Atualização do Codificador
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define a atualização do codificador
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    int SetEncoderUpgrade(String path)

Definir Atualização de Firmware das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define a atualização de firmware das juntas
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    public int SetJointFirmwareUpgrade(int type, String path)

Definir Atualização de Firmware do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define a atualização de firmware do painel de controle
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    public int SetCtrlFirmwareUpgrade(int type, String path)

Definir Atualização de Firmware da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Define a atualização de firmware da extremidade
    * @param [in] type Tipo de arquivo de atualização; 1-atualizar firmware; 2-atualizar arquivo de configuração do escravo
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    public int SetEndFirmwareUpgrade(int type, String path)

Atualização do Arquivo de Configuração Completa de Parâmetros das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Atualização do arquivo de configuração completa de parâmetros das juntas
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    public int JointAllParamUpgrade(String path)

Exemplo de Código para Atualização de Firmware do Escravo do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFirmWareUpgrade(Robot robot)
    {
        robot.RobotEnable(0);
        robot.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/standardQX/jointallparametersFR56.0.db");
        System.out.println("robot JointAllParamUpgrade rtn is:"+ rtn);

        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade config param rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        System.out.println("robot SetEndFirmwareUpgrade config param rtn is:"+ rtn);

        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/standardQX/FR_CTRL_PRIMCU_FV201010_MAIN_U4_T01_20240529.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/standardQX/FR_END_FV201010_MAIN_U01_T01_20250522.bin");
        System.out.println("robot SetEndFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/standardQX/FR_SERVO_FV502211_MAIN_U7_T07_20250217.bin");
        System.out.println("robot SetJointFirmwareUpgrade rtn is:"+ rtn);

        robot.CloseRPC();
    }

Atualização do Sistema Operacional do Robô (Painel de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Atualização do sistema operacional do robô (Painel de controle LA)
     * @param [in] filePath Caminho completo do pacote de atualização do sistema operacional
     * @return  Código de erro
     */
    public int KernelUpgrade(String filePath)

Obter Resultado da Atualização do Sistema Operacional do Robô (Painel de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém o resultado da atualização do sistema operacional do robô (Painel de controle LA)
     * @param [out] result Resultado da atualização: 0: sucesso; -1: falha
     * @return  Código de erro
     */
    public int GetKernelUpgradeResult(int[] result)

Geração de Log MCU do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Geração de log MCU do robô
    * @return Código de erro
    */
    public int RobotMCULogCollect()

Definir Parada do Robô Quando a Comunicação da Porta é Desconectada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a parada do robô quando a comunicação da porta é desconectada
    * @param portID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param enable 0-desativar; 1-ativar
    * @param confirmTime Duração de confirmação de interrupção da comunicação (ms)[0-5000]
    * @return Código de erro
    */
    public int SetRobotStopOnComDisc(int portID, bool enable, int confirmTime)
    
Obter Parâmetros de Parada do Robô Quando a Comunicação da Porta é Desconectada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros de parada do robô quando a comunicação da porta é desconectada
    * @param portID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param enable Array de resultados, índice 0: 0-desativar; 1-ativar
    * @param confirmTime Array de resultados, índice 0: Duração de confirmação de interrupção da comunicação (ms)[0-5000] 
    * @return Código de erro
    */
    public int GetRobotStopOnComDisc(int portID, int[] enable, int[] confirmTime)

Exemplo de Código para Parâmetros de Parada do Robô Quando a Comunicação da Porta é Desconectada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    void TestRobotStopOnComDisc(Robot robot)
    {
        int[] enable = {0};
        int[] confirmTime = {0};
        int rtn = 0;
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        System.out.printf("SetRobotStopOnComDisc %d\n", rtn);

        robot.GetRobotStopOnComDisc(0, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 8080 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(1, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 8083 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(2, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 20002 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(3, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 20004 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);

        return;
    }

Enviar Quadro de Comando UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Envia quadro de comando UDP
    * @param quadro de comando
    * @return Código de erro
    */
    public int SendUDPFrame(String frame)
    
Exemplo de Código SDK para Comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestRobotUDP (Robot robot) {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Resposta UDP recebida do robô]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("内容 (content): " + content);
            return 0;
        });
        // Enviar quadro
        String frameToSend = "/f/bIII52III236III7IIIMode(1)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII52III236III7IIIMode(0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII41III201III153IIIMoveJ(53.857,-89.441,119.453,-22.664,61.059,3.369,-54.249,-491.930,375.396,96.474,-6.896,-7.783,0,0,100,100,100,0.000,0.000,0.000,0.000,-1,0,0,0,0,0,0,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII42III203III163IIIMoveL(81.736,-85.284,114.974,-23.261,88.746,6.799,125.744,-506.570,375.396,96.474,-6.896,-7.783,0,0,100,100,100,-1,0,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,0,100,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII47III400III15IIIGetMCVersion(1)III/b/f/f/bIII48III424III21IIIGetSlaveFirmVersion()III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
    }
        
Definir Cor do LED da Extremidade do Robô Personalizada pelo Usuário
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a cor do LED da extremidade do robô personalizada pelo usuário
    * @param r Controle do LED vermelho da extremidade; 0-desligado; 1-ligado
    * @param g Controle do LED verde da extremidade; 0-desligado; 1-ligado
    * @param b Controle do LED azul da extremidade; 0-desligado; 1-ligado
    * @return Código de erro
    */
    public int SetUserLEDColor(bool r, bool g, bool b)
            
Exemplo de Código SDK para Definir Cor do LED da Extremidade do Robô Personalizada pelo Usuário
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public void testled(robot)
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