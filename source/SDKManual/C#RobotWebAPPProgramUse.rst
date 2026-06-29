Uso do Programa WebAPP do Robô
==========================================

.. toctree::
    :maxdepth: 5

Definir carregamento automático do programa de trabalho padrão na inicialização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define o carregamento automático do programa de trabalho padrão na inicialização
    * @param  [in] flag  0-não carregar automaticamente o programa padrão na inicialização, 1-carregar automaticamente o programa padrão na inicialização
    * @param  [in] program_name Nome e caminho do programa de trabalho, ex: "movej.lua"
    */
    int LoadDefaultProgConfig(byte flag, string program_name);

Carregar o programa de trabalho especificado
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Carrega o programa de trabalho especificado
    * @param  [in] program_name Nome e caminho do programa de trabalho, ex: "movej.lua"
    * @return  Código de erro
    */
    int ProgramLoad(string program_name);

Obter o nome do programa de trabalho carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o nome do programa de trabalho carregado
    * @param  [out] program_name Nome e caminho do programa de trabalho, ex: "movej.lua"
    * @return  Código de erro
    */
    int GetLoadedProgram(ref string program_name);

Obter o número da linha atual de execução do programa de trabalho do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o número da linha atual de execução do programa de trabalho do robô
    * @param  [out] line  Número da linha
    * @return  Código de erro
    */
    int GetCurrentLine(ref int line);

Executar o programa de trabalho atualmente carregado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Executa o programa de trabalho atualmente carregado
    * @return  Código de erro
    */
    int ProgramRun();

Pausar o programa de trabalho atualmente em execução
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Pausa o programa de trabalho atualmente em execução
    * @return  Código de erro
    */
    int ProgramPause();

Retomar o programa de trabalho atualmente pausado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Retoma o programa de trabalho atualmente pausado
    * @return  Código de erro
    */
    int ProgramResume();

Terminar o programa de trabalho atualmente em execução
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Termina o programa de trabalho atualmente em execução
    * @return  Código de erro
    */
    int ProgramStop();

Obter o estado de execução do programa de trabalho do robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém o estado de execução do programa de trabalho do robô
    * @param  [out] state 1-programa parado ou nenhum programa em execução, 2-programa em execução, 3-programa pausado
    * @return  Código de erro
    */
    int GetProgramState(ref byte state);

Exemplo de Código de Operação de Programa LUA do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnWebApp_Click(object sender, EventArgs e)
    {
        string program_name = "Text1.lua";
        string loaded_name = "";
        byte state = 0;
        int line = 0;

        robot.Mode(0);
        robot.LoadDefaultProgConfig(0, program_name);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        Thread.Sleep(1000);
        robot.ProgramPause();
        robot.GetProgramState(ref state);
        Console.WriteLine("program state:{0}\n", state);
        robot.GetCurrentLine(ref line);
        Console.WriteLine("current line:{0}\n", line);
        robot.GetLoadedProgram(ref loaded_name);
        Console.WriteLine("program name:{0}\n", loaded_name);
        Thread.Sleep(1000);
        robot.ProgramResume();
        Thread.Sleep(1000);
        robot.ProgramStop();
        Thread.Sleep(1000);
    }

Baixar arquivo Lua
+++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Baixa arquivo Lua
    * @param [in] fileName Programa de trabalho a ser baixado "test.lua" ou "test.tar.gz"
    * @param [in] savePath Caminho local para salvar o programa de trabalho "D://Down/"
    * @return Código de erro
    */
    public int LuaDownLoad(string fileName, string savePath);

Enviar arquivo Lua
+++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Envia arquivo Lua
    * @param [in] filePath Caminho do programa de trabalho local ".../test.lua" ou ".../test.tar.gz"
    * @param [out] errStr Mensagem de erro
    * @return Código de erro
    */
    public int LuaUpload(string filePath, ref string errStr);

Excluir arquivo Lua
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Exclui arquivo Lua
    * @param [in] fileName Nome do programa de trabalho a ser excluído "test.lua"
    * @return Código de erro
    */
    public int LuaDelete(string fileName);

Obter todos os nomes de arquivos Lua atuais
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém todos os nomes de arquivos Lua atuais
    * @param [out] luaNames Lista de nomes dos programas de trabalho
    * @return Código de erro
    */
    public int GetLuaList(ref List<string> luaNames);

Exemplo de Código de Envio e Download de Arquivo LUA do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnUploadLua_Click(object sender, EventArgs e)
    {
        int rtn;
        List<string> luaNames = new List<string>();
        rtn = robot.GetLuaList(ref luaNames);
        Console.WriteLine("res is: {0}", rtn);
        Console.WriteLine("size is: {0}", luaNames.Count);
        foreach (var name in luaNames)
        {
            Console.WriteLine(name);
        }
        rtn = robot.LuaDownLoad("TT.lua", "D://zDOWN/");
        Console.WriteLine("LuaDownLoad rtn is {0}", rtn);
        string errStr = "";
        Thread.Sleep(2000);

        rtn = robot.LuaUpload("D://zUP/airlab.lua", ref errStr);
        Console.WriteLine("LuaUpload rtn is {0}", errStr);
        Thread.Sleep(2000);
        rtn = robot.LuaDelete("TT.lua");
        Console.WriteLine("LuaDelete rtn is {0}", rtn);
    }