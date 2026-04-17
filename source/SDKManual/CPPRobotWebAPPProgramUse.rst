Uso do Programa WebAPP do Robô
=======================================

.. toctree::
    :maxdepth: 5

Definir carregamento automático do programa de trabalho padrão na inicialização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Define o carregamento automático do programa de trabalho padrão na inicialização
    * @param  [in] flag  0-não carregar automaticamente o programa padrão na inicialização, 1-carregar automaticamente o programa padrão na inicialização
    * @param  [in] program_name Nome e caminho do programa de trabalho, ex: "/fruser/movej.lua", onde "/fruser/" é o caminho fixo para QX, "/usr/local/etc/controller/lua/" é o caminho fixo para LA
    * @return  Código de erro
    */
    errno_t LoadDefaultProgConfig(uint8_t flag, char program_name[64]);

Carregar o programa de trabalho especificado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Carrega o programa de trabalho especificado
    * @param  [in] program_name Nome e caminho do programa de trabalho, ex: "/fruser/movej.lua", onde "/fruser/" é o caminho fixo para QX, "/usr/local/etc/controller/lua/" é o caminho fixo para LA
    * @return  Código de erro
    */
    errno_t ProgramLoad(char program_name[64]);

Obter o nome do programa de trabalho carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o nome do programa de trabalho carregado
    * @param  [out] program_name Nome e caminho do programa de trabalho, ex: "/fruser/movej.lua", onde "/fruser/" é o caminho fixo para QX, "/usr/local/etc/controller/lua/" é o caminho fixo para LA
    * @return  Código de erro
    */
    errno_t GetLoadedProgram(char program_name[64]);

Obter o número da linha atual de execução do programa de trabalho do robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o número da linha atual de execução do programa de trabalho do robô
    * @param  [out] line  Número da linha
    * @return  Código de erro
    */
    errno_t GetCurrentLine(int *line);

Executar o programa de trabalho atualmente carregado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Executa o programa de trabalho atualmente carregado
    * @return  Código de erro
    */
    errno_t ProgramRun();

Pausar o programa de trabalho atualmente em execução
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Pausa o programa de trabalho atualmente em execução
    * @return  Código de erro
    */
    errno_t ProgramPause();

Retomar o programa de trabalho atualmente pausado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Retoma o programa de trabalho atualmente pausado
    * @return  Código de erro
    */
    errno_t ProgramResume();

Terminar o programa de trabalho atualmente em execução
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Termina o programa de trabalho atualmente em execução
    * @return  Código de erro
    */
    errno_t ProgramStop();

Obter o estado de execução do programa de trabalho do robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  Obtém o estado de execução do programa de trabalho do robô
    * @param  [out] state 1-programa parado ou nenhum programa em execução, 2-programa em execução, 3-programa pausado
    * @return  Código de erro
    */
    errno_t GetProgramState(uint8_t *state);

Exemplo de Código de Operação de Programa LUA do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLuaOp(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      char program_name[64] = "/fruser/test.lua";
      char loaded_name[64] = "";
      uint8_t state;
      int line;
      robot.Mode(0);
      robot.LoadDefaultProgConfig(0, program_name);
      robot.ProgramLoad(program_name);
      robot.ProgramRun();
      robot.Sleep(1000);
      robot.ProgramPause();
      robot.GetProgramState(&state);
      printf("program state:%u\n", state);
      robot.GetCurrentLine(&line);
      printf("current line:%d\n", line);
      robot.GetLoadedProgram(loaded_name);
      printf("program name:%s\n", loaded_name);
      robot.Sleep(1000);
      robot.ProgramResume();
      robot.Sleep(1000);
      robot.ProgramStop();
      robot.Sleep(1000);
      robot.CloseRPC();
      return 0;
    }

Baixar arquivo Lua
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Baixa arquivo Lua
    * @param [in] fileName Nome do arquivo Lua a ser baixado, ex: "test.lua"
    * @param [in] savePath Caminho local para salvar o arquivo, ex: "D://Down/"
    * @return Código de erro
    */
    errno_t LuaDownLoad(std::string fileName, std::string savePath);

Excluir arquivo Lua
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Exclui arquivo Lua
    * @param [in] fileName Nome do arquivo Lua a ser excluído, ex: "test.lua"
    * @return Código de erro
    */
    errno_t LuaDelete(std::string fileName);

Obter todos os nomes de arquivos Lua atuais
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém todos os nomes de arquivos Lua atuais
    * @param [out] luaNames Lista de nomes de arquivos Lua
    * @return Código de erro
    */
    errno_t GetLuaList(std::list<std::string>* luaNames);

Enviar arquivo Lua
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Envia arquivo Lua
    * @param [in] filePath Caminho do arquivo Lua local
    * @return Código de erro
    */
    errno_t LuaUpload(std::string filePath);

Exemplo de Código de Envio e Download de Arquivo LUA do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLUAUpDownLoad(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      list<std::string> luaNames;
      rtn = robot.GetLuaList(&luaNames);
      std::cout << "res is: " << rtn << std::endl;
      std::cout << "size is: " << luaNames.size() << std::endl;
      for (auto it = luaNames.begin(); it != luaNames.end(); it++)
      {
        std::cout << it->c_str() << std::endl;
      }
      rtn = robot.LuaDownLoad("test.lua", "D://zDOWN/");
      printf("LuaDownLoad rtn is %d\n", rtn);
      rtn = robot.LuaUpload("D://zUP/airlab.lua");
      printf("LuaUpload rtn is %d\n", rtn);
      rtn = robot.LuaDelete("test.lua");
      printf("LuaDelete rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }