CNDE
=============

.. toctree:: 
    :maxdepth: 5

Configurar Feedback de Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configura o feedback de estado do robô
    * @param state Lista de enums de estado do robô
    * @param period Período de feedback de estado, intervalo 8-1000
    * @return Código de erro, 0-normal, 4-erro de parâmetro, 18-campo de estado não existe, 20-bytes totais excedem 4K
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> state, int period)
    
Adicionar um Estado do Robô à Configuração de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Adiciona um estado do robô à lista de configuração
    * @param state Enum de estado do robô
    * @return Código de erro, 0-normal, 17-estado já existe, 18-campo de estado não existe, 20-excede 4K
    */
    public int AddRobotRealtimeState(RobotState state)
    
Remover um Estado do Robô da Configuração de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Remove um estado do robô da lista de configuração
    * @param state Enum de estado do robô
    * @return Código de erro, 0-normal, 18-estado não existe, 19-pelo menos um estado deve permanecer
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
Definir Período de Feedback de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o período de feedback de estado CNDE
    * @param period Período de feedback de estado, intervalo 8-1000
    * @return Código de erro, 0-normal, 4-erro de parâmetro
    */
    public int SetRobotRealtimeStatePeriod(int period)
            
Obter o Conjunto Completo de Estados e o Período do Feedback de Estado CNDE Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Obtém todos os conjuntos de estados atuais e o período
     * @return Estrutura de resultado de configuração contendo lista de estados e período
    */
    public StateConfigResult GetRobotRealtimeStateConfig()
                
Exemplo de Código de Uso do Feedback de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Exemplo de uso da interface de configuração de estado em tempo real CNDE
    */
    public static void TestRealtimeStateConfig(Robot robot)
    {
        
        // 1. Criar lista de estados inicial
        List<RobotState> stateList1 = new ArrayList<>();
        stateList1.add(RobotState.ProgramState);
        stateList1.add(RobotState.RobotState);
        stateList1.add(RobotState.JointCurPos);
        stateList1.add(RobotState.ToolCurPos);
        
        // 2. Primeira chamada ao SetRobotRealtimeStateConfig para configurar estados e período
        int period1 = 100;  // Período 100ms
        int rtn = robot.SetRobotRealtimeStateConfig(stateList1, period1);
        System.out.printf("1. SetRobotRealtimeStateConfig (lista inicial, período=%d) rtn: %d%n", period1, rtn);
        
        if (rtn == 0) {
            // 3. Adicionar estado adicional
            rtn = robot.AddRobotRealtimeState(RobotState.RobotTime);
            System.out.printf("2. AddRobotRealtimeState (RobotTime) rtn: %d%n", rtn);
            
            // 4. Chamar SetRobotRealtimeStateConfig novamente para reconfigurar (lista de estados diferente)
            List<RobotState> stateList2 = new ArrayList<>();
            stateList2.add(RobotState.ProgramState);
            stateList2.add(RobotState.RobotState);
            stateList2.add(RobotState.MainCode);
            stateList2.add(RobotState.SubCode);
            stateList2.add(RobotState.JointCurPos);
            stateList2.add(RobotState.ToolCurPos);
            stateList2.add(RobotState.ActualJointTorque);
            
            int period2 = 50;  // Período 50ms
            rtn = robot.SetRobotRealtimeStateConfig(stateList2, period2);
            System.out.printf("3. SetRobotRealtimeStateConfig (lista atualizada, período=%d) rtn: %d%n", period2, rtn);
            
            // 5. Modificar período
            int newPeriod = 80;  // Período 80ms
            rtn = robot.SetRobotRealtimeStatePeriod(newPeriod);
            System.out.printf("4. SetRobotRealtimeStatePeriod (período=%d) rtn: %d%n", newPeriod, rtn);
            
            // 6. Obter configuração atual e imprimir
            Robot.StateConfigResult configResult = robot.GetRobotRealtimeStateConfig();
            System.out.println("5. GetRobotRealtimeStateConfig resultado:");
            System.out.printf("   - Período: %d ms%n", configResult.period);
            System.out.println("   - Estados Configurados:");
            for (int i = 0; i < configResult.stateList.size(); i++) {
                System.out.printf("     [%d] %s%n", i, configResult.stateList.get(i));
            }
            
            rtn = robot.RPC("192.168.58.2");
            if (rtn == 0) {
                System.out.println("conexão rpc bem-sucedida");
            } else {
                System.out.println("conexão rpc falhou");
                return;
            }
            // Aguardar estabelecimento da conexão CNDE
            System.out.println("Aguardando conexão CNDE...");
            while (robot.CNDEGetStateData() == null) {
                robot.Sleep(100);
            }
            System.out.println("Conexão CNDE estabelecida, iniciando recebimento de dados...");

            // 7. Loop para ler estado em tempo real e verificar configuração
            System.out.println("6. Lendo estados em tempo real...");
            while(true) {
                robot.Sleep(1000);
                // Obter dados de estado via CNDE
                ROBOT_STATE_PKG pkg = robot.CNDEGetStateData();
                if (pkg == null) {
                    System.out.println("Dados de estado nulos, conexão CNDE desconectada, aguardando reconexão");
                    continue;  // Continuar loop durante desconexão, aguardando reconexão
                }
                System.out.println("\n--- Tempo do Robô ---");
                if (pkg.robotTime != null) {
                    System.out.println("robotTime: " + pkg.robotTime.year + "-" + pkg.robotTime.month + "-" + pkg.robotTime.day +
                            " " + pkg.robotTime.hour + ":" + pkg.robotTime.minute + ":" + pkg.robotTime.second +
                            "." + pkg.robotTime.millisecond);
                }

                System.out.println("   --- Informações de Estado ---");
                System.out.printf("   program_state: %d%n", pkg.program_state);
                System.out.printf("   robot_state: %d%n", pkg.robot_state);
                System.out.printf("   main_code: %d%n", pkg.main_code);
                System.out.printf("   sub_code: %d%n", pkg.sub_code);
                System.out.println("   --- Posições das Juntas (actual_joint_pos) ---");
                System.out.printf("   jt_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[0], pkg.jt_cur_pos[1], pkg.jt_cur_pos[2]);
                System.out.printf("   jt_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[3], pkg.jt_cur_pos[4], pkg.jt_cur_pos[5]);
                System.out.println("   --- Posições TCP (actual_TCP_pos) ---");
                System.out.printf("   tl_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[0], pkg.tl_cur_pos[1], pkg.tl_cur_pos[2]);
                System.out.printf("   tl_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[3], pkg.tl_cur_pos[4], pkg.tl_cur_pos[5]);
                System.out.println("   --- Torques das Juntas (actual_joint_torque) ---");
                System.out.printf("   jt_cur_tor[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[0], pkg.jt_cur_tor[1], pkg.jt_cur_tor[2]);
                System.out.printf("   jt_cur_tor[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[3], pkg.jt_cur_tor[4], pkg.jt_cur_tor[5]);
                robot.Sleep(500);
            }
        } else {
            System.out.printf("SetRobotRealtimeStateConfig falhou com erro: %d%n", rtn);
        }
    }