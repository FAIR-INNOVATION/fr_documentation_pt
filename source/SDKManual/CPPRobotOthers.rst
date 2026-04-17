Outras Interfaces
=====================

.. toctree::
    :maxdepth: 5

Obter Chave Pública SSH
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a chave pública SSH
    * @param [out] keygen Chave pública
    * @return Código de erro
    */
    errno_t GetSSHKeygen(char keygen[1024]);

Enviar Comando SCP
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Envia comando SCP
    * @param [in] mode 0-envio (computador host -> controlador), 1-download (controlador -> computador host)
    * @param [in] sshname Nome de usuário do computador host
    * @param [in] sship Endereço IP do computador host
    * @param [in] usr_file_url Caminho do arquivo no computador host
    * @param [in] robot_file_url Caminho do arquivo no controlador do robô
    * @return Código de erro
    */
    errno_t SetSSHScpCmd(int mode, char sshname[32], char sship[32], char usr_file_url[128], char robot_file_url[128]);

Calcular o Valor MD5 de um Arquivo em um Caminho Especificado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Calcula o valor MD5 de um arquivo em um caminho especificado
    * @param [in] file_path Caminho do arquivo incluindo o nome do arquivo, o caminho padrão da pasta Traj é: "/fruser/traj/", ex: "/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 Valor MD5 do arquivo
    * @return Código de erro
    */
    errno_t ComputeFileMD5(char file_path[256], char md5[256]);

Exemplo de Código de Comandos SSH e MD5 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSSHMd5(void)
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
      char file_path[256] = "/fruser/airlab.lua";
      char md5[256] = { 0 };
      uint8_t emerg_state = 0;
      uint8_t si0_state = 0;
      uint8_t si1_state = 0;
      int sdk_com_state = 0;
      char ssh_keygen[1024] = { 0 };
      int retval = robot.GetSSHKeygen(ssh_keygen);
      printf("GetSSHKeygen retval is: %d\n", retval);
      printf("ssh key is: %s \n", ssh_keygen);
      char ssh_name[32] = "fr";
      char ssh_ip[32] = "192.168.58.45";
      char ssh_route[128] = "/home/fr";
      char ssh_robot_url[128] = "/root/robot/dhpara.config";
      retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
      printf("SetSSHScpCmd retval is: %d\n", retval);
      printf("robot url is: %s\n", ssh_robot_url);
      robot.ComputeFileMD5(file_path, md5);
      printf("md5 is: %s \n", md5);
      robot.CloseRPC();
      return 0;
    }

Definir Período de Feedback da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o período de feedback da porta 20004 do robô
    * @param [in] period Período de feedback da porta 20004 do robô (ms)
    * @return Código de erro
    */
    errno_t SetRobotRealtimeStateSamplePeriod(int period);

Obter Período de Feedback da Porta 20004 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o período de feedback da porta 20004 do robô
    * @param [out] period Período de feedback da porta 20004 do robô (ms)
    * @return Código de erro
    */
    errno_t GetRobotRealtimeStateSamplePeriod(int& period);

Exemplo de Código de Configuração do Período de Feedback de Estado da Porta 20004 do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestRealtimePeriod(void)
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
      robot.SetRobotRealtimeStateSamplePeriod(10);
      int getPeriod = 0;
      robot.GetRobotRealtimeStateSamplePeriod(getPeriod);
      cout << "period is " << getPeriod << endl;
      robot.Sleep(1000);
      robot.CloseRPC();
      return 0;
    }

Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Atualização de software do robô
    * @param [in] filePath Caminho completo do pacote de atualização de software
    * @param [in] block Se bloqueia até a conclusão da atualização true: bloqueante; false: não bloqueante
    * @return Código de erro
    */
    errno_t SoftwareUpgrade(std::string filePath, bool block);

Obter Estado da Atualização de Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado da atualização de software do robô
    * @param [out] state Estado da atualização do pacote de software do robô (0-ocioso ou enviando pacote de atualização; 1~100: porcentagem de conclusão da atualização; -1: falha na atualização do software; -2: falha na verificação; -3: falha na verificação da versão; -4: falha na descompactação; -5: falha na atualização da configuração do usuário; -6: falha na atualização da configuração do periférico; -7: falha na atualização da configuração do eixo estendido; -8: falha na atualização da configuração do robô; -9: falha na atualização da configuração dos parâmetros DH)
    * @return Código de erro
    */
    errno_t GetSoftwareUpgradeState(int &state);

Exemplo de Código de Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUpgrade(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(3);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SoftwareUpgrade("D://zUP/QNX/software.tar.gz", false);
      while (true)
      {
        int curState = -1;
        robot.GetSoftwareUpgradeState(curState);
        printf("upgrade state is %d\n", curState);
        robot.Sleep(300);
      }
      robot.CloseRPC();
      return 0;
    }

Download do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Download do banco de dados da tabela de pontos
    * @param [in] pointTableName Nome da tabela de pontos a ser baixada    pointTable1.db
    * @param [in] saveFilePath Caminho de armazenamento para download da tabela de pontos   C://test/
    * @return Código de erro
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

