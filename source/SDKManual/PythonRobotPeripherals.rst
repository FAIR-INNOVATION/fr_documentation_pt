Periféricos do Robô
========================

.. toctree:: 
    :maxdepth: 5

Configurar Garra
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "Descrição", "Configura a garra"
    "Parâmetros Obrigatórios", "- ``company``: Fabricante da garra, 1-Robotiq, 2-Huiling, 3-Tianji, 4-Dahuan, 5-Zhixing;
    - ``device``: Número do dispositivo, Robotiq(0-2F-85 series), Huiling(0-NK series,1-Z-EFG-100), Tianji(0-TEG-110), Dahuan(0-PGI-140), Zhixing(0-CTPM2F20)"
    "Parâmetros Padrão", "- ``softversion``: Número da versão do software, não usado no momento, padrão 0;
    - ``bus``: Posição do barramento onde o dispositivo está montado, não usado no momento, padrão 0;"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Obter Configuração da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperConfig()``"
    "Descrição", "Obtém a configuração da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``[number,company,device,softversion]``: number, número da garra; company, fabricante da garra, 1-Robotiq, 2-Huiling, 3-Tianji, 4-Dahuan, 5-Zhixing; device, número do dispositivo, Robotiq(0-2F-85 series), Huiling(0-NK series,1-Z-EFG-100), Tianji(0-TEG-110), Dahuan(0-PGI-140), Zhixing(0-CTPM2F20); softvesion, número da versão do software, não usado no momento, padrão 0."

Ativar Garra
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ActGripper(index,action)``"
    "Descrição", "Ativa a garra"
    "Parâmetros Obrigatórios", "- ``index``: Número da garra;
    - ``action``: 0-reset, 1-ativar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Controlar Garra
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "Descrição", "Controla a garra"
    "Parâmetros Obrigatórios", "- ``index``: Número da garra;
    - ``pos``: Porcentagem de posição, faixa [0~100];
    - ``vel``: Porcentagem de velocidade, faixa [0~100];
    - ``force``: Porcentagem de torque, faixa [0~100];
    - ``maxtime``: Tempo máximo de espera, faixa [0~30000], unidade [ms];
    - ``block``: 0-bloqueado, 1-não bloqueado;
    - ``type``: Tipo de garra, 0-garra paralela; 1-garra rotativa;
    - ``rotNum``: Número de rotações;
    - ``rotVel``: Porcentagem de velocidade de rotação [0-100];
    - ``rotTorque``: Porcentagem de torque de rotação [0-100]."
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Obter Estado de Movimento da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperMotionDone()``"
    "Descrição", "Obtém o estado de movimento da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``[fault,status]``: Estado de movimento da garra, fault:0-sem erro, 1-com erro; status:0-movimento não concluído, 1-movimento concluído"

Obter Estado de Ativação da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperActivateStatus()``"
    "Descrição", "Obtém o estado de ativação da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``gripper_active``: bit0~bit15 correspondem aos números das garras 0~15, bit=0 não ativado, bit=1 ativado"

Obter Posição da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperCurPosition()``"
    "Descrição", "Obtém a posição da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``position``: Porcentagem de posição, faixa 0~100%"

Obter Velocidade da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperCurSpeed()``"
    "Descrição", "Obtém a velocidade da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``speed``: Porcentagem de velocidade, faixa 0~100%"

Obter Corrente da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperCurCurrent()``"
    "Descrição", "Obtém a corrente da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``current``: Porcentagem de corrente, faixa 0~100%"

Obter Tensão da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperVoltage()``"
    "Descrição", "Obtém a tensão da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``voltage``: Tensão, unidade 0.1V"

Obter Temperatura da Garra
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperTemp()``"
    "Descrição", "Obtém a temperatura da garra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``temp``: Temperatura, unidade ℃"

Calcular Ponto de Pré-Captura - Visão
+++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "Descrição", "Calcula o ponto de pré-captura - Visão"
    "Parâmetros Obrigatórios", "- ``desc_pos``: Pose cartesiana do ponto de captura;
    - ``zlength``: Deslocamento no eixo Z;
    - ``zangle``: Deslocamento de rotação em torno do eixo Z"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``pre_pos``: Pose cartesiana do ponto de pré-captura"

Calcular Ponto de Retirada - Visão
+++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "Descrição", "Calcula o ponto de retirada - Visão"
    "Parâmetros Obrigatórios", "- ``desc_pos``: Pose cartesiana do ponto de captura;
    - ``zlength``: Deslocamento no eixo Z;
    - ``zangle``: Deslocamento de rotação em torno do eixo Z"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``post_pos``: Pose cartesiana do ponto de retirada"

Exemplo de Código para Operações com a Garra do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    company = 4
    device = 0
    softversion = 0
    bus = 2
    index = 2
    act = 0
    max_time = 30000
    block = 0
    status = 0
    fault = 0
    active_status = 0
    current_pos = 0
    current = 0
    voltage = 0
    temp = 0
    speed = 0
    robot.SetGripperConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.GetGripperConfig()
    print(f"gripper config:{company},{device},{softversion},{bus}")
    robot.ActGripper(index, act)
    time.sleep(1)
    act = 1
    robot.ActGripper(index, act)
    time.sleep(1)
    error = robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    time.sleep(1)
    error = robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    error, [fault, status] = robot.GetGripperMotionDone()
    print(f"motion status:{fault},{status}")
    error, [fault, active_status] = robot.GetGripperActivateStatus()
    print(f"gripper active fault is:{fault},status is:{active_status}")
    error, [fault, current_pos] = robot.GetGripperCurPosition()
    print(f"fault is:{fault},current position is:{current_pos}")
    error, [fault, current] = robot.GetGripperCurCurrent()
    print(f"fault is:{fault},current current is:{current}")
    error, [fault, voltage] = robot.GetGripperVoltage()
    print(f"fault is:{fault},current voltage is:{voltage}")
    error, [fault, temp] = robot.GetGripperTemp()
    print(f"fault is:{fault},current temperature is:{temp}")
    error, [fault, speed] = robot.GetGripperCurSpeed()
    print(f"fault is:{fault},current speed is:{speed}")
    retval = 0
    prepick_pose = [0.0]*6
    postpick_pose = [0.0]*6
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval, prepick_pose = robot.ComputePrePick(p1Desc, 10, 0)
    print(f"ComputePrePick retval is:{retval}")
    print(f"xyz is:{prepick_pose[0]},{prepick_pose[1]},{prepick_pose[2]};rpy is:{prepick_pose[3]},{prepick_pose[4]},{prepick_pose[5]}")
    retval, postpick_pose = robot.ComputePostPick(p2Desc, -10, 0)
    print(f"ComputePostPick retval is:{retval}")
    print(f"xyz is:{postpick_pose[0]},{postpick_pose[1]},{postpick_pose[2]};rpy is:{postpick_pose[3]},{postpick_pose[4]},{postpick_pose[5]}")
    robot.CloseRPC()

Obter Número de Rotações da Garra Rotativa
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperRotNum()``"
    "Descrição", "Obtém o número de rotações da garra rotativa"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``num``: Número de rotações"

Obter Porcentagem de Velocidade de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperRotSpeed()``"
    "Descrição", "Obtém a porcentagem de velocidade de rotação da garra rotativa"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``speed``: Porcentagem de velocidade de rotação"

