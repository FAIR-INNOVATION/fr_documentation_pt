机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDO(id, status, smooth=0, block=0)``"
    "描述", "设置控制箱数字量输出"
    "必选参数", "-  ``id``:io编号，范围[0~15]；
    - ``status``:0-关，1-开；"
    "默认参数", "- ``smooth``:0-不平滑，1-平滑 默认0;
    - ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置工具数字量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDO (id, status, smooth=0, block=0)``"
    "描述", "设置工具数字量输出"
    "必选参数", "-  ``id``:io编号，范围[0~1]；
    - ``status``:0-关，1-开；"
    "默认参数", "- ``smooth``:0-不平滑，1-平滑；
    - ``block``:0-阻塞，1-非阻塞。"
    "返回值", "错误码 成功-0  失败- errcode"

设置控制箱模拟量输出
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAO(id,value,block=0)``"
    "描述", "设置控制箱模拟量输出"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；"
    "默认参数", "- ``block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置工具模拟量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolAO(id,value,block=0)``"
    "描述", "设置工具模拟量输出"
    "必选参数", "- ``id``:io编号，范围[0]；
    - ``value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；"
    "默认参数", "- ``block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置数字量、模拟量输出代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0  
    block = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3) 
    status = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1) 
    status = 0 
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    robot.CloseRPC()

获取控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDI(id, block=0)``"
    "描述", "获取控制箱数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~15]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``di``: 0-低电平，1-高电平"

获取工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDI(id, block=0)``"
    "描述", "获取工具数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode
    - ``di``: 0-低电平，1-高电平"

获取控制箱模拟量输入
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAI(id, block = 0)``"
    "描述", "获取控制箱模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0 "
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``value``: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

获取工具模拟量输入
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolAI(id, block = 0)``"
    "描述", "获取末端模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``value``: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

获取机器人末端点记录按钮状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxlePointRecordBtnState()``"
    "描述", "获取机器人末端点记录按钮状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``buttonstatus``: 按钮状态，0-按下，1-松开"

获取机器人末端DO输出状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDO()``"
    "描述", "获取机器人末端DO输出状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``do_state``: DO输出状态，do0~do1对应bit1~bit2,从bit0开始"

获取机器人控制器DO输出状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDO()``"
    "描述", "获取机器人控制器DO输出状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``do_state_h``: DO输出状态，co0~co7对应bit0~bit7 do_state_l DO输出状态，do0~do7对应bit0~bit7"

获取机器人DI、DO状态代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    block = 0 
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}") 
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    robot.CloseRPC()