Upload do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Upload do banco de dados da tabela de pontos
    * @param [in] pointTableFilePath Caminho completo do arquivo da tabela de pontos para upload   C://test/pointTable1.db
    * @return Código de erro
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

Atualização do Arquivo Lua da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Atualização do arquivo Lua da tabela de pontos
    * @param [in] pointTableName Nome da tabela de pontos a ser alternada   "pointTable1.db", quando a tabela de pontos estiver vazia, ou seja "", indica que o programa Lua será atualizado para o programa inicial sem aplicação da tabela de pontos
    * @param [in] luaFileName Nome do arquivo Lua a ser atualizado   "testPointTable.lua"
    * @param [out] errorStr Mensagem de erro da alternância da tabela de pontos
    * @return Código de erro
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

Exemplo de Código de Operação da Tabela de Pontos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestPointTable(void)
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
      string save_path = "D://zDOWN/";
      string point_table_name = "point_table_FR5.db";
      rtn = robot.PointTableDownLoad(point_table_name, save_path);
      cout << "download : " << point_table_name << " fail: " << rtn << endl;
      string upload_path = "D://zUP/point_table_FR5.db";
      rtn = robot.PointTableUpLoad(upload_path);
      cout << "retval is: " << rtn << endl;
      string point_tablename = "point_table_FR5.db";
      string lua_name = "airlab.lua";
      rtn = robot.PointTableUpdateLua(point_tablename, lua_name);
      cout << "retval is: " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

Download de Logs do Controlador
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Download de logs do controlador
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    errno_t RbLogDownload(std::string savePath);

Download de Todas as Fontes de Dados
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Download de todas as fontes de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    errno_t AllDataSourceDownload(std::string savePath);

Download do Pacote de Backup de Dados
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Download do pacote de backup de dados
    * @param [in] savePath Caminho para salvar o arquivo "D://zDown/"
    * @return Código de erro
    */
    errno_t DataPackageDownload(std::string savePath);

Exemplo de Código de Download de Dados do Controlador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestDownLoadRobotData(void)
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
      rtn = robot.RbLogDownload("D://zDOWN/");
      cout << "RbLogDownload rtn is " << rtn << endl;
      rtn = robot.AllDataSourceDownload("D://zDOWN/");
      cout << "AllDataSourceDownload rtn is " << rtn << endl;
      rtn = robot.DataPackageDownload("D://zDOWN/");
      cout << "DataPackageDownload rtn is " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

Definir Atualização de Firmware das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a atualização de firmware das juntas
    * @param [in] type Tipo de arquivo de atualização; 1-atualização de firmware (necessário colocar o robô em modo boot antes do uso); 2-atualização do arquivo de configuração do escravo (necessário desabilitar o robô antes do uso)
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    errno_t SetJointFirmwareUpgrade(int type, std::string path);

Definir Atualização de Firmware da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a atualização de firmware da caixa de controle
    * @param [in] type Tipo de arquivo de atualização; 1-atualização de firmware (necessário colocar o robô em modo boot antes do uso); 2-atualização do arquivo de configuração do escravo (necessário desabilitar o robô antes do uso)
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    errno_t SetCtrlFirmwareUpgrade(int type, std::string path);

Definir Atualização de Firmware da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a atualização de firmware da extremidade
    * @param [in] type Tipo de arquivo de atualização; 1-atualização de firmware (necessário colocar o robô em modo boot antes do uso); 2-atualização do arquivo de configuração do escravo (necessário desabilitar o robô antes do uso)
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    errno_t SetEndFirmwareUpgrade(int type, std::string path);

Atualização do Arquivo de Configuração de Parâmetros Completos das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Atualização do arquivo de configuração de parâmetros completos das juntas (necessário desabilitar o robô antes do uso)
    * @param [in] path Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)
    * @return Código de erro
    */
    errno_t JointAllParamUpgrade(std::string path);

Exemplo de Código de Atualização de Firmware dos Escravos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestFirmWareUpgrade()
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
    robot.RobotEnable(0);
    robot.Sleep(200);
    rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/jointallparameters.db");
    printf("robot JointAllParamUpgrade rtn is %d\n", rtn);
    rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
    printf("robot SetCtrlFirmwareUpgrade config param rtn is %d\n", rtn);
    rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
    printf("robot SetEndFirmwareUpgrade config param rtn is %d\n", rtn);
    robot.SetSysServoBootMode();
    rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/upgrade/FR_CTRL_PRIMCU_FV201212_MAIN_U4_T01_20250428(MT).bin");
    printf("robot SetCtrlFirmwareUpgrade rtn is %d\n", rtn);
    rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/upgrade/FR_END_FV201009_MAIN_U1_T01_20250428.bin");
    printf("robot SetEndFirmwareUpgrade rtn is %d\n", rtn);
    rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/upgrade/FR_SERVO_FV504214_MAIN_U7_T07_20250519.bin");
    printf("robot SetJointFirmwareUpgrade rtn is %d\n", rtn);
    robot.CloseRPC();
    return 0;
    }

