Controle de Força do Robô
====================================

.. toctree::
    :maxdepth: 5

Configuração do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_SetConfig(company, device, softversion=0, bus=0)``"
    "Descrição", "Configuração do sensor de força"
    "Parâmetros obrigatórios", "- ``company``: Fabricante do sensor, 17-Kunwei Technology, 19-Instituto de Pesquisa 11 da Aeroespacial, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin, 23-NBIT, 24-Xin Jingcheng (XJC), 26-NSR;
    - ``device``: Número do dispositivo, Kunwei (0-KWR75B), Instituto de Pesquisa 11 (0-MCS6A-200-4), ATI (0-AXIA80-M8), Zhongke Midian (0-MST2010), Weihang Minxin (0-WHC6L-YB-10A), NBIT (0-XLH93003ACS), Xin Jingcheng XJC (0-XJC-6F-D82), NSR (0-NSR-FTSensorA);"
    "Parâmetros padrão", "- ``softversion``: Número da versão do software, não utilizado no momento, padrão 0;
    - ``bus``: Posição do barramento onde o dispositivo está conectado, não utilizado no momento, padrão 0;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Configuração do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_GetConfig()``"
    "Descrição", "Obtém a configuração do sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``[number, company, device, softversion, bus]``: number Número do sensor; company Fabricante do sensor de força, 17-Kunwei Technology, 19-Instituto de Pesquisa 11 da Aeroespacial, 20-Sensor ATI, 21-Zhongke Midian, 22-Weihang Minxin; device Número do dispositivo, Kunwei (0-KWR75B), Instituto de Pesquisa 11 (0-MCS6A-200-4), ATI (0-AXIA80-M8), Zhongke Midian (0-MST2010), Weihang Minxin (0-WHC6L-YB10A); softversion Número da versão do software, não utilizado no momento, padrão 0"

Ativar Sensor de Força
+++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_Activate(state)``"
    "Descrição", "Ativa o sensor de força"
    "Parâmetros obrigatórios", "- ``state``: 0-reset, 1-ativar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calibrar Zero do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_SetZero(state)``"
    "Descrição", "Calibra o zero do sensor de força"
    "Parâmetros obrigatórios", "- ``state``: 0-remover zero, 1-corrigir zero"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Sistema de Coordenadas de Referência do Sensor de Força
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_SetRCS(ref, coord=[0,0,0,0,0,0])``"
    "Descrição", "Define o sistema de coordenadas de referência do sensor de força"
    "Parâmetros obrigatórios", "- ``ref``: 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base"
    "Parâmetros padrão", "- ``coord``: [x,y,z,rx,ry,rz] Valores do sistema de coordenadas personalizado, padrão [0,0,0,0,0,0]"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Peso da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetForceSensorPayload(weight)``"
    "Descrição", "Define o peso da carga sob o sensor de força"
    "Parâmetros obrigatórios", "- ``weight``: Peso da carga em kg"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Centro de Massa da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetForceSensorPayloadCog(x, y, z)``"
    "Descrição", "Define o centro de massa da carga sob o sensor de força"
    "Parâmetros obrigatórios", "
    - ``x``: Centro de massa da carga x mm
    - ``y``: Centro de massa da carga y mm
    - ``z``: Centro de massa da carga z mm
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Peso da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetForceSensorPayload()``"
    "Descrição", "Obtém o peso da carga sob o sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weight``: Peso da carga em kg"

Obter Centro de Massa da Carga sob o Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetForceSensorPayloadCog()``"
    "Descrição", "Obtém o centro de massa da carga sob o sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``x``: Centro de massa da carga x mm
    - ``y``: Centro de massa da carga y mm
    - ``z``: Centro de massa da carga z mm"

Calibração Automática do Zero do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ForceSensorAutoComputeLoad()``"
    "Descrição", "Calibração automática do zero do sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weight``: Massa do sensor em kg
    - ``pos=[x,y,z]``: Centro de massa do sensor em mm"

Obter Dados de Força/Torque no Sistema de Coordenadas de Referência
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_GetForceTorqueRCS()``"
    "Descrição", "Obtém dados de força/torque no sistema de coordenadas de referência"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``data=[fx,fy,fz,tx,ty,tz]``: Dados de força/torque no sistema de coordenadas de referência"

Obter Dados Brutos de Força/Torque do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_GetForceTorqueOrigin()``"
    "Descrição", "Obtém dados brutos de força/torque do sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``data=[fx,fy,fz,tx,ty,tz]``: Dados brutos de força/torque do sensor de força"

Exemplo de Código de Configuração e Calibração Automática do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error, ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    ftCoord = [0, 0, 0, 0, 0, 0]
    robot.FT_SetRCS(0, ftCoord)
    robot.SetForceSensorPayload(0.824)
    robot.SetForceSensorPayloadCog(0.778, 2.554, 48.765)
    error, weight = robot.GetForceSensorPayload()
    error, x, y, z = robot.GetForceSensorPayloadCog()
    print(f"the FT load is {weight}, {x} {y} {z}")
    robot.SetForceSensorPayload(0)
    robot.SetForceSensorPayloadCog(0, 0, 0)
    error, computeWeight, tran = robot.ForceSensorAutoComputeLoad()
    print(f"the result is weight {computeWeight} pos is {tran[0]} {tran[1]} {tran[2]}")
    robot.CloseRPC()

Registro de Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_PdIdenRecord(tool_id)``"
    "Descrição", "Registro de identificação do peso da carga"
    "Parâmetros obrigatórios", "- ``tool_id``: Número do sistema de coordenadas do sensor, intervalo [0~14]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Cálculo da Identificação do Peso da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_PdIdenCompute()``"
    "Descrição", "Cálculo da identificação do peso da carga"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weight``: Peso da carga, em kg"

Registro de Identificação do Centro de Massa da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_PdCogIdenRecord(tool_id, index)``"
    "Descrição", "Registro de identificação do centro de massa da carga"
    "Parâmetros obrigatórios", "- ``tool_id``: Número do sistema de coordenadas do sensor, intervalo [0~14];
    - ``index``: Número do ponto [1~3]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Cálculo da Identificação do Centro de Massa da Carga
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_PdCogIdenCompute()``"
    "Descrição", "Cálculo da identificação do centro de massa da carga"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``cog=[cogx, cogy, cogz]``: Centro de massa da carga, em mm"

Exemplo de Código de Identificação da Carga do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error, ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    tcoord = [0, 0, 35.0, 0, 0, 0]
    robot.SetToolCoord(10, tcoord, 1, 0, 0, 0)
    robot.FT_PdIdenRecord(10)
    time.sleep(1)
    error, weight = robot.FT_PdIdenCompute()
    print(f"payload weight:{weight}")
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 1)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 2)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 3)
    time.sleep(1)
    error, cog = robot.FT_PdCogIdenCompute()
    print(f"FT_PdCogIdenCompute return {error}")
    print(f"cog:{cog[0]},{cog[1]},{cog[2]}")
    robot.CloseRPC()

Proteção contra Colisão
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_Guard(flag, sensor_num, select, force_torque, max_threshold, min_threshold)``"
    "Descrição", "Proteção contra colisão"
    "Parâmetros obrigatórios", "- ``flag``: 0-desativar proteção contra colisão, 1-ativar proteção contra colisão;
    - ``sensor_num``: Número do sensor de força;
    - ``select``: Seis graus de liberdade detectam colisão [fx,fy,fz,mx,my,mz], 0-não ativo, 1-ativo;
    - ``force_torque``: Força/torque de detecção de colisão, em N ou Nm;
    - ``max_threshold``: Limiar máximo;
    - ``min_threshold``: Limiar mínimo;
    - Faixa de detecção de força/torque: (force_torque - min_threshold, force_torque + max_threshold)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Proteção contra Colisão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    sensor_id = 1
    select = [1, 1, 1, 1, 1, 1]
    max_threshold = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    min_threshold = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    ft = None
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    error = robot.FT_Guard(1, sensor_id, select, [0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    robot.FT_Guard(0, sensor_id, select, [0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.CloseRPC()

Controle de Força Constante
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M=None, B=None, threshold=[0.2,0.2], adjustCoeff=[1.0,1.0], polishRadio=0, filter_Sign=0, posAdapt_sign=0, isNoBlock=0)``"
    "Descrição", "Controle de força constante"
    "Parâmetros obrigatórios", "- ``flag``: Flag de ativação do controle de força constante, 0-desativar, 1-ativar;
    - ``sensor_id``: Número do sensor de força;
    - ``select``: Seis graus de liberdade são detectados [fx,fy,fz,mx,my,mz], 0-não ativo, 1-ativo;
    - ``ft``: Força/torque detectado, em N ou Nm;
    - ``ft_pid``: [f_p,f_i,f_d,m_p,m_i,m_d], parâmetros PID de força, parâmetros PID de torque;
    - ``adj_sign``: Estado de ativação da adaptação, 0-desativar, 1-ativar;
    - ``ILC_sign``: Estado de ativação do controle ILC, 0-parar, 1-treinar, 2-praticar;
    - ``max_dis``: Distância máxima de ajuste;
    - ``max_ang``: Ângulo máximo de ajuste;"
    "Parâmetros padrão", "- ``M``: Parâmetro de massa;
    - ``B``: Parâmetro de amortecimento;
    - ``threshold``: Limiares de ativação rx, ry [0-10], padrão 0.2;
    - ``adjustCoeff``: Coeficientes de ajuste de torque rx, ry [0-1], padrão 1;
    - ``polishRadio``: Raio do disco de polimento, em mm;
    - ``filter_Sign``: Flag de ativação do filtro 0-desativar; 1-ativar, padrão 0-desativar;
    - ``posAdapt_sign``: Flag de ativação da adaptação de postura 0-desativar; 1-ativar, padrão 0-desativar;
    - ``isNoBlock``: Flag de bloqueio, 0-bloqueante; 1-não bloqueante, padrão 0-bloqueante;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle de Força Constante com Amortecimento
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    sensor_id = 10
    select = [0, 0, 1, 0, 0, 0]
    ft_pid = [0.0008, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 1000.0
    max_ang = 20.0
    ft = [0.0] * 6
    epos = [0.0] * 4
    j1 = [80.765, -98.795, 106.548, -97.734, -89.999, 94.842]
    j2 = [43.067, -84.429, 92.620, -98.175, -90.011, 57.144]
    desc_p1 = [5.009, -547.463, 262.053, -179.999, -0.019, 75.923]
    desc_p2 = [-347.966, -547.463, 262.048, -180.000, -0.019, 75.923]
    offset_pos = [0.0] * 6
    M = [2.0, 2.0]
    B = [15.0, 15.0]
    threshold = [1.0, 1.0]
    adjustCoeff = [1.0, 0.8]
    polishRadio = 0.0
    filter_Sign = 0
    posAdapt_sign = 1
    isNoBlock = 0
    ft[2] = -10.0
    while True:
        rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0)
        print(f"FT_Control start rtn is {rtn}")
        rtn = robot.MoveL(desc_pos=desc_p1, tool=1, user=0, vel=100, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=epos, search=0, offset_flag=0, offset_pos=offset_pos)
        rtn = robot.MoveL(desc_pos=desc_p2, tool=1, user=0, vel=100, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=epos, search=0, offset_flag=0, offset_pos=offset_pos)
        rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0)
        print(f"FT_Control end rtn is {rtn}")
    robot.CloseRPC()
    return 0

Busca em Espiral
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_SpiralSearch(rcs, ft, dr=0.7, max_t_ms=60000, max_vel=5)``"
    "Descrição", "Busca em espiral"
    "Parâmetros obrigatórios", "- ``rcs``: Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base
    - ``ft``: Limiar de força ou torque (0~100), em N ou Nm;"
    "Parâmetros padrão", "- ``dr``: Avanço do raio por volta, em mm, padrão 0.7;
    - ``max_t_ms``: Tempo máximo de busca, em ms, padrão 60000;
    - ``max_vel``: Velocidade linear máxima, em mm/s, padrão 5"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Inserção Rotativa
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_RotInsertion(rcs, ft, orn, angVelRot=3, angleMax=45, angAccmax=0, rotorn=1, strategy=0)``"
    "Descrição", "Inserção rotativa"
    "Parâmetros obrigatórios", "- ``rcs``: Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base;
    - ``ft``: Limiar de força ou torque (0~100), em N ou Nm;
    - ``orn``: Direção da força/torque, 1-ao longo do eixo Z, 2-em torno do eixo Z;"
    "Parâmetros padrão", "- ``angVelRot``: Velocidade angular de rotação, em °/s, padrão 3;
    - ``angleMax``: Ângulo máximo de rotação, em °, padrão 45;
    - ``angAccmax``: Aceleração angular máxima, em °/s², não utilizado no momento, padrão 0;
    - ``rotorn``: Direção de rotação, 1-horário, 2-anti-horário, padrão 1;
    - ``strategy``: Estratégia de tratamento quando força/torque não são detectados, 0-reportar erro; 1-avisar, continuar movimento"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Instruções de Busca em Espiral, Inserção Linear, etc.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904,-99.669,117.473,-108.616,-91.726,74.256]
    j2 = [-45.615,-106.172,124.296,-107.151,-91.282,74.255]
    j3 = [-29.777,-84.536,109.275,-114.075,-86.655,74.257]
    j4 = [-31.154,-95.317,94.276,-88.079,-89.740,74.256]
    desc_pos1 = [-419.524,-13.000,351.569,-178.118,0.314,3.833]
    desc_pos2 = [-321.222,185.189,335.520,-179.030,-1.284,-29.869]
    desc_pos3 = [-487.434,154.362,308.576,176.600,0.268,-14.061]
    desc_pos4 = [-443.165,147.881,480.951,179.511,-0.775,-15.409]
    offset_pos = [0.0]*6
    epos = [0.0]*4
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

Inserção Linear
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_LinInsertion(rcs, ft, disMax, linorn, lin_v=1.0, lin_a=1.0)``"
    "Descrição", "Inserção linear"
    "Parâmetros obrigatórios", "- ``rcs``: Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base;
    - ``ft``: Limiar de força ou torque (0~100), em N ou Nm;
    - ``disMax``: Distância máxima de inserção, em mm;
    - ``linorn``: Direção de inserção: 0-direção negativa, 1-direção positiva"
    "Parâmetros padrão", "- ``lin_v``: Velocidade linear, em mm/s, padrão 1;
    - ``lin_a``: Aceleração linear, em mm/s², não utilizado no momento, padrão 1"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Instruções de Busca em Espiral, Inserção Linear, etc.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    status = 1
    sensor_num = 1
    gain = [0.0001, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 5.0
    ft = [0.0,0.0,-10.0,0.0,0.0,0.0]
    rcs = 0
    dr = 0.7
    fFinish = 1.0
    t = 60000.0
    vmax = 3.0
    force_goal = 20.0
    lin_v = 0.0
    lin_a = 0.0
    disMax = 100.0
    linorn = 1
    angVelRot = 2.0
    forceInsertion = 1.0
    angleMax = 45
    orn = 1
    angAccmax = 0.0
    rotorn = 1
    select1 = [0, 0, 1, 1, 1, 0]
    robot.FT_Control(status, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_SpiralSearch(rcs, dr, fFinish, t, vmax)
    print(f"FT_SpiralSearch rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select2 = [1, 1, 1, 0, 0, 0]
    gain[0] = 0.00005
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select3 = [0, 0, 1, 1, 1, 0]
    ft[2] = -10.0
    gain[0] = 0.0001
    robot.FT_Control(1, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn)
    print(f"FT_RotInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select4 = [1, 1, 1, 0, 0, 0]
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

Localização de Superfície
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_FindSurface(rcs, dir, axis, disMax, ft, lin_v=3.0, lin_a=0.0)``"
    "Descrição", "Localização de superfície"
    "Parâmetros obrigatórios", "- ``rcs``: Sistema de coordenadas de referência, 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas base;
    - ``dir``: Direção do movimento, 1-direção positiva, 2-direção negativa;
    - ``axis``: Eixo de movimento, 1-x, 2-y, 3-z;
    - ``disMax``: Distância máxima de busca, em mm;
    - ``ft``: Limiar de força para terminar o movimento, em N;"
    "Parâmetros padrão", "- ``lin_v``: Velocidade linear de busca, em mm/s, padrão 3;
    - ``lin_a``: Aceleração linear de busca, em mm/s², padrão 0;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Iniciar Cálculo da Posição do Plano Médio
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_CalCenterStart()``"
    "Descrição", "Iniciar cálculo da posição do plano médio"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Finalizar Cálculo da Posição do Plano Médio
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_CalCenterEnd()``"
    "Descrição", "Finalizar cálculo da posição do plano médio"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro
    - ``pos=[x,y,z,rx,ry,rz]``: Posição do plano médio"

Exemplo de Código de Localização de Superfície
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    rcs = 0
    dir = 1
    axis = 1
    lin_v = 3.0
    lin_a = 0.0
    maxdis = 50.0
    ft_goal = 2.0
    desc_pos = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    xcenter = [0, 0, 0, 0, 0, 0]
    ycenter = [0, 0, 0, 0, 0, 0]
    ft = [-2.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.FT_CalCenterStart()
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error, xcenter = robot.FT_CalCenterEnd()
    print(f"xcenter:{xcenter[0]},{xcenter[1]},{xcenter[2]},{xcenter[3]},{xcenter[4]},{xcenter[5]}")
    robot.MoveCart(xcenter, 9, 0, 60.0)
    robot.FT_CalCenterStart()
    dir = 1
    axis = 2
    lin_v = 6.0
    maxdis = 150.0
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error, ycenter = robot.FT_CalCenterEnd()
    print(f"ycenter:{ycenter[0]},{ycenter[1]},{ycenter[2]},{ycenter[3]},{ycenter[4]},{ycenter[5]}")
    robot.MoveCart(ycenter, 9, 0, 60.0)
    robot.CloseRPC()

Ativar Controle de Compliance
++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_ComplianceStart(p, force)``"
    "Descrição", "Ativar controle de compliance"
    "Parâmetros obrigatórios", "- ``p``: Coeficiente de ajuste de posição ou coeficiente de compliance
    - ``force``: Limiar de força para ativação do compliance, em N"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desativar Controle de Compliance
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FT_ComplianceStop()``"
    "Descrição", "Desativar controle de compliance"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle de Compliance
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    flag = 1
    sensor_id = 1
    select = [1, 1, 1, 0, 0, 0]
    ft_pid = [0.0005, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 0.0
    ft = [-10.0, -10.0, -10.0, 0.0, 0.0, 0.0]
    offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0]  # Alternativa para DescPose(0, 0, 0, 0, 0, 0)
    epos = [0.0,0.0,0.0,0.0]  # Alternativa para ExaxisPos(0, 0, 0, 0)
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]  # JointPos
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]  # DescPose
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    p = 0.00005
    force = 30.0
    rtn = robot.FT_ComplianceStart(p, force)
    print(f"FT_ComplianceStart rtn is {rtn}")
    count = 3
    while count > 0:
        robot.MoveL(desc_pos=desc_p1, tool=0, user=0, vel=100.0)
        robot.MoveL(desc_pos=desc_p2, tool=0, user=0, vel=100.0)
        count -= 1
    robot.FT_ComplianceStop()
    print(f"FT_ComplianceStop rtn is {rtn}")
    flag = 0
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

Inicialização do Filtro de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadIdentifyDynFilterInit()``"
    "Descrição", "Inicialização do filtro de identificação da carga"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Inicialização das Variáveis de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadIdentifyDynVarInit()``"
    "Descrição", "Inicialização das variáveis de identificação da carga"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Programa Principal de Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadIdentifyMain(joint_torque, joint_pos, t)``"
    "Descrição", "Programa principal de identificação da carga"
    "Parâmetros obrigatórios", "- ``joint_torque``: Torque das juntas j1-j6;
    - ``joint_pos``: Posição das juntas j1-j6
    - ``t``: Período de amostragem"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Resultado da Identificação da Carga
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadIdentifyGetResult(gain)``"
    "Descrição", "Obtém o resultado da identificação da carga"
    "Parâmetros obrigatórios", "- ``gain``: Coeficiente do termo gravitacional double[6], coeficiente do termo centrífugo double[6]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weight``: Peso da carga
    - ``cog=[x,y,z]``: Coordenadas do centro de massa da carga"

Exemplo de Código de Identificação da Carga do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    retval = robot.LoadIdentifyDynFilterInit()
    print(f"LoadIdentifyDynFilterInit retval is: {retval}")
    retval = robot.LoadIdentifyDynVarInit()
    print(f"LoadIdentifyDynVarInit retval is: {retval}")
    error, posJ = robot.GetActualJointPosDegree(0)
    posJ[1] += 10  # Modificar junta 2
    error, joint_toq = robot.GetJointTorques(0)
    joint_toq[1] += 2  # Modificar torque na junta 2
    tmpTorque = joint_toq.copy()
    retval = robot.LoadIdentifyMain(tmpTorque, posJ, 1)
    print(f"LoadIdentifyMain retval is: {retval}")
    gain = [0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0]
    weight = [0.0]
    load_pos = [0.0, 0.0, 0.0]
    retval, weight, load_pos = robot.LoadIdentifyGetResult(gain)
    print(f"LoadIdentifyGetResult retval is: {retval} ; weight is {weight}  cog is {load_pos[0]} {load_pos[1]} {load_pos[2]}")
    robot.CloseRPC()

Arrasto Assistido por Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``EndForceDragControl(status, asaptiveFlag, interfereDragFlag, ingularityConstraintsFlag, M, B, K, F, Fmax, Vmax, forceCollisionFlag=0)``"
    "Descrição", "Arrasto assistido por sensor de força"
    "Parâmetros obrigatórios", "- ``status``: Estado de controle, 0-desativar; 1-ativar
    - ``asaptiveFlag``: Flag de ativação de adaptação, 0-desativar; 1-ativar
    - ``interfereDragFlag``: Flag de arrasto em zona de interferência, 0-desativar; 1-ativar
    - ``ingularityConstraintsFlag``: Estratégia de ponto singular, 0-evitar; 1-atravessar
    - ``forceCollisionFlag``: Flag de detecção de colisão do robô durante arrasto assistido; 0-desativar; 1-ativar
    - ``M=[m1,m2,m3,m4,m5,m6]``: Coeficiente de inércia
    - ``B=[b1,b2,b3,b4,b5,b6]``: Coeficiente de amortecimento
    - ``K=[k1,k2,k3,k4,k5,k6]``: Coeficiente de rigidez
    - ``F=[f1,f2,f3,f4,f5,f6]``: Limiar de força de arrasto 6D
    - ``Fmax``: Limite máximo de força de arrasto
    - ``Vmax``: Limite máximo de velocidade das juntas"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado do Interruptor de Arrasto do Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetForceAndTorqueDragState()``"
    "Descrição", "Obtém o estado do interruptor de arrasto do sensor de força"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``dragState``: Estado de controle de arrasto assistido por sensor de força, 0-desativar; 1-ativar
    - ``sixDimensionalDragState``: Estado de controle de arrasto assistido por força 6D, 0-desativar; 1-ativar"

Ativação Automática do Sensor de Força Após Limpeza de Erro
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetForceSensorDragAutoFlag(status)``"
    "Descrição", "Ativação automática do sensor de força após limpeza de erro"
    "Parâmetros obrigatórios", "- ``status``: Estado de controle, 0-desativar; 1-ativar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Arrasto Assistido por Sensor de Força
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.SetForceSensorDragAutoFlag(1)
    M = [15.0, 15.0, 15.0, 0.5, 0.5, 0.1]
    B = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    K = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    F = [10.0, 10.0, 10.0, 1.0, 1.0, 1.0]
    robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100)
    time.sleep(5)
    drag_state = 0
    six_dimensional_drag_state = 0
    error, drag_state, six_dimensional_drag_state = robot.GetForceAndTorqueDragState()
    print(f"the drag state is {drag_state} {six_dimensional_drag_state}")
    robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100)
    robot.CloseRPC()

Definir Interruptor e Parâmetros do Arrasto Híbrido de Força 6D e Impedância Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ForceAndJointImpedanceStartStop(status, impedanceFlag, lamdeDain, KGain, BGain, dragMaxTcpVel, dragMaxTcpOriVel)``"
    "Descrição", "Define o interruptor e parâmetros do arrasto híbrido de força 6D e impedância articular"
    "Parâmetros obrigatórios", "- ``status``: Estado de controle, 0-desativar; 1-ativar
    - ``impedanceFlag``: Flag de ativação de impedância, 0-desativar; 1-ativar
    - ``lamdeDain``: [D1,D2,D3,D4,D5,D6] Ganho de arrasto
    - ``KGain``: [K1,K2,K3,K4,K5,K6] Ganho de rigidez
    - ``BGain``: [B1,B2,B3,B4,B5,B6] Ganho de amortecimento
    - ``dragMaxTcpVel``: Velocidade linear máxima do TCP durante arrasto
    - ``dragMaxTcpOriVel``: Velocidade angular máxima do TCP durante arrasto"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Arrasto Híbrido de Força 6D e Impedância Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    lamde_dain = [3.0, 2.0, 2.0, 2.0, 2.0, 3.0]
    k_gain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    b_gain = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    time.sleep(5)
    robot.DragTeachSwitch(0)
    rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    robot.CloseRPC()

Controle de Ativação/Desativação de Impedância
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ImpedanceControlStartStop(status, workSpace, forceThreshold, m, b, k, maxV, maxVA, maxW, maxWA)``"
    "Descrição", "Controle de ativação/desativação de impedância"
    "Parâmetros obrigatórios", "- ``status``: 0-desativar; 1-ativar
    - ``workSpace``: 0-espaço articular; 1-espaço cartesiano
    - ``forceThreshold``: Limiar de força de ativação (N)
    - ``m``: Parâmetro de massa
    - ``b``: Parâmetro de amortecimento
    - ``k``: Parâmetro de rigidez
    - ``maxV``: Velocidade linear máxima (mm/s)
    - ``maxVA``: Aceleração linear máxima (mm/s²)
    - ``maxW``: Velocidade angular máxima (°/s)
    - ``maxWA``: Aceleração angular máxima (°/s²)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle de Ativação/Desativação de Impedância
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    j1 = [102.622, -135.990, 120.769, -73.950, -90.848, 35.507]
    j2 = [93.674, -80.062, 82.947, -92.199, -90.967, 26.559]
    desc_pos1 = [136.552, -149.799, 449.532, 179.817, -1.172, 157.123]
    desc_pos2 = [136.540, -561.048, 449.542, 179.819, -1.172, 157.122]
    offset_pos = [0.0] * 6
    epos = [0.0] * 4
    tool = 0
    user = 0
    vel = 100.0
    acc = 200.0
    ovl = 100.0
    blendT = -1.0
    blendR = -1.0
    flag = 0
    search = 0
    robot.SetSpeed(20)
    company = 17
    device = 0
    softversion = 0
    bus = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    rnt, [company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    robot.FT_SetZero(1)
    time.sleep(1)
    forceThreshold = [30.0, 30.0, 30.0, 5.0, 5.0, 5.0]
    m = [0.1, 0.1, 0.1, 0.02, 0.02, 0.02]
    b = [1.0, 1.0, 1.0, 0.08, 0.08, 0.08]
    k = [0.0] * 6
    rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100)
    print(f"ImpedanceControlStartStop errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, speedPercent=1)
    print(f"movel errcode:{rtn}")
    robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100)
    robot.CloseRPC()

Ativar Função de Compensação de Torque e Coeficientes de Compensação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetCoderCompenParams(status, torqueCoeff)``"
    "Descrição", "Ativa a função de compensação de torque e coeficientes de compensação"
    "Parâmetros obrigatórios", "- ``status``: Interruptor, 0-desativar; 1-ativar
    - ``torqueCoeff``: Coeficientes de compensação de torque J1-J6 [0-1]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"