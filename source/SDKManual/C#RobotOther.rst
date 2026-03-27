其他接口
================

.. toctree:: 
    :maxdepth: 5

获取SSH公钥
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SSH公钥 
    * @param [out] keygen 公钥
    * @return 错误码 
    */
    int GetSSHKeygen(ref string keygen);

下发SCP指令
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
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
    int SetSSHScpCmd(int mode, string sshname, string sship, string usr_file_url, string robot_file_url);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算指定路径下文件的MD5值 
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码 
    */
    int ComputeFileMD5(string file_path, ref string md5);

机器人SSH、MD5指令代码示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        string file_path = "/fruser/airlab.lua";
        string md5 = "";
        byte emerg_state = 0;
        byte si0_state = 0;
        byte si1_state = 0;
        int sdk_com_state = 0;

        string ssh_keygen = "";
        int retval = robot.GetSSHKeygen(ref ssh_keygen);
        Console.WriteLine("GetSSHKeygen retval is: {0}", retval);
        Console.WriteLine("ssh key is: {0}", ssh_keygen);

        string ssh_name = "fr";
        string ssh_ip = "192.168.58.45";
        string ssh_route = "/home/fr";
        string ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        Console.WriteLine("SetSSHScpCmd retval is: {0}", retval);
        Console.WriteLine("robot url is: {0}", ssh_robot_url);

        robot.ComputeFileMD5(file_path, ref md5);
        Console.WriteLine("md5 is: {0}", md5);
    }

设置机器人 20004 端口反馈周期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人 20004 端口反馈周期
    * @param [in] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    int SetRobotRealtimeStateSamplePeriod(int period);

获取机器人 20004 端口反馈周期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人 20004 端口反馈周期
    * @param [out] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    int GetRobotRealtimeStateSamplePeriod((ref int period);   

机器人20004端口状态反馈周期配置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button47_Click(object sender, EventArgs e)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        int getPeriod = 0;
        robot.GetRobotRealtimeStateSamplePeriod(ref getPeriod);
        Console.WriteLine("period is {0}", getPeriod);
        Thread.Sleep(1000);
    }

机器人软件升级
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 机器人软件升级
    * @param [in] filePath 软件升级包全路径
    * @param [in] block 是否阻塞至升级完成 true:阻塞；false:非阻塞
    * @return  错误码
    */
    int SoftwareUpgrade(string filePath, bool block);

获取机器人软件升级状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人软件升级状态
    * @param [out] state 机器人软件包升级状态  0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败
    * @return  错误码
    */
    int GetSoftwareUpgradeState(ref int state);

机器人软件升级代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button48_Click(object sender, EventArgs e)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            int curState = -1;
            robot.GetSoftwareUpgradeState(ref curState);
            Console.WriteLine("upgrade state is {0}", curState);
            Thread.Sleep(300);
        }
    }

下载点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从机器人控制器下载到本地计算机 
    * @param [in] pointTableName 控制器中的点位表名称：pointTable1.db
    * @param [in] saveFilePath 点位表下载到计算机的路径 C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

上传点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从本地计算机上传至机器人控制器 
    * @param [in] pointTableFilePath 点位表在本地计算机的绝对路径C://test/pointTabl e1.db
    * @return 错误码 
    */
    int PointTableUpLoad(string pointTableFilePath);

点位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用给定的点位表更新lua程序中的点
    * @param [in] pointTableName 控制器中的点位表名称："pointTable1.db", 当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "test.lua"
    * @param [out] errorStr 点位表更新lua错误信息  
    * @return 错误码 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

切换点位表并应用
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 切换点位表并应用
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db"
    * @param [out] errorStr 切换点位表错误信息   
    * @return 错误码 
    */
    int PointTableSwitch(string pointTableName, ref string errorStr);

机器人点位表操作代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        string save_path = "D://zDOWN/";
        string point_table_name = "test_point_A.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);
        Console.WriteLine("download : {0} fail: {1}", point_table_name, rtn);

        string upload_path = "D://zUP/test_point_A.db";
        rtn = robot.PointTableUpLoad(upload_path);
        Console.WriteLine("retval is: {0}", rtn);

        string point_tablename = "test_point_A.db";
        string lua_name = "Text1.lua";

        string errorStr = "";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name, ref errorStr);
        Console.WriteLine("retval is: {0}", rtn);
    }

控制器日志下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制器日志下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int RbLogDownload(string savePath);

所有数据源下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 所有数据源下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int AllDataSourceDownload(string savePath);

数据备份包下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 数据备份包下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int DataPackageDownload(string savePath);

下载控制器数据代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button50_Click(object sender, EventArgs e)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");
        Console.WriteLine("RbLogDownload rtn is {0}", rtn);

        rtn = robot.AllDataSourceDownload("D://zDOWN/");
        Console.WriteLine("AllDataSourceDownload rtn is {0}", rtn);

        rtn = robot.DataPackageDownload("D://zDOWN/");
        Console.WriteLine("DataPackageDownload rtn is {0}", rtn);
    }

机器人操作系统升级(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 机器人操作系统升级(LA控制箱)
     * @param [in] filePath 操作系统升级包全路径
     * @return  错误码
     */
    public int KernelUpgrade(string filePath)

获取机器人操作系统升级结果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 获取机器人操作系统升级结果(LA控制箱)
     * @param [out] result 升级结果：0:成功；-1:失败
     * @return  错误码
     */
    public int GetKernelUpgradeResult(ref int[] result)

设置编码器升级
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置编码器升级
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int SetEncoderUpgrade(string path);

设置关节固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置关节固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int SetJointFirmwareUpgrade(int type, string path);

设置控制箱固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置控制箱固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int SetCtrlFirmwareUpgrade(int type, string path);

设置末端固件升级
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int SetEndFirmwareUpgrade(int type, string path);

关节全参数配置文件升级
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 关节全参数配置文件升级
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int JointAllParamUpgrade(string path);

机器人从站固件升级代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    private void button83_Click(object sender, EventArgs e)
    {
        robot.RobotEnable(0);
        Thread.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/jointallparameters.db");
        Console.WriteLine($"robot JointAllParamUpgrade rtn is{rtn}");
        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/upgrade/FR_CTRL_PRIMCU_FV201212_MAIN_U4_T01_20250428(MT).bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/upgrade/FR_END_FV201009_MAIN_U1_T01_20250428.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/upgrade/FR_SERVO_FV504214_MAIN_U7_T07_20250519.bin");
        Console.WriteLine($"robot SetJointFirmwareUpgrade rtn is{rtn}");
    }

机器人MCU日志生成
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 机器人MCU日志生成
    * @return 错误码
    */
    public int RobotMCULogCollect();

设置端口通讯断开时停止机器人运行
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 设置端口通讯断开时停止机器人运行
    * @param [in] pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param [in] enable 0-关闭；1-开启
    * @param [in] confirmTime 通讯中断确认时长(ms)[0-5000]
    * @return  错误码
    */
    public int SetRobotStopOnComDisc(int portID, bool enable, int confirmTime)

获取端口通讯断开时停止机器人运行参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 获取端口通讯断开时停止机器人运行参数
    * @param [in] pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param [out] enable 0-关闭；1-开启
    * @param [out] confirmTime 通讯中断确认时长(ms)[0-5000]
    * @return  错误码
    */
    public int GetRobotStopOnComDisc(int portID, ref bool enable, ref int confirmTime)
    
端口通讯断开时停止机器人运行参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    void TestRobotStopOnComDisc()
    {
        int rtn = 0;

        // 设置四个端口的参数
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        Console.WriteLine($"SetRobotStopOnComDisc {rtn}");

        bool enable = false;
        int confirmTime = 0;

        // 获取并打印每个端口的设置
        robot.GetRobotStopOnComDisc(0, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(1, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8083 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(2, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(3, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

    }

UDP发送指令帧
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief UDP发送指令帧
    * @param [in] 指令帧
    * @return 错误码
    */
    public int SendUDPFrame(string frame)
        
基于UDP通信的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestRobotUDP()
    {
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[UDP响应] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };


        //发送帧
        string frameToSend = "/f/bIII52III236III7IIIMode(1)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII52III236III7IIIMode(0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII41III201III153IIIMoveJ(53.857,-89.441,119.453,-22.664,61.059,3.369,-54.249,-491.930,375.396,96.474,-6.896,-7.783,0,0,100,100,100,0.000,0.000,0.000,0.000,-1,0,0,0,0,0,0,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII42III203III163IIIMoveL(81.736,-85.284,114.974,-23.261,88.746,6.799,125.744,-506.570,375.396,96.474,-6.896,-7.783,0,0,100,100,100,-1,0,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,0,100,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII47III400III15IIIGetMCVersion(1)III/b/f/f/bIII48III424III21IIIGetSlaveFirmVersion()III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);

    }
        
设置用户自定义机器人末端灯色
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置用户自定义机器人末端灯色
    * @param [in] r 末端红灯控制；0-灭；1-亮
    * @param [in] g 末端绿灯控制；0-灭；1-亮
    * @param [in] b 末端蓝灯控制；0-灭；1-亮
    * @return 错误码
    */
    public int SetUserLEDColor(bool r, bool g, bool b)
            
设置用户自定义机器人末端灯色的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void testled()
    {
        robot.SetUserLEDColor(true, true, true);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(true, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, true, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, true);
    }