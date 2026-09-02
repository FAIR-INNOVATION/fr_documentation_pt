E/S do Robô
============

.. toctree::
    :maxdepth: 5

Definir Saída Digital da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDO(id, status, smooth=0, block=0)``"
    "Descrição", "Define a saída digital da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~15];
    - ``status``: 0-desligado, 1-ligado;"
    "Parâmetros padrão", "- ``smooth``: 0-não suave, 1-suave, padrão 0;
    - ``block``: 0-bloqueante, 1-não bloqueante, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Saída Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolDO(id, status, smooth=0, block=0)``"
    "Descrição", "Define a saída digital da ferramenta"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];
    - ``status``: 0-desligado, 1-ligado;"
    "Parâmetros padrão", "- ``smooth``: 0-não suave, 1-suave;
    - ``block``: 0-bloqueante, 1-não bloqueante."
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Saída Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetAO(id, value, block=0)``"
    "Descrição", "Define a saída analógica da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];
    - ``value``: Percentagem do valor de corrente ou tensão, intervalo [0~100%] correspondendo à corrente [0~20mA] ou tensão [0~10V];"
    "Parâmetros padrão", "- ``block``: [0]-bloqueante, [1]-não bloqueante, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Saída Analógica da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolAO(id, value, block=0)``"
    "Descrição", "Define a saída analógica da ferramenta"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0];
    - ``value``: Percentagem do valor de corrente ou tensão, intervalo [0~100%] correspondendo à corrente [0~20mA] ou tensão [0~10V];"
    "Parâmetros padrão", "- ``block``: [0]-bloqueante, [1]-não bloqueante, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Configurar Saídas Digitais e Analógicas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0
    block = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    status = 0
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    robot.CloseRPC()

Obter Entrada Digital da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDI(id, block=0)``"
    "Descrição", "Obtém a entrada digital da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~15];"
    "Parâmetros padrão", "- ``block``: 0-bloqueante, 1-não bloqueante, padrão 0"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``di``: 0-nível baixo, 1-nível alto"

Obter Entrada Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolDI(id, block=0)``"
    "Descrição", "Obtém a entrada digital da ferramenta"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];"
    "Parâmetros padrão", "- ``block``: 0-bloqueante, 1-não bloqueante, padrão 0"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro
    - ``di``: 0-nível baixo, 1-nível alto"

Obter Entrada Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAI(id, block=0)``"
    "Descrição", "Obtém a entrada analógica da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];"
    "Parâmetros padrão", "- ``block``: 0-bloqueante, 1-não bloqueante, padrão 0"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``value``: Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]"

Obter Entrada Analógica da Ferramenta
+++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolAI(id, block=0)``"
    "Descrição", "Obtém a entrada analógica da extremidade"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0];"
    "Parâmetros padrão", "- ``block``: 0-bloqueante, 1-não bloqueante, padrão 0"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``value``: Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V]"

Obter Estado do Botão de Gravação de Ponto da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetAxlePointRecordBtnState()``"
    "Descrição", "Obtém o estado do botão de gravação de ponto da extremidade do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``buttonstatus``: Estado do botão, 0-pressionado, 1-solto"

Obter Estado de Saída DO da Extremidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolDO()``"
    "Descrição", "Obtém o estado de saída DO da extremidade do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``do_state``: Estado de saída DO, do0~do1 correspondem aos bits 1~2, começando no bit 0"

Obter Estado de Saída DO do Controlador do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDO()``"
    "Descrição", "Obtém o estado de saída DO do controlador do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``do_state_h``: Estado de saída DO, co0~co7 correspondem aos bits 0~7 do_state_l Estado de saída DO, do0~do7 correspondem aos bits 0~7"

Exemplo de Código para Obter Estado DI e DO do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    block = 0
    error, di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error, tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error, ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}")
    error, tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error, button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error, tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error, [do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state high: {do_state_h}")
    print(f"DO state low: {do_state_l}")
    robot.CloseRPC()

Aguardar Entrada Digital da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitDI(id, status, maxtime, opt)``"
    "Descrição", "Aguarda a entrada digital da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~15];
    - ``status``: 0-desligado, 1-ligado;
    - ``maxtime``: Tempo máximo de espera, em [ms];
    - ``opt``: Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Aguardar Entrada Digital Múltipla da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitMultiDI(mode, id, status, maxtime, opt)``"
    "Descrição", "Aguarda a entrada digital múltipla da caixa de controle"
    "Parâmetros obrigatórios", "- ``mode``: [0]-E lógico múltiplo, [1]-OU lógico múltiplo;
    - ``id``: Número da E/S, bits 0~7 correspondem a DI0~DI7, bits 8~15 correspondem a CI0~CI7;
    - ``status``: bits 0~7 correspondem ao estado de DI0~DI7, bits 8~15 correspondem ao estado dos bits de estado de CI0~CI7 [0]-desligado, [1]-ligado;
    - ``maxtime``: Tempo máximo de espera, em [ms];
    - ``opt``: Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente."
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Aguardar Entrada Digital da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitToolDI(id, status, maxtime, opt)``"
    "Descrição", "Aguarda a entrada digital da extremidade"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];
    - ``status``: 0-desligado, 1-ligado;
    - ``maxtime``: Tempo máximo de espera, em [ms];
    - ``opt``: Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Aguardar Entrada Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitAI(id, sign, value, maxtime, opt)``"
    "Descrição", "Aguarda a entrada analógica da caixa de controle"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0~1];
    - ``sign``: 0-maior que, 1-menor que
    - ``value``: Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V];
    - ``maxtime``: Tempo máximo de espera, em [ms];
    - ``opt``: Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Aguardar Entrada Analógica da Ferramenta
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``WaitToolAI(id, sign, value, maxtime, opt)``"
    "Descrição", "Aguarda a entrada analógica da extremidade"
    "Parâmetros obrigatórios", "- ``id``: Número da E/S, intervalo [0];
    - ``sign``: 0-maior que, 1-menor que
    - ``value``: Percentagem do valor de corrente ou tensão de entrada, intervalo [0~100] correspondendo à corrente [0~20mA] ou tensão [0~10V];
    - ``maxtime``: Tempo máximo de espera, em [ms];
    - ``opt``: Estratégia após timeout, 0-parar o programa e indicar timeout, 1-ignorar indicação de timeout e continuar a execução do programa, 2-esperar indefinidamente"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Aguardar Sinais de Entrada Digital e Analógica da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0
    block = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    status = 0
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    block = 0
    error, di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error, tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error, ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}")
    error, tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error, button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error, tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error, [do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state high: {do_state_h}")
    print(f"DO state low: {do_state_l}")
    rtn = robot.WaitDI(0, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitMultiDI(1, 3, 3, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolDI(1, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    robot.CloseRPC()

Definir se a Saída DO da Caixa de Controle é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetCtlBoxDO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída DO da caixa de controle é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída AO da Caixa de Controle é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetCtlBoxDO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída AO da caixa de controle é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída DO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetAxleDO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída DO da ferramenta de extremidade é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída AO da Ferramenta de Extremidade é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetAxleAO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída AO da ferramenta de extremidade é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída DO Estendida é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetExtDO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída DO estendida é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída AO Estendida é Reiniciada Após Parada/Pausa
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetExtAO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída AO estendida é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir se a Saída DO do SmartTool é Reiniciada Após Parada/Pausa
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetOutputResetSmartToolDO(resetFlag, reloadFlag)``"
    "Descrição", "Define se a saída DO do SmartTool é reiniciada após parada/pausa"
    "Parâmetros obrigatórios", "
    - ``resetFlag``: 0-não reiniciar; 1-reiniciar
    - ``reloadFlag``: Se recarregar após retomar da pausa, 0-não carregar; 1-carregar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código para Reinicialização de Saída Após Parada/Pausa do Programa LUA
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    for i in range(16):
        robot.SetDO(i, 1, 0, 0)
        time.sleep(0.2)
    resetFlag = 0
    resumeReloadFlag = 0
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag)
    robot.ProgramLoad("test.lua")
    robot.ProgramRun()
    time.sleep(2)
    robot.PauseMotion()
    time.sleep(2)
    robot.ResumeMotion()
    time.sleep(2)
    robot.CloseRPC()
    return 0

Definir Função da Porta CI Configurável
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDIConfig(config)``"
    "Descrição", "Define a função da porta CI configurável"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função CI0-CI7, 0-nenhum;1-sucesso de abertura de arco;2-preparação da soldadora;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
      8-pausa/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem do trabalho;12-comutação manual/automático;
      13-sucesso na busca de posição do fio de solda;14-interrupção de movimento;15-iniciar programa principal;16-iniciar retrocesso;17-confirmação de início;
      18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
      22-modo de redução de nível 1;23-modo de redução de nível 2;24-modo de redução de nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
      27-ativar arrasto auxiliar;28-desativar arrasto auxiliar;29-ativar/desativar arrasto auxiliar;30-limpar todos os erros;
      31-comutação manual/automático (nível alto/baixo);32-ativar;33-desativar;34-ativar/desativar (borda de subida/descida);35-iniciar/terminar rastreamento de ponto fixo
      36-Entrar em movimento com velocidade de segurança;37-Bloqueio de arrasto por anel de corrente;38-Bloqueio assistido por sensor de força"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Função da Porta CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDIConfig()``"
    "Descrição", "Obtém a função da porta CI configurável da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função CI0-CI7, 0-nenhum;1-sucesso de abertura de arco;2-preparação da soldadora;3-detecção de esteira;4-pausa;5-retomar;6-iniciar;7-parar;
      8-pausa/retomar;9-iniciar/parar;10-arrasto com pedal;11-mover para origem do trabalho;12-comutação manual/automático;
      13-sucesso na busca de posição do fio de solda;14-interrupção de movimento;15-iniciar programa principal;16-iniciar retrocesso;17-confirmação de início;
      18-sinal de detecção fotoelétrica X;19-sinal de detecção fotoelétrica Y;20-sinal de parada de emergência externa 1;21-sinal de parada de emergência externa 2;
      22-modo de redução de nível 1;23-modo de redução de nível 2;24-modo de redução de nível 3 (parada);25-retomar soldagem;26-terminar soldagem;
      27-ativar arrasto auxiliar;28-desativar arrasto auxiliar;29-ativar/desativar arrasto auxiliar;30-limpar todos os erros;
      31-comutação manual/automático (nível alto/baixo);32-ativar;33-desativar;34-ativar/desativar (borda de subida/descida);35-iniciar/terminar rastreamento de ponto fixo
      36-Entrar em movimento com velocidade de segurança;37-Bloqueio de arrasto por anel de corrente;38-Bloqueio assistido por sensor de força
      201-Sinal de entrada de parada de emergência externa 1-dois canais; 202-Sinal de entrada de parada de emergência externa 2-dois canais; 203-Modo reduzido de nível 1-dois canais;
      204-Modo reduzido de nível 2-dois canais; 205-Modo reduzido de nível 3-dois canais; 206-Parada normal-dois canais; 207-Parede de segurança 1-dois canais; 208-Parede de segurança 2-dois canais;
      209-Parede de segurança 3-dois canais; 210-Parede de segurança 4-dois canais; 211-Parede de segurança 5-dois canais; 212-Parede de segurança 6-dois canais; 213-Parede de segurança 7-dois canais;
      214-Parede de segurança 8-dois canais; 215-Reinicialização de parada de segurança-dois canais;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Função da Porta CO Configurável
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDOConfig(config)``"
    "Descrição", "Define a função da porta CO configurável"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função CO0-CO7, 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pulverização;4-limpeza do bico de pulverização;5-sinal de gás;6-sinal de abertura de arco;7-avanço do fio por ponto;
      8-retrocesso do fio;9-porta de entrada JOB1;10-porta de entrada JOB2;11-porta de entrada JOB3;12-controle de iniciar/parar esteira;13-robô em pausa;14-origem do trabalho alcançada;
      15-área de interferência alcançada;16-controle de iniciar/parar busca de posição do fio;17-robô iniciado com sucesso;18-iniciar/parar programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1-seguro;
      21-sinal de saída de parada de emergência 2-seguro;22-parada/início de execução do script LUA;23-saída de estado seguro-seguro;24-saída de estado de parada protetiva-seguro;
      25-robô em movimento-seguro;26-robô em modo reduzido-seguro;27-robô em modo não reduzido-seguro;28-robô não parado;29-erro do robô-erro de ponto de comando;
      30-erro do robô-erro do driver;31-erro do robô-erro de limite flexível excedido;32-erro do robô-erro de colisão;33-erro do robô-erro de número de escravas ativas;
      34-erro do robô-erro de escrava;35-erro do robô-erro de E/S;36-erro do robô-erro da garra;37-erro do robô-erro de arquivo;38-erro do robô-erro de pose singular;
      39-erro do robô-erro de comunicação do driver;40-erro do robô-erro de parâmetro;41-erro do robô-erro de limite flexível do eixo externo excedido;42-aviso do robô-aviso;
      43-aviso do robô-aviso de porta de segurança;44-aviso do robô-aviso de movimento;45-aviso do robô-aviso de área de interferência;46-aviso do robô-aviso de parede de segurança;
      47-estado ativado;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Função da Porta CO Configurável
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDOConfig()``"
    "Descrição", "Obtém a função da porta CO configurável"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função CO0-CO7, 0-nenhum;1-erro do robô;2-robô em movimento;3-iniciar/parar pulverização;4-limpeza do bico de pulverização;5-sinal de gás;6-sinal de abertura de arco;7-avanço do fio por ponto;
      8-retrocesso do fio;9-porta de entrada JOB1;10-porta de entrada JOB2;11-porta de entrada JOB3;12-controle de iniciar/parar esteira;13-robô em pausa;14-origem do trabalho alcançada;
      15-área de interferência alcançada;16-controle de iniciar/parar busca de posição do fio;17-robô iniciado com sucesso;18-iniciar/parar programa;19-modo automático/manual;20-sinal de saída de parada de emergência 1-seguro;
      21-sinal de saída de parada de emergência 2-seguro;22-parada/início de execução do script LUA;23-saída de estado seguro-seguro;24-saída de estado de parada protetiva-seguro;
      25-robô em movimento-seguro;26-robô em modo reduzido-seguro;27-robô em modo não reduzido-seguro;28-robô não parado;29-erro do robô-erro de ponto de comando;
      30-erro do robô-erro do driver;31-erro do robô-erro de limite flexível excedido;32-erro do robô-erro de colisão;33-erro do robô-erro de número de escravas ativas;
      34-erro do robô-erro de escrava;35-erro do robô-erro de E/S;36-erro do robô-erro da garra;37-erro do robô-erro de arquivo;38-erro do robô-erro de pose singular;
      39-erro do robô-erro de comunicação do driver;40-erro do robô-erro de parâmetro;41-erro do robô-erro de limite flexível do eixo externo excedido;42-aviso do robô-aviso;
      43-aviso do robô-aviso de porta de segurança;44-aviso do robô-aviso de movimento;45-aviso do robô-aviso de área de interferência;46-aviso do robô-aviso de parede de segurança;
      47-estado ativado;48-elevação automática durante desconexão;49-aviso de interferência do cubo 1;50-aviso de interferência do cubo 2;51-aviso de interferência do cubo 3;52-aviso de interferência do cubo 4;
      201-Sinal de saída de parada de emergência 1-dois canais; 202-Sinal de saída de parada de emergência 2-dois canais; 203-Saída de status de segurança-dois canais; 204-Saída de status de parada protetiva-dois canais; 205-Robô em movimento-dois canais;
	  206-Robô em modo reduzido-dois canais; 207-Robô em modo não reduzido-dois canais;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolDIConfig(config)``"
    "Descrição", "Define a função da porta End-CI configurável da extremidade"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função End CI0-CI1, 0-nenhum;1-chave da ferramenta de arrasto para ensino;2-sinal de gravação de ponto;3-comutação manual/automático (sinal de pulso);4-iniciar/parar gravação TPD;5-pausar movimento;
      6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto auxiliar do sensor de força;12-desativar arrasto auxiliar do sensor de força;
      13-ativar/desativar arrasto auxiliar do sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-movimento PTP para origem do trabalho;17-interrupção de movimento, parar movimento atual com base no sinal;
      18-iniciar programa principal;19-iniciar retrocesso;20-confirmação de início;21-retomar soldagem;22-terminar soldagem;23-limpar erro;24-comutação manual/automático (nível alto/baixo)
      25-ativar;26-desativar;27-ativar/desativar;28-sinal de iniciar/parar rastreamento servo a laser;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Função da Porta End-CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolDIConfig()``"
    "Descrição", "Obtém a função da porta End-CI configurável da extremidade"
    "Parâmetros obrigatórios", "
    - ``config``: Array de códigos de função End CI0-CI1, 0-nenhum;1-chave da ferramenta de arrasto para ensino;2-sinal de gravação de ponto;3-comutação manual/automático (sinal de pulso);4-iniciar/parar gravação TPD;5-pausar movimento;
      6-retomar movimento;7-iniciar;8-parar;9-pausar/retomar;10-iniciar/parar;11-ativar arrasto auxiliar do sensor de força;12-desativar arrasto auxiliar do sensor de força;
      13-ativar/desativar arrasto auxiliar do sensor de força;14-sinal de detecção a laser X;15-sinal de detecção a laser Y;16-movimento PTP para origem do trabalho;17-interrupção de movimento, parar movimento atual com base no sinal;
      18-iniciar programa principal;19-iniciar retrocesso;20-confirmação de início;21-retomar soldagem;22-terminar soldagem;23-limpar erro;24-comutação manual/automático (nível alto/baixo)
      25-ativar;26-desativar;27-ativar/desativar;28-sinal de iniciar/parar rastreamento servo a laser;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Estado Ativo do CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDIConfigLevel(config)``"
    "Descrição", "Define o estado ativo do CI configurável da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado Ativo do CI Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDIConfigLevel()``"
    "Descrição", "Obtém o estado ativo do CI configurável da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Estado Ativo do CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetDOConfigLevel(config)``"
    "Descrição", "Define o estado ativo do CO configurável da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado Ativo do CO Configurável da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetDOConfigLevel()``"
    "Descrição", "Obtém o estado ativo do CO configurável da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CO0-CO7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Estado Ativo do CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetToolDIConfigLevel(config)``"
    "Descrição", "Define o estado ativo do CI configurável da extremidade"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado Ativo do CI Configurável da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetToolDIConfigLevel()``"
    "Descrição", "Obtém o estado ativo do CI configurável da extremidade"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas CI0-CI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Estado Ativo do DI Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetStandardDILevel(config)``"
    "Descrição", "Define o estado ativo do DI padrão da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado Ativo do DI Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetStandardDILevel()``"
    "Descrição", "Obtém o estado ativo do DI padrão da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas DI0-DI7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Estado Ativo do DO Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetStandardDOLevel(config)``"
    "Descrição", "Define o estado ativo do DO padrão da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Estado Ativo do DO Padrão da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetStandardDOLevel()``"
    "Descrição", "Obtém o estado ativo do DO padrão da caixa de controle"
    "Parâmetros obrigatórios", "
    - ``config``: Array de estado ativo das portas DO0-DO7; 0-ativo em nível alto; 1-ativo em nível baixo"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK de Configuração de E/S
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')


    def TestIOConfig(self):
        # Definir e obter configuração DI
        setDIConfig = [1, 2, 3, 4, 5, 6, 7, 8]
        getDIConfig = [0] * 8
        rtn = robot.SetDIConfig(setDIConfig)
        print(f"SetDIConfig rtn is {rtn}")
        rtn, getDIConfig = robot.GetDIConfig()
        print(f"GetDIConfig rtn is {rtn}, value is {getDIConfig[0]} {getDIConfig[1]} {getDIConfig[2]} {getDIConfig[3]} {getDIConfig[4]} {getDIConfig[5]} {getDIConfig[6]} {getDIConfig[7]}")

        # Definir e obter configuração DO
        setDOConfig = [9, 10, 11, 12, 13, 14, 15, 16]
        getDOConfig = [0] * 8
        rtn = robot.SetDOConfig(setDOConfig)
        print(f"SetDOConfig rtn is {rtn}")
        rtn, getDOConfig = robot.GetDOConfig()
        print(f"GetDOConfig rtn is {rtn}, value is {getDOConfig[0]} {getDOConfig[1]} {getDOConfig[2]} {getDOConfig[3]} {getDOConfig[4]} {getDOConfig[5]} {getDOConfig[6]} {getDOConfig[7]}")

        # Definir e obter configuração DI da ferramenta
        setToolDIConfig = [17, 18]
        getToolDIConfig = [0] * 2
        rtn = robot.SetToolDIConfig(setToolDIConfig)
        print(f"SetToolDIConfig rtn is {rtn}")
        rtn, getToolDIConfig = robot.GetToolDIConfig()
        print(f"GetToolDIConfig rtn is {rtn}, value is {getToolDIConfig[0]} {getToolDIConfig[1]}")

        # Definir e obter configuração de nível DI (0: nível baixo ativo, 1: nível alto ativo)
        setDIConfigLevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getDIConfigLevel = [0] * 8
        rtn = robot.SetDIConfigLevel(setDIConfigLevel)
        print(f"SetDIConfigLevel rtn is {rtn}")
        rtn, getDIConfigLevel = robot.GetDIConfigLevel()
        print(f"GetDIConfigLevel rtn is {rtn}, value is {getDIConfigLevel[0]} {getDIConfigLevel[1]} {getDIConfigLevel[2]} {getDIConfigLevel[3]} {getDIConfigLevel[4]} {getDIConfigLevel[5]} {getDIConfigLevel[6]} {getDIConfigLevel[7]}")

        # Definir e obter configuração de nível DO (0: nível baixo ativo, 1: nível alto ativo)
        setDOConfigLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getDOConfigLevel = [0] * 8
        rtn = robot.SetDOConfigLevel(setDOConfigLevel)
        print(f"SetDOConfigLevel rtn is {rtn}")
        rtn, getDOConfigLevel = robot.GetDOConfigLevel()
        print(f"GetDOConfigLevel rtn is {rtn}, value is {getDOConfigLevel[0]} {getDOConfigLevel[1]} {getDOConfigLevel[2]} {getDOConfigLevel[3]} {getDOConfigLevel[4]} {getDOConfigLevel[5]} {getDOConfigLevel[6]} {getDOConfigLevel[7]}")

        # Definir e obter configuração de nível DI da ferramenta
        setToolDIConfigLevel = [1, 0]
        getToolDIConfigLevel = [0] * 2
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel)
        print(f"SetToolDIConfigLevel rtn is {rtn}")
        rtn, getToolDIConfigLevel = robot.GetToolDIConfigLevel()
        print(f"GetToolDIConfigLevel rtn is {rtn}, value is {getToolDIConfigLevel[0]} {getToolDIConfigLevel[1]}")

        # Definir e obter configuração de nível DI padrão
        setStandardDILevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getStandardDILevel = [0] * 8
        rtn = robot.SetStandardDILevel(setStandardDILevel)
        print(f"SetStandardDILevel rtn is {rtn}")
        rtn, getStandardDILevel = robot.GetStandardDILevel()
        print(f"GetStandardDILevel rtn is {rtn}, value is {getStandardDILevel[0]} {getStandardDILevel[1]} {getStandardDILevel[2]} {getStandardDILevel[3]} {getStandardDILevel[4]} {getStandardDILevel[5]} {getStandardDILevel[6]} {getStandardDILevel[7]}")

        # Definir e obter configuração de nível DO padrão
        setStandardDOLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getStandardDOLevel = [0] * 8
        rtn = robot.SetStandardDOLevel(setStandardDOLevel)
        print(f"SetStandardDOLevel rtn is {rtn}")
        rtn, getStandardDOLevel = robot.GetStandardDOLevel()
        print(f"GetStandsrdDOLevel rtn is {rtn}, value is {getStandardDOLevel[0]} {getStandardDOLevel[1]} {getStandardDOLevel[2]} {getStandardDOLevel[3]} {getStandardDOLevel[4]} {getStandardDOLevel[5]} {getStandardDOLevel[6]} {getStandardDOLevel[7]}")

        # Aguardar 2 segundos
        time.sleep(2)

        # Fechar conexão
        robot.CloseRPC()
        time.sleep(1)

    # Chamar função de teste
    TestIOConfig(robot)