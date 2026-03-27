机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置轨迹记录参数
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDParam(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "设置轨迹记录参数"
    "必选参数", "- ``name``：轨迹名；
    - ``period_ms``：采样周期，固定值，2ms 或 4ms 或 8ms;"
    "默认参数", "- ``type``：数据类型，1-关节位置；
    - ``di_choose``：DI 选择,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不选择，1-选择 默认0;
    - ``do_choose``：DO 选择,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不选择，1-选择 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

开始轨迹记录
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDStart(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "开始轨迹记录"
    "必选参数", "- ``name``：轨迹名；
    - ``period_ms``：采样周期，固定值，2ms或4ms或8ms；"
    "默认参数", "- ``type``：数数据类型，1-关节位置 默认1;
    - ``di_choose``：DI 选择,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不选择，1-选择 默认0;
    - ``do_choose``：DO 选择,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不选择，1-选择 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

停止轨迹记录
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWebTPDStop()``"
    "描述", "停止轨迹记录"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

删除轨迹记录
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDDelete(name)``"
    "描述", "删除轨迹记录"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
+++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    robot.SetTPDParam(name, period_ms)
    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(1)
    robot.SetTPDStart(name, period_ms)
    print("SetTPDStart")
    time.sleep(10)
    robot.SetWebTPDStop()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

轨迹预加载
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTPD(name)``"
    "描述", "轨迹预加载"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹复现
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTPD(name,blend,ovl)``"
    "描述", "轨迹复现"
    "必选参数", "- ``name``:轨迹名
    - ``blend``：是否平滑，0-不平滑，1-平滑
    - ``ovl``：速度缩放因子，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取轨迹起始位姿
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTPDStartPose(name)``"
    "描述", "获取轨迹起始位姿"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：轨迹起始位姿"

机器人TPD轨迹记录代码示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    ovl = 100.0
    blend = 0
    rtn = robot.LoadTPD(name)
    print(f"LoadTPD rtn is: {rtn}")
    error,start_pose = robot.GetTPDStartPose(name)
    print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. "
          f"rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
    robot.MoveCart(start_pose, 0, 0, 100, 100)
    time.sleep(1)
    rtn = robot.MoveTPD(name, blend, ovl)
    print(f"MoveTPD rtn is: {rtn}")
    time.sleep(5)
    robot.SetTPDDelete(name)
    robot.CloseRPC()

轨迹预处理
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryJ(name,ovl,opt=1)``"
    "描述", "轨迹预处理"
    "必选参数", "- ``name``:轨迹名,如：/fruser/traj/trajHelix_aima_1.txt;
    - ``ovl``：速度缩放百分比，范围[0~100];"
    "默认参数", "- ``opt``：1-控制点，默认为1"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹复现
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryJ()``"
    "描述", "轨迹复现"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取轨迹起始位姿
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryStartPose(name)``"
    "描述", "获取轨迹起始位姿"
    "必选参数", "``name``:轨迹名"
    "默认参数", "无"       
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：轨迹起始位姿"

获取轨迹点编号
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryPointNum()``"
    "描述", "获取轨迹点编号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``pnum``：轨迹点编号"

设置轨迹运行中的速度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJSpeed(ovl)``"
    "描述", "设置轨迹运行中的速度"
    "必选参数", "``ovl``:速度缩放百分比，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的力和扭矩
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceTorque(ft)``"
    "描述", "设置轨迹运行中的力和扭矩"
    "必选参数", "``ft=[fx,fy,fz,tx,ty,tz]``:单位N和Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿x方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fx)``"
    "描述", "设置轨迹运行中的沿x方向的力"
    "必选参数", "``ft``:沿x方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿y方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fy)``"
    "描述", "设置轨迹运行中的沿y方向的力"
    "必选参数", "``fy``:沿y方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿z方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fz)``"
    "描述", "设置轨迹运行中的沿z方向的力"
    "必选参数", "``fz``:沿z方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕x轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tx)``"
    "描述", "设置轨迹运行中的绕x轴的扭矩"
    "必选参数", "``tx``:绕x轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕y轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(ty)``"
    "描述", "设置轨迹运行中的绕y轴的扭矩"
    "必选参数", "``ty``:绕y轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕z轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tz)``"
    "描述", "设置轨迹运行中的绕z轴的扭矩"
    "必选参数", "- ``tz``:绕z轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

上传轨迹J文件
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJUpLoad(filePath)``"
    "描述", "上传轨迹J文件"
    "必选参数", "- ``filePath``:上传轨迹文件的全路径名，C://test/testJ.txt"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

删除轨迹J文件
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJDelete(filePath)``"
    "描述", "删除轨迹J文件"
    "必选参数", "- ``filePath``:删除轨迹文件的全路径名，C://test/testJ.txt"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人轨迹J文件复现代码示例
+++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "/fruser/traj/traj.txt"
    rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1)
    print(f"LoadTrajectoryJ {traj_file_name}, rtn is: {rtn}")
    rtn,traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos:{traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},"
          f"{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 50, 100, 100)
    rtn,traj_num = robot.GetTrajectoryPointNum()
    print(f"GetTrajectoryStartPose rtn is: {rtn}, traj num is: {traj_num}")
    rtn = robot.SetTrajectoryJSpeed(50.0)
    print(f"SetTrajectoryJSpeed is: {rtn}")
    traj_force = [0.0,0.0,0.0,0.0,0.0,0.0]
    traj_force[0] = 10  # fx = 10
    rtn = robot.SetTrajectoryJForceTorque(traj_force)
    print(f"SetTrajectoryJForceTorque rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFx(10.0)
    print(f"SetTrajectoryJForceFx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFy(0.0)
    print(f"SetTrajectoryJForceFy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFz(0.0)
    print(f"SetTrajectoryJForceFz rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTx(10.0)
    print(f"SetTrajectoryJTorqueTx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTy(10.0)
    print(f"SetTrajectoryJTorqueTy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTz(10.0)
    print(f"SetTrajectoryJTorqueTz rtn is: {rtn}")
    rtn = robot.MoveTrajectoryJ()
    print(f"MoveTrajectoryJ rtn is: {rtn}")
    robot.CloseRPC()

轨迹预处理(轨迹前瞻)
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryLA(name, mode, errorLim, type, precision, vamx, amax, jmax, flag)``"
    "描述", "轨迹预处理(轨迹前瞻)"
    "必选参数", "- ``name``:轨迹文件名
    - ``mode``：采样模式，0-不进行采样；1-等数据间隔采样；2-等误差限制采样
    - ``errorLim``:误差限制，使用直线拟合生效
    - ``type``:平滑方式，0-贝塞尔平滑
    - ``precision``:平滑精度，使用贝塞尔平滑时生效
    - ``vamx``:设定的最大速度，mm/s
    - ``amax``:设定的最大加速度，mm/s2
    - ``jmax``:设定的最大加加速度，mm/s3
    - ``flag``:匀速前瞻开启开关 0-不开启；1-开启"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹复现(轨迹前瞻)
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryLA()``"
    "描述", "轨迹复现(轨迹前瞻)"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹复现(轨迹前瞻)代码示例
+++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "/fruser/traj/traj.txt"
    rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 50, 200, 1000, 0)
    print(f"LoadTrajectoryLA {traj_file_name}, rtn is: {rtn}")
    rtn, traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos: {traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100)
    rtn = robot.MoveTrajectoryLA()
    print(f"MoveTrajectoryLA rtn is: {rtn}")
    robot.CloseRPC()

运动到TPD轨迹记录起点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToTPDStart(name, moveType, ovl)``"
    "描述", "运动到TPD轨迹记录起点"
    "必选参数", "
    - ``name``:轨迹文件名
    - ``moveType``：运动类型；0-PTP; 1-LIN
    - ``ovl``:速度缩放百分比，范围[0~100]
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

运动到TPD轨迹记录起点的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # A connection is established with the robot controller. A successful connection returns a robot object
    # 与机器人控制器建立连接,连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    import time

    def TestTPD(self):
        type = 1
        name = "tpd2025"
        period_ms = 4
        di_choose = 0
        do_choose = 0

        robot.SetTPDParam(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)

        robot.Mode(1)
        time.sleep(1)
        robot.DragTeachSwitch(1)
        robot.SetTPDStart(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)
        time.sleep(3)
        robot.SetWebTPDStop()
        robot.DragTeachSwitch(0)

        time.sleep(1)
        ovl = 100.0
        blend = 0
        start_pose = [0.0] * 6
        rtn = robot.LoadTPD(name)
        print(f"LoadTPD rtn is: {rtn}")

        rtn, start_pose = robot.GetTPDStartPose(name)
        print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
        # robot.MoveCart(desc_pos=start_pose, tool=0, user=0, vel=100, acc=100, ovl=ovl, blendT=-1, config=-1)
        #time.sleep(1)

        rtn = robot.MoveToTPDStart(name, 0, 100)
        print(f"MoveToTPDStart rtn is: {rtn}")

        rtn = robot.MoveTPD(name, blend, ovl)
        print(f"MoveTPD rtn is: {rtn}")
        time.sleep(5)

        robot.SetTPDDelete(name)

        robot.CloseRPC()
        return 0

    TestTPD(robot)
