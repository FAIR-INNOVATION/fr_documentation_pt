Fundamentos do Robô
==========================

.. toctree::
    :maxdepth: 5

Instanciar o Robô
++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``RPC(ip)``"
    "Descrição", "Instancia um objeto robô"
    "Parâmetros obrigatórios", "- ``ip``: Endereço IP do robô, o IP padrão de fábrica é `192.168.58.2`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Sucesso: retorna um objeto robô
    - Falha: o objeto criado é destruído"

Fechar Conexão RPC
++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``CloseRPC()``"
    "Descrição", "Fecha a conexão RPC"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Nenhum"

Consultar Número da Versão do SDK
++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSDKVersion()``"
    "Descrição", "Consulta o número da versão do SDK"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``sdk``: Número da versão do SDK, número da versão do controlador"

Obter IP do Controlador
+++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetControllerIP()``"
    "Descrição", "Consulta o IP do controlador"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``ip``: IP do controlador"

Controlar a Entrada ou Saída do Modo de Ensino por Arrasto do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``DragTeachSwitch(state)``"
    "Descrição", "Controla a entrada ou saída do modo de ensino por arrasto do robô"
    "Parâmetros obrigatórios", "- ``state``: 1-entrar no modo de ensino por arrasto, 0-sair do modo de ensino por arrasto"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Verificar se o Robô está em Modo de Arrasto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``IsInDragTeach()``"
    "Descrição", "Verifica se o robô está em modo de ensino por arrasto"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``state``: 0-não está em modo de ensino por arrasto, 1-está em modo de ensino por arrasto"

Controlar a Habilitação ou Desabilitação do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``RobotEnable(state)``"
    "Descrição", "Controla a habilitação ou desabilitação do robô"
    "Parâmetros obrigatórios", "- ``state``: 1-habilitar, 0-desabilitar"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Controlar a Comutação entre Modo Manual e Automático do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``Mode(state)``"
    "Descrição", "Controla a comutação entre modo manual e automático do robô"
    "Parâmetros obrigatórios", "- ``state``: 0-modo automático, 1-modo manual"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Desligar o Sistema Operacional do Robô
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ShutDownRobotOS()``"
    "Descrição", "Desliga o sistema operacional do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Inicializar Parâmetros de Log
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoggerInit(output_model=1, file_path="", file_num=5)``"
    "Descrição", "Inicializa os parâmetros de log"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``output_model``: Modo de saída, 0-saída direta; 1-saída com buffer; 2-saída assíncrona, padrão 1
    - ``file_path``: Caminho + nome do arquivo de salvamento, o nome deve estar no formato xxx.log, ex: /home/fr/linux/fairino.log. Padrão é o caminho do programa em execução, nome padrão: fairino_ano+mês+data.log (ex: fairino_2024_03_13.log);
    - ``file_num``: Número de arquivos armazenados em rotação, 1~20, padrão 5. Limite máximo de 50 MB por arquivo;"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Nível de Filtro de Log
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetLoggerLevel(lvl=1)``"
    "Descrição", "Define o nível de filtro de log"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "- ``lvl``: Nível de filtro, quanto menor o valor, menos logs são exibidos, 1-erro, 2-aviso, 3-informação, 4-depuração, padrão 1"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Controle Básico do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    error, version = robot.GetSDKVersion()
    print(f"SDK version: {version}")
    error, ip = robot.GetControllerIP()
    print(f"controller ip: {ip}")
    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(state=1)
    time.sleep(1)
    error, state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.DragTeachSwitch(state=0)
    time.sleep(1)
    error, state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.RobotEnable(0)
    time.sleep(3)
    robot.RobotEnable(1)
    robot.Mode(0)
    time.sleep(1)
    robot.Mode(1)
    robot.CloseRPC()

Obter Versão do Software do Robô
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSoftwareVersion()``"
    "Descrição", "Obtém a versão do software do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``robotModel``: Modelo do robô
    - ``webVersion``: Versão web
    - ``controllerVersion``: Versão do controlador"

Obter Informações da Versão do Hardware do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSlaveHardVersion()``"
    "Descrição", "Obtém as informações da versão do hardware do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``ctrlBoxBoardVersion``: Versão da caixa de controle
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

Obter Informações da Versão do Firmware do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSlaveFirmVersion()``"
    "Descrição", "Obtém as informações da versão do firmware do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``ctrlBoxBoardVersion``: Versão da caixa de controle
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

Exemplo de Código para Obter Versões de Software e Firmware do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn, robotModel, webversion, controllerVersion = robot.GetSoftwareVersion()
    print(f"Getsoftwareversion rtn is: {rtn}")
    print(f"robotmodel is: {robotModel}, webversion is: {webversion}, controllerVersion is: {controllerVersion}\n")
    rtn, ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion = robot.GetHardwareversion()
    print(f"GetHardwareversion rtn is: {rtn}")
    print(f"GetHardwareversion get hardware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    rtn, ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion = robot.GetFirmwareVersion()
    print(f"GetFirmwareversion rtn is: {rtn}")
    print(f"GetFirmwareversion get firmware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    robot.CloseRPC()