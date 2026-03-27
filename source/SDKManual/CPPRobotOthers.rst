其他接口
=================

.. toctree:: 
    :maxdepth: 5

获取SSH公钥
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取SSH公钥
    * @param [out] keygen 公钥
    * @return 错误码
    */
    errno_t GetSSHKeygen(char keygen[1024]);

下发SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 下发SCP指令
    * @param [in] mode 0-上传（上位机->控制器），1-下载（控制器->上位机）
    * @param [in] sshname 上位机用户名
    * @param [in] sship 上位机ip地址
    * @param [in] usr_file_url 上位机文件路径
    * @param [in] robot_file_url 机器人控制器文件路径
    * @return 错误码
    */
    errno_t SetSSHScpCmd(int mode, char sshname[32], char sship[32], char usr_file_url[128], char robot_file_url[128]);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 计算指定路径下文件的MD5值
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码
    */
    errno_t ComputeFileMD5(char file_path[256], char md5[256]);

机器人SSH、MD5指令代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSSHMd5(void)
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
      char file_path[256] = "/fruser/airlab.lua";
      char md5[256] = { 0 };
      uint8_t emerg_state = 0;
      uint8_t si0_state = 0;
      uint8_t si1_state = 0;
      int sdk_com_state = 0;
      char ssh_keygen[1024] = { 0 };
      int retval = robot.GetSSHKeygen(ssh_keygen);
      printf("GetSSHKeygen retval is: %d\n", retval);
      printf("ssh key is: %s \n", ssh_keygen);
      char ssh_name[32] = "fr";
      char ssh_ip[32] = "192.168.58.45";
      char ssh_route[128] = "/home/fr";
      char ssh_robot_url[128] = "/root/robot/dhpara.config";
      retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
      printf("SetSSHScpCmd retval is: %d\n", retval);
      printf("robot url is: %s\n", ssh_robot_url);
      robot.ComputeFileMD5(file_path, md5);
      printf("md5 is: %s \n", md5);
      robot.CloseRPC();
      return 0;
    }

设置机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置机器人 20004 端口反馈周期
    * @param [in] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    errno_t SetRobotRealtimeStateSamplePeriod(int period);

获取机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人 20004 端口反馈周期
    * @param [out] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    errno_t GetRobotRealtimeStateSamplePeriod(int& period);

机器人20004端口状态反馈周期配置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestRealtimePeriod(void)
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
      robot.SetRobotRealtimeStateSamplePeriod(10);
      int getPeriod = 0;
      robot.GetRobotRealtimeStateSamplePeriod(getPeriod);
      cout << "period is " << getPeriod << endl;
      robot.Sleep(1000);
      robot.CloseRPC();
      return 0;
    }


机器人软件升级
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人软件升级
    * @param [in] filePath 软件升级包全路径
    * @param [in] block 是否阻塞至升级完成 true:阻塞；false:非阻塞
    * @return 错误码
    */
    errno_t SoftwareUpgrade(std::string filePath, bool block);

获取机器人软件升级状态
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人软件升级状态
    * @param [out] state 机器人软件包升级状态(0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败)
    * @return 错误码
    */
    errno_t GetSoftwareUpgradeState(int &state);

机器人软件升级代码示例
+++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestUpgrade(void)
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
      robot.SoftwareUpgrade("D://zUP/QNX/software.tar.gz", false);
      while (true)
      {
        int curState = -1;
        robot.GetSoftwareUpgradeState(curState);
        printf("upgrade state is %d\n", curState);
        robot.Sleep(300);
      }
      robot.CloseRPC();
      return 0;
    }

下载点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下载点位表数据库
    * @param [in] pointTableName 要下载的点位表名称    pointTable1.db
    * @param [in] saveFilePath 下载点位表的存储路径   C://test/
    * @return 错误码
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

上传点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传点位表数据库
    * @param [in] pointTableFilePath 上传点位表的全路径名   C://test/pointTable1.db
    * @return 错误码
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

点位表更新lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 点位表更新lua文件
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db",当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "testPointTable.lua"
    * @param [out] errorStr 切换点位表错误信息
    * @return 错误码
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

