机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置工具参考点-六点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolPoint(point_num)``"
    "描述", "设置工具参考点-六点法"
    "必选参数", "- ``point_num``：点编号,范围[1~6]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算工具坐标系-六点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTool()``"
    "描述", "计算工具坐标系-六点法（设置完六个工具参考点后再进行计算）"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

设置工具参考点-四点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTcp4RefPoint(point_num)``"
    "描述", "设置工具参考点-四点法"
    "必选参数", "``point_num``：点编号,范围[1~4]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

计算工具坐标系-四点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTcp4()``"
    "描述", "计算工具坐标系-四点法（设置完四个工具参考点后再进行计算）"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

根据点位信息计算工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeToolCoordWithPoints(method, pos)``"
    "描述", "根据点位信息计算工具坐标系"
    "必选参数", "- ``method``：计算方法；0-四点法；1-六点法
    - ``pos``：关节位置组，四点法时数组长度为4个，六点法时数组长度为6个"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``tcp_offset=[x,y,z,rx,ry,rz]``：根据点位信息计算得到的工具坐标系，单位 [mm][°]"

设置工具坐标系
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolCoord(id,t_coord,type,install,toolID,loadNum)``"
    "描述", "设置工具坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[1~15]；
    - ``t_coord``:工具中心点相对末端法兰中心位姿，单位[mm][°]；
    - ``type``:0-工具坐标系，1-传感器坐标系；
    - ``install``:安装位置，0-机器人末端，1-机器人外部
    - ``toolID``:工具ID
    - ``loadNum``:负载编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置工具坐标系列表
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolList(id,t_coord ,type, install, loadNum)``"
    "描述", "设置工具坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[1~15]；
    - ``t_coord``:[x,y,z,rx,ry,rz] 工具中心点相对末端法兰中心位姿，单位[mm][°]；
    - ``type``:0-工具坐标系，1-传感器坐标系；
    - ``install``:安装位置，0-机器人末端，1-机器人外部
    - ``loadNum``:负载编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取当前工具坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTCPOffset(flag=1)``"
    "描述", "获取当前工具坐标系"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: 当前工具坐标系相对位姿，单位[mm][°]"

机器人工具坐标系操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posJ = [p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint]
    rtn,coordRtn = robot.ComputeToolCoordWithPoints(1, posJ)
    print(f"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(4)
    robot.MoveJ(joint_pos=p5Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(5)
    robot.MoveJ(joint_pos=p6Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(6)
    rtn,coordRtn = robot.ComputeTool()
    print(f"6 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolList(1, coordRtn, 0, 0, 0)
    robot.MoveJ(joint_pos=p1Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(4)
    rtn,coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0)
    rtn,getCoord = robot.GetTCPOffset(0)
    print(f"GetTCPOffset    {rtn}  coord is {getCoord[0]} {getCoord[1]} {getCoord[2]} {getCoord[3]} {getCoord[4]} {getCoord[5]}")
    robot.CloseRPC()

设置外部工具参考点-六点法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExTCPPoint(point_num)``"
    "描述", "设置外部工具参考点-三点法"
    "必选参数", "- ``point_num``：点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

计算外部工具坐标系-六点法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeExTCF(point_num)``"
    "描述", "计算外部工具坐标系-三点法（设置完三个参考点后再进行计算）"
    "必选参数", "``point_num``：点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``etcp=[x,y,z,rx,ry,rz]``：外部工具坐标系"

设置外部工具坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolCoord(id,etcp,etool)``"
    "描述", "设置外部工具坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``etcp``:外部工具坐标系，单位[mm][°]；
    - ``etool``:末端工具坐标系，单位[mm][°]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置外部工具坐标系列表
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolList(id,etcp ,etool)``"
    "描述", "设置外部工具坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``etcp``:外部工具坐标系，单位[mm][°]；
    - ``etool``:末端工具坐标系，单位[mm][°]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

机器人外部工具坐标系操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    robot.MoveJ(joint_pos=p1Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(3)
    rtn,coordRtn = robot.ComputeExTCF()
    print(f"ComputeExTCF {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetExToolCoord(1, coordRtn, offdese)
    robot.SetExToolList(1, coordRtn, offdese)
    robot.CloseRPC()

设置工件参考点-三点法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoordPoint(point_num)``"
    "描述", "设置工件参考点-三点法"
    "必选参数", "``point_num``:点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

计算工件坐标系-三点法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoord(method, refFrame)``"
    "描述", "计算工件坐标系-三点法（三个参考点设置完成后再进行计算）;"
    "必选参数", "- ``method``：计算方式0：原点-x轴-z轴，1：原点-x轴-xy平面
    - ``refFrame``：参考坐标系"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``wobj_pose=[x,y,z,rx,ry,rz]``：工件坐标系"

设置工件坐标系
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoord(id, coord, refFrame)``"
    "描述", "设置工件坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``coord``:工件坐标系相对于末端法兰中心位姿，单位 [mm][°]
    - ``refFrame``:参考坐标系"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置工件坐标系列表
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjList(id, coord, refFrame)``"
    "描述", "设置工件坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``coord``:工件坐标系相对于末端法兰中心位姿，单位 [mm][°]
    - ``refFrame``:参考坐标系"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

根据点位信息计算工件坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoordWithPoints(method, pos, refFrame)``"
    "描述", "根据点位信息计算工件坐标系"
    "必选参数", "- ``method``：计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
    - ``pos``：三个TCP位置组
    - ``refFrame``：参考坐标系"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``wobj_offset=[x,y,z,rx,ry,rz]``：根据点位信息计算得到的工件坐标系，单位 [mm][°]"

获取当前工件坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWObjOffset(flag=1)``"
    "描述", "获取当前工件坐标系"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞，默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: 当前工件坐标系相对位姿，单位[mm][°]"

机器人工件坐标系操作代码示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    rtn,coordRtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0)
    print(f"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(3)
    rtn,coordRtn = robot.ComputeWObjCoord(1, 0)
    print(f"ComputeWObjCoord   {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetWObjCoord(1, coordRtn, 0)
    robot.SetWObjList(1, coordRtn, 0)
    rtn,getWobjDesc = robot.GetWObjOffset(0)
    print(f"GetWObjOffset    {rtn}  coord is {getWobjDesc[0]} {getWobjDesc[1]} {getWobjDesc[2]} {getWobjDesc[3]} {getWobjDesc[4]} {getWobjDesc[5]}")
    robot.CloseRPC()

设置全局速度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSpeed(vel)``"
    "描述", "设置全局速度"
    "必选参数", "- ``vel``:速度百分比，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置机器人加速度
+++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOaccScale(acc)``"
    "描述", "设置机器人加速度"
    "必选参数", "- ``acc``:机器人加速度百分比"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取默认速度
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDefaultTransVel()``"
    "描述", "获取默认速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``vel``: 默认速度，单位 [mm/s]"

设置末端负载重量
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadWeight(loadNum, weight)``"
    "描述", "设置末端负载重量,错误负载重量设置可能会导致拖动模式下机器人失控"
    "必选参数", "- ``loadNum``:负载编号
    - ``weight``:单位[kg]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置末端负载质心坐标
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadCoord(x,y,z,loadNum = 0)``"
    "描述", "设置末端负载质心坐标,错误负载质心设置可能会导致拖动模式下机器人失控"
    "必选参数", "- ``x``: 质心坐标，单位[mm]
    - ``y``: 质心坐标，单位[mm]
    - ``z``: 质心坐标，单位[mm]"
    "默认参数", "- ``loadNum``: 负载编号，默认0"
    "返回值", "错误码 成功-0  失败- errcode "

获取当前负载的重量
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayload(flag=1)``"
    "描述", "获取当前负载的质量"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weight``：当前负载重量，单位 [kg]"

获取当前负载的质心
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayloadCog(flag=1)``"
    "描述", "获取当前负载的质心"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``cog=[x,y,z]``: 当前质心坐标，单位 [mm]"

设置机器人安装方式-固定安装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallPos(method)``"
    "描述", "设置机器人安装方式-固定安装,错误安装方式设置会导致拖动模式下机器人失控"
    "必选参数", "- ``method``:0-平装，1-侧装，2-挂装"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置机器人安装角度-自由安装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallAngle(yangle,zangle)``"
    "描述", "设置机器人安装角度-自由安装,错误安装角度设置会导致拖动模式下机器人失控"
    "必选参数", "- ``yangle``：倾斜角
    - ``zangle``：旋转角"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取机器人安装角度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotInstallAngle()``"
    "描述", "获取机器人安装角度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[yangle,zangle]``：yangle-倾斜角,zangle-旋转角"

设置系统变量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysVarValue(id,value)``"
    "描述", "设置系统变量"
    "必选参数", "- ``id``：变量编号，范围[1~20];
    - ``value``：变量值"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取系统变量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSysVarValue(id)``"
    "描述", "获取系统变量值"
    "必选参数", "- ``id``：系统变量编号，范围[1~20]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``var_value``：系统变量值"

机器人常用设置代码示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1, 100):
        robot.SetSpeed(i)
        robot.SetOaccScale(i)
        time.sleep(0.03)
    error,defaultVel = robot.GetDefaultTransVel()
    print(f"GetDefaultTransVel is {defaultVel}")
    for i in range(1, 21):
        robot.SetSysVarValue(i, i + 0.5)
        time.sleep(0.1)
    for i in range(1, 21):
        value = robot.GetSysVarValue(i)
        print(f"sys value {i} is: {value}")
        time.sleep(0.1)
    robot.SetLoadWeight(0, 2.5)
    robot.SetLoadCoord(3.0,4.0,5.0)
    time.sleep(1)
    error,getLoad = robot.GetTargetPayload(0)
    error,getLoadTran = robot.GetTargetPayloadCog(0)
    print(f"get load is {getLoad}; get load cog is {getLoadTran[0]} {getLoadTran[1]} {getLoadTran[2]}")
    robot.SetRobotInstallPos(0)
    robot.SetRobotInstallAngle(15.0, 25.0)
    error,[anglex, angley] = robot.GetRobotInstallAngle()
    print(f"GetRobotInstallAngle x: {anglex}; y: {angley}")
    robot.CloseRPC()

关节摩擦力补偿开关
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FrictionCompensationOnOff(state)``"
    "描述", "关节摩擦力补偿开关"
    "必选参数", "- ``state``：0-关，1-开"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_level(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-正装"
    "必选参数", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_wall(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-侧装"
    "必选参数", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_ceiling(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-倒装"
    "必选参数", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置关节摩擦力补偿系数-自由安装
+++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_freedom(coeff)``"
    "描述", "设置关节摩擦力补偿系数-自由安装"
    "必选参数", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人设置关节摩擦力补偿代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    lcoeff = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    wcoeff = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
    ccoeff = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    fcoeff = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    rtn = robot.FrictionCompensationOnOff(1)
    print(f"FrictionCompensationOnOff rtn is {rtn}")
    rtn = robot.SetFrictionValue_level(lcoeff)
    print(f"SetFrictionValue_level rtn is {rtn}")
    rtn = robot.SetFrictionValue_wall(wcoeff)
    print(f"SetFrictionValue_wall rtn is {rtn}")
    rtn = robot.SetFrictionValue_ceiling(ccoeff)
    print(f"SetFrictionValue_ceiling rtn is {rtn}")
    rtn = robot.SetFrictionValue_freedom(fcoeff)
    print(f"SetFrictionValue_freedom rtn is {rtn}")
    robot.CloseRPC()

查询机器人错误码
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotErrorCode()``"
    "描述", "查询机器人错误码"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[maincode subcode]``：机器人错误码，maincode-主错误码，subcode-子错误码"

错误状态清除
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ResetAllError()``"
    "描述", "错误状态清除，只能清除可复位的错误"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人故障状态获取及清除错误代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    robot.MoveJ(joint_pos=p1Joint, tool=5, user=2, vel=50)
    time.sleep(1)
    error,[maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    time.sleep(1)
    robot.ResetAllError()
    time.sleep(1)
    error,[maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    robot.CloseRPC()

设置宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWideBoxTempFanMonitorParam(enable, period)``"
    "描述", "设置宽电压控制箱温度及风扇转速监控参数"
    "必选参数", "- ``enable``：0-不使能监测；1-使能监测
    - ``period``：监测周期(s),范围1-100"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWideBoxTempFanMonitorParam()``"
    "描述", "获取宽电压控制箱温度及风扇转速监控参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``enable``：0-不使能监测；1-使能监测
    - ``period``：监测周期(s),范围1-100"

宽电压控制箱温度和风扇电流状态获取代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.SetWideBoxTempFanMonitorParam(1, 2)
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    rtn = robot.SetWideBoxTempFanMonitorParam(0, 2)
    print(f"SetWideBoxTempFanMonitorParam rtn is:{rtn}")
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    robot.CloseRPC()

设置焦点标定点
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFocusCalibPoint(pointNum, point)``"
    "描述", "设置焦点标定点"
    "必选参数", "- ``pointNum``：焦点标定点编号 1-8
    - ``point``：标定点坐标"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算焦点标定结果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFocusCalib(pointNum)``"
    "描述", "计算焦点标定结果"
    "必选参数", "- ``pointNum``：标定点个数"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``resultPos``：标定结果XYZ
    - ``accuracy``：标定精度误差"

开启焦点跟随
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FocusStart(kp=50.0, kpredic=19.0, aMax=1440, vMax=180, type=0)``"
    "描述", "开启焦点跟随"
    "必选参数", "无"
    "默认参数", "- ``kp``：比例参数，默认50.0
    - ``kpredic``：前馈参数，默认19.0
    - ``aMax``：最大角加速度限制，默认1440°/s^2
    - ``vMax``：最大角速度限制，默认180°/s
    - ``type``：锁定X轴指向(0-参考输入矢量；1-水平；2-垂直)，默认0"
    "返回值", "错误码 成功-0  失败- errcode"

停止焦点跟随
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FocusEnd()``"
    "描述", "停止焦点跟随"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焦点坐标
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFocusPosition(pos)``"
    "描述", "设置焦点坐标"
    "必选参数", "- ``pos``：焦点坐标XYZ"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人焦点跟随代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 100, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(4)
    rtn,coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool {rtn} coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} "
          f"{coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0)
    error, p1Desc = robot.GetForwardKin(p1Joint)
    error, p2Desc = robot.GetForwardKin(p2Joint)
    error, p3Desc = robot.GetForwardKin(p3Joint)
    robot.SetFocusCalibPoint(1, p1Desc)
    robot.SetFocusCalibPoint(2, p2Desc)
    robot.SetFocusCalibPoint(3, p3Desc)
    rtn, resultPos, accuracy = robot.ComputeFocusCalib(pointNum=3)
    print(f"ComputeFocusCalib coord is {rtn} {resultPos[0]} {resultPos[1]} {resultPos[2]} accuracy is {accuracy}")
    rtn = robot.SetFocusPosition(resultPos)
    error, p5Desc = robot.GetForwardKin(p5Joint)
    error, p6Desc = robot.GetForwardKin(p6Joint)
    robot.MoveL(desc_pos=p5Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.FocusStart(50, 19, 710, 90, 0)
    robot.MoveL(desc_pos=p5Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.FocusEnd()
    robot.CloseRPC()

关节扭矩传感器灵敏度标定功能开启
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityEnable(status)``"
    "描述", "关节扭矩传感器灵敏度标定功能开启"
    "必选参数", "- ``status``：0-关闭；1-开启"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

关节扭矩传感器灵敏度数据采集
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityCollect()``"
    "描述", "关节扭矩传感器灵敏度数据采集"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取关节扭矩传感器灵敏度标定结果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityCalibration()``"
    "描述", "获取关节扭矩传感器灵敏度标定结果"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``calibResult``：j1~j6关节灵敏度[0-1]
    - ``linearityn``：j1~j6关节线性度[0-1]"

获取关节扭矩传感器迟滞误差
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointHysteresisError()``"
    "描述", "获取关节扭矩传感器迟滞误差"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``hysteresisError``：j1~j6关节迟滞误差"

获取关节扭矩传感器重复精度
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointRepeatability()``"
    "描述", "获取关节扭矩传感器重复精度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``repeatability``：j1~j6关节重复精度"

设置关节力传感器参数
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAdmittanceParams(M, B, K, threshold, sensitivity, setZeroFlag)``"
    "描述", "设置关节力传感器参数"
    "必选参数", "
    - ``M``：J1-J6质量系数[0.001 ~ 10]
    - ``B``：J1-J6阻尼系数[0.001 ~ 10]
    - ``K``：J1-J6刚度系数[0.001 ~ 10]
    - ``threshold``：力控制阈值，Nm
    - ``sensitivity``：灵敏度,Nm/V,[0 ~ 10]
    - ``setZeroFlag``：功能开启标志位；0-关闭；1-开启；2-位置1记录零点；3-位置2记录零点"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

关节扭矩传感器灵敏度自动标定代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.JointSensitivityEnable(0)
    rtn = robot.JointSensitivityEnable(1)
    print(f"JointSensitivityEnable rtn is {rtn}")
    curJPos = [0.0] * 6
    rtn, curJPos = robot.GetActualJointPosDegree(0)
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    jointPos1 = [curJPos[0], 0.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos1 = [0.0] * 6
    rtn, descPos1 = robot.GetForwardKin(jointPos1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 1 rtn is {rtn}")
    time.sleep(0.1)
    jointPos2 = [curJPos[0], -30.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos2 = [0.0] * 6
    rtn, descPos2 = robot.GetForwardKin(jointPos2)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 2 rtn is {rtn}")
    time.sleep(0.1)
    jointPos3 = [curJPos[0], -60.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos3 = [0.0] * 6
    rtn, descPos3 = robot.GetForwardKin(jointPos3)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 3 rtn is {rtn}")
    time.sleep(0.1)
    jointPos4 = [curJPos[0], -90.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos4 = [0.0] * 6
    rtn, descPos4 = robot.GetForwardKin(jointPos4)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 4 rtn is {rtn}")
    time.sleep(0.1)
    jointPos5 = [curJPos[0], -120.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos5 = [0.0] * 6
    rtn, descPos5 = robot.GetForwardKin(jointPos5)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 5 rtn is {rtn}")
    time.sleep(0.1)
    jointPos6 = [curJPos[0], -150.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos6 = [0.0] * 6
    rtn, descPos6 = robot.GetForwardKin(jointPos6)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 6 rtn is {rtn}")
    time.sleep(0.1)
    jointPos7 = [curJPos[0], -180.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos7 = [0.0] * 6
    rtn, descPos7 = robot.GetForwardKin(jointPos7)
    robot.MoveJ(joint_pos=jointPos7, desc_pos=descPos7, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 7 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 8 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 9 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 10 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 11 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 12 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 13 rtn is {rtn}")
    time.sleep(0.1)
    calibResult = [0.0] * 6
    linearity = [0.0] * 6
    rtn,calibResult, linearity = robot.JointSensitivityCalibration()
    print(f"JointSensitivityCalibration rtn is {rtn}")
    rtn = robot.JointSensitivityEnable(0)
    print(f"JointSensitivityEnable rtn is {rtn}")
    print(f"jointSensor Calib result is {calibResult[0]},{calibResult[1]},{calibResult[2]},{calibResult[3]},{calibResult[4]},{calibResult[5]}")
    print( f"jointSensor linearity is {linearity[0]},{linearity[1]},{linearity[2]},{linearity[3]},{linearity[4]},{linearity[5]}")
    hysteresisError = [0.0] * 6
    rtn,hysteresisError = robot.JointHysteresisError()
    print(f"JointHysteresisError result is {hysteresisError[0]},{hysteresisError[1]},{hysteresisError[2]},{hysteresisError[3]},{hysteresisError[4]},{hysteresisError[5]}")
    repeatability = [0.0] * 6
    rtn,repeatability = robot.JointRepeatability()
    print(f"JointRepeatability result is {repeatability[0]},{repeatability[1]},{repeatability[2]},{repeatability[3]},{repeatability[4]},{repeatability[5]}")
    M = [1.0] * 6
    B = [1.0] * 6
    K = [0.0] * 6
    threshold = [1.0] * 6
    setZeroFlag = 1
    rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag)
    print(f"SetAdmittanceParams rtn is {rtn}")
    robot.CloseRPC()

获取机器人8个从站端口错误帧数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlavePortErrCounter()``"
    "描述", "获取机器人8个从站端口错误帧数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``inRecvErr``：输入接收错误帧数
    - ``inCRCErr``：输入CRC错误帧数
    - ``inTransmitErr``：输入转发错误帧数
    - ``inLinkErr``：输入链接错误帧数
    - ``outRecvErr``：输出接收错误帧数
    - ``outCRCErr``：输出CRC错误帧数
    - ``outTransmitErr``：输出转发错误帧数
    - ``outLinkErr``：输出链接错误帧数"

从站端口错误帧清零
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityEnable(slaveID)``"
    "描述", "从站端口错误帧清零"
    "必选参数", "- ``slaveID``：从站编号0~7"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取从站端口错误帧代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    inRecvErr = [0] * 8
    inCRCErr = [0] * 8
    inTransmitErr = [0] * 8
    inLinkErr = [0] * 8
    outRecvErr = [0] * 8
    outCRCErr = [0] * 8
    outTransmitErr = [0] * 8
    outLinkErr = [0] * 8
    rtn,inRecvErr, inCRCErr, inTransmitErr, inLinkErr, outRecvErr, outCRCErr, outTransmitErr, outLinkErr = robot.GetSlavePortErrCounter()
    for i in range(8):
        if inRecvErr[i] != 0:
            print(f"inRecvErr {i} is {inRecvErr[i]}")
        if inCRCErr[i] != 0:
            print(f"inCRCErr {i} is {inCRCErr[i]}")
        if inTransmitErr[i] != 0:
            print(f"inTransmitErr {i} is {inTransmitErr[i]}")
        if inLinkErr[i] != 0:
            print(f"inLinkErr {i} is {inLinkErr[i]}")
        if outRecvErr[i] != 0:
            print(f"outRecvErr {i} is {outRecvErr[i]}")
        if outCRCErr[i] != 0:
            print(f"outCRCErr {i} is {outCRCErr[i]}")
        if outTransmitErr[i] != 0:
            print(f"outTransmitErr {i} is {outTransmitErr[i]}")
        if outLinkErr[i] != 0:
            print(f"outLinkErr {i} is {outLinkErr[i]}")
    print("others has no err!")
    for i in range(8):
        robot.SlavePortErrCounterClear(i)
    robot.CloseRPC()

设置各轴速度前馈系数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetVelFeedForwardRatio(radio)``"
    "描述", "设置各轴速度前馈系数"
    "必选参数", "- ``radio``：各轴速度前馈系数"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取各轴速度前馈系数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetVelFeedForwardRatio()``"
    "描述", "获取各轴速度前馈系数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``radio``：各轴速度前馈系数"

机器人速度前馈系数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    setRadio = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    robot.SetVelFeedForwardRatio(setRadio)
    getRadio = [0.0] * 6
    rtn,getRadio = robot.GetVelFeedForwardRatio()
    print(f"{getRadio[0]},{getRadio[1]},{getRadio[2]},{getRadio[3]},{getRadio[4]},{getRadio[5]}")
    robot.CloseRPC()

光电传感器TCP标定-计算工具RPY
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TCPComputeRPY(Btool, Etool, sensor, radius, dz)``"
    "描述", "光电传感器TCP标定-计算工具RPY"
    "必选参数", "
    - ``Btool``：机器人笛卡尔位置
    - ``Etool``：当前工具坐标系数值
    - ``Btsenserool``：当前传感器坐标系数值(暂未开放)
    - ``radius``：圆周运动半径mm(暂未开放)
    - ``dz``：沿基座标系z轴负方向运动距离；当dz = 10000时，函数直接返回工具RPY"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

光电传感器TCP标定-计算工具XYZ
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TCPComputeXYZ(select, originDirection, pos1, pos2, pos3, pos4)``"
    "描述", "光电传感器TCP标定-计算工具XYZ"
    "必选参数", "
    - ``select``：0-计算工具TCP；1-计算传感器原点；2-计算传感器姿态；3-直接返回工具TCP；4-记录当前工件坐标系和工具坐标系
    - ``originDirection``：0-X方向；1-Y方向；2-Z方向
    - ``pos1``：机器人笛卡尔位置1
    - ``pos2``：机器人笛卡尔位置2
    - ``pos3``：机器人笛卡尔位置3
    - ``pos4``：机器人笛卡尔位置4"
    "默认参数", "无"
    "返回值", "
    - 错误码 成功-0  失败- errcode
    - 返回值（调用成功返回） TCP 工具XYZ数值"

光电传感器TCP标定-开始记录末端法兰中心位置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TCPRecordFlangePosStart()``"
    "描述", "光电传感器TCP标定-开始记录末端法兰中心位置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

光电传感器TCP标定-停止记录末端法兰中心位置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TCPRecordFlangePosEnd()``"
    "描述", "光电传感器TCP标定-停止记录末端法兰中心位置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

光电传感器TCP标定-获取末端工具中心点位置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TCPGetRecordFlangePos()``"
    "描述", "光电传感器TCP标定-获取末端工具中心点位置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "
    - 错误码 成功-0  失败- errcode
    - 返回值（调用成功返回） TCP 工具中心点位置(x,y,z)"

光电传感器TCP标定
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PhotoelectricSensorTCPCalibration(luaPath, offsetX)``"
    "描述", "光电传感器TCP标定"
    "必选参数", "
    - ``luaPath``：自动标定lua程序路径：QX版本机器人-'/fruser/FR_CalibrateTheToolTcp.lua';LA版本机器人-'/usr/local/etc/controller/lua/FR_CalibrateTheToolTcp.lua'
    - ``offsetX``：示教点偏移(x,y,z)mm"
    "默认参数", "无"
    "返回值", "
    - 错误码 成功-0  失败- errcode
    - 返回值（调用成功返回） TCP 工具XYZ数值"

光电传感器TCP标定代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    offset = [10.0, 10.0, 3.0]
    TCP = [0.0] * 6
    rtn, TCP = robot.PhotoelectricSensorTCPCalibration("/fruser/FR_CalibrateTheToolTcp.lua", offset)
    print(f"PhotoelectricSensorTCPCalibration rtn is {rtn},{TCP[0]},{TCP[1]},{TCP[2]},{TCP[3]},{TCP[4]},{TCP[5]}")
    robot.CloseRPC()
    return 0