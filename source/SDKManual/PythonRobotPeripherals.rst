机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "描述", "配置夹爪"
    "必选参数", "- ``company``：夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行；
    - ``device``：设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)"
    "默认参数", "- ``softversion``：软件版本号，暂不使用，默认为0；
    - ``bus``：设备挂载末端总线位置，暂不使用，默认为0；"
    "返回值", "错误码 成功-0  失败- errcode "

获取夹爪配置
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperConfig()``"
    "描述", "获取夹爪配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[number,company,device,softversion]``： number，夹爪编号;company，夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行 ;device，设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20);softvesion，软件版本号，暂不使用，默认为0。"

激活夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ActGripper(index,action)``"
    "描述", "激活夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``action``:0-复位，1-激活"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

控制夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "描述", "控制夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``pos``:位置百分比，范围[0~100]；
    - ``vel``:速度百分比，范围[0~100];
    - ``force``:力矩百分比，范围[0~100]；
    - ``maxtime``:最大等待时间，范围[0~30000]，单位[ms]；
    - ``block``:0-阻塞，1-非阻塞；
    - ``type``:夹爪类型，0-平行夹爪；1-旋转夹爪；
    - ``rotNum``:rotNum 旋转圈数；
    - ``rotVel``:旋转速度百分比[0-100]；
    - ``rotTorque``:旋转力矩百分比[0-100]。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取夹爪运动状态
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperMotionDone()``"
    "描述", "获取夹爪运动状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[fault,status]``：夹爪运动状态，fault:0-无错误，1-有错误；status:0-运动未完成，1-运动完成"

获取夹爪激活状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperActivateStatus()``"
    "描述", "获取夹爪激活状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``gripper_active``：bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活"

获取夹爪位置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurPosition()``"
    "描述", "获取夹爪位置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``position``：位置百分比，范围0~100%"

获取夹爪速度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurSpeed()``"
    "描述", "获取夹爪速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``speed``：速度百分比，范围0~100%"

获取夹爪电流
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurCurrent()``"
    "描述", "获取夹爪电流"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``current``：电流百分比，范围0~100%"

获取夹爪电压
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperVoltage()``"
    "描述", "获取夹爪电压"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``voltage``：电压,单位0.1V"

获取夹爪温度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperTemp()``"
    "描述", "获取夹爪温度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``temp``：温度，单位℃"

计算预抓取点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "描述", "计算预抓取点-视觉"
    "必选参数", "- ``desc_pos``：夹抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``pre_pos``：预抓取点笛卡尔位姿"

计算撤退点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "描述", "计算撤退点-视觉"
    "必选参数", "- ``desc_pos``：抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``post_pos``：撤退点笛卡尔位姿"

机器人夹爪操作代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 4
    device = 0
    softversion = 0
    bus = 2
    index = 2
    act = 0
    max_time = 30000
    block = 0
    status = 0
    fault = 0
    active_status = 0
    current_pos = 0
    current = 0
    voltage = 0
    temp = 0
    speed = 0
    robot.SetGripperConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.GetGripperConfig()
    print(f"gripper config:{company},{device},{softversion},{bus}")
    robot.ActGripper(index, act)
    time.sleep(1)
    act = 1
    robot.ActGripper(index, act)
    time.sleep(1)
    error = robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    time.sleep(1)
    error = robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    error, [fault, status] = robot.GetGripperMotionDone()
    print(f"motion status:{fault},{status}")
    error, [fault, active_status] = robot.GetGripperActivateStatus()
    print(f"gripper active fault is:{fault},status is:{active_status}")
    error, [fault, current_pos] = robot.GetGripperCurPosition()
    print(f"fault is:{fault},current position is:{current_pos}")
    error, [fault, current] = robot.GetGripperCurCurrent()
    print(f"fault is:{fault},current current is:{current}")
    error, [fault, voltage] = robot.GetGripperVoltage()
    print(f"fault is:{fault},current voltage is:{voltage}")
    error, [fault, temp] = robot.GetGripperTemp()
    print(f"fault is:{fault},current temperature is:{temp}")
    error, [fault, speed] = robot.GetGripperCurSpeed()
    print(f"fault is:{fault},current speed is:{speed}")
    retval = 0
    prepick_pose = [0.0]*6
    postpick_pose = [0.0]*6
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval, prepick_pose = robot.ComputePrePick(p1Desc, 10, 0)
    print(f"ComputePrePick retval is:{retval}")
    print(f"xyz is:{prepick_pose[0]},{prepick_pose[1]},{prepick_pose[2]};rpy is:{prepick_pose[3]},{prepick_pose[4]},{prepick_pose[5]}")
    retval, postpick_pose = robot.ComputePostPick(p2Desc, -10, 0)
    print(f"ComputePostPick retval is:{retval}")
    print(f"xyz is:{postpick_pose[0]},{postpick_pose[1]},{postpick_pose[2]};rpy is:{postpick_pose[3]},{postpick_pose[4]},{postpick_pose[5]}")
    robot.CloseRPC()

