Introdução ao CNDE
=============================

O Protocolo de Troca de Dados Configurável em Rede (doravante denominado CNDE) para robôs colaborativos é uma forma pela qual o cliente controla o robô e obtém o feedback de estado do robô através da comunicação UDP.

A Tabela 1-1 é o conjunto de todos os estados do robô que podem ser obtidos pelo CNDE. O cliente pode selecionar arbitrariamente vários estados necessários da tabela e fazer com que o robô forneça o feedback de estado de acordo com um período de feedback definido.

Da mesma forma, o cliente pode selecionar as combinações de funções de controle do robô necessárias na Tabela 1-2 para realizar operações de controle do robô. Os dados de comunicação entre o cliente e o CNDE do robô devem seguir o formato de quadro especificado. As portas de comunicação CNDE do robô são 20005 e 20006. A porta 20005 é usada para comunicação TCP e a porta 20006 é usada para comunicação UDP.

O uso da função CNDE do robô envolve principalmente os seguintes quatro passos:

① Configuração do conteúdo dos dados de entrada e saída: O cliente envia uma instrução de configuração de entrada ou saída para o robô, onde o conteúdo da instrução é uma série de nomes de funções de controle ou estado, como "std_DI_box, cfg_DI_box, motion_queue_len". Após o robô registrar e identificar esses nomes, ele retorna ao cliente os tipos de dados das funções correspondentes, como "UINT8, UINT8, INT32", indicando que a configuração foi bem-sucedida.

② Iniciar a saída de dados CNDE do robô: O cliente envia uma instrução para iniciar a saída de dados CNDE para o robô. O robô então começa a enviar os dados de estado do robô para o cliente via UDP na forma de um array de bytes (modo little-endian), de acordo com o período configurado.

③ Analisar os dados de estado do robô: O cliente recebe os dados de estado de feedback do robô em um loop e analisa os dados com base nos tipos de dados retornados pelo robô durante a configuração de saída e no comprimento de bytes correspondente a cada tipo de dados na Tabela 1-3, obtendo assim os valores reais de cada estado. Os dados de saída CNDE do robô suportam no máximo 4096 bytes, e o período de saída CNDE pode ser configurado entre 1 e 200 ms.

④ Enviar dados de controle do robô: O cliente monta o pacote de dados de controle com base nos tipos de dados retornados pelo robô durante a configuração de entrada e no comprimento de bytes correspondente a cada tipo de dados na Tabela 1-3, e envia via comunicação UDP para o robô. Após receber os dados de controle, o robô analisa os dados e executa as operações de controle. A entrada CNDE do robô suporta 256 receitas. O cliente pode configurar várias receitas de entrada conforme a necessidade e, ao enviar dados de entrada para o robô, deve especificar o número da receita correspondente aos dados atuais.

