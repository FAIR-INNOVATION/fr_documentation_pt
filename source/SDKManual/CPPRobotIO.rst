机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置控制箱数字量输出
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

设置工具数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置工具数字量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetToolDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

设置控制箱模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置控制箱模拟量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetAO(int id, float value, uint8_t block);

设置工具模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置工具模拟量输出
    * @param  [in] id  io编号，范围[0]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetToolAO(int id, float value, uint8_t block);

设置数字量、模拟量输出代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestAODO(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 1;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         status = 0;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetToolAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         robot.CloseRPC();
         return 0;
     }

获取控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    errno_t  GetDI(int id, uint8_t block, uint8_t *result);

获取工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    errno_t  GetToolDI(int id, uint8_t block, uint8_t *result);

获取控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    errno_t  GetAI(int id, uint8_t block, float *result); 

获取工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    errno_t  GetToolAI(int id, uint8_t block, float *result);

获取机器人末端点记录按钮状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人末端点记录按钮状态
     * @param [out] state 按钮状态，0-按下，1-松开
     * @return 错误码
     */
    errno_t  GetAxlePointRecordBtnState(uint8_t *state);

获取机器人末端DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人末端DO输出状态
     * @param [out] do_state DO输出状态，do0~do1对应bit1~bit2,从bit0开始
     * @return 错误码
     */
    errno_t  GetToolDO(uint8_t *do_state);

获取机器人控制器DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人控制器DO输出状态
     * @param [out] do_state_h DO输出状态，co0~co7对应bit0~bit7
     * @param [out] do_state_l DO输出状态，do0~do7对应bit0~bit7
     * @return 错误码
     */
    errno_t  GetDO(uint8_t *do_state_h, uint8_t *do_state_l);

获取机器人DI、DO状态代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestGetDIAI(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         robot.GetDI(0, block, &di);
         printf("di0:%u\n", di);
         tool_di = robot.GetToolDI(1, block, &tool_di);
         printf("tool_di1:%u\n", tool_di);
         robot.GetAI(0, block, &ai);
         printf("ai0:%f\n", ai);
         tool_ai = robot.GetToolAI(0, block, &tool_ai);
         printf("tool_ai0:%f\n", tool_ai);
         uint8_t _button_state = 0;
         robot.GetAxlePointRecordBtnState(&_button_state);
         printf("_button_state is: %u\n", _button_state);
         uint8_t tool_do_state = 0;
         robot.GetToolDO(&tool_do_state);
         printf("tool DO state is: %u\n", tool_do_state);
         uint8_t do_state_h = 0;
         uint8_t do_state_l = 0;
         robot.GetDO(&do_state_h, &do_state_l);
         printf("DO state high is: %u \n DO state low is: %u\n", do_state_h, do_state_l);
         robot.CloseRPC();
         return 0;
     }

等待控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitDI(int id, uint8_t status, int max_time, int opt);

等待控制箱多路数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  WaitMultiDI(int mode, int id, uint8_t status, int max_time, int opt);

等待工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitToolDI(int id, uint8_t status, int max_time, int opt);

等待控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  WaitAI(int id, int sign, float value, int max_time, int opt);  

等待工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  WaitToolAI(int id, int sign, float value, int max_time, int opt); 

等待控制箱数字、模拟输入信号代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionchanged:: C++SDK-v2.1.2.0
    
.. code-block:: c++
    :linenos:

     int TestWaitDIAI(void)
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
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         rtn = robot.WaitDI(0, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitMultiDI(1, 3, 3, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolDI(1, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }


设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱DO停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    errno_t SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag = 0);

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱AO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    errno_t SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag = 0);

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端工具DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return 错误码
    */
    errno_t SetOutputResetAxleDO(int resetFlag, int reloadFlag = 0);

设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端工具AO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return  错误码
    */
    errno_t SetOutputResetAxleAO(int resetFlag, int reloadFlag = 0);

设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return  错误码
    */
    errno_t SetOutputResetExtDO(int resetFlag, int reloadFlag = 0);

设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展AO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return  错误码
    */
    errno_t SetOutputResetExtAO(int resetFlag, int reloadFlag = 0);

设置SmartTool停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置SmartTool停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @param [in] reloadFlag 暂停恢复后是否重加载，0-不加载；1-加载
    * @return  错误码
    */
    errno_t SetOutputResetSmartToolDO(int resetFlag, int reloadFlag = 0);

设置LUA程序停止/暂停后输出复位代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestDOReset(void)
    {
    ROBOT_STATE_PKG pkg = {};
    FRRobot robot;
    robot.LoggerInit();
    robot.SetLoggerLevel(3);
    int rtn = robot.RPC("192.168.58.2");
    if (rtn != 0)
    {
        return -1;
    }
    robot.SetReConnectParam(true, 30000, 500);
    for (int i = 0; i < 16; i++)
    {
        robot.SetDO(i, 1, 0, 0);
        robot.Sleep(200);
    }
    int resetFlag = 0;
    int resumeReloadFlag = 0;
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);
    robot.ProgramLoad("/fruser/test.lua");
    robot.ProgramRun();
    robot.Sleep(2000);
    robot.PauseMotion();
    robot.Sleep(2000);
    robot.ResumeMotion();
    robot.Sleep(2000);
    robot.CloseRPC();
    return 0;
    }

