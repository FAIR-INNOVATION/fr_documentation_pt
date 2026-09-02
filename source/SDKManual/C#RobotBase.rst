Fundamentos do Robô
=======================================

.. toctree:: 
    :maxdepth: 5

Instanciar o Robô
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Construtor da classe de interface do robô
    */
    Robot(); 

Estabelecer Comunicação com o Controlador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Estabelecer comunicação com o controlador do robô
    * @param  [in] ip  Endereço IP do controlador, padrão de fábrica é 192.168.58.2
    * @return Código de erro
    */
    int RPC(string ip);

Encerrar Comunicação com o Robô
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Encerrar comunicação com o controlador do robô
    * @return Código de erro
    */ 
    int CloseRPC(); 

Consultar Número da Versão do SDK
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Consultar número da versão do SDK
    * @param [out] version Número da versão do SDK
    * @return Código de erro
    */  
    int GetSDKVersion(ref string version);

Obter IP do Controlador
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter IP do controlador
    * @param  [out] ip  IP do controlador
    * @return  Código de erro
    */
    int GetControllerIP(ref string ip);

Controlar a Entrada ou Saída do Robô no Modo de Ensinamento por Arrasto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Controlar a entrada ou saída do robô no modo de ensinamento por arrasto
    * @param  [in] state 0-sair do modo de ensinamento por arrasto, 1-entrar no modo de ensinamento por arrasto
    * @return  Código de erro
    */
    int DragTeachSwitch(byte state);

Verificar se o Robô Está no Modo de Arrasto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Verificar se o robô está no modo de ensinamento por arrasto
    * @param  [out] state 0-não está no modo de ensinamento por arrasto, 1-está no modo de ensinamento por arrasto
    * @return  Código de erro
    */
    int IsInDragTeach(ref byte state); 

Controlar a Habilitação ou Desabilitação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Controlar a habilitação ou desabilitação do robô. Por padrão, o robô é automaticamente habilitado após a inicialização.
    * @param  [in] state  0-desabilitar, 1-habilitar
    * @return  Código de erro
    */
    int RobotEnable(byte state); 

Controlar a Alternância entre Modo Manual e Automático do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Controlar a alternância entre modo manual e automático do robô
    * @param [in] mode 0-modo automático, 1-modo manual
    * @return Código de erro
    */
    int Mode(int mode);

Desligar o Sistema Operacional do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Desligar o sistema operacional do robô
    * @return Código de erro
    */
    int ShutDownRobotOS();

Exemplo de Código
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        int rtn = robot.ShutDownRobotOS();
        Console.WriteLine($"ShutDownRobotOS rtn is {rtn}");
    }

Definir Parâmetros de Reconexão de Comunicação com o Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir parâmetros de reconexão de comunicação com o robô
    * @param [in] enable Ativar ou não true-ativar, false-desativar
    * @param [in] times Número de tentativas de reconexão
    * @param [in] period Intervalo de tempo entre tentativas de reconexão (milissegundos)
    */
    void SetReconnectParam(bool enable, int times, int period);

Exemplo de Código
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnStandard_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 20000);// Parâmetros de reconexão
        robot.RPC("192.168.58.2"); 

        string ip = "";
        string version = "";
        byte state = 0;

        robot.GetSDKVersion(ref version);
        Console.WriteLine($"SDK version : {version}");
        robot.GetControllerIP(ref ip);
        Console.WriteLine($"controller ip : {ip}");

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        int rtn = robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.DragTeachSwitch(0);
        Thread.Sleep(1000);
        robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.RobotEnable(0);
        Thread.Sleep(3000);
        robot.RobotEnable(1);

        robot.Mode(0);
        Thread.Sleep(1000);
        robot.Mode(1);
        
        rtn = robot.HiSpeedManualSwitch(1);
        Console.WriteLine($"change high speed mode {rtn}");
        Thread.Sleep(10000);

        rtn = robot.HiSpeedManualSwitch(0);
        Console.WriteLine($"change low speed mode {rtn}");
        Thread.Sleep(1000);
    }

Inicializar Parâmetros de Log
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Inicializar parâmetros de log
    * @param [in] logType: Modo de saída, DIRECT-saída direta; BUFFER-saída com buffer; ASYNC-saída assíncrona
    * @param [in] logLevel: Nível de filtragem do log, ERROR-erro; WARNING-aviso; INFO-informação; DEBUG-depuração
    * @param [in] filePath: Caminho para salvar o arquivo, ex: "D://Log/"
    * @param [in] saveFileNum: Número de arquivos a serem salvos. Arquivos que excederem tanto o número de arquivos salvos quanto o número de dias salvos serão excluídos.
    * @param [in] saveDays: Número de dias para salvar os arquivos. Arquivos que excederem tanto o número de arquivos salvos quanto o número de dias salvos serão excluídos.
    * @return Código de erro
    */
    int LoggerInit(FrLogType logType = FrLogType.DIRECT, FrLogLevel logLevel = FrLogLevel.INFO, string filePath = "", int saveFileNum = 10, int saveDays = 10);

