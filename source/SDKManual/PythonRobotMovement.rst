机器人运动
============

.. toctree:: 
    :maxdepth: 5

jog点动
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StartJOG(ref,nb,dir,max_dis,vel=20.0,acc=100.0)``"
    "描述", "jog点动"
    "必选参数", "- ``ref``：0-关节点动,2-基坐标系点动,4-工具坐标系点动,8-工件坐标系点动；
    - ``nb``：1-1关节(x轴),2-2关节(y轴),3-3关节(z轴),4-4关节(rx),5-5关节(ry),6-6关节(rz);
    - ``dir``：0-负方向，1-正方向;
    - ``max_dis``：单次点动最大角度/距离，单位 ° 或 mm;"
    "默认参数", "- ``vel``：速度百分比，[0~100] 默认20;
    - ``acc``：加速度百分比，[0~100] 默认100;"
    "返回值", "错误码 成功-0  失败- errcode"

jog点动减速停止
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StopJOG(ref)``"
    "描述", "jog点动减速停止"
    "必选参数", "- ``ref``：1-关节点动停止,3-基坐标系点动停止,5-工具坐标系点动停止,9-工件坐标系点动停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

jog点动立即停止
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ImmStopJOG()``"
    "描述", "jog点动立即停止"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人点动控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    for i in range(6):
        robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(5)
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(9)
        time.sleep(1)
    robot.CloseRPC()

关节空间运动
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveJ(joint_pos, tool, user, desc_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0, ovl = 100.0, exaxis_pos = [0.0,0.0,0.0,0.0], blendT = -1.0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "关节空间运动"
    "必选参数", "- ``joint_pos``:目标关节位置，单位[°]；
    - ``tool``:工具号，[0~14]；
    - ``user``:工件号，[0~14]；"
    "默认参数", "- ``desc_pos``:目标笛卡尔位姿，单位 [mm][°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用正运动学求解返回值;
    - ``vel``:速度百分比，[0~100] 默认20.0;
    - ``acc``:加速度百分比，[0~100]，暂不开放；
    - ``ovl``:速度缩放因子，[0~100] 默认100.0;
    - ``exaxis_pos``:外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``blendT``:[-1.0]-运动到位 (阻塞)，[0~500.0]-平滑时间 (非阻塞)，单位 [ms] 默认-1.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``offset_pos``:位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0];"
    "返回值", "错误码  成功-0  失败- errcode"

笛卡尔空间直线运动
+++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveL(desc_pos, tool, user, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0,blendR=-1.0, blendMode = 0,exaxis_pos=[0.0, 0.0, 0.0, 0.0], search=0, offset_flag=0,offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],oacc = 100.0,config=-1,velAccParamMode=0,overSpeedStrategy=0,speedPercent=10)``"
    "描述", "笛卡尔空间直线运动"
    "必选参数", "- ``desc_pos``:目标笛卡尔位姿，单位[mm][°]；
    - ``tool``:工具号，[0~14]；
    - ``user``:工件号，[0~14]；"
    "默认参数", "- ``joint_pos``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel``:速度百分比，[0~100] 默认20.0；
    - ``acc``:加速度百分比，[0~100]，暂不开放 默认0.0；
    - ``ovl``:速度缩放因子，[0~100] 默认100.0；
    - ``blendR``:[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0;
    - ``blendMode``:过渡方式；0-内切过渡；1-角点过渡,默认-0;
    - ``exaxis_pos``:外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``search``:[0]-不焊丝寻位，[1]-焊丝寻位；
    - ``offset_flag``:[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``offset_pos``:位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0];
    - ``oacc``:加速度缩放因子[0-100]/物理加速度(mm/s2) 默认 100;
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1
    - ``velAccParamMode``:速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默认0
    - ``overSpeedStrategy``:超速处理策略，0-策略关闭；1-标准；2-超速时报错停止；3-自适应降速，默认为0
    - ``speedPercent``:允许降速阈值百分比[0-100]，默认10%
    "
    "返回值", "错误码 成功-0  失败- errcode"

笛卡尔空间圆弧运动
++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveC(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=100.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], offset_flag_p=0,offset_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_t=20.0, acc_t=100.0, exaxis_pos_t=[0.0, 0.0, 0.0, 0.0], offset_flag_t=0,offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],ovl=100.0, blendR=-1.0,oacc=100.0,config=-1,velAccParamMode=0)``"
    "描述", "笛卡尔空间圆弧运动"
    "必选参数", "- ``desc_pos_p``:路径点笛卡尔位姿，单位[mm][°]；
    - ``tool_p``:路径点工具号，[0~14];
    - ``user_p``:路径点工件号，[0~14];
    - ``desc_pos_t``:目标点笛卡尔位姿，单位 [mm][°];
    - ``tool_t``:工具号，[0~14]；
    - ``user_t``:工件号，[0~14]；"
    "默认参数", "- ``joint_pos_p``:路径点关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``joint_pos_t``:目标点关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel_p``:路径点速度百分比，[0~100] 默认20.0;
    - ``acc_p``:路径点加速度百分比，[0~100] 暂不开放,默认0.0;
    - ``exaxis_pos_p``:路径点外部轴 1位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``offset_flag_p``:路径点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``vel_t``:目标点速度百分比，[0~100] 默认20.0;
    - ``acc_t``:目标点加速度百分比，[0~100] 暂不开放 默认0.0;
    - ``exaxis_pos_t``:目标点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``offset_flag_t``:目标点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``offset_pos_t``:目标点位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0];
    - ``ovl:``:速度缩放因子，[0~100] 默认100.0;
    - ``blendR``:[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0;
    - ``oacc``:加速度缩放因子[0-100]/物理加速度(mm/s2) 默认 100;
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1;
    - ``velAccParamMode``:速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

笛卡尔空间整圆运动
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Circle(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=0.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=0.0,exaxis_pos_t=[0.0, 0.0, 0.0, 0.0],ovl=100.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], oacc=100.0, blendR=-1,config=-1,velAccParamMode=0)``"
    "描述", "笛卡尔空间整圆运动"
    "必选参数", "- ``desc_pos_p``:路径点笛卡尔位姿，单位[mm][°]；
    - ``tool_p``:工具号，[0~14]；
    - ``user_p``:工件号，[0~14]；
    - ``desc_pos_t``:目标点笛卡尔位姿，单位[mm][°]；
    - ``tool_t``:工具号，[0~14]；
    - ``user_t``:工件号，[0~14]；"
    "默认参数", "- ``joint_pos_p``:路径点关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``joint_pos_t``:目标点关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel_p``:速度百分比，[0~100] 默认20.0;
    - ``acc_p``:路径点加速度百分比，[0~100] 暂不开放 默认0.0;
    - ``exaxis_pos_p``:路径点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``vel_t``:目标点速度百分比，[0~100] 默认20.0;
    - ``acc_t``:目标点加速度百分比，[0~100] 暂不开放 默认0.0;
    - ``exaxis_pos_t``:标点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]
    - ``ovl``:速度缩放因子，[0~100] 默认100.0;
    - ``offset_flag``:是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``offset_pos``:位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]
    - ``oacc``:加速度缩放因子[0-100]/物理加速度(mm/s2)，默认：100；
    - ``blendR``:-1：阻塞；0~1000：平滑半径,默认：-1；
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1;
    - ``velAccParamMode``:速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

笛卡尔空间点到点运动
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveCart(desc_pos, tool, user, vel = 20.0, acc = 0.0, ovl = 100.0, blendT = -1.0, config = -1)``"
    "描述", "笛卡尔空间点到点运动"
    "必选参数", "- ``desc_pos``:目标笛卡尔位置；
    - ``tool``:工具号，[0~14]；
    - ``user``:工件号，[0~14]；"
    "默认参数", "- ``vel``:速度，范围 [0~100]，默认为 20.0;
    - ``acc``:加速度，范围 [0~100]，暂不开放,默认为 0.0;
    - ``ovl``:速度缩放因子，[0~100]，默认为 100.0;
    - ``blendT``:[-1.0]-运动到位 (阻塞)，[0~500]-平滑时间 (非阻塞)，单位 [ms] 默认为 -1.0;
    - ``config``:关节配置，[-1]-参考当前关节位置求解，[0~7]-依据关节配置求解 默认为 -1"
    "返回值", "错误码 成功-0  失败- errcode"

机器人基本运动指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    j4 = [-31.154, -95.317, 94.276, -88.079, -89.740, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    desc_pos4 = [-443.165, 147.881, 480.951, 179.511, -0.775, -15.409]
    offset_pos = [0.0] * 6
    epos = [0.0] * 4
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    oacc = 100.0
    blendT = 0.0
    blendR = 0.0
    flag = 0
    search = 0
    blendMode = 0
    velAccMode = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos,oacc=oacc, velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel,acc_t=acc, exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, oacc=oacc, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl,offset_flag=flag, offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    rtn = robot.MoveCart(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, acc=acc,ovl=ovl, blendT=blendT, config=-1)
    print(f"MoveCart errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos, config=-1,velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc,exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, config=-1, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl, offset_flag=flag,offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    robot.CloseRPC()
    return 0

笛卡尔空间螺旋线运动
++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSpiral(desc_pos, tool, user, param, joint_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0, exaxis_pos = [0.0,0.0,0.0,0.0], ovl = 100.0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0], config = -1)``"
    "描述", "笛卡尔空间螺旋线运动"
    "必选参数", "- ``desc_pos``:目标笛卡尔位姿，单位[mm][°];
    - ``tool``:工具号，[0~14];
    - ``user``:工件号，[0~14];
    - ``param=[circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]``：circle_num: 螺旋圈数;circle_angle: 螺旋倾角;rad_init: 螺旋初始半径;rad_add: 半径增量;rotaxis_add: 转轴方向增量;rot_direction: 旋转方向，0-顺时针，1-逆时针, velAccMode速度加速度参数模式：0-角速度恒定，1-线速度恒定;"
    "默认参数", "- ``joint_pos``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel``:速度百分比，[0~100] 默认20.0;
    - ``acc``:加速度百分比，[0~100] 默认100.0;
    - ``exaxis_pos``:外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0];
    - ``ovl``:速度缩放因子，[0~100] 默认100.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0;
    - ``offset_pos``:位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j = [67.957, -81.482, 87.595, -95.691, -94.899, -9.727]
    desc_pos = [-123.142, -551.735, 430.549, 178.753, -4.757, 167.754]
    offset_pos1 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    offset_pos2 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    epos = [0.0] * 4
    sp = [2, 30.0, 50.0, 10.0, 10.0, 0, 1]  # [circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]
    tool = 0
    user = 0
    vel = 30.0
    acc = 60.0
    ovl = 100.0
    blendT = -1.0
    flag = 2
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos1)
    print(f"movej errcode:{rtn}")
    rtn = robot.NewSpiral(desc_pos=desc_pos, tool=tool, user=user, vel=vel, acc=acc, exaxis_pos=epos, ovl=ovl, offset_flag=flag, offset_pos=offset_pos2, param=sp)
    print(f"newspiral errcode:{rtn}")
    robot.CloseRPC()
    return 0

伺服运动开始
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveStart(cmdType=0)``"
    "描述", "伺服运动开始，配合ServoJ、ServoCart指令使用"
    "必选参数", "- ``cmdType``: 命令传输类型，0=XML-RPC，1=UDP透传"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

伺服运动结束
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveEnd(cmdType=0)``"
    "描述", "伺服运动结束，配合ServoJ、ServoCart指令使用"
    "必选参数", "- ``cmdType``: 命令传输类型，0=XML-RPC，1=UDP透传"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关节空间伺服模式运动
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJ(joint_pos, axisPos, acc = 0.0, vel = 0.0, cmdT = 0.008, filterT = 0.0, gain = 0.0, id=0, cmdType=0)``"
    "描述", "关节空间伺服模式运动"
    "必选参数", "- ``joint_pos``:目标关节位置，单位[°]；
    - ``axisPos``:外部轴位置,单位mm；"
    "默认参数", "- ``acc``:加速度，范围 [0~100]，暂不开放，默认为 0.0;
    - ``vel``:速度，范围 [0~100]，暂不开放，默认为 0.0;
    - ``cmdT``:指令下发周期，单位s，建议范围[0.001~0.0016], 默认为0.008;
    - ``filterT``:滤波时间，单位 [s]，暂不开放， 默认为0.0;
    - ``gain``:目标位置的比例放大器，暂不开放， 默认为0.0;
    - ``id``:servoJ指令ID,默认为0;
    - ``cmdType``:命令传输类型，0=XML-RPC，1=UDP透传;"
    "返回值", "错误码 成功-0  失败- errcode"

基于UDP通信的ServoJ、ServoMoveStart、ServoMoveEnd SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def TestServoJUDP(self):
        # 设置回调
        def callback(src_type, count, cmd_id, data_len, content):
            print("回调函数: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        # # 初始化关节位置和外部轴位置
        j= [105, -108, 74, -66, -88.893, -1.621]
        offset_pos = [0, 0, 0, 0, 0, 0]
        epos = [0, 0, 0, 0]
        # # 移动到初始位置
        result=robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100,exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        print("MoveJ返回结果: {}".format(result))
        vel = 0.0
        acc = 0.0
        cmdT = 0.016
        filterT = 0.0
        gain = 0.0
        flag = 0
        dt = 0.1
        cmdID = 0

        # 获取当前关节位置
        ret, j = robot.GetActualJointPosDegree(flag)
        if ret != 0:
            print(f"GetActualJointPosDegree errcode:{ret}")
        while 1:
            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("ServoMoveStart返回结果: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT,filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] += dt
                j[1] += dt
                j[2] += dt
                j[3] += dt
                j[4] += dt
                j[5] += dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("ServoMoveEnd返回结果: {}".format(result))

            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("ServoMoveStart返回结果: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT,filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] -= dt
                j[1] -= dt
                j[2] -= dt
                j[3] -= dt
                j[4] -= dt
                j[5] -= dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("ServoMoveEnd返回结果: {}".format(result))
        robot.CloseRPC()
        return 0
    TestServoJUDP(robot)

关节空间伺服模式运动代码示例
++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j = [0.0] * 6
    epos = [0.0] * 4
    vel = 0.0
    acc = 0.0
    cmdT = 0.008
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 500
    dt = 0.1
    cmdID = 0
    ret, j = robot.GetActualJointPosDegree(flag)
    if ret == 0:
        cmdID += 1
        robot.ServoMoveStart()
        while count:
            robot.ServoJ(joint_pos=j,axisPos= epos,acc= acc,vel= vel, cmdT=cmdT, filterT=filterT, gain=gain, id=cmdID)
            j[4] += dt
            count -= 1
            time.sleep(cmdT)
            rtn,pkg = robot.GetRobotRealTimeState()
            print(f"Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")

            if count < 50:
                robot.MotionQueueClear()
                print(f"After queue clear, Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")
                break
        robot.ServoMoveEnd()
    else:
        print(f"GetActualJointPosDegree errcode:{ret}")
    robot.CloseRPC()

关节扭矩控制开始
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJTStart(cmdType=0)``"
    "描述", "关节扭矩控制开始"
    "必选参数", "- ``cmdType``: 命令传输类型，0=XML-RPC，1=UDP透传"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关节扭矩控制
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJT(torque, interval, checkFlag=0, jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], cmdType=0)``"
    "描述", "关节扭矩控制"
    "必选参数", "- ``torque``:j1~j6关节扭矩，单位Nm
                - ``interval``:指令周期，单位s，范围[0.001~0.008]
                - ``checkFlag``:检测策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同时限制,默认0
                - ``jPowerLimit``:默认参数 jPowerLimit 关节最大功率限制(W)，默认[0.0,0.0,0.0,0.0,0.0,0.0]
                - ``jVelLimit``:关节最大速度(°/s)，默认[0.0,0.0,0.0,0.0,0.0,0.0]
                - ``cmdType``:命令传输类型，0=XML-RPC，1=UDP透传"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关节扭矩控制结束
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJTEnd(cmdType=0)``"
    "描述", "关节扭矩控制结束"
    "必选参数", "- ``cmdType``: 命令传输类型，0=XML-RPC，1=UDP透传"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

基于UDP通信的ServoJT、ServoJTStart、ServoJTEnd SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def TestServoJTUDP(self):
        # 设置回调
        def callback(src_type, count, cmd_id, data_len, content):
            print("回调函数: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        while True:
            # 初始化关节位置和外部轴位置
            j = [0, -90, 90, 0, 0, 0]
            epos = [0, 0, 0, 0]
            offset_pos = [0, 0, 0, 0, 0, 0]

            # 移动到初始位置
            robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
            time.sleep(3)
            # 开启拖动示教
            result=robot.DragTeachSwitch(1)
            print("DragTeachSwitch返回结果: {}".format(result))
            torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # 获取关节力矩
            ret, torques = robot.GetJointTorques(flag=1)
            if ret != 0:
                print(f"GetJointTorques errcode:{ret}")

            count = 100
            result = robot.ServoJTStart(cmdType=1)
            print("ServoJTStart返回结果: {}".format(result))
            # 正向力矩控制
            while True:
                torques[0] = 0.03
                result = robot.ServoJT(
                    torque=torques,
                    interval=0.001,
                    checkFlag=0,
                    jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    cmdType=1
                )
                print("返回结果: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] > 30:
                    break

            # 反向力矩控制
            while True:
                torques[0] = -0.03
                result = robot.ServoJT(
                        torque=torques,
                        interval=0.001,
                        checkFlag=0,
                        jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        cmdType=1
                    )
                print("返回结果: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] < 0:
                    break

            # 结束力矩控制并关闭拖动示教
            result = robot.ServoJTEnd(cmdType=1)
            print("ServoJTEnd返回结果: {}".format(result))
            result = robot.DragTeachSwitch(0)
            print("DragTeachSwitch返回结果: {}".format(result))

        robot.CloseRPC()
        return 0
    TestServoJTUDP(robot)

关节扭矩控制代码示例
++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    # torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error,torques = robot.GetJointTorques(1)
    robot.ServoJTStart()
    count = 100
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

笛卡尔空间伺服模式运动
++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoCart(mode, desc_pos, exaxis, pos_gain=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0], acc=0.0, vel=0.0, cmdT=0.008,filterT=0.0, gain=0.0)``"
    "描述", "笛卡尔空间伺服模式运动"
    "必选参数", "- ``mode``:[0]-绝对运动(基坐标系)，[1]-增量运动(基坐标系)，[2]-增量运动(工具坐标系)；
    - ``exaxis``:扩展轴位置；
    - ``desc_pos``:目标笛卡尔位置/目标笛卡尔位置增量；"
    "默认参数", "- ``pos_gain``:位姿增量比例系数，仅在增量运动下生效，范围 [0~1], 默认为 [1.0, 1.0, 1.0, 1.0, 1.0, 1.0];
    - ``acc``:加速度，范围 [0~100]，暂不开放，默认为 0.0;
    - ``vel``:速度，范围 [0~100]，暂不开放，默认为 0.0;
    - ``cmdT``:指令下发周期，单位s，建议范围[0.001~0.0016], 默认为0.008;
    - ``filterT``:滤波时间，单位 [s]，暂不开放， 默认为0.0;
    - ``gain``:目标位置的比例放大器，暂不开放， 默认为0.0;"
    "返回值", "错误码 成功-0  失败- errcode"

笛卡尔空间伺服模式运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    desc_pos_dt = [83.00800, 50.525000, 29.246, 179.629, -7.138, -166.975]
    exaxis = [100.0, 0.0, 0.0, 0.0]
    pos_gain = [0.0] * 6
    mode = 0
    vel = 0.0
    acc = 0.0
    cmdT = 0.001
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 5000
    robot.SetSpeed(20)
    while count:
        rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain)
        print(f"ServoCart rtn is {rtn}")
        count -= 1
        desc_pos_dt[0] += 0.01
        exaxis[0] += 0.01
    robot.CloseRPC()
    return 0

样条运动开始
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineStart()``"
    "描述", "样条运动开始"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

样条运动PTP
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplinePTP(joint_pos, tool, user, desc_pos = [0.0,0.0,0.0,0.0,0.0,0.0],  vel = 20.0,  acc = 100.0, ovl = 100.0)``"
    "描述", "样条运动PTP"
    "必选参数", "- ``joint_pos``:目标关节位置，单位[°]；
    - ``tool``:工具号，[0~14]；
    - ``user``:工件号，[0~14]；"
    "默认参数", "- ``desc_pos``:目标笛卡尔位姿，单位 [mm][°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用正运动学求解返回值;
    - ``vel``:速度，范围 [0~100]，默认为 20.0;
    - ``acc``:加速度，范围 [0~100]，默认为 100.0;
    - ``ovl``:速度缩放因子，[0~100]，默认为 100.0"
    "返回值", "错误码 成功-0  失败- errcode"

样条运动结束
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineEnd()``"
    "描述", "样条运动结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
样条运动代码示例
++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    joint_points = [
        [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256],  # j1
        [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255],  # j2
        [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260],  # j3
        [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]  # j4
    ]
    cart_points = [
        [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833],  # desc_pos1
        [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869],  # desc_pos2
        [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207],  # desc_pos3
        [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]  # desc_pos4
    ]
    offset_pos = [0] * 6 
    epos = [0] * 4 
    tool = user = 0
    vel = acc = ovl = 100.0 
    blendT = -1.0  
    flag = 0 
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=joint_points[0],tool=tool, user=user,vel=vel)
    print(f"MoveJ 错误码: {err1}")
    robot.SplineStart()
    robot.SplinePTP(joint_pos=joint_points[0],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[1],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[2],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[3],tool=tool, user=user)
    robot.SplineEnd()
    robot.CloseRPC()

新样条运动开始
+++++++++++++++++++
.. versionchanged:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplineStart(type,averageTime=2000)``"
    "描述", "新样条运动开始"
    "必选参数", "- ``type``:0-圆弧过渡，1-给定点位路径点"
    "默认参数", "- ``averageTime``:全局平均衔接时间（ms）默认为 2000"
    "返回值", "错误码 成功-0  失败- errcode"

新样条指令点
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplinePoint(desc_pos,tool,user,lastFlag,joint_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel = 0.0, acc = 0.0, ovl = 100.0 ,blendR = 0.0 )``"
    "描述", "新样条指令点"
    "必选参数", "- ``desc_pos``:目标笛卡尔位姿，单位 [mm][°];
    - ``tool``:工具号，[0~14]；
    - ``user``:工件号，[0~14]；
    - ``lastFlag``:是否为最后一个点，0-否，1-是;"
    "默认参数", "- ``joint_pos``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel``:速度，范围 [0~100]，暂不开放，默认为 0.0;；
    - ``acc``:加速度，范围 [0~100]，暂不开放，默认为 0.0;
    - ``ovl``:速度缩放因子，[0~100] 默认为 100.0;
    - ``blendR``: [0~1000]-平滑半径，单位 [mm] 默认0.0;"
    "返回值", "错误码 成功-0  失败- errcode"

新样条运动结束
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``NewSplineEnd()``"
    "描述", "新样条运动结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

新样条运动代码示例
++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260]
    j4 = [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]
    j5 = [-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    desc_pos4 = [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    print(f"movej errcode:{err1}")
    robot.NewSplineStart(1, 2000)
    robot.NewSplinePoint(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos3, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos5, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplineEnd()
    robot.CloseRPC()

机器人终止运动
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``StopMotion()``"
    "描述", "终止运动，使用终止运动需运动指令为非阻塞状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人暂停运动
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PauseMotion()``"
    "描述", "暂停运动，使用暂停运动需运动指令为非阻塞状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人恢复运动
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``ResumeMotion()``"
    "描述", "恢复运动，使用恢复运动需运动指令为非阻塞状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

运动暂停、恢复、停止代码示例
++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j1 =[-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j5 =[-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    rtn = robot.MoveJ(joint_pos=j5, tool=tool, user=user, vel=vel, blendT=1)
    time.sleep(1)
    robot.PauseMotion()
    time.sleep(1)
    robot.ResumeMotion()
    time.sleep(1)
    robot.StopMotion()
    time.sleep(1)
    robot.CloseRPC()

点位整体偏移开始
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetEnable(flag,offset_pos)``"
    "描述", "点位整体偏移开始"
    "必选参数", "- ``flag``:0-基坐标或工件坐标系下偏移， 2-工具坐标系下偏移；
    - ``offset_pos``:偏移量，单位[mm][°]。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

点位整体偏移结束
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetDisable()``"
    "描述", "点位整体偏移结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

点位偏移代码示例
+++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    time.sleep(1)
    robot.PointsOffsetEnable(flag=0, offset_pos=offset_pos1)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.PointsOffsetDisable()
    robot.CloseRPC()

控制箱运动AO开始
+++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveAOStart(AONum,maxTCPSpeed=1000,maxAOPercent=100,zeroZoneCmp=20)``"
    "描述", "控制箱运动AO开始"
    "必选参数", "- ``AONum``:控制箱AO编号"
    "默认参数", "
    - ``maxTCPSpeed``:最大TCP速度值[1-5000mm/s]，默认1000；
    - ``maxAOPercent``:最大TCP速度值对应的AO百分比，默认100%；
    - ``zeroZoneCmp``:死区补偿值AO百分比，整形，默认为20%，范围[0-100]。"
    "返回值", "错误码 成功-0  失败- errcode"

控制箱运动AO结束
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveAOStop()``"
    "描述", "控制箱运动AO结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

末端运动AO开始
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveToolAOStart(AONum,maxTCPSpeed=1000,maxAOPercent=100,zeroZoneCmp =20)``"
    "描述", "末端运动AO开始"
    "必选参数", "- ``AONum``:末端AO编号"
    "默认参数", "
    - ``maxTCPSpeed``:最大TCP速度值[1-5000mm/s]，默认1000；
    - ``maxAOPercent``:最大TCP速度值对应的AO百分比，默认100%；
    - ``zeroZoneCmp``:死区补偿值AO百分比，整形，默认为20%，范围[0-100]。"
    "返回值", "错误码 成功-0  失败- errcode"

末端运动AO结束
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveToolAOStop()``"
    "描述", "末端运动AO结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
      
AO飞拍代码示例
+++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 20.0
    acc = 20.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveAOStop()
    time.sleep(1)
    robot.MoveToolAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveToolAOStop()
    robot.CloseRPC()

开始Ptp运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningStart(maxAcc, maxJek)``"
    "描述", "开始Ptp运动FIR滤波"
    "必选参数", "- ``maxAcc``:最大加速度极值(deg/s2)
    - ``maxJek``:统一关节急动度极值(deg/s3)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关闭Ptp运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningEnd()``"
    "描述", "关闭Ptp运动FIR滤波"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

开始LIN、ARC运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningStart(maxAccLin,maxAccDeg,maxJerkLin,maxJerkDeg)``"
    "描述", "开始LIN、ARC运动FIR滤波"
    "必选参数", "- ``maxAccLin``:线加速度极值(mm/s2)
    - ``maxAccDeg``:角加速度极值(deg/s2)
    - ``maxJerkLin``:线加加速度极值(mm/s3)
    - ``maxJerkDeg``:角加加速度极值(deg/s3)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关闭LIN、ARC运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningEnd()``"
    "描述", "关闭LIN、ARC运动FIR滤波"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"   

FIR滤波代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    midjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    endjointPos = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    middescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    enddescPose = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.PtpFIRPlanningStart(1000.0, 1000.0)
    print(f"PtpFIRPlanningStart rtn is {rtn}")
    error = robot.MoveJ(joint_pos=startjointPos,tool= 0,user= 0,desc_pos=startdescPose,vel= 100,acc=100,ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    error = robot.MoveJ(joint_pos=endjointPos,tool= 0,user= 0,desc_pos=enddescPose,vel= 100,acc=100,ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    robot.PtpFIRPlanningEnd()
    print(f"PtpFIRPlanningEnd rtn is {rtn}")
    rtn = robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000)
    print(f"LinArcFIRPlanningStart rtn is {rtn}")
    error = robot.MoveL(desc_pos=startdescPose,tool= 0,user= 0, joint_pos=startjointPos,vel= 100,overSpeedStrategy=1,speedPercent=1)
    print(f"MoveL rtn is {rtn}")
    error = robot.MoveC(desc_pos_p=middescPose,tool_p= 0,user_p= 0, joint_pos_p=midjointPos,vel_p= 100,desc_pos_t=enddescPose,tool_t= 0,user_t= 0,joint_pos_t=endjointPos,vel_t= 100)
    print(f"MoveC rtn is {rtn}")
    robot.LinArcFIRPlanningEnd()
    print(f"LinArcFIRPlanningEnd rtn is {rtn}")
    robot.CloseRPC()

加速度平滑开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothStart(saveFlag_flag)``"
    "描述", "加速度平滑开启"
    "必选参数", "- ``saveFlag_flag``：是否断电保存"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

加速度平滑关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothEnd(saveFlag_flag)``"
    "描述", "加速度平滑关闭"
    "必选参数", "- ``saveFlag_flag``：是否断电保存"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

加速度平滑代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AccSmoothStart(0)
    print(f"AccSmoothStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos,tool= 0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos,tool= 0,user= 0,vel= 100)
    rtn = robot.AccSmoothEnd(0)
    print(f"AccSmoothEnd rtn is {rtn}")

设置机器指定姿态速度开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedStart(ratio)``"
    "描述", "指定姿态速度开启"
    "必选参数", "- ``ratio``:姿态速度百分比[0-300]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

指定姿态速度关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedEnd()``"
    "描述", "指定姿态速度关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

机器人指定姿态速度代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AngularSpeedStart(50)
    print(f"AngularSpeedStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos, tool=0,user= 0,vel= 100)
    rtn = robot.AngularSpeedEnd()
    print(f"AngularSpeedEnd rtn is {rtn}")
    robot.CloseRPC()

奇异位姿保护开启
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SingularAvoidStart(protectMode, minShoulderPos=100, minElbowPos=50, minWristPos=10)``"
    "描述", "开启奇异位姿保护"
    "必选参数", "
    - ``protectMode``：奇异位姿保护保护模式：0-关节模式；1-笛卡尔模式
    "
    "默认参数", "- ``minShoulderPos``：肩奇异调整范围(mm), 默认100.0
    - ``minElbowPos``：肘奇异调整范围(mm), 默认50.0
    - ``minWristPos``：腕奇异调整范围(°), 默认10.0"
    "返回值", "- 错误码 成功-0  失败- errcode"

奇异位姿保护关闭
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SingularAvoidEnd()``"
    "描述", "关闭奇异位姿保护"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

机器人奇异位姿保护代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SingularAvoidStart(2, 10, 5, 5)
    print(f"SingularAvoidStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos, tool=0,user= 0,vel= 100)
    rtn = robot.SingularAvoidEnd()
    print(f"SingularAvoidEnd rtn is {rtn}")
    robot.CloseRPC()

清空运动指令队列
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MotionQueueClear()``"
    "描述", "清空运动指令队列"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

清空运动指令队列
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToIntersectLineStart(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveType,mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],extAxisFlag=0,exaxisPos=[0.0,0.0,0.0,0.0],moveDirection=0,offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "清空运动指令队列"
    "必选参数", "
    - ``mainPoint``：主管6个示教点的笛卡尔位姿
    - ``piecePoint``：辅管6个示教点的笛卡尔位姿
    - ``tool``：工具坐标系编号
    - ``wobj``：工件坐标系编号
    - ``vel``：速度百分比
    - ``acc``：加速度百分比
    - ``ovl``：速度缩放因子
    - ``oacc``：加速度缩放因子
    - ``moveType``：运动类型; 0-PTP；1-LIN
    - ``mainExaxisPos``：主管6个示教点扩展轴位置,默认[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``：拼接管6个示教点扩展轴位置,默认[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``：是否启用扩展轴；0-不启用；1-启用
    - ``exaxisPos``：起点扩展轴位置[0.0,0.0,0.0,0.0]
    - ``moveDirection``：运动方向；0-顺时针；1-逆时针
    - ``offset``：偏移量
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

相贯线运动
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveIntersectLine(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveDirection,mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],extAxisFlag=0,exaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "相贯线运动"
    "必选参数", "
    - ``mainPoint``：主管6个示教点的笛卡尔位姿
    - ``piecePoint``：辅管6个示教点的笛卡尔位姿
    - ``tool``：工具坐标系编号
    - ``wobj``：工件坐标系编号
    - ``vel``：速度百分比
    - ``acc``：加速度百分比
    - ``ovl``：速度缩放因子
    - ``oacc``：加速度缩放因子
    - ``moveDirection``：运动方向；0-顺时针；1-逆时针
    - ``mainExaxisPos``：主管6个示教点扩展轴位置,默认[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``：拼接管6个示教点扩展轴位置,默认[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``：是否启用扩展轴；0-不启用；1-启用
    - ``exaxisPos``：起点扩展轴位置[0.0,0.0,0.0,0.0]
    - ``offset``：偏移量
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

机器人相贯线运动代码示例
+++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    mainPoint = [[0.0] * 6 for _ in range(6)]
    piecePoint = [[0.0] * 6 for _ in range(6)]
    mainExaxisPos = [[0.0] * 4 for _ in range(6)]
    pieceExaxisPos = [[0.0] * 4 for _ in range(6)]
    extAxisFlag = 1
    exaxisPos = [[0.0] * 4 for _ in range(4)]
    offset = [0.0, 2.0, 30.0, -2.0, 0.0, 0.0]
    mainPoint[0] = [490.004, -383.194, 402.735, -9.332, -1.528, 69.594]
    mainPoint[1] = [444.950, -407.117, 389.011, -5.546, -2.196, 65.279]
    mainPoint[2] = [445.168, -463.605, 355.759, -1.544, -10.886, 57.104]
    mainPoint[3] = [507.529, -485.385, 343.013, -0.786, -4.834, 61.799]
    mainPoint[4] = [554.390, -442.647, 367.701, -4.761, -10.181, 64.925]
    mainPoint[5] = [532.552, -394.003, 396.467, -13.732, -13.592, 67.411]
    mainExaxisPos[0] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[1] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[2] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[3] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[4] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[5] = [-29.996, 0.000, 0.000, 0.000]
    piecePoint[0] = [505.571, -192.408, 316.759, 38.098, 37.051, 139.447]
    piecePoint[1] = [533.837, -201.558, 332.340, 34.644, 42.339, 137.748]
    piecePoint[2] = [530.386, -225.085, 373.808, 35.431, 45.111, 137.560]
    piecePoint[3] = [485.646, -229.195, 383.778, 33.870, 45.173, 137.064]
    piecePoint[4] = [460.551, -212.161, 354.256, 28.856, 45.602, 135.930]
    piecePoint[5] = [474.217, -197.124, 324.611, 42.469, 41.133, 148.167]
    pieceExaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[1] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[2] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[3] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[4] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[5] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[1] = [-44.994, 90.000, 0.000, 0.000]
    exaxisPos[2] = [-59.992, 0.002, 0.000, 0.000]
    exaxisPos[3] = [-44.994, -89.997, 0.000, 0.000]
    tool = 2
    wobj = 0
    vel = 100.0
    acc = 100.0
    ovl = 12.0
    oacc = 12.0
    moveType = 1
    moveDirection = 1
    rtn = robot.MoveToIntersectLineStart(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag,exaxisPos=exaxisPos[0], tool=tool, wobj=wobj, vel=vel, acc=acc, ovl=ovl, oacc=oacc, moveType=moveType, moveDirection=moveDirection, offset=offset)
    print(f"MoveToIntersectLineStart rtn is {rtn}")
    rtn = robot.MoveIntersectLine(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag, exaxisPos=exaxisPos, tool=tool,wobj=wobj, vel=vel, acc=acc, ovl=5.0, oacc=5.0, moveDirection=moveDirection, offset=offset)
    print(f"MoveIntersectLine rtn is {rtn}")
    robot.CloseRPC()

原地空运动
+++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveStationary()``"
    "描述", "原地空运动"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"
 
原地空运动代码示例
+++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 0, 10, 100)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    rtn = robot.MoveStationary()
    print(f"MoveStationary rtn is {rtn}")
    rtn = robot.LaserSensorRecord1(0, 10)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    robot.CloseRPC()
    return 0

定点摆动开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OriginPointWeaveStart(weaveNum, mode, refPoint, weaveTime)``"
    "描述", "定点摆动开始"
    "必选参数", "
    - ``weaveNum``:摆动编号[0-7]
    - ``mode``:0-工具坐标系；1-参考点
    - ``refPoint``:参考点笛卡尔坐标[x,y,z,a,b,c]
    - ``weaveTime``:摆动时间[s]
    - "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

定点摆动结束
+++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OriginPointWeaveEnd()``"
    "描述", "定点摆动结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

定点摆动的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')

    def TestOriginPointWeave(self):
        time.sleep(2)
        # 初始化关节位置、外部轴和偏移
        j = [39.886, -98.580, -124.032, -47.393, 90.000, 40.842]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        # 参考点位置 [x, y, z, rx, ry, rz]
        refPoint = [400.021, 300.022, 299.996, 179.997, -0.003, -90.956]

        # 移动到起始位置
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 第一次摆动：绝对坐标系（tool=0），模式0
        robot.OriginPointWeaveStart(0, 0, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        time.sleep(2)

        # 再次移动到起始位置
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 第二次摆动：绝对坐标系（tool=0），模式1
        robot.OriginPointWeaveStart(0, 1, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        # 关闭连接
        robot.CloseRPC()
        time.sleep(1)

    TestOriginPointWeave(robot)