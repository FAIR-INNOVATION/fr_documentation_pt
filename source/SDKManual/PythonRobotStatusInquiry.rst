Consulta de Estado do Robô
==============================

.. toctree:: 
    :maxdepth: 5

Obter Posição Articular Atual (graus)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualJointPosDegree(flag=1)``"
    "Descrição", "Obtém a posição articular atual (graus)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``: Posição articular atual (graus)"

Obter Posição Articular Atual (radianos)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualJointPosRadian(flag=1)``"
    "Descrição", "Obtém a posição articular atual (radianos)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``: Posição articular atual (radianos)"

Obter Velocidade de Feedback da Junta (graus/s)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualJointSpeedsDegree(flag=1)``"
    "Descrição", "Obtém a velocidade de feedback da junta (graus/s)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``speed=[j1,j2,j3,j4,j5,j6]``: Velocidade de feedback da junta (graus/s)"

Obter Aceleração de Feedback da Junta (graus/s²)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualJointAccDegree(flag=1)``"
    "Descrição", "Obtém a aceleração de feedback da junta (graus/s²)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``acc=[j1,j2,j3,j4,j5,j6]``: Aceleração de feedback da junta (graus/s²)"

Obter Velocidade Linear Composta do TCP de Comando
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTargetTCPCompositeSpeed(flag=1)``"
    "Descrição", "Obtém a velocidade linear composta do TCP de comando"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``[tcp_speed, ori_speed]``: tcp_speed - velocidade linear composta, ori_speed - velocidade angular composta"

Obter Velocidade Linear Composta do TCP de Feedback
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualTCPCompositeSpeed(flag=1)``"
    "Descrição", "Obtém a velocidade linear composta do TCP de feedback"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``[tcp_speed, ori_speed]``: tcp_speed - velocidade linear composta, ori_speed - velocidade angular composta"

Obter Velocidade do TCP de Comando
+++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTargetTCPSpeed(flag=1)``"
    "Descrição", "Obtém a velocidade do TCP de comando"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``speed=[x,y,z,rx,ry,rz]``: Velocidade do TCP de comando, mm/s"

Obter Velocidade do TCP de Feedback
+++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualTCPSpeed(flag=1)``"
    "Descrição", "Obtém a velocidade do TCP de feedback"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``speed=[x,y,z,rx,ry,rz]``: Velocidade do TCP de feedback"

Obter Pose Atual da Ferramenta
++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualTCPPose(flag=1)``"
    "Descrição", "Obtém a pose atual da ferramenta"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``: Pose atual da ferramenta"

Obter Número do Sistema de Coordenadas da Ferramenta Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualTCPNum(flag=1)``"
    "Descrição", "Obtém o número do sistema de coordenadas da ferramenta atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``tool_id``: Número do sistema de coordenadas da ferramenta"

Obter Número do Sistema de Coordenadas da Peça Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualWObjNum(flag=1)``"
    "Descrição", "Obtém o número do sistema de coordenadas da peça atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``wobj_id``: Número do sistema de coordenadas da peça"

Obter Pose Atual do Flange da Extremidade
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetActualToolFlangePose(flag=1)``"
    "Descrição", "Obtém a pose atual do flange da extremidade"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``flange_pose=[x,y,z,rx,ry,rz]``: Pose atual do flange da extremidade"

Obter Torque Articular Atual
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetJointTorques(flag=1)``"
    "Descrição", "Obtém o torque articular atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``torques=[j1,j2,j3,j4,j5,j6]``: Torque articular"

Obter Tempo do Sistema
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSystemClock()``"
    "Descrição", "Obtém o tempo do sistema"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``t_ms``: Tempo do sistema, unidade [ms]"

Consultar se o Movimento do Robô foi Concluído
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotMotionDone()``"
    "Descrição", "Consulta se o movimento do robô foi concluído"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``state``: Estado de movimento do robô, 0-não concluído, 1-concluído"

