机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAnticollision (mode,level,config)``"
    "描述", "设置碰撞等级"
    "必选参数", "- ``mode``:0-等级，1-百分比；
    - ``level=[j1,j2,j3,j4,j5,j6]``:碰撞阈值；
    - ``config``:0-不更新配置文件，1-更新配置文件"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置碰撞后策略
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionStrategy(strategy,safeTime,safeDistance,safeVel,safetyMargin)``"
    "描述", "设置碰撞后策略"
    "必选参数", "- ``strategy``：0-报错暂停，1-继续运行，2-报错停止，3-重力矩模式，4-震荡相应模式，5-碰撞回弹模式"
    "默认参数", "- ``safeTime``：安全停止时间[1000-2000]ms，默认为：1000
    - ``safeDistance``：安全停止距离[1-150]mm，默认为：100
    - ``safeVel``：安全停止速度[50-250]mm/s，默认为：250
    - ``safetyMargin[6]``：安全系数[1-10]，默认为：[10,10,10,10,10,10]"
    "返回值", "错误码 成功-0  失败- errcode"

自定义碰撞检测阈值功能开始，设置关节端和TCP端的碰撞检测阈值
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomCollisionDetectionStart(flag, jointDetectionThreshould, tcpDetectionThreshould, block)``"
    "描述", "自定义碰撞检测阈值功能开始，设置关节端和TCP端的碰撞检测阈值"
    "必选参数", "- ``flag``： 1-仅关节检测开启；2-仅TCP检测开启；3-关节和TCP检测同时开启
    - ``jointDetectionThreshould``： 关节碰撞检测阈值 j1-j6
    - ``tcpDetectionThreshould``： TCP碰撞检测阈值，xyzabc
    - ``block``： 0-非阻塞；1-阻塞"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

自定义碰撞检测阈值功能关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomCollisionDetectionEnd()``"
    "描述", "自定义碰撞检测阈值功能关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

机器人碰撞等级设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    mode = 0
    config = 1
    level1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    level2 = [50.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    rtn = robot.SetAnticollision(mode, level1, config)
    print(f"SetAnticollision mode 0 rtn is {rtn}")
    mode = 1
    rtn = robot.SetAnticollision(mode, level2, config)
    print(f"SetAnticollision mode 1 rtn is {rtn}")
    p1Joint = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    p2Joint = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100, blendR=2)
    robot.ResetAllError()
    safety = [5, 5, 5, 5, 5, 5]
    rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety)
    print(f"SetCollisionStrategy rtn is {rtn}")
    jointDetectionThreshould = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    tcpDetectionThreshould = [60, 60, 60, 60, 60, 60]
    rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0)
    print(f"CustomCollisionDetectionStart rtn is {rtn}")
    robot.MoveL(desc_pos=p1Desc, tool=0, user=0, vel=100)
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100)
    rtn = robot.CustomCollisionDetectionEnd()
    print(f"CustomCollisionDetectionEnd rtn is {rtn}")
    robot.CloseRPC()

设置正限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitPositive(p_limit)``"
    "描述", "设置正限位"
    "必选参数", "- ``p_limit=[j1,j2,j3,j4,j5,j6]``：六个关节位置"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置负限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitNegative(n_limit)``"
    "描述", "设置负限位"
    "必选参数", "- ``n_limit=[j1,j2,j3,j4,j5,j6]``：六个关节位置"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取关节软限位角度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointSoftLimitDeg(flag=1)``"
    "描述", "获取关节软限位角度"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[j1min,j1max,j2min,j2max,j3min,j3max, j4min,j4max,j5min, j5max, j6min,j6max]``：轴1~轴6，关节负限位与正限位，单位[mm]"

机器人限位设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    plimit = [170.0, 80.0, 150.0, 80.0, 170.0, 160.0]
    robot.SetLimitPositive(plimit)
    nlimit = [-170.0, -260.0, -150.0, -260.0, -170.0, -160.0]
    robot.SetLimitNegative(nlimit)
    error,neg_deg = robot.GetJointSoftLimitDeg(0)
    print(f"pos limit deg: {neg_deg[1]}, {neg_deg[3]}, {neg_deg[5]}, {neg_deg[7]}, {neg_deg[9]}, {neg_deg[11]}")
    print(f"neg limit deg: {neg_deg[0]}, {neg_deg[2]}, {neg_deg[4]}, {neg_deg[6]}, {neg_deg[8]}, {neg_deg[10]}")
    robot.CloseRPC()

设置机器人碰撞检测方法
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionDetectionMethod(method, thresholdMode)``"
    "描述", "设置机器人碰撞检测方法"
    "必选参数", "
    - ``method``：碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
    - ``thresholdMode``：碰撞等级阈值方式；0-碰撞等级固定阈值方式；1-自定义碰撞检测阈值  
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

设置静态下碰撞检测开始关闭
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStaticCollisionOnOff(status)``"
    "描述", "设置静态下碰撞检测开始关闭"
    "必选参数", "
    - ``status``： 0-关闭；1-开启
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

设置机器人碰撞检测方法代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetCollisionDetectionMethod(0,0)
    rtn = robot.SetStaticCollisionOnOff(1)
    print(f"SetStaticCollisionOnOff On rtn is {rtn}")
    time.sleep(5)
    rtn = robot.SetStaticCollisionOnOff(0)
    print(f"SetStaticCollisionOnOff Off rtn is {rtn}")
    robot.CloseRPC()

关节扭矩功率检测
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPowerLimit(status, power)``"
    "描述", "关节扭矩功率检测"
    "必选参数", "
    - ``status``：0-关闭；1-开启
    - ``power``：设定最大功率(W)
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"
    
关节扭矩功率检测代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    robot.SetPowerLimit(1, 200)
    error,torques = robot.GetJointTorques(1)
    count = 100
    robot.ServoJTStart()
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)  # 1ms delay
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

设置安全速度参数
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetVelReducePara(enable, maxTCPVel, strategy)``"
    "描述", "设置安全速度参数"
    "必选参数", "
    - ``enable``：0-关；1-手动模式启用；2-所有模式启用(不支持自动限速)
    - ``maxTCPVel``：限制最大TCP速度;[0-1000]mm/s
    - ``strategy``：超速后策略；0-停止报警；1-自动限速；2-停止报警并去使能
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

设置安全速度参数的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def TestSetVelReducePara(self):
        # 初始化关节位置、外部轴和偏移
        j1 = [0, -90, 90, 0, 0, 0]
        j2 = [90, -90, 90, 0, 0, 0]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        # 设置基础速度
        robot.SetSpeed(80)

        # 测试参数错误的情况（mode=2 无效？）
        rtn = robot.SetVelReducePara(2, 30, 1)
        print(f"SetVelReducePara param error rtn is {rtn}")

        # 关闭减速功能（mode=0, action=1 表示禁用减速）
        rtn = robot.SetVelReducePara(0, 30, 1)
        print(f"SetVelReducePara disable reduce vel rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 启用减速功能（mode=1, action=1）
        rtn = robot.SetVelReducePara(1, 30, 1)
        print(f"SetVelReducePara reduce vel rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 测试 action=2（可能表示急停或禁用机器人）
        rtn = robot.SetVelReducePara(2, 30, 2)
        print(f"SetVelReducePara disable robot rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 等待、复位错误并重新使能机器人
        time.sleep(2)
        robot.ResetAllError()
        robot.RobotEnable(1)
        time.sleep(1)

        # 测试 action=0（可能表示仅上报错误，不执行动作）
        rtn = robot.SetVelReducePara(2, 30, 0)
        print(f"SetVelReducePara report error rtn is {rtn}")
        robot.MoveJ(joint_pos=j1, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=0, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 关闭连接
        robot.CloseRPC()

    TestSetVelReducePara(robot)