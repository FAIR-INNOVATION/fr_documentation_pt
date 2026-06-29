IO do Robô
============

.. toctree:: 
    :maxdepth: 5

Definir Saída Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a saída digital do painel de controle
    * @param  [in] id  Número do IO, faixa [0~15]
    * @param  [in] status 0-desligar, 1-ligar
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetDO(int id, int status, int smooth, int block); 

Definir Saída Digital da Ferramenta
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a saída digital da ferramenta
    * @param  [in] id  Número do IO, faixa [0~1]
    * @param  [in] status 0-desligar, 1-ligar
    * @param  [in] smooth 0-não suave, 1-suave
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetToolDO(int id, int status, int smooth, int block); 

Definir Saída Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a saída analógica do painel de controle
    * @param  [in] id  Número do IO, faixa [0~1]
    * @param  [in] value  Porcentagem do valor de corrente ou tensão, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetAO(int id, double value, int block); 

Definir Saída Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Define a saída analógica da ferramenta
    * @param  [in] id  Número do IO, faixa [0]
    * @param  [in] value  Porcentagem do valor de corrente ou tensão, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @return  Código de erro
    */
    int SetToolAO(int id, double value, int block); 

Exemplo de Código para Definir Saídas Digitais e Analógicas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAODO(Robot robot)
    {

        int status = 1;
        int smooth = 0;
        int block = 0;

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
            robot.SetAO(0, i, block);
            robot.Sleep(30);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetToolAO(0, i, block);
            robot.Sleep(30);
        }

        robot.CloseRPC();
        return 0;
    }

Obter Entrada Digital do Painel de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a entrada digital do painel de controle
    * @param  [in] id  Número do IO, faixa [0~15]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] level  0-nível baixo, 1-nível alto
    * @return  Código de erro
    */   
    int GetDI(int id, int block, int[] level);

Obter Entrada Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a entrada digital da ferramenta
    * @param  [in] id    Número do IO, faixa [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] level 0-nível baixo, 1-nível alto
    * @return  Código de erro
    */   
    int GetToolDI(int id, int block, int[] level);

Obter Entrada Analógica do Painel de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a entrada analógica do painel de controle
    * @param  [in] id  Número do IO, faixa [0~1]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] percent  Porcentagem do valor de corrente ou tensão de entrada, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */   
    int GetAI(int id, int block, double[] percent)

Obter Entrada Analógica da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém a entrada analógica da ferramenta
    * @param  [in] id  Número do IO, faixa [0]
    * @param  [in] block  0-bloqueante, 1-não bloqueante
    * @param  [out] percent  Porcentagem do valor de corrente ou tensão de entrada, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @return  Código de erro
    */   
    int GetToolAI(int id, int block, double[] percent)

Obter Estado do Botão de Gravação de Ponto da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado do botão de gravação de ponto da extremidade do robô
    * @param  [out] state Estado do botão, 0-pressionado, 1-solto
    * @return  Código de erro
    */   
    int GetAxlePointRecordBtnState(int[] state)

Obter Estado da Saída DO da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado da saída DO da extremidade do robô
    * @param  [out] do_state Estado da saída DO, do0~do1 correspondem aos bits 1~2, começando do bit0
    * @return  Código de erro
    */   
    int GetToolDO(int[] do_state)

Obter Estado da Saída DO do Controlador do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Obtém o estado da saída DO do controlador do robô
    * @param  [out] do_state_h Estado da saída DO, co0~co7 correspondem aos bits 0~7
    * @param  [out] do_state_l Estado da saída DO, do0~do7 correspondem aos bits 0~7
    * @return  Código de erro
    */   
    int GetDO(int[] do_state_h, int[] do_state_l)

Exemplo de Código para Obter Estados DI e DO do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetDIAI(Robot robot)
    {
        int status = 1;
        int smooth = 0;
        int block = 0;
        int[] di =new int[]{0}, tool_di =new int[] {0};
        double[] ai =new double[] {0}, tool_ai = new double[]{0};
        double value = 0.0;


        robot.GetDI(0, block, di);
        System.out.println("di0:"+di[0]);

        robot.GetToolDI(1, block, tool_di);
        System.out.println("tool_di1:"+ tool_di[0]);

        robot.GetAI(0, block, ai);
        System.out.println("ai0:"+ ai[0]);

        robot.GetToolAI(0, block, tool_ai);
        System.out.println("tool_ai0:"+ tool_ai[0]);

        int[] _button_state=new int[]{0};
        robot.GetAxlePointRecordBtnState(_button_state);
        System.out.println("_button_state is: "+ _button_state[0]);

        int[] tool_do_state=new int[]{0};
        robot.GetToolDO(tool_do_state);
        System.out.println("tool DO state is: "+ tool_do_state[0]);

        int[] do_state_h=new int[]{0};
        int[] do_state_l=new int[]{0};
        robot.GetDO(do_state_h, do_state_l);
        System.out.println("DO state high is: "+do_state_h[0]+", DO state low is: "+ do_state_l[0]);

        return 0;
    }

Aguardar Entrada Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada digital do painel de controle
    * @param  [in]  id  Número do IO, faixa [0~15]
    * @param  [in]  status 0-desligar, 1-ligar
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após tempo limite, 0-parar o programa e indicar tempo limite, 1-ignorar o aviso de tempo limite e continuar a execução, 2-aguardar indefinidamente
    * @return  Código de erro
    */
    int WaitDI(int id, int status, int max_time, int opt); 

Aguardar Múltiplas Entradas Digitais do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda múltiplas entradas digitais do painel de controle
    * @param  [in] mode 0-E lógico (AND) para múltiplos canais, 1-Ou lógico (OR) para múltiplos canais
    * @param  [in] id  Número do IO, bit0~bit7 correspondem a DI0~DI7, bit8~bit15 correspondem a CI0~CI7
    * @param  [in] status 0-desligar, 1-ligar
    * @param  [in] max_time  Tempo máximo de espera, unidade ms
    * @param  [in] opt  Estratégia após tempo limite, 0-parar o programa e indicar tempo limite, 1-ignorar o aviso de tempo limite e continuar a execução, 2-aguardar indefinidamente
    * @return  Código de erro
    */
    int WaitMultiDI(int mode, int id, int status, int max_time, int opt); 

Aguardar Entrada Digital da Ferramenta
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada digital da ferramenta
    * @param  [in]  id  Número do IO, faixa [0~1]
    * @param  [in]  status 0-desligar, 1-ligar
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após tempo limite, 0-parar o programa e indicar tempo limite, 1-ignorar o aviso de tempo limite e continuar a execução, 2-aguardar indefinidamente
    * @return  Código de erro
    */
    int WaitToolDI(int id, int status, int max_time, int opt); 

Aguardar Entrada Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada analógica do painel de controle
    * @param  [in]  id  Número do IO, faixa [0~1]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value  Porcentagem do valor de corrente ou tensão de entrada, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após tempo limite, 0-parar o programa e indicar tempo limite, 1-ignorar o aviso de tempo limite e continuar a execução, 2-aguardar indefinidamente
    * @return  Código de erro
    */
    int WaitAI(int id, int sign, double value, int max_time, int opt);   

Aguardar Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada analógica da ferramenta
    * @param  [in]  id  Número do IO, faixa [0]
    * @param  [in]  sign 0-maior que, 1-menor que
    * @param  [in]  value  Porcentagem do valor de corrente ou tensão de entrada, faixa [0~100] corresponde a corrente [0~20mA] ou tensão [0~10V]
    * @param  [in]  max_time  Tempo máximo de espera, unidade ms
    * @param  [in]  opt  Estratégia após tempo limite, 0-parar o programa e indicar tempo limite, 1-ignorar o aviso de tempo limite e continuar a execução, 2-aguardar indefinidamente
    * @return  Código de erro
    */
    int WaitToolAI(int id, int sign, double value, int max_time, int opt); 

