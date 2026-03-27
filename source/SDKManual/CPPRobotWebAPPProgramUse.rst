机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置开机自动加载默认的作业程序
    * @param  [in] flag  0-开机不自动加载默认程序，1-开机自动加载默认程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    errno_t  LoadDefaultProgConfig(uint8_t flag, char program_name[64]);

加载指定的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  加载指定的作业程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    errno_t  ProgramLoad(char program_name[64]);

获取已加载的作业程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取已加载的作业程序名
    * @param  [out] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    errno_t  GetLoadedProgram(char program_name[64]);  

获取当前机器人作业程序的执行行号
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取当前机器人作业程序执行的行号
    * @param  [out] line  行号
    * @return  错误码
    */   
    errno_t  GetCurrentLine(int *line);

运行当前加载的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  运行当前加载的作业程序
    * @return  错误码
    */
    errno_t  ProgramRun();

暂停当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  暂停当前运行的作业程序
    * @return  错误码
    */ 
    errno_t  ProgramPause();

恢复当前暂停的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  恢复当前暂停的作业程序
    * @return  错误码
    */ 
    errno_t  ProgramResume();  

终止当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  终止当前运行的作业程序
    * @return  错误码
    */ 
    errno_t  ProgramStop();    

获取机器人作业程序执行状态
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取机器人作业程序执行状态
    * @param  [out]  state 1-程序停止或无程序运行，2-程序运行中，3-程序暂停
    * @return  错误码
    */
    errno_t  GetProgramState(uint8_t *state);

机器人LUA程序操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

下载Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下载Lua文件
    * @param [in] fileName 要下载的lua文件名，例如：“test.lua”
    * @param [in] savePath 保存文件本地路径，例如：“D://Down/”
    * @return 错误码
    */
    errno_t LuaDownLoad(std::string fileName, std::string savePath);

删除Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 删除Lua文件
    * @param [in] fileName 要删除的lua文件名，例如：“test.lua”
    * @return 错误码
    */
    errno_t LuaDelete(std::string fileName);

获取当前所有lua文件名称
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取当前所有lua文件名称
    * @param [out] luaNames lua文件名列表
    * @return 错误码
    */
    errno_t GetLuaList(std::list<std::string>* luaNames);

上传Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传Lua文件
    * @param [in] filePath 本地lua文件路径名
    * @return 错误码
    */
    errno_t LuaUpload(std::string filePath);

机器人LUA文件上传下载代码示例
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