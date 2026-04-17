E/S do Robô
==================

.. toctree:: 
    :maxdepth: 5

Definir Saída Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir saída digital do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in] status 0-desligado, 1-ligado
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetDO(int id, byte status, byte smooth, byte block); 

Definir Saída Digital da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir saída digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] status 0-desligado, 1-ligado
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetToolDO(int id, byte status, byte smooth, byte block); 

Definir Saída Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir saída analógica do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] value Percentual do valor de corrente ou tensão, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetAO(int id, float value, byte block); 

Definir Saída Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Definir saída analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in] value Percentual do valor de corrente ou tensão, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetToolAO(int id, float value, byte block);

Exemplo de Código para Definir Saídas Digitais e Analógicas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos: 

    private void button14_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;


        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 0;

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 1;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        status = 0;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetAO(0, i, block);
            Thread.Sleep(30);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetToolAO(0, i, block);
            Thread.Sleep(30);
        }

    }

Obter Entrada Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter entrada digital do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  0-nível baixo, 1-nível alto
    * @return  Código de erro
    */   
    int GetDI(int id, byte block, ref byte level);

Obter Entrada Digital da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter entrada digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  0-nível baixo, 1-nível alto
    * @return  Código de erro
    */   
    int GetToolDI(int id, byte block, ref byte level); 

Obter Entrada Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter entrada analógica do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  Percentual do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */   
    int GetAI(int id, byte block, ref float persent); 

Obter Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obter entrada analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] result  Percentual do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */   
    int GetToolAI(int id, byte block, ref float persent); 

Obter Estado do Botão de Registro de Ponto da Extremidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter estado do botão de registro de ponto da extremidade do robô
    * @param [out] state Estado do botão, 0-pressionado, 1-solto
    * @return Código de erro
    */ 
    int GetAxlePointRecordBtnState(ref byte state); 

Obter Estado de Saída DO da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter estado de saída DO da extremidade do robô
    * @param [out] do_state Estado de saída DO, do0~do1 correspondem aos bits 1~2, começando do bit0
    * @return Código de erro
    */ 
    int GetToolDO(ref byte do_state);

Obter Estado de Saída DO do Controlador do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter estado de saída DO do controlador do robô
    * @param [out] do_state_h Estado de saída DO, co0~co7 correspondem aos bits 0~7
    * @param [out] do_state_l Estado de saída DO, do0~do7 correspondem aos bits 0~7
    * @return Código de erro
    */ 
    int GetDO(ref int do_state_h, ref int do_state_l);   

Exemplo de Código para Obter Estados DI e DO do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button15_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        robot.GetDI(0, block, ref di);
        Console.WriteLine($"di0: {di}");

        tool_di = (byte)robot.GetToolDI(1, block, ref tool_di);
        Console.WriteLine($"tool_di1: {tool_di}");

        robot.GetAI(0, block, ref ai);
        Console.WriteLine($"ai0: {ai}");

        tool_ai = robot.GetToolAI(0, block, ref tool_ai);
        Console.WriteLine($"tool_ai0: {tool_ai}");

        byte _button_state = 0;
        robot.GetAxlePointRecordBtnState(ref _button_state);
        Console.WriteLine($"_button_state is: {_button_state}");

        byte tool_do_state = 0;
        robot.GetToolDO(ref tool_do_state);
        Console.WriteLine($"tool DO state is: {tool_do_state}");

        int do_state_h = 0;
        int do_state_l = 0;
        robot.GetDO(ref do_state_h, ref do_state_l);
        Console.WriteLine($"DO state high is: {do_state_h}\n DO state low is: {do_state_l}");
    }

Aguardar Entrada Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aguardar entrada digital do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~15]
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar o timeout e continuar a execução, 2-esperar indefinidamente
    * @return  Código de erro
    */
    int WaitDI(int id, byte status, int max_time, int opt); 

Aguardar Entrada Digital Multicanal do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aguardar entrada digital multicanal do painel de controle
    * @param  [in] mode 0-E lógico multicanal, 1-OU lógico multicanal
    * @param  [in] id  Número da E/S, bits 0~7 correspondem a DI0~DI7, bits 8~15 correspondem a CI0~CI7
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar o timeout e continuar a execução, 2-esperar indefinidamente
    * @return  Código de erro
    */
    int WaitMultiDI(int mode, int id, byte status, int max_time, int opt); 

Aguardar Entrada Digital da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aguardar entrada digital da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in]  status 0-desligado, 1-ligado
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar o timeout e continuar a execução, 2-esperar indefinidamente
    * @return  Código de erro
    */
    int WaitToolDI(int id, byte status, int max_time, int opt); 

Aguardar Entrada Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aguardar entrada analógica do painel de controle
    * @param  [in] id  Número da E/S, intervalo [0~1]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value Percentual do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar o timeout e continuar a execução, 2-esperar indefinidamente
    * @return  Código de erro
    */
    int WaitAI(int id, int sign, float value, int max_time, int opt);   

Aguardar Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aguardar entrada analógica da ferramenta
    * @param  [in] id  Número da E/S, intervalo [0]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value Percentual do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar o timeout e continuar a execução, 2-esperar indefinidamente
    * @return  Código de erro
    */
    int WaitToolAI(int id, int sign, float value, int max_time, int opt); 

Exemplo de Código para Aguardar Sinais de Entrada Digital e Analógica do Painel de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnIOTest_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        int rtn = robot.WaitDI(0, 1, 1000, 1);
        Console.WriteLine("WaitDI over; rtn is: " + rtn);

        robot.WaitMultiDI(1, 3, 3, 1000, 1);
        Console.WriteLine("WaitMultiDI over; rtn is: " + rtn);

        robot.WaitToolDI(1, 1, 1000, 1);
        Console.WriteLine("WaitToolDI over; rtn is: " + rtn);

        robot.WaitAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitAI over; rtn is: " + rtn);

        robot.WaitToolAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitToolAI over; rtn is: " + rtn);
    }

Definir se a Saída DO do Painel de Controle Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída DO do painel de controle deve ser reinicializada após parada/pausa
    * @param [in] resetFlag 0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag);

Definir se a Saída AO do Painel de Controle Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída AO do painel de controle deve ser reinicializada após parada/pausa
    * @param [in] resetFlag  0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag);

Definir se a Saída DO da Ferramenta na Extremidade Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída DO da ferramenta na extremidade deve ser reinicializada após parada/pausa
    * @param [in] resetFlag  0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetAxleDO(int resetFlag, int reloadFlag);

Definir se a Saída AO da Ferramenta na Extremidade Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída AO da ferramenta na extremidade deve ser reinicializada após parada/pausa
    * @param [in] resetFlag 0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetAxleAO(int resetFlag, int reloadFlag);

Definir se a Saída DO Estendida Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída DO estendida deve ser reinicializada após parada/pausa
    * @param [in] resetFlag  0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return  Código de erro
    */
    public int SetOutputResetExtDO(int resetFlag, int reloadFlag);

Definir se a Saída AO Estendida Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída AO estendida deve ser reinicializada após parada/pausa
    * @param [in] resetFlag 0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetExtAO(int resetFlag, int reloadFlag);

Definir se a Saída DO do SmartTool Deve ser Reinicializada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Definir se a saída DO do SmartTool deve ser reinicializada após parada/pausa
    * @param [in] resetFlag 0-não reinicializar; 1-reinicializar
    * @param [in] reloadFlag Recarregar após retomar da pausa? 0-não recarregar; 1-recarregar
    * @return Código de erro
    */
    public int SetOutputResetSmartToolDO(int resetFlag, int reloadFlag);

Exemplo de Código para Reinicialização de Saída Após Parada/Pausa do Programa LUA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestDOReset()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, 1, 0, 0);
            Thread.Sleep(200);
        }

        int resetFlag = 1;
        int resumeReloadFlag = 1;
        int rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();

        Thread.Sleep(2000);
        robot.PauseMotion();
        Thread.Sleep(2000);
        robot.ResumeMotion();
        Thread.Sleep(2000);
    }

Definir Função da Porta CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir função da porta CI configurável do painel de controle
    * @param [in] config Código de função para CI0-CI7;
    * 0-nenhum;1-sucesso na abertura de arco;2-preparação da máquina de solda;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
    8-pausar/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem de trabalho;12-alternar manual/automático;
    13-sucesso na busca de posição do arame;14-interrupção de movimento;15-iniciar programa principal;16-iniciar rebobinagem;17-confirmar início;
    18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
    22-modo de redução nível 1;23-modo de redução nível 2;24-modo de redução nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
    27-ativar arrasto assistido;28-desativar arrasto assistido;29-ativar/desativar arrasto assistido;30-limpar todos os erros;
    31-alternar manual/automático (nível alto/baixo);32-habilitar;33-desabilitar;34-habilitar/desabilitar (borda de subida/descida);35-iniciar/parar rastreamento de ponto fixo
    * @return Código de erro
    */
    public int SetDIConfig(int[] config)

Obter Função da Porta CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter função da porta CI configurável do painel de controle
    * @param [in] config Código de função para CI0-CI7;
    * 0-nenhum;1-sucesso na abertura de arco;2-preparação da máquina de solda;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
    8-pausar/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem de trabalho;12-alternar manual/automático;
    13-sucesso na busca de posição do arame;14-interrupção de movimento;15-iniciar programa principal;16-iniciar rebobinagem;17-confirmar início;
    18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
    22-modo de redução nível 1;23-modo de redução nível 2;24-modo de redução nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
    27-ativar arrasto assistido;28-desativar arrasto assistido;29-ativar/desativar arrasto assistido;30-limpar todos os erros;
    31-alternar manual/automático (nível alto/baixo);32-habilitar;33-desabilitar;34-habilitar/desabilitar (borda de subida/descida);35-iniciar/parar rastreamento de ponto fixo
    * @return Código de erro
    */
    public int GetDIConfig(out int[] config)

Definir Função da Porta CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir função da porta CO configurável do painel de controle
    * @param [out] config Código de função para CO0-CO7;
    * 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pintura;4-limpeza do bocal de pintura;5-sinal de envio de gás;6-sinal de abertura de arco;7-alimentação de arame ponto a ponto;
    8-alimentação de arame reversa;9-porta de entrada JOB 1;10-porta de entrada JOB 2;11-porta de entrada JOB 3;12-controle de início/parada da esteira;13-robô pausado;14-chegada na origem de trabalho;
    15-chegada na zona de interferência;16-controle de início/parada da busca de posição do arame;17-inicialização do robô concluída;18-parada/início do programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1 - segurança;
    21-sinal de saída de parada de emergência 2 - segurança;22-parada/início da execução do script LUA;23-saída de estado de segurança - segurança;24-saída de estado de parada protetiva - segurança;
    25-robô em movimento - segurança;26-modo de redução do robô - segurança;27-modo de não redução do robô - segurança;28-robô não parado;29-erro do robô - erro de ponto de comando;
    30-erro do robô - erro do driver;31-erro do robô - erro de limite suave excedido;32-erro do robô - erro de colisão;33-erro do robô - erro no número de escravos ativos;
    34-erro do robô - erro de escravo;35-erro do robô - erro de E/S;36-erro do robô - erro de garra;37-erro do robô - erro de arquivo;38-erro do robô - erro de pose singular;
    39-erro do robô - erro de comunicação com o driver;40-erro do robô - erro de parâmetro;41-erro do robô - erro de limite suave excedido no eixo externo;42-aviso do robô - aviso;
    43-aviso do robô - aviso de porta de segurança;44-aviso do robô - aviso de movimento;45-aviso do robô - aviso de zona de interferência;46-aviso do robô - aviso de parede de segurança;
    47-estado de habilitação;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;
    * @return Código de erro
    */
    public int SetDOConfig(int[] config)

Obter Função da Porta CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter função da porta CO configurável do painel de controle
    * @param [out] config Código de função para CO0-CO7;
    * 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pintura;4-limpeza do bocal de pintura;5-sinal de envio de gás;6-sinal de abertura de arco;7-alimentação de arame ponto a ponto;
    8-alimentação de arame reversa;9-porta de entrada JOB 1;10-porta de entrada JOB 2;11-porta de entrada JOB 3;12-controle de início/parada da esteira;13-robô pausado;14-chegada na origem de trabalho;
    15-chegada na zona de interferência;16-controle de início/parada da busca de posição do arame;17-inicialização do robô concluída;18-parada/início do programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1 - segurança;
    21-sinal de saída de parada de emergência 2 - segurança;22-parada/início da execução do script LUA;23-saída de estado de segurança - segurança;24-saída de estado de parada protetiva - segurança;
    25-robô em movimento - segurança;26-modo de redução do robô - segurança;27-modo de não redução do robô - segurança;28-robô não parado;29-erro do robô - erro de ponto de comando;
    30-erro do robô - erro do driver;31-erro do robô - erro de limite suave excedido;32-erro do robô - erro de colisão;33-erro do robô - erro no número de escravos ativos;
    34-erro do robô - erro de escravo;35-erro do robô - erro de E/S;36-erro do robô - erro de garra;37-erro do robô - erro de arquivo;38-erro do robô - erro de pose singular;
    39-erro do robô - erro de comunicação com o driver;40-erro do robô - erro de parâmetro;41-erro do robô - erro de limite suave excedido no eixo externo;42-aviso do robô - aviso;
    43-aviso do robô - aviso de porta de segurança;44-aviso do robô - aviso de movimento;45-aviso do robô - aviso de zona de interferência;46-aviso do robô - aviso de parede de segurança;
    47-estado de habilitação;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;
    * @return Código de erro
    */
    public int GetDOConfig(out int[] config)

Definir Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir função da porta End-CI configurável da extremidade
    * @param [in] config Código de função para End CI0-CI1;
    * 0-nenhum;1-interruptor de ferramenta de ensinamento por arrasto;2-sinal de registro de ponto;3-alternar manual/automático (sinal de pulso);4-iniciar/parar registro TPD;5-pausar movimento;
    6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto assistido por sensor de força;12-desativar arrasto assistido por sensor de força;
    13-ativar/desativar arrasto assistido por sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-mover PTP para origem de trabalho;17-interromper movimento, parar o movimento atual de acordo com o sinal;
    18-iniciar programa principal;19-iniciar rebobinagem;20-confirmar início;21-retomar soldagem;22-terminar soldagem;23-limpar erros;24-alternar manual/automático (nível alto/baixo);
    25-habilitar;26-desabilitar;27-habilitar/desabilitar;28-sinal de início/parada de rastreamento servo a laser;
    * @return Código de erro
    */
    public int SetToolDIConfig(int[] config)

Obter Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter função da porta End-CI configurável da extremidade
    * @param [out] config Código de função para End CI0-CI1;
    * 0-nenhum;1-interruptor de ferramenta de ensinamento por arrasto;2-sinal de registro de ponto;3-alternar manual/automático (sinal de pulso);4-iniciar/parar registro TPD;5-pausar movimento;
    6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto assistido por sensor de força;12-desativar arrasto assistido por sensor de força;
    13-ativar/desativar arrasto assistido por sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-mover PTP para origem de trabalho;17-interromper movimento, parar o movimento atual de acordo com o sinal;
    18-iniciar programa principal;19-iniciar rebobinagem;20-confirmar início;21-retomar soldagem;22-terminar soldagem;23-limpar erros;24-alternar manual/automático (nível alto/baixo);
    25-habilitar;26-desabilitar;27-habilitar/desabilitar;28-sinal de início/parada de rastreamento servo a laser;
    * @return Código de erro
    */
    public int GetToolDIConfig(out int[] config)

Definir Estado Ativo da CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir estado ativo da CI configurável do painel de controle
    * @param [in] config Estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int SetDIConfigLevel(int[] config)

Obter Estado Ativo da CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter estado ativo da CI configurável do painel de controle
    * @param [out] config Estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int GetDIConfigLevel(out int[] config)

Definir Estado Ativo da CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir estado ativo da CO configurável do painel de controle
    * @param [in] config Estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int SetDOConfigLevel(int[] config)

Obter Estado Ativo da CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter estado ativo da CO configurável do painel de controle
    * @param [out] config Estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int GetDOConfigLevel(out int[] config)

Definir Estado Ativo da CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir estado ativo da CI configurável da extremidade
    * @param [in] config Estado ativo das portas CI0-CI1; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int SetToolDIConfigLevel(int[] config)

Obter Estado Ativo da CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter estado ativo da CI configurável da extremidade
    * @param [out] config Estado ativo das portas CI0-CI1; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int GetToolDIConfigLevel(out int[] config)

Definir Estado Ativo do DI Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir estado ativo do DI padrão do painel de controle
    * @param [in] config Estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int SetStandardDILevel(int[] config)

Obter Estado Ativo do DI Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter estado ativo do DI padrão do painel de controle
    * @param [out] config Estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int GetStandardDILevel(out int[] config)

Definir Estado Ativo do DO Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir estado ativo do DO padrão do painel de controle
    * @param [in] config Estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int SetStandardDOLevel(int[] config)

Obter Estado Ativo do DO Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter estado ativo do DO padrão do painel de controle
    * @param [out] config Estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo
    * @return Código de erro
    */
    public int GetStandardDOLevel(out int[] config)

Exemplo de Código de Configuração de E/S do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestIOConfig()
    {
        int rtn = 0;

        // ---------- Testar função da porta CI configurável ----------
        int[] setDIConfig = new int[] { 3, 9, 1, 4, 5, 6, 7, 8 };
        rtn = robot.SetDIConfig(setDIConfig);
        Console.WriteLine($"SetDIConfig rtn is {rtn}");

        // Usar o parâmetro out para receber o array de configuração obtido
        int[] getDIConfig;
        rtn = robot.GetDIConfig(out getDIConfig);  
        Console.WriteLine($"GetDIConfig rtn is {rtn}, value is {string.Join(" ", getDIConfig)}");

        // ---------- Testar função da porta CO configurável ----------
        int[] setDOConfig = new int[] { 9, 10, 11, 12, 13, 14, 15, 16 };
        rtn = robot.SetDOConfig(setDOConfig);
        Console.WriteLine($"SetDOConfig rtn is {rtn}");

        int[] getDOConfig;
        rtn = robot.GetDOConfig(out getDOConfig);
        Console.WriteLine($"GetDOConfig rtn is {rtn}, value is {string.Join(" ", getDOConfig)}");

        // ---------- Testar função da porta CI configurável da extremidade ----------
        int[] setToolDIConfig = new int[] { 17, 18 };
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        Console.WriteLine($"SetToolDIConfig rtn is {rtn}");

        int[] getToolDIConfig;
        rtn = robot.GetToolDIConfig(out getToolDIConfig);
        Console.WriteLine($"GetToolDIConfig rtn is {rtn}, value is {string.Join(" ", getToolDIConfig)}");

        // ---------- Testar estado ativo da CI configurável do painel de controle ----------
        int[] setDIConfigLevel = new int[] { 1, 1, 1, 1, 0, 0, 0, 0 };
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        Console.WriteLine($"SetDIConfigLevel rtn is {rtn}");

        int[] getDIConfigLevel;
        rtn = robot.GetDIConfigLevel(out getDIConfigLevel);
        Console.WriteLine($"GetDIConfigLevel rtn is {rtn}, value is {string.Join(" ", getDIConfigLevel)}");

        // ---------- Testar estado ativo da CO configurável do painel de controle ----------
        int[] setDOConfigLevel = new int[] { 0, 0, 0, 0, 1, 1, 1, 1 };
        rtn = robot.SetDIConfigLevel(setDOConfigLevel);
        Console.WriteLine($"SetDOConfigLevel rtn is {rtn}");

        int[] getDOConfigLevel;
        rtn = robot.GetDOConfigLevel(out getDOConfigLevel);
        Console.WriteLine($"GetDOConfigLevel rtn is {rtn}, value is {string.Join(" ", getDOConfigLevel)}");

        // ---------- Testar estado ativo da CI configurável da extremidade ----------
        int[] setToolDIConfigLevel = new int[] { 1, 0 };
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        Console.WriteLine($"SetToolDIConfigLevel rtn is {rtn}");

        int[] getToolDIConfigLevel;
        rtn = robot.GetToolDIConfigLevel(out getToolDIConfigLevel);
        Console.WriteLine($"GetToolDIConfigLevel rtn is {rtn}, value is {string.Join(" ", getToolDIConfigLevel)}");

        // ---------- Testar estado ativo do DI padrão do painel de controle ----------
        int[] setStandardDILevel = new int[] { 1, 1, 1, 1, 0, 0, 0, 0 };
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        Console.WriteLine($"SetStandardDILevel rtn is {rtn}");

        int[] getStandardDILevel;
        rtn = robot.GetStandardDILevel(out getStandardDILevel);
        Console.WriteLine($"GetStandardDILevel rtn is {rtn}, value is {string.Join(" ", getStandardDILevel)}");

        // ---------- Testar estado ativo do DO padrão do painel de controle ----------
        int[] setStandardDOLevel = new int[] { 0, 0, 0, 0, 1, 1, 1, 1 };
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        Console.WriteLine($"SetStandardDOLevel rtn is {rtn}");

        int[] getStandardDOLevel;
        rtn = robot.GetStandardDOLevel(out getStandardDOLevel);
        Console.WriteLine($"GetStandardDOLevel rtn is {rtn}, value is {string.Join(" ", getStandardDOLevel)}");

    }