Obter Porcentagem de Torque de Rotação da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetGripperRotTorque()``"
    "Descrição", "Obtém a porcentagem de torque de rotação da garra rotativa"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``fault``: 0-sem erro, 1-com erro
    - ``torque``: Porcentagem de torque de rotação"

Exemplo de Código para Obter Estado da Garra Rotativa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    fault = 0
    rotNum = 0.0
    rotSpeed = 0
    rotTorque = 0
    error,fault, rotNum = robot.GetGripperRotNum()
    error,fault, rotSpeed = robot.GetGripperRotSpeed()
    error,fault, rotTorque = robot.GetGripperRotTorque()
    print(f"gripper rot num:{rotNum},gripper rotSpeed:{rotSpeed},gripper rotTorque:{rotTorque}")
    robot.CloseRPC()

Iniciar/Parar Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorStartEnd(status)``"
    "Descrição", "Inicia/para a esteira transportadora"
    "Parâmetros Obrigatórios", "- ``status``: Estado da esteira, 1-iniciar, 0-parar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Registrar Ponto de Detecção IO
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorPointIORecord()``"
    "Descrição", "Registra o ponto de detecção IO"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Registrar Ponto A
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorPointARecord()``"
    "Descrição", "Registra o ponto A"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Registrar Ponto de Referência
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorRefPointRecord()``"
    "Descrição", "Registra o ponto de referência"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Registrar Ponto B
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorPointBRecord()``"
    "Descrição", "Registra o ponto B"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Detecção IO de Peça na Esteira
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorIODetect(max_t)``"
    "Descrição", "Detecção IO de peça na esteira"
    "Parâmetros Obrigatórios", "- ``max_t``: Tempo máximo de detecção, unidade ms"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Posição Atual do Objeto
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorGetTrackData(mode)``"
    "Descrição", "Obtém a posição atual do objeto"
    "Parâmetros Obrigatórios", "- ``mode``: 1-captura com rastreamento 2-movimento com rastreamento 3-rastreamento TPD"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Iniciar Rastreamento da Esteira
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorTrackStart(status)``"
    "Descrição", "Inicia o rastreamento da esteira"
    "Parâmetros Obrigatórios", "- ``status``: Estado, 1-iniciar, 0-parar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Parar Rastreamento da Esteira
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorTrackEnd()``"
    "Descrição", "Para o rastreamento da esteira"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Configurar Parâmetros da Esteira
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorSetParam(param, followType, startDis, endDis)``"
    "Descrição", "Configura os parâmetros da esteira"
    "Parâmetros Obrigatórios", "- ``param``: = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                    - ``encChannel``: Canal do encoder 1-2
                    - ``resolution``: Resolução do encoder, número de pulsos por rotação do encoder
                    - ``lead``: Relação de transmissão mecânica, distância percorrida pela esteira por rotação do encoder
                    - ``wpAxis``: Número do sistema de coordenadas da peça (para movimento de rastreamento, escolha o número do sistema de coordenadas; para captura com rastreamento e rastreamento TPD, defina como 0)
                    - ``vision``: Se usa visão  0-não usa 1-usa,
                    - ``speedRadio``: Relação de velocidade (para a opção de captura com rastreamento da esteira, faixa de velocidade (1-100); para movimento de rastreamento e rastreamento TPD, defina como 1)"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Compensação do Ponto de Captura da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorCatchPointComp(cmp)``"
    "Descrição", "Compensação do ponto de captura da esteira"
    "Parâmetros Obrigatórios", "- ``cmp``: Compensação de posição [x,y,z]"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Movimento Linear com Rastreamento da Esteira
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorTrackMoveL(name,tool,wobj,vel=20,acc=100,ovl=100,blendR=-1.0)``"
    "Descrição", "Movimento linear com rastreamento da esteira"
    "Parâmetros Obrigatórios", "- ``name``: cvrCatchPoint ou cvrRaisePoint
    - ``tool``: Número da ferramenta
    - ``wobj``: Número da peça"
    "Parâmetros Padrão", "- ``vel``: Velocidade padrão 20
    - ``acc``: Aceleração padrão 100
    - ``ovl``: Fator de escala de velocidade padrão 100
    - ``blendR``: [-1.0]-movimento concluído (bloqueado), [0~1000]-raio de suavização (não bloqueado), unidade [mm] padrão -1.0"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Detecção de Entrada de Comunicação da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorComDetect(timeout)``"
    "Descrição", "Detecção de entrada de comunicação da esteira"
    "Parâmetros Obrigatórios", "- ``timeout``: Tempo limite de espera ms"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Acionamento da Detecção de Entrada de Comunicação da Esteira
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ConveyorComDetectTrigger()``"
    "Descrição", "Acionamento da detecção de entrada de comunicação da esteira"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código de Operação da Esteira do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    retval = robot.ConveyorStartEnd(1)
    print(f"ConveyorStartEnd retval is:{retval}")
    retval = robot.ConveyorPointIORecord()
    print(f"ConveyorPointIORecord retval is:{retval}")
    retval = robot.ConveyorPointARecord()
    print(f"ConveyorPointARecord retval is:{retval}")
    retval = robot.ConveyorRefPointRecord()
    print(f"ConveyorRefPointRecord retval is:{retval}")
    retval = robot.ConveyorPointBRecord()
    print(f"ConveyorPointBRecord retval is:{retval}")
    retval = robot.ConveyorStartEnd(0)
    print(f"ConveyorStartEnd retval is:{retval}")
    param = [1.0, 10000.0, 200.0, 0.0, 0.0, 20.0]
    retval = robot.ConveyorSetParam(param,0)
    print(f"ConveyorSetParam retval is:{retval}")
    cmp = [0.0, 0.0, 0.0]
    retval = robot.ConveyorCatchPointComp(cmp)
    print(f"ConveyorCatchPointComp retval is:{retval}")
    index = 1
    max_time = 30000
    block = 0
    retval = 0
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval = robot.MoveCart(p1Desc, 1, 0, 100.0)
    print(f"MoveCart retval is:{retval}")
    retval = robot.WaitMs(1)
    print(f"WaitMs retval is:{retval}")
    retval = robot.ConveyorIODetect(10000)
    print(f"ConveyorIODetect retval is:{retval}")
    retval = robot.ConveyorGetTrackData(1)
    print(f"ConveyorGetTrackData retval is:{retval}")
    retval = robot.ConveyorTrackStart(1)
    print(f"ConveyorTrackStart retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.ConveyorTrackEnd()
    print(f"ConveyorTrackEnd retval is:{retval}")
    robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0)
    retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    robot.CloseRPC()

Configuração de Parâmetros de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetStationaryTrackPara(self, trackMode, trackTime, trackDis)``"
    "Descrição", "Configura os parâmetros de rastreamento em posição da esteira transportadora"
    "Parâmetros Obrigatórios", "
    - ``trackMode``: 0-tempo; 1-distância; 2-tempo e distância, qualquer condição satisfeita
    - ``trackTime``: Tempo de rastreamento, unidade s
    - ``trackDis``: Distância de rastreamento
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"

Aguardar Conclusão do Movimento Vazio em Posição
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitStationaryMotionDone(self)``"
    "Descrição", "Aguardar a conclusão do movimento vazio em posição"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"

Exemplo de Código de Movimento de Rastreamento em Posição da Esteira Transportadora
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time


    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5) 
        j1 = [-35.146, -102.684, 120.805, -100.401, -90.295, 150.105]
        d1 = [-121.814, -348.341, 209.978, -173.152, -3.585, -5.446]

        ex = [0.0, 0.0, 0.0, 0.0]
        zeroOff = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        tool = 1
        workpiece = 1

        para = [0, 10000, 200, 0, 0, 10]
    
        rtn = robot.ConveyorSetParam(para= para)
        print(f"ConveyorSetParam rtn is {rtn}")

        robot.MoveJ(joint_pos=j1, desc_pos=d1, tool=tool, user=workpiece,
                    vel=100, acc=100, ovl=100, exaxis_pos=ex,
                    blendT=-1, offset_flag=0, offset_pos=zeroOff)

        print("--- Step 1: SetDO(6,1) ---")
        rtn = robot.SetDO(6, 1, 0, 0)
        print(f"  SetDO(6,1) rtn={rtn}")

        print("--- Step 2: ConveyorTrackStart(2) ---")
        rtn = robot.ConveyorTrackStart(2)
        print(f"  ConveyorTrackStart(2) rtn={rtn}")

        print("--- Step 3: ConveyorIODetect(10000) ---")
        rtn = robot.ConveyorIODetect(10000)
        print(f"  ConveyorIODetect(10000) rtn={rtn}")

        print("--- Step 4: ConveyorGetTrackData(2) ---")
        rtn = robot.ConveyorGetTrackData(2)
        print(f"  ConveyorGetTrackData(2) rtn={rtn}")

        print("--- Step 5: SetStationaryTrackPara(0,5,5) ---")
        rtn = robot.SetStationaryTrackPara(0, 5, 5)
        print(f"  SetStationaryTrackPara(0,5,5) rtn={rtn}")

        print("--- Step 6: MoveStationary() ---")
        rtn = robot.MoveStationary()
        print(f"  MoveStationary() rtn={rtn}")

        rtn = robot.WaitStationaryMotionDone()
        print(f"  WaitStationaryMotionDone() rtn={rtn}")

        print("--- Step 7: ConveyorTrackEnd() ---")
        rtn = robot.ConveyorTrackEnd()
        print(f"  ConveyorTrackEnd() rtn={rtn}")

        print("--- Step 8: SetDO(6,0) ---")
        rtn = robot.SetDO(6, 0, 0, 0)
        print(f"  SetDO(6,0) rtn={rtn}")

        robot.CloseRPC()


    if __name__ == "__main__":
        main()

Configurar Sensor de Extremidade
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AxleSensorConfig(idCompany, idDevice, idSoftware, idBus)``"
    "Descrição", "Configura o sensor de extremidade"
    "Parâmetros Obrigatórios", "
    - ``idCompany``: Fabricante, 18-JUNKONG; 25-HUIDE
    - ``idDevice``: Tipo, 0-JUNKONG/RYR6T.V1.0
    - ``idSoftware``: Versão do software, 0-J1.0/HuiDe1.0 (temporariamente não disponível)
    - ``idBus``: Posição de montagem, 1-porta 1 da extremidade; 2-porta 2 da extremidade...8-porta 8 da extremidade (temporariamente não disponível)
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Configuração do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AxleSensorConfigGet()``"
    "Descrição", "Obtém a configuração do sensor de extremidade"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``idCompany``: Fabricante, 18-JUNKONG; 25-HUIDE
    - ``idDevice``: Tipo, 0-JUNKONG/RYR6T.V1.0"
        
Ativar Sensor de Extremidade
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AxleSensorActivate(actFlag)``"
    "Descrição", "Ativa o sensor de extremidade"
    "Parâmetros Obrigatórios", "``actFlag``: 0-reset; 1-ativar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Valor do sistema de coordenadas [x,y,z,rx,ry,rz]"

Escrita no Registrador do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "Descrição", "Escrita no registrador do sensor de extremidade"
    "Parâmetros Obrigatórios", "- ``devAddr``: Endereço do dispositivo 0-255
    - ``regHAddr``: 8 bits altos do endereço do registrador
    - ``regLAddr``: 8 bits baixos do endereço do registrador
    - ``regNum``: Número de registradores 0-255
    - ``data1``: Valor 1 a ser escrito no registrador
    - ``data2``: Valor 2 a ser escrito no registrador
    - ``isNoBlock``: Se é bloqueante 0-bloqueado; 1-não bloqueado"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Exemplo de Código do Sensor de Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.AxleSensorConfig(18, 0, 0, 1)
    error, company, type = robot.AxleSensorConfigGet()
    print(f"company is:{company},type is:{type}")
    rtn = robot.AxleSensorActivate(1)
    print(f"AxleSensorActivate rtn is:{rtn}")
    time.sleep(1)
    rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0)
    print(f"AxleSensorRegWrite rtn is:{rtn}")
    robot.CloseRPC()

Obter Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetExDevProtocol()``"
    "Descrição", "Obtém o protocolo de periféricos do robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode; 
    - ``protocol``: Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster"

Definir Protocolo de Periféricos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExDevProtocol(protocol)``"
    "Descrição", "Define o protocolo de periféricos do robô"
    "Parâmetros Obrigatórios", "- ``protocol``: Número do protocolo de periféricos do robô 4096-placa de controle do eixo de extensão; 4097-ModbusSlave; 4098-ModbusMaster"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Definir Protocolo de Periféricos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    protocol = 4096
    rtn = robot.SetExDevProtocol(protocol)
    print(f"SetExDevProtocol rtn:{rtn}")
    rtn, protocol = robot.GetExDevProtocol()
    print(f"GetExDevProtocol rtn:{rtn},protocol is:{protocol}")
    robot.CloseRPC()


Obter Parâmetros de Comunicação da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxleCommunicationParam()``"
    "Descrição", "Obtém os parâmetros de comunicação da extremidade"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``baudRate``: Taxa de transmissão: suporta 1-9600, 2-14400, 3-19200, 4-38400, 5-56000, 6-67600, 7-115200, 8-128000
    - ``dataBit``: Bits de dados: suporta (8,9), atualmente o mais comum é 8
    - ``stopBit``: Bits de parada: 1-1, 2-0.5, 3-2, 4-1.5, atualmente o mais comum é 1
    - ``verify``: Bits de paridade: 0-None, 1-Odd, 2-Even, atualmente o mais comum é 0
    - ``timeout``: Tempo limite: 1~1000ms, este valor precisa ser definido com um parâmetro de tempo razoável em combinação com o periférico
    - ``timeoutTimes``: Número de tentativas: 1~10, usado principalmente para reenvio em caso de tempo limite, reduzindo ocorrências anormais ocasionais e melhorando a experiência do usuário
    - ``period``: Intervalo de tempo de comandos periódicos: 1~1000ms, usado principalmente para o intervalo de tempo entre cada envio de comandos periódicos"

