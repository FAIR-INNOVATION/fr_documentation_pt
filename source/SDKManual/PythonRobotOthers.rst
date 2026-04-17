Outras Interfaces
===========================

.. toctree::
    :maxdepth: 5

Obter Chave Pública SSH
++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSSHKeygen()``"
    "Descrição", "Obtém a chave pública SSH"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``keygen``: Chave pública"

Enviar Comando SCP
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetSSHScpCmd(mode, sshname, sship, usr_file_url, robot_file_url)``"
    "Descrição", "Envia comando SCP"
    "Parâmetros obrigatórios", "- ``mode``: 0-envio (computador host -> controlador), 1-download (controlador -> computador host)
    - ``sshname``: Nome de usuário do computador host
    - ``sship``: Endereço IP do computador host
    - ``usr_file_url``: Caminho do arquivo no computador host
    - ``robot_file_url``: Caminho do arquivo no controlador do robô"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Calcular o Valor MD5 de um Arquivo em um Caminho Especificado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ComputeFileMD5(file_path)``"
    "Descrição", "Calcula o valor MD5 de um arquivo em um caminho especificado"
    "Parâmetros obrigatórios", "- ``file_path``: Caminho do arquivo incluindo o nome do arquivo, o caminho padrão da pasta Traj é: /fruser/traj/, ex: /fruser/traj/trajHelix_aima_1.txt"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``md5``: Valor MD5 do arquivo"

Exemplo de Código de Comandos SSH e MD5 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    file_path = "/fruser/airlab.lua"
    md5 = ""
    emerg_state = 0
    si0_state = 0
    si1_state = 0
    sdk_com_state = 0
    ssh_keygen = ""
    retval, ssh_keygen = robot.GetSSHKeygen()
    print(f"GetSSHKeygen retval is: {retval}")
    print(f"ssh key is: {ssh_keygen}")
    ssh_name = "fr"
    ssh_ip = "192.168.58.45"
    ssh_route = "/home/fr"
    ssh_robot_url = "/root/robot/dhpara.config"
    retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url)
    print(f"SetSSHScpCmd retval is: {retval}")
    print(f"robot url is: {ssh_robot_url}")
    error, md5 = robot.ComputeFileMD5(file_path)
    print(f"md5 is: {md5}")
    robot.CloseRPC()

Definir Período de Feedback da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotRealtimeStateSamplePeriod(period)``"
    "Descrição", "Define o período de feedback da porta 20004 do robô"
    "Parâmetros obrigatórios", "- ``period``: Período de feedback da porta 20004 do robô (ms)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Período de Feedback da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotRealtimeStateSamplePeriod()``"
    "Descrição", "Obtém o período de feedback da porta 20004 do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``period``: Período de feedback da porta 20004 do robô (ms)"

Exemplo de Código de Configuração do Período de Feedback de Estado da Porta 20004 do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.SetRobotRealtimeStateSamplePeriod(10)
    error, getPeriod = robot.GetRobotRealtimeStateSamplePeriod()
    print(f"period is {getPeriod}")
    time.sleep(1)
    robot.CloseRPC()

Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SoftwareUpgrade(filePath, block)``"
    "Descrição", "Atualização de software do robô"
    "Parâmetros obrigatórios", "- ``filePath``: Caminho completo do pacote de atualização de software
    - ``block``: Se bloqueia até a conclusão da atualização true: bloqueante; false: não bloqueante"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro"

Obter Estado da Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetSoftwareUpgradeState()``"
    "Descrição", "Obtém o estado da atualização de software do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``state``: Estado da atualização do pacote de software do robô, 0: ocioso ou enviando pacote de atualização, 1~100: percentagem de conclusão da atualização, -1: falha na atualização do software, -2: falha na verificação, -3: falha na verificação da versão, -4: falha na descompactação, -5: falha na atualização da configuração do usuário, -6: falha na atualização da configuração do periférico, -7: falha na atualização da configuração do eixo estendido, -8: falha na atualização da configuração do robô, -9: falha na atualização da configuração dos parâmetros DH"

