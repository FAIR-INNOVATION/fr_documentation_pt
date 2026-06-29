E/S do Robô
============

.. toctree::
    :maxdepth: 5

Definir Saída Digital da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a saída digital da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in] status 0-desligado, 1-ligado
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    errno_t  SetDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

Definir Saída Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a saída digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] status 0-desligado, 1-ligado
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    errno_t  SetToolDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

Definir Saída Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a saída analógica da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] value  Percentagem do valor de corrente ou tensão, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    errno_t  SetAO(int id, float value, uint8_t block);

Definir Saída Analógica da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define a saída analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in] value  Percentagem do valor de corrente ou tensão, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    errno_t  SetToolAO(int id, float value, uint8_t block);

Exemplo de Código para Configurar Saídas Digitais e Analógicas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestAODO(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 1;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         status = 0;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetToolAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         robot.CloseRPC();
         return 0;
     }

Obter Entrada Digital da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a entrada digital da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  0-nível baixo, 1-nível alto
    * @return  Código de erro
    */
    errno_t  GetDI(int id, uint8_t block, uint8_t *result);

Obter Entrada Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a entrada digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  0-nível baixo, 1-nível alto
    * @return  Código de erro
    */
    errno_t  GetToolDI(int id, uint8_t block, uint8_t *result);

Obter Entrada Analógica da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a entrada analógica da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */
    errno_t  GetAI(int id, uint8_t block, float *result);

Obter Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém a entrada analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */
    errno_t  GetToolAI(int id, uint8_t block, float *result);

Obter Estado do Botão de Gravação de Ponto da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém o estado do botão de gravação de ponto da extremidade do robô
     * @param [out] state Estado do botão, 0-pressionado, 1-solto
     * @return Código de erro
     */
    errno_t  GetAxlePointRecordBtnState(uint8_t *state);

Obter Estado de Saída DO da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém o estado de saída DO da extremidade do robô
     * @param [out] do_state Estado de saída DO, do0~do1 correspondem aos bits 1~2, começando no bit 0
     * @return Código de erro
     */
    errno_t  GetToolDO(uint8_t *do_state);

Obter Estado de Saída DO do Controlador do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém o estado de saída DO do controlador do robô
     * @param [out] do_state_h Estado de saída DO, co0~co7 correspondem aos bits 0~7
     * @param [out] do_state_l Estado de saída DO, do0~do7 correspondem aos bits 0~7
     * @return Código de erro
     */
    errno_t  GetDO(uint8_t *do_state_h, uint8_t *do_state_l);

Exemplo de Código para Obter Estado DI e DO do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestGetDIAI(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         robot.GetDI(0, block, &di);
         printf("di0:%u\n", di);
         tool_di = robot.GetToolDI(1, block, &tool_di);
         printf("tool_di1:%u\n", tool_di);
         robot.GetAI(0, block, &ai);
         printf("ai0:%f\n", ai);
         tool_ai = robot.GetToolAI(0, block, &tool_ai);
         printf("tool_ai0:%f\n", tool_ai);
         uint8_t _button_state = 0;
         robot.GetAxlePointRecordBtnState(&_button_state);
         printf("_button_state is: %u\n", _button_state);
         uint8_t tool_do_state = 0;
         robot.GetToolDO(&tool_do_state);
         printf("tool DO state is: %u\n", tool_do_state);
         uint8_t do_state_h = 0;
         uint8_t do_state_l = 0;
         robot.GetDO(&do_state_h, &do_state_l);
         printf("DO state high is: %u \n DO state low is: %u\n", do_state_h, do_state_l);
         robot.CloseRPC();
         return 0;
     }

Aguardar Entrada Digital da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada digital da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, em ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente
    * @return  Código de erro
    */
    errno_t  WaitDI(int id, uint8_t status, int max_time, int opt);

Aguardar Entrada Digital Múltipla da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada digital múltipla da caixa de controle
    * @param  [in] mode 0-E lógico múltiplo, 1-OU lógico múltiplo
    * @param  [in] id  Número da E/S, bits 0~7 correspondem a DI0~DI7, bits 8~15 correspondem a CI0~CI7
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, em ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente
    * @return  Código de erro
    */
    errno_t  WaitMultiDI(int mode, int id, uint8_t status, int max_time, int opt);

Aguardar Entrada Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, em ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente
    * @return  Código de erro
    */
    errno_t  WaitToolDI(int id, uint8_t status, int max_time, int opt);

Aguardar Entrada Analógica da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada analógica da caixa de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value  Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, em ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente
    * @return  Código de erro
    */
    errno_t  WaitAI(int id, int sign, float value, int max_time, int opt);

Aguardar Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value  Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, em ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente
    * @return  Código de erro
    */
    errno_t  WaitToolAI(int id, int sign, float value, int max_time, int opt);

Exemplo de Código para Aguardar Sinais de Entrada Digital e Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

     int TestWaitDIAI(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         rtn = robot.WaitDI(0, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitMultiDI(1, 3, 3, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolDI(1, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

Definir se a Saída DO da Caixa de Controle é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída DO da caixa de controle é reiniciada após parada/pausa
    * @param [in] resetFlag 0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    errno_t SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag = 0);

Definir se a Saída AO da Caixa de Controle é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída AO da caixa de controle é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    errno_t SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag = 0);

Definir se a Saída DO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída DO da ferramenta de extremidade é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    errno_t SetOutputResetAxleDO(int resetFlag, int reloadFlag = 0);

Definir se a Saída AO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída AO da ferramenta de extremidade é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return  Código de erro
    */
    errno_t SetOutputResetAxleAO(int resetFlag, int reloadFlag = 0);

Definir se a Saída DO Estendida é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída DO estendida é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return  Código de erro
    */
    errno_t SetOutputResetExtDO(int resetFlag, int reloadFlag = 0);

Definir se a Saída AO Estendida é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída AO estendida é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return  Código de erro
    */
    errno_t SetOutputResetExtAO(int resetFlag, int reloadFlag = 0);

Definir se a Saída DO do SmartTool é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define se a saída DO do SmartTool é reiniciada após parada/pausa
    * @param [in] resetFlag  0-não reiniciar; 1-reiniciar
    * @param [in] reloadFlag Se recarregar após retomar da pausa, 0-não carregar; 1-carregar
    * @return  Código de erro
    */
    errno_t SetOutputResetSmartToolDO(int resetFlag, int reloadFlag = 0);

Exemplo de Código para Reinicialização de Saída Após Parada/Pausa do Programa LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    int TestDOReset(void)
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
    for (int i = 0; i < 16; i++)
    {
        robot.SetDO(i, 1, 0, 0);
        robot.Sleep(200);
    }
    int resetFlag = 0;
    int resumeReloadFlag = 0;
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);
    robot.ProgramLoad("test.lua");
    robot.ProgramRun();
    robot.Sleep(2000);
    robot.PauseMotion();
    robot.Sleep(2000);
    robot.ResumeMotion();
    robot.Sleep(2000);
    robot.CloseRPC();
    return 0;
    }

Definir Função da Porta CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a função da porta CI configurável da caixa de controle
    * @param [in] config Código da função CI0-CI7;
    * 0-nenhum;1-sucesso de abertura de arco;2-preparação da soldadora;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
    8-pausa/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem do trabalho;12-comutação manual/automático;
    13-sucesso na busca de posição do fio de solda;14-interrupção de movimento;15-iniciar programa principal;16-iniciar retrocesso;17-confirmação de início;
    18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
    22-modo de redução de nível 1;23-modo de redução de nível 2;24-modo de redução de nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
    27-ativar arrasto auxiliar;28-desativar arrasto auxiliar;29-ativar/desativar arrasto auxiliar;30-limpar todos os erros;
    31-comutação manual/automático (nível alto/baixo);32-ativar;33-desativar;34-ativar/desativar (borda de subida/descida);35-iniciar/terminar rastreamento de ponto fixo
    * @return Código de erro
    */
    errno_t SetDIConfig(int config[8]);