设置控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t SetDIConfig(int config[8]);

获取控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t GetDIConfig(int config[8]);

设置控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t SetDOConfig(int config[8]);

获取控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t GetDOConfig(int config[8]);

设置末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t SetToolDIConfig(int config[2]);

获取末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
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
    errno_t GetToolDIConfig(int config[2]);
    
设置控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱可配置CI有效状态
    * @param [in] config CI0-CI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t SetDIConfigLevel(int config[8]);
        
获取控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取控制箱可配置CI有效状态
    * @param [out] config CI0-CI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t GetDIConfigLevel(int config[8]);
        
设置控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱可配置CO有效状态
    * @param [in] config CO0-CO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t SetDOConfigLevel(int config[8]);

获取控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取控制箱可配置CO有效状态
    * @param [out] config CO0-CO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t GetDOConfigLevel(int config[8]);
    
设置末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端可配置CI有效状态
    * @param [in] config CI0-CI1端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t SetToolDIConfigLevel(int config[2]);
    
获取末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取末端可配置CI有效状态
    * @param [out] config CI0-CI1端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t GetToolDIConfigLevel(int config[2]);
    
设置控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱标准DI有效状态
    * @param [in] config DI0-DI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t SetStandardDILevel(int config[8]);
    
获取控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取控制箱标准DI有效状态
    * @param [out] config DI0-DI7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t GetStandardDILevel(int config[8]);

设置控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱标准DO有效状态
    * @param [in] config DO0-DO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t SetStandardDOLevel(int config[8]);
    
获取控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取控制箱标准DO有效状态
    * @param [out] config DO0-DO7端口有效状态；0-高电平有效；1-低电平有效
    * @return 错误码
    */
    errno_t GetStandardDOLevel(int config[8]);
        
机器人IO配置代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestIOConfig()
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
        int setDIConfig[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int getDIConfig[8] = { 0 };
        rtn = robot.SetDIConfig(setDIConfig);
        printf("SetDIConfig rtn is %d\n", rtn);
        rtn = robot.GetDIConfig(getDIConfig);
        printf("GetDIConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn, 
            getDIConfig[0], getDIConfig[1], getDIConfig[2], getDIConfig[3], getDIConfig[4], getDIConfig[5], getDIConfig[6], getDIConfig[7]);
        int setDOConfig[8] = { 9, 10, 11, 12, 13, 14, 15, 16 };
        int getDOConfig[8] = { 0 };
        rtn = robot.SetDOConfig(setDOConfig);
        printf("SetDOConfig rtn is %d\n", rtn);
        rtn = robot.GetDOConfig(getDOConfig);
        printf("GetDOConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfig[0], getDOConfig[1], getDOConfig[2], getDOConfig[3], getDOConfig[4], getDOConfig[5], getDOConfig[6], getDOConfig[7]);
        int setToolDIConfig[2] = { 17, 18 };
        int getToolDIConfig[2] = { 0 };
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        printf("SetToolDIConfig rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfig(getToolDIConfig);
        printf("GetToolDIConfig rtn is %d, value is %d %d \n", rtn, getToolDIConfig[0], getToolDIConfig[1]);
        int setDIConfigLevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getDIConfigLevel[8] = { 0 };
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        printf("SetDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDIConfigLevel(getDIConfigLevel);
        printf("GetDIConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDIConfigLevel[0], getDIConfigLevel[1], getDIConfigLevel[2], getDIConfigLevel[3], getDIConfigLevel[4], getDIConfigLevel[5], getDIConfigLevel[6], getDIConfigLevel[7]);
        int setDOConfigLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getDOConfigLevel[8] = { 0 };
        rtn = robot.SetDOConfigLevel(setDOConfigLevel);
        printf("SetDOConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDOConfigLevel(getDOConfigLevel);
        printf("GetDOConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfigLevel[0], getDOConfigLevel[1], getDOConfigLevel[2], getDOConfigLevel[3], getDOConfigLevel[4], getDOConfigLevel[5], getDOConfigLevel[6], getDOConfigLevel[7]);
        int setToolDIConfigLevel[2] = { 1, 0 };
        int getToolDIConfigLevel[2] = { 0 };
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        printf("SetToolDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfigLevel(getToolDIConfigLevel);
        printf("GetToolDIConfigLevel rtn is %d, value is %d %d \n", rtn, getToolDIConfigLevel[0], getToolDIConfigLevel[1]);
        int setStandardDILevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getStandardDILevel[8] = { 0 };
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        printf("SetStandardDILevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDILevel(getStandardDILevel);
        printf("GetStandardDILevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDILevel[0], getStandardDILevel[1], getStandardDILevel[2], getStandardDILevel[3], getStandardDILevel[4], getStandardDILevel[5], getStandardDILevel[6], getStandardDILevel[7]);
        int setStandardDOLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getStandardDOLevel[8] = { 0 };
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        printf("SetStandardDOLevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDOLevel(getStandardDOLevel);
        printf("GetStandsrdDOLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDOLevel[0], getStandardDOLevel[1], getStandardDOLevel[2], getStandardDOLevel[3], getStandardDOLevel[4], getStandardDOLevel[5], getStandardDOLevel[6], getStandardDOLevel[7]);
        robot.Sleep(2000);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }