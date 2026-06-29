Uso do Programa WebAPP do Robô
=======================================

.. toctree::
    :maxdepth: 5

Definir carregamento automático do programa de trabalho padrão na inicialização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o carregamento automático do programa de trabalho padrão na inicialização
    * @param [in] flag 0-não carregar automaticamente o programa padrão na inicialização, 1-carregar automaticamente o programa padrão na inicialização
    * @param [in] program_name Nome e caminho do programa de trabalho, ex: "movej.lua"
    * @return Código de erro
    */
    int LoadDefaultProgConfig(int flag, String program_name);

Carregar o programa de trabalho especificado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Carrega o programa de trabalho especificado
    * @param [in] program_name Nome e caminho do programa de trabalho, ex: "movej.lua"
    * @return Código de erro
    */
    int ProgramLoad(String program_name);

Obter o nome do programa de trabalho carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o nome do programa de trabalho carregado
    * @param [out] program_name program_name[0]: Nome e caminho do programa de trabalho, ex: "movej.lua"
    * @return Código de erro
    */
    int GetLoadedProgram(String[] program_name);

Obter o número da linha atual de execução do programa de trabalho do robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o número da linha atual de execução do programa de trabalho do robô
    * @param [out] List[0]: código de erro; List[1]: int line Número da linha
    * @return Código de erro
    */
    List<Integer> GetCurrentLine();

Executar o programa de trabalho atualmente carregado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Executa o programa de trabalho atualmente carregado
    * @return Código de erro
    */
    int ProgramRun();

Pausar o programa de trabalho atualmente em execução
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Pausa o programa de trabalho atualmente em execução
    * @return Código de erro
    */
    int PauseMotion();

Retomar o programa de trabalho atualmente pausado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Retoma o programa de trabalho atualmente pausado
    * @return Código de erro
    */
    int ResumeMotion();

Terminar o programa de trabalho atualmente em execução
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Termina o programa de trabalho atualmente em execução
    * @return Código de erro
    */
    int StopMotion();

Obter o estado de execução do programa de trabalho do robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o estado de execução do programa de trabalho do robô
    * @param [out] state 1-programa parado ou nenhum programa em execução, 2-programa em execução, 3-programa pausado
    * @return Código de erro
    */
    public int GetProgramState(int[] state)

Exemplo de Código de Operação de Programa LUA do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLuaOp(Robot robot)
    {
        String program_name = "Text1.lua";
        String[] loaded_name = new String[]{""};
        int[] state = new int[]{0};
        List<Integer> line = new ArrayList<>();

        robot.Mode(0);
        robot.LoadDefaultProgConfig(0, program_name);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        robot.Sleep(1000);
        robot.ProgramPause();
        robot.GetProgramState(state);
        System.out.println("program state:"+ state[0]);
        line = robot.GetCurrentLine();
        System.out.println("current line:"+ line);
        robot.GetLoadedProgram(loaded_name);
        System.out.println("program name:"+ loaded_name[0]);
        robot.Sleep(1000);
        robot.ProgramResume();
        robot.Sleep(1000);
        robot.ProgramStop();
        robot.Sleep(1000);

        robot.CloseRPC();
        return 0;
    }

Baixar Programa Lua
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Baixa programa de trabalho
    * @param [in] fileName Nome do arquivo Lua a ser baixado "test.lua" ou "test.tar.gz"
    * @param [in] savePath Caminho local para salvar o arquivo "D://Down/"
    * @return Código de erro
    */
    int LuaDownLoad(String fileName, String savePath);

Excluir Programa Lua
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Exclui programa de trabalho
    * @param [in] fileName Nome do programa de trabalho a ser excluído "test.lua"
    * @return Código de erro
    */
    int LuaDelete(String fileName);

Obter todos os nomes de arquivos Lua atuais
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém todos os nomes de arquivos Lua atuais
    * @param [out] luaNames Lista de nomes dos programas de trabalho
    * @return Código de erro
    */
    int GetLuaList(List<String> luaNames);

Enviar Programa Lua
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Envia programa de trabalho
    * @param [in] filePath Caminho do arquivo Lua local ".../test.lua" ou ".../test.tar.gz"
    * @param [out] errStr Mensagem de erro
    * @return Código de erro
    */
    int LuaUpload(String filePath, String errStr);

Exemplo de Código de Envio e Download de Arquivo LUA do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLUAUpDownLoad(Robot robot)
    {
        List<String> luaNames = new ArrayList<>();
        int rtn = robot.GetLuaList(luaNames);
        System.out.println("res is: "+rtn);
        System.out.println("size is: "+luaNames.size());
        for (int it = 1; it < luaNames.size(); it++)
        {
            System.out.println(luaNames.get(it));
        }

        rtn = robot.LuaDownLoad("test.lua", "D://zDOWN/");
        System.out.println("LuaDownLoad rtn is:"+rtn);

        rtn = robot.LuaUpload("D://zUP/XG.lua", "");
        System.out.println("LuaUpload rtn is:"+ rtn);

        rtn = robot.LuaDelete("XG.lua");
        System.out.println("LuaDelete rtn is:"+ rtn);

        return 0;
    }