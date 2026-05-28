Eixo de Extensão
==========================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "Descrição", "Define os parâmetros do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``servoCompany``: Fabricante do servo driver, 1-Dynatect;
    - ``servoModel``: Modelo do servo driver, 1-FD100-750C;
    - ``servoSoftVersion``: Versão do software do servo driver, 1-V1.0;
    - ``servoResolution``: Resolução do codificador;
    - ``axisMechTransRatio``: Relação de transmissão mecânica;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Parâmetros de Configuração do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoGetParam(servoId)``"
    "Descrição", "Obtém os parâmetros de configuração do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``servoCompany``: Fabricante do servo driver, 1-Dynatect;
    - ``servoModel``: Modelo do servo driver, 1-FD100-750C;
    - ``servoSoftVersion``: Versão do software do servo driver, 1-V1.0;
    - ``servoResolution``: Resolução do codificador;
    - ``axisMechTransRatio``: Relação de transmissão mecânica;"

Habilitar/Desabilitar Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoEnable(servoId,status)``"
    "Descrição", "Habilita/desabilita o eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``status``: Estado de habilitação, 0-desabilitar, 1-habilitar;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Modo de Controle do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetControlMode(servoId,mode)``"
    "Descrição", "Define o modo de controle do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``mode``: Modo de controle, 0-modo posição, 1-modo velocidade;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Posição Alvo do Eixo de Extensão 485 (Modo Posição)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "Descrição", "Define a posição alvo do eixo de extensão 485 (modo posição)"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``pos``: Posição alvo, mm ou °;
    - ``speed``: Velocidade alvo, mm/s ou °/s;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Torque Alvo do Eixo de Extensão 485 (Modo Torque) - Temporariamente não disponível
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetTargetTorque(servoId,torque)``"
    "Descrição", "Define o torque alvo do eixo de extensão 485 (modo torque)"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``torque``: Torque alvo, Nm;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Homing do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "Descrição", "Define o homing do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``mode``: Modo de homing, 1-homing na posição atual; 2-homing no limite negativo; 3-homing no limite positivo;
    - ``searchVel``: Velocidade de busca, mm/s ou °/s;
    - ``latchVel``: Velocidade de fixação, mm/s ou °/s;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Limpar Informações de Erro do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoClearError(servoId)``"
    "Descrição", "Limpa as informações de erro do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Estado do Servo do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoGetStatus(servoId)``"
    "Descrição", "Obtém o estado do servo do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``servoErrCode``: Código de falha do servo driver
    - ``servoState``: Estado do servo driver bit0:0-desabilitado; 1-habilitado; bit1:0-parado; 1-em movimento; bit2:0-limite positivo não acionado; 1-limite positivo acionado; bit3:0-limite negativo não acionado; 1-limite negativo acionado; bit4:0-posicionamento não concluído; 1-posicionamento concluído; bit5:0-homing não concluído; 1-homing concluído;
    - ``servoPos``: Posição atual do servo mm ou °;
    - ``servoSpeed``: Velocidade atual do servo mm/s ou °/s;
    - ``servoTorque``: Torque atual do servo Nm;"

Definir Velocidade Alvo do Eixo de Extensão 485 (Modo Velocidade)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "Descrição", "Define a velocidade alvo do eixo de extensão 485 (modo velocidade)"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;
    - ``speed``: Velocidade alvo, mm/s ou °/s;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Número do Eixo de Dados do Eixo de Extensão 485 no Feedback de Estado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServosetStatusID(servoId)``"
    "Descrição", "Define o número do eixo de dados do eixo de extensão 485 no feedback de estado"
    "Parâmetros Obrigatórios", "- ``servoId``: ID do servo driver, faixa [1-15], correspondente ao ID do escravo;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetAcc(acc, dec)``"
    "Descrição", "Define a aceleração/desaceleração do movimento do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``acc``: Aceleração do movimento do eixo de extensão 485
    - ``dec``: Desaceleração do movimento do eixo de extensão 485"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoSetEmergencyStopAcc(acc, dec)``"
    "Descrição", "Define a aceleração/desaceleração de parada de emergência do eixo de extensão 485"
    "Parâmetros Obrigatórios", "- ``acc``: Aceleração de parada de emergência do eixo de extensão 485
    - ``dec``: Desaceleração de parada de emergência do eixo de extensão 485"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoGetAcc()``"
    "Descrição", "Obtém a aceleração/desaceleração do movimento do eixo de extensão 485"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``acc``: Aceleração do movimento do eixo de extensão 485
    - ``dec``: Desaceleração do movimento do eixo de extensão 485"

Obter Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AuxServoGetEmergencyStopAcc()``"
    "Descrição", "Obtém a aceleração/desaceleração de parada de emergência do eixo de extensão 485"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``acc``: Aceleração de parada de emergência do eixo de extensão 485
    - ``dec``: Desaceleração de parada de emergência do eixo de extensão 485"

Exemplo de Código de Controle do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45)
    print(f"AuxServoSetParam is: {retval}")
    servoCompany = 0
    servoModel = 0
    servoSoftVersion = 0
    servoResolution = 0
    axisMechTransRatio = 0.0
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14)
    print(f"AuxServoSetParam is: {retval}")
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36)
    print(f"AuxServoSetParam is: {retval}")
    time.sleep(3)
    robot.AuxServoSetAcc(3000, 3000)
    robot.AuxServoSetEmergencyStopAcc(5000, 5000)
    time.sleep(1)
    emagacc = 0.0
    emagdec = 0.0
    acc = 0.0
    dec = 0.0
    error,emagacc, emagdec = robot.AuxServoGetEmergencyStopAcc()
    print(f"emergency acc is {emagacc}  dec is {emagdec}")
    error,acc, dec = robot.AuxServoGetAcc()
    print(f"acc is {acc}  dec is {dec}")
    robot.AuxServoSetControlMode(1, 0)
    time.sleep(2)
    retval = robot.AuxServoEnable(1, 0)
    print(f"AuxServoEnable disenable {retval}")
    time.sleep(1)
    servoErrCode = 0
    servoState = 0
    servoPos = 0.0
    servoSpeed = 0.0
    servoTorque = 0.0
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoEnable(1, 1)
    print(f"AuxServoEnable enable {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoHoming(1, 1, 5, 1,100)
    print(f"AuxServoHoming {retval}")
    time.sleep(3)
    retval = robot.AuxServoSetTargetPos(1, 200, 30,100)
    print(f"AuxServoSetTargetPos {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoSpeed {servoSpeed}")
    time.sleep(8)
    robot.AuxServoSetControlMode(1, 1)
    time.sleep(2)
    robot.AuxServoEnable(1, 0)
    time.sleep(1)
    robot.AuxServoEnable(1, 1)
    time.sleep(1)
    robot.AuxServoSetTargetSpeed(1, 100, 80)
    time.sleep(5)
    robot.AuxServoSetTargetSpeed(1, 0, 80)
    robot.CloseRPC()

Configuração dos Parâmetros de Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevSetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum, selfConnect)``"
    "Descrição", "Configuração dos parâmetros de comunicação UDP do eixo de extensão"
    "Parâmetros Obrigatórios", "
    - ``ip``: Endereço IP do CLP;
    - ``port``: Número da porta;
    - ``period``: Período de comunicação (ms, temporariamente não disponível);
    - ``lossPkgTime``: Tempo de detecção de perda de pacotes (ms);
    - ``lossPkgNum``: Número de perdas de pacotes;
    - ``disconnectTime``: Duração de confirmação de desconexão da comunicação;
    - ``reconnectEnable``: Habilitação de reconexão automática em caso de desconexão da comunicação 0-desabilitar 1-habilitar;
    - ``reconnectPeriod``: Intervalo de reconexão (ms);
    - ``reconnectNum``: Número de tentativas de reconexão
    - ``selfConnect``: Se estabelece conexão automaticamente após reinicialização; 0-não estabelecer; 1-estabelecer"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Parâmetros de Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevGetUDPComParam()``"
    "Descrição", "Obtém os parâmetros de comunicação UDP do eixo de extensão"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "
    - Código de erro: Sucesso-0   Falha - errcode;
    - ``ip``: Endereço IP do CLP;
    - ``port``: Número da porta;
    - ``period``: Período de comunicação (ms, temporariamente não disponível);
    - ``lossPkgTime``: Tempo de detecção de perda de pacotes (ms);
    - ``lossPkgNum``: Número de perdas de pacotes;
    - ``disconnectTime``: Duração de confirmação de desconexão da comunicação;
    - ``reconnectEnable``: Habilitação de reconexão automática em caso de desconexão da comunicação 0-desabilitar 1-habilitar;
    - ``reconnectPeriod``: Intervalo de reconexão (ms);
    - ``reconnectNum``: Número de tentativas de reconexão
    - ``selfConnect``: Se reconecta automaticamente após reinicialização do painel de controle; 0-não reconectar; 1-reconectar"
 
Carregar Comunicação UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevLoadUDPDriver()``"
    "Descrição", "Carrega a comunicação UDP"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
    
Descarregar Comunicação UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevUnloadUDPDriver()``"
    "Descrição", "Descarrega a comunicação UDP"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Restaurar Conexão Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevUDPClientComReset()``"
    "Descrição", "Restaura a conexão após desconexão anormal da comunicação UDP do eixo de extensão"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Fechar Comunicação Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtDevUDPClientComClose()``"
    "Descrição", "Fecha a comunicação após desconexão anormal da comunicação UDP do eixo de extensão"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Configuração dos Parâmetros do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisParamConfig(axisId, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc,axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType)``"
    "Descrição", "Configuração dos parâmetros do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "
    - ``axisId``: Número do eixo [1-4];
    - ``axisType``: Tipo de eixo de extensão 0-translação; 1-rotação;
    - ``axisDirection``: Direção do eixo de extensão 0-positiva; 1-negativa;
    - ``axisMax``: Posição máxima do eixo de extensão mm;
    - ``axisMin``: Posição mínima do eixo de extensão mm;
    - ``axisVel``: Velocidade mm/s;
    - ``axisAcc``: Aceleração mm/s2;
    - ``axisLead``: Passo mm;
    - ``encResolution``: Resolução do codificador;
    - ``axisOffect``: Deslocamento do ponto inicial da solda no eixo de extensão;
    - ``axisCompany``: Fabricante do driver 1-Huichuan; 2-Huichuan; 3-Panasonic;
    - ``axisModel``: Modelo do driver 1-Huichuan-SV-XD3EA040L-E, 2-Huichuan-SV-X2EA150A-A, 1-Huichuan-SV620PT5R4I, 1-Panasonic-MADLN15SG, 2-Panasonic-MSDLN25SG, 3-Panasonic-MCDLN35SG;
    - ``axisEncType``: Tipo de codificador  0-incremental; 1-absoluto;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Aquisição de Parâmetros de Eixo Estendido via UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisGetParamConfig(self, axisID)``"
    "Descrição", "Aquisição de parâmetros de eixo estendido via UDP"
    "Parâmetros Obrigatórios", "
    - ``axisID``：Número do eixo estendido [1-4]
    - ``axisType``：Tipo de eixo estendido 0-linear; 1-rotativo
    - ``axisDirection``：Direção do eixo estendido 0-positiva; 1-negativa
    - ``axisMax``：Posição máxima do eixo estendido mm
    - ``axisMin``：Posição mínima do eixo estendido mm
    - ``axisVel``：Velocidade mm/s
    - ``axisAcc``：Aceleração mm/s²
    - ``axisLead``：Passo mm
    - ``encResolution``：Resolução do encoder
    - ``axisOffect``：Deslocamento do eixo estendido para ponto inicial da solda
    - ``axisCompany``：Fabricante do driver 1-Hechen; 2-Inovance; 3-Panasonic
    - ``axisModel``：Modelo do driver 1-Hechen-SV-XD3EA040L-E, 2-Hechen-SV-X2EA150A-A, 1-Inovance-SV620PT5R4I, 1-Panasonic-MADLN15SG, 2-Panasonic-MSDLN25SG, 3-Panasonic-MCDLN35SG
    - ``axisEncType``：Tipo de encoder 0-incremental; 1-absoluto
    "
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro Sucesso-0 Falha- errcode"

