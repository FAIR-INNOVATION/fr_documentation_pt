Fundamentos do Robô
==========================

.. toctree:: 
    :maxdepth: 5

Instanciar o Robô
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Construtor da classe de interface do robô
    */
    Robot robot = new Robot(); 

Estabelecer Comunicação com o Controlador
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Estabelece comunicação com o controlador do robô
    * @param  [in] ip  Endereço IP do controlador, padrão de fábrica é 192.168.58.2
    * @return Código de erro
    */
    int RPC(String ip);

Encerrar Comunicação com o Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Encerra a comunicação com o robô
    * @return Código de erro 
    */ 
    int CloseRPC(); 

Consultar Número da Versão do SDK
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Consulta o número da versão do SDK 
    * @return Número da versão 
    */  
    String GetSDKVersion();

Obter IP do Controlador
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o IP do controlador
    * @param  [out] ip  IP do controlador
    * @return  Código de erro
    */
    int GetControllerIP(String[] ip);

Controlar a Entrada ou Saída do Modo de Arrastagem de Ensino do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Controla a entrada ou saída do modo de arrastagem de ensino do robô
    * @param  [in] state 0-sair do modo de arrastagem de ensino, 1-entrar no modo de arrastagem de ensino
    * @return  Código de erro
    */
    int DragTeachSwitch(int state);

Consultar se o Robô Está no Modo de Arrastagem de Ensino
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Consulta se o robô está no modo de arrastagem de ensino
    * @param  [in] state 0-não está no modo de arrastagem de ensino, 1-está no modo de arrastagem de ensino
    * @return  Código de erro
    */
    int IsInDragTeach(List<Number> state);

Controlar a Habilitação ou Desabilitação do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Controla a habilitação ou desabilitação do robô. O robô é automaticamente habilitado após a inicialização por padrão.
    * @param  [in] state  0-desabilitar, 1-habilitar
    * @return  Código de erro
    */
    int RobotEnable(int state); 

Controlar a Alternância entre Modo Manual e Automático do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Controla a alternância entre modo manual e automático do robô
    * @param [in] mode 0-modo automático, 1-modo manual
    * @return Código de erro
    */
    int Mode(int mode);

Desligar o Sistema Operacional do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief Desliga o sistema operacional do robô
    * @return Código de erro
    */
    int ShutDownRobotOS();

Definir Parâmetros de Reconexão com o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros de reconexão com o robô
    * @param [in] enable Se habilita, true: habilitar, false: desabilitar
    * @param [in] times Número de tentativas de reconexão
    * @param [in] period Intervalo de tempo entre tentativas de reconexão
    * @return Código de erro
    */
    int SetReconnectParam(boolean enable, int times, int period);

Inicializar Parâmetros de Log
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Inicializa os parâmetros de log
    * @param [in] logType Modo de saída, DIRETO - saída direta; BUFFER - saída com buffer; ASSÍNCRONO - saída assíncrona
    * @param [in] logLevel Nível de filtro de log, ERRO - erro; AVISO - aviso; INFO - informação; DEBUG - depuração
    * @param [in] filePath Caminho para salvar o arquivo, ex: "D://Log/"
    * @param [in] saveFileNum Número de arquivos a serem salvos. Arquivos que excederem tanto o número de arquivos salvos quanto os dias de salvamento serão excluídos.
    * @param [in] saveDays Número de dias para salvar os arquivos. Arquivos que excederem tanto o número de arquivos salvos quanto os dias de salvamento serão excluídos.
    * @return Código de erro
    */
    int LoggerInit(FrLogType logType, FrLogLevel logLevel, String filePath, int saveFileNum, int saveDays)

Definir Nível de Filtro de Log
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o nível de filtro de log
    * @param [in] logLevel Nível de filtro de log, ERRO - erro; AVISO - aviso; INFO - informação; DEBUG - depuração
    * @return Código de erro
    */
    int SetLoggerLevel(FrLogLevel logLevel)

Exemplo de Código de Controle Básico do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("Conexão RPC bem-sucedida");
        }
        else
        {
            System.out.println("Falha na conexão RPC");
            return ;
        }
        String[] ip={""};
        String version = "";
        version=robot.GetSDKVersion();
        System.out.println("Versão do SDK : " + version);
        int rtn = robot.GetControllerIP(ip);
        System.out.println("IP do controlador : " +  ip[0] + "  " + rtn);
        robot.Mode(1);//1-modo manual  0-modo automático
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);//Entrar no modo de arrastagem
        robot.Sleep(1000);
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("Estado da arrastagem : " + pkg.robot_state);
        robot.Sleep(1000);
        robot.DragTeachSwitch(0);//Sair do modo de arrastagem
        robot.Sleep(1000);
        pkg = robot.GetRobotRealTimeState();
        System.out.println("Estado da arrastagem : " + pkg.robot_state);
        
        if (pkg.robot_state ==4){
           System.out.println("Modo de arrastagem");
        }else {
           System.out.println("Modo não-arrastagem");
        }
    }

Obter Versão do Software do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a versão do software do robô
    * @param [out] robotModel Modelo do robô
    * @param [out] webVersion Versão do web
    * @param [out] controllerVersion Versão do controlador
    * @return Código de erro 
    */
    int GetSoftwareVersion(String robotModel, String webVersion, String controllerVersion);

Obter Versão do Hardware do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a versão do hardware do robô
    * @param [out] ctrlBoxBoardVersion Versão do hardware da placa-mãe do painel de controle
    * @param [out] driver1Version Versão do hardware do driver 1
    * @param [out] driver1Version Versão do hardware do driver 2
    * @param [out] driver1Version Versão do hardware do driver 3
    * @param [out] driver1Version Versão do hardware do driver 4
    * @param [out] driver1Version Versão do hardware do driver 5
    * @param [out] driver1Version Versão do hardware do driver 6
    * @param [out] endBoardVersion Versão do hardware da placa de extremidade
    * @return Código de erro 
    */
    int GetHardwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

Obter Versão do Firmware do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a versão do firmware do robô
    * @param [out] ctrlBoxBoardVersion Versão do firmware da placa-mãe do painel de controle
    * @param [out] driver1Version Versão do firmware do driver 1
    * @param [out] driver1Version Versão do firmware do driver 2
    * @param [out] driver1Version Versão do firmware do driver 3
    * @param [out] driver1Version Versão do firmware do driver 4
    * @param [out] driver1Version Versão do firmware do driver 5
    * @param [out] driver1Version Versão do firmware do driver 6
    * @param [out] endBoardVersion Versão do firmware da placa de extremidade
    * @return Código de erro 
    */
    int GetFirmwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

Exemplo de Código para Obter Versões de Software e Firmware do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//Definir número de tentativas de reconexão, intervalo
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("Conexão RPC bem-sucedida");
        }
        else
        {
            System.out.println("Falha na conexão RPC");
            return ;
        }
        String ctrlBoxBoardVersion = "";
        String driver1Version = "";
        String driver2Version = "";
        String driver3Version = "";
        String driver4Version = "";
        String driver5Version = "";
        String driver6Version = "";
        String endBoardVersion = "";
        robot.GetHardwareVersion(ctrlBoxBoardVersion ,driver1Version,  driver2Version,  driver3Version,
                 driver4Version,  driver5Version,  driver6Version,  endBoardVersion);

        robot.GetFirmwareVersion(ctrlBoxBoardVersion, driver1Version, driver2Version, driver3Version,
                driver4Version, driver5Version, driver6Version, endBoardVersion);
    }