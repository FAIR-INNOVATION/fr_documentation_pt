机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  机器人接口类构造函数
    */
    Robot(); 

与控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  与机器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出场默认为192.168.58.2
    * @return 错误码
    */
    int RPC(string ip);

与机器人断开通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 与机器人控制器断开通信 
    * @return 错误码 
    */ 
    int CloseRPC(); 

查询SDK版本号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 查询 SDK 版本号 
    * @param [out] version SDK 版本号 
    * @return 错误码 
    */  
    int GetSDKVersion(ref string version);

获取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制器IP
    * @param  [out] ip  控制器IP
    * @return  错误码
    */
    int GetControllerIP(ref string ip);

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制机器人进入或退出拖动示教模式
    * @param  [in] state 0-退出拖动示教模式，1-进入拖动示教模式
    * @return  错误码
    */
    int DragTeachSwitch(byte state);

查询机器人是否处于拖动模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查询机器人是否处于拖动示教模式
    * @param  [out] state 0-非拖动示教模式，1-拖动示教模式
    * @return  错误码
    */
    int IsInDragTeach(ref byte state); 

控制机器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制机器人上使能或下使能，机器人上电后默认自动上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  错误码
    */
    int RobotEnable(byte state); 

控制机器人手自动模式切换
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制机器人手自动模式切换
    * @param [in] mode 0-自动模式，1-手动模式
    * @return 错误码
    */
    int Mode(int mode);

关闭机器人操作系统
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 关闭机器人操作系统
    * @return 错误码
    */
    int ShutDownRobotOS();

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        int rtn = robot.ShutDownRobotOS();
        Console.WriteLine($"ShutDownRobotOS rtn is {rtn}");
    }

设置与机器人通讯重连参数
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置与机器人通讯重连参数
    * @param [in] enable 是否开启 true-使能，false-不使能
    * @param [in] times 重连次数
    * @param [in] period 重连时间间隔（毫秒）
    */
    void SetReconnectParam(bool enable, int times, int period);

代码示例
+++++++++++++
.. code-block:: c#
    :linenos:

    private void btnStandard_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 20000);//断线重连参数
        robot.RPC("192.168.58.2"); 

        string ip = "";
        string version = "";
        byte state = 0;

        robot.GetSDKVersion(ref version);
        Console.WriteLine($"SDK version : {version}");
        robot.GetControllerIP(ref ip);
        Console.WriteLine($"controller ip : {ip}");

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        int rtn = robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.DragTeachSwitch(0);
        Thread.Sleep(1000);
        robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.RobotEnable(0);
        Thread.Sleep(3000);
        robot.RobotEnable(1);

        robot.Mode(0);
        Thread.Sleep(1000);
        robot.Mode(1);
    }

初始化日志参数
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 初始化日志参数
    * @param [in] logType：输出模式，DIRECT-直接输出；BUFFER-缓冲输出；ASYNC-异步输出
    * @param [in] logLevel：日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @param [in] filePath: 文件保存路径，如“D://Log/”
    * @param [in] saveFileNum：保存文件个数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @param [in] saveDays: 保存文件天数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @return 错误码
    */
    int LoggerInit(FrLogType logType = FrLogType.DIRECT, FrLogLevel logLevel = FrLogLevel.INFO, string filePath = "", int saveFileNum = 10, int saveDays = 10);

设置日志过滤等级
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置日志过滤等级
    * @param [in] logLevel: 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @return 错误码
    */
    int SetLoggerLevel(FrLogLevel logLevel);

获取机器人软件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人软件版本信息
    * @param [out] robotModel 机器人型号
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 错误码 
    */ 
    int GetSoftwareVersion(ref string robotModel, ref string webVersion, ref string controllerVersion);
    
获取机器人硬件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人硬件版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱载板硬件版本
    * @param [out] driver1Version 驱动器1硬件版本
    * @param [out] driver1Version 驱动器2硬件版本
    * @param [out] driver1Version 驱动器3硬件版本
    * @param [out] driver1Version 驱动器4硬件版本
    * @param [out] driver1Version 驱动器5硬件版本
    * @param [out] driver1Version 驱动器6硬件版本
    * @param [out] endBoardVersion 末端板硬件版本
    * @return 错误码 
    */ 
    int GetHardwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

获取机器人固件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人固件版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱载板固件版本
    * @param [out] driver1Version 驱动器1固件版本
    * @param [out] driver1Version 驱动器2固件版本
    * @param [out] driver1Version 驱动器3固件版本
    * @param [out] driver1Version 驱动器4固件版本
    * @param [out] driver1Version 驱动器5固件版本
    * @param [out] driver1Version 驱动器6固件版本
    * @param [out] endBoardVersion 末端板固件版本
    * @return 错误码 
    */ 
    int GetFirmwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnGetVersions_Click(object sender, EventArgs e)
    {
        string[] ver = new string[20];
        int rtn = 0;
        rtn = robot.GetSoftwareVersion(ref ver[0], ref ver[1], ref ver[2]);
        rtn = robot.GetHardwareVersion(ref ver[3], ref ver[4], ref ver[5], ref ver[6], ref ver[7], ref ver[8], ref ver[9], ref ver[10]);
        rtn = robot.GetFirmwareVersion(ref ver[11], ref ver[12], ref ver[13], ref ver[14], ref ver[15], ref ver[16], ref ver[17], ref ver[18]);
        Console.WriteLine($"robotmodel  is: {ver[0]}");
        Console.WriteLine($"webVersion  is: {ver[1]}");
        Console.WriteLine($"controllerVersion  is: {ver[2]}");
        Console.WriteLine($"Hard ctrlBox Version  is: {ver[3]}");
        Console.WriteLine($"Hard driver1 Version  is: {ver[4]}");
        Console.WriteLine($"Hard driver2 Version  is: {ver[5]}");
        Console.WriteLine($"Hard driver3 Version  is: {ver[6]}");
        Console.WriteLine($"Hard driver4 Version  is: {ver[7]}");
        Console.WriteLine($"Hard driver5 Version  is: {ver[8]}");
        Console.WriteLine($"Hard driver6 Version  is: {ver[9]}");
        Console.WriteLine($"Hard end Version  is: {ver[10]}");
        Console.WriteLine($"Firm ctrlBox Version  is: {ver[11]}");
        Console.WriteLine($"Firm driver1 Version  is: {ver[12]}");
        Console.WriteLine($"Firm driver2 Version  is: {ver[13]}");
        Console.WriteLine($"Firm driver3 Version  is: {ver[14]}");
        Console.WriteLine($"Firm driver4 Version  is: {ver[15]}");
        Console.WriteLine($"Firm driver5 Version  is: {ver[16]}");
        Console.WriteLine($"Firm driver6 Version  is: {ver[17]}");
        Console.WriteLine($"Firm end Version  is: {ver[18]}");
    }