Definir Posição do Robô em Relação ao Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotPosToAxis(installType)``"
    "Descrição", "Define a posição do robô em relação ao eixo de extensão"
    "Parâmetros Obrigatórios", "- ``installType``: 0-robô instalado no eixo externo, 1-robô instalado fora do eixo externo;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir Configuração dos Parâmetros DH do Sistema de Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAxisDHParaConfig(axisConfig,axisDHd1,axisDHd2,axisDHd3,axisDHd4,axisDHa1, axisDHa2,axisDHa3,axisDHa4)``"
    "Descrição", "Define a configuração dos parâmetros DH do sistema de eixo de extensão"
    "Parâmetros Obrigatórios", "
    - ``axisConfig``: Configuração do eixo externo, 0-trilho linear de 1 grau de liberdade, 1-posicionador tipo L de 2 graus de liberdade, 2-3 graus de liberdade, 3-4 graus de liberdade, 4-posicionador de 1 grau de liberdade;
    - ``axisDHd1``: Parâmetro DH do eixo externo d1 mm;
    - ``axisDHd2``: Parâmetro DH do eixo externo d2 mm;
    - ``axisDHd3``: Parâmetro DH do eixo externo d3 mm;
    - ``axisDHd4``: Parâmetro DH do eixo externo d4 mm;
    - ``axisDHa1``: Parâmetro DH do eixo externo a1 mm;
    - ``axisDHa2``: Parâmetro DH do eixo externo a2 mm;
    - ``axisDHa3``: Parâmetro DH do eixo externo a3 mm;
    - ``axisDHa4``: Parâmetro DH do eixo externo a4 mm;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
                          
Habilitar Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisServoOn(axisID, status)``"
    "Descrição", "Habilita o eixo de extensão UDP"
    "Parâmetros Obrigatórios", "- ``axisID``: Número do eixo [1-4];
    - ``status``: 0-desabilitar; 1-habilitar;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Homing do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisSetHoming(axisID, mode, searchVel, latchVel)``"
    "Descrição", "Homing do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "
    - ``axisID``: Número do eixo [1-4];
    - ``mode``: Modo de homing 0-homing na posição atual, 1-homing no limite negativo, 2-homing no limite positivo;
    - ``searchVel``: Velocidade de busca (mm/s);
    - ``latchVel``: Velocidade de fixação da busca (mm/s);"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Iniciar Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisStartJog( axisID, direction, vel, acc, maxDistance)``"
    "Descrição", "Inicia o jog do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "
    - ``axisID``: Número do eixo [1-4];
    - ``direction``: Direção de rotação 0-reversa; 1-positiva;
    - ``vel``: Velocidade (mm/s);
    - ``acc``: Aceleração (mm/s);
    - ``maxDistance``: Distância máxima de jog;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Parar Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisStopJog(axisID)``"
    "Descrição", "Para o jog do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "- ``axisID``: Número do eixo [1-4];"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código de Configuração e Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    from fairino.Robot import RobotState
    import time

    def main():
        # Adicionar dados de estado em tempo real a serem obtidos (se necessário)
        # rtn = AddRobotRealtimeState([RobotState.ExaxisCoordID])
        # if rtn != 0:
        #     print(f"✗ Falha ao adicionar campo, código de erro: {rtn}")
        #     return None
        # print("✓ Campo adicionado com sucesso")

        # Estabelecer conexão com o controlador do robô
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  # Aguardar conexão e recebimento de dados

        # Configurar parâmetros de comunicação UDP
        rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
        print(f"ExtDevSetUDPComParam rtn is {rtn}")

        # Obter parâmetros de comunicação UDP
        error, param = robot.ExtDevGetUDPComParam()
        print("ExtDevGetUDPComParam return ", error)
        print("Parâmetros de comunicação do eixo estendido UDP: ", param)

        # Carregar driver UDP
        robot.ExtDevLoadUDPDriver()

        # Definir tempo de conclusão do comando do eixo estendido
        rtn = robot.SetExAxisCmdDoneTime(5000.0)
        print(f"SetExAxisCmdDoneTime rtn is {rtn}")

        # Habilitação servo do eixo estendido
        rtn = robot.ExtAxisServoOn(1, 1)
        print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
        rtn = robot.ExtAxisServoOn(2, 1)
        print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
        time.sleep(2)

        # Homing do eixo estendido
        robot.ExtAxisSetHoming(1, 0, 10, 2)
        time.sleep(2)
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
        print(f"ExtAxisSetHoming rtn is {rtn}")

        time.sleep(4)

        # Definir posição relativa do robô em relação ao eixo estendido
        rtn = robot.SetRobotPosToAxis(1)
        print(f"SetRobotPosToAxis rtn is {rtn}")

        # Definir configuração de parâmetros DH do eixo estendido
        rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0)
        print(f"SetAxisDHParaConfig rtn is {rtn}")

        # Configurar parâmetros do eixo estendido 1
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
        print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")

        # Obter configuração de parâmetros do eixo estendido 1
        rtn, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType = robot.ExtAxisGetParamConfig(1)
        print(f"axis id 1 ExtAxisGetParamConfig : axisType {axisType}, axisDirection {axisDirection}, axisMax {axisMax}, axisMin {axisMin}, axisVel {axisVel}, axisAcc {axisAcc}, axisLead {axisLead}, encResolution {encResolution}, axisOffect {axisOffect}, axisCompany {axisCompany}, axisModel {axisModel}, axisEncType {axisEncType}")

        # Configurar parâmetros do eixo estendido 2
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
        print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")

        # Obter configuração de parâmetros do eixo estendido 2
        rtn, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType = robot.ExtAxisGetParamConfig(2)
        print(f"axis id 2 ExtAxisGetParamConfig : axisType {axisType}, axisDirection {axisDirection}, axisMax {axisMax}, axisMin {axisMin}, axisVel {axisVel}, axisAcc {axisAcc}, axisLead {axisLead}, encResolution {encResolution}, axisOffect {axisOffect}, axisCompany {axisCompany}, axisModel {axisModel}, axisEncType {axisEncType}")

        time.sleep(3)

        # Teste de jog do eixo estendido 1
        robot.ExtAxisStartJog(1, 0, 10, 10, 30)
        time.sleep(1)
        robot.ExtAxisStopJog(1)
        time.sleep(3)
        robot.ExtAxisServoOn(1, 0)

        time.sleep(3)

        # Teste de jog do eixo estendido 2
        robot.ExtAxisStartJog(2, 0, 10, 10, 30)
        time.sleep(1)
        robot.ExtAxisStopJog(2)
        time.sleep(3)
        robot.ExtAxisServoOn(2, 0)

        # Descarregar driver UDP
        robot.ExtDevUnloadUDPDriver()

        # Fechar conexão
        robot.CloseRPC()


    # Chamar função de teste
    main()