Exemplo de Código para Aguardar Sinais de Entrada Digital e Analógica do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWaitDIAI(Robot robot)
    {
        int rtn=-1;

        int status = 1;
        int smooth = 0;
        int block = 0;
        int di = 0, tool_di = 0;
        double ai = 0.0, tool_ai = 0.0;
        double value = 0.0;

        rtn = robot.WaitDI(0, 1, 1000, 1);
        System.out.println("WaitDI over; rtn is: "+ rtn);

        robot.WaitMultiDI(1, 3, 3, 1000, 1);
        System.out.println("WaitDI over; rtn is: "+ rtn);

        robot.WaitToolDI(1, 1, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);

        robot.WaitAI(0, 0, 50, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);

        robot.WaitToolAI(0, 0, 50, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);
        return 0;
    }

Definir se a Saída do DO do Painel de Controle é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do DO do painel de controle é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag)

Definir se a Saída do AO do Painel de Controle é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do AO do painel de controle é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag)

Definir se a Saída do DO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do DO da ferramenta de extremidade é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetAxleDO(int resetFlag, int reloadFlag)

Definir se a Saída do AO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do AO da ferramenta de extremidade é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetAxleAO(int resetFlag, int reloadFlag)
    
Definir se a Saída do DO de Extensão é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do DO de extensão é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetExtDO(int resetFlag, int reloadFlag)
    
Definir se a Saída do AO de Extensão é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do AO de extensão é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetExtAO(int resetFlag, int reloadFlag)

Definir se a Saída do SmartTool é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define se a saída do SmartTool é reiniciada após parada/pausa
    * @param resetFlag  0-não reiniciar; 1-reiniciar
    * @param reloadFlag Se recarrega após retomar da pausa, 0-não carregar; 1-carregar
    * @return Código de erro
    */
    public int SetOutputResetSmartToolDO(int resetFlag, int reloadFlag)

Exemplo de Código para Definir Reinicialização da Saída Após Parada/Pausa do Programa LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestDOReset(Robot robot)
    {
        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, 1, 0, 0);
            robot.Sleep(200);
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
        robot.ProgramLoad("test.lua");
        robot.ProgramRun();
        robot.Sleep(2000);
        robot.PauseMotion();
        robot.Sleep(2000);
        robot.ResumeMotion();
        robot.Sleep(2000);
        robot.CloseRPC();
    }

Definir Função da Porta CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a função da porta CI configurável do painel de controle
    * @param config Códigos de função CI0-CI7;
    * 0-Nenhum;1-Sucesso de partida de arco;2-Fonte de solda pronta;3-Detecção de esteira;4-Pausar;5-Retomar;6-Iniciar;7-Parar;
    8-Pausar/Retomar;9-Iniciar/Parar;10-Arrastagem por pedal;11-Mover para ponto de operação;12-Alternar manual/automático;
    13-Sucesso da busca de posição do arame;14-Interrupção de movimento;15-Iniciar programa principal;16-Iniciar rebobinagem;17-Confirmar início;
    18-Sinal de detecção fotoelétrica X;19-Sinal de detecção fotoelétrica Y;20-Sinal de entrada de parada de emergência externa 1;21-Sinal de entrada de parada de emergência externa 2;
    22-Modo de redução nível 1;23-Modo de redução nível 2;24-Modo de redução nível 3 (parada);25-Recuperar soldagem;26-Terminar soldagem;
    27-Ativar arrastagem assistida;28-Desativar arrastagem assistida;29-Ativar/Desativar arrastagem assistida;30-Limpar todos os erros;
    31-Alternar manual/automático (nível alto/baixo);32-Habilitar;33-Desabilitar;34-Habilitar/Desabilitar (borda de subida/descida);35-Iniciar/Parar rastreamento pontual
    * @return Código de erro
    */
    public int SetDIConfig(int[] config)

Obter Função da Porta CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a função da porta CI configurável do painel de controle
    * @param config Códigos de função CI0-CI7;
    * 0-Nenhum;1-Sucesso de partida de arco;2-Fonte de solda pronta;3-Detecção de esteira;4-Pausar;5-Retomar;6-Iniciar;7-Parar;
    8-Pausar/Retomar;9-Iniciar/Parar;10-Arrastagem por pedal;11-Mover para ponto de operação;12-Alternar manual/automático;
    13-Sucesso da busca de posição do arame;14-Interrupção de movimento;15-Iniciar programa principal;16-Iniciar rebobinagem;17-Confirmar início;
    18-Sinal de detecção fotoelétrica X;19-Sinal de detecção fotoelétrica Y;20-Sinal de entrada de parada de emergência externa 1;21-Sinal de entrada de parada de emergência externa 2;
    22-Modo de redução nível 1;23-Modo de redução nível 2;24-Modo de redução nível 3 (parada);25-Recuperar soldagem;26-Terminar soldagem;
    27-Ativar arrastagem assistida;28-Desativar arrastagem assistida;29-Ativar/Desativar arrastagem assistida;30-Limpar todos os erros;
    31-Alternar manual/automático (nível alto/baixo);32-Habilitar;33-Desabilitar;34-Habilitar/Desabilitar (borda de subida/descida);35-Iniciar/Parar rastreamento pontual
    * @return Código de erro
    */
    public int GetDIConfig(int[] config)

Definir Função da Porta CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a função da porta CO configurável do painel de controle
    * @param config Códigos de função CO0-CO7;
    * 0-Nenhum;1-Erro do robô;2-Robô em movimento;3-Iniciar/Parar pintura;4-Limpeza da pistola de pintura;5-Sinal de fluxo de gás;6-Sinal de partida de arco;7-Alimentação de arame ponto a ponto;
    8-Alimentação de arame reversa;9-Porta de entrada JOB 1;10-Porta de entrada JOB 2;11-Porta de entrada JOB 3;12-Controle de início/parada da esteira;13-Robô em pausa;14-Ponto de operação atingido;
    15-Área de interferência atingida;16-Controle de início/parada da busca de posição do arame;17-Início do robô concluído;18-Início/Parada do programa;19-Modo automático/manual;20-Sinal de saída de parada de emergência 1 - seguro;
    21-Sinal de saída de parada de emergência 2 - seguro;22-Execução/Parada do programa de script LUA;23-Saída de estado seguro - seguro;24-Saída de estado de parada protetiva - seguro;
    25-Robô em movimento - seguro;26-Modo de redução do robô - seguro;27-Modo não reduzido do robô - seguro;28-Robô não parado;29-Erro do robô - erro de ponto de comando;
    30-Erro do robô - erro do driver;31-Erro do robô - erro de limite flexível excedido;32-Erro do robô - erro de colisão;33-Erro do robô - erro no número de escravos ativos;
    34-Erro do robô - erro de escravo;35-Erro do robô - erro de IO;36-Erro do robô - erro da garra;37-Erro do robô - erro de arquivo;38-Erro do robô - erro de pose singular;
    39-Erro do robô - erro de comunicação do driver;40-Erro do robô - erro de parâmetro;41-Erro do robô - erro de limite flexível do eixo externo excedido;42-Aviso do robô - aviso;
    43-Aviso do robô - aviso de porta de segurança;44-Aviso do robô - aviso de movimento;45-Aviso do robô - aviso de área de interferência;46-Aviso do robô - aviso de parede de segurança;
    47-Estado de habilitação;48-Elevação automática por desconexão em andamento;49-Aviso de interferência do cuboide 1;50-Aviso de interferência do cuboide 2;51-Aviso de interferência do cuboide 3;52-Aviso de interferência do cuboide 4;
    * @return Código de erro
    */
    public int SetDOConfig(int[] config)

