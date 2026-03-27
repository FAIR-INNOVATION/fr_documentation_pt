机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  机器人接口类构造函数
    */
    FRRobot();

与控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  与机器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出场默认为192.168.58.2
    * @return 错误码
    */
    errno_t  RPC(const char *ip);

与控制器关闭通讯
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  与机器人控制器关闭通讯
     * @return 错误码
     */
    errno_t  CloseRPC();

查询SDK版本号
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查询SDK版本号
    * @param  [out] version   SDK版本号
    * @return  错误码
    */  
    errno_t  GetSDKVersion(char *version);

获取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取控制器IP
    * @param  [out] ip  控制器IP
    * @return  错误码
    */
    errno_t  GetControllerIP(char *ip);

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制机器人进入或退出拖动示教模式
    * @param  [in] state 0-退出拖动示教模式，1-进入拖动示教模式
    * @return  错误码
    */
    errno_t  DragTeachSwitch(uint8_t state);

查询机器人是否处于拖动模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查询机器人是否处于拖动示教模式
    * @param  [out] state 0-非拖动示教模式，1-拖动示教模式
    * @return  错误码
    */
    errno_t  IsInDragTeach(uint8_t *state);

控制机器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制机器人上使能或下使能，机器人上电后默认自动上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  错误码
    */
    errno_t  RobotEnable(uint8_t state);

控制机器人手自动模式切换
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制机器人手自动模式切换
    * @param [in] mode 0-自动模式，1-手动模式
    * @return 错误码
    */
    errno_t  Mode(int mode);

关闭机器人操作系统
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 关闭机器人操作系统
    * @return 错误码
    */
    errno_t ShutDownRobotOS();

设置与机器人通讯重连参数
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置与机器人通讯重连参数
    * @param [in] enable 网络故障时使能重连 true-使能 false-不使能
    * @param [in] reconnectTime 重连时间，单位ms
    * @param [in] period 重连周期，单位ms
    * @return 错误码
    */
    errno_t SetReConnectParam(bool enable, int reconnectTime = 30000, int period = 50);

关闭机器人操作系统
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 关闭机器人操作系统
    * @return 错误码
    */
    int ShutDownRobotOS();

初始化日志参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 初始化日志参数;
    * @param output_model：输出模式，0-直接输出；1-缓冲输出；2-异步输出;
    * @param file_path: 文件保存路径+名称，,长度上限256，名称必须是xxx.log的形式，比如/home/fr/linux/fairino.log;
    * @param file_num：滚动存储的文件数量，1~20个.单个文件上限50M;
    * @return errno_t 错误码;
    */
	errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

设置日志过滤等级
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param lvl: 过滤等级值，值越小输出日志越少，默认值是1. 1-error, 2-warnning, 3-inform, 4-debug;
    */
    void SetLoggerLevel(int lvl = 1);

机器人基础控制代码示例
++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestRobotCtrl(void)
    {
            ROBOT_STATE_PKG pkg = {};
            FRRobot robot;
            robot.LoggerInit();
            robot.SetLoggerLevel(1);
            int rtn = robot.RPC("192.168.58.2");
            robot.SetReConnectParam(true, 30000, 500);
            char ip[64] = "";
            char version[64] = "";
            uint8_t state;
            robot.GetSDKVersion(version);
            printf("SDK version:%s\n", version);
            robot.GetControllerIP(ip);
            printf("controller ip:%s\n", ip);
            robot.Mode(1);
            robot.Sleep(1000);
            robot.DragTeachSwitch(1);
            robot.Sleep(1000);
            robot.IsInDragTeach(&state);
            printf("drag state :%u\n", state);
            robot.Sleep(3000);
            robot.DragTeachSwitch(0);
            robot.Sleep(1000);
            robot.IsInDragTeach(&state);
            printf("drag state :%u\n", state);
            robot.Sleep(3000);
            robot.RobotEnable(0);
            robot.Sleep(3000);
            robot.RobotEnable(1);
            robot.Mode(0);
            robot.Sleep(1000);
            robot.Mode(1);
            robot.Sleep(3000);
            robot.ShutDownRobotOS();
            robot.CloseRPC();
            return 0;
    }

获取机器人软件版本代码示例
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人软件版本
    * @param[out]	robotModel 机器人型号
    * @param[out]	webversion web版本
    * @param[out]	controllerVersion 控制器版本
    * @return 错误码
    */
    errno_t GetSoftwareVersion(char robotModel[64], char webVersion[64], char controllerVersion[64]);

获取机器人硬件版本
+++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人硬件版本
    * @param[out] ctrlBoxBoardversion 控制箱载板硬件版本
    * @param[out] driver1version 驱动器1硬件版本
    * @param[out] driver2version 驱动器2硬件版本
    * @param[out] driver3version 驱动器3硬件版本
    * @param[out] driver4version 驱动器4硬件版本
    * @param[out] driver5version 驱动器5硬件版本
    * @param[out] driver6version 驱动器6硬件版本
    * @param[out] endBoardversion 未端版硬件版本
    */
    errno_t GetHardwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

获取机器人固件版本
+++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人固件版本
    * @param[out] ctrlBoxBoardversion 控制箱载板固件版本
    * @param[out] driver1version 驱动器1固件版本
    * @param[out] driver2version 驱动器2固件版本
    * @param[out] driver3version 驱动器3固件版本
    * @param[out] driver4version 驱动器4固件版本
    * @param[out] driver5version 驱动器5固件版本
    * @param[out] driver6version 驱动器6固件版本
    * @param[out] endBoardversion 未端版固件版本
    */
    errno_t GetFirmwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

获取机器人软固件版本代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGetVersions(void)
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
         char robotModel[64] = { 0 };
         char webversion[64] = { 0 };
         char controllerVersion[64] = { 0 };
         char ctrlBoxBoardversion[128] = { 0 };
         char driver1version[128] = { 0 };
         char driver2version[128] = { 0 };
         char driver3version[128] = { 0 };
         char driver4version[128] = { 0 };
         char driver5version[128] = { 0 };
         char driver6version[128] = { 0 };
         char endBoardversion[128] = { 0 };
         rtn = robot.GetSoftwareVersion(robotModel, webversion, controllerVersion);
         printf("Getsoftwareversion rtn is: %d\n", rtn);
         printf("robotmodel is: %s, webversion is: %s, controllerVersion is: %s \n\n", robotModel, webversion, controllerVersion);
         rtn = robot.GetHardwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetHardwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         rtn = robot.GetFirmwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetFirmwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         robot.CloseRPC();
         return 0;
     }
