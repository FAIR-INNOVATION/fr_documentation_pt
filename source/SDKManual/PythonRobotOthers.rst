其他接口
=================

.. toctree:: 
    :maxdepth: 5

获取SSH公钥
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSSHKeygen()``"
    "描述", "获取SSH公钥"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``keygen``：公钥"

下发SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSSHScpCmd(mode, sshname, sship, usr_file_url, robot_file_url)``"
    "描述", "下发SCP指令"
    "必选参数", "- ``mode``：0-上传（上位机->控制器），1-下载（控制器->上位机）
    - ``sshname``：上位机用户名
    - ``sship``：上位机ip地址
    - ``usr_file_url``：上位机文件路径
    - ``robot_file_url``：机器人控制器文件路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算指定路径下文件的MD5值
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFileMD5(file_path)``"
    "描述", "计算指定路径下文件的MD5值"
    "必选参数", "- ``file_path``：文件路径包含文件名，默认Traj文件夹路径为:/fruser/traj/,如/fruser/traj/trajHelix_aima_1.txt"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``md5``：文件MD5值"

机器人SSH、MD5指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    file_path = "/fruser/airlab.lua"
    md5 = ""
    emerg_state = 0
    si0_state = 0
    si1_state = 0
    sdk_com_state = 0
    ssh_keygen = ""
    retval,ssh_keygen = robot.GetSSHKeygen()
    print(f"GetSSHKeygen retval is: {retval}")
    print(f"ssh key is: {ssh_keygen}")
    ssh_name = "fr"
    ssh_ip = "192.168.58.45"
    ssh_route = "/home/fr"
    ssh_robot_url = "/root/robot/dhpara.config"
    retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url)
    print(f"SetSSHScpCmd retval is: {retval}")
    print(f"robot url is: {ssh_robot_url}")
    error, md5 = robot.ComputeFileMD5(file_path)
    print(f"md5 is: {md5}")
    robot.CloseRPC()

设置机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateSamplePeriod(period)``"
    "描述", "设置机器人 20004 端口反馈周期"
    "必选参数", "- ``period``：机器人 20004 端口反馈周期(ms)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealtimeStateSamplePeriod()``"
    "描述", "获取机器人 20004 端口反馈周期"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``period``：机器人 20004 端口反馈周期(ms)"

机器人20004端口状态反馈周期配置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.SetRobotRealtimeStateSamplePeriod(10)
    error,getPeriod = robot.GetRobotRealtimeStateSamplePeriod()
    print(f"period is {getPeriod}")
    time.sleep(1)
    robot.CloseRPC()

机器人软件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SoftwareUpgrade(filePath, block)``"
    "描述", "机器人软件升级"
    "必选参数", "- ``filePath``：软件升级包全路径
    - ``block``：是否阻塞至升级完成 true:阻塞；false:非阻塞"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode "

获取机器人软件升级状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareUpgradeState()``"
    "描述", "获取机器人软件升级状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``state``：机器人软件包升级状态，0：空闲中或上传升级包中，1~100：升级完成百分比，-1：升级软件失败，-2：校验失败，-3：版本校验失败，-4：解压失败，-5：用户配置升级失败，-6：外设配置升级失败，-7：扩展轴配置升级失败，-8：机器人配置升级失败，-9：DH参数配置升级失败"

机器人软件升级代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", False)
    print(f"SoftwareUpgrade error is {error}")
    while True:
        curState = robot.GetSoftwareUpgradeState()
        print(f"upgrade state is {curState}")
        time.sleep(3)
    robot.CloseRPC()

下载点位表数据库
+++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableDownLoad(point_table_name, save_file_path)``"
    "描述", "下载点位表数据库"
    "必选参数", "- ``point_table_name``：要下载的点位表名称    pointTable1.db;
    - ``save_file_path``:下载点位表的存储路径   C://test/;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

上传点位表数据库
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpLoad(point_table_file_path)``"
    "描述", "上传点位表数据库"
    "必选参数", "- ``point_table_file_path``：上传点位表的全路径名   C://test/pointTable1.db"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

点位表更新lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "描述", "点位表更新lua文件"
    "必选参数", "- ``point_table_name``：要切换的点位表名称pointTable1.db,当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    - ``lua_file_name``: 要更新的lua文件名称 testPointTable.lua"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人点位表操作代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    save_path = "D://zDOWN/"
    point_table_name = "point_table_FR5.db"
    rtn = robot.PointTableDownLoad(point_table_name, save_path)
    print(f"download : {point_table_name} fail: {rtn}")
    upload_path = "D://zDOWN/point_table_FR5.db"
    rtn = robot.PointTableUpLoad(upload_path)
    print(f"retval is: {rtn}")
    point_tablename = "point_table_FR5.db"
    lua_name = "test0610.lua"
    rtn,error = robot.PointTableUpdateLua(point_tablename, lua_name)
    print(f"retval is: {rtn}")
    robot.CloseRPC()

控制器日志下载
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RbLogDownload(savePath)``"
    "描述", "控制器日志下载"
    "必选参数", "- ``savePath``：保存文件路径D://zDown/"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

所有数据源下载
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AllDataSourceDownload(savePath)``"
    "描述", "所有数据源下载"
    "必选参数", "- ``savePath``：保存文件路径D://zDown/"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

数据备份包下载
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DataPackageDownload(savePath)``"
    "描述", "数据备份包下载"
    "必选参数", "- ``savePath``：保存文件路径D://zDown/"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

下载控制器数据代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.RbLogDownload("D://zDOWN/")
    print(f"RbLogDownload rtn is {rtn}")
    rtn = robot.AllDataSourceDownload("D://zDOWN/")
    print(f"AllDataSourceDownload rtn is {rtn}")
    rtn = robot.DataPackageDownload("D://zDOWN/")
    print(f"DataPackageDownload rtn is {rtn}")
    robot.CloseRPC()

设置编码器升级
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetEncoderUpgrade(path)``"
    "描述", "设置编码器升级"
    "必选参数", "- ``path``：本地升级包全路径(D://zUP/XXXXX.bin)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置关节固件升级
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetJointFirmwareUpgrade(type, path)``"
    "描述", "设置关节固件升级"
    "必选参数", "- ``type``：升级文件类型；1-升级固件；2-升级从站配置文件
    - ``path``：本地升级包全路径(D://zUP/XXXXX.bin)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置控制箱固件升级
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCtrlFirmwareUpgrade(type, path)``"
    "描述", "设置控制箱固件升级"
    "必选参数", "- ``type``：升级文件类型；1-升级固件；2-升级从站配置文件
    - ``path``：本地升级包全路径(D://zUP/XXXXX.bin)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置末端固件升级
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetEndFirmwareUpgrade(type, path)``"
    "描述", "设置末端固件升级"
    "必选参数", "- ``type``：升级文件类型；1-升级固件；2-升级从站配置文件
    - ``path``：本地升级包全路径(D://zUP/XXXXX.bin)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
       
关节全参数配置文件升级
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointAllParamUpgrade(path)``"
    "描述", "关节全参数配置文件升级"
    "必选参数", "- ``path``：本地升级包全路径(D://zUP/XXXXX.bin)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人从站固件升级代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.RobotEnable(0)
    time.sleep(0.2)
    rtn = robot.JointAllParamUpgrade("D://zUP/MT/joint0603/jointallparameters.db")
    print(f"robot JointAllParamUpgrade rtn is {rtn}")
    rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Cbd_Asix_V2.0.bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Axle_Asix_V2.4.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    robot.SetSysServoBootMode()
    time.sleep(0.2)
    rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/MT/FR_CTRL_PRIMCU_FV201412_MAIN_U4_T01_20250630(MT).bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/MT/FR_END_FV2010010_MAIN_U1_T01_20250603.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/MT/FR_SERVO_FV504215_MAIN_U7_T07_20250603.bin")
    print(f"robot SetJointFirmwareUpgrade rtn is {rtn}")
    robot.CloseRPC()
       
机器人操作系统升级(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``KernelUpgrade(filePath)``"
    "描述", "机器人操作系统升级(LA控制箱)"
    "必选参数", "- ``filePath``：操作系统升级包全路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
       
获取机器人操作系统升级结果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetKernelUpgradeResult()``"
    "描述", "获取机器人操作系统升级结果(LA控制箱)"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
       
机器人MCU日志生成
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotMCULogCollect()``"
    "描述", "机器人MCU日志生成"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
           
设置端口通讯断开时停止机器人运行
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotStopOnComDisc(portID, enable, confirmTime)``"
    "描述", "设置端口通讯断开时停止机器人运行"
    "必选参数", "
    - ``portID``：端口编号 0-8080；1-8083；2-20002；3-20004
    - ``enable``：0-关闭；1-开启
    - ``confirmTime``：通讯中断确认时长(ms)[0-5000]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
           
获取端口通讯断开时停止机器人运行参数
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotStopOnComDisc(portID)``"
    "描述", "获取端口通讯断开时停止机器人运行参数"
    "必选参数", "
    - ``portID``：端口编号 0-8080；1-8083；2-20002；3-20004
    - ``enable``：0-关闭；1-开启
    - ``confirmTime``：通讯中断确认时长(ms)[0-5000]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

端口通讯断开时停止机器人运行参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot
    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def test_robot_stop_on_com_disc(self):
        # 初始化参数
        enable = False
        confirm_time = 0

        # 设置通信断开时机器人停止功能
        rtn = robot.SetRobotStopOnComDisc(0, True, 330)
        print(f"SetRobotStopOnComDisc index0: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(1, True, 550)
        print(f"SetRobotStopOnComDisc index1: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(2, True, 110)
        print(f"SetRobotStopOnComDisc index2: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(3, True, 220)
        print(f"SetRobotStopOnComDisc index3: {rtn}")

        # 获取通信断开时机器人停止设置
        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(0)
        print(f"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(1)
        print(f"GetRobotStopOnComDisc 80803 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(2)
        print(f"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(3)
        print(f"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        # 关闭RPC连接
        robot.CloseRPC()
        return 0

    test_robot_stop_on_com_disc(robot)

UDP发送指令帧
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SendUDPFrame(frame)``"
    "描述", "UDP发送指令帧"
    "必选参数", "
    - ``frame``：发送UDP数据，透传，不封装"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

基于UDP通信的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def TestSendUDPFrame(self):
        # 设置回调
        def callback(src_type, count, cmd_id, data_len, content):
            print("收到回复: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0
        robot.SetUDPCmdRpyCallback(callback)

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame Mode(0) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII21III303III7IIIMode(1)III/b/f")
        print(f"SendUDPFrame Mode(1) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII49III201III184IIIMoveJ(-15.625, -82.680, 101.654, -110.950, -88.290, 0.017, -383.012, -2.325, 242.655, -178.024, 1.710, 74.416, 0, 0, 100, 100, 100, 0.000, 0.000, 0.000, 0.000, -1, 0, 0, 0, 0, 0, 0, 0)III/b/f")
        print(f"SendUDPFrame MoveJ(-15.625) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII48III203III199IIIMoveL(-75.622, -82.680, 101.654, -110.950, -88.290, 0.017, -193.537, 330.525, 242.657, -178.024, 1.710, 14.420, 0, 0, 100, 100, 100, -1, 0, 0.000, 0.000, 0.000, 0.000, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0)III/b/f")
        print(f"SendUDPFrame MoveL(-75.622) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII4III905III20IIIGetSoftwareVersion()III/b/f")
        print(f"SendUDPFrame GetSoftwareVersion() rtn is {rtn}")

        time.sleep(1)

        # 发送UDP帧数据校验测试
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("III20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III6IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/b|||20|||303|||7|||Mode(0)|||/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bII20II303II7IIMode(0)II/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        robot.CloseRPC()
        time.sleep(1)

    TestSendUDPFrame(robot)
    
设置用户自定义机器人末端灯色
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetUserLEDColor(r, g, b)``"
    "描述", "设置用户自定义机器人末端灯色"
    "必选参数", "
    - ``r``：末端红灯控制；0-灭；1-亮
    - ``g``：末端绿灯控制；0-灭；1-亮
    - ``b``：末端蓝灯控制；0-灭；1-亮
    - "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置用户自定义机器人末端灯色的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')


    def testled(self):
        # 设置用户LED灯颜色
        # 参数顺序: R, G, B (红, 绿, 蓝)

        # 白色 (红绿蓝全亮)
        robot.SetUserLEDColor(True, True, True)
        time.sleep(1)

        # 关闭所有灯
        robot.SetUserLEDColor(False, False, False)
        time.sleep(1)

        # 红色 (仅红灯亮)
        robot.SetUserLEDColor(True, False, False)
        time.sleep(1)

        # 绿色 (仅绿灯亮)
        robot.SetUserLEDColor(False, True, False)
        time.sleep(1)

        # 蓝色 (仅蓝灯亮)
        robot.SetUserLEDColor(False, False, True)

        # 关闭连接
        robot.CloseRPC()

    testled(robot)