Exemplo de Código de Atualização de Software do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    error = robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", False)
    print(f"SoftwareUpgrade error is {error}")
    while True:
        curState = robot.GetSoftwareUpgradeState()
        print(f"upgrade state is {curState}")
        time.sleep(3)
    robot.CloseRPC()

Download do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PointTableDownLoad(point_table_name, save_file_path)``"
    "Descrição", "Download do banco de dados da tabela de pontos"
    "Parâmetros obrigatórios", "- ``point_table_name``: Nome da tabela de pontos a ser baixada pointTable1.db;
    - ``save_file_path``: Caminho de armazenamento para download da tabela de pontos C://test/;"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Upload do Banco de Dados da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PointTableUpLoad(point_table_file_path)``"
    "Descrição", "Upload do banco de dados da tabela de pontos"
    "Parâmetros obrigatórios", "- ``point_table_file_path``: Caminho completo do arquivo da tabela de pontos para upload C://test/pointTable1.db"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Atualização do Arquivo Lua da Tabela de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "Descrição", "Atualização do arquivo Lua da tabela de pontos"
    "Parâmetros obrigatórios", "- ``point_table_name``: Nome da tabela de pontos a ser alternada pointTable1.db, quando a tabela de pontos estiver vazia, ou seja "", indica que o programa Lua será atualizado para o programa inicial sem aplicação da tabela de pontos
    - ``lua_file_name``: Nome do arquivo Lua a ser atualizado testPointTable.lua"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Operação da Tabela de Pontos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    save_path = "D://zDOWN/"
    point_table_name = "point_table_FR5.db"
    rtn = robot.PointTableDownLoad(point_table_name, save_path)
    print(f"download : {point_table_name} fail: {rtn}")
    upload_path = "D://zDOWN/point_table_FR5.db"
    rtn = robot.PointTableUpLoad(upload_path)
    print(f"retval is: {rtn}")
    point_tablename = "point_table_FR5.db"
    lua_name = "test0610.lua"
    rtn, error = robot.PointTableUpdateLua(point_tablename, lua_name)
    print(f"retval is: {rtn}")
    robot.CloseRPC()

Download de Logs do Controlador
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``RbLogDownload(savePath)``"
    "Descrição", "Download de logs do controlador"
    "Parâmetros obrigatórios", "- ``savePath``: Caminho para salvar o arquivo D://zDown/"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Download de Todas as Fontes de Dados
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``AllDataSourceDownload(savePath)``"
    "Descrição", "Download de todas as fontes de dados"
    "Parâmetros obrigatórios", "- ``savePath``: Caminho para salvar o arquivo D://zDown/"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Download do Pacote de Backup de Dados
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``DataPackageDownload(savePath)``"
    "Descrição", "Download do pacote de backup de dados"
    "Parâmetros obrigatórios", "- ``savePath``: Caminho para salvar o arquivo D://zDown/"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Download de Dados do Controlador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.RbLogDownload("D://zDOWN/")
    print(f"RbLogDownload rtn is {rtn}")
    rtn = robot.AllDataSourceDownload("D://zDOWN/")
    print(f"AllDataSourceDownload rtn is {rtn}")
    rtn = robot.DataPackageDownload("D://zDOWN/")
    print(f"DataPackageDownload rtn is {rtn}")
    robot.CloseRPC()

Definir Atualização do Codificador
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetEncoderUpgrade(path)``"
    "Descrição", "Define a atualização do codificador"
    "Parâmetros obrigatórios", "- ``path``: Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Atualização de Firmware das Juntas
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetJointFirmwareUpgrade(type, path)``"
    "Descrição", "Define a atualização de firmware das juntas"
    "Parâmetros obrigatórios", "- ``type``: Tipo de arquivo de atualização; 1-atualização de firmware; 2-atualização do arquivo de configuração do escravo
    - ``path``: Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Atualização de Firmware da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetCtrlFirmwareUpgrade(type, path)``"
    "Descrição", "Define a atualização de firmware da caixa de controle"
    "Parâmetros obrigatórios", "- ``type``: Tipo de arquivo de atualização; 1-atualização de firmware; 2-atualização do arquivo de configuração do escravo
    - ``path``: Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Atualização de Firmware da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetEndFirmwareUpgrade(type, path)``"
    "Descrição", "Define a atualização de firmware da extremidade"
    "Parâmetros obrigatórios", "- ``type``: Tipo de arquivo de atualização; 1-atualização de firmware; 2-atualização do arquivo de configuração do escravo
    - ``path``: Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Atualização do Arquivo de Configuração de Parâmetros Completos das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``JointAllParamUpgrade(path)``"
    "Descrição", "Atualização do arquivo de configuração de parâmetros completos das juntas"
    "Parâmetros obrigatórios", "- ``path``: Caminho completo do pacote de atualização local (D://zUP/XXXXX.bin)"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Atualização de Firmware dos Escravos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    robot.RobotEnable(0)
    time.sleep(0.2)
    rtn = robot.JointAllParamUpgrade("D://zUP/MT/joint0603/jointallparameters.db")
    print(f"robot JointAllParamUpgrade rtn is {rtn}")
    rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Cbd_Asix_V2.0.bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Axle_Asix_V2.4.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    robot.SetSysServoBootMode()
    time.sleep(0.2)
    rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/MT/FR_CTRL_PRIMCU_FV201412_MAIN_U4_T01_20250630(MT).bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/MT/FR_END_FV2010010_MAIN_U1_T01_20250603.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/MT/FR_SERVO_FV504215_MAIN_U7_T07_20250603.bin")
    print(f"robot SetJointFirmwareUpgrade rtn is {rtn}")
    robot.CloseRPC()

Atualização do Sistema Operacional do Robô (Caixa de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``KernelUpgrade(filePath)``"
    "Descrição", "Atualização do sistema operacional do robô (caixa de controle LA)"
    "Parâmetros obrigatórios", "- ``filePath``: Caminho completo do pacote de atualização do sistema operacional"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Resultado da Atualização do Sistema Operacional do Robô (Caixa de Controle LA)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetKernelUpgradeResult()``"
    "Descrição", "Obtém o resultado da atualização do sistema operacional do robô (caixa de controle LA)"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Geração de Logs MCU do Robô
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``RobotMCULogCollect()``"
    "Descrição", "Geração de logs MCU do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Definir Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetRobotStopOnComDisc(portID, enable, confirmTime)``"
    "Descrição", "Define a parada da operação do robô quando a comunicação da porta for desconectada"
    "Parâmetros obrigatórios", "
    - ``portID``: Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    - ``enable``: 0-desativar; 1-ativar
    - ``confirmTime``: Duração de confirmação da interrupção da comunicação (ms)[0-5000]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter Parâmetros de Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetRobotStopOnComDisc(portID)``"
    "Descrição", "Obtém os parâmetros de parada da operação do robô quando a comunicação da porta for desconectada"
    "Parâmetros obrigatórios", "
    - ``portID``: Número da porta 0-8080; 1-8083; 2-20002; 3-20004
    - ``enable``: 0-desativar; 1-ativar
    - ``confirmTime``: Duração de confirmação da interrupção da comunicação (ms)[0-5000]"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código de Parâmetros de Parada da Operação do Robô Quando a Comunicação da Porta For Desconectada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot
    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def test_robot_stop_on_com_disc(self):
        # Inicializar parâmetros
        enable = False
        confirm_time = 0

        # Definir a função de parada do robô quando a comunicação for desconectada
        rtn = robot.SetRobotStopOnComDisc(0, True, 330)
        print(f"SetRobotStopOnComDisc index0: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(1, True, 550)
        print(f"SetRobotStopOnComDisc index1: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(2, True, 110)
        print(f"SetRobotStopOnComDisc index2: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(3, True, 220)
        print(f"SetRobotStopOnComDisc index3: {rtn}")

        # Obter a configuração de parada do robô quando a comunicação for desconectada
        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(0)
        print(f"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(1)
        print(f"GetRobotStopOnComDisc 80803 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(2)
        print(f"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(3)
        print(f"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        # Fechar conexão RPC
        robot.CloseRPC()
        return 0

    test_robot_stop_on_com_disc(robot)

Envio de Quadro de Comando via UDP
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SendUDPFrame(frame)``"
    "Descrição", "Envio de quadro de comando via UDP"
    "Parâmetros obrigatórios", "
    - ``frame``: Envia dados UDP, transmissão transparente, não encapsulada"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK Baseado em Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')

    def TestSendUDPFrame(self):
        # Definir retorno de chamada
        def callback(src_type, count, cmd_id, data_len, content):
            print("Resposta recebida: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0
        robot.SetUDPCmdRpyCallback(callback)

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame Mode(0) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII21III303III7IIIMode(1)III/b/f")
        print(f"SendUDPFrame Mode(1) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII49III201III184IIIMoveJ(-15.625, -82.680, 101.654, -110.950, -88.290, 0.017, -383.012, -2.325, 242.655, -178.024, 1.710, 74.416, 0, 0, 100, 100, 100, 0.000, 0.000, 0.000, 0.000, -1, 0, 0, 0, 0, 0, 0, 0)III/b/f")
        print(f"SendUDPFrame MoveJ(-15.625) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII48III203III199IIIMoveL(-75.622, -82.680, 101.654, -110.950, -88.290, 0.017, -193.537, 330.525, 242.657, -178.024, 1.710, 14.420, 0, 0, 100, 100, 100, -1, 0, 0.000, 0.000, 0.000, 0.000, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0)III/b/f")
        print(f"SendUDPFrame MoveL(-75.622) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII4III905III20IIIGetSoftwareVersion()III/b/f")
        print(f"SendUDPFrame GetSoftwareVersion() rtn is {rtn}")

        time.sleep(1)

        # Teste de validação de envio de quadro UDP
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("III20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III6IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/b|||20|||303|||7|||Mode(0)|||/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bII20II303II7IIMode(0)II/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        robot.CloseRPC()
        time.sleep(1)

    TestSendUDPFrame(robot)

Definir Cor da Luz da Extremidade do Robô Personalizada pelo Usuário
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``SetUserLEDColor(r, g, b)``"
    "Descrição", "Define a cor da luz da extremidade do robô personalizada pelo usuário"
    "Parâmetros obrigatórios", "
    - ``r``: Controle da luz vermelha da extremidade; 0-apagada; 1-acesa
    - ``g``: Controle da luz verde da extremidade; 0-apagada; 1-acesa
    - ``b``: Controle da luz azul da extremidade; 0-apagada; 1-acesa
    - "
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Exemplo de Código SDK para Definir Cor da Luz da Extremidade do Robô Personalizada pelo Usuário
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # Estabelece conexão com o controlador do robô
    robot = Robot.RPC('192.168.58.2')


    def testled(self):
        # Definir cor da luz LED do usuário
        # Ordem dos parâmetros: R, G, B (vermelho, verde, azul)

        # Branco (vermelho, verde e azul acesos)
        robot.SetUserLEDColor(True, True, True)
        time.sleep(1)

        # Desligar todas as luzes
        robot.SetUserLEDColor(False, False, False)
        time.sleep(1)

        # Vermelho (apenas luz vermelha acesa)
        robot.SetUserLEDColor(True, False, False)
        time.sleep(1)

        # Verde (apenas luz verde acesa)
        robot.SetUserLEDColor(False, True, False)
        time.sleep(1)

        # Azul (apenas luz azul acesa)
        robot.SetUserLEDColor(False, False, True)

        # Fechar conexão
        robot.CloseRPC()

    testled(robot)