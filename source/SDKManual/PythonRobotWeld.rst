Soldagem
======================

.. toctree::
    :maxdepth: 5

Definir Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime)``"
    "Descrição", "Define os parâmetros da curva de processo de soldagem"
    "Parâmetros obrigatórios", "
    - ``id``: Número do processo de soldagem (1-99)
    - ``startCurrent``: Corrente de abertura de arco (A)
    - ``startVoltage``: Tensão de abertura de arco (V)
    - ``startTime``: Tempo de abertura de arco (ms)
    - ``weldCurrent``: Corrente de soldagem (A)
    - ``weldVoltage``: Tensão de soldagem (V)
    - ``endCurrent``: Corrente de fechamento de arco (A)
    - ``endVoltage``: Tensão de fechamento de arco (V)
    - ``endTime``: Tempo de fechamento de arco (ms)
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingGetProcessParam(id)``"
    "Descrição", "Obtém os parâmetros da curva de processo de soldagem"
    "Parâmetros obrigatórios", "
    - ``id``: Número do processo de soldagem (1-99)
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``startCurrent``: Corrente de abertura de arco (A)
    - ``startVoltage``: Tensão de abertura de arco (V)
    - ``startTime``: Tempo de abertura de arco (ms)
    - ``weldCurrent``: Corrente de soldagem (A)
    - ``weldVoltage``: Tensão de soldagem (V)
    - ``endCurrent``: Corrente de fechamento de arco (A)
    - ``endVoltage``: Tensão de fechamento de arco (V)
    - ``endTime``: Tempo de fechamento de arco (ms)
    "

Definir Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)``"
    "Descrição", "Define a relação entre corrente de soldagem e saída analógica"
    "Parâmetros obrigatórios", "- ``currentMin``: Valor de corrente do ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    - ``currentMax``: Valor de corrente do ponto direito da relação linear corrente de soldagem-saída analógica (A)
    - ``outputVoltageMin``: Valor de tensão de saída analógica do ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    - ``outputVoltageMax``: Valor de tensão de saída analógica do ponto direito da relação linear corrente de soldagem-saída analógica (V)
    - ``AOIndex``: Porta de saída analógica para corrente de soldagem"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)``"
    "Descrição", "Define a relação entre tensão de soldagem e saída analógica"
    "Parâmetros obrigatórios", "- ``weldVoltageMin``: Valor de tensão de soldagem do ponto esquerdo da relação linear tensão de soldagem-saída analógica (A)
    - ``weldVoltageMax``: Valor de tensão de soldagem do ponto direito da relação linear tensão de soldagem-saída analógica (A)
    - ``outputVoltageMin``: Valor de tensão de saída analógica do ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    - ``outputVoltageMax``: Valor de tensão de saída analógica do ponto direito da relação linear tensão de soldagem-saída analógica (V)
    - ``AOIndex``: Porta de saída analógica para tensão de soldagem"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingGetCurrentRelation()``"
    "Descrição", "Obtém a relação entre corrente de soldagem e saída analógica"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``currentMin``: Valor de corrente do ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    - ``currentMax``: Valor de corrente do ponto direito da relação linear corrente de soldagem-saída analógica (A)
    - ``outputVoltageMin``: Valor de tensão de saída analógica do ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    - ``outputVoltageMax``: Valor de tensão de saída analógica do ponto direito da relação linear corrente de soldagem-saída analógica (V)
    - ``AOIndex``: Porta de saída analógica para tensão de soldagem"

Obter Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingGetVoltageRelation()``"
    "Descrição", "Obtém a relação entre tensão de soldagem e saída analógica"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``weldVoltageMin``: Valor de tensão de soldagem do ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    - ``weldVoltageMax``: Valor de tensão de soldagem do ponto direito da relação linear tensão de soldagem-saída analógica (V)
    - ``outputVoltageMin``: Valor de tensão de saída analógica do ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    - ``outputVoltageMax``: Valor de tensão de saída analógica do ponto direito da relação linear corrente de soldagem-saída analógica (V)
    - ``AOIndex``: Porta de saída analógica para tensão de soldagem"

