其他接口
================

.. toctree:: 
    :maxdepth: 5

获取SSH公钥
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取SSH公钥
    * @param [out] keygen 公钥
    * @return 错误码
    */
    int GetSSHKeygen(String[] keygen)

下发SCP指令
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
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
    int SetSSHScpCmd(int mode, String sshname, String sship, String usr_file_url, String robot_file_url)

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 计算指定路径下文件的MD5值
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码
    */
    int ComputeFileMD5(String file_path, String[] md5)

机器人SSH、MD5指令代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSSHMd5(Robot robot)
    {
        String file_path= "/fruser/airlab.lua";
        String[] md5 =new String[]{""};

        String[] ssh_keygen=new String[]{""};
        int retval = robot.GetSSHKeygen(ssh_keygen);
        System.out.println(ssh_keygen[0]);

        String ssh_name = "fr";
        String ssh_ip = "192.168.58.45";
        String ssh_route = "/home/fr";
        String ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        System.out.println("SetSSHScpCmd retval is:"+ retval);
        System.out.println("robot url is:"+ ssh_robot_url);

        robot.ComputeFileMD5(file_path, md5);
        System.out.println("md5 is:+"+ md5[0]);
        return 0;
    }

设置机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置机器人 20004 端口反馈周期
    * @param [in] period 机器人 20004 端口反馈周期(ms)
    * @return  错误码
    */
    public int SetRobotRealtimeStateSamplePeriod(int period)

获取机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人 20004 端口反馈周期
    * @return  List[0]:错误码; List[1]:机器人 20004 端口反馈周期(ms)
    */
    public List<Integer> GetRobotRealtimeStateSamplePeriod()

机器人20004端口状态反馈周期配置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRealtimePeriod(Robot robot)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        List<Integer> getPeriod = new ArrayList<>();
        getPeriod=robot.GetRobotRealtimeStateSamplePeriod();
        robot.Sleep(1000);

        return 0;
    }

机器人软件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人软件升级
     * @param [in] filePath 软件升级包全路径
     * @param [in] block 是否阻塞至升级完成 true:阻塞；false:非阻塞
     * @return  错误码
     */
    public int SoftwareUpgrade(String filePath, boolean block)

获取机器人软件升级状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人软件升级状态
    * @return  List[0]:错误码; List[1]:机器人软件升级状态 0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败
    */
    public List<Integer> GetSoftwareUpgradeState()

机器人软件升级代码示例
+++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUpgrade(Robot robot)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            List<Integer> inter=new ArrayList<>();
            inter=robot.GetSoftwareUpgradeState();
            System.out.println("upgrade state is:"+ inter.get(1));
            robot.Sleep(300);
        }
    }

下载点位表数据库
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下载点位表数据库 
    * @param [in] pointTableName 要下载的点位表名称    pointTable1.db
    * @param [in] saveFilePath 下载点位表的存储路径   C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(String pointTableName, String saveFilePath);

上传点位表数据库
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上传点位表数据库 
    * @param [in] pointTableFilePath 上传点位表的全路径名   C://test/pointTable1.db
    * @return 错误码 
    */
    int PointTableUpLoad(String pointTableFilePath);

点位表更新lua文件
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 点位表更新lua文件
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db",当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "testPointTable.lua"
    * @param [out] errorStr 切换点位表错误信息
    * @return 错误码 
    */
    int PointTableUpdateLua(String pointTableName, String luaFileName, String errorStr);

机器人点位表操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPointTable(Robot robot)
    {
        String save_path = "D://zDOWN/";
        String point_table_name = "point_table_FR5.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);

        String upload_path = "D://zUP/point_table_FR5.db";
        rtn = robot.PointTableUpLoad(upload_path);

        String point_tablename = "point_table_FR5.db";
        String lua_name = "airlab.lua";
        String err="";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name,err);

        robot.CloseRPC();
        return 0;
    }

控制器日志下载
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 控制器日志下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    int RbLogDownload(String savePath);

所有数据源下载
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 所有数据源下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    int AllDataSourceDownload(String savePath);

数据备份包下载
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 数据备份包下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return 错误码
    */
    int DataPackageDownload(String savePath);

下载控制器数据代码示例
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestDownLoadRobotData(Robot robot)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");

        rtn = robot.AllDataSourceDownload("D://zDOWN/");

        rtn = robot.DataPackageDownload("D://zDOWN/");
        return 0;
    }

设置编码器升级
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置编码器升级
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    int SetEncoderUpgrade(String path)

设置关节固件升级
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置关节固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    public int SetJointFirmwareUpgrade(int type, String path)

设置控制箱固件升级
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置控制箱固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    public int SetCtrlFirmwareUpgrade(int type, String path)

设置末端固件升级
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置末端固件升级
    * @param [in] type 升级文件类型；1-升级固件；2-升级从站配置文件
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    public int SetEndFirmwareUpgrade(int type, String path)

关节全参数配置文件升级
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 关节全参数配置文件升级
    * @param [in] path 本地升级包全路径(D://zUP/XXXXX.bin)
    * @return 错误码
    */
    public int JointAllParamUpgrade(String path)

机器人从站固件升级代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFirmWareUpgrade(Robot robot)
    {
        robot.RobotEnable(0);
        robot.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/standardQX/jointallparametersFR56.0.db");
        System.out.println("robot JointAllParamUpgrade rtn is:"+ rtn);

        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade config param rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        System.out.println("robot SetEndFirmwareUpgrade config param rtn is:"+ rtn);

        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/standardQX/FR_CTRL_PRIMCU_FV201010_MAIN_U4_T01_20240529.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/standardQX/FR_END_FV201010_MAIN_U01_T01_20250522.bin");
        System.out.println("robot SetEndFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/standardQX/FR_SERVO_FV502211_MAIN_U7_T07_20250217.bin");
        System.out.println("robot SetJointFirmwareUpgrade rtn is:"+ rtn);

        robot.CloseRPC();
    }

机器人操作系统升级(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人操作系统升级(LA控制箱)
     * @param [in] filePath 操作系统升级包全路径
     * @return  错误码
     */
    public int KernelUpgrade(String filePath)

获取机器人操作系统升级结果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取机器人操作系统升级结果(LA控制箱)
     * @param [out] result 升级结果：0:成功；-1:失败
     * @return  错误码
     */
    public int GetKernelUpgradeResult(int[] result)

机器人MCU日志生成
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 机器人MCU日志生成
    * @return 错误码
    */
    public int RobotMCULogCollect()

设置端口通讯断开时停止机器人运行
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置端口通讯断开时停止机器人运行
    * @param pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param enable 0-关闭；1-开启
    * @param confirmTime 通讯中断确认时长(ms)[0-5000]
    * @return 错误码
    */
    public int SetRobotStopOnComDisc(int portID, bool enable, int confirmTime)
    
获取端口通讯断开时停止机器人运行参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取端口通讯断开时停止机器人运行参数
    * @param pordID 端口编号 0-8080；1-8083；2-20002；3-20004
    * @param enable 结果数组，index 0: 0-关闭；1-开启
    * @param confirmTime 结果数组，index 0: 通讯中断确认时长(ms)[0-5000] 
    * @return 错误码
    */
    public int GetRobotStopOnComDisc(int pordID, int[] enable, int[] confirmTime)

端口通讯断开时停止机器人运行参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    void TestRobotStopOnComDisc(Robot robot)
    {
        int[] enable = {0};
        int[] confirmTime = {0};
        int rtn = 0;
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        System.out.printf("SetRobotStopOnComDisc %d\n", rtn);

        robot.GetRobotStopOnComDisc(0, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 8080 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(1, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 8083 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(2, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 20002 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);
        robot.GetRobotStopOnComDisc(3, enable, confirmTime);
        System.out.printf("GetRobotStopOnComDisc 20004 rtn %d; enable is %d; confirm time is %d\n", rtn, enable[0], confirmTime[0]);

        return;
    }

UDP发送指令帧
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP发送指令帧
    * @param 指令帧
    * @return 错误码
    */
    public int SendUDPFrame(String frame)
    
关于UDP通信的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestRobotUDP (Robot robot) {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[收到机器人 UDP 回复]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("内容 (content): " + content);
            return 0;
        });
        // 发送帧
        String frameToSend = "/f/bIII52III236III7IIIMode(1)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII52III236III7IIIMode(0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII41III201III153IIIMoveJ(53.857,-89.441,119.453,-22.664,61.059,3.369,-54.249,-491.930,375.396,96.474,-6.896,-7.783,0,0,100,100,100,0.000,0.000,0.000,0.000,-1,0,0,0,0,0,0,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII42III203III163IIIMoveL(81.736,-85.284,114.974,-23.261,88.746,6.799,125.744,-506.570,375.396,96.474,-6.896,-7.783,0,0,100,100,100,-1,0,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,0,100,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
        frameToSend = "/f/bIII47III400III15IIIGetMCVersion(1)III/b/f/f/bIII48III424III21IIIGetSlaveFirmVersion()III/b/f";
        robot.SendUDPFrame(frameToSend);
        robot.Sleep(2000);
    }
        
设置用户自定义机器人末端灯色
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置用户自定义机器人末端灯色
    * @param r 末端红灯控制；0-灭；1-亮
    * @param g 末端绿灯控制；0-灭；1-亮
    * @param b 末端蓝灯控制；0-灭；1-亮
    * @return 错误码
    */
    public int SetUserLEDColor(bool r, bool g, bool b)
            
设置用户自定义机器人末端灯色的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public void testled(robot)
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