Definir Nível de Filtragem do Log
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir nível de filtragem do log
    * @param [in] logLevel: Nível de filtragem do log, ERROR-erro; WARNING-aviso; INFO-informação; DEBUG-depuração
    * @return Código de erro
    */
    int SetLoggerLevel(FrLogLevel logLevel);

Obter Versão do Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter informações da versão do software do robô
    * @param [out] robotModel Modelo do robô
    * @param [out] webVersion Versão web
    * @param [out] controllerVersion Versão do controlador
    * @return Código de erro
    */ 
    int GetSoftwareVersion(ref string robotModel, ref string webVersion, ref string controllerVersion);

Obter Versão do Hardware do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter informações da versão do hardware do robô
    * @param [out] ctrlBoxBoardVersion Versão do hardware da placa base do painel de controle
    * @param [out] driver1Version Versão do hardware do driver 1
    * @param [out] driver2Version Versão do hardware do driver 2
    * @param [out] driver3Version Versão do hardware do driver 3
    * @param [out] driver4Version Versão do hardware do driver 4
    * @param [out] driver5Version Versão do hardware do driver 5
    * @param [out] driver6Version Versão do hardware do driver 6
    * @param [out] endBoardVersion Versão do hardware da placa da extremidade
    * @return Código de erro
    */ 
    int GetHardwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

Obter Versão do Firmware do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter informações da versão do firmware do robô
    * @param [out] ctrlBoxBoardVersion Versão do firmware da placa base do painel de controle
    * @param [out] driver1Version Versão do firmware do driver 1
    * @param [out] driver2Version Versão do firmware do driver 2
    * @param [out] driver3Version Versão do firmware do driver 3
    * @param [out] driver4Version Versão do firmware do driver 4
    * @param [out] driver5Version Versão do firmware do driver 5
    * @param [out] driver6Version Versão do firmware do driver 6
    * @param [out] endBoardVersion Versão do firmware da placa da extremidade
    * @return Código de erro
    */ 
    int GetFirmwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnGetVersions_Click(object sender, EventArgs e)
    {
        string[] ver = new string[20];
        int rtn = 0;
        rtn = robot.GetSoftwareVersion(ref ver[0], ref ver[1], ref ver[2]);
        rtn = robot.GetHardwareVersion(ref ver[3], ref ver[4], ref ver[5], ref ver[6], ref ver[7], ref ver[8], ref ver[9], ref ver[10]);
        rtn = robot.GetFirmwareVersion(ref ver[11], ref ver[12], ref ver[13], ref ver[14], ref ver[15], ref ver[16], ref ver[17], ref ver[18]);
        Console.WriteLine($"robotmodel  is: {ver[0]}");
        Console.WriteLine($"webVersion  is: {ver[1]}");
        Console.WriteLine($"controllerVersion  is: {ver[2]}");
        Console.WriteLine($"Hard ctrlBox Version  is: {ver[3]}");
        Console.WriteLine($"Hard driver1 Version  is: {ver[4]}");
        Console.WriteLine($"Hard driver2 Version  is: {ver[5]}");
        Console.WriteLine($"Hard driver3 Version  is: {ver[6]}");
        Console.WriteLine($"Hard driver4 Version  is: {ver[7]}");
        Console.WriteLine($"Hard driver5 Version  is: {ver[8]}");
        Console.WriteLine($"Hard driver6 Version  is: {ver[9]}");
        Console.WriteLine($"Hard end Version  is: {ver[10]}");
        Console.WriteLine($"Firm ctrlBox Version  is: {ver[11]}");
        Console.WriteLine($"Firm driver1 Version  is: {ver[12]}");
        Console.WriteLine($"Firm driver2 Version  is: {ver[13]}");
        Console.WriteLine($"Firm driver3 Version  is: {ver[14]}");
        Console.WriteLine($"Firm driver4 Version  is: {ver[15]}");
        Console.WriteLine($"Firm driver5 Version  is: {ver[16]}");
        Console.WriteLine($"Firm driver6 Version  is: {ver[17]}");
        Console.WriteLine($"Firm end Version  is: {ver[18]}");
    }

Alternar para o Modo Manual de Alta Velocidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Alternar para o modo manual de alta velocidade
    * @param [in] state 0-sair do modo manual de alta velocidade; 1-entrar no modo manual de alta velocidade
    * @return Código de erro
    */
    public int HiSpeedManualSwitch(int state)    