Definir Parâmetros de Comunicação da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleCommunicationParam(baudRate, dataBit, stopBit, verify, timeout, timeoutTimes, period)``"
    "Descrição", "Define os parâmetros de comunicação da extremidade"
    "Parâmetros Obrigatórios", "- ``baudRate``: Taxa de transmissão: suporta 1-9600, 2-14400, 3-19200, 4-38400, 5-56000, 6-67600, 7-115200, 8-128000
    - ``dataBit``: Bits de dados: suporta (8,9), atualmente o mais comum é 8
    - ``stopBit``: Bits de parada: 1-1, 2-0.5, 3-2, 4-1.5, atualmente o mais comum é 1
    - ``verify``: Bits de paridade: 0-None, 1-Odd, 2-Even, atualmente o mais comum é 0
    - ``timeout``: Tempo limite: 1~1000ms, este valor precisa ser definido com um parâmetro de tempo razoável em combinação com o periférico
    - ``timeoutTimes``: Número de tentativas: 1~10, usado principalmente para reenvio em caso de tempo limite
    - ``period``: Intervalo de tempo de comandos periódicos: 1~1000ms, usado principalmente para o intervalo de tempo entre cada envio de comandos periódicos"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Definir Tipo de Transferência de Arquivo da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleFileType(type)``"
    "Descrição", "Define o tipo de transferência de arquivo da extremidade"
    "Parâmetros Obrigatórios", "- ``type``: 1-arquivo de atualização MCU, 2-arquivo LUA"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Ativar Execução LUA na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleLuaEnable(enable)``"
    "Descrição", "Ativa a execução LUA na extremidade"
    "Parâmetros Obrigatórios", "- ``enable``: 0-desativar; 1-ativar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Recuperação de Erro de Arquivo LUA na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRecoverAxleLuaErr(enable)``"
    "Descrição", "Recuperação de erro de arquivo LUA na extremidade"
    "Parâmetros Obrigatórios", "- ``status``: 0-não recuperar; 1-recuperar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode "

Obter Estado de Ativação da Execução LUA na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxleLuaEnableStatus()``"
    "Descrição", "Obtém o estado de ativação da execução LUA na extremidade"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode 
    - ``enable``: 0-desativar; 1-ativar"

Definir os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleLuaEnableDeviceType(self, forceSensorEnable, gripperEnable, IOEnable, dexhandEnable)``"
    "Descrição", "Define os tipos de dispositivo de extremidade habilitados para o LUA"
    "Parâmetros obrigatórios", "
    - ``forceSensorEnable``: Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    - ``gripperEnable``: Status de habilitação da garra, 0-desabilitado; 1-habilitado
    - ``IOEnable``: Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    - ``dexhandEnable``: Status de habilitação da mão destra, 0-desabilitado; 1-habilitado"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro, 0-sucesso; diferente de zero-erro"

Obter os tipos de dispositivo de extremidade habilitados para LUA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxleLuaEnableDeviceType()``"
    "Descrição", "Obtém os tipos de dispositivo de extremidade habilitados para o LUA"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro, 0-sucesso; diferente de zero-erro
    - ``forceSensorEnable``: Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    - ``gripperEnable``: Status de habilitação da garra, 0-desabilitado; 1-habilitado
    - ``IOEnable``: Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    - ``dexhandEnable``: Status de habilitação da mão destra, 0-desabilitado; 1-habilitado"

Obter os dispositivos de extremidade atualmente configurados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxleLuaEnableDevice()``"
    "Descrição", "Obtém os dispositivos de extremidade atualmente configurados"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro, 0-sucesso; diferente de zero-erro
    - ``forceSensorEnable[8]``: Status de habilitação do sensor de força, 0-desabilitado; 1-habilitado
    - ``gripperEnable[8]``: Status de habilitação da garra, 0-desabilitado; 1-habilitado
    - ``IOEnable[8]``: Status de habilitação do dispositivo IO, 0-desabilitado; 1-habilitado
    - ``dexhandEnable``: Status de habilitação da mão destra, 0-desabilitado; 1-habilitado"

Definir as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleLuaGripperFunc(id, func)``"
    "Descrição", "Define as funções de controle de ação da garra habilitadas"
    "Parâmetros obrigatórios", "
    - ``id``: Número do dispositivo da garra
    - ``func``: 0-habilitação da garra; 1-inicialização da garra; 2-definição de posição; 3-definição de velocidade; 4-definição de torque; 6-leitura do estado da garra; 7-leitura do estado de inicialização; 8-leitura do código de falha; 9-leitura da posição; 10-leitura da velocidade; 11-leitura do torque; 12-definição do número de rotações para garra rotativa; 13-definição da velocidade de rotação para garra rotativa; 14-definição do torque de rotação para garra rotativa; 15-leitura do estado da garra rotativa; 16-leitura do estado de inicialização da garra rotativa; 17-leitura do número de rotações da garra rotativa; 18-leitura da velocidade da garra rotativa; 19-leitura do torque da garra rotativa; 20-definição de movimento síncrono multi-eixo; 21-comando de limpeza de falhas; 22-estado de operação de eixo único; 23-estado de operação de todos os eixos;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro, 0-sucesso; diferente de zero-erro"

Obter as funções de controle de ação da garra habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxleLuaGripperFunc(id)``"
    "Descrição", "Obtém as funções de controle de ação da garra habilitadas"
    "Parâmetros obrigatórios", "- ``id``: Número do dispositivo da garra"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro, 0-sucesso; diferente de zero-erro
    - ``func``: 0-habilitação da garra; 1-inicialização da garra; 2-definição de posição; 3-definição de velocidade; 4-definição de torque; 6-leitura do estado da garra; 7-leitura do estado de inicialização; 8-leitura do código de falha; 9-leitura da posição; 10-leitura da velocidade; 11-leitura do torque; 12-definição do número de rotações para garra rotativa; 13-definição da velocidade de rotação para garra rotativa; 14-definição do torque de rotação para garra rotativa; 15-leitura do estado da garra rotativa; 16-leitura do estado de inicialização da garra rotativa; 17-leitura do número de rotações da garra rotativa; 18-leitura da velocidade da garra rotativa; 19-leitura do torque da garra rotativa; 20-definição de movimento síncrono multi-eixo; 21-comando de limpeza de falhas; 22-estado de operação de eixo único; 23-estado de operação de todos os eixos;"

Escrita de Arquivo no Escravo Ethercat do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SlaveFileWrite(type,slaveID,fileName)``"
    "Descrição", "Escrita de arquivo no escravo Ethercat do robô"
    "Parâmetros Obrigatórios", "- ``type``: Tipo de arquivo do escravo, 1-arquivo de atualização do escravo; 2-arquivo de configuração do escravo
    - ``slaveID``: Número do escravo
    - ``fileName``: Nome do arquivo a ser enviado"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Enviar Arquivo de Protocolo Aberto LUA da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AxleLuaUpload(filePath)``"
    "Descrição", "Envia arquivo de protocolo aberto LUA da extremidade"
    "Parâmetros Obrigatórios", "- ``filePath``: Caminho do arquivo lua local .../AXLE_LUA_End_DaHuan.lua"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Entrar no Modo Boot do Escravo Ethercat do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetSysServoBootMode(filePath)``"
    "Descrição", "Entrar no modo boot do escravo Ethercat do robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Operações com Arquivos LUA da Extremidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua")
    param = [7, 8, 1, 0, 5, 3, 1]  # Parâmetros AxleComParam correspondentes
    robot.SetAxleCommunicationParam(7, 8, 1, 0, 5, 3, 1)
    error,getParam0,getParam1,getParam2,getParam3,getParam4,getParam5,getParam6 = robot.GetAxleCommunicationParam()
    print(f"GetAxleCommunicationParam param is:{getParam0} {getParam1} {getParam2} {getParam3} {getParam4} {getParam5} {getParam6}")
    robot.SetAxleLuaEnable(1)
    error,luaEnableStatus = robot.GetAxleLuaEnableStatus()
    robot.SetAxleLuaEnableDeviceType(0, 1, 0)
    error,forceEnable, gripperEnable, ioEnable = robot.GetAxleLuaEnableDeviceType()
    print(f"GetAxleLuaEnableDeviceType param is:{forceEnable} {gripperEnable} {ioEnable}")
    func = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    robot.SetAxleLuaGripperFunc(1, func)
    error,getFunc = robot.GetAxleLuaGripperFunc(1)
    error,getforceEnable, getgripperEnable, getioEnable = robot.GetAxleLuaEnableDevice()
    print("\ngetforceEnable status:", end=" ")
    for i in range(8):
        print(f"{getforceEnable[i]},", end="")
    print("\ngetgripperEnable status:", end=" ")
    for i in range(8):
        print(f"{getgripperEnable[i]},", end="")
    print("\ngetioEnable status:", end=" ")
    for i in range(8):
        print(f"{getioEnable[i]},", end="")
    print()
    robot.ActGripper(1, 0)
    time.sleep(2)
    robot.ActGripper(1, 1)
    time.sleep(2)
    robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0)
    while True:
        error,pkg = robot.GetRobotRealTimeState()
        print(f"gripper pos is:{pkg.gripper_position}")
        time.sleep(0.1)
    robot.CloseRPC()

    
Obter Estado dos Botões do SmartTool
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSmarttoolBtnState()``"
    "Descrição", "Obtém o estado dos botões do SmartTool"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``state``: Estado dos botões do SmartTool; (bit0:0-comunicação normal; 1-comunicação perdida; bit1-operação de desfazer; bit2-limpar programa; bit3-tecla A; bit4-tecla B; bit5-tecla C; bit6-tecla D; bit7-tecla E; bit8-tecla IO; bit9-manual/automático; bit10-iniciar)"

Exemplo de Código do Botão SmartTool
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    while True:
        error,state = robot.GetSmarttoolBtnState()
        print(f"{state:016b}")
        time.sleep(0.1)

Definir Detecção de Força da Carga Antes de Ativar a Arrastagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTorqueDetectionSwitch(flag)``"
    "Descrição", "Define a detecção de força da carga antes de ativar a arrastagem"
    "Parâmetros Obrigatórios", "- ``flag``: 0-desativar; 1-ativar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Função de Ligar/Desligar Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingLaserOnOff(OnOff, weldId)``"
    "Descrição", "Função para ligar/desligar o periférico laser"
    "Parâmetros Obrigatórios", "- ``OnOff``: 0-desligar; 1-ligar"
    "Parâmetros Padrão", "- ``weldId``: ID da solda, padrão 0"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Função de Iniciar/Parar Rastreamento a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingTrackOnOff(OnOff, coordId)``"
    "Descrição", "Função para iniciar/parar o rastreamento a laser"
    "Parâmetros Obrigatórios", "- ``OnOff``: 0-parar; 1-iniciar
    - ``coordId``: Número do sistema de coordenadas da ferramenta do periférico laser"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Busca de Posição a Laser - Direção Fixa
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingSearchStart_xyz(direction, vel, distance, timeout, posSensorNum)``"
    "Descrição", "Busca de posição a laser - Direção fixa"
    "Parâmetros Obrigatórios", "- ``direction``: 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    - ``vel``: Velocidade unidade %
    - ``distance``: Distância máxima de busca unidade mm
    - ``timeout``: Tempo limite de busca unidade ms
    - ``posSensorNum``: Número do sistema de coordenadas da ferramenta calibrado para o laser"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Busca de Posição a Laser - Direção Arbitrária
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingSearchStart_point(directionPoint, vel, distance, timeout, posSensorNum)``"
    "Descrição", "Busca de posição a laser - Direção arbitrária"
    "Parâmetros Obrigatórios", "- ``directionPoint``: Coordenadas xyz do ponto de entrada da busca, [x,y,z]
    - ``vel``: Velocidade unidade %
    - ``distance``: Distância máxima de busca unidade mm
    - ``timeout``: Tempo limite de busca unidade ms
    - ``posSensorNum``: Número do sistema de coordenadas da ferramenta calibrado para o laser"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Configuração de IP do Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingSensorConfig(ip, port)``"
    "Descrição", "Configuração de IP do laser"
    "Parâmetros Obrigatórios", "- ``ip``: Endereço IP do periférico laser
    - ``port``: Número da porta do periférico laser"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Configuração do Período de Amostragem do Periférico Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserTrackingSensorSamplePeriod(period)``"
    "Descrição", "Configuração do período de amostragem do periférico laser"
    "Parâmetros Obrigatórios", "- ``period``: Período de amostragem do periférico laser unidade ms"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Carregar Driver do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadPosSensorDriver(type)``"
    "Descrição", "Carrega o driver do periférico laser"
    "Parâmetros Obrigatórios", "- ``type``: Tipo de protocolo do driver do periférico laser 101-Ruiniu 102-Chuangxiang 103-Quanshi 104-Tongzhou 105-Aotai"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Descarregar Driver do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``UnLoadPosSensorDriver()``"
    "Descrição", "Descarrega o driver do periférico laser"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Gravação da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserSensorRecord1(status, delayTime)``"
    "Descrição", "Gravação da trajetória da solda a laser"
    "Parâmetros Obrigatórios", "- ``status``: 0-parar gravação 1-rastreamento em tempo real 2-iniciar gravação
    - ``delayTime``: Tempo de atraso unidade ms"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Reprodução da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserSensorReplay(delayTime, speed)``"
    "Descrição", "Reprodução da trajetória da solda a laser"
    "Parâmetros Obrigatórios", "- ``delayTime``: Tempo de atraso unidade ms
    - ``speed``: Velocidade unidade %"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
    
Reprodução do Rastreamento a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveLTR()``"
    "Descrição", "Reprodução do rastreamento a laser"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Reprodução da Trajetória da Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserSensorRecordandReplay(delayMode, delayTime, delayDisExAxisNum, delayDis, sensitivePara, int trackMode, int triggerMode, double runTime, speed)``"
    "Descrição", "Reprodução da trajetória da solda a laser"
    "Parâmetros Obrigatórios", "- ``delayMode``: Modo de atraso 0-tempo de atraso 1-distância de atraso
    - ``delayTime``: Tempo de atraso unidade ms
    - ``delayDisExAxisNum``: Número do eixo de extensão
    - ``delayDis``: Distância de atraso unidade mm
    - ``sensitivePara``: Coeficiente de sensibilidade de compensação
    - ``trackMode``: Tipo de rastreamento pontual. 0-movimento assíncrono do eixo de extensão; 1-robô
    - ``triggerMode``: Modo de acionamento do rastreamento pontual. 0-duração do rastreamento; 1-IO
    - ``runTime``: Duração do rastreamento pontual do robô (s)
    - ``speed``: Velocidade unidade %"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Mover para o Início da Gravação da Solda
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToLaserRecordStart(moveType, ovl)``"
    "Descrição", "Mover para o início da gravação da solda"
    "Parâmetros Obrigatórios", "- ``moveType``: 0-PTP 1-LIN
    - ``ovl``: Velocidade unidade %"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Mover para o Fim da Gravação da Solda
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToLaserRecordEnd(moveType, ovl)``"
    "Descrição", "Mover para o fim da gravação da solda"
    "Parâmetros Obrigatórios", "- ``moveType``: 0-PTP 1-LIN
    - ``ovl``: Velocidade unidade %"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Mover para o Ponto de Busca do Sensor a Laser
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToLaserSeamPos(moveFlag, ovl, dataFlag, plateType, trackOffectType, offset)``"
    "Descrição", "Mover para o ponto de busca do sensor a laser"
    "Parâmetros Obrigatórios", "- ``moveFlag``: Tipo de movimento: 0-PTP; 1-LIN
    - ``ovl``: Fator de escala de velocidade, 0-100
    - ``dataFlag``: Seleção de dados de cache da solda: 0-executar dados planejados; 1-executar dados gravados
    - ``plateType``: Tipo de placa: 0-placa ondulada; 1-placa corrugada; 2-placa de cerca; 3-barril de óleo; 4-aço de casco ondulado
    - ``trackOffectType``: Tipo de deslocamento do sensor a laser: 0-sem deslocamento; 1-deslocamento no sistema de coordenadas base; 2-deslocamento no sistema de coordenadas da ferramenta; 3-deslocamento com base nos dados brutos do sensor a laser
    - ``offset``: Valor de deslocamento"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Informações de Coordenadas do Ponto de Busca do Sensor a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetLaserSeamPos(trackOffectType, offset)``"
    "Descrição", "Obtém as informações de coordenadas do ponto de busca do sensor a laser"
    "Parâmetros Obrigatórios", "- ``trackOffectType``: Tipo de deslocamento do sensor a laser: 0-sem deslocamento; 1-deslocamento no sistema de coordenadas base; 2-deslocamento no sistema de coordenadas da ferramenta; 3-deslocamento com base nos dados brutos do sensor a laser
    - ``offset``: Valor de deslocamento"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``jPos``: Posição articular [°]
    - ``descPos``: Posição cartesiana [mm]
    - ``tool``: Sistema de coordenadas da ferramenta
    - ``user``: Sistema de coordenadas da peça
    - ``exaxis``: Posição do eixo de extensão [mm]"

Exemplo de Código para Configuração e Depuração de Parâmetros do Periférico Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.LaserTrackingSensorConfig("192.168.58.20", 5020)
    robot.LaserTrackingSensorSamplePeriod(20)
    robot.LoadPosSensorDriver(101)
    robot.LaserTrackingLaserOnOff(0, 0)
    time.sleep(3)
    robot.LaserTrackingLaserOnOff(1, 0)
    robot.CloseRPC()

Exemplo de Código para Digitalização e Reprodução de Trajetória a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    i = 0
    while i<10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(2, 10)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 50,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(0, 10)
        robot.MoveToLaserRecordStart(1, 30)
        robot.LaserSensorReplay(10, 100)
        robot.MoveLTR()
        robot.LaserSensorRecord1(0, 10)
        i = i+1
    robot.CloseRPC()

Exemplo de Código para Busca de Posição e Rastreamento em Tempo Real a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    time.sleep(8)
    i = 0
    while i < 10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        directionPoint = [0.0] * 3
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3)
        robot.LaserTrackingSearchStop()
        robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese)
        robot.LaserTrackingTrackOnOff(1, 3)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 20,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingTrackOnOff(0, 3)
        i = i + 1
        print(i)
    robot.CloseRPC()

Exemplo de Código para Rastreamento a Laser Síncrono com Eixo de Extensão e Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    startexaxisPos = [0.0, 0.0, 0.0, 0.0]
    seamexaxisPos = [-10.0, 0.0, 0.0, 0.0]
    endexaxisPos = [-30.0, 0.0, 0.0, 0.0]
    offdese = [0.0] * 6
    seamjointPos = [0.0] * 6
    seamdescPose = [0.0] * 6
    i=0
    while i < 10:
        startjointPos = [58.337, -119.628, 146.037, -116.358, -92.224, -117.654]
        startdescPose = [-53.375, -255.363, 0.919, 178.054, 1.077, -94.026]
        robot.ExtAxisSyncMoveJ(joint_pos=startjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= startexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
        ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2)
        robot.LaserTrackingSearchStop()
        tool = 0
        user = 0
        rnte, seamjointPos, seamdescPose, tool, user, startexaxisPos = robot.GetLaserSeamPos(0, offdese)
        print(f"{seamjointPos[0]},{seamjointPos[1]},{seamjointPos[2]},{seamjointPos[3]},{seamjointPos[4]},{seamjointPos[5]},{seamdescPose[0]},{seamdescPose[1]},{seamdescPose[2]},{seamdescPose[3]},{seamdescPose[4]},{seamdescPose[5]}")
        if ret == 0:
            robot.ExtAxisSyncMoveJ(joint_pos=seamjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= seamexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(1, 2)
            endjointPos = [70.580, -90.918, 126.593, -125.154, -92.162, -105.403]
            enddescPose = [-53.375, -419.020, 0.920, 178.054, 1.076, -94.026]
            robot.ExtAxisSyncMoveL(desc_pos=enddescPose, tool=1,user= 0,vel= 20,acc= 100, ovl=100,blendR= -1,exaxis_pos= endexaxisPos,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(0, 2)
        i = i+1
        print(i)
    robot.CloseRPC()

Controlar Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetSuckerCtrl(slaveID, len, ctrlValue)``"
    "Descrição", "Controla a matriz de ventosas"
    "Parâmetros Obrigatórios", "- ``slaveID``: Número do escravo
    - ``len``: Comprimento
    - ``ctrlValue``: Valor de controle 1-sucção com vácuo máximo 2-sucção com vácuo definido 3-parar sucção"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Estado da Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSuckerState(slaveID)``"
    "Descrição", "Obtém o estado da matriz de ventosas"
    "Parâmetros Obrigatórios", "- ``slaveID``: Número do escravo"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``state``: Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    - ``pressValue``: Vácuo atual unidade kPa
    - ``error``: Código de erro atual da ventosa"

Aguardar Estado da Ventosa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitSuckerState(slaveID, state, ms)``"
    "Descrição", "Aguarda o estado da ventosa"
    "Parâmetros Obrigatórios", "- ``slaveID``: Número do escravo
    - ``state``: Estado de sucção 0-objeto solto 1-objeto detectado e sucção bem-sucedida 2-objeto não detectado 3-objeto desprendido
    - ``ms``: Tempo máximo de espera"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Instruções de Controle da Matriz de Ventosas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("C://openlua/CtrlDev_sucker.lua")
    time.sleep(2)
    robot.UnloadCtrlOpenLUA(1)
    robot.LoadCtrlOpenLUA(1)
    time.sleep(1)
    ctrl = bytearray(20)
    ctrl[0] = 1
    robot.SetSuckerCtrl(0, 1, ctrl)
    for i in range(100):
        rtn, state, press_value, error = robot.GetSuckerState(1)
        print(f"sucker1 state is {state}, pressValue is {press_value}, error num is {error}")
        rtn, state, press_value, error = robot.GetSuckerState(12)
        print(f"sucker12 state is {state}, pressValue is {press_value}, error num is {error}")
        time.sleep(0.1)
    ret = robot.WaitSuckerState(1, 1, 100)
    print(f"WaitSuckerState result is {ret}")
    ctrl[0] = 3
    robot.SetSuckerCtrl(1, 1, ctrl)
    robot.SetSuckerCtrl(12, 1, ctrl)
    robot.CloseRPC()

Enviar Arquivo Lua de Protocolo Aberto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``OpenLuaUpload(filePath)``"
    "Descrição", "Envia o arquivo Lua de protocolo aberto"
    "Parâmetros Obrigatórios", "- ``filePath``: Caminho do arquivo lua de protocolo aberto local"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Parâmetros da Placa Escrava
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetFieldBusConfig()``"
    "Descrição", "Obtém os parâmetros da placa escrava"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``type``: 0-Ethercat, 1-CClink, 3-Ethercat, 4-EIP
    - ``version``: Versão do protocolo
    - ``connState``: 0-desconectado 1-conectado"

Escrever DO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveWriteDO(DOIndex, wirteNum, status)``"
    "Descrição", "Escreve DO no escravo"
    "Parâmetros Obrigatórios", "- ``DOIndex``: Número do DO
    - ``wirteNum``: Número a ser escrito
    - ``status``: Valor a ser escrito, máximo de 8"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Escrever AO no Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveWriteAO(AOIndex, wirteNum, status)``"
    "Descrição", "Escreve AO no escravo"
    "Parâmetros Obrigatórios", "- ``AOIndex``: Número do AO
    - ``wirteNum``: Número a ser escrito
    - ``status``: Valor a ser escrito, máximo de 8"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Ler DI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveReadDI(DOIndex, readeNum)``"
    "Descrição", "Lê DI do escravo"
    "Parâmetros Obrigatórios", "- ``DOIndex``: Número do DI
    - ``readeNum``: Número a ser lido"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``status[8]``: Valor lido, máximo de 8"

Ler AI do Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveReadAI(AOIndex, readeNum)``"
    "Descrição", "Lê AI do escravo"
    "Parâmetros Obrigatórios", "- ``AOIndex``: Número do AI
    - ``readeNum``: Número a ser lido"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``status[8]``: Valor lido, máximo de 8"

Aguardar Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveWaitDI(DIIndex, status, waitMs)``"
    "Descrição", "Aguarda a entrada DI de extensão"
    "Parâmetros Obrigatórios", "- ``DIIndex``: Número do DI
    - ``status``: 0-nível baixo; 1-nível alto
    - ``waitMs``: Tempo máximo de espera (ms)"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FieldBusSlaveWaitAI(AIIndex, waitType, value, waitMs)``"
    "Descrição", "Aguarda a entrada AI de extensão"
    "Parâmetros Obrigatórios", "- ``AIIndex``: Número do AI
    - ``waitType``: 0-maior que; 1-menor que
    - ``value``: Valor do AI
    - ``waitMs``: Tempo máximo de espera (ms)"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Interfaces de Instrução do Modo Escravo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_field.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(3,"CtrlDev_field.lua")
    robot.UnloadCtrlOpenLUA(3)
    robot.LoadCtrlOpenLUA(3)
    time.sleep(8)
    rtn,type, version, conn_state = robot.GetFieldBusConfig()
    print(f"type is {type}, version is {version}, connState is {conn_state}")
    # Write digital outputs
    ctrl = [1, 0, 1]  # DO0=1, DO1=0, DO2=1
    robot.FieldBusSlaveWriteDO(0, 3, ctrl)
    # Write analog output
    ctrl_ao = [0x1000]  # AO2 = 0x1000
    robot.FieldBusSlaveWriteAO(2, 1, ctrl_ao)
    for i in range(100):
        rtn,di = robot.FieldBusSlaveReadDI(0, 4)
        print(f"DI0 is {di[0]}, DI1 is {di[1]}, DI2 is {di[2]}, DI3 is {di[3]}")
        rtn, ai = robot.FieldBusSlaveReadAI(0, 3)
        print(f"AI0 is {ai[0]}, AI1 is {ai[1]}, AI2 is {ai[2]}")
        time.sleep(0.01)
    ret = robot.FieldBusSlaveWaitDI(0, 1, 100)
    print(f"FieldBusSlaveWaitDI result is {ret}")
    ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00, 100)
    print(f"FieldBusSlaveWaitAI result is {ret}")
    robot.CloseRPC()

Interface SDK para Ativar/Desativar Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxleGenComEnable(mode)``"
    "Descrição", "Ativa/desativa a função de passagem direta na extremidade"
    "Parâmetros Obrigatórios", "- ``mode``: enable, 0-desativar, 1-ativar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Interface SDK para Transmissão e Recepção de Dados Aperiódicos na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SndRcvAxleGenComCmdData( len_snd, sndBuff, len_rcv)``"
    "Descrição", "Envia dados aperiódicos na extremidade e aguarda resposta"
    "Parâmetros Obrigatórios", "
    - ``len_snd``: Comprimento do envio;
    - ``sndBuff[]``: Dados a serem enviados;
    - ``len_rcv``: Comprimento da recepção selecionada;
    - ``rcvBuff[]``: Dados de resposta;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Comunicação de Dados Aperiódicos do Cabeçote de Moxabustão Beiyikang Baseado na Função de Passagem Direta na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # A connection is established with the robot controller. A successful connection returns a robot object
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')

    import time


    def testAxleGenCom(self):

        led_on = [0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79]
        led_off = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        version = [0xAB, 0xBA, 0x11, 0x00, 0x76]
        state = [0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B]
        cycleState = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        cnt = 1

        p1Joint = [88.708, -86.178, 140.989, -141.825, -89.162, -49.879]
        p1Desc = [188.007, -377.850, 260.207, 178.715, 2.823, -131.466]
        p2Joint = [112.131, -75.554, 126.989, -139.027, -88.044, -26.477]
        p2Desc = [368.003, -377.848, 260.211, 178.715, 2.823, -131.465]

        exaxisPos = [0, 0, 0, 0]
        offdese = [0, 0, 0, 0, 0, 0]

        # Ativa a função de passagem direta na extremidade
        robot.SetAxleGenComEnable(1)
        robot.SetAxleLuaEnable(1)

        while cnt <= 10000:
            # Lê o número da versão
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(len_snd=5, sndBuff=version, len_rcv=10)
            print(ret)
            print(rcvdata)
            print(f"hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}")
            if ret != 0:
                break
            time.sleep(1)
            # Lê o estado de presença do cabeçote de moxabustão
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, state, 6)
            print(f"state : {rcvdata[4]} ")
            time.sleep(1)
            # Ativa o laser do cabeçote de moxabustão
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, led_on, 6)
            print(f"led on rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,
                            offset_flag=0, offset_pos=offdese)
            time.sleep(4)
            # Desativa o laser do cabeçote de moxabustão
            ret, rcvdata = robot.SndRcvAxleGenComCmdData(6, led_off, 6)
            print(f"led off rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,offset_flag=0, offset_pos=offdese)
            time.sleep(1)
            print(f"***********************complate No. {cnt} SDK test*****************************")
            cnt = cnt + 1

        robot.CloseRPC()
        return 0

    testAxleGenCom(robot)
    
Download do Arquivo Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``OpenLuaDownload(fileName, savePath)``"
    "Descrição", "Download do arquivo Lua de protocolo aberto"
    "Parâmetros Obrigatórios", "
    - ``fileName``: Nome do arquivo de protocolo aberto `CtrlDev_XXX.lua`;
    - ``savePath``: Caminho para salvar o arquivo de protocolo aberto;
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
    
Excluir Arquivo Lua de Protocolo Aberto Específico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``OpenLuaDelete(fileName)``"
    "Descrição", "Exclui um arquivo Lua de protocolo aberto específico"
    "Parâmetros Obrigatórios", "
    - ``fileName``: Nome do arquivo lua de protocolo aberto a ser excluído `CtrlDev_XXX.lua`
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
    
Excluir Todos os Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AllOpenLuaDelete()``"
    "Descrição", "Exclui todos os arquivos Lua de protocolo aberto"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código SDK para Operações com Arquivos Lua de Protocolo Aberto
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')


    def TestCtrlOpenLuaOperate(self):
        # Envia arquivo Lua para o robô
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        # Download do arquivo Lua do robô
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        # Define o nome do Lua de protocolo aberto de controle
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        # Obtém o nome do Lua de protocolo aberto de controle
        rtn, name = robot.GetCtrlOpenLUAName()
        print(f"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}")
        
        # Carrega o Lua de protocolo aberto de controle
        rtn = robot.LoadCtrlOpenLUA(1)
        print(f"LoadCtrlOpenLUA rtn is {rtn}")
        time.sleep(2)
        
        # Descarrega o Lua de protocolo aberto de controle
        rtn = robot.UnloadCtrlOpenLUA(1)
        print(f"UnloadCtrlOpenLUA rtn is {rtn}")
        
        # Exclui o arquivo Lua especificado
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua")
        print(f"OpenLuaDelete rtn is {rtn}")
        
        # Exclui todos os arquivos Lua
        rtn = robot.AllOpenLuaDelete()
        print(f"AllOpenLuaDelete rtn is {rtn}")
        
        # Fecha a conexão
        robot.CloseRPC()
        time.sleep(1)


    # Chama a função de teste
    TestCtrlOpenLuaOperate(robot)

Controlar o Movimento da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDexterousHandsMove(self, idstart, slaveNum, pos, speed, force, max_time)``"
    "Descrição", "Controlar o movimento da mão destra"
    "Parâmetros Obrigatórios", "
    - ``idstart``: Número da estação escrava inicial;
    - ``slaveNum``: Número de escravos;
    - ``pos[16]``: Posição (-360~360);
    - ``speed[16]``: Percentual de velocidade, intervalo [0~100];
    - ``force[16]``: Percentual de torque, intervalo [0~100];
    - ``max_time``: Tempo máximo de espera, intervalo [0~30000], unidade ms;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"
        
Controlar o Reset e Ativação da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDexterousHandsAct(self, id, act)``"
    "Descrição", "Controlar o reset e ativação da mão destra"
    "Parâmetros Obrigatórios", "
    - ``id``: Número da estação escrava;
    - ``act``: 0-reset 1-ativação"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"
        
Limpar Erro da Mão Destra
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ClearDexterousHandsError(self)``"
    "Descrição", "Limpar erro da mão destra"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"
    
Definir as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDexterousHandsFunc(self, id, func)``"
    "Descrição", "Define as funções de controle de ação da mão destra habilitadas"
    "Parâmetros Obrigatórios", "
    - ``id``: Número da estação escrava da mão destra;
    - ``func``: Array de funções, 32 elementos
        0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque,
        6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade,
        11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação,
        15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação,
        19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único,
        23-estado de operação de todos os eixos"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"
    
Obter as Funções de Controle de Ação da Mão Destra Habilitadas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDexterousHandsFunc(self, id)``"
    "Descrição", "Obtém as funções de controle de ação da mão destra habilitadas"
    "Parâmetros Obrigatórios", "
    - ``id``: Número da estação escrava da mão destra;
    - ``func``: Array de funções, 32 elementos
        0-acionamento de aperto, 1-inicialização da garra, 2-definição de posição, 3-definição de velocidade, 4-definição de torque,
        6-leitura do estado da garra, 7-leitura do estado de inicialização, 8-leitura do código de falha, 9-leitura da posição, 10-leitura da velocidade,
        11-leitura do torque, 12-definição do número de rotações, 13-definição da velocidade de rotação, 14-definição do torque de rotação,
        15-leitura do estado da garra rotativa, 16-leitura do estado de inicialização da rotação, 17-leitura do número de rotações, 18-leitura da velocidade de rotação,
        19-leitura do torque de rotação, 20-definição de movimento síncrono multi-eixo, 21-comando de limpeza de falhas, 22-estado de operação de eixo único,
        23-estado de operação de todos os eixos"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro, 0-sucesso; diferente de zero-erro"

Exemplo de Código de Configuração e Movimento da Mão Destra no Efetuador Final  
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:  
     
    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')

    def main(self):

        id = 1                 
        slaveNum = 4         
        max_time = 8000      
        speed = [0] * 16     
        force = [0] * 16     

        for i in range(16):
            force[i] = 50 if i < 4 else 0

        def set_positions(v1, v2, v3, v4):
            pos = [0.0] * 16
            pos[0] = v1
            pos[1] = v2
            pos[2] = v3
            pos[3] = v4
            return pos

        j1 = [-53.426,-85.916,109.280,-86.236,-96.663,-28.560]
        j2 = [-91.877,-85.917,109.281,-86.236,-96.663,-28.560]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        ret = robot.ClearDexterousHandsError()
        print(f"ClearDexterousHandsError -> {ret}")

        setFunc = [0] * 32
        setFunc[2] = 1   
        setFunc[4] = 1   
        setFunc[9] = 1   
        setFunc[10] = 1  
        setFunc[11] = 1  
        setFunc[22] = 1  

        ret = robot.SetDexterousHandsFunc(id, setFunc)
        print(f"SetDexterousHandsFunc(init + funções de posição/torque habilitadas) -> {ret}")

        ret, getFunc = robot.GetDexterousHandsFunc(id)
        print(f"GetDexterousHandsFunc -> {ret}")
        if ret == 0:
            print("GetDexterousHandsFunc :")
            for i in range(len(getFunc)):
                print(f"  [{i}]={getFunc[i]}", end="")
                if (i + 1) % 8 == 0:
                    print()  
                elif i < len(getFunc) - 1:
                    print(", ", end="")
            if len(getFunc) % 8 != 0:

        ret = robot.SetDexterousHandsAct(id, 1)
        print(f"SetDexterousHandsAct() -> {ret}")
        if ret != 0:
            return
            pos = set_positions(20, 20, 20, 20)
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
        print(f"ret: {ret}")
        time.sleep(5)

        for iteration in range(1, 11):
            robot.MoveJ(joint_pos=j1, tool=1, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

            pos = set_positions(10, 10, 10, 10)
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
            time.sleep(1)

            robot.MoveJ(joint_pos=j2, tool=1, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

            pos = set_positions(50, 50, 50, 50)
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
            time.sleep(1)

    main(robot)