Obter Função da Porta CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a função da porta CO configurável do painel de controle
    * @param config Códigos de função CO0-CO7;
    * 0-Nenhum;1-Erro do robô;2-Robô em movimento;3-Iniciar/Parar pintura;4-Limpeza da pistola de pintura;5-Sinal de fluxo de gás;6-Sinal de partida de arco;7-Alimentação de arame ponto a ponto;
    8-Alimentação de arame reversa;9-Porta de entrada JOB 1;10-Porta de entrada JOB 2;11-Porta de entrada JOB 3;12-Controle de início/parada da esteira;13-Robô em pausa;14-Ponto de operação atingido;
    15-Área de interferência atingida;16-Controle de início/parada da busca de posição do arame;17-Início do robô concluído;18-Início/Parada do programa;19-Modo automático/manual;20-Sinal de saída de parada de emergência 1 - seguro;
    21-Sinal de saída de parada de emergência 2 - seguro;22-Execução/Parada do programa de script LUA;23-Saída de estado seguro - seguro;24-Saída de estado de parada protetiva - seguro;
    25-Robô em movimento - seguro;26-Modo de redução do robô - seguro;27-Modo não reduzido do robô - seguro;28-Robô não parado;29-Erro do robô - erro de ponto de comando;
    30-Erro do robô - erro do driver;31-Erro do robô - erro de limite flexível excedido;32-Erro do robô - erro de colisão;33-Erro do robô - erro no número de escravos ativos;
    34-Erro do robô - erro de escravo;35-Erro do robô - erro de IO;36-Erro do robô - erro da garra;37-Erro do robô - erro de arquivo;38-Erro do robô - erro de pose singular;
    39-Erro do robô - erro de comunicação do driver;40-Erro do robô - erro de parâmetro;41-Erro do robô - erro de limite flexível do eixo externo excedido;42-Aviso do robô - aviso;
    43-Aviso do robô - aviso de porta de segurança;44-Aviso do robô - aviso de movimento;45-Aviso do robô - aviso de área de interferência;46-Aviso do robô - aviso de parede de segurança;
    47-Estado de habilitação;48-Elevação automática por desconexão em andamento;49-Aviso de interferência do cuboide 1;50-Aviso de interferência do cuboide 2;51-Aviso de interferência do cuboide 3;52-Aviso de interferência do cuboide 4;
    * @return Código de erro
    */
    public int GetDOConfig(int[] config)

Definir Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a função da porta End-CI configurável da extremidade
    * @param config Códigos de função End CI0-CI1;
    * 0-Nenhum;1-Interruptor da ferramenta de arrastagem de ensino;2-Sinal de gravação de ponto;3-Alternar manual/automático (sinal de pulso);4-Iniciar/Parar gravação TPD;5-Pausar movimento;
    6-Retomar movimento;7-Iniciar;8-Parar;9-Pausar/Retomar;10-Iniciar/Parar;11-Ativar arrastagem assistida por sensor de força;12-Desativar arrastagem assistida por sensor de força;
    13-Ativar/Desativar arrastagem assistida por sensor de força;14-Sinal de detecção a laser X;15-Sinal de detecção a laser Y;16-Movimento PTP para ponto de operação;17-Interrupção de movimento, parar o movimento atual com base no sinal;
    18-Iniciar programa principal;19-Iniciar rebobinagem;20-Confirmar início;21-Recuperar soldagem;22-Terminar soldagem;23-Limpar erro;24-Alternar manual/automático (nível alto/baixo)
    25-Habilitar;26-Desabilitar;27-Habilitar/Desabilitar;28-Sinal de início/parada de rastreamento servo a laser;
    * @return Código de erro
    */
    public int SetToolDIConfig(int[] config)

Obter Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a função da porta End-CI configurável da extremidade
    * @param config Códigos de função End CI0-CI1;
    * 0-Nenhum;1-Interruptor da ferramenta de arrastagem de ensino;2-Sinal de gravação de ponto;3-Alternar manual/automático (sinal de pulso);4-Iniciar/Parar gravação TPD;5-Pausar movimento;
    6-Retomar movimento;7-Iniciar;8-Parar;9-Pausar/Retomar;10-Iniciar/Parar;11-Ativar arrastagem assistida por sensor de força;12-Desativar arrastagem assistida por sensor de força;
    13-Ativar/Desativar arrastagem assistida por sensor de força;14-Sinal de detecção a laser X;15-Sinal de detecção a laser Y;16-Movimento PTP para ponto de operação;17-Interrupção de movimento, parar o movimento atual com base no sinal;
    18-Iniciar programa principal;19-Iniciar rebobinagem;20-Confirmar início;21-Recuperar soldagem;22-Terminar soldagem;23-Limpar erro;24-Alternar manual/automático (nível alto/baixo)
    25-Habilitar;26-Desabilitar;27-Habilitar/Desabilitar;28-Sinal de início/parada de rastreamento servo a laser;
    * @return Código de erro
    */
    public int GetToolDIConfig(int[] config)
    
Definir Estado Ativo da CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o estado ativo da porta CI configurável do painel de controle
    * @param config Estado ativo das portas CI0-CI7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int SetDIConfigLevel(int[] config)
        
Obter Estado Ativo da CI Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado ativo da porta CI configurável do painel de controle
    * @param config Estado ativo das portas CI0-CI7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int GetDIConfigLevel(int[] config)
        
Definir Estado Ativo da CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o estado ativo da porta CO configurável do painel de controle
    * @param config Estado ativo das portas CO0-CO7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int SetDOConfigLevel(int[] config)

Obter Estado Ativo da CO Configurável do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado ativo da porta CO configurável do painel de controle
    * @param config Estado ativo das portas CO0-CO7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int GetDOConfigLevel(int[] config)
    
Definir Estado Ativo da CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o estado ativo da porta CI configurável da extremidade
    * @param config Estado ativo das portas CI0-CI1; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int SetToolDIConfigLevel(int[] config)
    
Obter Estado Ativo da CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado ativo da porta CI configurável da extremidade
    * @param config Estado ativo das portas CI0-CI1; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int GetToolDIConfigLevel(int[] config)
    
Definir Estado Ativo do DI Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o estado ativo do DI padrão do painel de controle
    * @param config Estado ativo das portas DI0-DI7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int SetStandardDILevel(int[] config)
    
Obter Estado Ativo do DI Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado ativo do DI padrão do painel de controle
    * @param config Estado ativo das portas DI0-DI7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int GetStandardDILevel(int[] config)

Definir Estado Ativo do DO Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o estado ativo do DO padrão do painel de controle
    * @param config Estado ativo das portas DO0-DO7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int SetStandardDOLevel(int[] config)
    
Obter Estado Ativo do DO Padrão do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado ativo do DO padrão do painel de controle
    * @param config Estado ativo das portas DO0-DO7; 0-nível alto ativo; 1-nível baixo ativo
    * @return Código de erro
    */
    public int GetStandardDOLevel(int[] config)
        
Exemplo de Código de Configuração de IO do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    public static int TestIOConfig(Robot robot) {
        int[] setDIConfig = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
        int[] getDIConfig = new int[8];
        int rtn = robot.SetDIConfig(setDIConfig);
        System.out.println("SetDIConfig rtn is " + rtn);
        rtn = robot.GetDIConfig(getDIConfig);
        System.out.println("GetDIConfig rtn is " + rtn + ", value is " + 
            getDIConfig[0] + " " + getDIConfig[1] + " " + getDIConfig[2] + " " + getDIConfig[3] + " " + 
            getDIConfig[4] + " " + getDIConfig[5] + " " + getDIConfig[6] + " " + getDIConfig[7]);

        int[] setDOConfig = new int[]{9, 10, 11, 12, 13, 14, 15, 16};
        int[] getDOConfig = new int[8];
        rtn = robot.SetDOConfig(setDOConfig);
        System.out.println("SetDOConfig rtn is " + rtn);
        rtn = robot.GetDOConfig(getDOConfig);
        System.out.println("GetDOConfig rtn is " + rtn + ", value is " + 
            getDOConfig[0] + " " + getDOConfig[1] + " " + getDOConfig[2] + " " + getDOConfig[3] + " " + 
            getDOConfig[4] + " " + getDOConfig[5] + " " + getDOConfig[6] + " " + getDOConfig[7]);

        int[] setToolDIConfig = new int[]{17, 18};
        int[] getToolDIConfig = new int[2];
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        System.out.println("SetToolDIConfig rtn is " + rtn);
        rtn = robot.GetToolDIConfig(getToolDIConfig);
        System.out.println("GetToolDIConfig rtn is " + rtn + ", value is " + getToolDIConfig[0] + " " + getToolDIConfig[1]);

        int[] setDIConfigLevel = new int[]{1, 1, 1, 1, 0, 0, 0, 0};
        int[] getDIConfigLevel = new int[8];
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        System.out.println("SetDIConfigLevel rtn is " + rtn);
        rtn = robot.GetDIConfigLevel(getDIConfigLevel);
        System.out.println("GetDIConfigLevel rtn is " + rtn + ", value is " + 
            getDIConfigLevel[0] + " " + getDIConfigLevel[1] + " " + getDIConfigLevel[2] + " " + getDIConfigLevel[3] + " " + 
            getDIConfigLevel[4] + " " + getDIConfigLevel[5] + " " + getDIConfigLevel[6] + " " + getDIConfigLevel[7]);

        int[] setDOConfigLevel = new int[]{0, 0, 0, 0, 1, 1, 1, 1};
        int[] getDOConfigLevel = new int[8];
        rtn = robot.SetDOConfigLevel(setDOConfigLevel);
        System.out.println("SetDOConfigLevel rtn is " + rtn);
        rtn = robot.GetDOConfigLevel(getDOConfigLevel);
        System.out.println("GetDOConfigLevel rtn is " + rtn + ", value is " + 
            getDOConfigLevel[0] + " " + getDOConfigLevel[1] + " " + getDOConfigLevel[2] + " " + getDOConfigLevel[3] + " " + 
            getDOConfigLevel[4] + " " + getDOConfigLevel[5] + " " + getDOConfigLevel[6] + " " + getDOConfigLevel[7]);

        int[] setToolDIConfigLevel = new int[]{1, 0};
        int[] getToolDIConfigLevel = new int[2];
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        System.out.println("SetToolDIConfigLevel rtn is " + rtn);
        rtn = robot.GetToolDIConfigLevel(getToolDIConfigLevel);
        System.out.println("GetToolDIConfigLevel rtn is " + rtn + ", value is " + getToolDIConfigLevel[0] + " " + getToolDIConfigLevel[1]);

        int[] setStandardDILevel = new int[]{1, 1, 1, 1, 0, 0, 0, 0};
        int[] getStandardDILevel = new int[8];
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        System.out.println("SetStandardDILevel rtn is " + rtn);
        rtn = robot.GetStandardDILevel(getStandardDILevel);
        System.out.println("GetStandardDILevel rtn is " + rtn + ", value is " + 
            getStandardDILevel[0] + " " + getStandardDILevel[1] + " " + getStandardDILevel[2] + " " + getStandardDILevel[3] + " " + 
            getStandardDILevel[4] + " " + getStandardDILevel[5] + " " + getStandardDILevel[6] + " " + getStandardDILevel[7]);

        int[] setStandardDOLevel = new int[]{0, 0, 0, 0, 1, 1, 1, 1};
        int[] getStandardDOLevel = new int[8];
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        System.out.println("SetStandardDOLevel rtn is " + rtn);
        rtn = robot.GetStandardDOLevel(getStandardDOLevel);
        System.out.println("GetStandardDOLevel rtn is " + rtn + ", value is " + 
            getStandardDOLevel[0] + " " + getStandardDOLevel[1] + " " + getStandardDOLevel[2] + " " + getStandardDOLevel[3] + " " + 
            getStandardDOLevel[4] + " " + getStandardDOLevel[5] + " " + getStandardDOLevel[6] + " " + getStandardDOLevel[7]);

        robot.Sleep(2000);
        return 0;
    }