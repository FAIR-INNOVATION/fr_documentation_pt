CNDE
=================

.. toctree:: 
    :maxdepth: 5

Configurar a Lista de Dados CNDE do Robô e o Período de Atualização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Configura a lista de dados e o período de atualização para o feedback de estado em tempo real do robô (sobrescreve a configuração anterior)
    * @param [in] states Lista de enums de estado a serem assinados, a ordem determina a disposição no pacote de dados
    * @param [in] period Período de atualização de dados, unidade milissegundos, intervalo de valores [8, 1000]
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha (ex. ERR_STATE_INVALID, ERR_PARAM_VALUE, etc.)
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> states, int period)

Adicionar um Item de Estado à Lista de Feedback de Estado Existente
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Adiciona um item de estado à lista de feedback de estado existente
    * @param [in] state Valor enum do estado a ser adicionado
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha (ex. ERR_STATE_ALREADY_EXISTS, ERR_STATE_INVALID, etc.)
    */
    public int AddRobotRealtimeState(RobotState state)
    
Remover um Item de Estado da Lista de Feedback de Estado Existente
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Remove um item de estado da lista de feedback de estado existente (pelo menos um estado deve permanecer)
    * @param [in] state Valor enum do estado a ser removido
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha (ex. ERR_STATE_INVALID, ERR_NEED_AT_LEAST_ONE_STATE)
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
Modificar Apenas o Período de Atualização do Feedback de Estado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
    * @brief Modifica apenas o período de atualização do feedback de estado sem alterar a lista de estados
    * @param [in] period Novo período de atualização, unidade milissegundos, intervalo de valores [8, 1000]
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha (ex. ERR_PARAM_VALUE)
    */
    public int SetRobotRealtimeStatePeriod(int period)
        
Obter a Lista de Feedback de Estado e o Período de Atualização Atualmente Configurados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a lista de feedback de estado e o período de atualização atualmente configurados
    * @param [out] states Retorna a lista de enums de estado atualmente assinados
    * @param [out] period Retorna o período de atualização de dados atual, unidade milissegundos
    * @return Retorna 0 em caso de sucesso; retorna um código de erro negativo em caso de falha
    */
    public int GetRobotRealtimeStateConfig(out List<RobotState> states, out int period)

Exemplo de Código SDK Relacionado à Configuração CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestRobotRealtimeStates()
    {
        // 1. Definir os campos de estado a serem assinados
        List<RobotState> requiredStates = new List<RobotState>
        {
            RobotState.JointCurPos,
            RobotState.ToolCurPos, 
            RobotState.JointDriverTemperature,
            RobotState.RobotTime,
        };

        // 2. Configurar o feedback de estado (período 8ms)
        int periodMs = 8;
        int ret = robot.SetRobotRealtimeStateConfig(requiredStates, periodMs);
        if (ret != 0)
        {
            Console.WriteLine($"Falha na configuração de estado, código de erro: {ret}");
            return;
        }
        Console.WriteLine($"Configuração de estado bem-sucedida, {requiredStates.Count} campos, período {periodMs} ms");

        // Verificar se a configuração foi aplicada
        List<RobotState> actualStates;
        int actualPeriod;
        robot.GetRobotRealtimeStateConfig(out actualStates, out actualPeriod);
        Console.WriteLine($"Número de estados efetivamente ativos: {actualStates.Count}, período: {actualPeriod} ms");
        Thread.Sleep(3000);
        // 3. Estabelecer conexão RPC (internamente conclui automaticamente o handshake CNDE)
        robot.SetReconnectParam(true, 10, 1000);
        ret = robot.RPC("192.168.58.2");  // Modificar de acordo com o IP real do robô
        if (ret != 0)
        {
            Console.WriteLine($"Falha na conexão RPC, código de erro: {ret}");
            return;
        }
        // 4. Loop para ler e imprimir os dados de estado
        DateTime startTime = DateTime.Now;
        const int durationSeconds = 500;

        while ((DateTime.Now - startTime).TotalSeconds < durationSeconds)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            ret = robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"GetRobotRealTimeState: {ret}");

            //Posições das juntas (graus)
            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
                Console.WriteLine($"Posições das juntas(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");

            //Pose TCP (mm /°)
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
                Console.WriteLine($"Pose TCP(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
    
            // Temperaturas das juntas
            if (pkg.jointDriverTemperature != null && pkg.jointDriverTemperature.Length >= 6)
                Console.WriteLine($"Temperaturas das juntas(°C): J1={pkg.jointDriverTemperature[0]:F2}, J2={pkg.jointDriverTemperature[1]:F2}, J3={pkg.jointDriverTemperature[2]:F2}, J4={pkg.jointDriverTemperature[3]:F2}, J5={pkg.jointDriverTemperature[4]:F2}, J6={pkg.jointDriverTemperature[5]:F2}");

            // Hora do robô
            Console.WriteLine($"Hora do robô: {pkg.robotTime.year}-{pkg.robotTime.mouth:D2}-{pkg.robotTime.day:D2} {pkg.robotTime.hour:D2}:{pkg.robotTime.minute:D2}:{pkg.robotTime.second:D2}.{pkg.robotTime.millisecond:D3}");

            await Task.Delay(100);
        }

        // 5. Desconectar
        robot.CloseRPC();
    }

Exemplo de Código SDK para Adicionar/Remover Estado CNDE e Definir Período de Comunicação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestAddDeleteCNDE()
    {
        List<RobotState> finalStates;
        int finalPeriod;
        // Configuração inicial: não solicitar nenhum estado (configuração padrão)
        List<RobotState> emptyStates = new List<RobotState>();
        int ret = robot.SetRobotRealtimeStateConfig(emptyStates, 20);

        robot.SetRobotRealtimeStatePeriod(10);
        // Remover dois estados
        ret = robot.DeleteRobotRealtimeState(RobotState.JointCurPos);
        Console.WriteLine($"Remoção de JointCurPos resultado: {ret}");
        ret = robot.DeleteRobotRealtimeState(RobotState.ToolCurPos);
        Console.WriteLine($"Remoção de ToolCurPos resultado: {ret}");
        // Adicionar um estado
        ret = robot.AddRobotRealtimeState(RobotState.CollisionLevel);
        Console.WriteLine($"Adição de CollisionLevel resultado: {ret}");

        // Obter a lista de configuração atual e reenviar
        List<RobotState> currentStates;
        int currentPeriod;
        robot.GetRobotRealtimeStateConfig(out currentStates, out currentPeriod);
        Console.WriteLine($"Número de estados de configuração atual: {currentStates.Count}");
        ret = robot.SetRobotRealtimeStateConfig(currentStates, currentPeriod);
        Console.WriteLine($"Aplicação da nova configuração resultado: {ret}"); Console.WriteLine($"Configuração inicial resultado: {ret}");
        robot.GetRobotRealtimeStateConfig(out finalStates, out finalPeriod);
        Console.WriteLine($"Número de estados de configuração: {finalStates.Count}");
        foreach (var s in finalStates) Console.WriteLine($"  {s}");
        Console.WriteLine($"Período: {finalPeriod} ms");

        Thread.Sleep(1000);
        // Estabelecer conexão RPC (internamente conecta automaticamente ao CNDE)
        robot.SetReconnectParam(true, 100, 1000);
        ret = robot.RPC("192.168.58.2");
        if (ret != 0)
        {
            Console.WriteLine($"Falha na conexão RPC: {ret}");
            return;
        }

        // Loop para imprimir os estados removidos e adicionados, estados removidos são impressos como 0, estados adicionados podem obter valores em tempo real normalmente
        DateTime lastTime = DateTime.Now;
        int frameCount = 0;
        DateTime startTime = DateTime.Now;
        while ((DateTime.Now - startTime).TotalSeconds < 10)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.GetRobotRealTimeState(ref pkg);
            DateTime now = DateTime.Now;
            double interval = (now - lastTime).TotalMilliseconds;
            lastTime = now;
            frameCount++;

            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  Posições das juntas(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");
            }
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  Pose TCP(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
            }
            // Nível de colisão
            if (pkg.collisionLevel != null && pkg.collisionLevel.Length >= 6)
                Console.WriteLine($"Nível de colisão: J1={pkg.collisionLevel[0]}, J2={pkg.collisionLevel[1]}, J3={pkg.collisionLevel[2]}, J4={pkg.collisionLevel[3]}, J5={pkg.collisionLevel[4]}, J6={pkg.collisionLevel[5]}");

            await Task.Delay(50);
        }
        //Desconectar
        robot.CloseRPC();
        Console.WriteLine("Teste concluído.");
    }