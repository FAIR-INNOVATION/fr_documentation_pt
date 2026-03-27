机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  机器人接口类构造函数
    */
    Robot robot = new Robot(); 

与控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  与机器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出场默认为192.168.58.2
    * @return 错误码
    */
    int RPC(String ip);

与机器人关闭通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 与机器人关闭通信
    * @return 错误码 
    */ 
    int CloseRPC(); 

查询SDK版本号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 查询 SDK 版本号 
    * @return 版本号 
    */  
    String GetSDKVersion();

获取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取控制器IP
    * @param  [out] ip  控制器IP
    * @return  错误码
    */
    int GetControllerIP(String[] ip);

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制机器人进入或退出拖动示教模式
    * @param  [in] state 0-退出拖动示教模式，1-进入拖动示教模式
    * @return  错误码
    */
    int DragTeachSwitch(int state);

查询机器人是否处于拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查询机器人是否处于拖动示教模式
    * @param  [in] state 0-非拖动示教模式，1-拖动示教模式
    * @return  错误码
    */
    int IsInDragTeach(List<Number> state);

控制机器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制机器人上使能或下使能，机器人上电后默认自动上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  错误码
    */
    int RobotEnable(int state); 

控制机器人手自动模式切换
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制机器人手自动模式切换
    * @param [in] mode 0-自动模式，1-手动模式
    * @return 错误码
    */
    int Mode(int mode);

关闭机器人操作系统
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 关闭机器人操作系统
    * @return 错误码
    */
    int ShutDownRobotOS();

设置与机器人通讯重连参数
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置与机器人通讯重连参数
    * @param [in] enable 是否使能，true:使能，false:不使能
    * @param [in] times 重连次数
    * @param [in] period 重连时间间隔
    * @return 错误码
    */
    int SetReconnectParam(boolean enable, int times, int period);

初始化日志参数
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 初始化日志参数
    * @param [in] logType 输出模式，DIRECT-直接输出；BUFFER-缓冲输出；ASYNC-异步输出
    * @param [in] logLevel 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @param [in] filePath 文件保存路径，如“D://Log/”
    * @param [in] saveFileNum 保存文件个数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @param [in] saveDays 保存文件天数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @return 错误码
    */
    int LoggerInit(FrLogType logType, FrLogLevel logLevel, String filePath, int saveFileNum, int saveDays)

设置日志过滤等级
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置日志过滤等级
    * @param [in] logLevel 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @return 错误码
    */
    int SetLoggerLevel(FrLogLevel logLevel)

机器人基础控制代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        String[] ip={""};
        String version = "";
        version=robot.GetSDKVersion();
        System.out.println("SDK version : " + version);
        int rtn = robot.GetControllerIP(ip);
        System.out.println("controller ip : " +  ip[0] + "  " + rtn);
        robot.Mode(1);//1-手动模式  0-自动模式
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);//进入拖动模式
        robot.Sleep(1000);
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        robot.Sleep(1000);
        robot.DragTeachSwitch(0);//退出拖动模式
        robot.Sleep(1000);
        pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        
        if (pkg.robot_state ==4){
           System.out.println("拖动模式");
        }else {
           System.out.println("非拖动模式");
        }
    }

获取机器人软件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人软件版本
    * @param [out] robotModel 机器人型号
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 错误码 
    */
    int GetSoftwareVersion(String robotModel, String webVersion, String controllerVersion);

获取机器人硬件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人硬件版本
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
    int GetHardwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

获取机器人固件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人固件版本
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
    int GetFirmwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

获取机器人软固件版本代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        String ctrlBoxBoardVersion = "";
        String driver1Version = "";
        String driver2Version = "";
        String driver3Version = "";
        String driver4Version = "";
        String driver5Version = "";
        String driver6Version = "";
        String endBoardVersion = "";
        robot.GetHardwareVersion(ctrlBoxBoardVersion ,driver1Version,  driver2Version,  driver3Version,
                 driver4Version,  driver5Version,  driver6Version,  endBoardVersion);

        robot.GetFirmwareVersion(ctrlBoxBoardVersion, driver1Version, driver2Version, driver3Version,
                driver4Version, driver5Version, driver6Version, endBoardVersion);
    }