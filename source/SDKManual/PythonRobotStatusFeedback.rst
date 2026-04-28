Descrição das Estruturas de Dados
============================================

.. toctree::
    :maxdepth: 5

Tipo de Estrutura de Feedback de Estado do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:
    
    class ROBOT_AUX_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("servoId", c_uint8),         # Número de ID do driver servo
            ("servoErrCode", c_int),     # Código de falha do driver servo
            ("servoState", c_int),       # Estado do driver servo
            ("servoPos", c_double),      # Posição atual do servo
            ("servoVel", c_float),       # Velocidade atual do servo
            ("servoTorque", c_float),    # Torque atual do servo
        ]

    class EXT_AXIS_STATUS(Structure):
        _pack_ = 1
        _fields_ = [
            ("pos", c_double),        # Posição do eixo de extensão
            ("vel", c_double),        # Velocidade do eixo de extensão
            ("errorCode", c_int),     # Código de falha do eixo de extensão
            ("ready", c_uint8),        # Servo pronto
            ("inPos", c_uint8),        # Servo na posição
            ("alarm", c_uint8),        # Alarme do servo
            ("flerr", c_uint8),        # Erro de seguimento
            ("nlimit", c_uint8),       # Limite negativo atingido
            ("pLimit", c_uint8),       # Limite positivo atingido
            ("mdbsOffLine", c_uint8),  # Barramento 485 do driver offline
            ("mdbsTimeout", c_uint8),  # Timeout de comunicação 485 entre placa de controle e caixa de controle
            ("homingStatus", c_uint8), # Status de homing do eixo de extensão
        ]

    class WELDING_BREAKOFF_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("breakOffState", c_uint8),        # Estado de interrupção da soldagem
            ("weldArcState", c_uint8),        # Estado de interrupção do arco de soldagem
        ]

    # ==================== Estrutura Completa de Estado do Robô ====================
    class RobotStatePkg(Structure):
        """
        Pacote de dados de feedback de estado do robô
        """
        _pack_ = 1
        _fields_ = [
            # Informações do cabeçalho do quadro
            ("frame_head", c_uint16),           # Cabeçalho do quadro, acordado como 0x5A5A
            ("frame_cnt", c_uint8),             # Contagem de quadros, contagem cíclica 0-255
            ("data_len", c_uint16),             # Comprimento do conteúdo dos dados
            ("program_state", c_uint8),         # Estado de execução do programa, 1-parado; 2-em execução; 3-pausado
            ("robot_state", c_uint8),             # Estado de movimento do robô, 1-parado; 2-em movimento; 3-pausado; 4-arrastando
            ("main_code", c_int),               # Código de falha principal
            ("sub_code", c_int),                # Código de falha secundário
            ("robot_mode", c_uint8),            # Modo do robô, 1-manual; 0-automático

            # Posições e velocidades das juntas
            ("jt_cur_pos", c_double * 6),       # Posições atuais das juntas de 6 eixos, unidade deg
            ("tl_cur_pos", c_double * 6),       # Posição atual da ferramenta [x,y,z,rx,ry,rz]
            ("flange_cur_pos", c_double * 6),   # Posição atual da flange final [x,y,z,rx,ry,rz]
            ("actual_qd", c_double * 6),        # Velocidades atuais de 6 juntas, unidade deg/s
            ("actual_qdd", c_double * 6),       # Acelerações atuais de 6 juntas, unidade deg/s^2
            ("target_TCP_CmpSpeed", c_double * 2),  # Velocidade de comando composta TCP [posição mm/s, orientação deg/s]
            ("target_TCP_Speed", c_double * 6), # Velocidade de comando TCP [x,y,z,rx,ry,rz]
            ("actual_TCP_CmpSpeed", c_double * 2),  # Velocidade efetiva composta TCP [posição mm/s, orientação deg/s]
            ("actual_TCP_Speed", c_double * 6), # Velocidade efetiva TCP [x,y,z,rx,ry,rz]
            ("jt_cur_tor", c_double * 6),       # Torques atuais de 6 eixos, unidade N·m

            # Sistemas de coordenadas da ferramenta e peça
            ("tool", c_int),                    # Número do sistema de coordenadas da ferramenta aplicado
            ("user", c_int),                    # Número do sistema de coordenadas da peça aplicado

            # I/O digital
            ("cl_dgt_output_h", c_uint8),       # Saída IO digital da caixa de controle 15-8
            ("cl_dgt_output_l", c_uint8),       # Saída IO digital da caixa de controle 7-0
            ("tl_dgt_output_l", c_uint8),       # Saída IO digital da ferramenta 7-0, apenas bit0-bit1 válidos
            ("cl_dgt_input_h", c_uint8),        # Entrada IO digital da caixa de controle 15-8
            ("cl_dgt_input_l", c_uint8),        # Entrada IO digital da caixa de controle 7-0
            ("tl_dgt_input_l", c_uint8),        # Entrada IO digital da ferramenta 7-0, apenas bit0-bit1 válidos

            # I/O analógico
            ("cl_analog_input", c_uint16 * 2),  # Entrada analógica da caixa de controle [0],[1]
            ("tl_anglog_input", c_uint16),      # Entrada analógica da ferramenta

            # Sensor de força/torque
            ("ft_sensor_raw_data", c_double * 6),   # Dados brutos do sensor de força/torque
            ("ft_sensor_data", c_double * 6),      # Dados do sensor de força/torque
            ("ft_sensor_active", c_uint8),          # Estado de ativação do sensor de força/torque

            # Sinais de estado
            ("EmergencyStop", c_uint8),         # Flag de parada de emergência, 0-não pressionada, 1-pressionada
            ("motion_done", c_int),             # Sinal de movimento concluído, 1-concluído, 0-não concluído
            ("gripper_motiondone", c_uint8),    # Sinal de movimento da garra concluído, 1-concluído, 0-não concluído
            ("mc_queue_len", c_int),            # Comprimento da fila de comandos de movimento
            ("collisionState", c_uint8),        # Detecção de colisão, 1-colisão, 0-sem colisão
            ("trajectory_pnum", c_int),         # Número do ponto de trajetória
            ("safety_stop0_state", c_uint8),    # Sinal de parada de segurança SI0
            ("safety_stop1_state", c_uint8),    # Sinal de parada de segurança SI1

            # Informações da garra
            ("gripper_fault_id", c_uint8),      # Número da garra com falha
            ("gripper_fault", c_uint16),        # Falha da garra
            ("gripper_active", c_uint16),      # Estado de ativação da garra
            ("gripper_position", c_uint8),      # Posição da garra
            ("gripper_speed", c_int8),          # Velocidade da garra
            ("gripper_current", c_int8),        # Corrente da garra
            ("gripper_temp", c_int),            # Temperatura da garra
            ("gripper_voltage", c_int),         # Tensão da garra

            # Estado dos eixos de extensão
            ("aux_axis_state", ROBOT_AUX_STATE * 25),    # Estado dos eixos de extensão 485 (25)
            ("extAxisStatus", EXT_AXIS_STATUS * 4), # Estado dos eixos de extensão UDP (4)

            # Estado de I/O estendido
            ("extDIState", c_uint16 * 8),       # Entrada DI estendida
            ("extDOState", c_uint16 * 8),       # Saída DO estendida
            ("extAIState", c_uint16 * 4),        # Entrada AI estendida
            ("extAOState", c_uint16 * 4),        # Saída AO estendida

            # Estado do robô e das juntas
            ("rbtEnableState", c_int),                  # Estado de habilitação do robô
            ("jointDriverTorque", c_double * 6),        # Torque do driver das juntas do robô
            ("jointDriverTemperature", c_double * 6),   # Temperatura do driver das juntas do robô

            # Tempo do robô
            #("robotTime", c_int * 7),             # Tempo do sistema do robô [ano,mês,dia,hora,minuto,segundo,milissegundo]
            ("year", ctypes.c_uint16),  # Ano
            ("mouth", ctypes.c_uint8),  # Mês
            ("day", ctypes.c_uint8),   # Dia
            ("hour", ctypes.c_uint8),   # Hora
            ("minute", ctypes.c_uint8), # Minuto
            ("second", ctypes.c_uint8), # Segundo
            ("millisecond", ctypes.c_uint16), # Milissegundo

            ("softwareUpgradeState", c_int),      # Estado de atualização do software do robô
            ("endLuaErrCode", c_uint16),          # Estado de execução Lua da extremidade

            # Saída analógica
            ("cl_analog_output", c_uint16 * 2), # Saída analógica da caixa de controle [0],[1]
            ("tl_analog_output", c_uint16),       # Saída analógica da ferramenta

            # Garra rotativa
            ("gripperRotNum", c_float),         # Número de rotações atual da garra rotativa
            ("gripperRotSpeed", c_uint8),       # Porcentagem de velocidade de rotação atual da garra rotativa
            ("gripperRotTorque", c_uint8),      # Porcentagem de torque de rotação atual da garra rotativa

            # Estado de interrupção da soldagem - usando estrutura
            ("weldingBreakOffState", WELDING_BREAKOFF_STATE),  # Estado de interrupção da soldagem

            # Torque da junta alvo
            ("jt_tgt_tor", c_double * 6),       # Torque de comando da junta

            ("smartToolState", c_int),          # Estado do botão da manopla SmartTool
            ("wideVoltageCtrlBoxTemp", c_float),        # Temperatura da caixa de controle de ampla tensão
            ("wideVoltageCtrlBoxFanCurrent", c_uint16), # Corrente do ventilador da caixa de controle de ampla tensão (mA)

            # Valores do sistema de coordenadas
            ("toolCoord", c_double * 6),        # Valores atuais do sistema de coordenadas da ferramenta; x,y,z,rx,ry,rz
            ("wobjCoord", c_double * 6),        # Valores atuais do sistema de coordenadas da peça; x,y,z,rx,ry,rz
            ("extoolCoord", c_double * 6),      # Valores atuais do sistema de coordenadas da ferramenta externa; x,y,z,rx,ry,rz
            ("exAxisCoord", c_double * 6),      # Valores atuais do sistema de coordenadas dos eixos de extensão; x,y,z,rx,ry,rz

            # Carga
            ("load", c_double),                 # Massa da carga
            ("loadCog", c_double * 3),            # Centro de gravidade da carga

            # Comandos servo
            ("lastServoTarget", c_double * 6),  # Última posição alvo ServoJ na fila
            ("servoJCmdNum", c_int),            # Contagem de comandos ServoJ

            # Dados da junta alvo
            ("targetJointPos", c_double * 6),   # Posição de comando de 6 juntas, unidade °
            ("targetJointVel", c_double * 6),   # Velocidade de comando de 6 juntas, unidade °/s
            ("targetJointAcc", c_double * 6),   # Aceleração de comando de 6 juntas, unidade °/s2
            ("targetJointCurrent", c_double * 6), # Corrente de comando de 6 juntas, unidade A
            ("actualJointCurrent", c_double * 6), # Corrente atual de 6 juntas, unidade A
            ("actualTCPForce", c_double * 6),   # Torque do end-effector do robô Nm; x,y,z,rx,ry,rz
            ("targetTCPPos", c_double * 6),     # Posição de comando TCP do robô mm; x,y,z,rx,ry,rz

            ("collisionLevel", c_uint8 * 6),    # Nível de colisão do robô
            ("speedScaleManual", c_double),     # Porcentagem de velocidade global no modo manual
            ("speedScaleAuto", c_double),       # Porcentagem de velocidade global no modo automático
            ("luaLineNum", c_int),              # Número da linha atual do programa Lua em execução
            ("abnomalStop", c_uint8),           # 0-sem anormalidade; 1-anormalidade presente
            ("currentLuaFileName", c_uint8 * 256),  # Nome do programa Lua atualmente em execução
            ("programTotalLine", c_uint8),      # Número total de linhas do programa Lua
            ("safetyBoxSingal", c_uint8 * 6),   # Estado dos botões da caixa de botões do robô

            # Dados de soldagem
            ("weldVoltage", c_double),          # Tensão de soldagem V
            ("weldCurrent", c_double),          # Corrente de soldagem
            ("weldTrackVel", c_double),         # Velocidade de rastreamento da junta de solda mm/s

            ("tpdException", c_uint8),            # Contagem de carregamento de trajetória TPD excedida, 0-não excedida, 1-excedida
            ("alarmRebootRobot", c_uint8),      # Aviso, 1-solte o botão de parada de emergência e reinicie a caixa de controle, 2-anomalia de comunicação da junta, reinicie a caixa de controle
            ("modbusMasterConnect", c_uint8),   # bit0-7 correspondem ao estado de conexão dos mestres ModbusTCP 0-7
            ("modbusSlaveConnect", c_uint8),    # Estado de conexão escrava ModbusTCP
            ("btnBoxStopSignal", c_uint8),      # Sinal de parada de emergência da caixa de botões
            ("dragAlarm", c_uint8),             # Aviso de arrasto
            ("safetyDoorAlarm", c_uint8),       # Aviso de porta de segurança
            ("safetyPlaneAlarm", c_uint8),      # Aviso de entrada na parede de segurança
            ("motonAlarm", c_uint8),            # Aviso de movimento
            ("interfaceAlarm", c_uint8),        # Aviso de entrada na área de interferência
            ("udpCmdState", c_int),             # Estado de conexão de comunicação UDP da porta 20007
            ("weldReadyState", c_uint8),        # Estado de prontidão da máquina de solda
            ("alarmCheckEmergStopBtn", c_uint8),    # 0-normal; 1-anomalia de comunicação, verifique se o botão de parada de emergência está liberado
            ("tsTmCmdComError", c_uint8),       # 0-normal; 1-falha de comunicação do comando de torque
            ("tsTmStateComError", c_uint8),     # 0-normal; 1-falha de comunicação do estado de torque
            ("ctrlBoxError", c_int),            # Erro da caixa de controle
            ("safetyDataState", c_uint8),       # Flag de estado dos dados de segurança
            ("forceSensorErrState", c_uint8),   # Falha de tempo limite de conexão do sensor de força
            ("ctrlOpenLuaErrCode", c_uint8 * 4),  # 4 códigos de erro do protocolo aberto do controlador periférico
            ("strangePosFlag", c_uint8),        # Flag de postura singular atual
            ("alarm", c_uint8),                 # Aviso
            ("driverAlarm", c_uint8),           # Número do eixo com alarme do driver
            ("aliveSlaveNumError", c_uint8),    # Erro de contagem de escravos ativos
            ("slaveComError", c_uint8 * 8),     # Estado de erro do escravo
            ("cmdPointError", c_uint8),         # Erro de ponto de comando
            ("IOError", c_uint8),               # Erro de IO
            ("gripperError", c_uint8),          # Erro da garra
            ("fileError", c_uint8),             # Erro de arquivo
            ("paraError", c_uint8),             # Erro de parâmetro
            ("exaxisOutLimitError", c_uint8),   # Erro de limite suave do eixo externo excedido
            ("driverComError", c_uint8 * 6),    # Falha de comunicação do driver
            ("driverError", c_uint8),           # Número do eixo com falha de comunicação do driver
            ("outSoftLimitError", c_uint8),     # Falha de limite suave excedido
            ("axleGenComData", c_uint8 * 130),   # Dados de comunicação geral de eixos não periódicos
            ("socketConnTimeout", c_uint8),     # Timeout de conexão do socket
            ("socketReadTimeout", c_uint8),     # Timeout de leitura do socket
            ("tsWebStateComErr", c_uint8),      # Erro de comunicação de estado TS_WEB
            ("check_sum", c_uint16)          # Checksum
        ]

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

Tipo de Enumeração da Lista de Configuração de Feedback de Estado do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    # ==================== Enumeracao da Lista de Configuração RobotState ====================
    class RobotState(enum.Enum):
        """Enumeracao do tipo de estado CNDE"""
        FrameHead = 0
        FrameCnt = 1
        DataLen = 2
        ProgramState = 3
        RobotState = 4
        MainCode = 5
        SubCode = 6
        RobotMode = 7
        JointCurPos = 8
        ToolCurPos = 9
        FlangeCurPos = 10
        ActualJointVel = 11
        ActualJointAcc = 12
        TargetTCPCmpSpeed = 13
        TargetTCPSpeed = 14
        ActualTCPCmpSpeed = 15
        ActualTCPSpeed = 16
        ActualJointTorque = 17
        Tool = 18
        User = 19
        ClDgtOutputH = 20
        ClDgtOutputL = 21
        TlDgtOutputL = 22
        ClDgtInputH = 23
        ClDgtInputL = 24
        TlDgtInputL = 25
        ClAnalogInput = 26
        TlAnglogInput = 27
        FtSensorRawData = 28
        FtSensorData = 29
        FtSensorActive = 30
        EmergencyStop = 31
        MotionDone = 32
        GripperMotiondone = 33
        McQueueLen = 34
        CollisionState = 35
        TrajectoryPnum = 36
        SafetyStop0State = 37
        SafetyStop1State = 38
        GripperFaultId = 39
        GripperFault = 40
        GripperActive = 41
        GripperPosition = 42
        GripperSpeed = 43
        GripperCurrent = 44
        GripperTemp = 45
        GripperVoltage = 46
        AuxState = 47
        ExtAxisStatus = 48
        ExtDIState = 49
        ExtDOState = 50
        ExtAIState = 51
        ExtAOState = 52
        RbtEnableState = 53
        JointDriverTorque = 54
        JointDriverTemperature = 55
        RobotTime = 56
        SoftwareUpgradeState = 57
        EndLuaErrCode = 58
        ClAnalogOutput = 59
        TlAnalogOutput = 60
        GripperRotNum = 61
        GripperRotSpeed = 62
        GripperRotTorque = 63
        WeldingBreakOffState = 64
        TargetJointTorque = 65
        SmartToolState = 66
        WideVoltageCtrlBoxTemp = 67
        WideVoltageCtrlBoxFanCurrent = 68
        ToolCoord = 69
        WobjCoord = 70
        ExtoolCoord = 71
        ExAxisCoord = 72
        Load = 73
        LoadCog = 74
        LastServoTarget = 75
        ServoJCmdNum = 76
        TargetJointPos = 77
        TargetJointVel = 78
        TargetJointAcc = 79
        TargetJointCurrent = 80
        ActualJointCurrent = 81
        ActualTCPForce = 82
        TargetTCPPos = 83
        CollisionLevel = 84
        SpeedScaleManual = 85
        SpeedScaleAuto = 86
        LuaLineNum = 87
        AbnomalStop = 88
        CurrentLuaFileName = 89
        ProgramTotalLine = 90
        SafetyBoxSingal = 91
        WeldVoltage = 92
        WeldCurrent = 93
        WeldTrackVel = 94
        TpdException = 95
        AlarmRebootRobot = 96
        ModbusMasterConnect = 97
        ModbusSlaveConnect = 98
        BtnBoxStopSignal = 99
        DragAlarm = 100
        SafetyDoorAlarm = 101
        SafetyPlaneAlarm = 102
        MotonAlarm = 103
        InterfaceAlarm = 104
        UdpCmdState = 105
        WeldReadyState = 106
        AlarmCheckEmergStopBtn = 107
        TsTmCmdComError = 108
        TsTmStateComError = 109
        CtrlBoxError = 110
        SafetyDataState = 111
        ForceSensorErrState = 112
        CtrlOpenLuaErrCode = 113
        StrangePosFlag = 114
        Alarm = 115
        DriverAlarm = 116
        AliveSlaveNumError = 117
        SlaveComError = 118
        CmdPointError = 119
        IOError = 120
        GripperError = 121
        FileError = 122
        ParaError = 123
        ExaxisOutLimitError = 124
        DriverComError = 125
        DriverError = 126
        OutSoftLimitError = 127
        AxleGenComData = 128
        SocketConnTimeout = 129
        SocketReadTimeout = 130
        TsWebStateComErr = 131
        CheckSum = 132