获取旋转夹爪的旋转圈数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotNum()``"
    "描述", "获取旋转夹爪的旋转圈数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``num``：旋转圈数"

获取旋转夹爪的旋转速度百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotSpeed()``"
    "描述", "获取旋转夹爪的旋转速度百分比"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``speed``：旋转速度百分比"

获取旋转夹爪的旋转力矩百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotTorque()``"
    "描述", "获取旋转夹爪的旋转力矩百分比"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``torque``：旋转力矩百分比"

获取旋转夹爪状态代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    fault = 0
    rotNum = 0.0
    rotSpeed = 0
    rotTorque = 0
    error,fault, rotNum = robot.GetGripperRotNum()
    error,fault, rotSpeed = robot.GetGripperRotSpeed()
    error,fault, rotTorque = robot.GetGripperRotTorque()
    print(f"gripper rot num:{rotNum},gripper rotSpeed:{rotSpeed},gripper rotTorque:{rotTorque}")
    robot.CloseRPC()

传动带启动、停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorStartEnd(status)``"
    "描述", "传动带启动、停止"
    "必选参数", "- ``status``： 传动带状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录IO检测点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointIORecord()``"
    "描述", "记录IO检测点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录A点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointARecord()``"
    "描述", "记录A点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录参考点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorRefPointRecord()``"
    "描述", "记录参考点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录B点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointBRecord()``"
    "描述", "记录B点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传送带工件IO检测
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorIODetect(max_t)``"
    "描述", "传送带工件IO检测"
    "必选参数", "- ``max_t``： 最大检测时间，单位ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取物体当前位置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorGetTrackData(mode)``"
    "描述", "获取物体当前位置"
    "必选参数", "- ``mode``： 1-跟踪抓取 2-跟踪运动 3-TPD跟踪"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪开始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackStart(status)``"
    "描述", "传动带跟踪开始"
    "必选参数", "- ``status``： 状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackEnd()``"
    "描述", "传动带跟踪停止"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带参数配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param, followType, startDis, endDis)``"
    "描述", "传动带参数配置"
    "必选参数", "- ``param``： = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                    - ``encChannel``: 编码器通道 1-2
                    - ``resolution``: 编码器分辨率 编码器旋转一圈脉冲个数
                    - ``lead``: 机械传动比 编码器旋转一圈传送带移动距离
                    - ``wpAxis``: 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
                    - ``vision``: 是否配视觉  0-不配 1-配,
                    - ``speedRadio``: 速度比  针对传送带跟踪抓取速度范围为（1-100）  跟踪运动、TPD跟踪设置为1
    - ``followType``：跟踪运动类型，0-跟踪运动；1-追检运动"
    "默认参数", "- ``startDis``：追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    - ``endDis``：追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100"
    "返回值", "错误码 成功-0  失败- errcode"

传动带抓取点补偿
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorCatchPointComp(cmp)``"
    "描述", "传动带抓取点补偿"
    "必选参数", "- ``cmp``： 补偿位置 [x,y,z]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

直线运动
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackMoveL(name,tool,wobj,vel=20,acc=100,ovl=100,blendR=-1.0)``"
    "描述", "直线运动"
    "必选参数", "- ``name``：cvrCatchPoint 或cvrRaisePoint
    - ``tool``: 工具号
    - ``wobj``:  工件号"
    "默认参数", "- ``vel``: 速度 默认20
    - ``acc``: 加速度 默认100
    - ``ovl``: 速度缩放因子 默认100
    - ``blendR``: [-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0"
    "返回值", "错误码 成功-0  失败- errcode"

传送带通讯输入检测
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetect(timeout)``"
    "描述", "传送带通讯输入检测"
    "必选参数", "- ``timeout``：等待超时时间ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传送带通讯输入检测触发
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetectTrigger()``"
    "描述", "传送带通讯输入检测触发"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人传送带操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.ConveyorStartEnd(1)
    print(f"ConveyorStartEnd retval is:{retval}")
    retval = robot.ConveyorPointIORecord()
    print(f"ConveyorPointIORecord retval is:{retval}")
    retval = robot.ConveyorPointARecord()
    print(f"ConveyorPointARecord retval is:{retval}")
    retval = robot.ConveyorRefPointRecord()
    print(f"ConveyorRefPointRecord retval is:{retval}")
    retval = robot.ConveyorPointBRecord()
    print(f"ConveyorPointBRecord retval is:{retval}")
    retval = robot.ConveyorStartEnd(0)
    print(f"ConveyorStartEnd retval is:{retval}")
    param = [1.0, 10000.0, 200.0, 0.0, 0.0, 20.0]
    retval = robot.ConveyorSetParam(param,0)
    print(f"ConveyorSetParam retval is:{retval}")
    cmp = [0.0, 0.0, 0.0]
    retval = robot.ConveyorCatchPointComp(cmp)
    print(f"ConveyorCatchPointComp retval is:{retval}")
    index = 1
    max_time = 30000
    block = 0
    retval = 0
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval = robot.MoveCart(p1Desc, 1, 0, 100.0)
    print(f"MoveCart retval is:{retval}")
    retval = robot.WaitMs(1)
    print(f"WaitMs retval is:{retval}")
    retval = robot.ConveyorIODetect(10000)
    print(f"ConveyorIODetect retval is:{retval}")
    retval = robot.ConveyorGetTrackData(1)
    print(f"ConveyorGetTrackData retval is:{retval}")
    retval = robot.ConveyorTrackStart(1)
    print(f"ConveyorTrackStart retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.ConveyorTrackEnd()
    print(f"ConveyorTrackEnd retval is:{retval}")
    robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0)
    retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    robot.CloseRPC()

末端传感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfig(idCompany, idDevice, idSoftware, idBus)``"
    "描述", "末端传感器配置"
    "必选参数", "
    - ``idCompany``: 厂商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 类型，0-JUNKONG/RYR6T.V1.0
    - ``idSoftware``: 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    - ``idBus``: 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取末端传感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfigGet()``"
    "描述", "获取末端传感器配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``idCompany``: 厂商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 类型，0-JUNKONG/RYR6T.V1.0"
        
末端传感器激活
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorActivate(actFlag)``"
    "描述", "末端传感器激活"
    "必选参数", "``actFlag``： 0-复位；1-激活"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``coord``: 坐标系值[x,y,z,rx,ry,rz]"

末端传感器寄存器写入
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端传感器寄存器写入"
    "必选参数", "- ``devAddr``：设备地址编号 0-255
    - ``regHAddr``：寄存器地址高8位
    - ``regLAddr``：寄存器地址低8位
    - ``regNum``：寄存器个数 0-255
    - ``data1``：写入寄存器数值1
    - ``data2``：写入寄存器数值2
    - ``isNoBlock``：是否阻塞 0-阻塞；1-非阻塞"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

末端传感器代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleSensorConfig(18, 0, 0, 1)
    error, company, type = robot.AxleSensorConfigGet()
    print(f"company is:{company},type is:{type}")
    rtn = robot.AxleSensorActivate(1)
    print(f"AxleSensorActivate rtn is:{rtn}")
    time.sleep(1)
    rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0)
    print(f"AxleSensorRegWrite rtn is:{rtn}")
    robot.CloseRPC()

获取机器人外设协议
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExDevProtocol()``"
    "描述", "获取机器人外设协议"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode; 
    - ``protocol``: 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster"

设置机器人外设协议
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExDevProtocol(protocol)``"
    "描述", "设置机器人外设协议"
    "必选参数", "- ``protocol``：机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置机器人外设协议代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    protocol = 4096
    rtn = robot.SetExDevProtocol(protocol)
    print(f"SetExDevProtocol rtn:{rtn}")
    rtn, protocol = robot.GetExDevProtocol()
    print(f"GetExDevProtocol rtn:{rtn},protocol is:{protocol}")
    robot.CloseRPC()


获取末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleCommunicationParam()``"
    "描述", "获取末端通讯参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：数据位:数据位支持（8,9），目前常用为 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用为 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用为 0
    - ``timeout``：超时时间:1~1000ms，此值需要结合外设搭配设置合理的时间参数
    - ``timeoutTimes``：超时次数:1~10，主要进行超时重发，减少偶发异常提高用户体验
    - ``period``：周期性指令时间间隔:1~1000ms，主要用于周期性指令每次下发的时间间隔"

设置末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleCommunicationParam(baudRate, dataBit, stopBit, verify, timeout, timeoutTimes, period)``"
    "描述", "设置末端通讯参数"
    "必选参数", "- ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：数据位:数据位支持（8,9），目前常用为 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用为 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用为 0
    - ``timeout``：超时时间:1~1000ms，此值需要结合外设搭配设置合理的时间参数
    - ``timeoutTimes``：超时次数:1~10，主要进行超时重发，减少偶发异常提高用户体验
    - ``period``：周期性指令时间间隔:1~1000ms，主要用于周期性指令每次下发的时间间隔"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置末端文件传输类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleFileType(type)``"
    "描述", "设置末端文件传输类型"
    "必选参数", "- ``type``：1-MCU升级文件,2-LUA文件"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置启用末端LUA执行
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnable(enable)``"
    "描述", "设置启用末端LUA执行"
    "必选参数", "- ``enable``：0-不启用；1-启用"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

末端LUA文件异常错误恢复
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRecoverAxleLuaErr(enable)``"
    "描述", "末端LUA文件异常错误恢复"
    "必选参数", "- ``status``：0-不恢复；1-恢复"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取末端LUA执行使能状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableStatus()``"
    "描述", "获取末端LUA执行使能状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``enable``：0-不启用；1-启用"

设置末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnableDeviceType(forceSensorEnable, gripperEnable, IOEnable)``"
    "描述", "设置末端LUA末端设备启用类型"
    "必选参数", "- ``forceSensorEnable``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable``：IO设备启用状态，0-不启用；1-启用"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDeviceType()``"
    "描述", "获取末端LUA末端设备启用类型"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``forceSensorEnable``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable``：IO设备启用状态，0-不启用；1-启用"

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDevice()``"
    "描述", "获取当前配置的末端设备"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``forceSensorEnable[8]``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable[8]``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable[8]``：IO设备启用状态，0-不启用；1-启用"

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "设置启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "获取启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"

机器人Ethercat从站文件写入
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SlaveFileWrite(type,slaveID,fileName)``"
    "描述", "机器人Ethercat从站文件写入"
    "必选参数", "- ``type``：从站文件类型，1-升级从站文件；2-升级从站配置文件
    - ``slaveID``：从站号
    - ``fileName``：上传文件名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

上传末端Lua开放协议文件
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleLuaUpload(filePath)``"
    "描述", "上传末端Lua开放协议文件"
    "必选参数", "- ``filePath``：本地lua文件路径名 .../AXLE_LUA_End_DaHuan.lua"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人Ethercat从站进入boot模式
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysServoBootMode(filePath)``"
    "描述", "机器人Ethercat从站进入boot模式"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人末端LUA文件操作代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua")
    param = [7, 8, 1, 0, 5, 3, 1]  # 对应AxleComParam参数
    robot.SetAxleCommunicationParam(7, 8, 1, 0, 5, 3, 1)
    error,getParam0,getParam1,getParam2,getParam3,getParam4,getParam5,getParam6 = robot.GetAxleCommunicationParam()
    print(f"GetAxleCommunicationParam param is:{getParam0} {getParam1} {getParam2} {getParam3} {getParam4} {getParam5} {getParam6}")
    robot.SetAxleLuaEnable(1)
    error,luaEnableStatus = robot.GetAxleLuaEnableStatus()
    robot.SetAxleLuaEnableDeviceType(0, 1, 0)
    error,forceEnable, gripperEnable, ioEnable = robot.GetAxleLuaEnableDeviceType()
    print(f"GetAxleLuaEnableDeviceType param is:{forceEnable} {gripperEnable} {ioEnable}")
    func = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    robot.SetAxleLuaGripperFunc(1, func)
    error,getFunc = robot.GetAxleLuaGripperFunc(1)
    error,getforceEnable, getgripperEnable, getioEnable = robot.GetAxleLuaEnableDevice()
    print("\ngetforceEnable status:", end=" ")
    for i in range(8):
        print(f"{getforceEnable[i]},", end="")
    print("\ngetgripperEnable status:", end=" ")
    for i in range(8):
        print(f"{getgripperEnable[i]},", end="")
    print("\ngetioEnable status:", end=" ")
    for i in range(8):
        print(f"{getioEnable[i]},", end="")
    print()
    robot.ActGripper(1, 0)
    time.sleep(2)
    robot.ActGripper(1, 1)
    time.sleep(2)
    robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0)
    while True:
        error,pkg = robot.GetRobotRealTimeState()
        print(f"gripper pos is:{pkg.gripper_position}")
        time.sleep(0.1)
    robot.CloseRPC()

    
获取SmartTool按钮状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSmarttoolBtnState()``"
    "描述", "获取SmartTool按钮状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)"

SmartTool按钮代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    while True:
        error,state = robot.GetSmarttoolBtnState()
        print(f"{state:016b}")
        time.sleep(0.1)

设置拖动开启前负载力检测
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTorqueDetectionSwitch(flag)``"
    "描述", "设置拖动开启前负载力检测"
    "必选参数", "- ``flag``：0-关闭；1-开启"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光外设打开关闭函数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingLaserOnOff(OnOff, weldId)``"
    "描述", "激光外设打开关闭函数"
    "必选参数", "- ``OnOff``：0-关闭；1-开启"
    "默认参数", "- ``weldId``：焊缝ID 默认为0"
    "返回值", "错误码 成功-0  失败- errcode"

激光跟踪开始结束函数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingTrackOnOff(OnOff, coordId)``"
    "描述", "激光跟踪开始结束函数"
    "必选参数", "- ``OnOff``：0-关闭；1-开启
    - ``coordId``：激光外设工具坐标系编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光寻位-固定方向
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSearchStart_xyz(direction, vel, distance, timeout, posSensorNum)``"
    "描述", "激光寻位-固定方向"
    "必选参数", "- ``direction``：0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    - ``vel``：速度 单位%
    - ``distance``：最大寻位距离 单位mm
    - ``timeout``：寻位超时时间 单位ms
    - ``posSensorNum``：激光标定的工具坐标编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光寻位-任意方向
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSearchStart_point(directionPoint, vel, distance, timeout, posSensorNum)``"
    "描述", "激光寻位-任意方向"
    "必选参数", "- ``directionPoint``：寻位输入的点的xyz左边,[x,y,z]
    - ``vel``：速度 单位%
    - ``distance``：最大寻位距离 单位mm
    - ``timeout``：寻位超时时间 单位ms
    - ``posSensorNum``：激光标定的工具坐标编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光IP配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSensorConfig(ip, port)``"
    "描述", "激光IP配置"
    "必选参数", "- ``ip``：激光外设的ip地址
    - ``port``：激光外设的端口号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光外设采样周期配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSensorSamplePeriod(period)``"
    "描述", "激光外设采样周期配置"
    "必选参数", "- ``period``：激光外设采样周期 单位ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光外设驱动加载
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadPosSensorDriver(type)``"
    "描述", "激光外设驱动加载"
    "必选参数", "- ``type``：激光外设驱动的协议类型 101-睿牛 102-创想 103-全视 104-同舟 105-奥太"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光外设驱动卸载
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``UnLoadPosSensorDriver()``"
    "描述", "激光外设驱动卸载"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊缝轨迹记录
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorRecord1(status, delayTime)``"
    "描述", "激光焊缝轨迹记录"
    "必选参数", "- ``status``：0-停止记录 1-实时跟踪  2-开始记录
    - ``delayTime``：延时时间 单位ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊缝轨迹复现
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorReplay(delayTime, speed)``"
    "描述", "激光焊缝轨迹复现"
    "必选参数", "- ``delayTime``：延时时间 单位ms
    - ``speed``：速度 单位%"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
激光跟踪复现
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveLTR()``"
    "描述", "激光跟踪复现"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊缝轨迹复现
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorRecordandReplay(delayMode, delayTime, delayDisExAxisNum, delayDis, sensitivePara, int trackMode, int triggerMode, double runTime, speed)``"
    "描述", "激光焊缝轨迹复现"
    "必选参数", "- ``delayMode``：模式 0-延时时间 1-延时距离
    - ``delayTime``：延时时间 单位ms
    - ``delayDisExAxisNum``：扩展轴编号
    - ``delayDis``：延时距离 单位mm
    - ``sensitivePara``：补偿灵敏系数
    - ``trackMode``：定点跟踪类型。0-扩展轴异步运动；1-机器人
    - ``triggerMode``：定点跟踪触发方式。0-跟踪时长；1-IO
    - ``runTime``：机器人定点跟踪时长(s)
    - ``speed``：速度 单位%"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

运动到焊缝记录的起点
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserRecordStart(moveType, ovl)``"
    "描述", "运动到焊缝记录的起点"
    "必选参数", "- ``moveType``：0-PTP 1-LIN
    - ``ovl``：速度 单位%"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

运动到焊缝记录的终点
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserRecordEnd(moveType, ovl)``"
    "描述", "运动到焊缝记录的终点"
    "必选参数", "- ``moveType``：0-PTP 1-LIN
    - ``ovl``：速度 单位%"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

运动到激光传感器寻位点
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserSeamPos(moveFlag, ovl, dataFlag, plateType, trackOffectType, offset)``"
    "描述", "运动到激光传感器寻位点"
    "必选参数", "- ``moveFlag``：运动类型：0-PTP；1-LIN
    - ``ovl``：速度缩放因子，0-100
    - ``dataFlag``：焊缝缓存数据选择：0-执行规划数据；1-执行记录数据
    - ``plateType``：板材类型：0-波纹板；1-瓦楞板；2-围栏板；3-油桶；4-波纹甲壳钢
    - ``trackOffectType``：激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
    - ``offset``：偏移量"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取激光传感器寻位点坐标信息
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserSeamPos(trackOffectType, offset)``"
    "描述", "获取激光传感器寻位点坐标信息"
    "必选参数", "- ``trackOffectType``：激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
    - ``offset``：偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``jPos``：关节位置[°]
    - ``descPos``：笛卡尔位置[mm]
    - ``tool``：工具坐标系
    - ``user``：工件坐标系
    - ``exaxis``：扩展轴位置[mm]"

激光外设传感器参数配置及调试代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.LaserTrackingSensorConfig("192.168.58.20", 5020)
    robot.LaserTrackingSensorSamplePeriod(20)
    robot.LoadPosSensorDriver(101)
    robot.LaserTrackingLaserOnOff(0, 0)
    time.sleep(3)
    robot.LaserTrackingLaserOnOff(1, 0)
    robot.CloseRPC()

激光轨迹扫描及轨迹复现的代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    i = 0
    while i<10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(2, 10)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 50,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(0, 10)
        robot.MoveToLaserRecordStart(1, 30)
        robot.LaserSensorReplay(10, 100)
        robot.MoveLTR()
        robot.LaserSensorRecord1(0, 10)
        i = i+1
    robot.CloseRPC()

激光寻位及实时跟踪的代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    time.sleep(8)
    i = 0
    while i < 10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        directionPoint = [0.0] * 3
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3)
        robot.LaserTrackingSearchStop()
        robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese)
        robot.LaserTrackingTrackOnOff(1, 3)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 20,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingTrackOnOff(0, 3)
        i = i + 1
        print(i)
    robot.CloseRPC()

扩展轴与机器人同步进行激光跟踪的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startexaxisPos = [0.0, 0.0, 0.0, 0.0]
    seamexaxisPos = [-10.0, 0.0, 0.0, 0.0]
    endexaxisPos = [-30.0, 0.0, 0.0, 0.0]
    offdese = [0.0] * 6
    seamjointPos = [0.0] * 6
    seamdescPose = [0.0] * 6
    i=0
    while i < 10:
        startjointPos = [58.337, -119.628, 146.037, -116.358, -92.224, -117.654]
        startdescPose = [-53.375, -255.363, 0.919, 178.054, 1.077, -94.026]
        robot.ExtAxisSyncMoveJ(joint_pos=startjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= startexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
        ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2)
        robot.LaserTrackingSearchStop()
        tool = 0
        user = 0
        rnte, seamjointPos, seamdescPose, tool, user, startexaxisPos = robot.GetLaserSeamPos(0, offdese)
        print(f"{seamjointPos[0]},{seamjointPos[1]},{seamjointPos[2]},{seamjointPos[3]},{seamjointPos[4]},{seamjointPos[5]},{seamdescPose[0]},{seamdescPose[1]},{seamdescPose[2]},{seamdescPose[3]},{seamdescPose[4]},{seamdescPose[5]}")
        if ret == 0:
            robot.ExtAxisSyncMoveJ(joint_pos=seamjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= seamexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(1, 2)
            endjointPos = [70.580, -90.918, 126.593, -125.154, -92.162, -105.403]
            enddescPose = [-53.375, -419.020, 0.920, 178.054, 1.076, -94.026]
            robot.ExtAxisSyncMoveL(desc_pos=enddescPose, tool=1,user= 0,vel= 20,acc= 100, ovl=100,blendR= -1,exaxis_pos= endexaxisPos,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(0, 2)
        i = i+1
        print(i)
    robot.CloseRPC()

控制阵列式吸盘
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSuckerCtrl(slaveID, len, ctrlValue)``"
    "描述", "控制阵列式吸盘"
    "必选参数", "- ``slaveID``：从站号
    - ``len``：长度
    - ``ctrlValue``：控制值 1-按最大真空度吸取 2-按设定真空度吸取 3-停止吸取"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取阵列式吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSuckerState(slaveID)``"
    "描述", "获取阵列式吸盘状态"
    "必选参数", "- ``slaveID``：从站号"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    - ``pressValue``：当前真空度 单位kpa
    - ``error``：吸盘当前的错误码"

等待吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitSuckerState(slaveID, state, ms)``"
    "描述", "等待吸盘状态"
    "必选参数", "- ``slaveID``：从站号
    - ``state``：吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    - ``ms``：等待最大时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

阵列式吸盘控制指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("C://项目/外设SDK/CtrlDev_sucker.lua")
    time.sleep(2)
    robot.UnloadCtrlOpenLUA(1)
    robot.LoadCtrlOpenLUA(1)
    time.sleep(1)
    ctrl = bytearray(20)
    ctrl[0] = 1
    robot.SetSuckerCtrl(0, 1, ctrl)
    for i in range(100):
        rtn, state, press_value, error = robot.GetSuckerState(1)
        print(f"sucker1 state is {state}, pressValue is {press_value}, error num is {error}")
        rtn, state, press_value, error = robot.GetSuckerState(12)
        print(f"sucker12 state is {state}, pressValue is {press_value}, error num is {error}")
        time.sleep(0.1)
    ret = robot.WaitSuckerState(1, 1, 100)
    print(f"WaitSuckerState result is {ret}")
    ctrl[0] = 3
    robot.SetSuckerCtrl(1, 1, ctrl)
    robot.SetSuckerCtrl(12, 1, ctrl)
    robot.CloseRPC()

上传开放协议的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaUpload(filePath)``"
    "描述", "上传开放协议的Lua文件"
    "必选参数", "- ``filePath``：本地开放协议lua文件路径名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取从站板卡参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetFieldBusConfig()``"
    "描述", "获取从站板卡参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``type``：0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    - ``version``：协议版本
    - ``connState``：0-未连接 1-已连接"

写入从站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWriteDO(DOIndex, wirteNum, status)``"
    "描述", "写入从站DO"
    "必选参数", "- ``DOIndex``：DO编号
    - ``wirteNum``：写入的数量
    - ``status``：写入的数值，最多写8个"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

写入从站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWriteAO(AOIndex, wirteNum, status)``"
    "描述", "写入从站AO"
    "必选参数", "- ``AOIndex``：AO编号
    - ``wirteNum``：写入的数量
    - ``status``：写入的数值，最多写8个"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

读取从站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadDI(DOIndex, readeNum)``"
    "描述", "读取从站DI"
    "必选参数", "- ``DOIndex``：DI编号
    - ``readeNum``：读取的数量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``status[8]``：读取到的数值，最多读8个"

读取从站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadAI(AOIndex, readeNum)``"
    "描述", "读取从站AI"
    "必选参数", "- ``AOIndex``：AI编号
    - ``readeNum``：读取的数量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``status[8]``：读取到的数值，最多读8个"

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWaitDI(DIIndex, status, waitMs)``"
    "描述", "等待扩展DI输入"
    "必选参数", "- ``DIIndex``：DI编号
    - ``status``：0-低电平；1-高电平
    - ``waitMs``：最大等待时间(ms)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWaitAI(AIIndex, waitType, value, waitMs)``"
    "描述", "等待扩展AI输入"
    "必选参数", "- ``AIIndex``：AI编号
    - ``waitType``：0-大于；1-小于
    - ``value``：AI值
    - ``waitMs``：最大等待时间(ms)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

从站模式相关接口指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/外设/CtrlDev_field.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(3,"CtrlDev_field.lua")
    robot.UnloadCtrlOpenLUA(3)
    robot.LoadCtrlOpenLUA(3)
    time.sleep(8)
    rtn,type, version, conn_state = robot.GetFieldBusConfig()
    print(f"type is {type}, version is {version}, connState is {conn_state}")
    # Write digital outputs
    ctrl = [1, 0, 1]  # DO0=1, DO1=0, DO2=1
    robot.FieldBusSlaveWriteDO(0, 3, ctrl)
    # Write analog output
    ctrl_ao = [0x1000]  # AO2 = 0x1000
    robot.FieldBusSlaveWriteAO(2, 1, ctrl_ao)
    for i in range(100):
        rtn,di = robot.FieldBusSlaveReadDI(0, 4)
        print(f"DI0 is {di[0]}, DI1 is {di[1]}, DI2 is {di[2]}, DI3 is {di[3]}")
        rtn, ai = robot.FieldBusSlaveReadAI(0, 3)
        print(f"AI0 is {ai[0]}, AI1 is {ai[1]}, AI2 is {ai[2]}")
        time.sleep(0.01)
    ret = robot.FieldBusSlaveWaitDI(0, 1, 100)
    print(f"FieldBusSlaveWaitDI result is {ret}")
    ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00, 100)
    print(f"FieldBusSlaveWaitAI result is {ret}")
    robot.CloseRPC()

末端透传功能打开关闭SDK接口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleGenComEnable(mode)``"
    "描述", "开启末端通用透传功能"
    "必选参数", "- ``mode``：使能，0-关闭，1-开启"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

末端透传功能非周期数据收发SDK接口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SndRcvAxleGenComCmdData( len_snd, sndBuff, len_rcv)``"
    "描述", "末端发送非周期数据并等待应答"
    "必选参数", "
    - ``len_snd``：发送的长度;
    - ``sndBuff[]``：发送数据;
    - ``len_rcv``：选择接受的长度;
    - ``rcvBuff[]``：应答的数据;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

基于末端透传功能倍益康艾灸头非周期数据通信代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # A connection is established with the robot controller. A successful connection returns a robot object
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    import time


    def testAxleGenCom(self):

        led_on = [0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79]
        led_off = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        version = [0xAB, 0xBA, 0x11, 0x00, 0x76]
        state = [0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B]
        cycleState = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        cnt = 1

        p1Joint = [88.708, -86.178, 140.989, -141.825, -89.162, -49.879]
        p1Desc = [188.007, -377.850, 260.207, 178.715, 2.823, -131.466]
        p2Joint = [112.131, -75.554, 126.989, -139.027, -88.044, -26.477]
        p2Desc = [368.003, -377.848, 260.211, 178.715, 2.823, -131.465]

        exaxisPos = [0, 0, 0, 0]
        offdese = [0, 0, 0, 0, 0, 0]

        #开启末端透传功能
        robot.SetAxleGenComEnable(1)
        robot.SetAxleLuaEnable(1)

        while cnt <= 10000:
            #读取版本号
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(len_snd=5, sndBuff=version, len_rcv=10)
            print(ret)
            print(rcvdata)
            print(f"hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}")
            if ret != 0:
                break
            time.sleep(1)
            # 读取艾灸头在位状态
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, state, 6)
            print(f"state : {rcvdata[4]} ")
            time.sleep(1)
            # 开启艾灸头激光
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, led_on, 6)
            print(f"led on rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,
                            offset_flag=0, offset_pos=offdese)
            time.sleep(4)
            # 关闭艾灸头激光
            ret, rcvdata = robot.SndRcvAxleGenComCmdData(6, led_off, 6)
            print(f"led off rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,offset_flag=0, offset_pos=offdese)
            time.sleep(1)
            print(f"***********************complate No. {cnt} SDK test*****************************")
            cnt = cnt + 1

        robot.CloseRPC()
        return 0

    testAxleGenCom(robot)
    
下载开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaDownload(fileName, savePath)``"
    "描述", "下载开放协议Lua文件"
    "必选参数", "
    - ``fileName``：开放协议文件名称“CtrlDev_XXX.lua”;
    - ``savePath``开放协议保存文件路径;
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
删除指定开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaDelete(fileName)``"
    "描述", "删除指定开放协议Lua文件"
    "必选参数", "
    - ``fileName``：要删除的开放协议lua文件名“CtrlDev_XXX.lua”
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
删除所有开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AllOpenLuaDelete()``"
    "描述", "删除所有开放协议Lua文件"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

开放协议lua文件操作SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')


    def TestCtrlOpenLuaOperate(self):
        # 上传Lua文件到机器人
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        # 从机器人下载Lua文件
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        # 设置控制开放的Lua文件名
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        # 获取控制开放的Lua文件名
        rtn, name = robot.GetCtrlOpenLUAName()
        print(f"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}")
        
        # 加载控制开放的Lua
        rtn = robot.LoadCtrlOpenLUA(1)
        print(f"LoadCtrlOpenLUA rtn is {rtn}")
        time.sleep(2)
        
        # 卸载控制开放的Lua
        rtn = robot.UnloadCtrlOpenLUA(1)
        print(f"UnloadCtrlOpenLUA rtn is {rtn}")
        
        # 删除指定的Lua文件
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua")
        print(f"OpenLuaDelete rtn is {rtn}")
        
        # 删除所有Lua文件
        rtn = robot.AllOpenLuaDelete()
        print(f"AllOpenLuaDelete rtn is {rtn}")
        
        # 关闭连接
        robot.CloseRPC()
        time.sleep(1)


    # 调用测试函数
    TestCtrlOpenLuaOperate(robot)