机器人点位表操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestPointTable(void)
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
      string save_path = "D://zDOWN/";
      string point_table_name = "point_table_FR5.db";
      rtn = robot.PointTableDownLoad(point_table_name, save_path);
      cout << "download : " << point_table_name << " fail: " << rtn << endl;
      string upload_path = "D://zUP/point_table_FR5.db";
      rtn = robot.PointTableUpLoad(upload_path);
      cout << "retval is: " << rtn << endl;
      string point_tablename = "point_table_FR5.db";
      string lua_name = "airlab.lua";
      rtn = robot.PointTableUpdateLua(point_tablename, lua_name);
      cout << "retval is: " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

控制器日志下载
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制器日志下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    errno_t RbLogDownload(std::string savePath);

所有数据源下载
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 所有数据源下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    errno_t AllDataSourceDownload(std::string savePath);

数据备份包下载
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 数据备份包下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    errno_t DataPackageDownload(std::string savePath);

下载控制器数据代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestDownLoadRobotData(void)
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
      rtn = robot.RbLogDownload("D://zDOWN/");
      cout << "RbLogDownload rtn is " << rtn << endl;
      rtn = robot.AllDataSourceDownload("D://zDOWN/");
      cout << "AllDataSourceDownload rtn is " << rtn << endl;
      rtn = robot.DataPackageDownload("D://zDOWN/");
      cout << "DataPackageDownload rtn is " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

设置关节固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置关节固件升级
    * @param [in] type 升级文件类型；1-升级固件(使用前需要使机器人进入boot模式)；2-升级从站配置文件(使用前需要去使能机器人)
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    errno_t SetJointFirmwareUpgrade(int type, std::string path);
  
设置控制箱固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱固件升级
    * @param [in] type 升级文件类型；1-升级固件(使用前需要使机器人进入boot模式)；2-升级从站配置文件(使用前需要去使能机器人)
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    errno_t SetCtrlFirmwareUpgrade(int type, std::string path);
  
设置末端固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端固件升级
    * @param [in] type 升级文件类型；1-升级固件(使用前需要使机器人进入boot模式)；2-升级从站配置文件(使用前需要去使能机器人)
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    errno_t SetEndFirmwareUpgrade(int type, std::string path);

关节全参数配置文件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 关节全参数配置文件升级(使用前需要去使能机器人)
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    errno_t JointAllParamUpgrade(std::string path);
    
机器人从站固件升级代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestFirmWareUpgrade()
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
    robot.RobotEnable(0);
    robot.Sleep(200);
    rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/jointallparameters.db");
    printf("robot JointAllParamUpgrade rtn is %d\n", rtn);
    rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
    printf("robot SetCtrlFirmwareUpgrade config param rtn is %d\n", rtn);
    rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
    printf("robot SetEndFirmwareUpgrade config param rtn is %d\n", rtn);
    robot.SetSysServoBootMode();
    rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/upgrade/FR_CTRL_PRIMCU_FV201212_MAIN_U4_T01_20250428(MT).bin");
    printf("robot SetCtrlFirmwareUpgrade rtn is %d\n", rtn);
    rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/upgrade/FR_END_FV201009_MAIN_U1_T01_20250428.bin");
    printf("robot SetEndFirmwareUpgrade rtn is %d\n", rtn);
    rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/upgrade/FR_SERVO_FV504214_MAIN_U7_T07_20250519.bin");
    printf("robot SetJointFirmwareUpgrade rtn is %d\n", rtn);
    robot.CloseRPC();
    return 0;
    }

机器人操作系统升级(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人操作系统升级(LA控制箱)
    * @param [in] filePath 操作系统升级包全路径
    * @return 错误码
    */
    errno_t KernelUpgrade(std::string filePath);
        
获取机器人操作系统升级结果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人操作系统升级结果(LA控制箱)
    * @param [out] result 升级结果：0:成功；-1:失败
    * @return 错误码
    */
    errno_t GetKernelUpgradeResult(int& result);
        
机器人MCU日志生成
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人MCU日志生成
    * @return 错误码
    */
    errno_t RobotMCULogCollect();
        
设置端口通讯断开时停止机器人运行
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置端口通讯断开时停止机器人运行
    * @param [in] pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param [in] enable 0-关闭；1-开启
    * @param [in] confirmTime 通讯中断确认时长(ms)[0-5000]
    * @return 错误码
    */
    errno_t SetRobotStopOnComDisc(int pordID, bool enable, int confirmTime);
        
获取端口通讯断开时停止机器人运行参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取端口通讯断开时停止机器人运行参数
    * @param [in] pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param [out] enable 0-关闭；1-开启
    * @param [out] confirmTime 通讯中断确认时长(ms)[0-5000]
    * @return 错误码
    */
    errno_t GetRobotStopOnComDisc(int pordID, bool &enable, int &confirmTime);

端口通讯断开时停止机器人运行参数代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestRobotStopOnComDisc()
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
        bool enable = false;
        int confirmTime = 0;
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        printf("SetRobotStopOnComDisc %d\n", rtn);
        robot.GetRobotStopOnComDisc(0, enable, confirmTime);
        printf("GetRobotStopOnComDisc 8080 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(1, enable, confirmTime);
        printf("GetRobotStopOnComDisc 80803 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(2, enable, confirmTime);
        printf("GetRobotStopOnComDisc 20002 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.GetRobotStopOnComDisc(3, enable, confirmTime);
        printf("GetRobotStopOnComDisc 20004 rtn %d; enable is %d; confirm time is %d\n", rtn, enable, confirmTime);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

UDP发送指令帧
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief UDP发送指令帧
    * @param [in] frame 发送数据帧字符串如：/f/bIII20III303III7IIIMode(0)III/b/f
    * @return 错误码
    */
    errno_t SendUDPFrame(std::string frame);

设置SDK通过UDP发送指令的执行结果回调函数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置SDK通过UDP发送指令的执行结果回调函数
    * @param [in] CallBack 回调函数；comType-指令结果通讯回复类型0-TCP，1-UDP；count-指令回复帧计数；cmdID-指令编号；contentLen-数据长度；content-数据内容
    * @return 错误码
    */
    errno_t SetCmdRpyCallback(void (*CallBack)(int comType, int count, int cmdID, int contentLen, std::string content));

UDP指令下发代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSendUDPFrame()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.SetCmdRpyCallback(UDPFrameCallBack);
        printf("SetCmdRpyCallback rtn is %d\n", rtn);
        rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame Mode(0) rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII21III303III7IIIMode(1)III/b/f");
        printf("SendUDPFrame Mode(1) rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII49III201III184IIIMoveJ(-15.625, -82.680, 101.654, -110.950, -88.290, 0.017, -383.012, -2.325, 242.655, -178.024, 1.710, 74.416, 0, 0, 100, 100, 100, 0.000, 0.000, 0.000, 0.000, -1, 0, 0, 0, 0, 0, 0, 0)III/b/f");
        printf("SendUDPFrame MoveJ(-15.625 rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII48III203III199IIIMoveL(-75.622, -82.680, 101.654, -110.950, -88.290, 0.017, -193.537, 330.525, 242.657, -178.024, 1.710, 14.420, 0, 0, 100, 100, 100, -1, 0, 0.000, 0.000, 0.000, 0.000, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0)III/b/f");
        printf("SendUDPFrame MoveL(-75.622 rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII4III905III20IIIGetSoftwareVersion()III/b/f");
        printf("SendUDPFrame GetSoftwareVersion() rtn is %d\n", rtn);
        robot.Sleep(1000);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("III20III303III7IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bIII20III303III6IIIMode(0)III/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/b|||20|||303|||7|||Mode(0)|||/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        rtn = robot.SendUDPFrame("/f/bII20II303II7IIMode(0)II/b/f");
        printf("SendUDPFrame rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }
    
设置用户自定义机器人末端灯色
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置用户自定义机器人末端灯色
    * @param [in] r 末端红灯控制；0-灭；1-亮
    * @param [in] g 末端绿灯控制；0-灭；1-亮
    * @param [in] b 末端蓝灯控制；0-灭；1-亮
    * @return 错误码
    */
    errno_t SetUserLEDColor(bool r, bool g, bool b);
        
设置用户自定义机器人末端灯色代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestUserLedColor()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return 0;
        }
        robot.SetReConnectParam(true, 30000, 500);
        robot.SetUserLEDColor(true, true, true);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(true, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, true, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, true);
        robot.Sleep(1000);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }