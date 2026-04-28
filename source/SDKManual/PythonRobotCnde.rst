CNDE
=============

.. toctree:: 
    :maxdepth: 5

Configurar Feedback de Estado CNDE do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotRealtimeStateConfig(states: List[RobotState], period: int = 500) -> int:``"
    "Descrição", "Define a configuração padrão do CNDE (chamar antes da conexão RPC)"
    "Parâmetros Obrigatórios", "
    - ``states``: Lista de enums RobotState
    - ``period``: Período de dados (ms), intervalo 8-1000, padrão 8ms
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro Sucesso-0 Falha-errcode"

Adicionar Estado do Robô à Configuração de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AddRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "Descrição", "Adiciona lista de estados CNDE com base na configuração existente (suporta manutenção dinâmica e isolamento IP)"
    "Parâmetros Obrigatórios", "
    - ``states``: Lista de enums RobotState, estados a adicionar
    - ``ip``: Opcional, especifica o IP do robô (para configuração isolada multi-robô; se não fornecido, modifica a configuração global)
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro Sucesso-0 Falha-errcode"

Remover Estado do Robô da Configuração de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``DeleteRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "Descrição", "Remove lista de estados CNDE com base na configuração existente (suporta manutenção dinâmica e isolamento IP)"
    "Parâmetros Obrigatórios", "
    - ``states``: Lista de enums RobotState, estados a remover
    - ``ip``: Opcional, especifica o IP do robô (para configuração isolada multi-robô; se não fornecido, modifica a configuração global)
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro Sucesso-0 Falha-errcode"

Definir Período de Feedback de Estado CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotRealtimeStatePeriod(period: int, ip: str = None) -> int:``"
    "Descrição", "Define o período de feedback de estado CNDE (suporta configuração global ou isolada por IP)"
    "Parâmetros Obrigatórios", "
    - ``period``: Período de dados (ms), intervalo 8-1000
    - ``ip``: Opcional, especifica o IP do robô (se não fornecido, modifica a configuração global)
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro Sucesso-0 Falha-errcode"

Obter o Conjunto Completo de Estados do Feedback de Estado CNDE Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CNDEGetConfig(self) -> tuple:``"
    "Descrição", "Obtém todos os conjuntos de estados atuais"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro Sucesso-0 Falha-errcode Estrutura de resultado de configuração contendo lista de estados"

Exemplo de Código de Uso do Feedback de Estado CNDE
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    from fairino.Robot import RobotState, SetRobotRealtimeStateConfig, DEFAULT_CNDE_STATES, AddRobotRealtimeState, DeleteRobotRealtimeState, SetRobotRealtimeStatePeriod
    import time

    # ==================== Parâmetros de Configuração Global ====================
    ROBOT_IP = '192.168.58.2'       # Endereço IP do robô
    # ========== Test1: Teste de Configuração CNDE e Aquisição de Dados =============
    # Etapas do teste:
    # 1. Definir configuração CNDE (JointCurPos, ToolCurPos, período 20ms)
    # 2. Estabelecer conexão RPC
    # 3. Imprimir dados de posições das juntas e pose TCP do robô
    # 4. Obter timestamp e verificar período
    # 5. Modificar configuração (RobotMode, RbtEnableState, período 10ms)
    # 6. Verificar se a nova configuração entrou em vigor

    def test1_cnde_config_and_data():
        """Test1: Teste de configuração CNDE e aquisição de dados - verificar configurações e tempo real dos dados"""
        print_separator("Test1: Teste de configuração CNDE e aquisição de dados")

        # ===== Passo 1: Definir configuração CNDE (JointCurPos, ToolCurPos, 20ms) =====
        print("\n[Passo 1] Definindo configuração CNDE...")
        print("  Campos de configuração: JointCurPos, ToolCurPos")
        print("  Período de feedback: 20ms")

        custom_states = [
            RobotState.JointCurPos,   # Posição atual da junta
            RobotState.ToolCurPos,    # Posição atual da ferramenta (TCP)
        ]

        rtn = SetRobotRealtimeStateConfig(custom_states, 20)
        if rtn != 0:
            print(f"✗ Falha ao definir configuração, código de erro: {rtn}")
            return None
        print("✓ Configuração CNDE definida com sucesso")

        # ===== Passo 2: Estabelecer conexão RPC =====
        print(f"\n[Passo 2] Estabelecendo conexão RPC ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # Aguardar conexão e recepção de dados

        # Verificar configuração
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ Conexão bem-sucedida, configuração atual: {len(states)} campos, período {period}ms")
        else:
            print("✗ Não foi possível obter a configuração CNDE")
            return robot

        # ===== Passo 3: Imprimir posições das juntas e pose TCP do robô =====
        print("\n[Passo 3] Imprimindo posições das juntas e pose TCP do robô...")
        print("  (Dica: Arraste o robô para observar as mudanças nos dados)")
        print("  Pressione Ctrl+C para interromper a impressão dos dados")
        print("  (Use o Wireshark para capturar pacotes e verificar o período real dos dados)\n")

        sample_count = 0
        try:
            while sample_count < 100:  # Coletar 100 amostras
                pkg = robot.robot_state_pkg

                # Imprimir a cada 10 quadros
                if sample_count % 10 == 0:
                    print(f"--- Amostra #{sample_count} ---")
                    print(f"  Posições das juntas (deg): [{', '.join([f'{x:.3f}' for x in pkg.jt_cur_pos])}]")
                    print(f"  Pose TCP (mm/deg): [{', '.join([f'{x:.3f}' for x in pkg.tl_cur_pos])}]")
                    print(f"  Contagem de quadros atual: {pkg.frame_cnt}")
                    print()

                sample_count += 1
                time.sleep(0.02)  # 20ms

        except KeyboardInterrupt:
            print("\n  Impressão de dados interrompida pelo usuário")

        # Fechar conexão
        robot.CloseRPC()
        time.sleep(1)

        # ===== Passo 4: Modificar configuração e verificar =====
        print("\n[Passo 4] Modificando configuração CNDE...")
        print("  Novos campos de configuração: RobotMode, RbtEnableState")
        print("  Novo período de feedback: 10ms")

        new_states = [
            RobotState.RobotMode,
            RobotState.RbtEnableState,
        ]

        # Definir nova configuração
        rtn = SetRobotRealtimeStateConfig(new_states, 10)
        if rtn != 0:
            print(f"✗ Falha ao definir nova configuração, código de erro: {rtn}")
            return robot
        print("✓ Nova configuração definida com sucesso")

        # Reconectar
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # Verificar nova configuração
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ Configuração atual: {[s.name for s in states]}")
            print(f"✓ Período atual: {period}ms")

            if period == 10:
                print("✓ Verificação de modificação de configuração aprovada (período alterado para 10ms)")
            else:
                print(f"⚠ Período não生效 (esperado 10ms, atual {period}ms)")

            # Imprimir novos dados
            pkg = robot.robot_state_pkg
            print(f"\n[Novos Dados de Configuração]")
            print(f"  robot_mode: {pkg.robot_mode}")
            print(f"  rbtEnableState: {pkg.rbtEnableState}")
        else:
            print("✗ Não foi possível obter a nova configuração")

        print("\n✓ Test1 concluído")
        return robot


    if __name__ == "__main__":
        test1_cnde_config_and_data()


    # ======== Test2: Teste de Adição/Remoção de Campos de Estado ====================
    # Função: Testar AddRobotRealtimeState() e DeleteRobotRealtimeState()
    # Etapas do teste:
    #   1. Usar AddRobotRealtimeState() para adicionar SpeedScaleManual e SpeedScaleAuto
    #   2. Conectar ao robô, imprimir velocidade global nos modos manual/automático
    #   3. Modificar a velocidade global no WebApp e observar as mudanças nos dados do SDK
    #   4. Usar DeleteRobotRealtimeState() para remover os campos adicionados
    #   5. Reconectar e verificar se os valores de velocidade são 0 (campos não são mais atualizados)


    def test2_add_delete_state():
        """Test2: Teste de adição/remoção de campos de estado - verificar adição e remoção dinâmica de estados CNDE"""
        print_separator("Test2: Teste de adição/remoção de campos de estado")

        # ===== Passo 1: Adicionar campos SpeedScaleManual e SpeedScaleAuto =====
        print("\n[Passo 1] Usando AddRobotRealtimeState() para adicionar campos de escala de velocidade...")
        print("  Campos adicionados: SpeedScaleManual, SpeedScaleAuto")

        rtn = AddRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ Falha na adição de campos, código de erro: {rtn}")
            return None
        print("✓ Campos adicionados com sucesso")

        # ===== Passo 2: Estabelecer conexão RPC e imprimir velocidade =====
        print(f"\n[Passo 2] Estabelecendo conexão RPC ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # Aguardar conexão e recepção de dados

        # Verificar configuração
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ Conexão bem-sucedida, configuração atual: {len(states)} campos")
            # Verificar se os campos adicionados estão incluídos
            has_manual = RobotState.SpeedScaleManual in states
            has_auto = RobotState.SpeedScaleAuto in states
            if has_manual and has_auto:
                print("✓ Verificação de configuração aprovada: SpeedScaleManual e SpeedScaleAuto foram adicionados")
            else:
                print(f"⚠ Aviso de verificação de configuração: Manual={has_manual}, Auto={has_auto}")
        else:
            print("✗ Não foi possível obter a configuração CNDE")

        # Imprimir dados de velocidade
        print("\n[Dados de Velocidade Atuais] (Modifique a velocidade global no WebApp para observar as mudanças)")
        print("  Dica: Habilite o robô arrastando-o e alterne entre modos manual/automático para observar os valores de velocidade")
        print("  Pressione Ctrl+C para interromper a impressão dos dados\n")

        sample_count = 0
        try:
            while sample_count < 100:  # Coletar 100 amostras (cerca de 10 segundos em intervalos de 100ms)
                pkg = robot.robot_state_pkg
                print(f"  [{sample_count:3d}] SpeedScaleManual: {pkg.speedScaleManual:.2f}, "
                    f"SpeedScaleAuto: {pkg.speedScaleAuto:.2f}, "
                    f"Mode: {pkg.robot_mode}")
                sample_count += 1
                time.sleep(0.1)  # Intervalo de 100ms
        except KeyboardInterrupt:
            print("\n  Impressão de dados interrompida pelo usuário")

        print(f"\n✓ Coleta de dados concluída, total de {sample_count} amostras")

        # ===== Passo 3: Desconectar =====
        print("\n[Passo 3] Desconectando conexão atual...")
        robot.CloseRPC()
        time.sleep(1.0)  # Aguardar o fechamento completo do CNDE

        # ===== Passo 4: Remover campos adicionados =====
        print("\n[Passo 4] Usando DeleteRobotRealtimeState() para remover campos de escala de velocidade...")
        rtn = DeleteRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ Falha na remoção de campos, código de erro: {rtn}")
            return robot
        print("✓ Campos removidos com sucesso")

        # ===== Passo 5: Reconectar e verificar se os valores dos campos são 0 =====
        print(f"\n[Passo 5] Reconectando e verificando os valores dos campos após remoção...")

        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # Ler valores de velocidade
        pkg = robot.robot_state_pkg
        manual_speed = pkg.speedScaleManual
        auto_speed = pkg.speedScaleAuto

        print(f"\n  SpeedScaleManual após remoção: {manual_speed:.2f}")
        print(f"  SpeedScaleAuto após remoção: {auto_speed:.2f}")

        # Verificar se são 0
        if manual_speed == 0 and auto_speed == 0:
            print("\n✓ Test2 verificação aprovada: valores de velocidade são 0 após a remoção dos campos")
        else:
            print(f"\n⚠ Test2 aviso: valores de velocidade não são zero após a remoção dos campos")

        print("\n✓ Test2 concluído")
        return robot

    if __name__ == "__main__":
        test2_add_delete_state()