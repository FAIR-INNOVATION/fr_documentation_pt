机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置控制箱数字量输出
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetDO(int id, byte status, byte smooth, byte block); 

设置工具数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具数字量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolDO(int id, byte status, byte smooth, byte block); 

设置控制箱模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置控制箱模拟量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetAO(int id, float value, byte block); 

设置工具模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具模拟量输出
    * @param  [in] id  io编号，范围[0]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolAO(int id, float value, byte block);

设置数字量、模拟量输出代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos: 

    private void button14_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;


        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 0;

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 1;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        status = 0;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetAO(0, i, block);
            Thread.Sleep(30);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetToolAO(0, i, block);
            Thread.Sleep(30);
        }

    }

获取控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    int GetDI(int id, byte block, ref byte level);

获取工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    int GetToolDI(int id, byte block, ref byte level); 

获取控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    int GetAI(int id, byte block, ref float persent); 

获取工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    int GetToolAI(int id, byte block, ref float persent); 

获取机器人末端记录按钮状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人末端记录按钮状态
    * @param [out] state 按钮状态，0-按下，1-松开
    * @return 错误码 
    */ 
    int GetAxlePointRecordBtnState(ref byte state); 

获取机器人末端DO输出状态
++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人末端DO输出状态 
    * @param [out] do_state DO输出状态，do0~do1对应bit1~bit2,从bit0开始 
    * @return 错误码 
    */ 
    int GetToolDO(ref byte do_state);

获取机器控制器DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人控制器DO输出状态 
    * @param [out] do_state_h DO输出状态，co0~co7对应bit0~bit7 
    * @param [out] do_state_l DO输出状态，do0~do7对应bit0~bit7
    * @return 错误码 
    */ 
    int GetDO(ref int do_state_h, ref int do_state_l);   

获取机器人DI、DO状态代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button15_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        robot.GetDI(0, block, ref di);
        Console.WriteLine($"di0: {di}");

        tool_di = (byte)robot.GetToolDI(1, block, ref tool_di);
        Console.WriteLine($"tool_di1: {tool_di}");

        robot.GetAI(0, block, ref ai);
        Console.WriteLine($"ai0: {ai}");

        tool_ai = robot.GetToolAI(0, block, ref tool_ai);
        Console.WriteLine($"tool_ai0: {tool_ai}");

        byte _button_state = 0;
        robot.GetAxlePointRecordBtnState(ref _button_state);
        Console.WriteLine($"_button_state is: {_button_state}");

        byte tool_do_state = 0;
        robot.GetToolDO(ref tool_do_state);
        Console.WriteLine($"tool DO state is: {tool_do_state}");

        int do_state_h = 0;
        int do_state_l = 0;
        robot.GetDO(ref do_state_h, ref do_state_l);
        Console.WriteLine($"DO state high is: {do_state_h}\n DO state low is: {do_state_l}");
    }

等待控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitDI(int id, byte status, int max_time, int opt); 

等待控制箱多路数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱多路数字量输入
    * @param  [in] mode 0-多路与，1-多路或
    * @param  [in] id  io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitMultiDI(int mode, int id, byte status, int max_time, int opt); 

等待工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolDI(int id, byte status, int max_time, int opt); 

等待控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitAI(int id, int sign, float value, int max_time, int opt);   

等待工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolAI(int id, int sign, float value, int max_time, int opt); 

等待控制箱数字、模拟输入信号代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnIOTest_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        int rtn = robot.WaitDI(0, 1, 1000, 1);
        Console.WriteLine("WaitDI over; rtn is: " + rtn);

        robot.WaitMultiDI(1, 3, 3, 1000, 1);
        Console.WriteLine("WaitMultiDI over; rtn is: " + rtn);

        robot.WaitToolDI(1, 1, 1000, 1);
        Console.WriteLine("WaitToolDI over; rtn is: " + rtn);

        robot.WaitAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitAI over; rtn is: " + rtn);

        robot.WaitToolAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitToolAI over; rtn is: " + rtn);
    }
    
设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱DO停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag);

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱AO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag);

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端工具DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetAxleDO(int resetFlag, int reloadFlag);

设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端工具AO停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetAxleAO(int resetFlag, int reloadFlag);

设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置扩展DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return  错误码
    */
    public int SetOutputResetExtDO(int resetFlag, int reloadFlag);

设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置扩展AO停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetExtAO(int resetFlag, int reloadFlag);

设置SmartTool停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置SmartTool停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    public int SetOutputResetSmartToolDO(int resetFlag, int reloadFlag);

设置LUA程序停止/暂停后输出复位代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestDOReset()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, 1, 0, 0);
            Thread.Sleep(200);
        }

        int resetFlag = 1;
        int resumeReloadFlag = 1;
        int rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();

        Thread.Sleep(2000);
        robot.PauseMotion();
        Thread.Sleep(2000);
        robot.ResumeMotion();
        Thread.Sleep(2000);
    }

设置控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱可配置CI端口功能
    * @param [in] config CI0-CI7功能编码；
    * 0-无;1-起弧成功;2-焊机准备;3-传送带检测;4-暂停;5-恢复;6-启动;7-停止;
    8-暂停/恢复;9-启动/停止;10-脚踏拖动;11-移至作业原点;12-手自动切换;
    13-焊丝寻位成功;14-运动中断;15-启动主程序;16-启动倒带;17-启动确认;
    18-光电检测信号X;19-光电检测信号Y;20-外部急停输入信号1;21-外部急停输入信号2;
    22-一级缩减模式;23-二级缩减模式;24-三级缩减模式(停止);25-恢复焊接;26-终止焊接;
    27-辅助拖动开启;28-辅助拖动关闭;29-辅助拖动开启/关闭;30-清除所有错误;
    31-手自动切换(高低电平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定点跟踪开始/结束
    * @return 错误码
    */
    public int SetDIConfig(int[] config)

获取控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱可配置CI端口功能
    * @param [in] config CI0-CI7功能编码；
    * 0-无;1-起弧成功;2-焊机准备;3-传送带检测;4-暂停;5-恢复;6-启动;7-停止;
    8-暂停/恢复;9-启动/停止;10-脚踏拖动;11-移至作业原点;12-手自动切换;
    13-焊丝寻位成功;14-运动中断;15-启动主程序;16-启动倒带;17-启动确认;
    18-光电检测信号X;19-光电检测信号Y;20-外部急停输入信号1;21-外部急停输入信号2;
    22-一级缩减模式;23-二级缩减模式;24-三级缩减模式(停止);25-恢复焊接;26-终止焊接;
    27-辅助拖动开启;28-辅助拖动关闭;29-辅助拖动开启/关闭;30-清除所有错误;
    31-手自动切换(高低电平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定点跟踪开始/结束
    * @return 错误码
    */
    public int GetDIConfig(out int[] config)

设置控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱可配置CO端口功能
    * @param [out] config CO0-CO7功能编码；
    * 0-无;1-机器人报错;2-机器人运动中;3-喷涂启停;4-喷涂清枪;5-送气信号;6-起弧信号;7-点动送丝;
    8-反向送丝;9-JOB输入口1;10-JOB输入口2;11-JOB输入口3;12-传送带启停控制;13-机器人暂停中;14-到达作业原点;
    15-到达干涉区;16-焊丝寻位启停控制;17-机器人启动完成;18-程序启动停止;19-自动手动模式;20-急停输出信号1-安全;
    21-急停输出信号2-安全;22-LUA脚本程序运行停止;23-安全状态输出-安全;24-保护性停止状态输出-安全;
    25-机器人运动中-安全;26-机器人缩减模式-安全;27-机器人非缩减模式-安全;28-机器人非停止;29-机器人报错-指令点错误;
    30-机器人报错-驱动器错误;31-机器人报错-超出软限位错误;32-机器人报错-碰撞错误;33-机器人报错-活动从站数量错误;
    34-机器人报错-从站错误;35-机器人报错-IO错误;36-机器人报错-夹爪错误;37-机器人报错-文件错误;38-机器人报错-奇异位姿错误;
    39-机器人报错-驱动器通信错误;40-机器人报错-参数错误;41-机器人报错-外部轴超出软限位错误;42-机器人警告-警告;
    43-机器人警告-安全门警告;44-机器人警告-运动警告;45-机器人警告-干涉区警告;46-机器人警告-安全墙警告;
    47-使能状态;48-断线自动抬升中;49-立方体1干涉警告;50-立方体2干涉警告;51-立方体3干涉警告;52-立方体4干涉警告;
    * @return 错误码
    */
    public int SetDOConfig(int[] config)

获取控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱可配置CO端口功能
    * @param [out] config CO0-CO7功能编码；
    * 0-无;1-机器人报错;2-机器人运动中;3-喷涂启停;4-喷涂清枪;5-送气信号;6-起弧信号;7-点动送丝;
    8-反向送丝;9-JOB输入口1;10-JOB输入口2;11-JOB输入口3;12-传送带启停控制;13-机器人暂停中;14-到达作业原点;
    15-到达干涉区;16-焊丝寻位启停控制;17-机器人启动完成;18-程序启动停止;19-自动手动模式;20-急停输出信号1-安全;
    21-急停输出信号2-安全;22-LUA脚本程序运行停止;23-安全状态输出-安全;24-保护性停止状态输出-安全;
    25-机器人运动中-安全;26-机器人缩减模式-安全;27-机器人非缩减模式-安全;28-机器人非停止;29-机器人报错-指令点错误;
    30-机器人报错-驱动器错误;31-机器人报错-超出软限位错误;32-机器人报错-碰撞错误;33-机器人报错-活动从站数量错误;
    34-机器人报错-从站错误;35-机器人报错-IO错误;36-机器人报错-夹爪错误;37-机器人报错-文件错误;38-机器人报错-奇异位姿错误;
    39-机器人报错-驱动器通信错误;40-机器人报错-参数错误;41-机器人报错-外部轴超出软限位错误;42-机器人警告-警告;
    43-机器人警告-安全门警告;44-机器人警告-运动警告;45-机器人警告-干涉区警告;46-机器人警告-安全墙警告;
    47-使能状态;48-断线自动抬升中;49-立方体1干涉警告;50-立方体2干涉警告;51-立方体3干涉警告;52-立方体4干涉警告;
    * @return 错误码
    */
    public int GetDOConfig(out int[] config)

设置末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端可配置End-CI端口功能
    * @param [in] config End CI0-CI1功能编码；
    * 0-无;1-拖动示教工具开关;2-点记录信号;3-手自动切换（脉冲信号）;4-TPD记录启动/停止;5-暂停运动;
    6-恢复运动;7-启动;8-停止;9-暂停/恢复;10-启动/停止;11-力传感器辅助拖动开启;12-力传感器辅助拖动关闭;
    13-力传感器辅助拖动开启/关闭;14-激光检测信号X;15-激光检测信号Y;16-PTP运动至作业原点;17-运动中断，根据信号停止当前运动;
    18-启动主程序;19-启动倒带;20-启动确认;21-恢复焊接;22-终止焊接;23-清除错误;24-手自动切换（高低电平）
    25-使能;26-去使能;27-使能/去使能;28-激光伺服跟踪启停信号;
    * @return 错误码
    */
    public int SetToolDIConfig(int[] config)

获取末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端可配置End-CI端口功能
    * @param [out] config End CI0-CI1功能编码；
    * 0-无;1-拖动示教工具开关;2-点记录信号;3-手自动切换（脉冲信号）;4-TPD记录启动/停止;5-暂停运动;
    6-恢复运动;7-启动;8-停止;9-暂停/恢复;10-启动/停止;11-力传感器辅助拖动开启;12-力传感器辅助拖动关闭;
    13-力传感器辅助拖动开启/关闭;14-激光检测信号X;15-激光检测信号Y;16-PTP运动至作业原点;17-运动中断，根据信号停止当前运动;
    18-启动主程序;19-启动倒带;20-启动确认;21-恢复焊接;22-终止焊接;23-清除错误;24-手自动切换（高低电平）
    25-使能;26-去使能;27-使能/去使能;28-激光伺服跟踪启停信号;
    * @return 错误码
    */
    public int GetToolDIConfig(out int[] config)
    
设置控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱可配置CI有效状态
    * @param [in] config CI0-CI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int SetDIConfigLevel(int[] config)
        
获取控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱可配置CI有效状态
    * @param [out] config CI0-CI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int GetDIConfigLevel(out int[] config)
        
设置控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱可配置CO有效状态
    * @param [in] config CO0-CO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int SetDOConfigLevel(int[] config)

获取控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱可配置CO有效状态
    * @param [out] config CO0-CO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int GetDOConfigLevel(out int[] config)
    
设置末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端可配置CI有效状态
    * @param [in] config CI0-CI1端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int SetToolDIConfigLevel(int[] config)
    
获取末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端可配置CI有效状态
    * @param [out] config CI0-CI1端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int GetToolDIConfigLevel(out int[] config)
    
设置控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱标准DI有效状态
    * @param [in] config DI0-DI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int SetStandardDILevel(int[] config)
    
获取控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱标准DI有效状态
    * @param [out] config DI0-DI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int GetStandardDILevel(out int[] config)

设置控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱标准DO有效状态
    * @param [in] config DO0-DO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int SetStandardDOLevel(int[] config)
    
获取控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱标准DO有效状态
    * @param [out] config DO0-DO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    public int GetStandardDOLevel(out int[] config)
        
机器人IO配置代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public void TestIOConfig()
    {
        int rtn = 0;

        // ---------- 测试可配置CI端口功能 ----------
        int[] setDIConfig = new int[] { 3, 9, 1, 4, 5, 6, 7, 8 };
        rtn = robot.SetDIConfig(setDIConfig);
        Console.WriteLine($"SetDIConfig rtn is {rtn}");

        // 使用 out 参数接收获取到的配置数组
        int[] getDIConfig;
        rtn = robot.GetDIConfig(out getDIConfig);  
        Console.WriteLine($"GetDIConfig rtn is {rtn}, value is {string.Join(" ", getDIConfig)}");

        // ---------- 测试可配置CO端口功能 ----------
        int[] setDOConfig = new int[] { 9, 10, 11, 12, 13, 14, 15, 16 };
        rtn = robot.SetDOConfig(setDOConfig);
        Console.WriteLine($"SetDOConfig rtn is {rtn}");

        int[] getDOConfig;
        rtn = robot.GetDOConfig(out getDOConfig);
        Console.WriteLine($"GetDOConfig rtn is {rtn}, value is {string.Join(" ", getDOConfig)}");

        // ---------- 测试末端可配置CI端口功能 ----------
        int[] setToolDIConfig = new int[] { 17, 18 };
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        Console.WriteLine($"SetToolDIConfig rtn is {rtn}");

        int[] getToolDIConfig;
        rtn = robot.GetToolDIConfig(out getToolDIConfig);
        Console.WriteLine($"GetToolDIConfig rtn is {rtn}, value is {string.Join(" ", getToolDIConfig)}");

        // ---------- 测试控制箱可配置CI有效状态 ----------
        int[] setDIConfigLevel = new int[] { 1, 1, 1, 1, 0, 0, 0, 0 };
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        Console.WriteLine($"SetDIConfigLevel rtn is {rtn}");

        int[] getDIConfigLevel;
        rtn = robot.GetDIConfigLevel(out getDIConfigLevel);
        Console.WriteLine($"GetDIConfigLevel rtn is {rtn}, value is {string.Join(" ", getDIConfigLevel)}");

        // ---------- 测试控制箱可配置CO有效状态 ----------
        int[] setDOConfigLevel = new int[] { 0, 0, 0, 0, 1, 1, 1, 1 };
        rtn = robot.SetDIConfigLevel(setDOConfigLevel);
        Console.WriteLine($"SetDOConfigLevel rtn is {rtn}");

        int[] getDOConfigLevel;
        rtn = robot.GetDOConfigLevel(out getDOConfigLevel);
        Console.WriteLine($"GetDOConfigLevel rtn is {rtn}, value is {string.Join(" ", getDOConfigLevel)}");

        // ---------- 测试末端可配置CI有效状态 ----------
        int[] setToolDIConfigLevel = new int[] { 1, 0 };
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        Console.WriteLine($"SetToolDIConfigLevel rtn is {rtn}");

        int[] getToolDIConfigLevel;
        rtn = robot.GetToolDIConfigLevel(out getToolDIConfigLevel);
        Console.WriteLine($"GetToolDIConfigLevel rtn is {rtn}, value is {string.Join(" ", getToolDIConfigLevel)}");

        // ---------- 测试控制箱标准DI有效状态 ----------
        int[] setStandardDILevel = new int[] { 1, 1, 1, 1, 0, 0, 0, 0 };
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        Console.WriteLine($"SetStandardDILevel rtn is {rtn}");

        int[] getStandardDILevel;
        rtn = robot.GetStandardDILevel(out getStandardDILevel);
        Console.WriteLine($"GetStandardDILevel rtn is {rtn}, value is {string.Join(" ", getStandardDILevel)}");

        // ---------- 测试控制箱标准DO有效状态 ----------
        int[] setStandardDOLevel = new int[] { 0, 0, 0, 0, 1, 1, 1, 1 };
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        Console.WriteLine($"SetStandardDOLevel rtn is {rtn}");

        int[] getStandardDOLevel;
        rtn = robot.GetStandardDOLevel(out getStandardDOLevel);
        Console.WriteLine($"GetStandardDOLevel rtn is {rtn}, value is {string.Join(" ", getStandardDOLevel)}");

    }