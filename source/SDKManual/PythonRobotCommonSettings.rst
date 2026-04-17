Configurações Comuns do Robô
==================================

.. toctree::
    :maxdepth: 5

Definir Ponto de Referência da Ferramenta - Método dos Seis Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolPoint(point_num)``"
    "Descrição", "Define o ponto de referência da ferramenta - método dos seis pontos"
    "Parâmetros obrigatórios", "- ``point_num``: Número do ponto, intervalo [1~6]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Sistema de Coordenadas da Ferramenta - Método dos Seis Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeTool()``"
    "Descrição", "Calcula o sistema de coordenadas da ferramenta - método dos seis pontos (após definir os seis pontos de referência da ferramenta)"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``tcp_pose=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da ferramenta"

Definir Ponto de Referência da Ferramenta - Método dos Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetTcp4RefPoint(point_num)``"
    "Descrição", "Define o ponto de referência da ferramenta - método dos quatro pontos"
    "Parâmetros obrigatórios", "- ``point_num``: Número do ponto, intervalo [1~4]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Sistema de Coordenadas da Ferramenta - Método dos Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeTcp4()``"
    "Descrição", "Calcula o sistema de coordenadas da ferramenta - método dos quatro pontos (após definir os quatro pontos de referência da ferramenta)"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``tcp_pose=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da ferramenta"

Calcular Sistema de Coordenadas da Ferramenta com Base em Informações de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeToolCoordWithPoints(method, pos)``"
    "Descrição", "Calcula o sistema de coordenadas da ferramenta com base em informações de pontos"
    "Parâmetros obrigatórios", "- ``method``: Método de cálculo; 0-método dos quatro pontos; 1-método dos seis pontos
    - ``pos``: Grupo de posições das juntas, comprimento do array é 4 para o método dos quatro pontos e 6 para o método dos seis pontos"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da ferramenta calculado com base nas informações dos pontos, unidades [mm][°]"

Definir Sistema de Coordenadas da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolCoord(id, t_coord, type, install, toolID, loadNum)``"
    "Descrição", "Define o sistema de coordenadas da ferramenta"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [1~15];
    - ``t_coord``: Pose do ponto central da ferramenta em relação ao centro do flange da extremidade, unidades [mm][°];
    - ``type``: 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor;
    - ``install``: Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    - ``toolID``: ID da ferramenta
    - ``loadNum``: Número da carga"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Lista de Sistemas de Coordenadas da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolList(id, t_coord, type, install, loadNum)``"
    "Descrição", "Define a lista de sistemas de coordenadas da ferramenta"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [1~15];
    - ``t_coord``: [x,y,z,rx,ry,rz] Pose do ponto central da ferramenta em relação ao centro do flange da extremidade, unidades [mm][°];
    - ``type``: 0-sistema de coordenadas da ferramenta, 1-sistema de coordenadas do sensor;
    - ``install``: Posição de instalação, 0-extremidade do robô, 1-externo ao robô
    - ``loadNum``: Número da carga"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Sistema de Coordenadas da Ferramenta Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTCPOffset(flag=1)``"
    "Descrição", "Obtém o sistema de coordenadas da ferramenta atual"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: Pose relativa do sistema de coordenadas da ferramenta atual, unidades [mm][°]"

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posJ = [p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint]
    rtn, coordRtn = robot.ComputeToolCoordWithPoints(1, posJ)
    print(f"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(1)
    robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(2)
    robot.MoveJ(joint_pos=p3Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(3)
    robot.MoveJ(joint_pos=p4Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(4)
    robot.MoveJ(joint_pos=p5Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(5)
    robot.MoveJ(joint_pos=p6Joint, tool=0, user=0, vel=100)
    robot.SetToolPoint(6)
    rtn, coordRtn = robot.ComputeTool()
    print(f"6 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolList(1, coordRtn, 0, 0, 0)
    robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint, tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint, tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(4)
    rtn, coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0)
    rtn, getCoord = robot.GetTCPOffset(0)
    print(f"GetTCPOffset    {rtn}  coord is {getCoord[0]} {getCoord[1]} {getCoord[2]} {getCoord[3]} {getCoord[4]} {getCoord[5]}")
    robot.CloseRPC()

Definir Ponto de Referência da Ferramenta Externa - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExTCPPoint(point_num)``"
    "Descrição", "Define o ponto de referência da ferramenta externa - método dos três pontos"
    "Parâmetros obrigatórios", "- ``point_num``: Número do ponto, intervalo [1~3]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Sistema de Coordenadas da Ferramenta Externa - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeExTCF(point_num)``"
    "Descrição", "Calcula o sistema de coordenadas da ferramenta externa - método dos três pontos (após definir os três pontos de referência)"
    "Parâmetros obrigatórios", "- ``point_num``: Número do ponto, intervalo [1~3]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``etcp=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da ferramenta externa"

Definir Sistema de Coordenadas da Ferramenta Externa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExToolCoord(id, etcp, etool)``"
    "Descrição", "Define o sistema de coordenadas da ferramenta externa"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [0~14];
    - ``etcp``: Sistema de coordenadas da ferramenta externa, unidades [mm][°];
    - ``etool``: Sistema de coordenadas da ferramenta da extremidade, unidades [mm][°];"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Lista de Sistemas de Coordenadas da Ferramenta Externa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExToolList(id, etcp, etool)``"
    "Descrição", "Define a lista de sistemas de coordenadas da ferramenta externa"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [0~14];
    - ``etcp``: Sistema de coordenadas da ferramenta externa, unidades [mm][°];
    - ``etool``: Sistema de coordenadas da ferramenta da extremidade, unidades [mm][°];"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Operações do Sistema de Coordenadas da Ferramenta Externa do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    robot.MoveJ(joint_pos=p1Joint, tool=1, user=0, vel=50)
    robot.SetExTCPPoint(1)
    robot.MoveJ(joint_pos=p2Joint, tool=1, user=0, vel=50)
    robot.SetExTCPPoint(2)
    robot.MoveJ(joint_pos=p3Joint, tool=1, user=0, vel=50)
    robot.SetExTCPPoint(3)
    rtn, coordRtn = robot.ComputeExTCF()
    print(f"ComputeExTCF {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetExToolCoord(1, coordRtn, offdese)
    robot.SetExToolList(1, coordRtn, offdese)
    robot.CloseRPC()

Definir Ponto de Referência da Peça - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWObjCoordPoint(point_num)``"
    "Descrição", "Define o ponto de referência da peça - método dos três pontos"
    "Parâmetros obrigatórios", "- ``point_num``: Número do ponto, intervalo [1~3]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Sistema de Coordenadas da Peça - Método dos Três Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeWObjCoord(method, refFrame)``"
    "Descrição", "Calcula o sistema de coordenadas da peça - método dos três pontos (após definir os três pontos de referência)"
    "Parâmetros obrigatórios", "- ``method``: Método de cálculo 0: origem-eixo x-eixo z, 1: origem-eixo x-plano xy
    - ``refFrame``: Sistema de coordenadas de referência"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``wobj_pose=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da peça"

Definir Sistema de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWObjCoord(id, coord, refFrame)``"
    "Descrição", "Define o sistema de coordenadas da peça"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [0~14];
    - ``coord``: Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade, unidades [mm][°]
    - ``refFrame``: Sistema de coordenadas de referência"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Lista de Sistemas de Coordenadas da Peça
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWObjList(id, coord, refFrame)``"
    "Descrição", "Define a lista de sistemas de coordenadas da peça"
    "Parâmetros obrigatórios", "- ``id``: Número do sistema de coordenadas, intervalo [0~14];
    - ``coord``: Pose do sistema de coordenadas da peça em relação ao centro do flange da extremidade, unidades [mm][°]
    - ``refFrame``: Sistema de coordenadas de referência"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Sistema de Coordenadas da Peça com Base em Informações de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeWObjCoordWithPoints(method, pos, refFrame)``"
    "Descrição", "Calcula o sistema de coordenadas da peça com base em informações de pontos"
    "Parâmetros obrigatórios", "- ``method``: Método de cálculo; 0: origem-eixo x-eixo z  1: origem-eixo x-plano xy
    - ``pos``: Grupo de três posições TCP
    - ``refFrame``: Sistema de coordenadas de referência"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: Sistema de coordenadas da peça calculado com base nas informações dos pontos, unidades [mm][°]"

Obter Sistema de Coordenadas da Peça Atual
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetWObjOffset(flag=1)``"
    "Descrição", "Obtém o sistema de coordenadas da peça atual"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: Pose relativa do sistema de coordenadas da peça atual, unidades [mm][°]"

Exemplo de Código para Operações do Sistema de Coordenadas da Peça do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    rtn, coordRtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0)
    print(f"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint, tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(1)
    robot.MoveJ(joint_pos=p2Joint, tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(2)
    robot.MoveJ(joint_pos=p3Joint, tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(3)
    rtn, coordRtn = robot.ComputeWObjCoord(1, 0)
    print(f"ComputeWObjCoord   {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetWObjCoord(1, coordRtn, 0)
    robot.SetWObjList(1, coordRtn, 0)
    rtn, getWobjDesc = robot.GetWObjOffset(0)
    print(f"GetWObjOffset    {rtn}  coord is {getWobjDesc[0]} {getWobjDesc[1]} {getWobjDesc[2]} {getWobjDesc[3]} {getWobjDesc[4]} {getWobjDesc[5]}")
    robot.CloseRPC()

Definir Velocidade Global
++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetSpeed(vel)``"
    "Descrição", "Define a velocidade global"
    "Parâmetros obrigatórios", "- ``vel``: Percentagem de velocidade, intervalo [0~100]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Aceleração do Robô
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOaccScale(acc)``"
    "Descrição", "Define a aceleração do robô"
    "Parâmetros obrigatórios", "- ``acc``: Percentagem de aceleração do robô"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Velocidade Padrão
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDefaultTransVel()``"
    "Descrição", "Obtém a velocidade padrão"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``vel``: Velocidade padrão, unidades [mm/s]"

Definir Peso da Carga na Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetLoadWeight(loadNum, weight)``"
    "Descrição", "Define o peso da carga na extremidade. Uma configuração incorreta do peso da carga pode causar perda de controle do robô no modo de arrasto"
    "Parâmetros obrigatórios", "- ``loadNum``: Número da carga
    - ``weight``: Unidade [kg]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coordenadas do Centro de Massa da Carga na Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetLoadCoord(x, y, z, loadNum=0)``"
    "Descrição", "Define as coordenadas do centro de massa da carga na extremidade. Uma configuração incorreta do centro de massa da carga pode causar perda de controle do robô no modo de arrasto"
    "Parâmetros obrigatórios", "- ``x``: Coordenada do centro de massa, unidade [mm]
    - ``y``: Coordenada do centro de massa, unidade [mm]
    - ``z``: Coordenada do centro de massa, unidade [mm]"
    "Parâmetros padrão", "- ``loadNum``: Número da carga, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Peso da Carga Atual
++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTargetPayload(flag=1)``"
    "Descrição", "Obtém a massa da carga atual"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weight``: Peso da carga atual, unidade [kg]"

Obter Centro de Massa da Carga Atual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetTargetPayloadCog(flag=1)``"
    "Descrição", "Obtém o centro de massa da carga atual"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``flag``: 0-bloqueante, 1-não bloqueante, padrão 1"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``cog=[x,y,z]``: Coordenadas do centro de massa atual, unidade [mm]"

Definir Modo de Instalação do Robô - Instalação Fixa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotInstallPos(method)``"
    "Descrição", "Define o modo de instalação do robô - instalação fixa. Uma configuração incorreta do modo de instalação pode causar perda de controle do robô no modo de arrasto"
    "Parâmetros obrigatórios", "- ``method``: 0-montagem normal, 1-montagem lateral, 2-montagem invertida"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Ângulo de Instalação do Robô - Instalação Livre
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotInstallAngle(yangle, zangle)``"
    "Descrição", "Define o ângulo de instalação do robô - instalação livre. Uma configuração incorreta do ângulo de instalação pode causar perda de controle do robô no modo de arrasto"
    "Parâmetros obrigatórios", "- ``yangle``: Ângulo de inclinação
    - ``zangle``: Ângulo de rotação"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Ângulo de Instalação do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotInstallAngle()``"
    "Descrição", "Obtém o ângulo de instalação do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``[yangle,zangle]``: yangle-ângulo de inclinação, zangle-ângulo de rotação"

Definir Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetSysVarValue(id, value)``"
    "Descrição", "Define a variável do sistema"
    "Parâmetros obrigatórios", "- ``id``: Número da variável, intervalo [1~20];
    - ``value``: Valor da variável"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Valor de Variável do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSysVarValue(id)``"
    "Descrição", "Obtém o valor da variável do sistema"
    "Parâmetros obrigatórios", "- ``id``: Número da variável do sistema, intervalo [1~20]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``var_value``: Valor da variável do sistema"

Exemplo de Código para Configurações Comuns do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    for i in range(1, 100):
        robot.SetSpeed(i)
        robot.SetOaccScale(i)
        time.sleep(0.03)
    error, defaultVel = robot.GetDefaultTransVel()
    print(f"GetDefaultTransVel is {defaultVel}")
    for i in range(1, 21):
        robot.SetSysVarValue(i, i + 0.5)
        time.sleep(0.1)
    for i in range(1, 21):
        value = robot.GetSysVarValue(i)
        print(f"sys value {i} is: {value}")
        time.sleep(0.1)
    robot.SetLoadWeight(0, 2.5)
    robot.SetLoadCoord(3.0, 4.0, 5.0)
    time.sleep(1)
    error, getLoad = robot.GetTargetPayload(0)
    error, getLoadTran = robot.GetTargetPayloadCog(0)
    print(f"get load is {getLoad}; get load cog is {getLoadTran[0]} {getLoadTran[1]} {getLoadTran[2]}")
    robot.SetRobotInstallPos(0)
    robot.SetRobotInstallAngle(15.0, 25.0)
    error, [anglex, angley] = robot.GetRobotInstallAngle()
    print(f"GetRobotInstallAngle x: {anglex}; y: {angley}")
    robot.CloseRPC()

Chave de Compensação de Atrito das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FrictionCompensationOnOff(state)``"
    "Descrição", "Chave de compensação de atrito das juntas"
    "Parâmetros obrigatórios", "- ``state``: 0-desligar, 1-ligar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Normal
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFrictionValue_level(coeff)``"
    "Descrição", "Define o coeficiente de compensação de atrito das juntas - instalação fixa - montagem normal"
    "Parâmetros obrigatórios", "- ``coeff=[j1,j2,j3,j4,j5,j6]``: Coeficientes de compensação das seis juntas"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Lateral
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFrictionValue_wall(coeff)``"
    "Descrição", "Define o coeficiente de compensação de atrito das juntas - instalação fixa - montagem lateral"
    "Parâmetros obrigatórios", "- ``coeff=[j1,j2,j3,j4,j5,j6]``: Coeficientes de compensação das seis juntas"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coeficiente de Compensação de Atrito das Juntas - Montagem Invertida
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFrictionValue_ceiling(coeff)``"
    "Descrição", "Define o coeficiente de compensação de atrito das juntas - instalação fixa - montagem invertida"
    "Parâmetros obrigatórios", "- ``coeff=[j1,j2,j3,j4,j5,j6]``: Coeficientes de compensação das seis juntas"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coeficiente de Compensação de Atrito das Juntas - Instalação Livre
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFrictionValue_freedom(coeff)``"
    "Descrição", "Define o coeficiente de compensação de atrito das juntas - instalação livre"
    "Parâmetros obrigatórios", "- ``coeff=[j1,j2,j3,j4,j5,j6]``: Coeficientes de compensação das seis juntas"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Configuração de Compensação de Atrito das Juntas do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    lcoeff = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    wcoeff = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
    ccoeff = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    fcoeff = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    rtn = robot.FrictionCompensationOnOff(1)
    print(f"FrictionCompensationOnOff rtn is {rtn}")
    rtn = robot.SetFrictionValue_level(lcoeff)
    print(f"SetFrictionValue_level rtn is {rtn}")
    rtn = robot.SetFrictionValue_wall(wcoeff)
    print(f"SetFrictionValue_wall rtn is {rtn}")
    rtn = robot.SetFrictionValue_ceiling(ccoeff)
    print(f"SetFrictionValue_ceiling rtn is {rtn}")
    rtn = robot.SetFrictionValue_freedom(fcoeff)
    print(f"SetFrictionValue_freedom rtn is {rtn}")
    robot.CloseRPC()

Consultar Código de Erro do Robô
++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotErrorCode()``"
    "Descrição", "Consulta o código de erro do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``[maincode subcode]``: Código de erro do robô, maincode-código de erro principal, subcode-código de erro secundário"

Limpar Estado de Erro
++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ResetAllError()``"
    "Descrição", "Limpa o estado de erro, apenas erros reinicializáveis podem ser limpos"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Obter Estado de Falha e Limpar Erro do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    robot.MoveJ(joint_pos=p1Joint, tool=5, user=2, vel=50)
    time.sleep(1)
    error, [maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    time.sleep(1)
    robot.ResetAllError()
    time.sleep(1)
    error, [maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    robot.CloseRPC()

Definir Parâmetros de Monitoramento de Temperatura e Velocidade da Ventoinha da Caixa de Controle de Larga Tensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWideBoxTempFanMonitorParam(enable, period)``"
    "Descrição", "Define os parâmetros de monitoramento de temperatura e velocidade da ventoinha da caixa de controle de larga tensão"
    "Parâmetros obrigatórios", "- ``enable``: 0-desativar monitoramento; 1-ativar monitoramento
    - ``period``: Período de monitoramento (s), intervalo 1-100"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros de Monitoramento de Temperatura e Velocidade da Ventoinha da Caixa de Controle de Larga Tensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetWideBoxTempFanMonitorParam()``"
    "Descrição", "Obtém os parâmetros de monitoramento de temperatura e velocidade da ventoinha da caixa de controle de larga tensão"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``enable``: 0-desativar monitoramento; 1-ativar monitoramento
    - ``period``: Período de monitoramento (s), intervalo 1-100"

Exemplo de Código para Obter Estado de Temperatura e Corrente da Ventoinha da Caixa de Controle de Larga Tensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.SetWideBoxTempFanMonitorParam(1, 2)
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    rtn = robot.SetWideBoxTempFanMonitorParam(0, 2)
    print(f"SetWideBoxTempFanMonitorParam rtn is:{rtn}")
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    robot.CloseRPC()

Definir Ponto de Calibração do Foco
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFocusCalibPoint(pointNum, point)``"
    "Descrição", "Define o ponto de calibração do foco"
    "Parâmetros obrigatórios", "- ``pointNum``: Número do ponto de calibração do foco 1-8
    - ``point``: Coordenadas do ponto de calibração"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Resultado da Calibração do Foco
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeFocusCalib(pointNum)``"
    "Descrição", "Calcula o resultado da calibração do foco"
    "Parâmetros obrigatórios", "- ``pointNum``: Número de pontos de calibração"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``resultPos``: Resultado da calibração XYZ
    - ``accuracy``: Erro de precisão da calibração"

Iniciar Rastreamento do Foco
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FocusStart(kp=50.0, kpredic=19.0, aMax=1440, vMax=180, type=0)``"
    "Descrição", "Inicia o rastreamento do foco"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``kp``: Parâmetro proporcional, padrão 50.0
    - ``kpredic``: Parâmetro feedforward, padrão 19.0
    - ``aMax``: Limite máximo de aceleração angular, padrão 1440°/s²
    - ``vMax``: Limite máximo de velocidade angular, padrão 180°/s
    - ``type``: Travar a direção do eixo X (0-vetor de entrada de referência; 1-horizontal; 2-vertical), padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parar Rastreamento do Foco
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``FocusEnd()``"
    "Descrição", "Para o rastreamento do foco"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Coordenadas do Foco
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetFocusPosition(pos)``"
    "Descrição", "Define as coordenadas do foco"
    "Parâmetros obrigatórios", "- ``pos``: Coordenadas do foco XYZ"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Rastreamento do Foco do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 100, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1, offset_flag=0, offset_pos=offdese)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1, offset_flag=0, offset_pos=offdese)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1, offset_flag=0, offset_pos=offdese)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1, offset_flag=0, offset_pos=offdese)
    robot.SetTcp4RefPoint(4)
    rtn, coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool {rtn} coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} "
          f"{coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0)
    error, p1Desc = robot.GetForwardKin(p1Joint)
    error, p2Desc = robot.GetForwardKin(p2Joint)
    error, p3Desc = robot.GetForwardKin(p3Joint)
    robot.SetFocusCalibPoint(1, p1Desc)
    robot.SetFocusCalibPoint(2, p2Desc)
    robot.SetFocusCalibPoint(3, p3Desc)
    rtn, resultPos, accuracy = robot.ComputeFocusCalib(pointNum=3)
    print(f"ComputeFocusCalib coord is {rtn} {resultPos[0]} {resultPos[1]} {resultPos[2]} accuracy is {accuracy}")
    rtn = robot.SetFocusPosition(resultPos)
    error, p5Desc = robot.GetForwardKin(p5Joint)
    error, p6Desc = robot.GetForwardKin(p6Joint)
    robot.MoveL(desc_pos=p5Desc, tool=1, user=0, vel=10, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=exaxisPos, search=0, offset_flag=1, offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc, tool=1, user=0, vel=10, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=exaxisPos, search=0, offset_flag=1, offset_pos=offdese)
    robot.FocusStart(50, 19, 710, 90, 0)
    robot.MoveL(desc_pos=p5Desc, tool=1, user=0, vel=10, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=exaxisPos, search=0, offset_flag=1, offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc, tool=1, user=0, vel=10, acc=100, ovl=100, blendR=-1, blendMode=0, exaxis_pos=exaxisPos, search=0, offset_flag=1, offset_pos=offdese)
    robot.FocusEnd()
    robot.CloseRPC()

Ativar Função de Calibração de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointSensitivityEnable(status)``"
    "Descrição", "Ativa a função de calibração de sensibilidade do sensor de torque das juntas"
    "Parâmetros obrigatórios", "- ``status``: 0-desativar; 1-ativar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Coleta de Dados de Sensibilidade do Sensor de Torque das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointSensitivityCollect()``"
    "Descrição", "Coleta de dados de sensibilidade do sensor de torque das juntas"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Resultado da Calibração de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointSensitivityCalibration()``"
    "Descrição", "Obtém o resultado da calibração de sensibilidade do sensor de torque das juntas"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``calibResult``: Sensibilidade das juntas j1~j6 [0-1]
    - ``linearityn``: Linearidade das juntas j1~j6 [0-1]"

Obter Erro de Histerese do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointHysteresisError()``"
    "Descrição", "Obtém o erro de histerese do sensor de torque das juntas"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``hysteresisError``: Erro de histerese das juntas j1~j6"

Obter Repetibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointRepeatability()``"
    "Descrição", "Obtém a repetibilidade do sensor de torque das juntas"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``repeatability``: Repetibilidade das juntas j1~j6"

Definir Parâmetros do Sensor de Força das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAdmittanceParams(M, B, K, threshold, sensitivity, setZeroFlag)``"
    "Descrição", "Define os parâmetros do sensor de força das juntas"
    "Parâmetros obrigatórios", "
    - ``M``: Coeficientes de massa J1-J6 [0.001 ~ 10]
    - ``B``: Coeficientes de amortecimento J1-J6 [0.001 ~ 10]
    - ``K``: Coeficientes de rigidez J1-J6 [0.001 ~ 10]
    - ``threshold``: Limiar de controle de força, Nm
    - ``sensitivity``: Sensibilidade, Nm/V, [0 ~ 10]
    - ``setZeroFlag``: Flag de ativação da função; 0-desativar; 1-ativar; 2-registrar ponto zero na posição 1; 3-registrar ponto zero na posição 2"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Calibração Automática de Sensibilidade do Sensor de Torque das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.JointSensitivityEnable(0)
    rtn = robot.JointSensitivityEnable(1)
    print(f"JointSensitivityEnable rtn is {rtn}")
    curJPos = [0.0] * 6
    rtn, curJPos = robot.GetActualJointPosDegree(0)
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    jointPos1 = [curJPos[0], 0.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos1 = [0.0] * 6
    rtn, descPos1 = robot.GetForwardKin(jointPos1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 1 rtn is {rtn}")
    time.sleep(0.1)
    jointPos2 = [curJPos[0], -30.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos2 = [0.0] * 6
    rtn, descPos2 = robot.GetForwardKin(jointPos2)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 2 rtn is {rtn}")
    time.sleep(0.1)
    jointPos3 = [curJPos[0], -60.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos3 = [0.0] * 6
    rtn, descPos3 = robot.GetForwardKin(jointPos3)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 3 rtn is {rtn}")
    time.sleep(0.1)
    jointPos4 = [curJPos[0], -90.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos4 = [0.0] * 6
    rtn, descPos4 = robot.GetForwardKin(jointPos4)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 4 rtn is {rtn}")
    time.sleep(0.1)
    jointPos5 = [curJPos[0], -120.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos5 = [0.0] * 6
    rtn, descPos5 = robot.GetForwardKin(jointPos5)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 5 rtn is {rtn}")
    time.sleep(0.1)
    jointPos6 = [curJPos[0], -150.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos6 = [0.0] * 6
    rtn, descPos6 = robot.GetForwardKin(jointPos6)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 6 rtn is {rtn}")
    time.sleep(0.1)
    jointPos7 = [curJPos[0], -180.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos7 = [0.0] * 6
    rtn, descPos7 = robot.GetForwardKin(jointPos7)
    robot.MoveJ(joint_pos=jointPos7, desc_pos=descPos7, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 7 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 8 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 9 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 10 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 11 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 12 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 13 rtn is {rtn}")
    time.sleep(0.1)
    calibResult = [0.0] * 6
    linearity = [0.0] * 6
    rtn, calibResult, linearity = robot.JointSensitivityCalibration()
    print(f"JointSensitivityCalibration rtn is {rtn}")
    rtn = robot.JointSensitivityEnable(0)
    print(f"JointSensitivityEnable rtn is {rtn}")
    print(f"jointSensor Calib result is {calibResult[0]},{calibResult[1]},{calibResult[2]},{calibResult[3]},{calibResult[4]},{calibResult[5]}")
    print(f"jointSensor linearity is {linearity[0]},{linearity[1]},{linearity[2]},{linearity[3]},{linearity[4]},{linearity[5]}")
    hysteresisError = [0.0] * 6
    rtn, hysteresisError = robot.JointHysteresisError()
    print(f"JointHysteresisError result is {hysteresisError[0]},{hysteresisError[1]},{hysteresisError[2]},{hysteresisError[3]},{hysteresisError[4]},{hysteresisError[5]}")
    repeatability = [0.0] * 6
    rtn, repeatability = robot.JointRepeatability()
    print(f"JointRepeatability result is {repeatability[0]},{repeatability[1]},{repeatability[2]},{repeatability[3]},{repeatability[4]},{repeatability[5]}")
    M = [1.0] * 6
    B = [1.0] * 6
    K = [0.0] * 6
    threshold = [1.0] * 6
    setZeroFlag = 1
    rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag)
    print(f"SetAdmittanceParams rtn is {rtn}")
    robot.CloseRPC()

Obter Número de Quadros com Erro nas 8 Portas Escravas do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSlavePortErrCounter()``"
    "Descrição", "Obtém o número de quadros com erro nas 8 portas escravas do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``inRecvErr``: Número de quadros com erro de receção de entrada
    - ``inCRCErr``: Número de quadros com erro CRC de entrada
    - ``inTransmitErr``: Número de quadros com erro de transmissão de entrada
    - ``inLinkErr``: Número de quadros com erro de ligação de entrada
    - ``outRecvErr``: Número de quadros com erro de receção de saída
    - ``outCRCErr``: Número de quadros com erro CRC de saída
    - ``outTransmitErr``: Número de quadros com erro de transmissão de saída
    - ``outLinkErr``: Número de quadros com erro de ligação de saída"

Limpar Quadros com Erro nas Portas Escravas
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointSensitivityEnable(slaveID)``"
    "Descrição", "Limpa os quadros com erro nas portas escravas"
    "Parâmetros obrigatórios", "- ``slaveID``: ID da escrava 0~7"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Obter Quadros com Erro nas Portas Escravas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    inRecvErr = [0] * 8
    inCRCErr = [0] * 8
    inTransmitErr = [0] * 8
    inLinkErr = [0] * 8
    outRecvErr = [0] * 8
    outCRCErr = [0] * 8
    outTransmitErr = [0] * 8
    outLinkErr = [0] * 8
    rtn, inRecvErr, inCRCErr, inTransmitErr, inLinkErr, outRecvErr, outCRCErr, outTransmitErr, outLinkErr = robot.GetSlavePortErrCounter()
    for i in range(8):
        if inRecvErr[i] != 0:
            print(f"inRecvErr {i} is {inRecvErr[i]}")
        if inCRCErr[i] != 0:
            print(f"inCRCErr {i} is {inCRCErr[i]}")
        if inTransmitErr[i] != 0:
            print(f"inTransmitErr {i} is {inTransmitErr[i]}")
        if inLinkErr[i] != 0:
            print(f"inLinkErr {i} is {inLinkErr[i]}")
        if outRecvErr[i] != 0:
            print(f"outRecvErr {i} is {outRecvErr[i]}")
        if outCRCErr[i] != 0:
            print(f"outCRCErr {i} is {outCRCErr[i]}")
        if outTransmitErr[i] != 0:
            print(f"outTransmitErr {i} is {outTransmitErr[i]}")
        if outLinkErr[i] != 0:
            print(f"outLinkErr {i} is {outLinkErr[i]}")
    print("others has no err!")
    for i in range(8):
        robot.SlavePortErrCounterClear(i)
    robot.CloseRPC()

Definir Coeficiente de Feedforward de Velocidade por Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetVelFeedForwardRatio(radio)``"
    "Descrição", "Define o coeficiente de feedforward de velocidade por eixo"
    "Parâmetros obrigatórios", "- ``radio``: Coeficiente de feedforward de velocidade por eixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Coeficiente de Feedforward de Velocidade por Eixo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetVelFeedForwardRatio()``"
    "Descrição", "Obtém o coeficiente de feedforward de velocidade por eixo"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``radio``: Coeficiente de feedforward de velocidade por eixo"

Exemplo de Código do Coeficiente de Feedforward de Velocidade do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    setRadio = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    robot.SetVelFeedForwardRatio(setRadio)
    getRadio = [0.0] * 6
    rtn, getRadio = robot.GetVelFeedForwardRatio()
    print(f"{getRadio[0]},{getRadio[1]},{getRadio[2]},{getRadio[3]},{getRadio[4]},{getRadio[5]}")
    robot.CloseRPC()

Calibração TCP do Sensor Fotoelétrico - Calcular RPY da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TCPComputeRPY(Btool, Etool, sensor, radius, dz)``"
    "Descrição", "Calibração TCP do sensor fotoelétrico - calcular RPY da ferramenta"
    "Parâmetros obrigatórios", "
    - ``Btool``: Posição cartesiana do robô
    - ``Etool``: Valor atual do sistema de coordenadas da ferramenta
    - ``Btsenserool``: Valor atual do sistema de coordenadas do sensor (não disponível no momento)
    - ``radius``: Raio do movimento circular mm (não disponível no momento)
    - ``dz``: Distância de movimento na direção negativa do eixo z do sistema de coordenadas base; quando dz = 10000, a função retorna diretamente o RPY da ferramenta"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Calibração TCP do Sensor Fotoelétrico - Calcular XYZ da Ferramenta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TCPComputeXYZ(select, originDirection, pos1, pos2, pos3, pos4)``"
    "Descrição", "Calibração TCP do sensor fotoelétrico - calcular XYZ da ferramenta"
    "Parâmetros obrigatórios", "
    - ``select``: 0-calcular TCP da ferramenta; 1-calcular origem do sensor; 2-calcular postura do sensor; 3-retornar diretamente o TCP da ferramenta; 4-registrar o sistema de coordenadas atual da peça e da ferramenta
    - ``originDirection``: 0-Direção X; 1-Direção Y; 2-Direção Z
    - ``pos1``: Posição cartesiana do robô 1
    - ``pos2``: Posição cartesiana do robô 2
    - ``pos3``: Posição cartesiana do robô 3
    - ``pos4``: Posição cartesiana do robô 4"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "
    - Código de erro: sucesso-0, falha-código de erro
    - Valor de retorno (se a chamada for bem-sucedida) TCP: valor XYZ da ferramenta"

Calibração TCP do Sensor Fotoelétrico - Iniciar Gravação da Posição do Centro do Flange da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TCPRecordFlangePosStart()``"
    "Descrição", "Calibração TCP do sensor fotoelétrico - iniciar gravação da posição do centro do flange da extremidade"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Calibração TCP do Sensor Fotoelétrico - Parar Gravação da Posição do Centro do Flange da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TCPRecordFlangePosEnd()``"
    "Descrição", "Calibração TCP do sensor fotoelétrico - parar gravação da posição do centro do flange da extremidade"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Calibração TCP do Sensor Fotoelétrico - Obter Posição do Centro da Ponta da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TCPGetRecordFlangePos()``"
    "Descrição", "Calibração TCP do sensor fotoelétrico - obter posição do centro da ponta da ferramenta"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "
    - Código de erro: sucesso-0, falha-código de erro
    - Valor de retorno (se a chamada for bem-sucedida) TCP: posição do centro da ponta da ferramenta (x, y, z)"

Calibração TCP do Sensor Fotoelétrico
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PhotoelectricSensorTCPCalibration(luaPath, offsetX)``"
    "Descrição", "Calibração TCP do sensor fotoelétrico"
    "Parâmetros obrigatórios", "
    - ``luaPath``: Caminho do programa lua para calibração automática: para robôs da versão QX - '/fruser/FR_CalibrateTheToolTcp.lua'; para robôs da versão LA - '/usr/local/etc/controller/lua/FR_CalibrateTheToolTcp.lua'
    - ``offsetX``: Deslocamento do ponto de ensino (x, y, z) mm"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "
    - Código de erro: sucesso-0, falha-código de erro
    - Valor de retorno (se a chamada for bem-sucedida) TCP: valor XYZ da ferramenta"

Exemplo de Código de Calibração TCP do Sensor Fotoelétrico
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    offset = [10.0, 10.0, 3.0]
    TCP = [0.0] * 6
    rtn, TCP = robot.PhotoelectricSensorTCPCalibration("/fruser/FR_CalibrateTheToolTcp.lua", offset)
    print(f"PhotoelectricSensorTCPCalibration rtn is {rtn},{TCP[0]},{TCP[1]},{TCP[2]},{TCP[3]},{TCP[4]},{TCP[5]}")
    robot.CloseRPC()
    return 0