Definir Ponto de Referência do Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisSetRefPoint(pointNum)``"
    "Descrição", "Define o ponto de referência do sistema de coordenadas do eixo de extensão - Método de quatro pontos"
    "Parâmetros Obrigatórios", "- ``pointNum``: Número do ponto [1-4];"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Calcular Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisComputeECoordSys()``"
    "Descrição", "Calcula o sistema de coordenadas do eixo de extensão - Método de quatro pontos"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``coord``: Valor do sistema de coordenadas do eixo de extensão [x,y,z,rx,ry,rz];"
                 
Definir Ponto de Referência do Sistema de Coordenadas do Posicionador - Método de Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PositionorSetRefPoint(pointNum)``"
    "Descrição", "Define o ponto de referência do sistema de coordenadas do posicionador - Método de quatro pontos"
    "Parâmetros Obrigatórios", "- ``pointNum``: Número do ponto [1-4];"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Calcular Sistema de Coordenadas do Posicionador - Método de Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PositionorComputeECoordSys()``"
    "Descrição", "Calcula o sistema de coordenadas do posicionador - Método de quatro pontos"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``coord``: Valor do sistema de coordenadas do posicionador [x,y,z,rx,ry,rz];"
             
Definir Pose do Ponto de Referência de Calibração no Sistema de Coordenadas da Extremidade do Posicionador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRefPointInExAxisEnd(pos)``"
    "Descrição", "Define a pose do ponto de referência de calibração no sistema de coordenadas da extremidade do posicionador"
    "Parâmetros Obrigatórios", "- ``pos``: Valor da pose [x,y,z,rx,ry,rz];"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Aplicar Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisActiveECoordSys(applyAxisId,axisCoordNum,coord,calibFlag)``"
    "Descrição", "Aplica o sistema de coordenadas do eixo de extensão"
    "Parâmetros Obrigatórios", "
    - ``applyAxisId``: Número do eixo de extensão bit0-bit3 correspondem aos números dos eixos de extensão 1-4, por exemplo, aplicar eixos de extensão 1 e 3 é 0b 0000 0101, ou seja, 5;
    - ``axisCoordNum``: Número do sistema de coordenadas do eixo de extensão;
    - ``coord``: Valor do sistema de coordenadas [x,y,z,rx,ry,rz];
    - ``calibFlag``: Flag de calibração 0-não, 1-sim;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Obter Sistema de Coordenadas do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisGetCoord()``"
    "Descrição", "Obtém o sistema de coordenadas do eixo de extensão"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``coord``: Sistema de coordenadas do eixo de extensão"

Exemplo de Código de Calibração do Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
    print(f"ExtDevSetUDPComParam rtn is {rtn}")
    rtn,udp_params = robot.ExtDevGetUDPComParam()
    ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum = udp_params
    patam = (
        f"\nip {ip}\nport {port}\nperiod {period}\nlossPkgTime {lossPkgTime}\n"
        f"lossPkgNum {lossPkgNum}\ndisConntime {disconnectTime}\nreconnecable {reconnectEnable}\n"
        f"reconnperiod {reconnectPeriod}\nreconnnun {reconnectNum}"
    )
    print(f"ExtDevGetUDPComParam rtn is {rtn}{patam}")
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
    rtn = robot.ExtAxisServoOn(2, 1)
    print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    print(f"ExtAxisSetHoming rtn is {rtn}")
    time.sleep(4)
    rtn = robot.SetRobotPosToAxis(1)
    print(f"SetRobotPosToAxis rtn is {rtn}")
    rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0)
    print(f"SetAxisDHParaConfig rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")
    toolCoord = [0, 0, 210, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    jSafe = [115.193, -96.149, 92.489, -87.068, -89.15, -83.488]
    j1 = [117.559, -92.624, 100.329, -96.909, -94.057, -83.488]
    j2 = [112.239, -90.096, 99.282, -95.909, -89.824, -83.488]
    j3 = [110.839, -83.473, 93.166, -89.22, -90.499, -83.487]
    j4 = [107.935, -83.572, 95.424, -92.873, -87.933, -83.488]
    descSafe = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc1 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc2 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc3 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc4 = [0.0,0.0,0.0,0.0,0.0,0.0]
    exaxisPos = [0.0,0.0,0.0,0.0]
    offdese = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, descSafe = robot.GetForwardKin(jSafe)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    error, desc1 = robot.GetForwardKin(j1)
    robot.MoveJ(joint_pos=j1,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    actualTCPPos = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, actualTCPPos = robot.GetActualTCPPose(0)
    robot.SetRefPointInExAxisEnd(actualTCPPos)
    rtn = robot.PositionorSetRefPoint(1)
    print(f"PositionorSetRefPoint 1 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc2 = robot.GetForwardKin(j2)
    rtn = robot.MoveJ(joint_pos=j2,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(2)
    print(f"PositionorSetRefPoint 2 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc3 = robot.GetForwardKin(j3)
    robot.MoveJ(joint_pos=j3,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(3)
    print(f"PositionorSetRefPoint 3 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc4 = robot.GetForwardKin(j4)
    robot.MoveJ(joint_pos=j4,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(4)
    print(f"PositionorSetRefPoint 4 rtn is {rtn}")
    time.sleep(2)
    axisCoord = [0.0,0.0,0.0,0.0,0.0,0.0]
    error,axisCoord = robot.PositionorComputeECoordSys()
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    print(f"PositionorComputeECoordSys rtn is {axisCoord[0]} {axisCoord[1]} {axisCoord[2]} {axisCoord[3]} {axisCoord[4]} {axisCoord[5]}")
    rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1)
    print(f"ExtAxisActiveECoordSys rtn is {rtn}")
    robot.CloseRPC()
          
Movimento do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisMove(pos,ovl,blend=-1)``"
    "Descrição", "Movimento do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "- ``pos=[exaxis[0],exaxis[1],exaxis[2],exaxis[3]]``: Posição alvo (posição eixo 1 ~ posição eixo 4);
    - ``ovl``: Porcentagem de velocidade"
    "Parâmetros Padrão", "- ``blend``: Parâmetro de suavização (mm ou ms), -1, aguardar conclusão do movimento, padrão -1"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
                                        
Exemplo de Código de Movimento do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    axisPos = [20,0,0,0]
    robot.ExtAxisMove(axisPos, 50, -1)
    robot.CloseRPC()
    return 0

Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisSyncMoveJ(joint_pos,tool,user,exaxis_pos, desc_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl= 100.0,  blendT=-1.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "Descrição", "Movimento síncrono do eixo de extensão UDP com movimento articular do robô"
    "Parâmetros Obrigatórios", "
    - ``joint_pos``: Posição articular alvo, unidade [°];
    - ``desc_pos``: Pose cartesiana alvo, unidade [mm][°]
    - ``tool``: Número da ferramenta, [0~14]
    - ``user``: Número da peça, [0~14]
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4"
    "Parâmetros Padrão", "
    - ``desc_pos``: Pose cartesiana alvo, unidade [mm][°] valor inicial padrão [0.0,0.0,0.0,0.0,0.0,0.0], o valor padrão usa o valor de retorno da cinemática direta;
    - ``vel``: Porcentagem de velocidade, [0~100] padrão 20.0;
    - ``acc``: Porcentagem de aceleração, [0~100] temporariamente não disponível, padrão 0.0;
    - ``ovl``: Fator de escala de velocidade, [0~100] padrão 100.0;
    - ``blendT``: [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade [ms] padrão -1.0;
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas da peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta padrão 0;
    - ``offset_pos``: Valor de deslocamento da pose, unidade [mm][°] padrão [0.0,0.0,0.0,0.0,0.0,0.0];"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode;"
                                        
Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    # Configura parâmetros de comunicação UDP e carrega
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # Configura parâmetros do eixo de extensão
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # Habilita e faz homing do eixo de extensão
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # Calibra o sistema de coordenadas do eixo de extensão
    pos = []  # Insira as coordenadas do ponto de calibração aqui
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # Esta operação deve ser repetida 4 vezes (com 4 pontos)
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # Ponto inicial e final do movimento síncrono
    startdescPose = []  # Insira as coordenadas específicas
    startjointPos = []  # Insira as coordenadas específicas
    startexaxisPos = []  # Insira as coordenadas específicas
    enddescPose = []  # Insira as coordenadas específicas
    endjointPos = []  # Insira as coordenadas específicas
    endexaxisPos = []  # Insira as coordenadas específicas
    # Move para o ponto inicial
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, -1, 0, offdese)
    robot.CloseRPC()
                  
Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisSyncMoveL(desc_pos, tool, user, exaxis_pos, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],config=-1)``"
    "Descrição", "Movimento síncrono do eixo de extensão UDP com movimento linear do robô"
    "Parâmetros Obrigatórios", "
    - ``desc_pos``: Pose cartesiana alvo, unidade [mm][°];
    - ``tool``: Número da ferramenta, [0~14];
    - ``user``: Número da peça, [0~14];
    - ``exaxis_pos``: Posição do eixo externo 1 ~ posição do eixo externo 4;"
    "Parâmetros Padrão", "
    - ``joint_pos``: Posição articular alvo, unidade [°] valor inicial padrão [0.0,0.0,0.0,0.0,0.0,0.0], o valor padrão usa o valor de retorno da cinemática inversa;
    - ``vel``: Porcentagem de velocidade, [0~100] padrão 20.0;
    - ``acc``: Porcentagem de aceleração, [0~100] temporariamente não disponível, padrão 0.0;
    - ``ovl``: Fator de escala de velocidade, [0~100] padrão 100.0;
    - ``blendR``: [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade [ms] padrão -1.0;
    - ``search``: [0]-sem busca de posição do arame, [1]-com busca de posição do arame;
    - ``offset_flag``: [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas da peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta padrão 0;
    - ``offset_pos``: Valor de deslocamento da pose, unidade [mm][°] padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular, padrão -1"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode;"
                                            
Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    # Configura parâmetros de comunicação UDP e carrega
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # Configura parâmetros do eixo de extensão
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # Habilita e faz homing do eixo de extensão
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # Calibra o sistema de coordenadas do eixo de extensão
    pos = []  # Insira as coordenadas do ponto de calibração
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # Deve ser chamado 4 vezes para calibração
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # Ponto inicial e final do movimento síncrono
    startdescPose = []  # Insira as coordenadas
    startjointPos = []  # Insira as coordenadas
    startexaxisPos = []  # Insira as coordenadas
    enddescPose = []  # Insira as coordenadas
    endjointPos = []  # Insira as coordenadas
    endexaxisPos = []  # Insira as coordenadas
    # Move para o ponto inicial
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos, tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0)
    # Executa movimento linear síncrono
    robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, 0, 0, offdese)
    robot.CloseRPC()
                      
Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ExtAxisSyncMoveC(desc_pos_p, tool_p, user_p,exaxis_pos_p, desc_pos_t, tool_t, user_t,exaxis_pos_t,joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=100.0, offset_flag_p=0, offset_pos_p =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0, config=-1)``"
    "Descrição", " Movimento síncrono do eixo de extensão UDP com movimento de arco do robô"
    "Parâmetros Obrigatórios", "
    - ``desc_pos_p``: Pose cartesiana do ponto de caminho, unidade [mm][°];
    - ``tool_p``: Número da ferramenta no ponto de caminho, [0~14];
    - ``user_p``: Número da peça no ponto de caminho, [0~14];
    - ``exaxis_pos_p``: Posição do eixo externo no ponto de caminho (posição eixo 1 ~ posição eixo 4) padrão [0.0,0.0,0.0,0.0];
    - ``desc_pos_t``: Pose cartesiana do ponto alvo, unidade [mm][°];
    - ``tool_t``: Número da ferramenta, [0~14];
    - ``user_t``: Número da peça, [0~14];
    - ``exaxis_pos_t``: Posição do eixo externo no ponto alvo (posição eixo 1 ~ posição eixo 4) padrão [0.0,0.0,0.0,0.0];"
    "Parâmetros Padrão", "
    - ``joint_pos_p``: Posição articular alvo, unidade [°] valor inicial padrão [0.0,0.0,0.0,0.0,0.0,0.0], o valor padrão usa o valor de retorno da cinemática inversa;
    - ``joint_pos_t``: Posição articular alvo, unidade [°] valor inicial padrão [0.0,0.0,0.0,0.0,0.0,0.0], o valor padrão usa o valor de retorno da cinemática inversa;
    - ``vel_p``: Porcentagem de velocidade no ponto de caminho, [0~100] padrão 20.0;
    - ``acc_p``: Porcentagem de aceleração no ponto de caminho, [0~100] temporariamente não disponível, padrão 0.0;
    - ``offset_flag_p``: Se há deslocamento no ponto de caminho [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas da peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta padrão 0;
    - ``offset_pos_p``: Valor de deslocamento da pose no ponto de caminho, unidade [mm][°] padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``vel_t``: Porcentagem de velocidade no ponto alvo, [0~100] padrão 20.0;
    - ``acc_t``: Porcentagem de aceleração no ponto alvo, [0~100] temporariamente não disponível, padrão 0.0;
    - ``offset_flag_t``: Se há deslocamento no ponto alvo [0]-sem deslocamento, [1]-deslocamento no sistema de coordenadas da peça/base, [2]-deslocamento no sistema de coordenadas da ferramenta padrão 0;
    - ``offset_pos_t``: Valor de deslocamento da pose no ponto alvo, unidade [mm][°] padrão [0.0,0.0,0.0,0.0,0.0,0.0];
    - ``ovl``: Fator de escala de velocidade, [0~100] padrão 100.0;
    - ``blendR``: [-1.0]-movimento concluído (bloqueado), [0~1000]-raio de suavização (não bloqueado), unidade [mm] padrão -1.0;
    - ``config``: Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular, padrão -1"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode;"
                                                
Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    # Configura parâmetros de comunicação UDP e carrega
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # Configura parâmetros do eixo de extensão
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # Habilita e faz homing do eixo de extensão
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # Calibra o sistema de coordenadas do eixo de extensão
    pos = []  # Insira as coordenadas do ponto de calibração
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # Chame 4 vezes para completar a calibração
    coord = []
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # Ponto inicial, ponto intermediário e ponto final do arco síncrono
    startdescPose = []# Insira as coordenadas
    startjointPos = []# Insira as coordenadas
    startexaxisPos =[]  # Insira as coordenadas do eixo de extensão
    middescPose = []# Insira o ponto intermediário
    midjointPos = []
    midexaxisPos =[]
    enddescPose = []
    endjointPos = []
    endexaxisPos =[]
    # Move para o ponto inicial
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    # Inicia movimento de arco síncrono
    robot.ExtAxisSyncMoveC(midjointPos,middescPose,1,1,midexaxisPos,
                           endjointPos,enddescPose,1,1,endexaxisPos,
                           100,100,0,offdese,
                           100,100,0,offdese,
                           100,0)
    robot.CloseRPC()

Definir DO de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAuxDO(DONum,bOpen,smooth,block)``"
    "Descrição", "Define o DO de extensão"
    "Parâmetros Obrigatórios", "
    - ``DONum``: Número do DO;
    - ``bOpen``: Interruptor True-Ligado, False-Desligado;
    - ``smooth``: Se é suave True - Sim, False - Não;
    - ``block``: Se é bloqueante True - Sim, False - Não;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Definir AO de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAuxAO(AONum,value,block)``"
    "Descrição", "Define o AO de extensão"
    "Parâmetros Obrigatórios", "
    - ``AONum``: Número do AO;
    - ``value``: Valor analógico [0-4095];
    - ``block``: Se é bloqueante True - Sim, False - Não;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Definir Tempo de Filtro de Entrada do DI de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAuxDIFilterTime(filterTime)``"
    "Descrição", "Define o tempo de filtro de entrada do DI de extensão"
    "Parâmetros Obrigatórios", "- ``filterTime``: Tempo de filtro (ms);"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Definir Tempo de Filtro de Entrada do AI de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAuxAIFilterTime(AINum,filterTime)``"
    "Descrição", "Define o tempo de filtro de entrada do AI de extensão"
    "Parâmetros Obrigatórios", "
    - ``AINum``: Número do AI;
    - ``filterTime``: Tempo de filtro (ms);"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Aguardar Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitAuxDI(DINum,bOpen,time,errorAlarm)``"
    "Descrição", "Aguarda a entrada DI de extensão"
    "Parâmetros Obrigatórios", "
    - ``DINum``: Número do DI;
    - ``bOpen``: Interruptor True-Ligado, False-Desligado;
    - ``time``: Tempo máximo de espera (ms);
    - ``errorAlarm``: Se continua o movimento True - Sim, False - Não"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitAuxAI(,AINum,sign,value,time,errorAlarm)``"
    "Descrição", "Aguarda a entrada AI de extensão"
    "Parâmetros Obrigatórios", "
    - ``AINum``: Número do AI;
    - ``sign``: 0-maior que; 1-menor que;
    - ``value``: Valor do AI;
    - ``time``: Tempo máximo de espera (ms);
    - ``errorAlarm``: Se continua o movimento True - Sim, False - Não"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"
        
Obter Valor do DI de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAuxDI(DINum,isNoBlock)``"
    "Descrição", "Obtém o valor do DI de extensão"
    "Parâmetros Obrigatórios", "
    - ``DINum``: Número do DI;
    - ``isNoBlock``: Se é não bloqueante True - Bloqueante false - Não bloqueante;"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``isOpen``: 0-Desligado; 1-Ligado;"
          
Obter Valor do AI de Extensão
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAuxAI(AINum,isNoBlock)``"
    "Descrição", "Obtém o valor do AI de extensão"
    "Parâmetros Obrigatórios", "
    - ``AINum``: Número do AI;
    - ``isNoBlock``: Se é não bloqueante True - Bloqueante False - Não bloqueante"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode;
    - ``value``: Valor de entrada;"

Exemplo de Código de IO de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    for i in range(128):
        robot.SetAuxDO(i, True, False, True)
        time.sleep(0.1)
    for i in range(128):
        robot.SetAuxDO(i, False, False, True)
        time.sleep(0.1)
    for i in range(409):
        value1 = i * 10
        value2 = 4095 - i * 10
        robot.SetAuxAO(0, value1, True)
        robot.SetAuxAO(1, value2, True)
        robot.SetAuxAO(2, value1, True)
        robot.SetAuxAO(3, value2, True)
        time.sleep(0.01)
    robot.SetAuxDIFilterTime(10)
    robot.SetAuxAIFilterTime(0, 10)
    for i in range(20):
        curValue = False
        error, curValue = robot.GetAuxDI(i, False)  # Nota: a referência de passagem de parâmetros pode precisar de ajuste interno da biblioteca
        print(f"DI{i}   {curValue}")
    curValue = -1
    for i in range(4):
        error, curValue = robot.GetAuxAI(i, True)  # Também atentar para a passagem por referência
        print(f"AI{i}   {curValue}")
    robot.WaitAuxDI(1, False, 1000, False)
    robot.WaitAuxAI(1, 1, 132, 1000, False)
    robot.CloseRPC()

Habilitar Dispositivo Móvel
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TractorEnable(enable)``"
    "Descrição", "Habilita o dispositivo móvel"
    "Parâmetros Obrigatórios", "- ``enable``: Estado de habilitação, 0-desabilitar, 1-habilitar"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Homing do Dispositivo Móvel
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TractorHoming()``"
    "Descrição", "Homing do dispositivo móvel"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Movimento Linear do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TractorMoveL(distance, vel)``"
    "Descrição", "Movimento linear do dispositivo móvel"
    "Parâmetros Obrigatórios", "- ``distance``: Distância do movimento linear (mm)
    - ``vel``: Porcentagem de velocidade do movimento linear (0-100)"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Movimento de Arco do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``TractorMoveC(radio, angle, vel)``"
    "Descrição", "Movimento de arco do dispositivo móvel"
    "Parâmetros Obrigatórios", "- ``radio``: Raio do movimento de arco (mm)
    - ``angle``: Ângulo do movimento de arco (°)
    - ``vel``: Porcentagem de velocidade do movimento de arco (0-100)"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Parar Movimento do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramStop()``"
    "Descrição", "Para o movimento do dispositivo móvel"
    "Parâmetros Obrigatórios", "Nenhum"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 1)
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    rtn = robot.ExtAxisServoOn(2, 1)
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    time.sleep(4)
    robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0)
    robot.TractorEnable(False)
    time.sleep(2)
    robot.TractorEnable(True)
    time.sleep(2)
    robot.TractorHoming()
    time.sleep(2)
    robot.TractorMoveL(100, 2)
    time.sleep(5)
    robot.TractorStop()
    robot.TractorMoveL(-100, 20)
    time.sleep(5)
    robot.TractorMoveC(300, 90, 20)
    time.sleep(10)
    robot.TractorMoveC(300, -90, 20)
    time.sleep(1)
    robot.CloseRPC()

Registrar Ponto do Sensor a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LaserRecordPoint(coordID)``"
    "Descrição", "Registra o ponto do sensor a laser"
    "Parâmetros Obrigatórios", "- ``coordID``: Sistema de coordenadas do sensor a laser"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "- Código de erro: Sucesso-0   Falha - errcode
    - ``joint``: Posição articular do ponto identificado pelo sensor a laser
    - ``desc``: Posição cartesiana do ponto identificado pelo sensor a laser
    - ``exaxis``: Posição do eixo de extensão do ponto identificado pelo sensor a laser"

Exemplo de Código para Registrar Ponto do Sensor a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    direction_point = [0, 0, 0]
    rtn = robot.LaserTrackingSearchStart(2, direction_point, 10, 100, 10000, 2)
    print(f"LaserTrackingSearchStart rtn is {rtn}")
    robot.LaserTrackingSearchStop()
    coord_id = 2
    rtn, joint, desc, exaxis = robot.LaserRecordPoint(coord_id)
    print(f"rtn is {rtn}")
    print(f"desc_pos:{desc[0]},{desc[1]},{desc[2]},"
          f"{desc[3]},{desc[4]},{desc[5]}")
    print(f"joint_pos:{joint[0]},{joint[1]},{joint[2]},{joint[3]},{joint[4]},{joint[5]}")
    print(f"exaxis pos is {exaxis[0]} {exaxis[1]} {exaxis[2]} {exaxis[3]}")
    off = [0] * 6
    robot.MoveJ(joint,tool=1,user=0,vel=100,acc=100,ovl=50,exaxis_pos=exaxis,blendT=-1,offset_flag=0,offset_pos=off)
    robot.CloseRPC()

Definir Estratégia de Movimento Síncrono do Eixo de Extensão com o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExAxisRobotPlan(strategy)``"
    "Descrição", "Define a estratégia de movimento síncrono do eixo de extensão com o robô"
    "Parâmetros Obrigatórios", "- ``strategy``: Estratégia; 0-prioridade para o robô; 1-eixo de extensão síncrono com o robô"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"

Exemplo de Código para Definir Estratégia de Movimento Síncrono do Eixo de Extensão com o Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se bem-sucedido
    robot = Robot.RPC('192.168.58.2')
    joint_pos1 = [-22.016, -49.217, 124.714, -161.100, -85.108, -0.333]
    joint_pos2 = [-21.083, -46.613, 110.079, -147.796, -80.757, -0.330]
    joint_pos3 = [-25.572, -60.090, 135.397, -163.889, -82.489, -0.345]
    desc_pos1 = [2.637, -0.001, 30.673, 178.786, -4.134, 68.326]
    desc_pos2 = [213.812, -1.440, 47.311, 177.410, 0.166, 68.946]
    desc_pos3 = [444.342, -12.723, 82.470, -177.701, -1.325, 65.151]
    epos1 = [0.001, 0.000, 0.000, 0.000]
    epos2 = [299.977, 0.000, 0.000, 0.000]
    epos3 = [399.969, 0.000, 0.000, 0.000]
    offset_pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SetExAxisRobotPlan(0)
    print(f"SetExAxisRobotPlan rtn is {rtn}")
    time.sleep(1)
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos1,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos1,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 1 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos2,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos2,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 2 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos3,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos3,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 3 rtn is {rtn}")
    time.sleep(8)
    robot.CloseRPC()

Configuração do Tempo de Conclusão do Posicionamento do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetExAxisCmdDoneTime(time)``"
    "Descrição", "Configuração do tempo de conclusão do posicionamento do eixo de extensão UDP"
    "Parâmetros Obrigatórios", "- ``time``: Tempo de conclusão do posicionamento [ms]"
    "Parâmetros Padrão", "Nenhum"
    "Valor de Retorno", "Código de erro: Sucesso-0   Falha - errcode"