Reprodução de Trajetória do Robô
===================================================

.. toctree::
    :maxdepth: 5

Definir Parâmetros de Gravação de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTPDParam(name, period_ms, type=1, di_choose=0, do_choose=0)``"
    "Descrição", "Define os parâmetros de gravação de trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória;
    - ``period_ms``: Período de amostragem, valor fixo, 2ms ou 4ms ou 8ms;"
    "Parâmetros padrão", "- ``type``: Tipo de dado, 1-posição articular;
    - ``di_choose``: Seleção DI, bits 0~7 correspondem a DI0~DI7 da caixa de controle, bits 8~9 correspondem a DI0~DI1 da extremidade, 0-não selecionar, 1-selecionar, padrão 0;
    - ``do_choose``: Seleção DO, bits 0~7 correspondem a DO0~DO7 da caixa de controle, bits 8~9 correspondem a DO0~DO1 da extremidade, 0-não selecionar, 1-selecionar, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Iniciar Gravação de Trajetória
++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTPDStart(name, period_ms, type=1, di_choose=0, do_choose=0)``"
    "Descrição", "Inicia a gravação de trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória;
    - ``period_ms``: Período de amostragem, valor fixo, 2ms ou 4ms ou 8ms;"
    "Parâmetros padrão", "- ``type``: Tipo de dado, 1-posição articular, padrão 1;
    - ``di_choose``: Seleção DI, bits 0~7 correspondem a DI0~DI7 da caixa de controle, bits 8~9 correspondem a DI0~DI1 da extremidade, 0-não selecionar, 1-selecionar, padrão 0;
    - ``do_choose``: Seleção DO, bits 0~7 correspondem a DO0~DO7 da caixa de controle, bits 8~9 correspondem a DO0~DO1 da extremidade, 0-não selecionar, 1-selecionar, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parar Gravação de Trajetória
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWebTPDStop()``"
    "Descrição", "Para a gravação de trajetória"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Excluir Gravação de Trajetória
+++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTPDDelete(name)``"
    "Descrição", "Exclui a gravação de trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código
+++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    robot.SetTPDParam(name, period_ms)
    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(1)
    robot.SetTPDStart(name, period_ms)
    print("SetTPDStart")
    time.sleep(10)
    robot.SetWebTPDStop()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

Pré-carregamento de Trajetória
+++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadTPD(name)``"
    "Descrição", "Pré-carregamento de trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Reprodução de Trajetória
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveTPD(name, blend, ovl)``"
    "Descrição", "Reprodução de trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória
    - ``blend``: Se suaviza, 0-não suaviza, 1-suaviza
    - ``ovl``: Fator de escala de velocidade, intervalo [0~100]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Pose Inicial da Trajetória
+++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTPDStartPose(name)``"
    "Descrição", "Obtém a pose inicial da trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``desc_pose=[x,y,z,rx,ry,rz]``: Pose inicial da trajetória"

Exemplo de Código de Gravação de Trajetória TPD do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    ovl = 100.0
    blend = 0
    rtn = robot.LoadTPD(name)
    print(f"LoadTPD rtn is: {rtn}")
    error, start_pose = robot.GetTPDStartPose(name)
    print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. "
          f"rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
    robot.MoveCart(start_pose, 0, 0, 100, 100)
    time.sleep(1)
    rtn = robot.MoveTPD(name, blend, ovl)
    print(f"MoveTPD rtn is: {rtn}")
    time.sleep(5)
    robot.SetTPDDelete(name)
    robot.CloseRPC()

Pré-processamento de Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadTrajectoryJ(name, ovl, opt=1)``"
    "Descrição", "Pré-processamento de trajetória"
    "Parâmetros obrigatórios", "
    - ``name``: Nome da trajetória, ex.: trajHelix_aima_1.txt, compatível também com nomes de caminho completo, ex.: /fruser/traj/trajHelix_aima_1.txt;
    - ``ovl``: Percentagem de escala de velocidade, intervalo [0~100];"
    "Parâmetros padrão", "- ``opt``: 1-ponto de controle, padrão 1"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Reprodução de Trajetória
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveTrajectoryJ()``"
    "Descrição", "Reprodução de trajetória"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Pose Inicial da Trajetória
++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTrajectoryStartPose(name)``"
    "Descrição", "Obtém a pose inicial da trajetória"
    "Parâmetros obrigatórios", "- ``name``: Nome da trajetória"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``desc_pose=[x,y,z,rx,ry,rz]``: Pose inicial da trajetória"

Obter Número do Ponto de Trajetória
++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTrajectoryPointNum()``"
    "Descrição", "Obtém o número do ponto de trajetória"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``pnum``: Número do ponto de trajetória"

