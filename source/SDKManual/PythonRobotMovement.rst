Movimento do Robô
========================

.. toctree::
    :maxdepth: 5

Movimento Jog
+++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``StartJOG(ref, nb, dir, max_dis, vel=20.0, acc=100.0)``"
    "Descrição", "Movimento jog"
    "Parâmetros obrigatórios", "- ``ref``: 0-jog por junta, 2-jog no sistema de coordenadas base, 4-jog no sistema de coordenadas da ferramenta, 8-jog no sistema de coordenadas da peça;
    - ``nb``: 1-junta1 (eixo X), 2-junta2 (eixo Y), 3-junta3 (eixo Z), 4-junta4 (rx), 5-junta5 (ry), 6-junta6 (rz);
    - ``dir``: 0-direção negativa, 1-direção positiva;
    - ``max_dis``: Ângulo/distância máxima por movimento jog, em ° ou mm;"
    "Parâmetros padrão", "- ``vel``: Percentagem de velocidade, [0~100], padrão 20;
    - ``acc``: Percentagem de aceleração, [0~100], padrão 100;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parada Desacelerada do Movimento Jog
++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``StopJOG(ref)``"
    "Descrição", "Parada desacelerada do movimento jog"
    "Parâmetros obrigatórios", "- ``ref``: 1-parada de jog por junta, 3-parada de jog no sistema de coordenadas base, 5-parada de jog no sistema de coordenadas da ferramenta, 9-parada de jog no sistema de coordenadas da peça"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parada Imediata do Movimento Jog
++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ImmStopJOG()``"
    "Descrição", "Parada imediata do movimento jog"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle de Movimento Jog do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    for i in range(6):
        robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(5)
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(9)
        time.sleep(1)
    robot.CloseRPC()

Movimento no Espaço Articular
++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveJ(joint_pos, tool, user, desc_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel=20.0, acc=0.0, ovl=100.0, exaxis_pos=[0.0,0.0,0.0,0.0], blendT=-1.0, offset_flag=0, offset_pos=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "Descrição", "Movimento no espaço articular"
    "Parâmetros obrigatórios", "- ``joint_pos``: Posição articular alvo, em [°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``desc_pos``: Pose cartesiana alvo, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática direta;
    - ``vel``: Percentagem de velocidade, [0~100], padrão 20.0;
    - ``acc``: Percentagem de aceleração, [0~100], temporariamente não disponível;
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``blendT``: [-1.0]-movimento até o final (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), unidade [ms], padrão -1.0;
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``offset_pos``: Deslocamento de pose, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0];"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento Linear no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveL(desc_pos, tool, user, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, blendMode=0, exaxis_pos=[0.0, 0.0, 0.0, 0.0], search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], oacc=100.0, config=-1, velAccParamMode=0, overSpeedStrategy=0, speedPercent=10)``"
    "Descrição", "Movimento linear no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``desc_pos``: Pose cartesiana alvo, unidades [mm][°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``joint_pos``: Posição articular alvo, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``vel``: Percentagem de velocidade, [0~100], padrão 20.0;
    - ``acc``: Percentagem de aceleração, [0~100], temporariamente não disponível, padrão 0.0;
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``blendR``: [-1.0]-movimento até o final (bloqueante), [0~1000]-raio de suavização (não bloqueante), unidade [mm], padrão -1.0;
    - ``blendMode``: Modo de transição; 0-transição tangente; 1-transição de canto, padrão 0;
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``search``: [0]-sem busca de posição do arame, [1]-com busca de posição do arame;
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``offset_pos``: Deslocamento de pose, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``oacc``: Fator de escala de aceleração [0-100]/aceleração física (mm/s²), padrão 100;
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular, padrão -1;
    - ``velAccParamMode``: Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s²), padrão 0;
    - ``overSpeedStrategy``: Estratégia de tratamento de excesso de velocidade, 0-estratégia desativada; 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0;
    - ``speedPercent``: Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    "
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento Circular no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveC(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_p=20.0, acc_p=100.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], offset_flag_p=0, offset_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, exaxis_pos_t=[0.0, 0.0, 0.0, 0.0], offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0, oacc=100.0, config=-1, velAccParamMode=0)``"
    "Descrição", "Movimento circular no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``desc_pos_p``: Pose cartesiana do ponto de passagem, unidades [mm][°];
    - ``tool_p``: Número da ferramenta do ponto de passagem, [0~14];
    - ``user_p``: Número da peça do ponto de passagem, [0~14];
    - ``desc_pos_t``: Pose cartesiana do ponto alvo, unidades [mm][°];
    - ``tool_t``: Número da ferramenta, [0~14];
    - ``user_t``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``joint_pos_p``: Posição articular do ponto de passagem, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``joint_pos_t``: Posição articular do ponto alvo, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``vel_p``: Percentagem de velocidade do ponto de passagem, [0~100], padrão 20.0;
    - ``acc_p``: Percentagem de aceleração do ponto de passagem, [0~100], temporariamente não disponível, padrão 0.0;
    - ``exaxis_pos_p``: Posição do eixo externo do ponto de passagem 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``offset_flag_p``: Se o ponto de passagem tem deslocamento [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``vel_t``: Percentagem de velocidade do ponto alvo, [0~100], padrão 20.0;
    - ``acc_t``: Percentagem de aceleração do ponto alvo, [0~100], temporariamente não disponível, padrão 0.0;
    - ``exaxis_pos_t``: Posição do eixo externo do ponto alvo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``offset_flag_t``: Se o ponto alvo tem deslocamento [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``offset_pos_t``: Deslocamento de pose do ponto alvo, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``blendR``: [-1.0]-movimento até o final (bloqueante), [0~1000]-raio de suavização (não bloqueante), unidade [mm], padrão -1.0;
    - ``oacc``: Fator de escala de aceleração [0-100]/aceleração física (mm/s²), padrão 100;
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular, padrão -1;
    - ``velAccParamMode``: Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s²), padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento Circular Completo no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``Circle(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_p=20.0, acc_p=0.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=0.0, exaxis_pos_t=[0.0, 0.0, 0.0, 0.0], ovl=100.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], oacc=100.0, blendR=-1, config=-1, velAccParamMode=0)``"
    "Descrição", "Movimento circular completo no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``desc_pos_p``: Pose cartesiana do ponto de passagem, unidades [mm][°];
    - ``tool_p``: Número da ferramenta, [0~14];
    - ``user_p``: Número da peça, [0~14];
    - ``desc_pos_t``: Pose cartesiana do ponto alvo, unidades [mm][°];
    - ``tool_t``: Número da ferramenta, [0~14];
    - ``user_t``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``joint_pos_p``: Posição articular do ponto de passagem, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``joint_pos_t``: Posição articular do ponto alvo, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``vel_p``: Percentagem de velocidade, [0~100], padrão 20.0;
    - ``acc_p``: Percentagem de aceleração do ponto de passagem, [0~100], temporariamente não disponível, padrão 0.0;
    - ``exaxis_pos_p``: Posição do eixo externo do ponto de passagem 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``vel_t``: Percentagem de velocidade do ponto alvo, [0~100], padrão 20.0;
    - ``acc_t``: Percentagem de aceleração do ponto alvo, [0~100], temporariamente não disponível, padrão 0.0;
    - ``exaxis_pos_t``: Posição do eixo externo do ponto alvo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``offset_flag``: Se tem deslocamento [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``offset_pos``: Deslocamento de pose, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``oacc``: Fator de escala de aceleração [0-100]/aceleração física (mm/s²), padrão 100;
    - ``blendR``: -1: bloqueante; 0~1000: raio de suavização, padrão -1;
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular, padrão -1;
    - ``velAccParamMode``: Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s²), padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento Ponto a Ponto no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveCart(desc_pos, tool, user, vel=20.0, acc=0.0, ovl=100.0, blendT=-1.0, config=-1)``"
    "Descrição", "Movimento ponto a ponto no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``desc_pos``: Posição cartesiana alvo;
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``vel``: Velocidade, intervalo [0~100], padrão 20.0;
    - ``acc``: Aceleração, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``blendT``: [-1.0]-movimento até o final (bloqueante), [0~500]-tempo de suavização (não bloqueante), unidade [ms], padrão -1.0;
    - ``config``: Configuração articular, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base na configuração articular, padrão -1"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Instruções Básicas de Movimento do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    j4 = [-31.154, -95.317, 94.276, -88.079, -89.740, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    desc_pos4 = [-443.165, 147.881, 480.951, 179.511, -0.775, -15.409]
    offset_pos = [0.0] * 6
    epos = [0.0] * 4
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    oacc = 100.0
    blendT = 0.0
    blendR = 0.0
    flag = 0
    search = 0
    blendMode = 0
    velAccMode = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos, oacc=oacc, velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, oacc=oacc, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl, offset_flag=flag, offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    rtn = robot.MoveCart(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendT=blendT, config=-1)
    print(f"MoveCart errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos, config=-1, velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, config=-1, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl, offset_flag=flag, offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    robot.CloseRPC()
    return 0

Movimento Helicoidal no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``NewSpiral(desc_pos, tool, user, param, joint_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel=20.0, acc=0.0, exaxis_pos=[0.0,0.0,0.0,0.0], ovl=100.0, offset_flag=0, offset_pos=[0.0,0.0,0.0,0.0,0.0,0.0], config=-1)``"
    "Descrição", "Movimento helicoidal no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``desc_pos``: Pose cartesiana alvo, unidades [mm][°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];
    - ``param=[circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]``: circle_num: Número de voltas da espiral; circle_angle: Ângulo de inclinação da espiral; rad_init: Raio inicial da espiral; rad_add: Incremento do raio; rotaxis_add: Incremento na direção do eixo de rotação; rot_direction: Direção de rotação, 0-horário, 1-anti-horário; velAccMode: Modo de parâmetro de velocidade/aceleração: 0-velocidade angular constante, 1-velocidade linear constante;"
    "Parâmetros padrão", "- ``joint_pos``: Posição articular alvo, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``vel``: Percentagem de velocidade, [0~100], padrão 20.0;
    - ``acc``: Percentagem de aceleração, [0~100], padrão 100.0;
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0];
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0;
    - ``offset_pos``: Deslocamento de pose, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular, padrão -1"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código
++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j = [67.957, -81.482, 87.595, -95.691, -94.899, -9.727]
    desc_pos = [-123.142, -551.735, 430.549, 178.753, -4.757, 167.754]
    offset_pos1 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    offset_pos2 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    epos = [0.0] * 4
    sp = [2, 30.0, 50.0, 10.0, 10.0, 0, 1]  # [circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]
    tool = 0
    user = 0
    vel = 30.0
    acc = 60.0
    ovl = 100.0
    blendT = -1.0
    flag = 2
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos1)
    print(f"movej errcode:{rtn}")
    rtn = robot.NewSpiral(desc_pos=desc_pos, tool=tool, user=user, vel=vel, acc=acc, exaxis_pos=epos, ovl=ovl, offset_flag=flag, offset_pos=offset_pos2, param=sp)
    print(f"newspiral errcode:{rtn}")
    robot.CloseRPC()
    return 0

Início do Movimento Servo
++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoMoveStart(cmdType=0)``"
    "Descrição", "Início do movimento servo, para uso com instruções ServoJ e ServoCart"
    "Parâmetros obrigatórios", "- ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do Movimento Servo
++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoMoveEnd(cmdType=0)``"
    "Descrição", "Fim do movimento servo, para uso com instruções ServoJ e ServoCart"
    "Parâmetros obrigatórios", "- ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento no Modo Servo no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoJ(joint_pos, axisPos, acc=0.0, vel=0.0, cmdT=0.008, filterT=0.0, gain=0.0, id=0, cmdType=0)``"
    "Descrição", "Movimento no modo servo no espaço articular"
    "Parâmetros obrigatórios", "- ``joint_pos``: Posição articular alvo, em [°];
    - ``axisPos``: Posição do eixo externo, em mm;"
    "Parâmetros padrão", "- ``acc``: Aceleração, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``vel``: Velocidade, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``cmdT``: Período de envio de instrução, em s, intervalo recomendado [0.001~0.0016], padrão 0.008;
    - ``filterT``: Tempo de filtro, em [s], temporariamente não disponível, padrão 0.0;
    - ``gain``: Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0.0;
    - ``id``: ID da instrução ServoJ, padrão 0;
    - ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK para ServoJ, ServoMoveStart, ServoMoveEnd com comunicação UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestServoJUDP(self):
        # Definir retorno de chamada
        def callback(src_type, count, cmd_id, data_len, content):
            print("Função de retorno de chamada: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        # # Inicializar posição articular e posição do eixo externo
        j = [105, -108, 74, -66, -88.893, -1.621]
        offset_pos = [0, 0, 0, 0, 0, 0]
        epos = [0, 0, 0, 0]
        # # Mover para posição inicial
        result = robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        print("Resultado de MoveJ: {}".format(result))
        vel = 0.0
        acc = 0.0
        cmdT = 0.016
        filterT = 0.0
        gain = 0.0
        flag = 0
        dt = 0.1
        cmdID = 0

        # Obter posição articular atual
        ret, j = robot.GetActualJointPosDegree(flag)
        if ret != 0:
            print(f"GetActualJointPosDegree errcode:{ret}")
        while 1:
            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("Resultado de ServoMoveStart: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT, filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] += dt
                j[1] += dt
                j[2] += dt
                j[3] += dt
                j[4] += dt
                j[5] += dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("Resultado de ServoMoveEnd: {}".format(result))

            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("Resultado de ServoMoveStart: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT, filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] -= dt
                j[1] -= dt
                j[2] -= dt
                j[3] -= dt
                j[4] -= dt
                j[5] -= dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("Resultado de ServoMoveEnd: {}".format(result))
        robot.CloseRPC()
        return 0

    TestServoJUDP(robot)

Exemplo de Código de Movimento no Modo Servo no Espaço Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j = [0.0] * 6
    epos = [0.0] * 4
    vel = 0.0
    acc = 0.0
    cmdT = 0.008
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 500
    dt = 0.1
    cmdID = 0
    ret, j = robot.GetActualJointPosDegree(flag)
    if ret == 0:
        cmdID += 1
        robot.ServoMoveStart()
        while count:
            robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT, filterT=filterT, gain=gain, id=cmdID)
            j[4] += dt
            count -= 1
            time.sleep(cmdT)
            rtn, pkg = robot.GetRobotRealTimeState()
            print(f"Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")

            if count < 50:
                robot.MotionQueueClear()
                print(f"After queue clear, Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")
                break
        robot.ServoMoveEnd()
    else:
        print(f"GetActualJointPosDegree errcode:{ret}")
    robot.CloseRPC()

Início do Controle de Torque Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoJTStart(cmdType=0)``"
    "Descrição", "Início do controle de torque articular"
    "Parâmetros obrigatórios", "- ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Controle de Torque Articular
+++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoJT(torque, interval, checkFlag=0, jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], cmdType=0)``"
    "Descrição", "Controle de torque articular"
    "Parâmetros obrigatórios", "- ``torque``: Torque das juntas j1~j6, em Nm
                - ``interval``: Período de instrução, em s, intervalo [0.001~0.008]
                - ``checkFlag``: Estratégia de detecção 0-sem limitação; 1-limitação de potência; 2-limitação de velocidade; 3-limitação simultânea de potência e velocidade, padrão 0
                - ``jPowerLimit``: Parâmetros padrão jPowerLimit Limite máximo de potência da junta (W), padrão [0.0,0.0,0.0,0.0,0.0,0.0]
                - ``jVelLimit``: Velocidade máxima da junta (°/s), padrão [0.0,0.0,0.0,0.0,0.0,0.0]
                - ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do Controle de Torque Articular
+++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoJTEnd(cmdType=0)``"
    "Descrição", "Fim do controle de torque articular"
    "Parâmetros obrigatórios", "- ``cmdType``: Tipo de transmissão de comando, 0=XML-RPC, 1=transmissão transparente UDP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK para ServoJT, ServoJTStart, ServoJTEnd com comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestServoJTUDP(self):
        # Definir retorno de chamada
        def callback(src_type, count, cmd_id, data_len, content):
            print("Função de retorno de chamada: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        while True:
            # Inicializar posição articular e posição do eixo externo
            j = [0, -90, 90, 0, 0, 0]
            epos = [0, 0, 0, 0]
            offset_pos = [0, 0, 0, 0, 0, 0]

            # Mover para posição inicial
            robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
            time.sleep(3)
            # Ativar arrasto para ensino
            result = robot.DragTeachSwitch(1)
            print("Resultado de DragTeachSwitch: {}".format(result))
            torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # Obter torque das juntas
            ret, torques = robot.GetJointTorques(flag=1)
            if ret != 0:
                print(f"GetJointTorques errcode:{ret}")

            count = 100
            result = robot.ServoJTStart(cmdType=1)
            print("Resultado de ServoJTStart: {}".format(result))
            # Controle de torque positivo
            while True:
                torques[0] = 0.03
                result = robot.ServoJT(
                    torque=torques,
                    interval=0.001,
                    checkFlag=0,
                    jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    cmdType=1
                )
                print("Resultado: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] > 30:
                    break

            # Controle de torque negativo
            while True:
                torques[0] = -0.03
                result = robot.ServoJT(
                        torque=torques,
                        interval=0.001,
                        checkFlag=0,
                        jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        cmdType=1
                    )
                print("Resultado: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] < 0:
                    break

            # Finalizar controle de torque e desativar arrasto para ensino
            result = robot.ServoJTEnd(cmdType=1)
            print("Resultado de ServoJTEnd: {}".format(result))
            result = robot.DragTeachSwitch(0)
            print("Resultado de DragTeachSwitch: {}".format(result))

        robot.CloseRPC()
        return 0

    TestServoJTUDP(robot)

Exemplo de Código de Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    # torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error, torques = robot.GetJointTorques(1)
    robot.ServoJTStart()
    count = 100
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

Movimento no Modo Servo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ServoCart(mode, desc_pos, exaxis, pos_gain=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0], acc=0.0, vel=0.0, cmdT=0.008, filterT=0.0, gain=0.0)``"
    "Descrição", "Movimento no modo servo no espaço cartesiano"
    "Parâmetros obrigatórios", "- ``mode``: [0]-movimento absoluto (sistema de coordenadas base), [1]-movimento incremental (sistema de coordenadas base), [2]-movimento incremental (sistema de coordenadas da ferramenta);
    - ``exaxis``: Posição do eixo estendido;
    - ``desc_pos``: Posição cartesiana alvo/incremento da posição cartesiana alvo;"
    "Parâmetros padrão", "- ``pos_gain``: Coeficiente de escala do incremento de pose, ativo apenas em movimento incremental, intervalo [0~1], padrão [1.0, 1.0, 1.0, 1.0, 1.0, 1.0];
    - ``acc``: Aceleração, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``vel``: Velocidade, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``cmdT``: Período de envio de instrução, em s, intervalo recomendado [0.001~0.0016], padrão 0.008;
    - ``filterT``: Tempo de filtro, em [s], temporariamente não disponível, padrão 0.0;
    - ``gain``: Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0.0;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Movimento no Modo Servo no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    desc_pos_dt = [83.00800, 50.525000, 29.246, 179.629, -7.138, -166.975]
    exaxis = [100.0, 0.0, 0.0, 0.0]
    pos_gain = [0.0] * 6
    mode = 0
    vel = 0.0
    acc = 0.0
    cmdT = 0.001
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 5000
    robot.SetSpeed(20)
    while count:
        rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain)
        print(f"ServoCart rtn is {rtn}")
        count -= 1
        desc_pos_dt[0] += 0.01
        exaxis[0] += 0.01
    robot.CloseRPC()
    return 0

Início do Movimento Spline
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SplineStart()``"
    "Descrição", "Início do movimento spline"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Movimento Spline PTP
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SplinePTP(joint_pos, tool, user, desc_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel=20.0, acc=100.0, ovl=100.0)``"
    "Descrição", "Movimento spline PTP"
    "Parâmetros obrigatórios", "- ``joint_pos``: Posição articular alvo, em [°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];"
    "Parâmetros padrão", "- ``desc_pos``: Pose cartesiana alvo, unidades [mm][°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática direta;
    - ``vel``: Velocidade, intervalo [0~100], padrão 20.0;
    - ``acc``: Aceleração, intervalo [0~100], padrão 100.0;
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do Movimento Spline
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SplineEnd()``"
    "Descrição", "Fim do movimento spline"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    joint_points = [
        [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256],  # j1
        [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255],  # j2
        [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260],  # j3
        [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]  # j4
    ]
    cart_points = [
        [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833],  # desc_pos1
        [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869],  # desc_pos2
        [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207],  # desc_pos3
        [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]  # desc_pos4
    ]
    offset_pos = [0] * 6
    epos = [0] * 4
    tool = user = 0
    vel = acc = ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=joint_points[0], tool=tool, user=user, vel=vel)
    print(f"MoveJ 错误码: {err1}")
    robot.SplineStart()
    robot.SplinePTP(joint_pos=joint_points[0], tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[1], tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[2], tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[3], tool=tool, user=user)
    robot.SplineEnd()
    robot.CloseRPC()

Início do Novo Movimento Spline
+++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.3

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``NewSplineStart(type, averageTime=2000)``"
    "Descrição", "Início do novo movimento spline"
    "Parâmetros obrigatórios", "- ``type``: 0-transição circular, 1-pontos fornecidos são pontos de caminho"
    "Parâmetros padrão", "- ``averageTime``: Tempo médio global de transição (ms), padrão 2000"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Ponto de Instrução do Novo Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``NewSplinePoint(desc_pos, tool, user, lastFlag, joint_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel=0.0, acc=0.0, ovl=100.0, blendR=0.0)``"
    "Descrição", "Ponto de instrução do novo spline"
    "Parâmetros obrigatórios", "- ``desc_pos``: Pose cartesiana alvo, unidades [mm][°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];
    - ``lastFlag``: Se é o último ponto, 0-não, 1-sim;"
    "Parâmetros padrão", "- ``joint_pos``: Posição articular alvo, unidade [°], padrão [0.0,0.0,0.0,0.0,0.0,0.0], valor padrão é o retorno da solução de cinemática inversa;
    - ``vel``: Velocidade, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``acc``: Aceleração, intervalo [0~100], temporariamente não disponível, padrão 0.0;
    - ``ovl``: Fator de escala de velocidade, [0~100], padrão 100.0;
    - ``blendR``: [0~1000]-raio de suavização, unidade [mm], padrão 0.0;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do Novo Movimento Spline
+++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``NewSplineEnd()``"
    "Descrição", "Fim do novo movimento spline"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código do Novo Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260]
    j4 = [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]
    j5 = [-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    desc_pos4 = [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    print(f"movej errcode:{err1}")
    robot.NewSplineStart(1, 2000)
    robot.NewSplinePoint(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos3, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos5, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplineEnd()
    robot.CloseRPC()

Parar Movimento do Robô
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``StopMotion()``"
    "Descrição", "Parar movimento, o uso de parar movimento requer que a instrução de movimento esteja em estado não bloqueante"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Pausar Movimento do Robô
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PauseMotion()``"
    "Descrição", "Pausar movimento, o uso de pausar movimento requer que a instrução de movimento esteja em estado não bloqueante"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Retomar Movimento do Robô
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ResumeMotion()``"
    "Descrição", "Retomar movimento, o uso de retomar movimento requer que a instrução de movimento esteja em estado não bloqueante"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Pausa, Retomada e Parada de Movimento
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j5 = [-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    rtn = robot.MoveJ(joint_pos=j5, tool=tool, user=user, vel=vel, blendT=1)
    time.sleep(1)
    robot.PauseMotion()
    time.sleep(1)
    robot.ResumeMotion()
    time.sleep(1)
    robot.StopMotion()
    time.sleep(1)
    robot.CloseRPC()

Início do Deslocamento Global de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PointsOffsetEnable(flag, offset_pos)``"
    "Descrição", "Início do deslocamento global de pontos"
    "Parâmetros obrigatórios", "- ``flag``: 0-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta;
    - ``offset_pos``: Quantidade de deslocamento, unidades [mm][°]."
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do Deslocamento Global de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PointsOffsetDisable()``"
    "Descrição", "Fim do deslocamento global de pontos"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Deslocamento de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    time.sleep(1)
    robot.PointsOffsetEnable(flag=0, offset_pos=offset_pos1)
    robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.PointsOffsetDisable()
    robot.CloseRPC()

Início do AO de Movimento da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveAOStart(AONum, maxTCPSpeed=1000, maxAOPercent=100, zeroZoneCmp=20)``"
    "Descrição", "Início do AO de movimento da caixa de controle"
    "Parâmetros obrigatórios", "- ``AONum``: Número da AO da caixa de controle"
    "Parâmetros padrão", "
    - ``maxTCPSpeed``: Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000;
    - ``maxAOPercent``: Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%;
    - ``zeroZoneCmp``: Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]."
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do AO de Movimento da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveAOStop()``"
    "Descrição", "Fim do AO de movimento da caixa de controle"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início do AO de Movimento da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToolAOStart(AONum, maxTCPSpeed=1000, maxAOPercent=100, zeroZoneCmp=20)``"
    "Descrição", "Início do AO de movimento da extremidade"
    "Parâmetros obrigatórios", "- ``AONum``: Número da AO da extremidade"
    "Parâmetros padrão", "
    - ``maxTCPSpeed``: Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000;
    - ``maxAOPercent``: Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%;
    - ``zeroZoneCmp``: Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]."
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim do AO de Movimento da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToolAOStop()``"
    "Descrição", "Fim do AO de movimento da extremidade"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Captura com AO
+++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 20.0
    acc = 20.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveAOStop()
    time.sleep(1)
    robot.MoveToolAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveToolAOStop()
    robot.CloseRPC()

Início do Filtro FIR para Movimento Ptp
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PtpFIRPlanningStart(maxAcc, maxJek)``"
    "Descrição", "Início do filtro FIR para movimento Ptp"
    "Parâmetros obrigatórios", "- ``maxAcc``: Valor extremo máximo de aceleração (deg/s²)
    - ``maxJek``: Valor extremo de jerk uniforme das juntas (deg/s³)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desligar o Filtro FIR para Movimento Ptp
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PtpFIRPlanningEnd()``"
    "Descrição", "Desligar o filtro FIR para movimento Ptp"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início do Filtro FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LinArcFIRPlanningStart(maxAccLin, maxAccDeg, maxJerkLin, maxJerkDeg)``"
    "Descrição", "Início do filtro FIR para movimento LIN e ARC"
    "Parâmetros obrigatórios", "- ``maxAccLin``: Valor extremo de aceleração linear (mm/s²)
    - ``maxAccDeg``: Valor extremo de aceleração angular (deg/s²)
    - ``maxJerkLin``: Valor extremo de jerk linear (mm/s³)
    - ``maxJerkDeg``: Valor extremo de jerk angular (deg/s³)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desligar o Filtro FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LinArcFIRPlanningEnd()``"
    "Descrição", "Desligar o filtro FIR para movimento LIN e ARC"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Filtro FIR
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    midjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    endjointPos = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    middescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    enddescPose = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.PtpFIRPlanningStart(1000.0, 1000.0)
    print(f"PtpFIRPlanningStart rtn is {rtn}")
    error = robot.MoveJ(joint_pos=startjointPos, tool=0, user=0, desc_pos=startdescPose, vel=100, acc=100, ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    error = robot.MoveJ(joint_pos=endjointPos, tool=0, user=0, desc_pos=enddescPose, vel=100, acc=100, ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    robot.PtpFIRPlanningEnd()
    print(f"PtpFIRPlanningEnd rtn is {rtn}")
    rtn = robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000)
    print(f"LinArcFIRPlanningStart rtn is {rtn}")
    error = robot.MoveL(desc_pos=startdescPose, tool=0, user=0, joint_pos=startjointPos, vel=100, overSpeedStrategy=1, speedPercent=1)
    print(f"MoveL rtn is {rtn}")
    error = robot.MoveC(desc_pos_p=middescPose, tool_p=0, user_p=0, joint_pos_p=midjointPos, vel_p=100, desc_pos_t=enddescPose, tool_t=0, user_t=0, joint_pos_t=endjointPos, vel_t=100)
    print(f"MoveC rtn is {rtn}")
    robot.LinArcFIRPlanningEnd()
    print(f"LinArcFIRPlanningEnd rtn is {rtn}")
    robot.CloseRPC()

Ativar Suavização de Aceleração
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AccSmoothStart(saveFlag_flag)``"
    "Descrição", "Ativar suavização de aceleração"
    "Parâmetros obrigatórios", "- ``saveFlag_flag``: Se salvar após desligamento"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desativar Suavização de Aceleração
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AccSmoothEnd(saveFlag_flag)``"
    "Descrição", "Desativar suavização de aceleração"
    "Parâmetros obrigatórios", "- ``saveFlag_flag``: Se salvar após desligamento"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Suavização de Aceleração
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AccSmoothStart(0)
    print(f"AccSmoothStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0, user=0, vel=100)
    robot.MoveJ(joint_pos=endjointPos, tool=0, user=0, vel=100)
    rtn = robot.AccSmoothEnd(0)
    print(f"AccSmoothEnd rtn is {rtn}")

Ativar Velocidade de Postura Especificada do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AngularSpeedStart(ratio)``"
    "Descrição", "Ativar velocidade de postura especificada"
    "Parâmetros obrigatórios", "- ``ratio``: Percentagem da velocidade de postura [0-300]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desativar Velocidade de Postura Especificada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AngularSpeedEnd()``"
    "Descrição", "Desativar velocidade de postura especificada"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Velocidade de Postura Especificada do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AngularSpeedStart(50)
    print(f"AngularSpeedStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0, user=0, vel=100)
    robot.MoveJ(joint_pos=endjointPos, tool=0, user=0, vel=100)
    rtn = robot.AngularSpeedEnd()
    print(f"AngularSpeedEnd rtn is {rtn}")
    robot.CloseRPC()

Ativar Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SingularAvoidStart(protectMode, minShoulderPos=100, minElbowPos=50, minWristPos=10)``"
    "Descrição", "Ativar proteção contra pose singular"
    "Parâmetros obrigatórios", "
    - ``protectMode``: Modo de proteção contra pose singular: 0-modo articular; 1-modo cartesiano
    "
    "Parâmetros padrão", "- ``minShoulderPos``: Faixa de ajuste da singularidade do ombro (mm), padrão 100.0
    - ``minElbowPos``: Faixa de ajuste da singularidade do cotovelo (mm), padrão 50.0
    - ``minWristPos``: Faixa de ajuste da singularidade do pulso (°), padrão 10.0"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Desativar Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SingularAvoidEnd()``"
    "Descrição", "Desativar proteção contra pose singular"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Proteção contra Pose Singular do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SingularAvoidStart(2, 10, 5, 5)
    print(f"SingularAvoidStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0, user=0, vel=100)
    robot.MoveJ(joint_pos=endjointPos, tool=0, user=0, vel=100)
    rtn = robot.SingularAvoidEnd()
    print(f"SingularAvoidEnd rtn is {rtn}")
    robot.CloseRPC()

Limpar Fila de Instruções de Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MotionQueueClear()``"
    "Descrição", "Limpar fila de instruções de movimento"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Mover para Ponto Inicial da Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveToIntersectLineStart(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveType, mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], extAxisFlag=0, exaxisPos=[0.0,0.0,0.0,0.0], moveDirection=0, offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "Descrição", "Mover para ponto inicial da linha de interseção"
    "Parâmetros obrigatórios", "
    - ``mainPoint``: Poses cartesianas dos 6 pontos de ensino do tubo principal
    - ``piecePoint``: Poses cartesianas dos 6 pontos de ensino do tubo auxiliar
    - ``tool``: Número do sistema de coordenadas da ferramenta
    - ``wobj``: Número do sistema de coordenadas da peça
    - ``vel``: Percentagem de velocidade
    - ``acc``: Percentagem de aceleração
    - ``ovl``: Fator de escala de velocidade
    - ``oacc``: Fator de escala de aceleração
    - ``moveType``: Tipo de movimento; 0-PTP; 1-LIN
    - ``mainExaxisPos``: Posições dos eixos estendidos dos 6 pontos de ensino do tubo principal, padrão [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``: Posições dos eixos estendidos dos 6 pontos de ensino do tubo de junção, padrão [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``: Se habilita o eixo estendido; 0-não habilita; 1-habilita
    - ``exaxisPos``: Posição do eixo estendido inicial [0.0,0.0,0.0,0.0]
    - ``moveDirection``: Direção do movimento; 0-horário; 1-anti-horário
    - ``offset``: Deslocamento
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Movimento na Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveIntersectLine(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveDirection, mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], extAxisFlag=0, exaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "Descrição", "Movimento na linha de interseção"
    "Parâmetros obrigatórios", "
    - ``mainPoint``: Poses cartesianas dos 6 pontos de ensino do tubo principal
    - ``piecePoint``: Poses cartesianas dos 6 pontos de ensino do tubo auxiliar
    - ``tool``: Número do sistema de coordenadas da ferramenta
    - ``wobj``: Número do sistema de coordenadas da peça
    - ``vel``: Percentagem de velocidade
    - ``acc``: Percentagem de aceleração
    - ``ovl``: Fator de escala de velocidade
    - ``oacc``: Fator de escala de aceleração
    - ``moveDirection``: Direção do movimento; 0-horário; 1-anti-horário
    - ``mainExaxisPos``: Posições dos eixos estendidos dos 6 pontos de ensino do tubo principal, padrão [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``: Posições dos eixos estendidos dos 6 pontos de ensino do tubo de junção, padrão [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``: Se habilita o eixo estendido; 0-não habilita; 1-habilita
    - ``exaxisPos``: Posição do eixo estendido inicial [0.0,0.0,0.0,0.0]
    - ``offset``: Deslocamento
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Movimento na Linha de Interseção do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    mainPoint = [[0.0] * 6 for _ in range(6)]
    piecePoint = [[0.0] * 6 for _ in range(6)]
    mainExaxisPos = [[0.0] * 4 for _ in range(6)]
    pieceExaxisPos = [[0.0] * 4 for _ in range(6)]
    extAxisFlag = 1
    exaxisPos = [[0.0] * 4 for _ in range(4)]
    offset = [0.0, 2.0, 30.0, -2.0, 0.0, 0.0]
    mainPoint[0] = [490.004, -383.194, 402.735, -9.332, -1.528, 69.594]
    mainPoint[1] = [444.950, -407.117, 389.011, -5.546, -2.196, 65.279]
    mainPoint[2] = [445.168, -463.605, 355.759, -1.544, -10.886, 57.104]
    mainPoint[3] = [507.529, -485.385, 343.013, -0.786, -4.834, 61.799]
    mainPoint[4] = [554.390, -442.647, 367.701, -4.761, -10.181, 64.925]
    mainPoint[5] = [532.552, -394.003, 396.467, -13.732, -13.592, 67.411]
    mainExaxisPos[0] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[1] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[2] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[3] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[4] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[5] = [-29.996, 0.000, 0.000, 0.000]
    piecePoint[0] = [505.571, -192.408, 316.759, 38.098, 37.051, 139.447]
    piecePoint[1] = [533.837, -201.558, 332.340, 34.644, 42.339, 137.748]
    piecePoint[2] = [530.386, -225.085, 373.808, 35.431, 45.111, 137.560]
    piecePoint[3] = [485.646, -229.195, 383.778, 33.870, 45.173, 137.064]
    piecePoint[4] = [460.551, -212.161, 354.256, 28.856, 45.602, 135.930]
    piecePoint[5] = [474.217, -197.124, 324.611, 42.469, 41.133, 148.167]
    pieceExaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[1] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[2] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[3] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[4] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[5] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[1] = [-44.994, 90.000, 0.000, 0.000]
    exaxisPos[2] = [-59.992, 0.002, 0.000, 0.000]
    exaxisPos[3] = [-44.994, -89.997, 0.000, 0.000]
    tool = 2
    wobj = 0
    vel = 100.0
    acc = 100.0
    ovl = 12.0
    oacc = 12.0
    moveType = 1
    moveDirection = 1
    rtn = robot.MoveToIntersectLineStart(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag, exaxisPos=exaxisPos[0], tool=tool, wobj=wobj, vel=vel, acc=acc, ovl=ovl, oacc=oacc, moveType=moveType, moveDirection=moveDirection, offset=offset)
    print(f"MoveToIntersectLineStart rtn is {rtn}")
    rtn = robot.MoveIntersectLine(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag, exaxisPos=exaxisPos, tool=tool, wobj=wobj, vel=vel, acc=acc, ovl=5.0, oacc=5.0, moveDirection=moveDirection, offset=offset)
    print(f"MoveIntersectLine rtn is {rtn}")
    robot.CloseRPC()

Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MoveStationary()``"
    "Descrição", "Movimento estacionário no local"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 0, 10, 100)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    rtn = robot.MoveStationary()
    print(f"MoveStationary rtn is {rtn}")
    rtn = robot.LaserSensorRecord1(0, 10)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    robot.CloseRPC()
    return 0

Início da Oscilação em Ponto Fixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``OriginPointWeaveStart(weaveNum, mode, refPoint, weaveTime)``"
    "Descrição", "Início da oscilação em ponto fixo"
    "Parâmetros obrigatórios", "
    - ``weaveNum``: Número da oscilação [0-7]
    - ``mode``: 0-sistema de coordenadas da ferramenta; 1-ponto de referência
    - ``refPoint``: Coordenadas cartesianas do ponto de referência [x, y, z, a, b, c]
    - ``weaveTime``: Tempo de oscilação [s]
    - "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``OriginPointWeaveEnd()``"
    "Descrição", "Fim da oscilação em ponto fixo"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK de Oscilação em Ponto Fixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestOriginPointWeave(self):
        time.sleep(2)
        # Inicializar posição articular, eixo externo e deslocamento
        j = [39.886, -98.580, -124.032, -47.393, 90.000, 40.842]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        # Posição do ponto de referência [x, y, z, rx, ry, rz]
        refPoint = [400.021, 300.022, 299.996, 179.997, -0.003, -90.956]

        # Mover para posição inicial
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Primeira oscilação: sistema de coordenadas absoluto (tool=0), modo 0
        robot.OriginPointWeaveStart(0, 0, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        time.sleep(2)

        # Mover novamente para posição inicial
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # Segunda oscilação: sistema de coordenadas absoluto (tool=0), modo 1
        robot.OriginPointWeaveStart(0, 1, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        # Fechar conexão
        robot.CloseRPC()
        time.sleep(1)

    TestOriginPointWeave(robot)

Exemplo de Código SDK de Oscilação em Ponto Fixo (incluindo laser e eixo estendido)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestOriginPointWeave(self):
        time.sleep(2)
        # Inicializar posição articular, eixo externo e deslocamento
        j = [39.886, -98.580, -124.032, -47.393, 90.000, 40.842]
        epos1 = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]
        epos2 = [5, 0.000, 0.000, 0.000]
        # Posição do ponto de referência [x, y, z, rx, ry, rz]
        refPoint = [400.021, 300.022, 299.996, 179.997, -0.003, -90.956]

        rtn = 0
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020)
        robot.LaserTrackingSensorSamplePeriod(20)
        robot.LoadPosSensorDriver(101)

        # Carregar driver UDP
        robot.ExtDevLoadUDPDriver()

        # Definir tempo de conclusão do comando do eixo externo
        rtn = robot.SetExAxisCmdDoneTime(5000.0)
        print(f"SetExAxisCmdDoneTime rtn is {rtn}")

        # Habilitar eixos externos 1 e 2
        rtn = robot.ExtAxisServoOn(1, 1)
        print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
        rtn = robot.ExtAxisServoOn(2, 1)
        print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
        time.sleep(2)

        # Definir retorno à origem do eixo externo
        robot.ExtAxisSetHoming(1, 0, 10, 2)
        robot.LaserTrackingLaserOnOff(1)

        # 1---sem eixo estendido
        robot.LaserTrackingTrackOnOff(1, 4)
        time.sleep(0.2)
        # Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 10)
        robot.MoveStationary()  # Executar movimento fixo
        robot.OriginPointWeaveEnd()
        robot.LaserTrackingTrackOnOff(0, 4)

        time.sleep(2)  # Aguardar 2 segundos

        # 2----com eixo estendido
        robot.ExtAxisMove(epos1, 100, -1)
        robot.LaserTrackingTrackOnOff(1, 4)
        # Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 20)
        robot.ExtAxisMove(epos2, 100, -1)
        robot.OriginPointWeaveEnd()
        robot.LaserTrackingTrackOnOff(0, 4)

        # Fechar conexão
        robot.CloseRPC()
        time.sleep(1)

    TestOriginPointWeave(robot)