Consultar o Comprimento do Cache da Fila de Movimento do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetMotionQueueLength()``"
    "Descrição", "Consulta o comprimento do cache da fila de movimento do robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``len``: Comprimento do cache"

Obter Estado de Parada de Emergência do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotEmergencyStopState()``"
    "Descrição", "Obtém o estado de parada de emergência do robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``state``: Estado de parada de emergência, 0-não em parada de emergência, 1-em parada de emergência"

Obter Estado de Comunicação entre o SDK e o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSDKComState()``"
    "Descrição", "Obtém o estado de comunicação entre o SDK e o robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``state``: Estado de comunicação, 0-comunicação normal, 1-comunicação anormal"

Obter Sinal de Parada de Segurança
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSafetyStopState()``"
    "Descrição", "Obtém o sinal de parada de segurança"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``[si0_state, si1_state]``: si0_state - Sinal de parada de segurança SI0, 0-inativo, 1-ativo; si1_state - Sinal de parada de segurança SI1, 0-inativo, 1-ativo"

Obter Temperatura Atual do Driver da Junta (℃)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetJointDriverTemperature()``"
    "Descrição", "Obtém a temperatura atual do driver da junta (℃)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``data=[t1,t2,t3,t4,t5,t6]``: Temperatura atual de cada junta"

Obter Torque Atual do Driver da Junta (Nm)
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetJointDriverTorque()``"
    "Descrição", "Obtém o torque atual do driver da junta (Nm)"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``data=[j1,j2,j3,j4,j5,j6]``: Torque articular [fx,fy,fz,tx,ty,tz]"

Obter Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotRealTimeState()``"
    "Descrição", "Obtém o estado do robô"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``robot_state_pkg``: Estrutura de estado do robô"

Exemplo de Código de Consulta de Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    error,[yangle, zangle] = robot.GetRobotInstallAngle()
    print(f"yangle:{yangle},zangle:{zangle}")
    error,j_deg = robot.GetActualJointPosDegree(0)
    print(f"joint pos deg:{j_deg[0]},{j_deg[1]},{j_deg[2]},{j_deg[3]},{j_deg[4]},{j_deg[5]}")
    error,jointSpeed = robot.GetActualJointSpeedsDegree(0)
    print(f"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}")
    error,jointAcc = robot.GetActualJointAccDegree(0)
    print(f"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}")
    error,[tcp_speed, ori_speed] = robot.GetTargetTCPCompositeSpeed(0)
    print(f"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,[tcp_speed, ori_speed] = robot.GetActualTCPCompositeSpeed(0)
    print(f"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,targetSpeed = robot.GetTargetTCPSpeed(0)
    print(f"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}")
    error,actualSpeed = robot.GetActualTCPSpeed(0)
    print(f"GetActualTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}")
    error,tcp = robot.GetActualTCPPose(0)
    print(f"tcp pose:{tcp[0]},{tcp[1]},{tcp[2]},{tcp[3]},{tcp[4]},{tcp[5]}")
    error,flange = robot.GetActualToolFlangePose(0)
    print(f"flange pose:{flange[0]},{flange[1]},{flange[2]},{flange[3]},{flange[4]},{flange[5]}")
    error,id = robot.GetActualTCPNum(0)
    print(f"tcp num:{id}")
    error,id = robot.GetActualWObjNum(0)
    print(f"wobj num:{id}")
    error,jtorque = robot.GetJointTorques(0)
    print(f"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}")
    error,t_ms = robot.GetSystemClock()
    print(f"system clock:{t_ms}")
    error,config = robot.GetRobotCurJointsConfig()
    print(f"joint config:{config}")
    error,motionDone = robot.GetRobotMotionDone()
    print(f"GetRobotMotionDone:{motionDone}")
    error,len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength:{len}")
    error,emergState = robot.GetRobotEmergencyStopState()
    print(f"GetRobotEmergencyStopState:{emergState}")
    error,comstate = robot.GetSDKComState()
    print(f"GetSDKComState:{comstate}")
    error,[si0_state, si1_state] = robot.GetSafetyStopState()
    print(f"GetSafetyStopState:{si0_state} {si1_state}")
    error,temp = robot.GetJointDriverTemperature()
    print(f"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}")
    error,torque = robot.GetJointDriverTorque()
    print(f"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}")
    error,pkg = robot.GetRobotRealTimeState()
    robot.CloseRPC()

Solução de Cinemática Inversa
++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetInverseKin(type,desc_pos,config=-1)``"
    "Descrição", "Cinemática inversa, resolve a posição articular a partir da pose cartesiana"
    "Parâmetros Obrigatórios", "- ``type``: 0-pose absoluta (sistema de coordenadas base), 1-pose relativa (sistema de coordenadas base), 2-pose relativa (sistema de coordenadas da ferramenta)
    - ``desc_pose``: [x,y,z,rx,ry,rz], pose da ferramenta, unidade [mm][°]"
    "Parâmetros Padrão", "- ``config``: Configuração articular, [-1]-resolve com base na posição articular atual, [0~7]-resolve com base em uma configuração articular específica. Padrão -1"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``: Solução da cinemática inversa, posição articular a partir da pose cartesiana"

Solução de Cinemática Inversa com Posição de Referência Especificada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetInverseKinRef(type,desc_pos,joint_pos_ref)``"
    "Descrição", "Cinemática inversa, resolve a posição articular a partir da pose da ferramenta, usando uma posição articular de referência"
    "Parâmetros Obrigatórios", "- ``type``: 0-pose absoluta (sistema de coordenadas base), 1-pose relativa (sistema de coordenadas base), 2-pose relativa (sistema de coordenadas da ferramenta)
    - ``desc_pos``: [x,y,z,rx,ry,rz] pose da ferramenta, unidade [mm][°]
    - ``joint_pos_ref``: [j1,j2,j3,j4,j5,j6], posição articular de referência, unidade [°]"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``: Solução da cinemática inversa, posição articular a partir da pose da ferramenta"

Solução de Cinemática Inversa Incluindo Posição do Eixo de Extensão no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetInverseKinExaxis(type, desc_pos, exaxis, tool, workPiece)``"
    "Descrição", "Solução de cinemática inversa incluindo posição do eixo de extensão no espaço cartesiano"
    "Parâmetros Obrigatórios", "- ``type``: 0-pose absoluta (sistema de coordenadas base), 1-pose incremental (sistema de coordenadas base), 2-pose incremental (sistema de coordenadas da ferramenta)
    - ``desc_pos``: Pose cartesiana
    - ``exaxis``: Posição do eixo de extensão
    - ``tool``: Número da ferramenta
    - ``workPiece``: Número da peça"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint_pos``: Posição articular"

Exemplo de Código para Solução de Cinemática Inversa Incluindo Posição do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    desc = [99.957, -0.002, 29.994, -176.569, -6.757, -167.462]
    exaxis = [100.0, 0.0, 0.0, 0.0]
    jointPos = [0.0] * 6
    offsetPos = [0.0] * 6
    rtn,pkg = robot.GetRobotRealTimeState()
    toolnum = pkg.tool
    workPcsNum = pkg.user
    rtn, jointPos = robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum)
    print(f"GetInverseKinExaxis joint is {jointPos[0]},{jointPos[1]},{jointPos[2]},{jointPos[3]},{jointPos[4]},{jointPos[5]}")
    robot.ExtAxisMove(exaxis, 100, -1)
    robot.MoveJ(joint_pos=jointPos, desc_pos=desc, tool=toolnum, user=workPcsNum, vel=100.0, acc=100.0, ovl=100.0, exaxis_pos=exaxis, blendT=-1, offset_flag=0, offset_pos=offsetPos)
    robot.CloseRPC()
    return 0

Solução de Cinemática Inversa - Verificar se Há Solução
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetInverseKinHasSolution(type,desc_pos,joint_pos_ref)``"
    "Descrição", "Cinemática inversa, verifica se há solução para a posição articular a partir da pose da ferramenta"
    "Parâmetros Obrigatórios", "- ``type``: 0-pose absoluta (sistema de coordenadas base), 1-pose relativa (sistema de coordenadas base), 2-pose relativa (sistema de coordenadas da ferramenta)
    - ``desc_pos``: [x,y,z,rx,ry,rz] pose da ferramenta, unidade [mm][°]
    - ``joint_pos_ref``: [j1,j2,j3,j4,j5,j6], posição articular de referência, unidade [°]"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``result``: “True” - há solução, “False” - não há solução"

Solução de Cinemática Direta
++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetForwardKin(joint_pos)``"
    "Descrição", "Cinemática direta, resolve a pose da ferramenta a partir da posição articular"
    "Parâmetros Obrigatórios", "- ``joint_pos``: [j1,j2,j3,j4,j5,j6]: posição articular, unidade [°]"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``desc_pos=[x,y,z,rx,ry,rz]``: Solução da cinemática direta, pose da ferramenta a partir da posição articular"

Exemplo de Código para Cálculos de Cinemática Direta e Inversa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    error, inverseRtn = robot.GetInverseKin(0, desc_pos=desc_pos1, config=-1)
    print(f"dcs1 GetInverseKin rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, inverseRtn = robot.GetInverseKinRef(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, hasResult = robot.GetInverseKinHasSolution(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef result {hasResult}")
    error, forwordResult = robot.GetForwardKin(j1)
    print(f"jpos1 forwordResult rtn is {forwordResult[0]}, {forwordResult[1]}, {forwordResult[2]}, "
          f"{forwordResult[3]}, {forwordResult[4]}, {forwordResult[5]}")
    robot.CloseRPC()

Consultar Dados do Ponto de Gerenciamento de Ensino do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotTeachingPoint(name)``"
    "Descrição", "Consulta os dados do ponto de gerenciamento de ensino do robô"
    "Parâmetros Obrigatórios", "``name``: Nome do ponto"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``[x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4]``: Dados do ponto"

Obter Parâmetros de Compensação DH
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDHCompensation()``"
    "Descrição", "Obtém os parâmetros de compensação DH"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``dhCompensation=[cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]``: Valores de compensação dos parâmetros DH do robô (mm)"

Obter Código SN do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotSN()``"
    "Descrição", "Obtém o código SN do painel de controle"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``SNCode``: Código SN do painel de controle"

Exemplo de Código para Consultar Dados do Ponto de Gerenciamento de Ensino do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    name = "P1"
    rtn, data = robot.GetRobotTeachingPoint(name)
    print(f"{rtn} name is: {name}")
    for i in range(20):
        print(f"data is: {data[i]}")
    rtn,que_len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength rtn is: {rtn}, queue length is: {que_len}")
    retval,dh = robot.GetDHCompensation()
    print(f"retval is: {retval}")
    print(f"dh is: {dh[0]} {dh[1]} {dh[2]} {dh[3]} {dh[4]} {dh[5]}")
    error,sn = robot.GetRobotSN()
    print(f"robot SN is {sn[0]}")
    robot.CloseRPC()

Obter Sistema de Coordenadas da Ferramenta por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolCoordWithID(id)``"
    "Descrição", "Obtém o sistema de coordenadas da ferramenta por ID"
    "Parâmetros Obrigatórios", "- ``id``: Número do sistema de coordenadas da ferramenta"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "
    - Código de erro, 0-sucesso; diferente de zero-erro
    - ``coord``: Valores do sistema de coordenadas
    - ``type``: Tipo de ferramenta (opcional) 0-ferramenta; 1-sensor
    - ``install``: Posição de instalação (opcional) 0-extremidade do robô; 1-externa ao robô
    - ``toolID``: ID da ferramenta
    - ``loadNo``: Número de carga
    "

Obter Sistema de Coordenadas da Peça por ID
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetWObjCoordWithID(id)``"
    "Descrição", "Obtém o sistema de coordenadas da peça por ID"
    "Parâmetros Obrigatórios", "- ``id``: Número do sistema de coordenadas da peça"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "
    - Código de erro, 0-sucesso; diferente de zero-erro
    - ``coord``: Valores do sistema de coordenadas
    - ``refFrame``: Sistema de coordenadas de referência
    "

Obter Sistema de Coordenadas da Ferramenta Externa por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetExToolCoordWithID(id)``"
    "Descrição", "Obtém o sistema de coordenadas da ferramenta externa por ID"
    "Parâmetros Obrigatórios", "- ``id``: Número do sistema de coordenadas da ferramenta externa"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "
    - Código de erro, 0-sucesso; diferente de zero-erro
    - ``coord``: Valores do sistema de coordenadas
    - ``tcoord``: Pose do sistema de coordenadas da peça montado na extremidade do robô (6 valores: [x, y, z, rx, ry, rz])
    "

Obter Sistema de Coordenadas do Eixo Estendido por ID
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetExAxisCoordWithID(id)``"
    "Descrição", "Obtém o sistema de coordenadas do eixo estendido por ID"
    "Parâmetros Obrigatórios", "- ``id``: Número do sistema de coordenadas do eixo estendido"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "
    - Código de erro, 0-sucesso; diferente de zero-erro
    - ``coord``: Valores do sistema de coordenadas
    - ``axisCoordNum``: Número do eixo estendido (opcional) bit0-bit3 correspondem aos eixos estendidos 1-4; por exemplo, valor 3 corresponde aos eixos estendidos [1,2]
    - ``calibFlag``: Flag de calibração (opcional) 0-não calibrado; 1-calibrado
    "

Obter Massa da Carga e Centro de Gravidade por Número
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTargetPayloadWithID(id)``"
    "Descrição", "Obtém a massa da carga e o centro de gravidade pelo número"
    "Parâmetros Obrigatórios", "- ``id``: Número do sistema de coordenadas do eixo de extensão"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``weight``: Massa da carga
    - ``cog``: Centro de gravidade da carga"

Obter Sistema de Coordenadas da Ferramenta Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetCurToolCoord()``"
    "Descrição", "Obtém o sistema de coordenadas da ferramenta atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Valor do sistema de coordenadas"

Obter Sistema de Coordenadas da Peça Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetCurWObjCoord()``"
    "Descrição", "Obtém o sistema de coordenadas da peça atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Valor do sistema de coordenadas"

Obter Sistema de Coordenadas da Ferramenta Externa Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetCurExToolCoord()``"
    "Descrição", "Obtém o sistema de coordenadas da ferramenta externa atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Valor do sistema de coordenadas"

Obter Sistema de Coordenadas do Eixo de Extensão Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetCurExAxisCoord()``"
    "Descrição", "Obtém o sistema de coordenadas do eixo de extensão atual"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Valor do sistema de coordenadas"

Exemplo de Código para Obter Sistemas de Coordenadas e Carga do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time

    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  

        time.sleep(2)

        id = 1
        rtn, toolCoord, type_val, install, toolID, loadNo = robot.GetToolCoordWithID(id)
        print(f"GetToolCoordWithID {id}, {toolCoord[0]:.6f} {toolCoord[1]:.6f} {toolCoord[2]:.6f} {toolCoord[3]:.6f} {toolCoord[4]:.6f} {toolCoord[5]:.6f},  type = {type_val}, install = {install}, toolID = {toolID}, loadNo = {loadNo}")
        rtn, wobjCoord, refFrame = robot.GetWObjCoordWithID(id)
        print(f"GetWObjCoordWithID {id}, {wobjCoord[0]:.6f} {wobjCoord[1]:.6f} {wobjCoord[2]:.6f} {wobjCoord[3]:.6f} {wobjCoord[4]:.6f} {wobjCoord[5]:.6f}, refFrame = {refFrame}")
        rtn, extoolCoord, exworkpieceCoord = robot.GetExToolCoordWithID(21)
        print(f"GetExToolCoordWithID {id}, {extoolCoord[0]:.6f} {extoolCoord[1]:.6f} {extoolCoord[2]:.6f} {extoolCoord[3]:.6f} {extoolCoord[4]:.6f} {extoolCoord[5]:.6f}, {exworkpieceCoord[0]:.6f} {exworkpieceCoord[1]:.6f} {exworkpieceCoord[2]:.6f} {exworkpieceCoord[3]:.6f} {exworkpieceCoord[4]:.6f} {exworkpieceCoord[5]:.6f}")
        rtn, exAxisCoord, axisCoordNum, calibFlag = robot.GetExAxisCoordWithID(id)
        print(f"GetExAxisCoordWithID {id}, {exAxisCoord[0]:.6f} {exAxisCoord[1]:.6f} {exAxisCoord[2]:.6f} {exAxisCoord[3]:.6f} {exAxisCoord[4]:.6f} {exAxisCoord[5]:.6f}, axisCoordNum = {axisCoordNum}, calibFlag = {calibFlag}")
        rtn, weight, cog = robot.GetTargetPayloadWithID(id)
        print(f"GetTargetPayloadWithID {id}, {weight:.6f} {cog[0]:.6f} {cog[1]:.6f} {cog[2]:.6f}")
        rtn, toolCoord = robot.GetCurToolCoord()
        print(f"GetCurToolCoord {toolCoord[0]:.6f} {toolCoord[1]:.6f} {toolCoord[2]:.6f} {toolCoord[3]:.6f} {toolCoord[4]:.6f} {toolCoord[5]:.6f}")
        rtn, wobjCoord = robot.GetCurWObjCoord()
        print(f"GetCurWObjCoord {wobjCoord[0]:.6f} {wobjCoord[1]:.6f} {wobjCoord[2]:.6f} {wobjCoord[3]:.6f} {wobjCoord[4]:.6f} {wobjCoord[5]:.6f}")
        rtn, extoolCoord = robot.GetCurExToolCoord()
        print(f"GetCurExToolCoord {extoolCoord[0]:.6f} {extoolCoord[1]:.6f} {extoolCoord[2]:.6f} {extoolCoord[3]:.6f} {extoolCoord[4]:.6f} {extoolCoord[5]:.6f}")

        rtn, exAxisCoord = robot.GetCurExAxisCoord()
        print(f"GetCurExAxisCoord {exAxisCoord[0]:.6f} {exAxisCoord[1]:.6f} {exAxisCoord[2]:.6f} {exAxisCoord[3]:.6f} {exAxisCoord[4]:.6f} {exAxisCoord[5]:.6f}")
        rtn, weightT = robot.GetTargetPayload(0)
        rtn, cogT = robot.GetTargetPayloadCog(0)
        print(f"GetTargetPayload {weightT:.6f} {cogT[0]:.6f} {cogT[1]:.6f} {cogT[2]:.6f}")
        coordSet = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

        rtn = robot.SetToolCoord(1, coordSet, 0, 0, 1, 0)
        print(f"SetToolCoord rtn is {rtn}")

        rtn = robot.SetWObjCoord(1, coordSet, 0)
        print(f"SetWObjCoord rtn is {rtn}")

        rtn = robot.SetLoadWeight(1, 1.3)
        print(f"SetLoadWeight rtn is {rtn}")

        rtn = robot.SetLoadCoord(10.0, 20.0, 30.0,1)
        print(f"SetLoadCoord rtn is {rtn}")

        etcp = [0.0, 0.0, 100.0, 0.0, 0.0, 0.0]
        etool = [0.0, 0.0, 50.0, 0.0, 0.0, 0.0]
        rtn = robot.SetExToolCoord(21, etcp, etool)
        print(f"SetExToolCoord rtn is {rtn}")

        rtn = robot.ExtAxisActiveECoordSys(1, 1, coordSet, 1)
        print(f"ExtAxisActiveECoordSys rtn is {rtn}")

        robot.CloseRPC()

    if __name__ == "__main__":
        main()