等待控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitDI(id,status,maxtime,opt)``"
    "描述", "等待控制箱数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~15]；
    - ``status``:0-关，1-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱多路数字量输入
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMultiDI(mode,id,status,maxtime,opt)``"
    "描述", "等待控制箱多路数字量输入"
    "必选参数", "- ``mode``:[0]-多路与，[1]-多路或；
    - ``id``:io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7；
    - ``status``:bit0~bit7对应DI0~DI7状态，bit8~bit15对应CI0~CI7状态位的状态[0]-关，[1]-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolDI(id,status,maxtime,opt)``"
    "描述", "等待末端数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``status``:0-关，1-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAI(id,sign,value,maxtime,opt)``"
    "描述", "等待控制箱模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``sign``:0-大于，1-小于
    - ``value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待工具模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolAI(id,sign,value,maxtime,opt)``"
    "描述", "等待末端模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0]；
    - ``sign``:0-大于，1-小于
    - ``value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱数字、模拟输入信号代码示例
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0
    block = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    status = 0
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    block = 0
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}")
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    rtn = robot.WaitDI(0, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitMultiDI(1, 3, 3, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolDI(1, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    robot.CloseRPC()

设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag,reloadFlag)``"
    "描述", "设置控制箱DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag,reloadFlag)``"
    "描述", "设置控制箱AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleDO(resetFlag,reloadFlag)``"
    "描述", "设置末端工具DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleAO(resetFlag,reloadFlag)``"
    "描述", "设置末端工具AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtDO (resetFlag,reloadFlag)``"
    "描述", "设置扩展DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtAO (resetFlag,reloadFlag)``"
    "描述", "设置扩展AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置SmartTool停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetSmartToolDO(resetFlag,reloadFlag)``"
    "描述", "设置SmartTool停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置LUA程序停止/暂停后输出复位代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    for i in range(16):
        robot.SetDO(i, 1, 0, 0)
        time.sleep(0.2)
    resetFlag = 0
    resumeReloadFlag = 0
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag)
    robot.ProgramLoad("/fruser/test.lua")
    robot.ProgramRun()
    time.sleep(2)
    robot.PauseMotion()
    time.sleep(2)
    robot.ResumeMotion()
    time.sleep(2)
    robot.CloseRPC()
    return 0
    
设置可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDIConfig(config)``"
    "描述", "设置可配置CI端口功能"
    "必选参数", "
    - ``config``：CI0-CI7功能编码数组,  0-无;1-起弧成功;2-焊机准备;3-传送带检测;4-暂停;5-恢复;6-启动;7-停止;
      58-暂停/恢复;9-启动/停止;10-脚踏拖动;11-移至作业原点;12-手自动切换;
      613-焊丝寻位成功;14-运动中断;15-启动主程序;16-启动倒带;17-启动确认;
      718-光电检测信号X;19-光电检测信号Y;20-外部急停输入信号1;21-外部急停输入信号2;
      822-一级缩减模式;23-二级缩减模式;24-三级缩减模式(停止);25-恢复焊接;26-终止焊接;
      927-辅助拖动开启;28-辅助拖动关闭;29-辅助拖动开启/关闭;30-清除所有错误;
      1031-手自动切换(高低电平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定点跟踪开始/结束"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
获取控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDIConfig()``"
    "描述", "获取控制箱可配置CI端口功能"
    "必选参数", "
    - ``config``：CI0-CI7功能编码数组,  0-无;1-起弧成功;2-焊机准备;3-传送带检测;4-暂停;5-恢复;6-启动;7-停止;
      58-暂停/恢复;9-启动/停止;10-脚踏拖动;11-移至作业原点;12-手自动切换;
      613-焊丝寻位成功;14-运动中断;15-启动主程序;16-启动倒带;17-启动确认;
      718-光电检测信号X;19-光电检测信号Y;20-外部急停输入信号1;21-外部急停输入信号2;
      822-一级缩减模式;23-二级缩减模式;24-三级缩减模式(停止);25-恢复焊接;26-终止焊接;
      927-辅助拖动开启;28-辅助拖动关闭;29-辅助拖动开启/关闭;30-清除所有错误;
      1031-手自动切换(高低电平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定点跟踪开始/结束"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
设置可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDOConfig(config)``"
    "描述", "设置可配置CO端口功能"
    "必选参数", "
    - ``config``：CO0-CO7功能编码数组,0-无;1-机器人报错;2-机器人运动中;3-喷涂启停;4-喷涂清枪;5-送气信号;6-起弧信号;7-点动送丝;
      58-反向送丝;9-JOB输入口1;10-JOB输入口2;11-JOB输入口3;12-传送带启停控制;13-机器人暂停中;14-到达作业原点;
      615-到达干涉区;16-焊丝寻位启停控制;17-机器人启动完成;18-程序启动停止;19-自动手动模式;20-急停输出信号1-安全;
      721-急停输出信号2-安全;22-LUA脚本程序运行停止;23-安全状态输出-安全;24-保护性停止状态输出-安全;
      825-机器人运动中-安全;26-机器人缩减模式-安全;27-机器人非缩减模式-安全;28-机器人非停止;29-机器人报错-指令点错误;
      930-机器人报错-驱动器错误;31-机器人报错-超出软限位错误;32-机器人报错-碰撞错误;33-机器人报错-活动从站数量错误;
      1034-机器人报错-从站错误;35-机器人报错-IO错误;36-机器人报错-夹爪错误;37-机器人报错-文件错误;38-机器人报错-奇异位姿错误;
      1139-机器人报错-驱动器通信错误;40-机器人报错-参数错误;41-机器人报错-外部轴超出软限位错误;42-机器人警告-警告;
      1243-机器人警告-安全门警告;44-机器人警告-运动警告;45-机器人警告-干涉区警告;46-机器人警告-安全墙警告;
      1347-使能状态;48-断线自动抬升中;49-立方体1干涉警告;50-立方体2干涉警告;51-立方体3干涉警告;52-立方体4干涉警告;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
获取可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDOConfig()``"
    "描述", "获取可配置CO端口功能"
    "必选参数", "
    - ``config``：CO0-CO7功能编码数组,0-无;1-机器人报错;2-机器人运动中;3-喷涂启停;4-喷涂清枪;5-送气信号;6-起弧信号;7-点动送丝;
      58-反向送丝;9-JOB输入口1;10-JOB输入口2;11-JOB输入口3;12-传送带启停控制;13-机器人暂停中;14-到达作业原点;
      615-到达干涉区;16-焊丝寻位启停控制;17-机器人启动完成;18-程序启动停止;19-自动手动模式;20-急停输出信号1-安全;
      721-急停输出信号2-安全;22-LUA脚本程序运行停止;23-安全状态输出-安全;24-保护性停止状态输出-安全;
      825-机器人运动中-安全;26-机器人缩减模式-安全;27-机器人非缩减模式-安全;28-机器人非停止;29-机器人报错-指令点错误;
      930-机器人报错-驱动器错误;31-机器人报错-超出软限位错误;32-机器人报错-碰撞错误;33-机器人报错-活动从站数量错误;
      1034-机器人报错-从站错误;35-机器人报错-IO错误;36-机器人报错-夹爪错误;37-机器人报错-文件错误;38-机器人报错-奇异位姿错误;
      1139-机器人报错-驱动器通信错误;40-机器人报错-参数错误;41-机器人报错-外部轴超出软限位错误;42-机器人警告-警告;
      1243-机器人警告-安全门警告;44-机器人警告-运动警告;45-机器人警告-干涉区警告;46-机器人警告-安全墙警告;
      1347-使能状态;48-断线自动抬升中;49-立方体1干涉警告;50-立方体2干涉警告;51-立方体3干涉警告;52-立方体4干涉警告;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
设置末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDIConfig(config)``"
    "描述", "设置末端可配置End-CI端口功能"
    "必选参数", "
    - ``config``：End CI0-CI1功能编码数组,0-无;1-拖动示教工具开关;2-点记录信号;3-手自动切换（脉冲信号）;4-TPD记录启动/停止;5-暂停运动;
      56-恢复运动;7-启动;8-停止;9-暂停/恢复;10-启动/停止;11-力传感器辅助拖动开启;12-力传感器辅助拖动关闭;
      613-力传感器辅助拖动开启/关闭;14-激光检测信号X;15-激光检测信号Y;16-PTP运动至作业原点;17-运动中断，根据信号停止当前运动;
      718-启动主程序;19-启动倒带;20-启动确认;21-恢复焊接;22-终止焊接;23-清除错误;24-手自动切换（高低电平）
      825-使能;26-去使能;27-使能/去使能;28-激光伺服跟踪启停信号;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
获取末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDIConfig()``"
    "描述", "获取末端可配置End-CI端口功能"
    "必选参数", "
    - ``config``：End CI0-CI1功能编码数组,0-无;1-拖动示教工具开关;2-点记录信号;3-手自动切换（脉冲信号）;4-TPD记录启动/停止;5-暂停运动;
      56-恢复运动;7-启动;8-停止;9-暂停/恢复;10-启动/停止;11-力传感器辅助拖动开启;12-力传感器辅助拖动关闭;
      613-力传感器辅助拖动开启/关闭;14-激光检测信号X;15-激光检测信号Y;16-PTP运动至作业原点;17-运动中断，根据信号停止当前运动;
      718-启动主程序;19-启动倒带;20-启动确认;21-恢复焊接;22-终止焊接;23-清除错误;24-手自动切换（高低电平）
      825-使能;26-去使能;27-使能/去使能;28-激光伺服跟踪启停信号;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "
    
设置控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDIConfigLevel(config)``"
    "描述", "设置控制箱可配置CI有效状态"
    "必选参数", "
    - ``config``：CI0-CI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取控制箱可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDIConfigLevel()``"
    "描述", "获取控制箱可配置CI有效状态"
    "必选参数", "
    - ``config``：CI0-CI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDOConfigLevel(config)``"
    "描述", "设置控制箱可配置CO有效状态"
    "必选参数", "
    - ``config``：CO0-CO7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取控制箱可配置CO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDOConfigLevel()``"
    "描述", "获取控制箱可配置CO有效状态"
    "必选参数", "
    - ``config``：CO0-CO7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDIConfigLevel(config)``"
    "描述", "设置末端可配置CI有效状态"
    "必选参数", "
    - ``config``：CI0-CI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取末端可配置CI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDIConfigLevel()``"
    "描述", "获取末端可配置CI有效状态"
    "必选参数", "
    - ``config``：CI0-CI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStandardDILevel(config)``"
    "描述", "设置控制箱标准DI有效状态"
    "必选参数", "
    - ``config``：DI0-DI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取控制箱标准DI有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetStandardDILevel()``"
    "描述", "获取控制箱标准DI有效状态"
    "必选参数", "
    - ``config``：DI0-DI7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStandardDOLevel(config)``"
    "描述", "设置控制箱标准DO有效状态"
    "必选参数", "
    - ``config``：DO0-DO7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
获取控制箱标准DO有效状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetStandardDOLevel()``"
    "描述", "获取控制箱标准DO有效状态"
    "必选参数", "
    - ``config``：DO0-DO7端口有效状态数组；0-高电平有效；1-低电平有效"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
IO配置相关的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 与机器人控制器建立连接
    robot = Robot.RPC('192.168.58.2')


    def TestIOConfig(self):
        # 设置和获取DI配置
        setDIConfig = [1, 2, 3, 4, 5, 6, 7, 8]
        getDIConfig = [0] * 8
        rtn = robot.SetDIConfig(setDIConfig)
        print(f"SetDIConfig rtn is {rtn}")
        rtn, getDIConfig = robot.GetDIConfig()
        print(f"GetDIConfig rtn is {rtn}, value is {getDIConfig[0]} {getDIConfig[1]} {getDIConfig[2]} {getDIConfig[3]} {getDIConfig[4]} {getDIConfig[5]} {getDIConfig[6]} {getDIConfig[7]}")

        # 设置和获取DO配置
        setDOConfig = [9, 10, 11, 12, 13, 14, 15, 16]
        getDOConfig = [0] * 8
        rtn = robot.SetDOConfig(setDOConfig)
        print(f"SetDOConfig rtn is {rtn}")
        rtn, getDOConfig = robot.GetDOConfig()
        print(f"GetDOConfig rtn is {rtn}, value is {getDOConfig[0]} {getDOConfig[1]} {getDOConfig[2]} {getDOConfig[3]} {getDOConfig[4]} {getDOConfig[5]} {getDOConfig[6]} {getDOConfig[7]}")

        # 设置和获取工具DI配置
        setToolDIConfig = [17, 18]
        getToolDIConfig = [0] * 2
        rtn = robot.SetToolDIConfig(setToolDIConfig)
        print(f"SetToolDIConfig rtn is {rtn}")
        rtn, getToolDIConfig = robot.GetToolDIConfig()
        print(f"GetToolDIConfig rtn is {rtn}, value is {getToolDIConfig[0]} {getToolDIConfig[1]}")

        # 设置和获取DI电平配置（0: 低电平有效, 1: 高电平有效）
        setDIConfigLevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getDIConfigLevel = [0] * 8
        rtn = robot.SetDIConfigLevel(setDIConfigLevel)
        print(f"SetDIConfigLevel rtn is {rtn}")
        rtn, getDIConfigLevel = robot.GetDIConfigLevel()
        print(f"GetDIConfigLevel rtn is {rtn}, value is {getDIConfigLevel[0]} {getDIConfigLevel[1]} {getDIConfigLevel[2]} {getDIConfigLevel[3]} {getDIConfigLevel[4]} {getDIConfigLevel[5]} {getDIConfigLevel[6]} {getDIConfigLevel[7]}")

        # 设置和获取DO电平配置（0: 低电平有效, 1: 高电平有效）
        setDOConfigLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getDOConfigLevel = [0] * 8
        rtn = robot.SetDOConfigLevel(setDOConfigLevel)
        print(f"SetDOConfigLevel rtn is {rtn}")
        rtn, getDOConfigLevel = robot.GetDOConfigLevel()
        print(f"GetDOConfigLevel rtn is {rtn}, value is {getDOConfigLevel[0]} {getDOConfigLevel[1]} {getDOConfigLevel[2]} {getDOConfigLevel[3]} {getDOConfigLevel[4]} {getDOConfigLevel[5]} {getDOConfigLevel[6]} {getDOConfigLevel[7]}")

        # 设置和获取工具DI电平配置
        setToolDIConfigLevel = [1, 0]
        getToolDIConfigLevel = [0] * 2
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel)
        print(f"SetToolDIConfigLevel rtn is {rtn}")
        rtn, getToolDIConfigLevel = robot.GetToolDIConfigLevel()
        print(f"GetToolDIConfigLevel rtn is {rtn}, value is {getToolDIConfigLevel[0]} {getToolDIConfigLevel[1]}")

        # 设置和获取标准DI电平配置
        setStandardDILevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getStandardDILevel = [0] * 8
        rtn = robot.SetStandardDILevel(setStandardDILevel)
        print(f"SetStandardDILevel rtn is {rtn}")
        rtn, getStandardDILevel = robot.GetStandardDILevel()
        print(f"GetStandardDILevel rtn is {rtn}, value is {getStandardDILevel[0]} {getStandardDILevel[1]} {getStandardDILevel[2]} {getStandardDILevel[3]} {getStandardDILevel[4]} {getStandardDILevel[5]} {getStandardDILevel[6]} {getStandardDILevel[7]}")

        # 设置和获取标准DO电平配置
        setStandardDOLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getStandardDOLevel = [0] * 8
        rtn = robot.SetStandardDOLevel(setStandardDOLevel)
        print(f"SetStandardDOLevel rtn is {rtn}")
        rtn, getStandardDOLevel = robot.GetStandardDOLevel()
        print(f"GetStandsrdDOLevel rtn is {rtn}, value is {getStandardDOLevel[0]} {getStandardDOLevel[1]} {getStandardDOLevel[2]} {getStandardDOLevel[3]} {getStandardDOLevel[4]} {getStandardDOLevel[5]} {getStandardDOLevel[6]} {getStandardDOLevel[7]}")

        # 等待2秒
        time.sleep(2)

        # 关闭连接
        robot.CloseRPC()
        time.sleep(1)

    # 调用测试函数
    TestIOConfig(robot)