Definir Corrente de Soldagem
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetCurrent(ioType, current, AOIndex, blend)``"
    "Descrição", "Define a corrente de soldagem"
    "Parâmetros obrigatórios", "- ``ioType``: Tipo 0-E/S do controlador; 1-E/S estendida
    - ``current``: Valor da corrente de soldagem (A)
    - ``AOIndex``: Porta de saída analógica da caixa de controle para corrente de soldagem (0-1)
    - ``blend``: Se suaviza 0-não suaviza, 1-suaviza"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Tensão de Soldagem
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetVoltage(ioType, voltage, AOIndex, blend)``"
    "Descrição", "Define a tensão de soldagem"
    "Parâmetros obrigatórios", "- ``ioType``: Tipo 0-E/S do controlador; 1-E/S estendida
    - ``voltage``: Valor da tensão de soldagem (V)
    - ``AOIndex``: Porta de saída analógica da caixa de controle para corrente de soldagem (0-1)
    - ``blend``: Se suaviza 0-não suaviza, 1-suaviza"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Parâmetros de Oscilação
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftRange, weaveRightRange, additionalStayTime, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary, weaveYawAngle, weaveRotAngle)``"
    "Descrição", "Define os parâmetros de oscilação"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número de configuração dos parâmetros de oscilação de soldagem
    - ``weaveType``: Tipo de oscilação 0-oscilação triangular plana; 1-oscilação triangular em L vertical; 2-oscilação circular horária; 3-oscilação circular anti-horária; 4-oscilação senoidal plana; 5-oscilação senoidal em L vertical; 6-oscilação triangular vertical; 7-oscilação senoidal vertical
    - ``weaveFrequency``: Frequência de oscilação (Hz)
    - ``weaveIncStayTime``: Modo de espera 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    - ``weaveRange``: Amplitude de oscilação (mm)
    - ``weaveLeftRange``: Comprimento da corda esquerda da oscilação triangular vertical (mm)
    - ``weaveRightRange``: Comprimento da corda direita da oscilação triangular vertical (mm)
    - ``additionalStayTime``: Tempo de permanência no ponto vertical da oscilação triangular vertical (mm)
    - ``weaveLeftStayTime``: Tempo de permanência à esquerda da oscilação (ms)
    - ``weaveRightStayTime``: Tempo de permanência à direita da oscilação (ms)
    - ``weaveCircleRadio``: Oscilação circular - taxa de retorno (0-100%)
    - ``weaveStationary``: Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera; 1-posição permanece estática durante o tempo de espera"
    "Parâmetros padrão", "- ``weaveYawAngle``: Ângulo de direção da oscilação (rotação em torno do eixo Z da oscilação), em graus, padrão 0
    - ``weaveRotAngle``: Ângulo de direção da oscilação (rotação em torno do eixo X da oscilação), em graus, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Definir Parâmetros de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000)
    robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333)
    start_current = 0
    start_voltage = 0
    start_time = 0
    weld_current = 0
    weld_voltage = 0
    end_current = 0
    end_voltage = 0
    end_time = 0
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current, end_voltage, end_time = robot.WeldingGetProcessParam(1)
    print(f"the Num 1 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current, end_voltage, end_time = robot.WeldingGetProcessParam(2)
    print(f"the Num 2 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0)
    print(f"WeldingSetCurrentRelation rtn is: {rtn}")
    rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1)
    print(f"WeldingSetVoltageRelation rtn is: {rtn}")
    current_min = 0
    current_max = 0
    vol_min = 0
    vol_max = 0
    output_vmin = 0
    output_vmax = 0
    cur_index = 0
    vol_index = 0
    rtn, current_min, current_max, output_vmin, output_vmax, cur_index = robot.WeldingGetCurrentRelation()
    print(f"WeldingGetCurrentRelation rtn is: {rtn}")
    print(f"current min {current_min} current max {current_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn, vol_min, vol_max, output_vmin, output_vmax, vol_index = robot.WeldingGetVoltageRelation()
    print(f"WeldingGetVoltageRelation rtn is: {rtn}")
    print(f"vol min {vol_min} vol max {vol_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn = robot.WeldingSetCurrent(1, 100, 0, 0)
    print(f"WeldingSetCurrent rtn is: {rtn}")
    time.sleep(3)
    rtn = robot.WeldingSetVoltage(1, 10, 0, 0)
    print(f"WeldingSetVoltage rtn is: {rtn}")
    rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 0.0, 60.000000)
    print(f"rtn is: {rtn}")
    robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0)
    rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200)
    print(f"WeldingSetCheckArcInterruptionParam {rtn}")
    rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0)
    print(f"WeldingSetReWeldAfterBreakOffParam {rtn}")
    enable = 0
    length = 0
    velocity = 0
    move_type = 0
    check_enable = 0
    arc_interrupt_time_length = 0
    rtn, check_enable, arc_interrupt_time_length = robot.WeldingGetCheckArcInterruptionParam()
    print(f"WeldingGetCheckArcInterruptionParam checkEnable {check_enable} arcInterruptTimeLength {arc_interrupt_time_length}")
    rtn, enable, length, velocity, move_type = robot.WeldingGetReWeldAfterBreakOffParam()
    print(f"WeldingGetReWeldAfterBreakOffParam enable = {enable}, length = {length}, velocity = {velocity}, moveType = {move_type}")
    robot.SetWeldMachineCtrlModeExtDoNum(17)
    for i in range(5):
        robot.SetWeldMachineCtrlMode(0)
        time.sleep(1)
        robot.SetWeldMachineCtrlMode(1)
        time.sleep(1)
    robot.CloseRPC()

Definir Parâmetros de Oscilação em Tempo Real
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveOnlineSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)``"
    "Descrição", "Define parâmetros de oscilação em tempo real"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número de configuração dos parâmetros de oscilação de soldagem
    - ``weaveType``: Tipo de oscilação 0-oscilação triangular plana; 1-oscilação triangular em L vertical; 2-oscilação circular horária; 3-oscilação circular anti-horária; 4-oscilação senoidal plana; 5-oscilação senoidal em L vertical; 6-oscilação triangular vertical; 7-oscilação senoidal vertical
    - ``weaveFrequency``: Frequência de oscilação (Hz)
    - ``weaveIncStayTime``: Modo de espera 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    - ``weaveRange``: Amplitude de oscilação (mm)
    - ``weaveLeftStayTime``: Tempo de permanência à esquerda da oscilação (ms)
    - ``weaveRightStayTime``: Tempo de permanência à direita da oscilação (ms)
    - ``weaveCircleRadio``: Oscilação circular - taxa de retorno (0-100%)
    - ``weaveStationary``: Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera; 1-posição permanece estática durante o tempo de espera"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingGetCheckArcInterruptionParam()``"
    "Descrição", "Obtém os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``checkEnable``: Se habilita a detecção; 0-não habilita; 1-habilita
    - ``arcInterruptTimeLength``: Duração de confirmação da interrupção do arco (ms)"

Definir Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetCheckArcInterruptionParam(checkEnable, arcInterruptTimeLength)``"
    "Descrição", "Define os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô"
    "Parâmetros obrigatórios", "- ``checkEnable``: Se habilita a detecção; 0-não habilita; 1-habilita
    - ``arcInterruptTimeLength``: Duração de confirmação da interrupção do arco (ms)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros de Recuperação de Interrupção de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingGetReWeldAfterBreakOffParam()``"
    "Descrição", "Obtém os parâmetros de recuperação de interrupção de soldagem do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``enable``: Se habilita a recuperação de interrupção de soldagem
    - ``length``: Distância de sobreposição da solda (mm)
    - ``velocity``: Percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100)
    - ``moveType``: Modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP"

Definir Parâmetros de Recuperação de Interrupção de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetReWeldAfterBreakOffParam(enable, length, velocity, moveType)``"
    "Descrição", "Define os parâmetros de recuperação de interrupção de soldagem do robô"
    "Parâmetros obrigatórios", "- ``enable``: Se habilita a recuperação de interrupção de soldagem
    - ``length``: Distância de sobreposição da solda (mm)
    - ``velocity``: Percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100)
    - ``moveType``: Modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Porta DO Estendida do Modo de Controle da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWeldMachineCtrlModeExtDoNum(DONum)``"
    "Descrição", "Define a porta DO estendida do modo de controle da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DONum``: Porta DO do modo de controle da máquina de solda (0-127)
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Modo de Controle da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWeldMachineCtrlMode(mode, ioType)``"
    "Descrição", "Define o modo de controle da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``ioType``: Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    - ``mode``: Modo de controle da máquina de solda; 0-unário
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início da Soldagem
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ARCStart(ioType, arcNum, timeout)``"
    "Descrição", "Início da soldagem"
    "Parâmetros obrigatórios", "- ``ioType``: Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    - ``arcNum``: Número do arquivo de configuração da máquina de solda
    - ``timeout``: Tempo limite de abertura de arco"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Soldagem
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ARCEnd(ioType, arcNum, timeout)``"
    "Descrição", "Fim da soldagem"
    "Parâmetros obrigatórios", "- ``ioType``: Tipo 0-E/S do controlador; 1-E/S estendida
    - ``arcNum``: Número do arquivo de configuração da máquina de solda
    - ``timeout``: Tempo limite de abertura de arco"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início da Oscilação
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveStart(weaveNum)``"
    "Descrição", "Início da oscilação"
    "Parâmetros obrigatórios", "- ``weaveNum``: Tipo 0-E/S do controlador; 1-E/S estendida"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Oscilação
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveEnd(weaveNum)``"
    "Descrição", "Fim da oscilação"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número de configuração dos parâmetros de oscilação de soldagem"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Alimentação de Arame para Frente
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetForwardWireFeed(ioType, wireFeed)``"
    "Descrição", "Alimentação de arame para frente"
    "Parâmetros obrigatórios", "- ``ioType``: 0-E/S do controlador; 1-E/S estendida
    - ``wireFeed``: Controle de alimentação de arame 0-parar alimentação; 1-alimentar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Alimentação de Arame para Trás
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetReverseWireFeed(ioType, wireFeed)``"
    "Descrição", "Alimentação de arame para trás"
    "Parâmetros obrigatórios", "- ``ioType``: 0-E/S do controlador; 1-E/S estendida
    - ``wireFeed``: Controle de alimentação de arame 0-parar alimentação; 1-alimentar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fornecimento de Gás
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAspirated(ioType, airControl)``"
    "Descrição", "Fornecimento de gás"
    "Parâmetros obrigatórios", "- ``ioType``: 0-E/S do controlador; 1-E/S estendida
    - ``airControl``: Controle de fornecimento de gás 0-parar fornecimento; 1-fornecer"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Retomada de Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingStartReWeldAfterBreakOff()``"
    "Descrição", "Define a retomada de soldagem do robô após interrupção"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Saída da Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingAbortWeldAfterBreakOff()``"
    "Descrição", "Define a saída da soldagem do robô após interrupção"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.SetForwardWireFeed(0, 1)
    time.sleep(1)
    robot.SetForwardWireFeed(0, 0)
    robot.SetReverseWireFeed(0, 1)
    time.sleep(1)
    robot.SetReverseWireFeed(0, 0)
    robot.SetAspirated(0, 1)
    time.sleep(1)
    robot.SetAspirated(0, 0)
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint, tool=13, user=0)
    robot.ARCStart(1, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=p2Desc, tool=13, user=0)
    robot.ARCEnd(1, 0, 10000)
    robot.WeaveEnd(0)
    robot.WeldingStartReWeldAfterBreakOff()
    robot.WeldingAbortWeldAfterBreakOff()
    robot.CloseRPC()

Início da Soldagem por Segmentos
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SegmentWeldStart(startDesePos, endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave, weaveNum, tool, user, vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, exaxis_pos=[0.0, 0.0, 0.0, 0.0], search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "Descrição", "Início da soldagem por segmentos"
    "Parâmetros obrigatórios", "- ``startDesePos``: Pose cartesiana inicial, unidades [mm][°]
    - ``endDesePos``: Pose cartesiana alvo, unidades [mm][°]
    - ``startJPos``: Posição articular inicial, unidades [°]
    - ``endJPos``: Posição articular alvo, unidades [°]
    - ``weldLength``: Comprimento de solda, unidades [mm]
    - ``noWeldLength``: Comprimento não soldado, unidades [mm]
    - ``weldIOType``: Tipo de E/S de soldagem (0-E/S da caixa de controle; 1-E/S estendida) arcNum Número do arquivo de configuração da máquina de solda
    - ``timeout``: Tempo limite de extinção do arco
    - ``isWeave``: Soldagem False-não soldar
    - ``weaveNum``: Número de configuração dos parâmetros de oscilação de soldagem
    - ``tool``: Número da ferramenta, [0~14]
    - ``user``: Número da peça, [0~14]"
    "Parâmetros padrão", "- ``vel``: Percentagem de velocidade, [0~100] padrão 20.0
    - ``acc``: Aceleração [0~100] temporariamente não disponível, padrão 0.0
    - ``ovl``: Fator de escala de velocidade, [0~100] padrão 100.0
    - ``blendR``: [-1.0]-movimento até o final (bloqueante), [0~1000]-raio de suavização (não bloqueante), unidade [mm] padrão -1.0
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4, padrão [0.0,0.0,0.0,0.0]
    - ``search``: [0]-sem busca de posição do arame, [1]-com busca de posição do arame
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta, padrão 0
    - ``offset_pos``: Deslocamento de pose, unidades [mm][°] padrão [0.0,0.0,0.0,0.0,0.0,0.0]"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Soldagem por Segmentos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    rtn = robot.SegmentWeldStart(p1Desc, p2Desc, p1Joint, p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0)
    print(f"SegmentWeldStart rtn is {rtn}")
    robot.CloseRPC()

Início da Oscilação de Simulação
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveStartSim(weaveNum)``"
    "Descrição", "Início da oscilação de simulação"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número do parâmetro de oscilação"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Oscilação de Simulação
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveEndSim(weaveNum)``"
    "Descrição", "Fim da oscilação de simulação"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número do parâmetro de oscilação"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início da Detecção de Alerta de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveInspectStart(weaveNum)``"
    "Descrição", "Início da detecção de alerta de trajetória (sem movimento)"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número do parâmetro de oscilação"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Detecção de Alerta de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveInspectEnd(weaveNum)``"
    "Descrição", "Fim da detecção de alerta de trajetória (sem movimento)"
    "Parâmetros obrigatórios", "- ``weaveNum``: Número do parâmetro de oscilação"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Início da Mudança Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveChangeStart(weaveChangeFlag, weaveNum, velStart, velEnd)``"
    "Descrição", "Início da mudança gradual da oscilação"
    "Parâmetros obrigatórios", "- ``weaveChangeFlag``: Número da oscilação 1-alterar parâmetro de oscilação; 2-alterar parâmetro de oscilação + velocidade de soldagem
    - ``weaveNum``: Número da oscilação
    - ``velStart``: Velocidade inicial de soldagem, (cm/min)
    - ``velEnd``: Velocidade final de soldagem, (cm/min)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Soldagem com Mudança Gradual de Oscilação do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint, tool=13, user=0)
    robot.WeaveStartSim(0)
    robot.MoveL(desc_pos=p2Desc, tool=13, user=0)
    robot.WeaveEndSim(0)
    robot.MoveJ(joint_pos=p1Joint, tool=13, user=0)
    robot.WeaveInspectStart(0)
    robot.MoveL(desc_pos=p2Desc, tool=13, user=0)
    robot.WeaveInspectEnd(0)
    robot.WeldingSetVoltage(1, 19, 0, 0)
    robot.WeldingSetCurrent(1, 190, 0, 0)
    robot.MoveL(desc_pos=p1Desc, tool=1, user=1, vel=100, acc=100, ovl=50)
    robot.ARCStart(1, 0, 10000)
    robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(1, 0, 50, 30)
    robot.MoveL(desc_pos=p2Desc, tool=1, user=1, vel=100)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.ARCEnd(1, 0, 10000)
    robot.CloseRPC()

Fim da Mudança Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeaveChangeEnd()``"
    "Descrição", "Fim da mudança gradual da oscilação"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Detecção de Gás da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAirControlExtDoNum(DONum)``"
    "Descrição", "E/S estendida - configurar sinal de detecção de gás da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DONum``: Número DO estendido do sinal de detecção de gás
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Abertura de Arco da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetArcStartExtDoNum(DONum)``"
    "Descrição", "E/S estendida - configurar sinal de abertura de arco da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DONum``: Número DO estendido do sinal de detecção de gás
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Alimentação de Arame para Trás da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWireReverseFeedExtDoNum(DONum)``"
    "Descrição", "E/S estendida - configurar sinal de alimentação de arame para trás da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DONum``: Número DO estendido do sinal de detecção de gás
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Alimentação de Arame para Frente da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWireForwardFeedExtDoNum(DONum)``"
    "Descrição", "E/S estendida - configurar sinal de alimentação de arame para frente da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DONum``: Número DO estendido do sinal de detecção de gás
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Sucesso de Abertura de Arco da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetArcDoneExtDiNum(DINum)``"
    "Descrição", "E/S estendida - configurar sinal de sucesso de abertura de arco da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DINum``: Número DI estendido do sinal de prontidão da máquina de solda
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Prontidão da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetArcDoneExtDiNum(DINum)``"
    "Descrição", "E/S estendida - configurar sinal de prontidão da máquina de solda"
    "Parâmetros obrigatórios", "
    - ``DINum``: Número DI estendido do sinal de prontidão da máquina de solda
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

E/S Estendida - Configurar Sinal de Recuperação de Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExtDIWeldBreakOffRecover(reWeldDINum, abortWeldDINum)``"
    "Descrição", "E/S estendida - configurar sinal de recuperação de interrupção de soldagem"
    "Parâmetros obrigatórios", "
    - ``reWeldDINum``: Número DI estendido do sinal de retomada de soldagem após interrupção
    - ``abortWeldDINum``: Número DI estendido do sinal de saída de soldagem após interrupção
    "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Configurar Sinais de Soldagem com E/S Estendida
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetArcStartExtDoNum(10)
    print(f"SetArcStartExtDoNum rtn is {rtn}")
    rtn = robot.SetAirControlExtDoNum(20)
    print(f"SetAirControlExtDoNum rtn is {rtn}")
    rtn = robot.SetWireForwardFeedExtDoNum(30)
    print(f"SetWireForwardFeedExtDoNum rtn is {rtn}")
    rtn = robot.SetWireReverseFeedExtDoNum(40)
    rtn = robot.SetWeldReadyExtDiNum(50)
    print(f"SetWeldReadyExtDiNum rtn is {rtn}")
    rtn = robot.SetArcDoneExtDiNum(60)
    print(f"SetArcDoneExtDiNum rtn is {rtn}")
    rtn = robot.SetExtDIWeldBreakOffRecover(70, 80)
    print(f"SetExtDIWeldBreakOffRecover rtn is {rtn}")
    rtn = robot.SetWireSearchExtDIONum(0, 1)
    print(f"SetWireSearchExtDIONum rtn is {rtn}")
    robot.CloseRPC()

Controle de Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceControl(flag, delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd, sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent, offsetType, offsetParameter)``"
    "Descrição", "Controle de rastreamento de arco"
    "Parâmetros obrigatórios", "- ``flag``: Chave, 0-desligar; 1-ligar
    - ``delayTime``: Tempo de atraso, em ms
    - ``isLeftRight``: Compensação de desvio esquerda/direita 0-desativar, 1-ativar
    - ``klr``: Coeficiente de ajuste esquerda/direita (sensibilidade)
    - ``tStartLr``: Tempo de início da compensação esquerda/direita cyc
    - ``stepMaxLr``: Quantidade máxima de compensação por vez esquerda/direita mm
    - ``sumMaxLr``: Quantidade máxima total de compensação esquerda/direita mm
    - ``isUpLow``: Compensação de desvio acima/abaixo 0-desativar, 1-ativar
    - ``kud``: Coeficiente de ajuste acima/abaixo (sensibilidade)
    - ``tStartUd``: Tempo de início da compensação acima/abaixo cyc
    - ``stepMaxUd``: Quantidade máxima de compensação por vez acima/abaixo mm
    - ``sumMaxUd``: Quantidade máxima total de compensação acima/abaixo
    - ``axisSelect``: Seleção do sistema de coordenadas acima/abaixo, 0-oscilação; 1-ferramenta; 2-base
    - ``referenceType``: Modo de definição da corrente de referência acima/abaixo, 0-feedback; 1-constante
    - ``referSampleStartUd``: Início da amostragem da corrente de referência acima/abaixo (feedback), cyc
    - ``referSampleCountUd``: Contagem do ciclo de amostragem da corrente de referência acima/abaixo (feedback), cyc
    - ``referenceCurrent``: Corrente de referência acima/abaixo mA
    - ``offsetType``: Tipo de rastreamento com deslocamento, 0-sem deslocamento; 1-amostragem; 2-percentagem
    - ``offsetParameter``: Parâmetro de deslocamento; amostragem (tempo de início da amostragem de deslocamento, padrão um ciclo); percentagem (percentagem de deslocamento (-100 ~ 100))"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Seleção da Banda de Passagem AI do Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceExtAIChannelConfig(channel)``"
    "Descrição", "Seleção da banda de passagem AI do rastreamento de arco"
    "Parâmetros obrigatórios", "- ``channel``: Banda de passagem AI do rastreamento de arco, [0-3]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Ativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceReplayStart()``"
    "Descrição", "Ativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceReplayEnd()``"
    "Descrição", "Desativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Mudança de Coordenadas de Deslocamento - Soldagem de Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``MultilayerOffsetTrsfToBase(pointo, pointX, pointZ, dx, dy, db)``"
    "Descrição", "Mudança de coordenadas de deslocamento - soldagem de múltiplas camadas e múltiplos passes"
    "Parâmetros obrigatórios", "- ``pointo``: Pose cartesiana do ponto de referência
    - ``pointX``: Pose cartesiana do ponto de direção de deslocamento no eixo X do ponto de referência
    - ``pointZ``: Pose cartesiana do ponto de direção de deslocamento no eixo Z do ponto de referência
    - ``dx``: Quantidade de deslocamento na direção X (mm)
    - ``dz``: Quantidade de deslocamento na direção Z (mm)
    - ``dry``: Quantidade de deslocamento em torno do eixo Y (°)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``offset``: Deslocamento calculado"

Exemplo de Código de Rastreamento de Arco com Soldagem de Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    mulitilineorigin1_joint = [-24.090, -63.501, 84.288, -111.940, -93.426, 57.669]
    mulitilineorigin1_desc = [-677.559, 190.951, -1.205, 1.144, -41.482, -82.577]
    mulitilineX1_desc = [-677.556, 211.949, -1.206]
    mulitilineZ1_desc = [-677.564, 190.956, 19.817]
    mulitilinesafe_joint = [-25.734, -63.778, 81.502, -108.975, -93.392, 56.021]
    mulitilinesafe_desc = [-677.561, 211.950, 19.812, 1.144, -41.482, -82.577]
    mulitilineorigin2_joint = [-29.743, -75.623, 101.241, -116.354, -94.928, 55.735]
    mulitilineorigin2_desc = [-563.961, 215.359, -0.681, 2.845, -40.476, -87.443]
    mulitilineX2_desc = [-563.965, 220.355, -0.680]
    mulitilineZ2_desc = [-563.968, 215.362, 4.331]
    epos = [0, 0, 0, 0]
    offset = [0, 0, 0, 0, 0, 0]
    time.sleep(0.01)
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin1_desc, tool=13, user=0, vel=10, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin2_desc, tool=13, user=0, vel=10, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin1_desc, tool=13, user=0, vel=10, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error = robot.WeaveStart(0)
    print(f"WeaveStart return: {error}")
    error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10, 0, 0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin2_desc, tool=13, user=0, vel=1, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10, 0, 0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.WeaveEnd(0)
    print(f"WeaveEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin1_desc, tool=13, user=0, vel=10, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin2_desc, tool=13, user=0, vel=2, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin1_desc, tool=13, user=0, vel=10, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0)
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos=mulitilineorigin2_desc, tool=13, user=0, vel=2, speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 3000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos=mulitilinesafe_joint, tool=13, user=0, vel=10)
    print(f"MoveJ return: {error}")
    robot.CloseRPC()

Seleção do Canal AI de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceAIChannelCurrent(channel)``"
    "Descrição", "Seleção do canal AI de feedback de corrente da máquina de solda para rastreamento de arco"
    "Parâmetros obrigatórios", "- ``channel``: Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Seleção do Canal AI de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceAIChannelVoltage(channel)``"
    "Descrição", "Seleção do canal AI de feedback de tensão da máquina de solda para rastreamento de arco"
    "Parâmetros obrigatórios", "- ``channel``: Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parâmetros de Conversão de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceCurrentPara(AILow, AIHigh, currentLow, currentHigh)``"
    "Descrição", "Parâmetros de conversão de feedback de corrente da máquina de solda para rastreamento de arco"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``AILow``: Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
    - ``AIHigh``: Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
    - ``currentLow``: Valor de corrente da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
    - ``currentHigh``: Valor de corrente da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Parâmetros de Conversão de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ArcWeldTraceVoltagePara(AILow, AIHigh, voltageLow, voltageHigh)``"
    "Descrição", "Parâmetros de conversão de feedback de tensão da máquina de solda para rastreamento de arco"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``AILow``: Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
    - ``AIHigh``: Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
    - ``voltageLow``: Valor de tensão da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
    - ``voltageHigh``: Valor de tensão da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')

    safetydescPose = [-504.043, 275.181, 40.908, -28.002, -42.025, -14.044]
    safetyjointPos = [-39.078, -76.732, 87.227, -99.47, -94.301, 18.714]
    startdescPose = [-473.86, 257.879, -20.849, -37.317, -42.021, 2.543]
    startjointPos = [-43.487, -76.526, 95.568, -104.445, -89.356, 3.72]
    enddescPose = [-499.844, 141.225, 7.72, -34.856, -40.17, 13.13]
    endjointPos = [-31.305, -82.998, 99.401, -104.426, -89.35, 3.696]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ---- definir tensão
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ---- definir corrente
    rtn = robot.ArcWeldTraceAIChannelCurrent(4)
    print("ArcWeldTraceAIChannelCurrent rtn is", rtn)
    rtn = robot.ArcWeldTraceAIChannelVoltage(5)
    print("ArcWeldTraceAIChannelVoltage rtn is", rtn)
    rtn = robot.ArcWeldTraceCurrentPara(0, 5, 0, 500)
    print("ArcWeldTraceCurrentPara rtn is", rtn)
    rtn = robot.ArcWeldTraceVoltagePara(1.018, 10, 0, 50)
    print("ArcWeldTraceVoltagePara rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=20, acc=100)
    robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl=2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)

Definir Portas E/S Estendidas para Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetWireSearchExtDIONum(searchDoneDINum, searchStartDONum)``"
    "Descrição", "Define as portas E/S estendidas para busca de posição do arame de solda"
    "Parâmetros obrigatórios", "- ``searchDoneDINum``: Porta DO de sucesso na busca de posição do arame (0-127)
    - ``searchStartDONum``: Porta DO de controle de início/parada da busca de posição do arame (0-127)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código
++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    toolCoord = [0, 0, 200, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    wobjCoord = [0, 0, 0, 0, 0, 0]
    robot.SetWObjCoord(1, wobjCoord, 0)
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10)
    robot.ExtDevLoadUDPDriver()
    robot.SetWireSearchExtDIONum(0, 0)
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    descStart = [216.543, 445.175, 93.465, 179.683, 1.757, -112.641]
    jointStart = [-128.345, -86.660, 114.679, -119.625, -89.219, 74.303]
    descEnd = [111.143, 523.384, 87.659, 179.703, 1.835, -97.750]
    jointEnd = [-113.454, -81.060, 109.328, -119.954, -89.218, 74.302]
    error = robot.MoveL(desc_pos=descStart, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    descREF0A = [142.135, 367.604, 86.523, 179.728, 1.922, -111.089]
    jointREF0A = [-126.794, -100.834, 128.922, -119.864, -89.218, 74.302]
    descREF0B = [254.633, 463.125, 72.604, 179.845, 2.341, -114.704]
    jointREF0B = [-130.413, -81.093, 112.044, -123.163, -89.217, 74.303]
    descREF1A = [92.556, 485.259, 47.476, -179.932, 3.130, -97.512]
    jointREF1A = [-113.231, -83.815, 119.877, -129.092, -89.217, 74.303]
    descREF1B = [203.103, 583.836, 63.909, 179.991, 2.854, -103.372]
    jointREF1B = [-119.088, -69.676, 98.692, -121.761, -89.219, 74.303]
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF1A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF1B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF1A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF1B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    varNameRef = ["REF0", "REF1", "#", "#", "#", "#"]
    varNameRes = ["RES0", "RES1", "#", "#", "#", "#"]
    offectFlag = 0
    offectPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error, offectFlag, offectPos = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes)
    print(f"GetWireSearchOffset return: {error}")
    error = robot.PointsOffsetEnable(0, offectPos)
    print(f"PointsOffsetEnable return: {error}")
    error = robot.MoveL(desc_pos=descStart, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.PointsOffsetDisable()
    robot.CloseRPC()

Início da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WireSearchStart(refPos, searchVel, searchDis, autoBackFlag, autoBackVel, autoBackDis, offectFlag)``"
    "Descrição", "Início da busca de posição do arame de solda"
    "Parâmetros obrigatórios", "- ``refPos``: 1-ponto de referência 0-ponto de contato
    - ``searchVel``: Velocidade de busca %
    - ``searchDis``: Distância de busca mm
    - ``autoBackFlag``: Flag de retorno automático, 0-não automático; -automático
    - ``autoBackVel``: Velocidade de retorno automático %
    - ``autoBackDis``: Distância de retorno automático mm
    - ``offectFlag``: 1-busca com deslocamento; 0-busca no ponto ensinado"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Fim da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WireSearchEnd(refPos, searchVel, searchDis, autoBackFlag, autoBackVel, autoBackDis, offectFlag)``"
    "Descrição", "Fim da busca de posição do arame de solda"
    "Parâmetros obrigatórios", "- ``refPos``: 1-ponto de referência 2-ponto de contato
    - ``searchVel``: Velocidade de busca %
    - ``searchDis``: Distância de busca mm
    - ``autoBackFlag``: Flag de retorno automático, 0-não automático; -automático
    - ``autoBackVel``: Velocidade de retorno automático %
    - ``autoBackDis``: Distância de retorno automático mm
    - ``offectFlag``: 1-busca com deslocamento; 2-busca no ponto ensinado"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular Deslocamento da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetWireSearchOffset(seamType, method, varNameRef, varNameRes)``"
    "Descrição", "Calcula o deslocamento da busca de posição do arame de solda"
    "Parâmetros obrigatórios", "- ``seamType``: Tipo de solda
    - ``method``: Método de cálculo
    - ``varNameRef``: Pontos de referência 1-6, `#` indica ausência de ponto variável
    - ``varNameRes``: Pontos de contato 1-6, `#` indica ausência de ponto variável"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``offsetFlag``: 0-deslocamento adicionado diretamente ao ponto de comando; 1-deslocamento requer transformação de coordenadas do ponto de comando
    - ``offset``: Deslocamento da pose [x, y, z, a, b, c]"

Aguardar Conclusão da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WireSearchWait(varname)``"
    "Descrição", "Aguarda a conclusão da busca de posição do arame de solda"
    "Parâmetros obrigatórios", "- ``varName``: Nome do ponto de contato `RES0 ~ RES99`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Escrever Ponto de Contato da Busca de Posição do Arame no Banco de Dados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetPointToDatabase(varName, pos)``"
    "Descrição", "Escreve o ponto de contato da busca de posição do arame no banco de dados"
    "Parâmetros obrigatórios", "- ``varName``: Nome do ponto de contato `RES0 ~ RES99`
    - ``pos``: Dados do ponto de contato [x, y, x, a, b, c]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Busca de Posição do Arame de Solda do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    toolCoord = [0, 0, 200, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    wobjCoord = [0, 0, 0, 0, 0, 0]
    robot.SetWObjCoord(1, wobjCoord, 0)
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    descStart = [216.543, 445.175, 93.465, 179.683, 1.757, -112.641]
    jointStart = [-128.345, -86.660, 114.679, -119.625, -89.219, 74.303]
    descEnd = [111.143, 523.384, 87.659, 179.703, 1.835, -97.750]
    jointEnd = [-113.454, -81.060, 109.328, -119.954, -89.218, 74.302]
    error = robot.MoveL(desc_pos=descStart, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    descREF0A = [142.135, 367.604, 86.523, 179.728, 1.922, -111.089]
    jointREF0A = [-126.794, -100.834, 128.922, -119.864, -89.218, 74.302]
    descREF0B = [254.633, 463.125, 72.604, 179.845, 2.341, -114.704]
    jointREF0B = [-130.413, -81.093, 112.044, -123.163, -89.217, 74.303]
    descREF1A = [92.556, 485.259, 47.476, -179.932, 3.130, -97.512]
    jointREF1A = [-113.231, -83.815, 119.877, -129.092, -89.217, 74.303]
    descREF1B = [203.103, 583.836, 63.909, 179.991, 2.854, -103.372]
    jointREF1B = [-119.088, -69.676, 98.692, -121.761, -89.219, 74.303]
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF1A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF1B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF1A, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF1B, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    varNameRef = ["REF0", "REF1", "#", "#", "#", "#"]
    varNameRes = ["RES0", "RES1", "#", "#", "#", "#"]
    offectFlag = 0
    offectPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error, offectFlag, offectPos = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes)
    print(f"GetWireSearchOffset return: {error}")
    error = robot.PointsOffsetEnable(0, offectPos)
    print(f"PointsOffsetEnable return: {error}")
    error = robot.MoveL(desc_pos=descStart, tool=1, user=1, vel=100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd, tool=1, user=1, vel=100, search=1)
    print(f"MoveL return: {error}")
    error = robot.PointsOffsetDisable()
    robot.CloseRPC()

Definir Início da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetVoltageGradualChangeStart(IOType, voltageStart, voltageEnd, AOIndex, blend)``"
    "Descrição", "Define o início da mudança gradual da tensão de soldagem"
    "Parâmetros obrigatórios", "- ``IOType``: Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    - ``voltageStart``: Tensão de soldagem inicial (V)
    - ``voltageEnd``: Tensão de soldagem final (V)
    - ``AOIndex``: Número da porta AO da caixa de controle (0-1)
    - ``blend``: Se suaviza 0-não suaviza; 1-suaviza"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Fim da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetVoltageGradualChangeEnd()``"
    "Descrição", "Define o fim da mudança gradual da tensão de soldagem"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Início da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetCurrentGradualChangeStart(IOType, currentStart, currentEnd, AOIndex, blend)``"
    "Descrição", "Define o início da mudança gradual da corrente de soldagem"
    "Parâmetros obrigatórios", "- ``IOType``: Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    - ``currentStart``: Corrente de soldagem inicial (A)
    - ``currentEnd``: Corrente de soldagem final (A)
    - ``AOIndex``: Número da porta AO da caixa de controle (0-1)
    - ``blend``: Se suaviza 0-não suaviza; 1-suaviza"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Fim da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WeldingSetCurrentGradualChangeEnd()``"
    "Descrição", "Define o fim da mudança gradual da corrente de soldagem"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Mudança Gradual de Corrente e Tensão de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    startdescPose = [-484.707, 276.996, -14.013, -37.657, -40.508, -1.548]
    startjointPos = [-45.421, -75.673, 93.627, -104.302, -87.938, 6.005]
    enddescPose = [-508.767, 137.109, -13.966, -37.639, -40.508, -1.559]
    endjointPos = [-32.768, -80.947, 100.254, -106.201, -87.201, 18.648]
    safedescPose = [-484.709, 294.436, 13.621, -37.660, -40.508, -1.545]
    safejointPos = [-46.604, -75.410, 89.109, -100.003, -88.012, 4.823]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ---- definir tensão
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ---- definir corrente
    robot.MoveJ(joint_pos=safejointPos, tool=1, user=0, vel=5, acc=100)
    rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0)
    print("WeldingSetCurrentGradualChangeStart rtn is", rtn)
    rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0)
    print("WeldingSetVoltageGradualChangeStart rtn is", rtn)
    rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    print("ArcWeldTraceControl rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=5, acc=100)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(2, 1, 24, 36)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl=2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.WeldingSetCurrentGradualChangeEnd()
    robot.WeldingSetVoltageGradualChangeEnd()

Definir Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CustomWeaveSetPara(id, pointNum, point, stayTime, frequency, incStayType, stationary)``"
    "Descrição", "Define parâmetros de oscilação personalizada"
    "Parâmetros obrigatórios", "- ``id``: Número da oscilação personalizada: 0-2
    - ``pointNum``: Número de pontos de oscilação 0-10
    - ``point``: Dados do ponto de extremidade de movimento x, y, z
    - ``stayTime``: Tempo de permanência da oscilação ms
    - ``frequency``: Frequência de oscilação Hz
    - ``incStayType``: Modo de espera: 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    - ``stationary``: Espera na posição de oscilação: 0-continua movimento durante o tempo de espera; 1-posição permanece estática durante o tempo de espera"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros de Oscilação Personalizada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CustomWeaveGetPara(id)``"
    "Descrição", "Obtém parâmetros de oscilação personalizada"
    "Parâmetros obrigatórios", "- ``id``: Número da oscilação personalizada: 0-2"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``pointNum``: Número de pontos de oscilação 0-10
    - ``point``: Dados do ponto de extremidade de movimento x, y, z
    - ``stayTime``: Tempo de permanência da oscilação ms
    - ``frequency``: Frequência de oscilação Hz
    - ``incStayType``: Modo de espera: 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    - ``stationary``: Espera na posição de oscilação: 0-continua movimento durante o tempo de espera; 1-posição permanece estática durante o tempo de espera"

Exemplo de Código de Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    point = [0.0] * 30
    point[0] = -3.0
    point[1] = -3.0
    point[2] = 0.0
    point[3] = -6.0
    point[4] = 0.0
    point[5] = 0.0
    point[6] = -3.0
    point[7] = 3.0
    point[8] = 0.0
    point[9] = 0.0
    point[10] = 0.0
    point[11] = 0.0
    stayTime = [0.0] * 10
    rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0)
    print(f"CustomWeaveSetPara rtn is {rtn}")
    time.sleep(1)
    pointNum = 0
    frequency = 0.0
    incStayType = 0
    stationary = 0
    rtn, pointNum, point, stayTime, frequency, incStayType, stationary = robot.CustomWeaveGetPara(2)
    print(f"pointNum is {pointNum}")
    for i in range(pointNum):
        print(f"point {i}, point x y z {point[i * 3 + 0]},{point[i * 3 + 1]},{point[i * 3 + 2]}")
    print(f"fre is {frequency}, stay is {incStayType},{stationary}")
    robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000)
    desc_p1 = [-288.650, 367.807, 288.404, 0.000, -0.001, 0.001]
    desc_p2 = [-431.714, 367.815, 288.415, 0.001, 0.001, 0.000]
    desc_p3 = [-348.666, 427.798, 288.404, -0.000, -0.000, 0.001]
    j1 = [140.656, -84.560, -91.707, -93.734, 90.000, 50.655]
    j2 = [149.873, -98.298, -77.599, -94.103, 90.000, 59.873]
    j3 = [139.773, -96.173, -80.014, -93.814, 90.000, 49.772]
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.Circle(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50, oacc=10)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveC(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=desc_p2, tool=3, user=0, vel=100, ovl=10, speedPercent=100)
    robot.WeaveEnd(0)
    robot.CloseRPC()