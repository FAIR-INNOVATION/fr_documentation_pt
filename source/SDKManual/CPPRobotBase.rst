Fundamentos do Robô
===========================

.. toctree::
    :maxdepth: 5

Instanciar o Robô
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Construtor da classe de interface do robô
    */
    FRRobot();

Estabelecer Comunicação com o Controlador
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Estabelece comunicação com o controlador do robô
    * @param [in] ip Endereço IP do controlador, padrão de fábrica é 192.168.58.2
    * @return Código de erro
    */
    errno_t RPC(const char *ip);

Encerrar Comunicação com o Controlador
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Encerra a comunicação com o controlador do robô
     * @return Código de erro
     */
    errno_t CloseRPC();

Consultar Número da Versão do SDK
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Consulta o número da versão do SDK
    * @param [out] version Número da versão do SDK
    * @return Código de erro
    */
    errno_t GetSDKVersion(char *version);

Obter IP do Controlador
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o IP do controlador
    * @param [out] ip IP do controlador
    * @return Código de erro
    */
    errno_t GetControllerIP(char *ip);

Controlar a Entrada ou Saída do Modo de Ensino por Arrasto do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Controla a entrada ou saída do modo de ensino por arrasto do robô
    * @param [in] state 0-sair do modo de ensino por arrasto, 1-entrar no modo de ensino por arrasto
    * @return Código de erro
    */
    errno_t DragTeachSwitch(uint8_t state);

Verificar se o Robô está em Modo de Arrasto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Verifica se o robô está em modo de ensino por arrasto
    * @param [out] state 0-não está em modo de ensino por arrasto, 1-está em modo de ensino por arrasto
    * @return Código de erro
    */
    errno_t IsInDragTeach(uint8_t *state);

Controlar a Habilitação ou Desabilitação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Controla a habilitação ou desabilitação do robô. Após ligar, o robô é habilitado automaticamente por padrão
    * @param [in] state 0-desabilitar, 1-habilitar
    * @return Código de erro
    */
    errno_t RobotEnable(uint8_t state);

Controlar a Comutação entre Modo Manual e Automático do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Controla a comutação entre modo manual e automático do robô
    * @param [in] mode 0-modo automático, 1-modo manual
    * @return Código de erro
    */
    errno_t Mode(int mode);

Desligar o Sistema Operacional do Robô
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Desliga o sistema operacional do robô
    * @return Código de erro
    */
    errno_t ShutDownRobotOS();

Definir Parâmetros de Reconexão de Comunicação com o Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros de reconexão de comunicação com o robô
    * @param [in] enable Habilita a reconexão em caso de falha de rede true-habilitar false-desabilitar
    * @param [in] reconnectTime Tempo de reconexão, em ms
    * @param [in] period Período de reconexão, em ms
    * @return Código de erro
    */
    errno_t SetReConnectParam(bool enable, int reconnectTime = 30000, int period = 50);

Desligar o Sistema Operacional do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Desliga o sistema operacional do robô
    * @return Código de erro
    */
    int ShutDownRobotOS();

Inicializar Parâmetros de Log
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Inicializa os parâmetros de log;
    * @param output_model: Modo de saída, 0-saída direta; 1-saída com buffer; 2-saída assíncrona;
    * @param file_path: Caminho + nome do arquivo de salvamento, limite de comprimento 256, o nome deve estar no formato xxx.log, ex: /home/fr/linux/fairino.log;
    * @param file_num: Número de arquivos armazenados em rotação, 1~20. Limite máximo de 50 MB por arquivo;
    * @return errno_t Código de erro;
    */
    errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

Definir Nível de Filtro de Log
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o nível de filtro de log;
    * @param lvl: Nível de filtro, quanto menor o valor, menos logs são exibidos. O valor padrão é 1. 1-erro, 2-aviso, 3-informação, 4-depuração;
    */
    void SetLoggerLevel(int lvl = 1);

Exemplo de Código de Controle Básico do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestRobotCtrl(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 30000, 500);
        int rtn = robot.RPC("192.168.57.2");
        
        char ip[64] = "";
        char version[64] = "";
        uint8_t state;
        robot.GetSDKVersion(version);
        printf("SDK version:%s\n", version);
        robot.GetControllerIP(ip);
        printf("controller ip:%s\n", ip);
        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.Sleep(1000);
        robot.IsInDragTeach(&state);
        printf("drag state :%u\n", state);
        robot.Sleep(3000);
        robot.DragTeachSwitch(0);
        robot.Sleep(1000);
        robot.IsInDragTeach(&state);
        printf("drag state :%u\n", state);
        robot.Sleep(3000);
        robot.RobotEnable(0);
        robot.Sleep(3000);
        robot.RobotEnable(1);
        robot.Mode(0);
        robot.Sleep(2000);
        robot.Mode(1);
        robot.Sleep(1000);
        rtn = robot.HiSpeedManualSwitch(1);
        printf("change high speed mode %d\n", rtn);
        robot.Sleep(3000);
        rtn = robot.HiSpeedManualSwitch(0);
        printf("change low speed mode %d\n", rtn);
        robot.Sleep(3000);
        robot.ShutDownRobotOS();
        robot.CloseRPC();
        return 0;
    }

Exemplo de Código para Obter Versão do Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a versão do software do robô
    * @param[out] robotModel Modelo do robô
    * @param[out] webVersion Versão web
    * @param[out] controllerVersion Versão do controlador
    * @return Código de erro
    */
    errno_t GetSoftwareVersion(char robotModel[64], char webVersion[64], char controllerVersion[64]);

Obter Versão do Hardware do Robô
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a versão do hardware do robô
    * @param[out] ctrlBoxBoardversion Versão do hardware da placa base da caixa de controle
    * @param[out] driver1version Versão do hardware do driver 1
    * @param[out] driver2version Versão do hardware do driver 2
    * @param[out] driver3version Versão do hardware do driver 3
    * @param[out] driver4version Versão do hardware do driver 4
    * @param[out] driver5version Versão do hardware do driver 5
    * @param[out] driver6version Versão do hardware do driver 6
    * @param[out] endBoardversion Versão do hardware da placa da extremidade
    */
    errno_t GetHardwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

Obter Versão do Firmware do Robô
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a versão do firmware do robô
    * @param[out] ctrlBoxBoardversion Versão do firmware da placa base da caixa de controle
    * @param[out] driver1version Versão do firmware do driver 1
    * @param[out] driver2version Versão do firmware do driver 2
    * @param[out] driver3version Versão do firmware do driver 3
    * @param[out] driver4version Versão do firmware do driver 4
    * @param[out] driver5version Versão do firmware do driver 5
    * @param[out] driver6version Versão do firmware do driver 6
    * @param[out] endBoardversion Versão do firmware da placa da extremidade
    */
    errno_t GetFirmwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

Exemplo de Código para Obter Versões de Software e Firmware do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGetVersions(void)
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
         char robotModel[64] = { 0 };
         char webversion[64] = { 0 };
         char controllerVersion[64] = { 0 };
         char ctrlBoxBoardversion[128] = { 0 };
         char driver1version[128] = { 0 };
         char driver2version[128] = { 0 };
         char driver3version[128] = { 0 };
         char driver4version[128] = { 0 };
         char driver5version[128] = { 0 };
         char driver6version[128] = { 0 };
         char endBoardversion[128] = { 0 };
         rtn = robot.GetSoftwareVersion(robotModel, webversion, controllerVersion);
         printf("Getsoftwareversion rtn is: %d\n", rtn);
         printf("robotmodel is: %s, webversion is: %s, controllerVersion is: %s \n\n", robotModel, webversion, controllerVersion);
         rtn = robot.GetHardwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetHardwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         rtn = robot.GetFirmwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetFirmwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         robot.CloseRPC();
         return 0;
     }