Atualização do Sistema Operacional do Robô (Caixa de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Atualização do sistema operacional do robô (caixa de controle LA)
    * @param [in] filePath Caminho completo do pacote de atualização do sistema operacional
    * @return Código de erro
    */
    errno_t KernelUpgrade(std::string filePath);

Obter Resultado da Atualização do Sistema Operacional do Robô (Caixa de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o resultado da atualização do sistema operacional do robô (caixa de controle LA)
    * @param [out] result Resultado da atualização: 0: sucesso; -1: falha
    * @return Código de erro
    */
    errno_t GetKernelUpgradeResult(int& result);

Geração de Logs MCU do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Geração de logs MCU do robô
    * @return Código de erro
    */
    errno_t RobotMCULogCollect();

Definir Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a parada da operação do robô quando a comunicação da porta for desconectada
    * @param [in] pordID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param [in] enable 0-desativar; 1-ativar
    * @param [in] confirmTime Duração de confirmação da interrupção da comunicação (ms)[0-5000]
    * @return Código de erro
    */
    errno_t SetRobotStopOnComDisc(int pordID, bool enable, int confirmTime);

Obter Parâmetros de Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os parâmetros de parada da operação do robô quando a comunicação da porta for desconectada
    * @param [in] pordID Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    * @param [out] enable 0-desativar; 1-ativar
    * @param [out] confirmTime Duração de confirmação da interrupção da comunicação (ms)[0-5000]
    * @return Código de erro
    */
    errno_t GetRobotStopOnComDisc(int pordID, bool &enable, int &confirmTime);

Exemplo de Código de Parâmetros de Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestRobotStopOnComDisc()
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
        bool enable = false;
        int confirmTime = 0;
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        printf("SetRobotStopOnComDisc %d\n", rtn);
        robot.GetRobotStopOnComDisc(0, enable, confirmTime);
        printf("GetRobotStopOnComDisc 8080 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(1, enable, confirmTime);
        printf("GetRobotStopOnComDisc 80803 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(2, enable, confirmTime);
        printf("GetRobotStopOnComDisc 20002 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(3, enable, confirmTime);
        printf("GetRobotStopOnComDisc 20004 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

Envio de Quadro de Comando via UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Envio de quadro de comando via UDP
    * @param [in] frame String do quadro de dados a ser enviado, ex: /f/bIII20III303III7IIIMode(0)III/b/f
    * @return Código de erro
    */
    errno_t SendUDPFrame(std::string frame);

Definir Função de Retorno de Chamada do Resultado da Execução do Comando Enviado pelo SDK via UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a função de retorno de chamada do resultado da execução do comando enviado pelo SDK via UDP
    * @param [in] CallBack Função de retorno de chamada; comType-Tipo de resposta de comunicação do resultado do comando 0-TCP, 1-UDP; count-Contagem do quadro de resposta do comando; cmdID-Número do comando; contentLen-Comprimento dos dados; content-Conteúdo dos dados
    * @return Código de erro
    */
    errno_t SetCmdRpyCallback(void (*CallBack)(int comType, int count, int cmdID, int contentLen, std::string content));

Exemplo de Código de Envio de Comando via UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSendUDPFrame()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.SetCmdRpyCallback(UDPFrameCallBack);
        printf("SetCmdRpyCallback rtn is %d\n", rtn);
        rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame Mode(0) rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII21III303III7IIIMode(1)III/b/f");
        printf("SendUDPFrame Mode(1) rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII49III201III184IIIMoveJ(-15.625, -82.680, 101.654, -110.950, -88.290, 0.017, -383.012, -2.325, 242.655, -178.024, 1.710, 74.416, 0, 0, 100, 100, 100, 0.000, 0.000, 0.000, 0.000, -1, 0, 0, 0, 0, 0, 0, 0)III/b/f");
        printf("SendUDPFrame MoveJ(-15.625 rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII48III203III199IIIMoveL(-75.622, -82.680, 101.654, -110.950, -88.290, 0.017, -193.537, 330.525, 242.657, -178.024, 1.710, 14.420, 0, 0, 100, 100, 100, -1, 0, 0.000, 0.000, 0.000, 0.000, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0)III/b/f");
        printf("SendUDPFrame MoveL(-75.622 rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII4III905III20IIIGetSoftwareVersion()III/b/f");
        printf("SendUDPFrame GetSoftwareVersion() rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("III20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bIII20III303III6IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/b|||20|||303|||7|||Mode(0)|||/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bII20II303II7IIMode(0)II/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

Definir Cor da Luz da Extremidade do Robô Personalizada pelo Usuário
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a cor da luz da extremidade do robô personalizada pelo usuário
    * @param [in] r Controle da luz vermelha da extremidade; 0-apagada; 1-acesa
    * @param [in] g Controle da luz verde da extremidade; 0-apagada; 1-acesa
    * @param [in] b Controle da luz azul da extremidade; 0-apagada; 1-acesa
    * @return Código de erro
    */
    errno_t SetUserLEDColor(bool r, bool g, bool b);

Exemplo de Código para Definir Cor da Luz da Extremidade do Robô Personalizada pelo Usuário
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUserLedColor()
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
        robot.SetUserLEDColor(true, true, true);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(true, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, true, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, true);
        robot.Sleep(1000);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }