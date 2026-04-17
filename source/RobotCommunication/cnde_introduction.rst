Introdução ao CNDE
=============================

O Protocolo de Troca de Dados Configurável em Rede (doravante denominado CNDE) para robôs colaborativos é uma forma pela qual o cliente controla o robô e obtém o feedback de estado do robô através da comunicação UDP.

A Tabela 1-1 é o conjunto de todos os estados do robô que podem ser obtidos pelo CNDE. O cliente pode selecionar arbitrariamente vários estados necessários da tabela e fazer com que o robô forneça o feedback de estado de acordo com um período de feedback definido.

Da mesma forma, o cliente também pode selecionar as combinações de funções de controle do robô necessárias da Tabela 1-2 para executar operações de controle do robô. Os dados de comunicação CNDE entre o cliente e o robô devem seguir um formato de quadro especificado. A porta de comunicação CNDE do robô é a 20006.

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

   * - ft_sensor_data
     - DOUBLE_6
     - Dados do sensor de força

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