Obter Função da Porta CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a função da porta CI configurável da caixa de controle
    * @param [in] config Código da função CI0-CI7;
    * 0-nenhum;1-sucesso de abertura de arco;2-preparação da soldadora;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
    8-pausa/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem do trabalho;12-comutação manual/automático;
    13-sucesso na busca de posição do fio de solda;14-interrupção de movimento;15-iniciar programa principal;16-iniciar retrocesso;17-confirmação de início;
    18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
    22-modo de redução de nível 1;23-modo de redução de nível 2;24-modo de redução de nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
    27-ativar arrasto auxiliar;28-desativar arrasto auxiliar;29-ativar/desativar arrasto auxiliar;30-limpar todos os erros;
    31-comutação manual/automático (nível alto/baixo);32-ativar;33-desativar;34-ativar/desativar (borda de subida/descida);35-iniciar/terminar rastreamento de ponto fixo
    * @return Código de erro
    */
    errno_t GetDIConfig(int config[8]);

Definir Função da Porta CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a função da porta CO configurável da caixa de controle
    * @param [out] config Código da função CO0-CO7;
    * 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pulverização;4-limpeza do bico de pulverização;5-sinal de gás;6-sinal de abertura de arco;7-avanço do fio por ponto;
    8-retrocesso do fio;9-porta de entrada JOB1;10-porta de entrada JOB2;11-porta de entrada JOB3;12-controle de iniciar/parar esteira;13-robô em pausa;14-origem do trabalho alcançada;
    15-área de interferência alcançada;16-controle de iniciar/parar busca de posição do fio;17-robô iniciado com sucesso;18-iniciar/parar programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1-seguro;
    21-sinal de saída de parada de emergência 2-seguro;22-parada/início de execução do script LUA;23-saída de estado seguro-seguro;24-saída de estado de parada protetiva-seguro;
    25-robô em movimento-seguro;26-robô em modo reduzido-seguro;27-robô em modo não reduzido-seguro;28-robô não parado;29-erro do robô-erro de ponto de comando;
    30-erro do robô-erro do driver;31-erro do robô-erro de limite flexível excedido;32-erro do robô-erro de colisão;33-erro do robô-erro de número de escravas ativas;
    34-erro do robô-erro de escrava;35-erro do robô-erro de E/S;36-erro do robô-erro da garra;37-erro do robô-erro de arquivo;38-erro do robô-erro de pose singular;
    39-erro do robô-erro de comunicação do driver;40-erro do robô-erro de parâmetro;41-erro do robô-erro de limite flexível do eixo externo excedido;42-aviso do robô-aviso;
    43-aviso do robô-aviso de porta de segurança;44-aviso do robô-aviso de movimento;45-aviso do robô-aviso de área de interferência;46-aviso do robô-aviso de parede de segurança;
    47-estado ativado;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;
    * @return Código de erro
    */
    errno_t SetDOConfig(int config[8]);

Obter Função da Porta CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a função da porta CO configurável da caixa de controle
    * @param [out] config Código da função CO0-CO7;
    * 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pulverização;4-limpeza do bico de pulverização;5-sinal de gás;6-sinal de abertura de arco;7-avanço do fio por ponto;
    8-retrocesso do fio;9-porta de entrada JOB1;10-porta de entrada JOB2;11-porta de entrada JOB3;12-controle de iniciar/parar esteira;13-robô em pausa;14-origem do trabalho alcançada;
    15-área de interferência alcançada;16-controle de iniciar/parar busca de posição do fio;17-robô iniciado com sucesso;18-iniciar/parar programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1-seguro;
    21-sinal de saída de parada de emergência 2-seguro;22-parada/início de execução do script LUA;23-saída de estado seguro-seguro;24-saída de estado de parada protetiva-seguro;
    25-robô em movimento-seguro;26-robô em modo reduzido-seguro;27-robô em modo não reduzido-seguro;28-robô não parado;29-erro do robô-erro de ponto de comando;
    30-erro do robô-erro do driver;31-erro do robô-erro de limite flexível excedido;32-erro do robô-erro de colisão;33-erro do robô-erro de número de escravas ativas;
    34-erro do robô-erro de escrava;35-erro do robô-erro de E/S;36-erro do robô-erro da garra;37-erro do robô-erro de arquivo;38-erro do robô-erro de pose singular;
    39-erro do robô-erro de comunicação do driver;40-erro do robô-erro de parâmetro;41-erro do robô-erro de limite flexível do eixo externo excedido;42-aviso do robô-aviso;
    43-aviso do robô-aviso de porta de segurança;44-aviso do robô-aviso de movimento;45-aviso do robô-aviso de área de interferência;46-aviso do robô-aviso de parede de segurança;
    47-estado ativado;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;
    * @return Código de erro
    */
    errno_t GetDOConfig(int config[8]);

