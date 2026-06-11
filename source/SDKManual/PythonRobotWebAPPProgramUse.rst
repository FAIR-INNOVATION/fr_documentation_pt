Uso do Programa WebAPP do Robô
========================================

.. toctree::
    :maxdepth: 5

Definir carregamento automático do programa de trabalho padrão na inicialização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LoadDefaultProgConfig(flag, program_name)``"
    "Descrição", "Define o carregamento automático do programa de trabalho padrão na inicialização"
    "Parâmetros obrigatórios", "
    - ``flag``: 1-carregar automaticamente o programa padrão na inicialização, 0-não carregar automaticamente
    - ``program_name``: Nome e caminho do programa de trabalho, ex: `movej.lua`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Carregar o programa de trabalho especificado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramLoad(program_name)``"
    "Descrição", "Carrega o programa de trabalho especificado"
    "Parâmetros obrigatórios", "- ``program_name``: Nome e caminho do programa de trabalho, ex: `movej.lua`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter o nome do programa de trabalho carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetLoadedProgram()``"
    "Descrição", "Obtém o nome do programa de trabalho carregado"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``program_name``: Nome do programa de trabalho carregado"

Obter o número da linha atual de execução do programa de trabalho do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetCurrentLine()``"
    "Descrição", "Obtém o número da linha atual de execução do programa de trabalho do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``line_num``: Número da linha atual de execução do programa de trabalho do robô"

Executar o programa de trabalho atualmente carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramRun()``"
    "Descrição", "Executa o programa de trabalho atualmente carregado"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Pausar o programa de trabalho atualmente em execução
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramPause()``"
    "Descrição", "Pausa o programa de trabalho atualmente em execução"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Retomar o programa de trabalho atualmente pausado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramResume()``"
    "Descrição", "Retoma o programa de trabalho atualmente pausado"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Terminar o programa de trabalho atualmente em execução
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``ProgramStop()``"
    "Descrição", "Termina o programa de trabalho atualmente em execução"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter o estado de execução do programa de trabalho do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetProgramState()``"
    "Descrição", "Obtém o estado de execução do programa de trabalho do robô"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``state``: Estado de execução do programa de trabalho do robô, 1-programa parado ou nenhum programa em execução, 2-programa em execução, 3-programa pausado"

Exemplo de Código de Operação de Programa LUA do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    program_name = "test0610.lua"
    loaded_name = ""
    state = 0
    line = 0
    robot.Mode(0)
    robot.LoadDefaultProgConfig(0, program_name)
    robot.ProgramLoad(program_name)
    robot.ProgramRun()
    time.sleep(1)
    robot.ProgramPause()
    error, state = robot.GetProgramState()
    print(f"program state:{state}")
    error, line = robot.GetCurrentLine()
    print(f"current line:{line}")
    error, loaded_name = robot.GetLoadedProgram()
    print(f"program name:{loaded_name}")
    time.sleep(1)
    robot.ProgramResume()
    time.sleep(1)
    robot.ProgramStop()
    time.sleep(1)
    robot.CloseRPC()

Baixar arquivo Lua
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LuaDownLoad(fileName, savePath)``"
    "Descrição", "Baixa arquivo Lua"
    "Parâmetros obrigatórios", "- ``fileName``: Nome do arquivo Lua a ser baixado, ex: `test.lua`
    - ``savePath``: Caminho local para salvar o arquivo, ex: `D://Down/`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Excluir arquivo Lua
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LuaDelete(fileName)``"
    "Descrição", "Exclui arquivo Lua"
    "Parâmetros obrigatórios", "- ``fileName``: Nome do arquivo Lua a ser excluído `test.lua`"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "Código de erro: sucesso-0, falha-código de erro"

Obter todos os nomes de arquivos Lua atuais
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``GetLuaList()``"
    "Descrição", "Obtém todos os nomes de arquivos Lua atuais"
    "Parâmetros obrigatórios", "Nenhum"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - ``lua_num``: Número de arquivos Lua
    - ``luaNames``: Lista de nomes de arquivos Lua"

Enviar arquivo Lua
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table::
    :stub-columns: 1
    :widths: 10 30

    "Protótipo", "``LuaUpload(filePath)``"
    "Descrição", "Envia arquivo Lua"
    "Parâmetros obrigatórios", "- ``filePath``: Caminho completo do arquivo para upload, ex: D://test/test.lua"
    "Parâmetros padrão", "Nenhum"
    "Valor de retorno", "- Código de erro: sucesso-0, falha-código de erro
    - errorStr (retornado se o arquivo Lua existir com erro)"

Exemplo de Código de Envio e Download de Arquivo LUA do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # Estabelece conexão com o controlador do robô, retorna um objeto robô se a conexão for bem-sucedida
    robot = Robot.RPC('192.168.58.2')
    rtn, lua_num, luaNames = robot.GetLuaList()
    print(f"res is:{rtn}")
    print(f"size is:{lua_num}")
    for name in luaNames:
        print(name)
    rtn = robot.LuaDownLoad("test0610.lua", "D://zDOWN/")
    print(f"LuaDownLoad rtn is:{rtn}")
    rtn = robot.LuaUpload("D://zDOWN/test0610.lua")
    print(f"LuaUpload rtn is:{rtn}")
    rtn = robot.LuaDelete("test0610.lua")
    print(f"LuaDelete rtn is:{rtn}")
    robot.CloseRPC()