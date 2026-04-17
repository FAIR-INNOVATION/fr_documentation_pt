Descrição das Estruturas de Dados
============================================

.. toctree::
    :maxdepth: 5

Pacote de Dados de Retroalimentação de Estado do Controlador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :header-rows: 1
    :name: Pacote de dados de retroalimentação de estado do controlador
    :widths: 20 30

    "Variável","Significado"
    "program_state","Estado de execução do programa, 1-parado; 2-em execução; 3-pausado"
    "robot_state","Estado de movimento do robô, 1-parado; 2-em movimento; 3-pausado; 4-arrasto"
    "main_code","Código de falha principal"
    "sub_code","Código de falha secundário"
    "robot_mode","Modo do robô, 0-modo automático; 1-modo manual"
    "jt_cur_pos[i]","Posições atuais das juntas, em graus, i:0~5"
    "tl_cur_pos[i]","Pose atual da ferramenta, em graus e mm, i:0~5"
    "flange_cur_pos[i]","Pose atual do flange da extremidade, em graus e mm, i:0~5"
    "actual_qd[i]","Velocidades atuais das juntas do robô, em graus/s, i:0~5"
    "actual_qdd[i]","Acelerações atuais das juntas do robô, em graus/s², i:0~5"
    "target_TCP_CmpSpeed[i]","Velocidade de comando sintética do TCP do robô, em mm/s e graus/s, i:0~1"
    "target_TCP_Speed[i]","Velocidade de comando do TCP do robô, em mm/s e graus/s, i:0~5"
    "actual_TCP_CmpSpeed[i]","Velocidade real sintética do TCP do robô, em mm/s e graus/s, i:0~1"
    "actual_TCP_Speed[i]","Velocidade real do TCP do robô, em mm/s e graus/s, i:0~5"
    "jt_cur_tor[i]","Torques atuais, em N·m, i:0~5"
    "tool","Número do sistema de coordenadas da ferramenta aplicado"
    "user","Número do sistema de coordenadas da peça aplicado"
    "cl_dgt_output_h","Saída digital da caixa de controle 15-8"
    "cl_dgt_output_l","Saída digital da caixa de controle 7-0"
    "tl_dgt_output_l","Saída digital da ferramenta 7-0, apenas bits 0-1 são válidos"
    "dgt_input_h","Entrada digital da caixa de controle 15-8"
    "cl_dgt_input_l","Entrada digital da caixa de controle 7-0"
    "tl_dgt_input_l","Entrada digital da ferramenta 7-0, apenas bits 0-1 são válidos"
    "cl_analog_input[i]","Entrada analógica da caixa de controle, i:0~2"
    "tl_anglog_input","Entrada analógica da ferramenta"
    "ft_sensor_raw_data","Dados brutos do sensor de torque, em N e Nm, i:0~5"
    "ft_sensor_data","Dados do sensor de torque, em N e Nm, i:0~5"
    "ft_sensor_active","Estado de ativação do sensor de torque, 0-reset, 1-ativado"
    "EmergencyStop","Sinalizador de parada de emergência, 0-parada de emergência não pressionada, 1-parada de emergência pressionada"
    "motion_done","Sinal de movimento concluído, 1-concluído, 0-não concluído"
    "gripper_motiondone","Sinal de movimento concluído da garra, 1-concluído, 0-não concluído"
    "mc_queue_len","Comprimento da fila de instruções de movimento"
    "collisionState","Detecção de colisão, 1-colisão, 0-sem colisão"
    "trajectory_pnum","Número do ponto de trajetória"
    "safety_stop0_state","Sinal de parada de segurança SI0"
    "safety_stop1_state","Sinal de parada de segurança SI1"
    "gripper_fault_id","Número da garra com falha"
    "gripper_fault","Falha da garra"
    "gripper_active","Estado de ativação da garra, 0-não ativada, 1-ativada"
    "gripper_position","Posição da garra (percentagem)"
    "gripper_speed","Velocidade da garra (percentagem)"
    "gripper_current","Corrente da garra (percentagem)"
    "gripper_tmp","Temperatura da garra, em °C"
    "gripper_voltage","Tensão da garra, em V"
    "auxState.servoId","Eixo estendido 485, número de ID do servo driver, i:0~3"
    "auxState.servoErrCode","Eixo estendido 485, código de falha do servo driver, i:0~3"
    "auxState.servoState","Eixo estendido 485, estado do servo driver, i:0~3"
    "auxState.servoPos","Eixo estendido 485, posição atual do servo, i:0~3"
    "auxState.servoVel","Eixo estendido 485, velocidade atual do servo, i:0~3"
    "auxState.servoTorque","Eixo estendido 485, torque atual do servo, i:0~3"
    "extAxisStatus[i].pos","Eixo estendido UDP, posição, i:0~3"
    "extAxisStatus[i].vel","Eixo estendido UDP, velocidade, i:0~3"
    "extAxisStatus[i].errorCode","Eixo estendido UDP, código de falha, i:0~3"
    "extAxisStatus[i].ready","Eixo estendido UDP, servo pronto, i:0~3"
    "extAxisStatus[i].inPos","Eixo estendido UDP, servo no lugar, i:0~3"
    "extAxisStatus[i].alarm","Eixo estendido UDP, alarme do servo, i:0~3"
    "extAxisStatus[i].flerr","Eixo estendido UDP, erro de seguimento, i:0~3"
    "extAxisStatus[i].nlimit","Eixo estendido UDP, limite negativo atingido, i:0~3"
    "extAxisStatus[i].pLimit","Eixo estendido UDP, limite positivo atingido, i:0~3"
    "extAxisStatus[i].mdbsOffLine","Eixo estendido UDP, driver offline no barramento 485"
    "extAxisStatus[i].mdbsTimeout","Eixo estendido UDP, tempo limite de comunicação 485 entre placa de controle e caixa de controle"
    "extAxisStatus[i].homingStatus","Eixo estendido UDP, estado de retorno à origem"
    "extDIState","Estado de entrada digital estendida"
    "extDOState","Estado de saída digital estendida"
    "extAIState","Estado de entrada analógica estendida"
    "extAOState","Estado de saída analógica estendida"
    "rbtEnableState","Estado de habilitação do robô"
    "jointDriverTorque","Torque atual do driver articular"
    "jointDriverTemperature","Temperatura atual do driver articular"
    "year","Ano"
    "mouth","Mês"
    "day","Dia"
    "hour","Hora"
    "minute","Minuto"
    "second","Segundo"
    "millisecond","Milissegundo"
    "softwareUpgradeState","Estado de atualização de software do robô"
    "endLuaErrCode","Estado de execução do LUA da extremidade"
    "cl_analog_output[i]","Saída analógica da caixa de controle, i:0~1"
    "tl_analog_output","Saída analógica da ferramenta"
    "gripperRotNum","Número atual de rotações da garra rotativa"
    "gripperRotSpeed","Percentagem da velocidade atual de rotação da garra rotativa"
    "gripperRotTorque","Percentagem do torque atual de rotação da garra rotativa"
    "weldingBreakOffState","Estado de interrupção da soldagem"
    "jt_tgt_tor","Torque de comando das juntas"
    "smartToolState","Estado do botão do SmartTool"
    "wideVoltageCtrlBoxTemp","Temperatura da caixa de controle de larga tensão"
    "wideVoltageCtrlBoxFanCurrent","Corrente da ventoinha da caixa de controle de larga tensão (mA)"
    "toolCoord[i]","Sistema de coordenadas da ferramenta, i:0~5"
    "wobjCoord[i]","Sistema de coordenadas da peça, i:0~5"
    "extoolCoord[i]","Sistema de coordenadas da ferramenta externa, i:0~5"
    "exAxisCoord[i]","Sistema de coordenadas do eixo estendido, i:0~5"
    "load","Massa da carga"
    "loadCog[i]","Centro de massa da carga, i:0~2"
    "lastServoTarget[i]","Última posição alvo do ServoJ na fila, i:0~5"
    "servoJCmdNum","Contagem de instruções ServoJ"

Estado do Controlador Servo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :header-rows: 1
    :name: Estado do controlador servo
    :widths: 20 30

    "Variável","Significado"
    "servoId","Número de ID do servo driver"
    "servoErrCode","Código de falha do servo driver"
    "servoState","Estado do servo driver"
    "servoPos","Posição atual do servo"
    "servoVel","Velocidade atual do servo"
    "servoTorque","Torque atual do servo"

Estado do Eixo Estendido
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :header-rows: 1
    :name: Estado do eixo estendido
    :widths: 20 30

    "Variável","Significado"
    "pos","Posição do eixo estendido"
    "vel","Velocidade do eixo estendido"
    "errorCode","Código de falha do eixo estendido"
    "ready","Servo pronto"
    "inPos","Servo no lugar"
    "alarm","Alarme do servo"
    "flerr","Erro de seguimento"
    "nlimit","Limite negativo atingido"
    "pLimit","Limite positivo atingido"
    "mdbsOffLine","Driver offline no barramento 485"
    "mdbsTimeout","Tempo limite de comunicação 485 entre placa de controle e caixa de controle"
    "homingStatus","Estado de retorno à origem do eixo estendido"

Estado de Interrupção da Soldagem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :header-rows: 1
    :name: Estado de interrupção da soldagem
    :widths: 20 30

    "Variável","Significado"
    "breakOffState","Estado de interrupção da soldagem"
    "weldArcState","Estado de interrupção do arco de soldagem"

Exemplo de Código
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    print("program_state:", robot.robot_state_pkg.program_state)
    print("robot_state:", robot.robot_state_pkg.robot_state)
    print("main_code:", robot.robot_state_pkg.main_code)
    print("sub_code:", robot.robot_state_pkg.sub_code)
    print("robot_mode:", robot.robot_state_pkg.robot_mode)
    print("jt_cur_pos0:", robot.robot_state_pkg.jt_cur_pos[0])
    print("jt_cur_pos1:", robot.robot_state_pkg.jt_cur_pos[1])
    print("jt_cur_pos2:", robot.robot_state_pkg.jt_cur_pos[2])
    print("jt_cur_pos3:", robot.robot_state_pkg.jt_cur_pos[3])
    print("jt_cur_pos4:", robot.robot_state_pkg.jt_cur_pos[4])
    print("jt_cur_pos5:", robot.robot_state_pkg.jt_cur_pos[5])
    print("tl_cur_pos0:", robot.robot_state_pkg.tl_cur_pos[0])
    print("tl_cur_pos1:", robot.robot_state_pkg.tl_cur_pos[1])
    print("tl_cur_pos2:", robot.robot_state_pkg.tl_cur_pos[2])
    print("tl_cur_pos3:", robot.robot_state_pkg.tl_cur_pos[3])
    print("tl_cur_pos4:", robot.robot_state_pkg.tl_cur_pos[4])
    print("tl_cur_pos5:", robot.robot_state_pkg.tl_cur_pos[5])
    print("flange_cur_pos0:", robot.robot_state_pkg.flange_cur_pos[0])
    print("flange_cur_pos1:", robot.robot_state_pkg.flange_cur_pos[1])
    print("flange_cur_pos2:", robot.robot_state_pkg.flange_cur_pos[2])
    print("flange_cur_pos3:", robot.robot_state_pkg.flange_cur_pos[3])
    print("flange_cur_pos4:", robot.robot_state_pkg.flange_cur_pos[4])
    print("flange_cur_pos5:", robot.robot_state_pkg.flange_cur_pos[5])
    print("actual_qd0:", robot.robot_state_pkg.actual_qd[0])
    print("actual_qd1:", robot.robot_state_pkg.actual_qd[1])
    print("actual_qd2:", robot.robot_state_pkg.actual_qd[2])
    print("actual_qd3:", robot.robot_state_pkg.actual_qd[3])
    print("actual_qd4:", robot.robot_state_pkg.actual_qd[4])
    print("actual_qd5:", robot.robot_state_pkg.actual_qd[5])
    print("actual_qdd0:", robot.robot_state_pkg.actual_qdd[0])
    print("actual_qdd1:", robot.robot_state_pkg.actual_qdd[1])
    print("actual_qdd2:", robot.robot_state_pkg.actual_qdd[2])
    print("actual_qdd3:", robot.robot_state_pkg.actual_qdd[3])
    print("actual_qdd4:", robot.robot_state_pkg.actual_qdd[4])
    print("actual_qdd5:", robot.robot_state_pkg.actual_qdd[5])
    print("target_TCP_CmpSpeed0:", robot.robot_state_pkg.target_TCP_CmpSpeed[0])
    print("target_TCP_CmpSpeed1:", robot.robot_state_pkg.target_TCP_CmpSpeed[1])
    print("target_TCP_Speed0:", robot.robot_state_pkg.target_TCP_Speed[0])
    print("target_TCP_Speed1:", robot.robot_state_pkg.target_TCP_Speed[1])
    print("target_TCP_Speed2:", robot.robot_state_pkg.target_TCP_Speed[2])
    print("target_TCP_Speed3:", robot.robot_state_pkg.target_TCP_Speed[3])
    print("target_TCP_Speed4:", robot.robot_state_pkg.target_TCP_Speed[4])
    print("target_TCP_Speed5:", robot.robot_state_pkg.target_TCP_Speed[5])
    print("actual_TCP_CmpSpeed0:", robot.robot_state_pkg.actual_TCP_CmpSpeed[0])
    print("actual_TCP_CmpSpeed1:", robot.robot_state_pkg.actual_TCP_CmpSpeed[1])
    print("actual_TCP_Speed0:", robot.robot_state_pkg.actual_TCP_Speed[0])
    print("actual_TCP_Speed1:", robot.robot_state_pkg.actual_TCP_Speed[1])
    print("actual_TCP_Speed2:", robot.robot_state_pkg.actual_TCP_Speed[2])
    print("actual_TCP_Speed3:", robot.robot_state_pkg.actual_TCP_Speed[3])
    print("actual_TCP_Speed4:", robot.robot_state_pkg.actual_TCP_Speed[4])
    print("actual_TCP_Speed5:", robot.robot_state_pkg.actual_TCP_Speed[5])
    print("jt_cur_tor0:", robot.robot_state_pkg.jt_cur_tor[0])
    print("jt_cur_tor1:", robot.robot_state_pkg.jt_cur_tor[1])
    print("jt_cur_tor2:", robot.robot_state_pkg.jt_cur_tor[2])
    print("jt_cur_tor3:", robot.robot_state_pkg.jt_cur_tor[3])
    print("jt_cur_tor4:", robot.robot_state_pkg.jt_cur_tor[4])
    print("jt_cur_tor5:", robot.robot_state_pkg.jt_cur_tor[5])
    print("tool:", robot.robot_state_pkg.tool)
    print("user:", robot.robot_state_pkg.user)
    print("cl_dgt_output_h:", robot.robot_state_pkg.cl_dgt_output_h)
    print("cl_dgt_output_l:", robot.robot_state_pkg.cl_dgt_output_l)
    print("tl_dgt_output_l:", robot.robot_state_pkg.tl_dgt_output_l)
    print("cl_dgt_input_h:", robot.robot_state_pkg.cl_dgt_input_h)
    print("cl_dgt_input_l:", robot.robot_state_pkg.cl_dgt_input_l)
    print("tl_dgt_input_l:", robot.robot_state_pkg.tl_dgt_input_l)
    print("cl_analog_input0:", robot.robot_state_pkg.cl_analog_input[0])
    print("cl_analog_input1:", robot.robot_state_pkg.cl_analog_input[1])
    print("tl_anglog_input:", robot.robot_state_pkg.tl_anglog_input)
    print("ft_sensor_raw_data0:", robot.robot_state_pkg.ft_sensor_raw_data[0])
    print("ft_sensor_raw_data1:", robot.robot_state_pkg.ft_sensor_raw_data[1])
    print("ft_sensor_raw_data2:", robot.robot_state_pkg.ft_sensor_raw_data[2])
    print("ft_sensor_raw_data3:", robot.robot_state_pkg.ft_sensor_raw_data[3])
    print("ft_sensor_raw_data4:", robot.robot_state_pkg.ft_sensor_raw_data[4])
    print("ft_sensor_raw_data5:", robot.robot_state_pkg.ft_sensor_raw_data[5])
    print("ft_sensor_data0:", robot.robot_state_pkg.ft_sensor_data[0])
    print("ft_sensor_data1:", robot.robot_state_pkg.ft_sensor_data[1])
    print("ft_sensor_data2:", robot.robot_state_pkg.ft_sensor_data[2])
    print("ft_sensor_data3:", robot.robot_state_pkg.ft_sensor_data[3])
    print("ft_sensor_data4:", robot.robot_state_pkg.ft_sensor_data[4])
    print("ft_sensor_data5:", robot.robot_state_pkg.ft_sensor_data[5])
    print("ft_sensor_active:", robot.robot_state_pkg.ft_sensor_active)
    print("EmergencyStop:", robot.robot_state_pkg.EmergencyStop)
    print("motion_done:", robot.robot_state_pkg.motion_done)
    print("gripper_motiondone:", robot.robot_state_pkg.gripper_motiondone)
    print("mc_queue_len:", robot.robot_state_pkg.mc_queue_len)
    print("collisionState:", robot.robot_state_pkg.collisionState)
    print("trajectory_pnum:", robot.robot_state_pkg.trajectory_pnum)
    print("safety_stop0_state:", robot.robot_state_pkg.safety_stop0_state)
    print("safety_stop1_state:", robot.robot_state_pkg.safety_stop1_state)
    print("gripper_fault_id:", robot.robot_state_pkg.gripper_fault_id)
    print("gripper_fault:", robot.robot_state_pkg.gripper_fault)
    print("gripper_active:", robot.robot_state_pkg.gripper_active)
    print("gripper_position:", robot.robot_state_pkg.gripper_position)
    print("gripper_speed:", robot.robot_state_pkg.gripper_speed)
    print("gripper_current:", robot.robot_state_pkg.gripper_current)
    print("gripper_tmp:", robot.robot_state_pkg.gripper_tmp)
    print("gripper_voltage:", robot.robot_state_pkg.gripper_voltage)
    print("auxState.servoId:", robot.robot_state_pkg.auxState.servoId)
    print("auxState.servoErrCode:", robot.robot_state_pkg.auxState.servoErrCode)
    print("auxState.servoState:", robot.robot_state_pkg.auxState.servoState)
    print("auxState.servoPos:", robot.robot_state_pkg.auxState.servoPos)
    print("auxState.servoVel:", robot.robot_state_pkg.auxState.servoVel)
    print("auxState.servoTorque:", robot.robot_state_pkg.auxState.servoTorque)
    for i in range(4):
        print("extAxisStatus.pos:", i, robot.robot_state_pkg.extAxisStatus[i].pos)
        print("extAxisStatus.vel:", i, robot.robot_state_pkg.extAxisStatus[i].vel)
        print("extAxisStatus.errorCode:", i, robot.robot_state_pkg.extAxisStatus[i].errorCode)
        print("extAxisStatus.ready:", i, robot.robot_state_pkg.extAxisStatus[i].ready)
        print("extAxisStatus.inPos:", i, robot.robot_state_pkg.extAxisStatus[i].inPos)
        print("extAxisStatus.alarm:", i, robot.robot_state_pkg.extAxisStatus[i].alarm)
        print("extAxisStatus.flerr:", i, robot.robot_state_pkg.extAxisStatus[i].flerr)
        print("extAxisStatus.nlimit:", i, robot.robot_state_pkg.extAxisStatus[i].nlimit)
        print("extAxisStatus.pLimit:", i, robot.robot_state_pkg.extAxisStatus[i].pLimit)
        print("extAxisStatus.mdbsOffLine:", i, robot.robot_state_pkg.extAxisStatus[i].mdbsOffLine)
        print("extAxisStatus.mdbsTimeout:", i, robot.robot_state_pkg.extAxisStatus[i].mdbsTimeout)
        print("extAxisStatus.homingStatus:", i, robot.robot_state_pkg.extAxisStatus[i].homingStatus)
    for i in range(8):
        print("extDIState:", i, robot.robot_state_pkg.extDIState[i])
        print("extDOState:", i, robot.robot_state_pkg.extDOState[i])
    for i in range(4):
        print("extAIState:", i, robot.robot_state_pkg.extAIState[i])
        print("extAOState:", robot.robot_state_pkg.extAOState[i])
    print("rbtEnableState:", robot.robot_state_pkg.rbtEnableState)
    print("jointDriverTorque0:", robot.robot_state_pkg.jointDriverTorque[0])
    print("jointDriverTorque1:", robot.robot_state_pkg.jointDriverTorque[1])
    print("jointDriverTorque2:", robot.robot_state_pkg.jointDriverTorque[2])
    print("jointDriverTorque3:", robot.robot_state_pkg.jointDriverTorque[3])
    print("jointDriverTorque4:", robot.robot_state_pkg.jointDriverTorque[4])
    print("jointDriverTorque5:", robot.robot_state_pkg.jointDriverTorque[5])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[0])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[1])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[2])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[3])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[4])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[5])
    print("year:", robot.robot_state_pkg.year)
    print("mouth:", robot.robot_state_pkg.mouth)
    print("day:", robot.robot_state_pkg.day)
    print("hour:", robot.robot_state_pkg.hour)
    print("minute:", robot.robot_state_pkg.minute)
    print("second:", robot.robot_state_pkg.second)
    print("millisecond:", robot.robot_state_pkg.millisecond)
    print("softwareUpgradeState:", robot.robot_state_pkg.softwareUpgradeState)
    print("endLuaErrCode:", robot.robot_state_pkg.endLuaErrCode)
    print("cl_analog_output[0]:", robot.robot_state_pkg.cl_analog_output[0])
    print("cl_analog_output[1]:", robot.robot_state_pkg.cl_analog_output[1])
    print("tl_analog_output:", robot.robot_state_pkg.tl_analog_output)
    print("gripperRotNum:", robot.robot_state_pkg.gripperRotNum)
    print("gripperRotSpeed:", robot.robot_state_pkg.gripperRotSpeed)
    print("gripperRotTorque:", robot.robot_state_pkg.gripperRotTorque)
    print("jt_tgt_tor:", robot.robot_state_pkg.jt_tgt_tor)
    print("smartToolState:", robot.robot_state_pkg.smartToolState)
    print("wideVoltageCtrlBoxTemp:", robot.robot_state_pkg.wideVoltageCtrlBoxTemp)
    print("wideVoltageCtrlBoxFanCurrent:", robot.robot_state_pkg.wideVoltageCtrlBoxFanCurrent)
    print("toolCoord0:", robot.robot_state_pkg.toolCoord[0])
    print("toolCoord1:", robot.robot_state_pkg.toolCoord[1])
    print("toolCoord2:", robot.robot_state_pkg.toolCoord[2])
    print("toolCoord3:", robot.robot_state_pkg.toolCoord[3])
    print("toolCoord4:", robot.robot_state_pkg.toolCoord[4])
    print("toolCoord5:", robot.robot_state_pkg.toolCoord[5])
    print("wobjCoord0:", robot.robot_state_pkg.wobjCoord[0])
    print("wobjCoord1:", robot.robot_state_pkg.wobjCoord[1])
    print("wobjCoord2:", robot.robot_state_pkg.wobjCoord[2])
    print("wobjCoord3:", robot.robot_state_pkg.wobjCoord[3])
    print("wobjCoord4:", robot.robot_state_pkg.wobjCoord[4])
    print("wobjCoord5:", robot.robot_state_pkg.wobjCoord[5])
    print("extoolCoord0:", robot.robot_state_pkg.extoolCoord[0])
    print("extoolCoord1:", robot.robot_state_pkg.extoolCoord[1])
    print("extoolCoord2:", robot.robot_state_pkg.extoolCoord[2])
    print("extoolCoord3:", robot.robot_state_pkg.extoolCoord[3])
    print("extoolCoord4:", robot.robot_state_pkg.extoolCoord[4])
    print("extoolCoord5:", robot.robot_state_pkg.extoolCoord[5])
    print("exAxisCoord0:", robot.robot_state_pkg.exAxisCoord[0])
    print("exAxisCoord1:", robot.robot_state_pkg.exAxisCoord[1])
    print("exAxisCoord2:", robot.robot_state_pkg.exAxisCoord[2])
    print("exAxisCoord3:", robot.robot_state_pkg.exAxisCoord[3])
    print("exAxisCoord4:", robot.robot_state_pkg.exAxisCoord[4])
    print("exAxisCoord5:", robot.robot_state_pkg.exAxisCoord[5])
    print("load:", robot.robot_state_pkg.load)
    print("loadCog0:", robot.robot_state_pkg.loadCog[0])
    print("loadCog1:", robot.robot_state_pkg.loadCog[1])
    print("loadCog2:", robot.robot_state_pkg.loadCog[2])
    print("lastServoTarget0:", robot.robot_state_pkg.lastServoTarget[0])
    print("lastServoTarget1:", robot.robot_state_pkg.lastServoTarget[1])
    print("lastServoTarget2:", robot.robot_state_pkg.lastServoTarget[2])
    print("lastServoTarget3:", robot.robot_state_pkg.lastServoTarget[3])
    print("lastServoTarget4:", robot.robot_state_pkg.lastServoTarget[4])
    print("lastServoTarget5:", robot.robot_state_pkg.lastServoTarget[5])
    print("servoJCmdNum:", robot.robot_state_pkg.servoJCmdNum)