.. centered:: Tabela 1-1 Funções de Configuração de Saída do Robô

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Tipo de Dado**
     - **Descrição**

   * - std_DI_box
     - UINT8
     - Entrada DI padrão do painel de controle (bit0 ~ bit7 representam DI0 ~ DI7)

   * - cfg_DI_box
     - UINT8
     - Entrada CI configurável do painel de controle (bit0 ~ bit7 representam CI0 ~ CI7)

   * - cfg_DI_tool
     - UINT8
     - Entrada DI da ferramenta configurável do painel de controle (bit0 ~ bit2 representam toolDI0 ~ toolDI1)

   * - std_AI0_box
     - DOUBLE
     - Entrada analógica AI0 do painel de controle (0 ~ 4095)

   * - std_AI1_box
     - DOUBLE
     - Entrada analógica AI1 do painel de controle (0 ~ 4095)

   * - std_AI_tool
     - DOUBLE
     - Entrada analógica tool_AI0 da ferramenta de extremidade (0 ~ 4095)

   * - run_up_time
     - DOUBLE
     - Tempo de funcionamento do robô desde a inicialização (s)

   * - target_joint_pos
     - DOUBLE_6
     - Posição alvo das juntas 1-6 (°)

   * - target_joint_vel
     - DOUBLE_6
     - Velocidade alvo das juntas 1-6 (°/s)

   * - target_joint_acc
     - DOUBLE_6
     - Aceleração alvo das juntas 1-6 (°/s²)

   * - target_joint_current
     - DOUBLE_6
     - Corrente alvo das juntas 1-6 (A)

   * - target_joint_torque
     - DOUBLE_6
     - Torque alvo das juntas 1-6 (Nm)

   * - actual_joint_pos
     - DOUBLE_6
     - Posição atual das juntas 1-6 (°)

   * - actual_joint_vel
     - DOUBLE_6
     - Velocidade atual das juntas 1-6 (°/s)

   * - actual_joint_current
     - DOUBLE_6
     - Corrente atual das juntas 1-6 (A)

   * - actual_joint_torque
     - DOUBLE_6
     - Torque alvo das juntas 1-6 (Nm)

   * - actual_TCP_pos
     - DOUBLE_6
     - Posição atual da ferramenta DKR (mm)

   * - actual_TCP_vel
     - DOUBLE_6
     - Velocidade atual da ferramenta DKR (mm/s)

   * - actual_TCP_force
     - DOUBLE_6
     - Força resultante na ferramenta DKR (N)

   * - target_TCP_pos
     - DOUBLE_6
     - Posição alvo da ferramenta DKR (mm)

   * - target_TCP_vel
     - DOUBLE_6
     - Velocidade alvo da ferramenta DKR (mm/s)

   * - std_DO_box
     - UINT8
     - Saída DO padrão do painel de controle (bit0 ~ bit7 representam DO0 ~ DO7)

   * - cfg_DO_box
     - UINT8
     - Saída CO configurável do painel de controle (bit0 ~ bit7 representam CO0 ~ CO7)

   * - cfg_DO_tool
     - UINT8
     - Saída DO da ferramenta padrão do painel de controle (bit0 ~ bit1 representam toolDO0 ~ toolDO1)

   * - std_AO0_box
     - DOUBLE
     - Saída analógica AO0 do painel de controle (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - Saída analógica AO1 do painel de controle (0.0 ~ 4095.0)

   * - std_AO_tool
     - DOUBLE
     - Saída analógica AO1 da ferramenta (0.0 ~ 4095.0)

   * - robot_mode
     - UINT8
     - Modo do robô (0-automático; 1-manual)

   * - collision_level
     - UINT8_6
     - Nível de colisão das juntas 1-6 (1 ~ 10)

   * - speed_scaling_man
     - DOUBLE
     - Porcentagem de velocidade no modo manual (0 ~ 100)

   * - speed_scaling_auto
     - DOUBLE
     - Porcentagem de velocidade no modo automático (0 ~ 100)

   * - program_state
     - UINT8
     - Estado de execução do programa do robô (1-parado; 2-em movimento; 3-pausado; 4-arrastando)

   * - line_number
     - INT32
     - Número da linha do programa em execução

   * - payload
     - DOUBLE
     - Massa da carga (kg)

   * - pay_cog
     - DOUBLE_3
     - Centro de gravidade da carga (x, y, z) (mm)

   * - motion_queue_len
     - INT32
     - Comprimento atual da fila de movimento
   
   * - ft_sensor_data
     - DOUBLE_6
     - Dados brutos do sensor de força

   * - main_code
     - INT32
     - Código de falha principal

   * - sub_code
     - INT32
     - Código de falha secundário

   * - emergency_stop
     - UINT8
     - Estado de parada de emergência

   * - motion_done
     - INT32
     - Estado de conclusão do movimento

   * - timestamp_us
     - UINT64
     - Tempo do sistema do robô (us)

   * - output_BIT_reg_8xX
     - UINT8_X
     - Registradores de saída do robô tipo BIT (8xX indica o número de registradores. Se você precisar de 16 registradores de saída tipo BIT, o nome real será: "output_BIT_reg_8x2". O robô suporta no máximo 128 registradores de saída tipo BIT)

   * - output_INT_reg_X
     - INT32_X
     - Registradores de saída do robô tipo INT (X indica o número de registradores. Se você precisar de 16 registradores de saída tipo INT, o nome real será: "output_INT_reg_16". O robô suporta no máximo 64 registradores de saída tipo INT)

   * - output_DOUBLE_reg_X
     - DOUBLE_X
     - Registradores de saída do robô tipo DOUBLE (X indica o número de registradores. Se você precisar de 16 registradores de saída tipo DOUBLE, o nome real será: "output_DOUBLE_reg_16". O robô suporta no máximo 64 registradores de saída tipo DOUBLE)

   * - servoj_time
     - UINT64_5
     - Dados de timestamp servoj, unidade ns

   * - actual_joint_temp
     - DOUBLE_6
     - Temperatura do driver das juntas j1-j6, unidade °

   * - axle_gen_com_data
     - UINT8_130
     - Dados periódicos gerais do end-effector

   * - abnormal_stop
     - UINT8
     - Status anormal, 0: sem anormalidade, 1: com anormalidade

   * - cur_lua_file_name
     - UINT8_256
     - Nome do arquivo Lua atualmente em execução

   * - prog_total_line
     - UINT8
     - Número total de linhas no arquivo atual

   * - safety_box_signal
     - UINT8_6
     - Sinal do botão da caixa de botões 0: pressionado 1: liberado

   * - welding_voltage
     - DOUBLE
     - Tensão de soldagem real, unidade V

   * - welding_current
     - DOUBLE
     - Corrente de soldagem real, unidade A

   * - welding_track_speed
     - DOUBLE
     - Velocidade de rastreamento da junta de solda mm/s

   * - tpd_exception
     - UINT8
     - Exceção TPD

   * - alarm_reboot_robot
     - UINT8
     - Aviso de reinicialização do robô

   * - modbus_master_connect
     - UINT8
     - | Status de conexão de 8 mestres Modbus  
       | bit0-bit7 representam os mestres 0-7, 0-não conectado, 1-conectado

   * - modbus_slave_connect
     - UINT8
     - Status de conexão do escravo Modbus, 0-não conectado, 1-conectado

   * - btn_box_stop_signal
     - UINT8
     - Sinal do botão de parada de emergência

   * - drag_alarm
     - UINT8
     - Aviso de arrasto

   * - safety_door_alarm
     - UINT8
     - Aviso de porta de segurança, 0 sem aviso, 1 porta de segurança acionada

   * - safety_plane_alarm
     - UINT8
     - Aviso de parede de segurança, 0 sem aviso, 1 entrada na parede de segurança

   * - motion_alarm
     - UINT8
     - | Aviso de movimento, 0-sem aviso,
       | 1-Mudança de postura da instrução LIN muito grande,
       | 2-Excesso de velocidade TCP,
       | 3-Colisão ocorrida,
       | 4-Eixo 1 excedeu velocidade máxima,
       | 5-Eixo 2 excedeu velocidade máxima,
       | 6-Eixo 3 excedeu velocidade máxima,
       | 7-Eixo 4 excedeu velocidade máxima,
       | 8-Eixo 5 excedeu velocidade máxima,
       | 9-Eixo 6 excedeu velocidade máxima,
       | 10-Eixo 1 desvio entre comando da junta e feedback muito grande,
       | 11-Eixo 2 desvio entre comando da junta e feedback muito grande,
       | 12-Eixo 3 desvio entre comando da junta e feedback muito grande,
       | 13-Eixo 4 desvio entre comando da junta e feedback muito grande,
       | 14-Eixo 5 desvio entre comando da junta e feedback muito grande,
       | 15-Eixo 6 desvio entre comando da junta e feedback muito grande,
       | 16-Postura singular,
       | 17-Velocidade de movimento da instrução LIN adaptativa,
       | 18-Ajuste de velocidade alvo tempo limite ou não concluído,
       | 19-Movimento de inserção rotativa falhou,
       | 20-Movimento de inserção helicoidal falhou,
       | 21-Movimento de inserção linear falhou,
       | 22-Movimento de posicionamento de superfície falhou

   * - interfere_alarm
     - UINT8
     - Aviso de área de interferência, 0 sem aviso, 1 entrada na área de interferência

   * - udp_cmd_state
     - INT32
     - Status da conexão UDP

   * - weld_ready_state
     - UINT8
     - Status de prontidão da máquina de solda, 1: pronto, 0: erro na máquina de solda

   * - alarm_check_emerg_stop_btn
     - UINT8
     - Aviso de anormalidade de comunicação da junta

   * - ts_tm_cmd_com_error
     - UINT8
     - Erro de comando do sistema de torque

   * - ts_tm_state_com_error
     - UINT8
     - Erro de estado do sistema de torque

   * - ctrl_box_error
     - INT32
     - Erro da caixa de controle

   * - safety_data_state
     - UINT8
     - Flag de status de dados de segurança, 0 sem anormalidade, 1-anormalidade

   * - force_sensor_err_state
     - UINT8
     - Falha de tempo limite de conexão do sensor de força; bit0-bit1 correspondem aos sensores de força ID1-ID2

   * - ctrl_open_lua_errcode
     - UINT8_4
     - Código de erro do protocolo aberto do controlador

   * - servo_id
     - UINT8
     - Número de ID do driver servo

   * - servo_errcode
     - INT32
     - Código de falha do driver servo

   * - servo_state
     - INT32
     - Status do driver servo

   * - servo_actual_pos
     - DOUBLE
     - Posição atual do servo

   * - servo_actual_speed
     - DOUBLE
     - Velocidade atual do servo
   
   * - servo_actual_torque
     - DOUBLE
     - Torque atual do servo
   
   * - gripper_active
     - INT32
     - Status de ativação da garra
   
   * - gripper_position
     - UINT8
     - Feedback de posição da garra (percentagem)
   
   * - gripper_speed
     - INT32
     - Feedback de velocidade da garra (percentagem)
   
   * - gripper_current
     - INT32
     - Feedback de corrente da garra (percentagem)
   
   * - gripper_temp
     - INT32
     - Temperatura atual da garra, unidade °
   
   * - gripper_voltage
     - INT32
     - Tensão atual da garra, unidade V
   
   * - rotating_gripper_num
     - DOUBLE
     - Feedback do número de rotações da garra rotativa
   
   * - rotating_gripper_speed
     - UINT8
     - Feedback da velocidade de rotação da garra rotativa (percentagem)
   
   * - rotating_gripper_tor
     - UINT8
     - Feedback do torque de rotação da garra rotativa (percentagem)
   
   * - weld_break_off_state
     - UINT8
     - Status de interrupção da soldagem: 0-soldagem não interrompida, 1-soldagem interrompida
   
   * - weld_arc_state
     - UINT8
     - Status do arco de soldagem, 0-arco não interrompido, 1-arco interrompido
   
   * - smarttool_state
     - UINT32
     - Dados de IO estendidos do end-effector (Smart-Tool)
   
   * - tool_coord
     - DOUBLE_6
     - Pose atual da ferramenta em relação ao end-effector
   
   * - wobj_coord
     - DOUBLE_6
     - Pose atual da peça de trabalho em relação à base
   
   * - exTool_coord
     - DOUBLE_6
     - Pose atual da ferramenta externa em relação à ferramenta
   
   * - exAxis_coord
     - DOUBLE_6
     - Pose atual do eixo externo em relação ao sistema de coordenadas da base
   
   * - robot_state
     - UINT8
     - | Status de operação do robô,
       | 1. Parado; 2. Em movimento; 3. Pausado; 4. Arrastando
   
   * - actual_flange_pos
     - DOUBLE_6
     - Pose real do end-effector
   
   * - target_TCP_cmpvel
     - DOUBLE_2
     - Velocidade linear e angular do comando TCP, unidade mm/s, °/s
   
   * - actual_TCP_cmpvel
     - DOUBLE_2
     - Velocidade linear e angular real do TCP, unidade mm/s, °/s
   
   * - tool_id
     - INT32
     - Número da ferramenta
   
   * - wobj_id
     - INT32
     - Número da peça de trabalho
   
   * - ft_sensor_raw_data
     - DOUBLE_6
     - Dados brutos de força/torque do end-effector no sistema de coordenadas do sensor
   
   * - ft_sensor_active
     - UINT8
     - Status de ativação do sensor de força/torque
   
   * - gripper_motion_done
     - UINT8
     - Movimento da garra concluído
   
   * - collision_state
     - UINT8
     - Status de detecção de colisão
   
   * - trajectory_pnum
     - INT32
     - Número de sequência atual do movimento de pontos discretos
   
   * - safety_stop0_state
     - UINT8
     - Status do sinal de parada de segurança SI0
   
   * - safety_stop1_state
     - UINT8
     - Status do sinal de parada de segurança SI1
   
   * - gripper_fault_id
     - UINT8
     - Número da garra com falha
   
   * - gripper_fault
     - INT32
     - Número do erro da garra
   
   * - ext_DI_state
     - UINT8_16
     - DI estendidos
   
   * - ext_DO_state
     - UINT8_16
     - DO estendidos
   
   * - ext_AI_state
     - INT32_4
     - AI estendidos
   
   * - ext_AO_state
     - INT32_4
     - AO estendidos
   
   * - rbt_enable_state
     - INT32
     - Status de conclusão da habilitação do driver
   
   * - joint_driver_torque
     - DOUBLE_6
     - Valores de torque reais das juntas j1-j6, unidade Nm
   
   * - robot_time
     - INT32_7
     - Tempo do sistema do robô, ano, mês, dia, hora, minuto, segundo, milissegundo
   
   * - software_upgrade_state
     - INT32
     - Status de atualização do software do robô
   
   * - end_lua_err_code
     - INT32
     - Status do sinal do botão do end-effector
   
   * - wide_voltage_ctrl_box_temp
     - DOUBLE
     - Temperatura da caixa de controle de ampla tensão, unidade °
   
   * - wide_voltage_ctrl_box_fan_current
     - INT32
     - Corrente do ventilador da caixa de controle de ampla tensão
   
   * - last_servoJ_target
     - DOUBLE_6
     - Última pose de comando alvo servoJ
   
   * - servoJ_cmd_num
     - INT32
     - Contagem de comandos servoJ
   
   * - strange_pos_flag
     - UINT8
     - Flag de postura singular
   
   * - alarm
     - UINT8
     - | Aviso, 0-sem aviso,
       | 1-Mudança de configuração da junta do ombro,
       | 2-Mudança de configuração da junta do cotovelo,
       | 3-Mudança de configuração da junta do punho,
       | 4-Inicialização RPY falhou,
       | 5-Timeout de espera WaitDI,
       | 6-Timeout de espera WaitAI,
       | 7-Timeout de espera WaitToolDI,
       | 8-Timeout de espera WaitToolAI,
       | 9-DI de sucesso de início de arco não configurado,
       | 10-Timeout de espera WaitAuxDI,
       | 11-Timeout de espera WaitAuxAI,
       | 12-Ponto inalcançável na trajetória de oscilação,
       | 13-Cálculo do ponto de coleta de rastreamento da esteira falhou,
       | 14-Anomalia de dados do sensor de torque da junta
   
   * - dr_alarm
     - UINT8
     - | Aviso do driver, 0-sem aviso,
       | 1-Aviso do driver do eixo 1, reiniciável,
       | 2-Aviso do driver do eixo 2, reiniciável,
       | 3-Aviso do driver do eixo 3, reiniciável,
       | 4-Aviso do driver do eixo 4, reiniciável,
       | 5-Aviso do driver do eixo 5, reiniciável,
       | 6-Aviso do driver do eixo 6, reiniciável
   
   * - alive_slave_num_error
     - UINT8
     - Falha na contagem de escravos ativos, 0-sem falha, 1-erro, não reiniciável
   
   * - slave_com_error
     - UINT8_8
     - | Falha de comunicação do escravo, 0-sem falha,
       | 1-Escravo offline,
       | 2-Estado do escravo inconsistente com o valor definido,
       | 3-Escravo não configurado,
       | 4-Erro de configuração do escravo,
       | 5-Erro de inicialização do escravo,
       | 6-Erro de inicialização da comunicação da caixa de correio do escravo
   
   * - cmd_point_error
     - UINT8
     - | Falha no ponto de comando, 0-sem falha,
       | 1-Erro no ponto de comando da junta,
       | 2-Erro no ponto alvo linear,
       | 3-Erro no ponto intermediário do arco,
       | 4-Erro no ponto alvo do arco,
       | 5-Espaçamento entre pontos de comando do arco muito pequeno,
       | 6-Erro no ponto intermediário 1 do círculo completo/hélice,
       | 7-Erro no ponto intermediário 2 do círculo completo/hélice,
       | 8-Erro no ponto intermediário 3 do círculo completo/hélice,
       | 9-Espaçamento entre pontos de comando do círculo completo/hélice muito pequeno,
       | 10-Erro no ponto de comando TPD,
       | 11-Ferramenta de comando TPD não corresponde à ferramenta atual,
       | 12-Desvio muito grande entre o comando TPD atual e o ponto inicial do próximo comando,
       | 13-Erro de alternância de ferramenta interna/externa,
       | 14-Erro no ponto inicial da nova hélice,
       | 15-Erro no ponto de comando da nova curva spline,
       | 17-Comando de junta PTP fora do limite,
       | 18-Comando de junta TPD fora do limite,
       | 19-Comando de junta emitido LIN\ARC fora do limite,
       | 20-Excesso de velocidade de comando no espaço cartesiano,
       | 21-Comando de torque no espaço da junta fora do limite,
       | 22-Comando de junta JOG fora do limite,
       | 23-Velocidade de comando do eixo 1 no espaço da junta fora do limite,
       | 24-Velocidade de comando do eixo 2 no espaço da junta fora do limite,
       | 25-Velocidade de comando do eixo 3 no espaço da junta fora do limite,
       | 26-Velocidade de comando do eixo 4 no espaço da junta fora do limite,
       | 27-Velocidade de comando do eixo 5 no espaço da junta fora do limite,
       | 28-Velocidade de comando do eixo 6 no espaço da junta fora do limite,
       | 29-Velocidade de feedback da junta fora do limite,
       | 30-Desvio entre comando da junta e feedback muito grande,
       | 31-Erro no ponto alvo DMP (incluindo incompatibilidade de ferramenta),
       | 32-Velocidade TCP fora do limite,
       | 33-Mudança de configuração da junta do próximo comando,
       | 34-Mudança de configuração da junta do comando atual,
       | 35-Velocidade da junta no comando LIN fora do limite,
       | 36-Velocidade adaptativa do comando LIN excede o limite,
       | 37-Ponto inalcançável na trajetória,
       | 38-Ponto inalcançável na trajetória - postura singular,
       | 49-Comandos PTP e SPTP não permitidos entre ARCSTART e ARCEND,
       | 50-Comandos PTP e SPTP não permitidos entre WEAVESTART e WEAVEEND,
       | 51-Erro de parâmetro de soldagem oscilante,
       | 52-Espaçamento entre pontos de comando de soldagem oscilante muito pequeno,
       | 53-Ponto inalcançável na trajetória de oscilação - postura singular,
       | 54-Ponto inalcançável na trajetória de oscilação - comando de junta fora do limite,
       | 55-Ponto inalcançável na trajetória de oscilação - exceção de planejamento (Z da ferramenta coincide com o ângulo da direção de avanço X),
       | 56-Ponto inalcançável na trajetória de oscilação - exceção de planejamento (erro no ponto de caminho do arco),
       | 65-Desvio de comando do sensor laser muito grande,
       | 66-Comando do sensor laser interrompido, rastreamento da junta de solda encerrado prematuramente,
       | 81-Velocidade de comando do eixo externo fora do limite,
       | 82-Desvio entre comando do eixo externo e feedback muito grande,
       | 83-Comunicação do periférico estendido (eixo externo/IO) interrompida,
       | 84-Exceção de perda de pacotes na comunicação do periférico estendido (eixo externo/IO),
       | 85-Velocidade de comando do eixo externo 1 no espaço da junta fora do limite,
       | 86-Velocidade de comando do eixo externo 2 no espaço da junta fora do limite,
       | 87-Velocidade de comando do eixo externo 3 no espaço da junta fora do limite,
       | 88-Velocidade de comando do eixo externo 4 no espaço da junta fora do limite,
       | 89-Erro de comunicação Ethercat do periférico estendido (eixo externo/IO),
       | 90-Erro de comunicação Canopen do periférico estendido (eixo externo/IO),
       | 97-Rastreamento da esteira - mudança de postura entre o ponto inicial e o ponto de referência muito grande,
       | 113-Controle de força constante - direção X excede a distância máxima de ajuste,
       | 114-Controle de força constante - direção Y excede a distância máxima de ajuste,
       | 115-Controle de força constante - direção Z excede a distância máxima de ajuste,
       | 116-Controle de força constante - direção RX excede o ângulo máximo de ajuste,
       | 117-Controle de força constante - direção RY excede o ângulo máximo de ajuste,
       | 118-Controle de força constante - direção RZ excede o ângulo máximo de ajuste,
       | 119-Erro de dados do sensor externo,
       | 120-Movimento de busca helicoidal falhou,
       | 121-Movimento de inserção rotativa falhou,
       | 122-Movimento de inserção linear falhou,
       | 123-Movimento de posicionamento de superfície falhou,
       | 124-Força de arrasto anormal, entrada no arrasto falhou,
       | 129-Número máximo de pontos de registro de torque excedido,
       | 130-Erro de alternância de velocidade,
       | 131-Direção da ferramenta fora do limite,
       | 132-Momento fora do limite,
       | 133-Potência fora do limite,
       | 134-Anomalia de diagnóstico STL-Flash,
       | 135-Anomalia de diagnóstico STL-RAM,
       | 136-Anomalia de diagnóstico STL-CPU,
       | 137-Anomalia de dados de segurança da placa de segurança II-ECAT,
       | 138-Anomalia de dados de segurança ECAT do eixo 1,
       | 139-Anomalia de dados de segurança ECAT do eixo 2,
       | 140-Anomalia de dados de segurança ECAT do eixo 3,
       | 141-Anomalia de dados de segurança ECAT do eixo 4,
       | 142-Anomalia de dados de segurança ECAT do eixo 5,
       | 143-Anomalia de dados de segurança ECAT do eixo 6,
       | 145-Anomalia de comunicação entre a placa de segurança e o controlador,
       | 147-Erro de acompanhamento de foco,
       | 148-Velocidade angular fora do limite,
       | 149-Anomalia de feedback da palavra de estado da junta
   
   * - IO_error
     - UINT8
     - | Falha de IO, 0-sem falha,
       | 1-Erro de canal, reiniciável,
       | 2-Erro de valor, reiniciável,
       | 3-Timeout de espera WaitDI, reiniciável,
       | 4-Timeout de espera WaitAI, reiniciável,
       | 5-Timeout de espera WaitAxleDI, reiniciável,
       | 6-Timeout de espera WaitAxleAI, reiniciável,
       | 7-Erro de função configurada do canal, reiniciável,
       | 8-Timeout de início de arco, reiniciável,
       | 9-Timeout de fim de arco, reiniciável,
       | 10-Timeout de busca, reiniciável,
       | 11-Timeout de detecção de IO da esteira, reiniciável,
       | 12-Timeout de espera WaitAuxDI, reiniciável,
       | 13-Timeout de espera WaitAuxAI, reiniciável,
       | 14-Timeout de busca de fio, reiniciável
   
   * - gripper_error
     - UINT8
     - Falha da garra, 0-sem falha, 1-Erro de timeout de movimento da garra, reiniciável
   
   * - file_error
     - UINT8
     - | Falha de arquivo de configuração, 0-sem falha,
       | 1-Erro de versão do arquivo de configuração zbt, erro de inicialização - não reiniciável,
       | 2-Falha no carregamento do arquivo de configuração zbt, erro de inicialização - não reiniciável,
       | 3-Erro de versão do arquivo de configuração user, erro de inicialização - não reiniciável,
       | 4-Falha no carregamento do arquivo de configuração user, erro de inicialização - não reiniciável,
       | 5-Erro de versão do arquivo de configuração exaxis, erro de inicialização - não reiniciável,
       | 6-Falha no carregamento do arquivo de configuração exaxis, erro de inicialização - não reiniciável,
       | 7-Inconsistência do modelo do robô, necessidade de redefinição - não reiniciável,
       | 8-Erro de versão do arquivo de configuração dhpara, erro de inicialização - não reiniciável,
       | 9-Falha no carregamento do arquivo de configuração dhpara, erro de inicialização - não reiniciável,
       | 10-Modelo do robô não definido - não reiniciável,
       | 11-Erro de versão do arquivo de configuração load, erro de inicialização - não reiniciável,
       | 12-Falha no carregamento do arquivo de configuração load, erro de inicialização - não reiniciável,
       | 13-Erro de versão do arquivo de configuração speed, erro de inicialização - não reiniciável,
       | 14-Falha no carregamento do arquivo de configuração speed, erro de inicialização - não reiniciável,
       | 15-Erro de versão do arquivo de configuração weavepara, erro de inicialização - não reiniciável,
       | 16-Falha no carregamento do arquivo de configuração weavepara, erro de inicialização - não reiniciável
   
   * - para_error
     - UINT8
     - | Falha de parâmetro de configuração, 0-sem falha,
       | 1-Erro de número da ferramenta fora do limite - reiniciável,
       | 2-Erro de limite de conclusão de posicionamento - reiniciável,
       | 3-Erro de nível de colisão - reiniciável,
       | 4-Erro de peso da carga - reiniciável,
       | 5-Erro de centro de massa da carga X - reiniciável,
       | 6-Erro de centro de massa da carga Y - reiniciável,
       | 7-Erro de centro de massa da carga Z - reiniciável,
       | 8-Erro de tempo de filtro DI - reiniciável,
       | 9-Erro de tempo de filtro AxleDI - reiniciável,
       | 10-Erro de tempo de filtro AI - reiniciável,
       | 11-Erro de tempo de filtro AxleAI - reiniciável,
       | 12-Erro de intervalo de nível alto/baixo DI - reiniciável,
       | 13-Erro de intervalo de nível alto/baixo DO - reiniciável,
       | 14-Erro de número da peça de trabalho fora do limite - reiniciável,
       | 15-Erro de número do eixo externo fora do limite - reiniciável,
       | 16-Rastreamento da esteira - erro de canal do encoder - reiniciável,
       | 17-Rastreamento da esteira - erro de número do eixo da peça de trabalho - reiniciável,
       | 18-Modo de montagem FR30L - erro de montagem não padrão - reiniciável
   
   * - exaxis_out_slimit_error
     - UINT8
     - | Falha de limite suave do eixo externo, 0-sem falha,
       | 1-Falha de limite suave do eixo externo 1, reiniciável,
       | 2-Falha de limite suave do eixo externo 2, reiniciável,
       | 3-Falha de limite suave do eixo externo 3, reiniciável,
       | 4-Falha de limite suave do eixo externo 4, reiniciável,
       | 5-Falha de limite suave do eixo externo 5, reiniciável,
       | 6-Falha de limite suave do eixo externo 6, reiniciável
   
   * - dr_com_err
     - UINT8_6
     - Falha de comunicação do driver, 0-sem falha, 1-falha
   
   * - dr_err
     - UINT8
     - | Falha do driver, 0-sem falha,
       | 1-Falha do driver do eixo 1, não reiniciável,
       | 2-Falha do driver do eixo 2, não reiniciável,
       | 3-Falha do driver do eixo 3, não reiniciável,
       | 4-Falha do driver do eixo 4, não reiniciável,
       | 5-Falha do driver do eixo 5, não reiniciável,
       | 6-Falha do driver do eixo 6, não reiniciável
   
   * - out_sflimit_err
     - UINT8
     - | Falha de limite suave, 0-sem falha,
       | 1-Falha de limite suave do eixo 1, reiniciável,
       | 2-Falha de limite suave do eixo 2, reiniciável,
       | 3-Falha de limite suave do eixo 3, reiniciável,
       | 4-Falha de limite suave do eixo 4, reiniciável,
       | 5-Falha de limite suave do eixo 5, reiniciável,
       | 6-Falha de limite suave do eixo 6, reiniciável

.. centered:: Tabela 1-2 Funções de Configuração de Controle de Entrada do Robô

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Tipo de Dado**
     - **Descrição**

   * - speed_mask
     - UINT8
     - Máscara de configuração de velocidade global: 0-não efetivo; 1-efetivo

   * - speed
     - UINT8
     - Definir velocidade global (0-100)

   * - std_DO_mask
     - UINT8
     - Máscara de controle de saída DO padrão do painel de controle (bit0 ~ bit7 representam DO0 ~ DO7)

   * - std_DO_box
     - UINT8
     - Saída DO padrão do painel de controle (bit0 ~ bit7 representam DO0 ~ DO7)

   * - cfg_DO_mask
     - UINT8
     - Máscara de controle de saída CO configurável do painel de controle (bit0 ~ bit7 representam CO0 ~ CO7)

   * - cfg_DO_box
     - UINT8
     - Saída CO configurável do painel de controle (bit0 ~ bit7 representam CO0 ~ CO7)

   * - cfg_DO_tool_mask
     - UINT8
     - Máscara de controle de saída DO da ferramenta padrão do painel de controle (bit0 ~ bit1 representam toolDO0 ~ toolDO1)

   * - cfg_DO_tool
     - UINT8
     - Saída DO da ferramenta padrão do painel de controle (bit0 ~ bit1 representam toolDO0 ~ toolDO1)

   * - std_AO_mask
     - UINT8
     - Máscara de controle de saída analógica do robô (bit0 ~ bit1 representam AO0 ~ AO1 do painel de controle; bit2 representa AO0 da ferramenta)

   * - std_AO0_box
     - DOUBLE
     - Saída analógica AO0 do painel de controle (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - Saída analógica AO1 do painel de controle (0.0 ~ 4095.0)

   * - std_AO0_tool
     - DOUBLE
     - Saída analógica AO1 da ferramenta (0.0 ~ 4095.0)

   * - input_BIT_reg_8xX
     - UINT8_X
     - Registradores de entrada do robô tipo BIT (8xX indica o número de registradores. Se você precisar de 16 registradores de entrada tipo BIT, o nome real será: "input_BIT_reg_8x2". O robô suporta no máximo 128 registradores tipo BIT)

   * - input_INT_reg_X
     - INT32_X
     - Registradores de entrada do robô tipo INT (X indica o número de registradores. Se você precisar de 16 registradores de entrada tipo INT, o nome real será: "input_INT_reg_16". O robô suporta no máximo 64 registradores tipo INT)
  
   * - input_DOUBLE_reg_X
     - DOUBLE_X
     - Registradores de entrada do robô tipo DOUBLE (X indica o número de registradores. Se você precisar de 16 registradores de entrada tipo DOUBLE, o nome real será: "input_DOUBLE_reg_16". O robô suporta no máximo 64 registradores tipo DOUBLE)

.. centered:: Tabela 1-3 Relação entre Tipos de Dados e Comprimento de Bytes

.. list-table::
   :widths: 60 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Tipo de Dado**
     - **Comprimento (bytes)**

   * - UINT8
     - 1

   * - INT32
     - 4

   * - DOUBLE
     - 8

   * - UINT8_X
     - 1*X

   * - INT32_X
     - 4*X

   * - DOUBLE_X
     - 8*X