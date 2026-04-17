Configurações de Segurança do Robô
===============================================

.. toctree:: 
    :maxdepth: 5

Definir Nível de Colisão
+++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAnticollision (mode,level,config)``"
    "Descrição", "Define o nível de colisão"
    "Parâmetros Obrigatórios", "- ``mode``: 0-nível, 1-porcentagem;
    - ``level=[j1,j2,j3,j4,j5,j6]``: Limiar de colisão;
    - ``config``: 0-não atualizar arquivo de configuração, 1-atualizar arquivo de configuração"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Estratégia Pós-Colisão
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetCollisionStrategy(strategy,safeTime,safeDistance,safeVel,safetyMargin)``"
    "Descrição", "Define a estratégia pós-colisão"
    "Parâmetros Obrigatórios", "- ``strategy``: 0-reportar erro e pausar, 1-continuar executando, 2-reportar erro e parar, 3-modo de torque gravitacional, 4-modo de resposta oscilatória, 5-modo de ricochete pós-colisão"
    "Parâmetros Padrão", "- ``safeTime``: Tempo de parada segura [1000-2000] ms, padrão: 1000
    - ``safeDistance``: Distância de parada segura [1-150] mm, padrão: 100
    - ``safeVel``: Velocidade de parada segura [50-250] mm/s, padrão: 250
    - ``safetyMargin[6]``: Fator de segurança [1-10], padrão: [10,10,10,10,10,10]"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Início da Função de Limite de Detecção de Colisão Personalizado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CustomCollisionDetectionStart(flag, jointDetectionThreshould, tcpDetectionThreshould, block)``"
    "Descrição", "Início da função de limite de detecção de colisão personalizado. Define os limites de detecção de colisão para as juntas e o TCP."
    "Parâmetros Obrigatórios", "- ``flag``: 1-ativa apenas detecção de juntas; 2-ativa apenas detecção de TCP; 3-ativa detecção de juntas e TCP simultaneamente
    - ``jointDetectionThreshould``: Limiares de detecção de colisão das juntas j1-j6
    - ``tcpDetectionThreshould``: Limiares de detecção de colisão do TCP, xyzabc
    - ``block``: 0-não bloqueante; 1-bloqueante"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"

Fim da Função de Limite de Detecção de Colisão Personalizado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CustomCollisionDetectionEnd()``"
    "Descrição", "Desativa a função de limite de detecção de colisão personalizado"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Configuração do Nível de Colisão do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    mode = 0
    config = 1
    level1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    level2 = [50.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    rtn = robot.SetAnticollision(mode, level1, config)
    print(f"SetAnticollision mode 0 rtn is {rtn}")
    mode = 1
    rtn = robot.SetAnticollision(mode, level2, config)
    print(f"SetAnticollision mode 1 rtn is {rtn}")
    p1Joint = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    p2Joint = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100, blendR=2)
    robot.ResetAllError()
    safety = [5, 5, 5, 5, 5, 5]
    rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety)
    print(f"SetCollisionStrategy rtn is {rtn}")
    jointDetectionThreshould = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    tcpDetectionThreshould = [60, 60, 60, 60, 60, 60]
    rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0)
    print(f"CustomCollisionDetectionStart rtn is {rtn}")
    robot.MoveL(desc_pos=p1Desc, tool=0, user=0, vel=100)
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100)
    rtn = robot.CustomCollisionDetectionEnd()
    print(f"CustomCollisionDetectionEnd rtn is {rtn}")
    robot.CloseRPC()

Definir Limite Positivo
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetLimitPositive(p_limit)``"
    "Descrição", "Define o limite positivo"
    "Parâmetros Obrigatórios", "- ``p_limit=[j1,j2,j3,j4,j5,j6]``: Posições das seis juntas"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Limite Negativo
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetLimitNegative(n_limit)``"
    "Descrição", "Define o limite negativo"
    "Parâmetros Obrigatórios", "- ``n_limit=[j1,j2,j3,j4,j5,j6]``: Posições das seis juntas"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Ângulos dos Limites Flexíveis das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetJointSoftLimitDeg(flag=1)``"
    "Descrição", "Obtém os ângulos dos limites flexíveis das juntas"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "``flag``: 0-bloqueante, 1-não bloqueante. Padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``[j1min,j1max,j2min,j2max,j3min,j3max, j4min,j4max,j5min, j5max, j6min,j6max]``: Eixos 1 a 6, limite negativo e positivo das juntas, unidade [mm]"

Exemplo de Código para Configuração de Limites do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    plimit = [170.0, 80.0, 150.0, 80.0, 170.0, 160.0]
    robot.SetLimitPositive(plimit)
    nlimit = [-170.0, -260.0, -150.0, -260.0, -170.0, -160.0]
    robot.SetLimitNegative(nlimit)
    error,neg_deg = robot.GetJointSoftLimitDeg(0)
    print(f"pos limit deg: {neg_deg[1]}, {neg_deg[3]}, {neg_deg[5]}, {neg_deg[7]}, {neg_deg[9]}, {neg_deg[11]}")
    print(f"neg limit deg: {neg_deg[0]}, {neg_deg[2]}, {neg_deg[4]}, {neg_deg[6]}, {neg_deg[8]}, {neg_deg[10]}")
    robot.CloseRPC()

Definir Método de Detecção de Colisão do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetCollisionDetectionMethod(method, thresholdMode)``"
    "Descrição", "Define o método de detecção de colisão do robô"
    "Parâmetros Obrigatórios", "
    - ``method``: Método de detecção de colisão: 0-modo corrente; 1-duplo encoder; 2-corrente e duplo encoder simultaneamente
    - ``thresholdMode``: Modo de limiar do nível de colisão; 0-modo de limiar fixo do nível de colisão; 1-limite de detecção de colisão personalizado  
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"

Ativar/Desativar Detecção de Colisão Estática
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetStaticCollisionOnOff(status)``"
    "Descrição", "Ativa/desativa a detecção de colisão estática"
    "Parâmetros Obrigatórios", "
    - ``status``: 0-desativar; 1-ativar
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Definir Método de Detecção de Colisão do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetCollisionDetectionMethod(0,0)
    rtn = robot.SetStaticCollisionOnOff(1)
    print(f"SetStaticCollisionOnOff On rtn is {rtn}")
    time.sleep(5)
    rtn = robot.SetStaticCollisionOnOff(0)
    print(f"SetStaticCollisionOnOff Off rtn is {rtn}")
    robot.CloseRPC()

Detecção de Potência do Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetPowerLimit(status, power)``"
    "Descrição", "Detecção de potência do torque das juntas"
    "Parâmetros Obrigatórios", "
    - ``status``: 0-desativar; 1-ativar
    - ``power``: Potência máxima definida (W)
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"
    
Exemplo de Código para Detecção de Potência do Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    robot.SetPowerLimit(1, 200)
    error,torques = robot.GetJointTorques(1)
    count = 100
    robot.ServoJTStart()
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)  # atraso de 1ms
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

Definir Parâmetros de Velocidade Segura
++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetVelReducePara(enable, maxTCPVel, strategy)``"
    "Descrição", "Define os parâmetros de velocidade segura"
    "Parâmetros Obrigatórios", "
    - ``enable``: 0-desativar; 1-ativar no modo manual; 2-ativar em todos os modos (não suporta limitação automática de velocidade)
    - ``maxTCPVel``: Limitar a velocidade TCP máxima; [0-1000] mm/s
    - ``strategy``: Estratégia após excesso de velocidade; 0-parar e alarmar; 1-limitar velocidade automaticamente; 2-parar, alarmar e desabilitar
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código SDK para Definir Parâmetros de Velocidade Segura
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestSetVelReducePara(self):
        # Inicializa posições articulares, eixo externo e deslocamento
        j1 = [0, -90, 90, 0, 0, 0]
        j2 = [90, -90, 90, 0, 0, 0]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        # Define a velocidade base
        robot.SetSpeed(80)

        # Testa caso de parâmetro inválido (mode=2 é inválido?)
        rtn = robot.SetVelReducePara(2, 30, 1)
        print(f"SetVelReducePara param error rtn is {rtn}")

        # Desativa a função de redução de velocidade (mode=0, action=1)
        rtn = robot.SetVelReducePara(0, 30, 1)
        print(f"SetVelReducePara disable reduce vel rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Ativa a função de redução de velocidade (mode=1, action=1)
        rtn = robot.SetVelReducePara(1, 30, 1)
        print(f"SetVelReducePara reduce vel rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Testa action=2 (pode indicar parada de emergência ou desabilitação do robô)
        rtn = robot.SetVelReducePara(2, 30, 2)
        print(f"SetVelReducePara disable robot rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Aguarda, reseta erros e reabilita o robô
        time.sleep(2)
        robot.ResetAllError()
        robot.RobotEnable(1)
        time.sleep(1)

        # Testa action=0 (pode indicar apenas relatar erro, sem executar ação)
        rtn = robot.SetVelReducePara(2, 30, 0)
        print(f"SetVelReducePara report error rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Fecha a conexão
        robot.CloseRPC()

    TestSetVelReducePara(robot)