Definir Velocidade Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJSpeed(ovl, mode)``"
    "Descrição", "Define a velocidade durante a execução da trajetória"
    "Parâmetros Obrigatórios", "
    - ``ovl``: Percentual de escala da velocidade, intervalo [0~100]
    - ``mode``: 0-modo de redução de velocidade; 1-comutação direta"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro Sucesso-0 Falha-errcode"

Exemplo de Código para Definir Velocidade Durante a Execução da Trajetória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelecer conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')


    def TestSetTrajectoryJSpeed(self):
        # Carregar arquivo de trajetória
        rtn = robot.TrajectoryJUpLoad("C://Users/lenovo/Desktop/trajHelix_aima_1.txt")
        print(f"Upload TrajectoryJ A {rtn}")

        traj_file_name = "trajHelix_aima_1.txt"
        # Carregar arquivo de trajetória, parâmetros: nome do arquivo, percentual de velocidade, loop (1: loop)
        rtn = robot.LoadTrajectoryJ(name=traj_file_name, ovl=100, opt=1)
        print(f"LoadTrajectoryJ {traj_file_name}, rtn is: {rtn}")

        # Obter pose inicial da trajetória
        rtn, traj_start_pose = robot.GetTrajectoryStartPose(name=traj_file_name)
        print(f"GetTrajectoryStartPose is: {rtn}")
        print(
            f"desc_pos:{traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")

        time.sleep(1)

        # Definir velocidade base e mover para o ponto inicial da trajetória
        robot.SetSpeed(50)
        robot.MoveCart(desc_pos=traj_start_pose, tool=0, user=0, vel=100, acc=100, ovl=100, blendT=-1, config=-1)

        # Obter número de pontos da trajetória
        rtn, traj_num = robot.GetTrajectoryPointNum()
        print(f"GetTrajectoryStartPose rtn is: {rtn}, traj num is: {traj_num}")

        # Iniciar movimento da trajetória
        rtn = robot.MoveTrajectoryJ()
        print(f"MoveTrajectoryJ rtn is: {rtn}")

        time.sleep(1)

        # Obter estado em tempo real do robô
        trajspeedMode = 0
        while True:
            rtn, pkg = robot.GetRobotRealTimeState()
            if pkg.motion_done != 0:
                break

            # Definir velocidade da trajetória para 10%
            rtn = robot.SetTrajectoryJSpeed(ovl=10.0, mode=trajspeedMode)
            print(f"SetTrajectoryJSpeed is: {rtn}")

            time.sleep(1)

            # Definir velocidade da trajetória para 80%
            rtn = robot.SetTrajectoryJSpeed(ovl=80.0, mode=trajspeedMode)
            print(f"SetTrajectoryJSpeed is: {rtn}")

            time.sleep(1)

        # Fechar conexão
        robot.CloseRPC()
        time.sleep(1)


    # Chamar função de teste
    TestSetTrajectoryJSpeed(robot)

Definir Força e Torque Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJForceTorque(ft)``"
    "Descrição", "Define a força e o torque durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``ft=[fx,fy,fz,tx,ty,tz]``: Unidades N e Nm"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Força na Direção X Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJForceFx(fx)``"
    "Descrição", "Define a força na direção X durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``ft``: Força na direção X, unidade N"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Força na Direção Y Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJForceFx(fy)``"
    "Descrição", "Define a força na direção Y durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``fy``: Força na direção Y, unidade N"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Força na Direção Z Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJForceFx(fz)``"
    "Descrição", "Define a força na direção Z durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``fz``: Força na direção Z, unidade N"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Torque em Torno do Eixo X Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJTorqueTx(tx)``"
    "Descrição", "Define o torque em torno do eixo X durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``tx``: Torque em torno do eixo X, unidade Nm"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Torque em Torno do Eixo Y Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJTorqueTx(ty)``"
    "Descrição", "Define o torque em torno do eixo Y durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``ty``: Torque em torno do eixo Y, unidade Nm"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Torque em Torno do Eixo Z Durante a Execução da Trajetória
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTrajectoryJTorqueTx(tz)``"
    "Descrição", "Define o torque em torno do eixo Z durante a execução da trajetória"
    "Parâmetros obrigatórios", "- ``tz``: Torque em torno do eixo Z, unidade Nm"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Upload de Arquivo de Trajetória J
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TrajectoryJUpLoad(filePath)``"
    "Descrição", "Upload de arquivo de trajetória J"
    "Parâmetros obrigatórios", "- ``filePath``: Caminho completo do arquivo de trajetória para upload, C://test/testJ.txt"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Excluir Arquivo de Trajetória J
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TrajectoryJDelete(filePath)``"
    "Descrição", "Exclui arquivo de trajetória J"
    "Parâmetros obrigatórios", "- ``filePath``: Caminho completo do arquivo de trajetória para exclusão, C://test/testJ.txt"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Reprodução de Arquivo de Trajetória J do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "traj.txt"
    rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1)
    print(f"LoadTrajectoryJ {traj_file_name}, rtn is: {rtn}")
    rtn, traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos:{traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},"
          f"{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 50, 100, 100)
    rtn, traj_num = robot.GetTrajectoryPointNum()
    print(f"GetTrajectoryStartPose rtn is: {rtn}, traj num is: {traj_num}")
    rtn = robot.SetTrajectoryJSpeed(50.0)
    print(f"SetTrajectoryJSpeed is: {rtn}")
    traj_force = [0.0,0.0,0.0,0.0,0.0,0.0]
    traj_force[0] = 10  # fx = 10
    rtn = robot.SetTrajectoryJForceTorque(traj_force)
    print(f"SetTrajectoryJForceTorque rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFx(10.0)
    print(f"SetTrajectoryJForceFx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFy(0.0)
    print(f"SetTrajectoryJForceFy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFz(0.0)
    print(f"SetTrajectoryJForceFz rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTx(10.0)
    print(f"SetTrajectoryJTorqueTx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTy(10.0)
    print(f"SetTrajectoryJTorqueTy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTz(10.0)
    print(f"SetTrajectoryJTorqueTz rtn is: {rtn}")
    rtn = robot.MoveTrajectoryJ()
    print(f"MoveTrajectoryJ rtn is: {rtn}")
    robot.CloseRPC()

Pré-processamento de Trajetória (Antecipação de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadTrajectoryLA(name, mode, errorLim, type, precision, vamx, amax, jmax, flag)``"
    "Descrição", "Pré-processamento de trajetória (antecipação de trajetória)"
    "Parâmetros obrigatórios", "- ``name``: Nome do arquivo de trajetória
    - ``mode``: Modo de amostragem, 0-sem amostragem; 1-amostragem por intervalo igual de dados; 2-amostragem por limite de erro igual
    - ``errorLim``: Limite de erro, ativo ao usar aproximação linear
    - ``type``: Modo de suavização, 0-suavização de Bézier
    - ``precision``: Precisão de suavização, ativo ao usar suavização de Bézier
    - ``vamx``: Velocidade máxima definida, mm/s
    - ``amax``: Aceleração máxima definida, mm/s²
    - ``jmax``: Jerk máximo definido, mm/s³
    - ``flag``: Interruptor de ativação da antecipação de velocidade constante, 0-não ativar; 1-ativar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Reprodução de Trajetória (Antecipação de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveTrajectoryLA()``"
    "Descrição", "Reprodução de trajetória (antecipação de trajetória)"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Reprodução de Trajetória (Antecipação de Trajetória)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "traj.txt"
    rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 50, 200, 1000, 0)
    print(f"LoadTrajectoryLA {traj_file_name}, rtn is: {rtn}")
    rtn, traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos: {traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100)
    rtn = robot.MoveTrajectoryLA()
    print(f"MoveTrajectoryLA rtn is: {rtn}")
    robot.CloseRPC()

Mover para o Ponto Inicial da Gravação da Trajetória TPD
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToTPDStart(name, moveType, ovl)``"
    "Descrição", "Mover para o ponto inicial da gravação da trajetória TPD"
    "Parâmetros obrigatórios", "
    - ``name``: Nome do arquivo de trajetória
    - ``moveType``: Tipo de movimento; 0-PTP; 1-LIN
    - ``ovl``: Percentagem de escala de velocidade, intervalo [0~100]
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK para Mover para o Ponto Inicial da Gravação da Trajetória TPD
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # A connection is established with the robot controller. A successful connection returns a robot object
    # Estabelece conexão com o controlador do robô. Uma conexão bem-sucedida retorna um objeto robô
    robot = Robot.RPC('192.168.58.2')
    import time

    def TestTPD(self):
        type = 1
        name = "tpd2025"
        period_ms = 4
        di_choose = 0
        do_choose = 0

        robot.SetTPDParam(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)

        robot.Mode(1)
        time.sleep(1)
        robot.DragTeachSwitch(1)
        robot.SetTPDStart(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)
        time.sleep(3)
        robot.SetWebTPDStop()
        robot.DragTeachSwitch(0)

        time.sleep(1)
        ovl = 100.0
        blend = 0
        start_pose = [0.0] * 6
        rtn = robot.LoadTPD(name)
        print(f"LoadTPD rtn is: {rtn}")

        rtn, start_pose = robot.GetTPDStartPose(name)
        print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
        # robot.MoveCart(desc_pos=start_pose, tool=0, user=0, vel=100, acc=100, ovl=ovl, blendT=-1, config=-1)
        # time.sleep(1)

        rtn = robot.MoveToTPDStart(name, 0, 100)
        print(f"MoveToTPDStart rtn is: {rtn}")

        rtn = robot.MoveTPD(name, blend, ovl)
        print(f"MoveTPD rtn is: {rtn}")
        time.sleep(5)

        robot.SetTPDDelete(name)

        robot.CloseRPC()
        return 0

    TestTPD(robot)