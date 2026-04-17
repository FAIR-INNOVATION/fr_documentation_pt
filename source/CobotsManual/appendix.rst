Apêndice
==============

.. toctree:: 
  :maxdepth: 5

Apêndice 1: Códigos de Erro do Controlador de Movimento e Soluções
----------------------------------------------------------------------------------------

.. csv-table:: 
   :header: "Código Principal", "Subcódigo", "Descrição"
   :widths: 20, 10, 70

   "0-Sem erro", "0", "Sem erro"
   "1-Erro no ponto de comando", "1", "Erro no ponto de comando da junta, reinicializável"
   "1-Erro no ponto de comando", "2", "Erro no ponto de destino linear (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "3", "Erro no ponto intermediário do arco (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "4", "Erro no ponto de destino do arco (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "5", "Distância entre pontos de comando do arco muito pequena, reinicializável"
   "1-Erro no ponto de comando", "6", "Erro no ponto intermediário 1 do círculo completo/hélice (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "7", "Erro no ponto intermediário 2 do círculo completo/hélice (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "8", "Erro no ponto intermediário 3 do círculo completo/hélice (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "9", "Distância entre pontos de comando do círculo completo/hélice muito pequena, reinicializável"
   "1-Erro no ponto de comando", "10", "Erro no ponto de comando TPD, reinicializável"
   "1-Erro no ponto de comando", "11", "Ferramenta de comando TPD incompatível com a ferramenta atual, reinicializável"
   "1-Erro no ponto de comando", "12", "Desvio excessivo entre o comando atual e o ponto de início do próximo comando TPD, reinicializável"
   "1-Erro no ponto de comando", "13", "Erro na alternância entre ferramenta interna e externa, reinicializável"
   "1-Erro no ponto de comando", "14", "Erro no ponto de início da nova hélice, reinicializável"
   "1-Erro no ponto de comando", "15", "Erro no ponto de comando da nova spline, reinicializável"
   "1-Erro no ponto de comando", "17", "Comando de junta PTP excede o limite, reinicializável"
   "1-Erro no ponto de comando", "18", "Comando de junta TPD excede o limite, reinicializável"
   "1-Erro no ponto de comando", "19", "Comando de junta LIN/ARC excede o limite, reinicializável"
   "1-Erro no ponto de comando", "20", "Excesso de velocidade no espaço cartesiano, não reinicializável"
   "1-Erro no ponto de comando", "21", "Comando de torque no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "22", "Comando de junta JOG excede o limite, reinicializável"
   "1-Erro no ponto de comando", "23", "Velocidade de comando do eixo 1 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "24", "Velocidade de comando do eixo 2 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "25", "Velocidade de comando do eixo 3 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "26", "Velocidade de comando do eixo 4 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "27", "Velocidade de comando do eixo 5 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "28", "Velocidade de comando do eixo 6 no espaço da junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "29", "Velocidade de realimentação da junta excede o limite, não reinicializável"
   "1-Erro no ponto de comando", "30", "Desvio excessivo entre o comando e a realimentação da junta, não reinicializável, requer reinicialização"
   "1-Erro no ponto de comando", "31", "Erro no ponto de destino DMP (inclui incompatibilidade de ferramenta), reinicializável"
   "1-Erro no ponto de comando", "33", "Mudança na configuração da junta do próximo comando (próximo comando tem pose singular, use o comando PTP ou altere o próximo ponto de comando), reinicializável"
   "1-Erro no ponto de comando", "34", "Mudança na configuração da junta do comando atual (próximo comando tem pose singular, use o comando PTP ou altere o próximo ponto de comando), reinicializável"
   "1-Erro no ponto de comando", "35", "Velocidade da junta no comando LIN excede o limite, reinicializável"
   "1-Erro no ponto de comando", "36", "Velocidade adaptativa do comando LIN excede o limite, reinicializável"
   "1-Erro no ponto de comando", "37", "Ponto inalcançável na trajetória, reinicializável"
   "1-Erro no ponto de comando", "38", "Ponto inalcançável na trajetória - pose singular, reinicializável"
   "1-Erro no ponto de comando", "49", "Erro de comando, apenas comandos LIN e ARC são permitidos entre ARCSTART e ARCEND, reinicializável"
   "1-Erro no ponto de comando", "50", "Erro de comando, apenas comandos LIN e ARC são permitidos entre WEAVESTART e WEAVEEND, reinicializável"
   "1-Erro no ponto de comando", "51", "Parâmetro de soldagem com oscilação incorreto, reinicializável"
   "1-Erro no ponto de comando", "52", "Distância entre pontos de comando de soldagem com oscilação muito pequena, reinicializável"
   "1-Erro no ponto de comando", "53", "Ponto inalcançável na trajetória de oscilação - pose singular, reinicializável"
   "1-Erro no ponto de comando", "54", "Ponto inalcançável na trajetória de oscilação - comando de junta excede o limite, reinicializável"
   "1-Erro no ponto de comando", "55", "Ponto inalcançável na trajetória de oscilação - erro de planejamento (ângulo entre o eixo Z da ferramenta e a direção X de avanço está alinhado), reinicializável"
   "1-Erro no ponto de comando", "56", "Ponto inalcançável na trajetória de oscilação - erro de planejamento (ponto de caminho do arco incorreto), reinicializável"
   "1-Erro no ponto de comando", "65", "Desvio excessivo do comando do sensor a laser, reinicializável"
   "1-Erro no ponto de comando", "66", "Interrupção do comando do sensor a laser, rastreamento de junta de solda encerrado prematuramente, reinicializável"
   "1-Erro no ponto de comando", "81", "Velocidade de comando do eixo externo excede o limite, reinicializável"
   "1-Erro no ponto de comando", "82", "Desvio excessivo entre o comando e a realimentação do eixo externo, não reinicializável, requer retorno à origem ou reinicialização"
   "1-Erro no ponto de comando", "83", "Erro de comunicação do periférico estendido (eixo externo/IO), reinicializável"
   "1-Erro no ponto de comando", "84", "Erro de perda de pacotes na comunicação do periférico estendido (eixo externo/IO), reinicializável"
   "1-Erro no ponto de comando", "97", "Rastreamento de esteira - mudança excessiva na pose entre o ponto de início e o ponto de referência, reinicializável"
   "1-Erro no ponto de comando", "113", "Controle de força constante - distância de ajuste máximo excedida na direção X, reinicializável"
   "1-Erro no ponto de comando", "114", "Controle de força constante - distância de ajuste máximo excedida na direção Y, reinicializável"
   "1-Erro no ponto de comando", "115", "Controle de força constante - distância de ajuste máximo excedida na direção Z, reinicializável"
   "1-Erro no ponto de comando", "116", "Controle de força constante - ângulo de ajuste máximo excedido na direção RX, reinicializável"
   "1-Erro no ponto de comando", "117", "Controle de força constante - ângulo de ajuste máximo excedido na direção RY, reinicializável"
   "1-Erro no ponto de comando", "118", "Controle de força constante - ângulo de ajuste máximo excedido na direção RZ, reinicializável"
   "1-Erro no ponto de comando", "119", "Dados incorretos do sensor externo, reinicializável"
   "1-Erro no ponto de comando", "120", "Falha no movimento de exploração em hélice, reinicializável"
   "1-Erro no ponto de comando", "121", "Falha no movimento de inserção rotativa, reinicializável"
   "1-Erro no ponto de comando", "122", "Falha no movimento de inserção linear, reinicializável"
   "1-Erro no ponto de comando", "123", "Falha no movimento de localização de superfície, reinicializável"
   "1-Erro no ponto de comando", "129", "Número máximo de pontos de registro de torque excedido, reinicializável"
   "1-Erro no ponto de comando", "130", "Erro na mudança de velocidade, reinicializável"
   "1-Erro no ponto de comando", "147", "Erro de rastreamento de foco, reinicializável"
   "1-Erro no ponto de comando", "148", "Velocidade de pose excede o limite, reinicializável"
   "1-Erro no ponto de comando", "149", "Realimentação anormal da palavra de estado da junta, reinicializável"
   "2-Falha no driver", "1", "Falha no driver do eixo 1, não reinicializável"
   "2-Falha no driver", "2", "Falha no driver do eixo 2, não reinicializável"
   "2-Falha no driver", "3", "Falha no driver do eixo 3, não reinicializável"
   "2-Falha no driver", "4", "Falha no driver do eixo 4, não reinicializável"
   "2-Falha no driver", "5", "Falha no driver do eixo 5, não reinicializável"
   "2-Falha no driver", "6", "Falha no driver do eixo 6, não reinicializável"
   "3-Falha de limite suave excedido", "1", "Limite suave excedido no eixo 1, reinicializável"
   "3-Falha de limite suave excedido", "2", "Limite suave excedido no eixo 2, reinicializável"
   "3-Falha de limite suave excedido", "3", "Limite suave excedido no eixo 3, reinicializável"
   "3-Falha de limite suave excedido", "4", "Limite suave excedido no eixo 4, reinicializável"
   "3-Falha de limite suave excedido", "5", "Limite suave excedido no eixo 5, reinicializável"
   "3-Falha de limite suave excedido", "6", "Limite suave excedido no eixo 6, reinicializável"
   "4-Falha de colisão", "1", "Falha de colisão no eixo 1, reinicializável"
   "4-Falha de colisão", "2", "Falha de colisão no eixo 2, reinicializável"
   "4-Falha de colisão", "3", "Falha de colisão no eixo 3, reinicializável"
   "4-Falha de colisão", "4", "Falha de colisão no eixo 4, reinicializável"
   "4-Falha de colisão", "5", "Falha de colisão no eixo 5, reinicializável"
   "4-Falha de colisão", "6", "Falha de colisão no eixo 6, reinicializável"
   "4-Falha de colisão", "7", "Falha de colisão na extremidade, reinicializável"
   "5-Número incorreto de escravos ativos", "1", "Número incorreto de escravos ativos, não reinicializável"
   "6-Erro de escravo", "1", "Escravo desconectado, não reinicializável"
   "6-Erro de escravo", "2", "Estado do escravo inconsistente com o valor definido, não reinicializável"
   "6-Erro de escravo", "3", "Escravo não configurado, não reinicializável"
   "6-Erro de escravo", "4", "Erro na configuração do escravo, não reinicializável"
   "6-Erro de escravo", "5", "Erro na inicialização do escravo, não reinicializável"
   "6-Erro de escravo", "6", "Erro na inicialização da comunicação por e-mail do escravo, não reinicializável"
   "7-Erro de E/S", "1", "Erro de canal, reinicializável"
   "7-Erro de E/S", "2", "Erro de valor, reinicializável"
   "7-Erro de E/S", "3", "Tempo limite de espera do WaitDI excedido, reinicializável"
   "7-Erro de E/S", "4", "Tempo limite de espera do WaitAI excedido, reinicializável"
   "7-Erro de E/S", "5", "Tempo limite de espera do WaitAxleDI excedido, reinicializável"
   "7-Erro de E/S", "6", "Tempo limite de espera do WaitAxleAI excedido, reinicializável"
   "7-Erro de E/S", "7", "Erro de funcionalidade configurada para o canal, reinicializável"
   "7-Erro de E/S", "8", "Tempo limite de abertura de arco excedido, reinicializável"
   "7-Erro de E/S", "9", "Tempo limite de fechamento de arco excedido, reinicializável"
   "7-Erro de E/S", "10", "Tempo limite de busca de posição excedido, reinicializável"
   "7-Erro de E/S", "11", "Tempo limite de detecção de E/S da esteira excedido, reinicializável"
   "7-Erro de E/S", "12", "Tempo limite de espera do WaitAuxDI excedido, reinicializável"
   "7-Erro de E/S", "13", "Tempo limite de espera do WaitAuxAI excedido, reinicializável"
   "7-Erro de E/S", "14", "Tempo limite de busca de posição do arame de solda excedido, reinicializável"
   "8-Erro da garra", "1", "Erro de tempo limite de movimento da garra, reinicializável"
   "9-Erro de arquivo", "1", "Erro de versão do arquivo de configuração zbt, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "2", "Falha ao carregar o arquivo de configuração zbt, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "3", "Erro de versão do arquivo de configuração user, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "4", "Falha ao carregar o arquivo de configuração user, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "5", "Erro de versão do arquivo de configuração exaxis, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "6", "Falha ao carregar o arquivo de configuração exaxis, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "7", "Inconsistência no modelo do robô, requer reconfiguração - não reinicializável"
   "9-Erro de arquivo", "8", "Erro de versão do arquivo de configuração dhpara, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "9", "Falha ao carregar o arquivo de configuração dhpara, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "10", "Modelo do robô não definido - não reinicializável"
   "9-Erro de arquivo", "11", "Erro de versão do arquivo de configuração load, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "12", "Falha ao carregar o arquivo de configuração load, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "13", "Erro de versão do arquivo de configuração speed, erro de inicialização - não reinicializável"
   "9-Erro de arquivo", "14", "Falha ao carregar o arquivo de configuração speed, erro de inicialização - não reinicializável"
   "10-Pose singular", "1", "Pose singular"
   "11-Erro de comunicação do driver", "1", "Erro de comunicação do driver do eixo 1, não reinicializável"
   "11-Erro de comunicação do driver", "2", "Erro de comunicação do driver do eixo 2, não reinicializável"
   "11-Erro de comunicação do driver", "3", "Erro de comunicação do driver do eixo 3, não reinicializável"
   "11-Erro de comunicação do driver", "4", "Erro de comunicação do driver do eixo 4, não reinicializável"
   "11-Erro de comunicação do driver", "5", "Erro de comunicação do driver do eixo 5, não reinicializável"
   "11-Erro de comunicação do driver", "6", "Erro de comunicação do driver do eixo 6, não reinicializável"
   "12-Limite suave do eixo externo", "1", "Limite suave excedido no eixo 1, reinicializável"
   "12-Limite suave do eixo externo", "2", "Limite suave excedido no eixo 2, reinicializável"
   "12-Limite suave do eixo externo", "3", "Limite suave excedido no eixo 3, reinicializável"
   "12-Limite suave do eixo externo", "4", "Limite suave excedido no eixo 4, reinicializável"
   "13-Erro de parâmetro definido", "1", "Número da ferramenta excede o limite, reinicializável"
   "13-Erro de parâmetro definido", "2", "Valor limite de conclusão de posicionamento incorreto, reinicializável"
   "13-Erro de parâmetro definido", "3", "Nível de colisão incorreto, reinicializável"
   "13-Erro de parâmetro definido", "4", "Peso da carga incorreto, reinicializável"
   "13-Erro de parâmetro definido", "5", "Coordenada X do centro de massa da carga incorreta, reinicializável"
   "13-Erro de parâmetro definido", "6", "Coordenada Y do centro de massa da carga incorreta, reinicializável"
   "13-Erro de parâmetro definido", "7", "Coordenada Z do centro de massa da carga incorreta, reinicializável"
   "13-Erro de parâmetro definido", "8", "Tempo de filtragem DI incorreto, reinicializável"
   "13-Erro de parâmetro definido", "9", "Tempo de filtragem AxleDI incorreto, reinicializável"
   "13-Erro de parâmetro definido", "10", "Tempo de filtragem AI incorreto, reinicializável"
   "13-Erro de parâmetro definido", "11", "Tempo de filtragem AxleAI incorreto, reinicializável"
   "13-Erro de parâmetro definido", "12", "Faixa de nível alto/baixo DI incorreta, reinicializável"
   "13-Erro de parâmetro definido", "13", "Faixa de nível alto/baixo DO incorreta, reinicializável"
   "13-Erro de parâmetro definido", "14", "Número da peça excede o limite, reinicializável"
   "13-Erro de parâmetro definido", "15", "Número do eixo externo excede o limite, reinicializável"
   "13-Erro de parâmetro definido", "16", "Erro no canal do codificador da esteira, reinicializável"
   "13-Erro de parâmetro definido", "17", "Erro no número do eixo da peça na esteira, reinicializável"

Apêndice 2: Tabela de Códigos de Falha do Servo Driver
-------------------------------------------------------------------------

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center

   * - **Código**
     - **Nome da Falha**
     - **Procedimento**

   * - 1
     - Sobrecorrente de software
     - | 1. Verifique se a carga ou resistência da junta aumentou ou está anormal.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 2
     - Sobretensão
     - Reduza a velocidade ou aceleração do robô.

   * - 3
     - Subtensão
     - | 1. Verifique se a saída de tensão da fonte de alimentação de 48V da caixa de controle está anormal.
       | 2. Verifique se há curto-circuito entre a placa de acionamento e o invólucro da junta.
       | 3. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 4
     - Superaquecimento
     - Reduza a carga ou a velocidade de operação do robô.

   * - 5
     - Sobrecarga
     - Reduza a carga ou a velocidade de operação do robô.

   * - 6
     - Excesso de velocidade
     - | 1. Verifique se o parafuso de fixação entre o módulo magnético e o eixo do motor está solto.
       | 2. Reexecute a calibração do codificador.
       | 3. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 7
     - Falha de parâmetro anormal
     - Repare ou substitua a placa de acionamento.

   * - 8
     - Falha de descontrole (overspeed)
     - | 1. Verifique se o parafuso de fixação entre o módulo magnético e o eixo do motor está solto.
       | 2. Reexecute a calibração do codificador.
       | 3. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 9
     - Falha de erro de posição
     - | 1. Verifique se a carga ou resistência da junta aumentou ou está anormal.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 10
     - Falha de estouro de posição
     - | 1. Verifique se o limite físico está solto.
       | 2. Reexecute a calibração do robô.

   * - 11
     - Sobrecorrente de hardware
     - Repare ou substitua a placa de acionamento.

   * - 12
     - Falha de inibição de acionamento
     - Não utilizado.

   * - 13
     - Falha de bloqueio do motor
     - | 1. Verifique se o eletroímã do freio está acionado.
       | 2. Verifique se houve colisão com o limite físico.
       | 3. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 14
     - Falha na fonte de alimentação de potência
     - Não utilizado.

   * - 15
     - Falha STO
     - Não utilizado.

   * - 16
     - Falha de ajuste de zero da corrente de fase AD
     - Repare ou substitua a placa de acionamento.

   * - 17
     - Falha EEPROM
     - Repare ou substitua a placa de acionamento.

   * - 18
     - Falha Hall
     - | 1. Verifique se o chicote Hall está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a junta.

   * - 19
     - Falha do codificador
     - Repare ou substitua o módulo magnético.

   * - 20
     - Falha de ajuste de zero do codificador
     - | 1. Reexecute a calibração do codificador.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.
   
   * - 21
     - Falha de perda do sinal Z do codificador
     - Não utilizado.

   * - 22
     - Falha de contagem do codificador
     - Não utilizado.

   * - 23
     - Falha de estouro de dados multivolta do codificador
     - Não utilizado.

   * - 24
     - Falha de clock externo
     - Repare ou substitua a placa de acionamento.

   * - 25
     - Falha de sequência de fases UVW
     - Não utilizado.

   * - 26
     - Falha FPGA
     - Não utilizado.

   * - 27
     - Falha de retorno à origem
     - Não utilizado.

   * - 28
     - Falha do codificador magnético
     - | 1. Verifique se o parafuso de fixação entre o módulo magnético e o eixo do motor está solto.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 29
     - Falha de fio de alimentação do motor rompido
     - | 1. Verifique se o cabo de alimentação do motor está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 30
     - Falha EtherCAT
     - | 1. Verifique se o cabo de rede está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 31
     - Falha EtherCAT_SM_DOG
     - | 1. Verifique se o cabo de rede está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 32
     - Falha EtherCAT_FATALSYNC
     - | 1. Verifique se o cabo de rede está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 33
     - Falha EtherCAT_SYNC
     - | 1. Verifique se o cabo de rede está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 34
     - Falha EtherCAT_RFT
     - | 1. Verifique se o cabo de rede está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 35
     - Falha de endereço do eixo do driver
     - | 1. Reconfigure o endereço do eixo do driver.
       | 2. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 36
     - Falha de calibração do robô
     - | 1. Reexecute a calibração do robô.
       | 2. Primeiro, use o JLINK para apagar a FLASH, depois recarregue o programa e recalibre.
       | 3. Se a falha persistir, repare ou substitua a placa de acionamento.

   * - 37
     - Falha de comunicação do codificador
     - | 1. Verifique se o chicote do codificador está firmemente conectado, sem curto ou circuito aberto.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 40
     - Falha do módulo magnético - falha de calibração
     - | 1. Reexecute a calibração do módulo magnético.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 41
     - Falha do módulo magnético - falha multivolta
     - | 1. Verifique se o parafuso de fixação entre o módulo magnético e o eixo do motor está solto.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 42
     - Falha do módulo magnético - falha do pequeno codificador magnético multivolta
     - | 1. Verifique se o chip do pequeno codificador magnético multivolta está anormal.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 43
     - Falha do módulo magnético - falha do grande codificador magnético multivolta
     - | 1. Verifique se o chip do grande codificador magnético multivolta está anormal.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 44
     - Falha do módulo magnético - falha do codificador magnético de volta única
     - | 1. Verifique se o chip do codificador magnético de volta única está anormal.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

   * - 45
     - Falha do módulo magnético - falha do codificador óptico
     - | 1. Verifique se o disco de codificação óptico está contaminado ou mal fixado.
       | 2. Se a falha persistir, repare ou substitua o módulo magnético.

Apêndice 3: Atualização via 485 da Placa de Extremidade
-------------------------------------------------------------------------

Durante o uso em campo, pode ser necessário atualizar o firmware para atender a novos requisitos. Um novo arquivo de atualização (XX_XX_MAIN.bin) será fornecido. A atualização da placa de extremidade é feita através da interface 485 (requer um conversor USB para 485). Os passos para a atualização são:

**Etapa 1: Conexão 485**, há um conector circular de comunicação de 5 pinos na extremidade do robô. A distribuição dos pinos e suas descrições são mostradas na Figura 1. Conecte o 485-A e 485-B da extremidade do robô aos terminais A e B do conversor USB-485 usando um par trançado.

.. figure:: appendix/001.png
   :align: center
   :width: 4in

.. centered:: Figura 18.3-1 Distribuição dos Pinos do Conector Circular

**Etapa 2: Conexão de hardware**, conecte o terminal USB do conversor USB-485 ao PC. No Gerenciador de Dispositivos do PC, se a ferramenta USB-485 for reconhecida, a seguinte interface aparecerá.

.. figure:: appendix/002.png
   :align: center
   :width: 6in

.. centered:: Figura 18.3-2 Identificação da Porta USB-485

**Etapa 3: Ferramenta de atualização**, após concluir a conexão, abra o “Assistente de Porta Serial FAIRINO”. Clique no botão “Placa de Extremidade”. Na seção “Configurações da Porta Serial”, selecione a porta serial identificada acima, configure a taxa de baud rate para 115200, 8 bits de dados, sem paridade, 1 bit de parada e, em seguida, abra a porta serial. Após a abertura bem-sucedida, a mensagem “Porta serial aberta com sucesso” será exibida.

.. figure:: appendix/003.png
   :align: center
   :width: 4in

.. centered:: Figura 18.3-3 Configurações da Porta Serial

**Etapa 4: Atualização do firmware**, selecione “Placa de Extremidade” e clique em “Atualização de Firmware”, conforme mostrado na figura:

.. figure:: appendix/004.png
   :align: center
   :width: 6in

.. centered:: Figura 18.3-4 Atualização de Firmware da Placa de Extremidade

-  Primeiro, clique em “Apagar Flash”. Após o sucesso da operação, uma mensagem de “Apagado com sucesso” aparecerá na área de recepção de dados.

-  Abra o arquivo (arquivo a ser atualizado), selecione o caminho onde ele está armazenado. Conforme mostrado abaixo, após a seleção, o nome do arquivo aparecerá na caixa de exibição.

.. figure:: appendix/005.png
   :align: center
   :width: 6in

.. centered:: Figura 18.3-5 Selecionar o Arquivo de Atualização

-  Clique em “Enviar Arquivo”. Quando a barra de progresso indicar 100%, significa que o envio do arquivo de atualização foi concluído.

**Etapa 5: Verificação da atualização**, reinicie o sistema. Na seção “Informações de Manutenção”, selecione “Consultar versão do firmware da placa de extremidade”. A versão do firmware será exibida na “Área de Recepção de Dados”. Se a versão for consistente com a do arquivo atualizado, a atualização foi bem-sucedida; caso contrário, a atualização falhou.

.. figure:: appendix/006.png
   :align: center
   :width: 6in

.. centered:: Figura 18.3-6 Consultar Versão do Firmware

Apêndice 4: Atualização via 485 da Caixa de Controle
----------------------------------------------------------------------

Na placa da caixa de controle do robô, há um conector “Fonte de Alimentação/Comunicação”. Conecte os terminais A e B da ferramenta USB-485 aos pinos “485-A” e “485-B” deste conector.

O processo de atualização é o mesmo da placa de extremidade; basta selecionar o software correspondente. Não será repetido aqui.

.. figure:: appendix/007.png
   :align: center
   :width: 4in

.. centered:: Figura 18.4-1 Conector de Fonte de Alimentação/Comunicação

Apêndice 5: Lista de Peças de Reposição e Peças Sujeitas a Desgaste
---------------------------------------------------------------------------

.. list-table::
   :widths: 40 40 20
   :header-rows: 0
   :align: center

   * - **Peça**
     - **Número**
     - **Quantidade**

   * - Parafuso M8*30
     - 4.0.08.2006185
     - 4

   * - Pino Cilíndrico Tipo A 8*20
     - 4.5.00.2013076
     - 2

   * - Fusível 5x20 6A
     - 
     - 1