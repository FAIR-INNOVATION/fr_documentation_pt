机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RPC(ip)``"
    "描述", "实例化一个机器人对象"
    "必选参数", "- ``ip``：机器人的IP地址，默认出厂IP为“192.168.58.2”"
    "默认参数", "无"
    "返回值", "- 成功：返回一个机器人对象
    - 失败：创建的对象会被销毁"

关闭RPC连接
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CloseRPC()``"
    "描述", "关闭RPC连接"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "无"

查询SDK版本号
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKVersion()``"
    "描述", "查询SDK版本号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode
    - ``sdk``：SDK版本号、控制器版本号"

获取控制器IP
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetControllerIP()``"
    "描述", "查询控制器IP"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ip``：控制器IP"

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DragTeachSwitch(state)``"
    "描述", "控制机器人进入或退出拖动示教模式"
    "必选参数", "- ``state``：1-进入拖动示教模式，0-退出拖动示教模式"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

查询机器人是否处于拖动模式
++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``IsInDragTeach()``"
    "描述", "查询机器人是否处于拖动示教模式"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：0-非拖动示教模式，1-拖动示教模式"

控制机器人上使能或下使能
++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotEnable(state)``"
    "描述", "控制机器人上使能或下使能"
    "必选参数", "- ``state``：1-上使能，0-下使能"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "


控制机器人手自动模式切换
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Mode(state)``"
    "描述", "控制机器人手自动模式切换"
    "必选参数", "- ``state``：0-自动模式，1-手动模式"
    "默认参数", "无"
    "返回值", "错误码  成功-0  失败- errcode"

关闭机器人操作系统
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ShutDownRobotOS()``"
    "描述", "关闭机器人操作系统"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

初始化日志参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoggerInit(output_model=1, file_path="", file_num=5)``"
    "描述", "初始化日志参数"
    "必选参数", "无"
    "默认参数", "- ``output_model``：输出模式，0-直接输出；1-缓冲输出；2-异步输出，默认1
    - ``file_path``：文件保存路径+名称，名称必须是xxx.log的形式，比如/home/fr/linux/fairino.log。默认执行程序所在路径，默认名称为：fairino_year+month+data.log(如:fairino_2024_03_13.log);
    - ``file_num``：滚动存储的文件数量，1~20个，默认值为5。单个文件上限50M;"
    "返回值", "错误码 成功-0  失败- errcode"

设置日志过滤等级
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoggerLevel(lvl=1)``"
    "描述", "设置日志过滤等级"
    "必选参数", "无"
    "默认参数", "- ``lvl``：过滤等级值，值越小输出日志越少, 1-error, 2-warnning, 3-inform, 4-debug,默认值是1"
    "返回值", "错误码 成功-0  失败- errcode"

机器人基础控制代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error,version = robot.GetSDKVersion()
    print(f"SDK version: {version}")
    error,ip = robot.GetControllerIP()
    print(f"controller ip: {ip}")
    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(state=1)
    time.sleep(1)
    error,state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.DragTeachSwitch(state=0)
    time.sleep(1)
    error,state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.RobotEnable(0)
    time.sleep(3)
    robot.RobotEnable(1)
    robot.Mode(0)
    time.sleep(1)
    robot.Mode(1)
    robot.CloseRPC()

获取机器人软件版本
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareVersion()``"
    "描述", "获取机器人软件版本"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``robotModel``：机器人模型
    - ``webVersion``：web版本
    - ``controllerVersion``：控制器版本"

获取机器人硬件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveHardVersion()``"
    "描述", "获取机器人硬件版本信息"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

获取机器人固件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveFirmVersion()``"
    "描述", "获取机器人固件版本信息"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

获取机器人软固件版本代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn,robotModel, webversion, controllerVersion = robot.GetSoftwareVersion()
    print(f"Getsoftwareversion rtn is: {rtn}")
    print(f"robotmodel is: {robotModel}, webversion is: {webversion}, controllerVersion is: {controllerVersion}\n")
    rtn,ctrlBoxBoardversion, driver1version, driver2version,driver3version, driver4version, driver5version,driver6version, endBoardversion = robot.GetHardwareversion()
    print(f"GetHardwareversion rtn is: {rtn}")
    print(f"GetHardwareversion get hardware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    rtn,ctrlBoxBoardversion, driver1version, driver2version,driver3version, driver4version, driver5version,driver6version, endBoardversion = robot.GetFirmwareVersion()
    print(f"GetFirmwareversion rtn is: {rtn}")
    print(f"GetFirmwareversion get firmware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    robot.CloseRPC()
