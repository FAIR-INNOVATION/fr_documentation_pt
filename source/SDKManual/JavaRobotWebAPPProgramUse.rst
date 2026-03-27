机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置开机自动加载默认的作业程序
    * @param  [in] flag  0-开机不自动加载默认程序，1-开机自动加载默认程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    int LoadDefaultProgConfig(int flag, String program_name); 

加载指定的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  加载指定的作业程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    int ProgramLoad(String program_name); 

获取已加载的作业程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取已加载的作业程序名
    * @param  [out] program_name program_name[0]:作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为QX固定路径，"/usr/local/etc/controller/lua/"为LA固定路径
    * @return  错误码
    */
    int GetLoadedProgram(String[] program_name); 

获取当前机器人作业程序的执行行号
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前机器人作业程序执行的行号
    * @param  [out] List[0]:错误码; List[1]:int line 行号
    * @return  错误码
    */   
    List<Integer> GetCurrentLine();

运行当前加载的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  运行当前加载的作业程序
    * @return  错误码
    */
    int ProgramRun();

暂停当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  暂停当前运行的作业程序
    * @return  错误码
    */ 
    int PauseMotion();

恢复当前暂停的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恢复当前暂停的作业程序
    * @return  错误码
    */ 
    int ResumeMotion(); 

终止当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  终止当前运行的作业程序
    * @return  错误码
    */ 
    int StopMotion();   

获取机器人作业程序执行状态
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人作业程序执行状态
    * @param   [out] state 1-程序停止或无程序运行，2-程序运行中，3-程序暂停
    * @return  错误码
    */
    public int GetProgramState(int[] state)

机器人LUA程序操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLuaOp(Robot robot)
    {
        String program_name = "/fruser/Text1.lua";
        String[] loaded_name = new String[]{""};
        int[] state=new int[]{0};
        List<Integer> line=new ArrayList<>();

        robot.Mode(0);
        robot.LoadDefaultProgConfig(0, program_name);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        robot.Sleep(1000);
        robot.ProgramPause();
        robot.GetProgramState(state);
        System.out.println("program state:"+ state[0]);
        line=robot.GetCurrentLine();
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

下载Lua程序
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下载作业程序
    * @param [in] fileName 要下载的lua文件名"test.lua"或"test.tar.gz"
    * @param [in] savePath 保存文件本地路径“D://Down/”
    * @return 错误码 
    */
    int LuaDownLoad(String fileName, String savePath);

删除Lua程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 删除作业程序
    * @param [in] fileName 要删除的作业程序名"test.lua"
    * @return 错误码 
    */
    int LuaDelete(String fileName);

获取当前所有lua文件名称
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取当前所有lua文件名称
    * @param [out] luaNames 作业程序名称列表
    * @return 错误码 
    */
    int GetLuaList(List<String> luaNames);

上传Lua程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上传作业程序
    * @param [in] filePath 本地lua文件路径名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 错误信息
    * @return 错误码 
    */
    int LuaUpload(String filePath, String errStr);

机器人LUA文件上传下载代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLUAUpDownLoad(Robot robot)
    {
        List<String> luaNames=new ArrayList<>();
        int rtn = robot.GetLuaList(luaNames);
        System.out.println("res is: "+rtn);
        System.out.println("size is: "+luaNames.size());
        for (int it =1; it < luaNames.size(); it++)
        {
            System.out.println(luaNames.get(it));
        }

        rtn = robot.LuaDownLoad("test.lua", "D://zDOWN/");
        System.out.println("LuaDownLoad rtn is:"+rtn);

        rtn = robot.LuaUpload("D://zUP/XG.lua","");
        System.out.println("LuaUpload rtn is:"+ rtn);

        rtn = robot.LuaDelete("XG.lua");
        System.out.println("LuaDelete rtn is:"+ rtn);

        return 0;
    }