Definir Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a função da porta End-CI configurável da extremidade
    * @param [in] config Código da função End CI0-CI1;
    * 0-nenhum;1-chave da ferramenta de arrasto para ensino;2-sinal de gravação de ponto;3-comutação manual/automático (sinal de pulso);4-iniciar/parar gravação TPD;5-pausar movimento;
    6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto auxiliar do sensor de força;12-desativar arrasto auxiliar do sensor de força;
    13-ativar/desativar arrasto auxiliar do sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-movimento PTP para origem do trabalho;17-interrupção de movimento, parar movimento atual com base no sinal;
    18-iniciar programa principal;19-iniciar retrocesso;20-confirmação de início;21-retomar soldagem;22-terminar soldagem;23-limpar erro;24-comutação manual/automático (nível alto/baixo)
    25-ativar;26-desativar;27-ativar/desativar;28-sinal de iniciar/parar rastreamento servo a laser;
    * @return Código de erro
    */
    errno_t SetToolDIConfig(int config[2]);

Obter Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a função da porta End-CI configurável da extremidade
    * @param [out] config Código da função End CI0-CI1;
    * 0-nenhum;1-chave da ferramenta de arrasto para ensino;2-sinal de gravação de ponto;3-comutação manual/automático (sinal de pulso);4-iniciar/parar gravação TPD;5-pausar movimento;
    6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto auxiliar do sensor de força;12-desativar arrasto auxiliar do sensor de força;
    13-ativar/desativar arrasto auxiliar do sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-movimento PTP para origem do trabalho;17-interrupção de movimento, parar movimento atual com base no sinal;
    18-iniciar programa principal;19-iniciar retrocesso;20-confirmação de início;21-retomar soldagem;22-terminar soldagem;23-limpar erro;24-comutação manual/automático (nível alto/baixo)
    25-ativar;26-desativar;27-ativar/desativar;28-sinal de iniciar/parar rastreamento servo a laser;
    * @return Código de erro
    */
    errno_t GetToolDIConfig(int config[2]);

Definir Estado Ativo do CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o estado ativo do CI configurável da caixa de controle
    * @param [in] config Estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t SetDIConfigLevel(int config[8]);

Obter Estado Ativo do CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado ativo do CI configurável da caixa de controle
    * @param [out] config Estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t GetDIConfigLevel(int config[8]);

Definir Estado Ativo do CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o estado ativo do CO configurável da caixa de controle
    * @param [in] config Estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t SetDOConfigLevel(int config[8]);

Obter Estado Ativo do CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado ativo do CO configurável da caixa de controle
    * @param [out] config Estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t GetDOConfigLevel(int config[8]);

Definir Estado Ativo do CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o estado ativo do CI configurável da extremidade
    * @param [in] config Estado ativo das portas CI0-CI1; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t SetToolDIConfigLevel(int config[2]);

Obter Estado Ativo do CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado ativo do CI configurável da extremidade
    * @param [out] config Estado ativo das portas CI0-CI1; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t GetToolDIConfigLevel(int config[2]);

Definir Estado Ativo do DI Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o estado ativo do DI padrão da caixa de controle
    * @param [in] config Estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t SetStandardDILevel(int config[8]);

Obter Estado Ativo do DI Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado ativo do DI padrão da caixa de controle
    * @param [out] config Estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t GetStandardDILevel(int config[8]);

Definir Estado Ativo do DO Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o estado ativo do DO padrão da caixa de controle
    * @param [in] config Estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t SetStandardDOLevel(int config[8]);

Obter Estado Ativo do DO Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado ativo do DO padrão da caixa de controle
    * @param [out] config Estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    errno_t GetStandardDOLevel(int config[8]);

Exemplo de Código de Configuração de E/S do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestIOConfig()
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
        int setDIConfig[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int getDIConfig[8] = { 0 };
        rtn = robot.SetDIConfig(setDIConfig);
        printf("SetDIConfig rtn is %d\n", rtn);
        rtn = robot.GetDIConfig(getDIConfig);
        printf("GetDIConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDIConfig[0], getDIConfig[1], getDIConfig[2], getDIConfig[3], getDIConfig[4], getDIConfig[5], getDIConfig[6], getDIConfig[7]);
        int setDOConfig[8] = { 9, 10, 11, 12, 13, 14, 15, 16 };
        int getDOConfig[8] = { 0 };
        rtn = robot.SetDOConfig(setDOConfig);
        printf("SetDOConfig rtn is %d\n", rtn);
        rtn = robot.GetDOConfig(getDOConfig);
        printf("GetDOConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfig[0], getDOConfig[1], getDOConfig[2], getDOConfig[3], getDOConfig[4], getDOConfig[5], getDOConfig[6], getDOConfig[7]);
        int setToolDIConfig[2] = { 17, 18 };
        int getToolDIConfig[2] = { 0 };
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        printf("SetToolDIConfig rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfig(getToolDIConfig);
        printf("GetToolDIConfig rtn is %d, value is %d %d \n", rtn, getToolDIConfig[0], getToolDIConfig[1]);
        int setDIConfigLevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getDIConfigLevel[8] = { 0 };
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        printf("SetDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDIConfigLevel(getDIConfigLevel);
        printf("GetDIConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDIConfigLevel[0], getDIConfigLevel[1], getDIConfigLevel[2], getDIConfigLevel[3], getDIConfigLevel[4], getDIConfigLevel[5], getDIConfigLevel[6], getDIConfigLevel[7]);
        int setDOConfigLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getDOConfigLevel[8] = { 0 };
        rtn = robot.SetDOConfigLevel(setDOConfigLevel);
        printf("SetDOConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDOConfigLevel(getDOConfigLevel);
        printf("GetDOConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfigLevel[0], getDOConfigLevel[1], getDOConfigLevel[2], getDOConfigLevel[3], getDOConfigLevel[4], getDOConfigLevel[5], getDOConfigLevel[6], getDOConfigLevel[7]);
        int setToolDIConfigLevel[2] = { 1, 0 };
        int getToolDIConfigLevel[2] = { 0 };
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        printf("SetToolDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfigLevel(getToolDIConfigLevel);
        printf("GetToolDIConfigLevel rtn is %d, value is %d %d \n", rtn, getToolDIConfigLevel[0], getToolDIConfigLevel[1]);
        int setStandardDILevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getStandardDILevel[8] = { 0 };
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        printf("SetStandardDILevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDILevel(getStandardDILevel);
        printf("GetStandardDILevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDILevel[0], getStandardDILevel[1], getStandardDILevel[2], getStandardDILevel[3], getStandardDILevel[4], getStandardDILevel[5], getStandardDILevel[6], getStandardDILevel[7]);
        int setStandardDOLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getStandardDOLevel[8] = { 0 };
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        printf("SetStandardDOLevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDOLevel(getStandardDOLevel);
        printf("GetStandsrdDOLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDOLevel[0], getStandardDOLevel[1], getStandardDOLevel[2], getStandardDOLevel[3], getStandardDOLevel[4], getStandardDOLevel[5], getStandardDOLevel[6], getStandardDOLevel[7]);
        robot.Sleep(2000);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }