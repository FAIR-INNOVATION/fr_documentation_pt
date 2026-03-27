扩展轴
=============

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "描述", "设置485扩展轴参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取485扩展轴配置参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetParam(servoId)``"
    "描述", "获取485扩展轴配置参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"

设置485扩展轴使能/去使能
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoEnable(servoId,status)``"
    "描述", "设置485扩展轴使能/去使能"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``status``：使能状态，0-去使能， 1-使能;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴控制模式
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetControlMode(servoId,mode)``"
    "描述", "设置485扩展轴控制模式"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：控制模式，0-位置模式，1-速度模式;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "描述", "设置485扩展轴目标位置(位置模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``pos``：目标位置，mm或°；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴目标转矩(力矩模式)-暂未开放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetTorque(servoId,torque)``"
    "描述", "设置485扩展轴目标转矩(力矩模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``torque``：目标力矩，Nm;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "描述", "设置485扩展轴回零"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：回零模式，1-当前位置回零；2-负限位回零；3-正限位回零;
    - ``searchVel``： 回零速度，mm/s或°/s;
    - ``latchVel``：箍位速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoClearError(servoId)``"
    "描述", "清除485扩展轴错误信息"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetStatus(servoId)``"
    "描述", "获取485扩展轴伺服状态"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoErrCode``：伺服驱动器故障码
    - ``servoState``：伺服驱动器状态 bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成；
    - ``servoPos``：伺服当前位置 mm或°；
    - ``servoSpeed``：伺服当前速度 mm/s或°/s；
    - ``servoTorque``：伺服当前转矩Nm；"

设置485扩展轴目标速度(速度模式)
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "描述", "设置485扩展轴目标速度(速度模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServosetStatusID(servoId)``"
    "描述", "设置状态反馈中485扩展轴数据轴号"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetAcc(acc, dec)``"
    "描述", "设置485扩展轴运动加减速度"
    "必选参数", "- ``acc``：485扩展轴运动加速度
    - ``dec``：485扩展轴运动减速度"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetEmergencyStopAcc(acc, dec)``"
    "描述", "设置485扩展轴急停加减速度"
    "必选参数", "- ``acc``：485扩展轴急停加速度
    - ``dec``：485扩展轴急停减速度"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetAcc()``"
    "描述", "获取485扩展轴运动加减速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``acc``：485扩展轴运动加速度
    - ``dec``：485扩展轴运动减速度"

获取485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetEmergencyStopAcc()``"
    "描述", "获取485扩展轴急停加减速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``acc``：485扩展轴急停加速度
    - ``dec``：485扩展轴急停减速度"

扩展轴控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45)
    print(f"AuxServoSetParam is: {retval}")
    servoCompany = 0
    servoModel = 0
    servoSoftVersion = 0
    servoResolution = 0
    axisMechTransRatio = 0.0
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14)
    print(f"AuxServoSetParam is: {retval}")
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36)
    print(f"AuxServoSetParam is: {retval}")
    time.sleep(3)
    robot.AuxServoSetAcc(3000, 3000)
    robot.AuxServoSetEmergencyStopAcc(5000, 5000)
    time.sleep(1)
    emagacc = 0.0
    emagdec = 0.0
    acc = 0.0
    dec = 0.0
    error,emagacc, emagdec = robot.AuxServoGetEmergencyStopAcc()
    print(f"emergency acc is {emagacc}  dec is {emagdec}")
    error,acc, dec = robot.AuxServoGetAcc()
    print(f"acc is {acc}  dec is {dec}")
    robot.AuxServoSetControlMode(1, 0)
    time.sleep(2)
    retval = robot.AuxServoEnable(1, 0)
    print(f"AuxServoEnable disenable {retval}")
    time.sleep(1)
    servoErrCode = 0
    servoState = 0
    servoPos = 0.0
    servoSpeed = 0.0
    servoTorque = 0.0
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoEnable(1, 1)
    print(f"AuxServoEnable enable {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoHoming(1, 1, 5, 1,100)
    print(f"AuxServoHoming {retval}")
    time.sleep(3)
    retval = robot.AuxServoSetTargetPos(1, 200, 30,100)
    print(f"AuxServoSetTargetPos {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoSpeed {servoSpeed}")
    time.sleep(8)
    robot.AuxServoSetControlMode(1, 1)
    time.sleep(2)
    robot.AuxServoEnable(1, 0)
    time.sleep(1)
    robot.AuxServoEnable(1, 1)
    time.sleep(1)
    robot.AuxServoSetTargetSpeed(1, 100, 80)
    time.sleep(5)
    robot.AuxServoSetTargetSpeed(1, 0, 80)
    robot.CloseRPC()

UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevSetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum, selfConnect)``"
    "描述", "UDP扩展轴通讯参数配置"
    "必选参数", "
    - ``ip``：PLC IP地址；
    - ``port``：端口号；
    - ``period``：通讯周期(ms，暂不开放)；
    - ``lossPkgTime``：丢包检测时间(ms)；
    - ``lossPkgNum``：丢包次数；
    - ``disconnectTime``：通讯断开确认时长；
    - ``reconnectEnable``：通讯断开自动重连使能 0-不使能 1-使能；
    - ``reconnectPeriod``：重连周期间隔(ms)；
    - ``reconnectNum``：重连次数
    - ``selfConnect``：断电重启是否自动建立连接；0-不建立连接；1-建立连接"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取UDP扩展轴通讯参数
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevGetUDPComParam()``"
    "描述", "获取UDP扩展轴通讯参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "
    - 错误码 成功-0  失败- errcode；
    - ``ip``：PLC IP地址；
    - ``port``：端口号；
    - ``period``：通讯周期(ms，暂不开放)；
    - ``lossPkgTime``：丢包检测时间(ms)；
    - ``lossPkgNum``：丢包次数；
    - ``disconnectTime``：通讯断开确认时长；
    - ``reconnectEnable``：通讯断开自动重连使能 0-不使能 1-使能；
    - ``reconnectPeriod``：重连周期间隔(ms)；
    - ``reconnectNum``：重连次数
    - ``selfConnect``：重启控制箱后是否自动重连；0-不重连；1-重连"
 
加载UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevLoadUDPDriver()``"
    "描述", "加载UDP通信"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
卸载UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUnloadUDPDriver()``"
    "描述", "卸载UDP通信"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴通信异常断开后恢复连接
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComReset()``"
    "描述", "UDP扩展轴通信异常断开后恢复连接"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴通信异常断开后关闭通讯
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComClose()``"
    "描述", "UDP扩展轴通信异常断开后关闭通讯"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisParamConfig(axisId, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc,axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType)``"
    "描述", "UDP扩展轴参数配置"
    "必选参数", "
    - ``axisId``：轴号[1-4]；
    - ``axisType``：扩展轴类型 0-平移；1-旋转；
    - ``axisDirection``：扩展轴方向 0-正向；1-反向；
    - ``axisMax``：扩展轴最大位置 mm；
    - ``axisMin``：扩展轴最小位置 mm；
    - ``axisVel``：速度mm/s；
    - ``axisAcc``：加速度mm/s2；
    - ``axisLead``：导程mm；
    - ``encResolution``：编码器分辨率；
    - ``axisOffect``：焊缝起始点扩展轴偏移量；
    - ``axisCompany``：驱动器厂家 1-禾川；2-汇川；3-松下；
    - ``axisModel``：驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG；
    - ``axisEncType``：编码器类型  0-增量；1-绝对值；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展机器人相对扩展轴位置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotPosToAxis(installType)``"
    "描述", "设置扩展机器人相对扩展轴位置"
    "必选参数", "- ``installType``：0-机器人安装在外部轴上，1-机器人安装在外部轴外；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展轴系统DH参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxisDHParaConfig(axisConfig,axisDHd1,axisDHd2,axisDHd3,axisDHd4,axisDHa1, axisDHa2,axisDHa3,axisDHa4)``"
    "描述", "设置扩展轴系统DH参数配置"
    "必选参数", "
    - ``axisConfig``：外部轴构型，0-单自由度直线滑轨，1-两自由度L型变位机，2-三自由度，3-四自由度，4-单自由度变位机；
    - ``axisDHd1``：外部轴DH参数d1 mm；
    - ``axisDHd2``：外部轴DH参数d2 mm；
    - ``axisDHd3``：外部轴DH参数d3 mm；
    - ``axisDHd4``：外部轴DH参数d4 mm；
    - ``axisDHa1``：外部轴DH参数a1 mm；
    - ``axisDHa2``：外部轴DH参数a2 mm；
    - ``axisDHa3``：外部轴DH参数a3 mm；
    - ``axisDHa4``：外部轴DH参数a4 mm；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
                          
UDP扩展轴使能
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisServoOn(axisID, status)``"
    "描述", "UDP扩展轴使能"
    "必选参数", "- ``axisID``：轴号[1-4]；
    - ``status``：0-去使能；1-使能；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetHoming(axisID, mode, searchVel, latchVel)``"
    "描述", "UDP扩展轴回零"
    "必选参数", "
    - ``axisID``：轴号[1-4]；
    - ``mode``：回零方式 0当前位置回零，1负限位回零，2-正限位回零；
    - ``searchVel``：寻零速度(mm/s)；
    - ``latchVel``：寻零箍位速度(mm/s)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴点动开始
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStartJog( axisID, direction, vel, acc, maxDistance)``"
    "描述", "UDP扩展轴点动开始"
    "必选参数", "
    - ``axisID``：轴号[1-4]；
    - ``direction``：转动方向 0-反向；1-正向；
    - ``vel``：速度(mm/s)；
    - ``acc``：加速度(mm/s)；
    - ``maxDistance``：最大点动距离；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴点动停止
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStopJog(axisID)``"
    "描述", "UDP扩展轴点动停止"
    "必选参数", "- ``axisID``：轴号[1-4]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴配置与点动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
    print(f"ExtDevSetUDPComParam rtn is {rtn}")
    ip = ""
    port = 0
    period = 0
    lossPkgTime = 0
    lossPkgNum = 0
    disconnectTime = 0
    reconnectEnable = 0
    reconnectPeriod = 0
    reconnectNum = 0
    rtn,[ip, port, period, lossPkgTime, lossPkgNum,disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum] = robot.ExtDevGetUDPComParam()
    param_str = (f"\nip {ip}\nport {port}\nperiod {period}\nlossPkgTime {lossPkgTime}"
                 f"\nlossPkgNum {lossPkgNum}\ndisConntime {disconnectTime}"
                 f"\nreconnecable {reconnectEnable}\nreconnperiod {reconnectPeriod}"
                 f"\nreconnnun {reconnectNum}")
    print(f"ExtDevGetUDPComParam rtn is {rtn}{param_str}")
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
    rtn = robot.ExtAxisServoOn(2, 1)
    print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    print(f"ExtAxisSetHoming rtn is {rtn}")
    time.sleep(4)
    rtn = robot.SetRobotPosToAxis(1)
    print(f"SetRobotPosToAxis rtn is {rtn}")
    rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0)
    print(f"SetAxisDHParaConfig rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")
    time.sleep(3)
    robot.ExtAxisStartJog(1, 0, 10, 10, 30)
    time.sleep(1)
    robot.ExtAxisStopJog(1)
    time.sleep(3)
    robot.ExtAxisServoOn(1, 0)
    time.sleep(3)
    robot.ExtAxisStartJog(2, 0, 10, 10, 30)
    time.sleep(1)
    robot.ExtAxisStopJog(2)
    time.sleep(3)
    robot.ExtAxisServoOn(2, 0)
    robot.ExtDevUnloadUDPDriver()
    robot.CloseRPC()

设置扩展轴坐标系参考点-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetRefPoint(pointNum)``"
    "描述", "设置扩展轴坐标系参考点-四点法"
    "必选参数", "- ``pointNum``：点编号[1-4]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
计算扩展轴坐标系-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisComputeECoordSys()``"
    "描述", "计算扩展轴坐标系-四点法"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``coord``：扩展轴坐标系值[x,y,z,rx,ry,rz]；"
                 
变位机坐标系参考点设置-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorSetRefPoint(pointNum)``"
    "描述", "变位机坐标系参考点设置-四点法"
    "必选参数", "- ``pointNum``：点编号[1-4]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

变位机坐标系计算-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorComputeECoordSys()``"
    "描述", "变位机坐标系计算-四点法"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``coord``：变位机坐标系值[x,y,z,rx,ry,rz]；"
             
设置标定参考点在变位机末端坐标系下位姿
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRefPointInExAxisEnd(pos)``"
    "描述", "设置标定参考点在变位机末端坐标系下位姿"
    "必选参数", "- ``pos``：位姿值[x,y,z,rx,ry,rz]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

应用扩展轴坐标系
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisActiveECoordSys(applyAxisId,axisCoordNum,coord,calibFlag)``"
    "描述", "应用扩展轴坐标系"
    "必选参数", "
    - ``applyAxisId``:扩展轴编号 bit0-bit3对应扩展轴编号1-4，如应用扩展轴1和3，则是 0b 0000 0101,也就是5；
    - ``axisCoordNum``：扩展轴坐标系编号；
    - ``coord``：坐标系值[x,y,z,rx,ry,rz]；
    - ``calibFlag``：标定标志 0-否，1-是；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取扩展轴坐标系
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisGetCoord()``"
    "描述", "获取扩展轴坐标系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``coord``：扩展轴坐标系"

扩展轴坐标系标定代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
    print(f"ExtDevSetUDPComParam rtn is {rtn}")
    rtn,udp_params = robot.ExtDevGetUDPComParam()
    ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum = udp_params
    patam = (
        f"\nip {ip}\nport {port}\nperiod {period}\nlossPkgTime {lossPkgTime}\n"
        f"lossPkgNum {lossPkgNum}\ndisConntime {disconnectTime}\nreconnecable {reconnectEnable}\n"
        f"reconnperiod {reconnectPeriod}\nreconnnun {reconnectNum}"
    )
    print(f"ExtDevGetUDPComParam rtn is {rtn}{patam}")
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
    rtn = robot.ExtAxisServoOn(2, 1)
    print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    print(f"ExtAxisSetHoming rtn is {rtn}")
    time.sleep(4)
    rtn = robot.SetRobotPosToAxis(1)
    print(f"SetRobotPosToAxis rtn is {rtn}")
    rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0)
    print(f"SetAxisDHParaConfig rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")
    toolCoord = [0, 0, 210, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    jSafe = [115.193, -96.149, 92.489, -87.068, -89.15, -83.488]
    j1 = [117.559, -92.624, 100.329, -96.909, -94.057, -83.488]
    j2 = [112.239, -90.096, 99.282, -95.909, -89.824, -83.488]
    j3 = [110.839, -83.473, 93.166, -89.22, -90.499, -83.487]
    j4 = [107.935, -83.572, 95.424, -92.873, -87.933, -83.488]
    descSafe = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc1 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc2 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc3 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc4 = [0.0,0.0,0.0,0.0,0.0,0.0]
    exaxisPos = [0.0,0.0,0.0,0.0]
    offdese = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, descSafe = robot.GetForwardKin(jSafe)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    error, desc1 = robot.GetForwardKin(j1)
    robot.MoveJ(joint_pos=j1,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    actualTCPPos = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, actualTCPPos = robot.GetActualTCPPose(0)
    robot.SetRefPointInExAxisEnd(actualTCPPos)
    rtn = robot.PositionorSetRefPoint(1)
    print(f"PositionorSetRefPoint 1 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc2 = robot.GetForwardKin(j2)
    rtn = robot.MoveJ(joint_pos=j2,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(2)
    print(f"PositionorSetRefPoint 2 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc3 = robot.GetForwardKin(j3)
    robot.MoveJ(joint_pos=j3,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(3)
    print(f"PositionorSetRefPoint 3 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc4 = robot.GetForwardKin(j4)
    robot.MoveJ(joint_pos=j4,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(4)
    print(f"PositionorSetRefPoint 4 rtn is {rtn}")
    time.sleep(2)
    axisCoord = [0.0,0.0,0.0,0.0,0.0,0.0]
    error,axisCoord = robot.PositionorComputeECoordSys()
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    print(f"PositionorComputeECoordSys rtn is {axisCoord[0]} {axisCoord[1]} {axisCoord[2]} {axisCoord[3]} {axisCoord[4]} {axisCoord[5]}")
    rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1)
    print(f"ExtAxisActiveECoordSys rtn is {rtn}")
    robot.CloseRPC()
          
UDP扩展轴运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisMove(pos,ovl,blend=-1)``"
    "描述", "UDP扩展轴运动"
    "必选参数", "- ``pos=[exaxis[0],exaxis[1],exaxis[2],exaxis[3]]``：目标位置 轴1位置~轴4位置;
    - ``ovl``：速度百分比"
    "默认参数", "- ``blend``：平滑参数(mm或ms)，-1,等待运动完成，默认-1"
    "返回值", "错误码 成功-0  失败- errcode"
                                        
UDP扩展轴运动代码示例
++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    axisPos = [20,0,0,0]
    robot.ExtAxisMove(axisPos, 50, -1)
    robot.CloseRPC()
    return 0

UDP扩展轴与机器人关节运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveJ(joint_pos,tool,user,exaxis_pos, desc_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl= 100.0,  blendT=-1.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP扩展轴与机器人关节运动同步运动"
    "必选参数", "
    - ``joint_pos``： 目标关节位置，单位 [°]；
    - ``desc_pos``：目标笛卡尔位姿，单位 [mm][°]
    - ``tool``：工具号，[0~14]
    - ``user``：工件号，[0~14]
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位"
    "默认参数", "
    - ``desc_pos``:目标笛卡尔位姿，单位 [mm][°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用正运动学求解返回值;
    - ``vel``： 速度百分比，[0~100] 默认20.0；
    - ``acc``：加速度百分比，[0~100] 暂不开放,默认0.0 ；
    - ``ovl``：速度缩放因子，[0~100] 默认100.0  ；
    - ``blendT``：[-1.0]-运动到位 (阻塞)，[0~500.0]-平滑时间 (非阻塞)，单位 [ms] 默认-1.0；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "返回值", "错误码 成功-0  失败- errcode；"
                                        
UDP扩展轴与机器人关节运动同步运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 设置UDP通信参数并加载
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 设置扩展轴参数
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 扩展轴使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 扩展轴坐标系标定
    pos = []  # 请在此填写标定点坐标
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 此操作应重复4次（用4个点）
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步运动起点与终点
    startdescPose = []  # 请填写具体坐标
    startjointPos = []  # 请填写具体坐标
    startexaxisPos = []  # 请填写具体坐标
    enddescPose = []  # 请填写具体坐标
    endjointPos = []  # 请填写具体坐标
    endexaxisPos = []  # 请填写具体坐标
    # 运动到起始点
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, -1, 0, offdese)
    robot.CloseRPC()
                  
UDP扩展轴与机器人直线运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveL(desc_pos, tool, user, exaxis_pos, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],config=-1)``"
    "描述", "UDP扩展轴与机器人直线运动同步运动"
    "必选参数", "
    - ``desc_pos``：目标笛卡尔位姿，单位 [mm][°]；
    - ``tool``：工具号，[0~14]；
    - ``user``：工件号，[0~14]；
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位；"
    "默认参数", "
    - ``joint_pos``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel``： 速度百分比，[0~100] 默认20.0；
    - ``acc``：加速度百分比，[0~100] 暂不开放,默认0.0；
    - ``ovl``：速度缩放因子，[0~100] 默认100.0；
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~500.0]-平滑时间 (非阻塞)，单位 [ms] 默认-1.0；
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0] ；
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1"
    "返回值", "错误码 成功-0  失败- errcode；"
                                            
UDP扩展轴与机器人直线运动同步运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 设置UDP通信参数并加载
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 设置扩展轴参数
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 扩展轴使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 扩展轴坐标系标定
    pos = []  # 请填写标定点坐标
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 需调用4次用于标定
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步运动起点与终点
    startdescPose = []  # 填写坐标
    startjointPos = []  # 填写坐标
    startexaxisPos = []  # 填写坐标
    enddescPose = []  # 填写坐标
    endjointPos = []  # 填写坐标
    endexaxisPos = []  # 填写坐标
    # 运动到起始点
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos, tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0)
    # 执行同步直线运动
    robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, 0, 0, offdese)
    robot.CloseRPC()
                      
UDP扩展轴与机器人圆弧运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveC(desc_pos_p, tool_p, user_p,exaxis_pos_p, desc_pos_t, tool_t, user_t,exaxis_pos_t,joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=100.0, offset_flag_p=0, offset_pos_p =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0, config=-1)``"
    "描述", " UDP扩展轴与机器人圆弧运动同步运动"
    "必选参数", "
    - ``desc_pos_p``：路径点笛卡尔位姿，单位 [mm][°]；
    - ``tool_p``：路径点工具号，[0~14]；
    - ``user_p``：路径点工件号，[0~14]；
    - ``exaxis_pos_p``：路径点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]；
    - ``desc_pos_t``：目标点笛卡尔位姿，单位 [mm][°]；
    - ``tool_t``：工具号，[0~14]；
    - ``user_t``：工件号，[0~14]；
    - ``exaxis_pos_t``：目标点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]；"
    "默认参数", "
    - ``joint_pos_p``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``joint_pos_t``:目标关节位置，单位 [°] 默认初值为[0.0,0.0,0.0,0.0,0.0,0.0]，默认值调用逆运动学求解返回值;
    - ``vel_p``: 路径点速度百分比，[0~100] 默认20.0；
    - ``acc_p``: 路径点加速度百分比，[0~100] 暂不开放,默认0.0 ；   
    - ``offset_flag_p``: 路径点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos_p``: 路径点位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``vel_t``: 目标点速度百分比，[0~100] 默认20.0；
    - ``acc_t``: 目标点加速度百分比，[0~100] 暂不开放 默认0.0；
    - ``offset_flag_t``: 目标点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos_t``: 目标点位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``ovl``: 速度缩放因子，[0~100] 默认100.0；
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0；
    - ``config``:逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解，默认-1"
    "返回值", "错误码 成功-0  失败- errcode；"
                                                
UDP扩展轴与机器人圆弧运动同步运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 设置UDP通信参数并加载
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 设置扩展轴参数
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 扩展轴使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 扩展轴坐标系标定
    pos = []  # 输入标定点坐标
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 调用4次以完成标定
    coord = []
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步圆弧起始点、中间点、终点
    startdescPose = []# 输入坐标
    startjointPos = []# 输入坐标
    startexaxisPos =[]  # 输入扩展轴坐标
    middescPose = []# 输入中间点
    midjointPos = []
    midexaxisPos =[]
    enddescPose = []
    endjointPos = []
    endexaxisPos =[]
    # 运动到起始点
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    # 开始同步圆弧运动
    robot.ExtAxisSyncMoveC(midjointPos,middescPose,1,1,midexaxisPos,
                           endjointPos,enddescPose,1,1,endexaxisPos,
                           100,100,0,offdese,
                           100,100,0,offdese,
                           100,0)
    robot.CloseRPC()

设置扩展DO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDO(DONum,bOpen,smooth,block)``"
    "描述", "设置扩展DO"
    "必选参数", "
    - ``DONum``： DO编号；
    - ``bOpen``：开关 True-开,False-关；
    - ``smooth``：是否平滑 True -是, False -否；
    - ``block``：是否阻塞 True -是, False -否；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展AO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAO(AONum,value,block)``"
    "描述", "设置扩展AO"
    "必选参数", "
    - ``AONum``： AO编号；
    - ``value``：模拟量值[0-4095]；
    - ``block``：是否阻塞 True -是, False -否；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
设置扩展DI输入滤波时间
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDIFilterTime(filterTime)``"
    "描述", "设置扩展DI输入滤波时间"
    "必选参数", "- ``filterTime``： 滤波时间(ms)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
设置扩展AI输入滤波时间
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAIFilterTime(AINum,filterTime)``"
    "描述", "设置扩展AI输入滤波时间"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``filterTime``： 滤波时间(ms)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxDI(DINum,bOpen,time,errorAlarm)``"
    "描述", "等待扩展DI输入"
    "必选参数", "
    - ``DINum``： DI编号；
    - ``bOpen``：开关 True-开,False-关；
    - ``time``：最大等待时间(ms)；
    - ``errorAlarm``：是否继续运动 True-是,False-否"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxAI(,AINum,sign,value,time,errorAlarm)``"
    "描述", "等待扩展AI输入"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``sign``：0-大于；1-小于；
    - ``value``：AI值；
    - ``time``：最大等待时间(ms)；
    - ``errorAlarm``：是否继续运动 True-是,False-否"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
获取扩展DI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxDI(DINum,isNoBlock)``"
    "描述", "获取扩展DI值"
    "必选参数", "
    - ``DINum``： DI编号；
    - ``isNoBlock``：是否阻塞 True-阻塞 false-非阻塞；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode；
    - ``isOpen``： 0-关；1-开；"
          
获取扩展AI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxAI(AINum,isNoBlock)``"
    "描述", "获取扩展AI值"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``isNoBlock``：是否阻塞 True-阻塞 False-非阻塞"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode；
    - ``value``：输入值；"

扩展IO代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    for i in range(128):
        robot.SetAuxDO(i, True, False, True)
        time.sleep(0.1)
    for i in range(128):
        robot.SetAuxDO(i, False, False, True)
        time.sleep(0.1)
    for i in range(409):
        value1 = i * 10
        value2 = 4095 - i * 10
        robot.SetAuxAO(0, value1, True)
        robot.SetAuxAO(1, value2, True)
        robot.SetAuxAO(2, value1, True)
        robot.SetAuxAO(3, value2, True)
        time.sleep(0.01)
    robot.SetAuxDIFilterTime(10)
    robot.SetAuxAIFilterTime(0, 10)
    for i in range(20):
        curValue = False
        error, curValue = robot.GetAuxDI(i, False)  # 注意：如库内部需引用方式，这里需修改
        print(f"DI{i}   {curValue}")
    curValue = -1
    for i in range(4):
        error, curValue = robot.GetAuxAI(i, True)  # 同样注意引用传参问题
        print(f"AI{i}   {curValue}")
    robot.WaitAuxDI(1, False, 1000, False)
    robot.WaitAuxAI(1, 1, 132, 1000, False)
    robot.CloseRPC()

可移动装置使能
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorEnable(enable)``"
    "描述", "可移动装置使能"
    "必选参数", "- ``enable``：使能状态，0-去使能，1-使能"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置回零
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorHoming()``"
    "描述", "可移动装置回零"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置直线运动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveL(distance, vel)``"
    "描述", "可移动装置直线运动"
    "必选参数", "- ``distance``：直线运动距离（mm）
    - ``vel``：直线运动速度百分比（0-100）"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置圆弧运动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveC(radio, angle, vel)``"
    "描述", "可移动装置圆弧运动"
    "必选参数", "- ``radio``：圆弧运动半径（mm）
    - ``angle``：圆弧运动角度（°）
    - ``vel``：圆弧运动速度百分比（0-100）"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置停止运动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "可移动装置停止运动"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置代码示例
++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 1)
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    rtn = robot.ExtAxisServoOn(2, 1)
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    time.sleep(4)
    robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0)
    robot.TractorEnable(False)
    time.sleep(2)
    robot.TractorEnable(True)
    time.sleep(2)
    robot.TractorHoming()
    time.sleep(2)
    robot.TractorMoveL(100, 2)
    time.sleep(5)
    robot.TractorStop()
    robot.TractorMoveL(-100, 20)
    time.sleep(5)
    robot.TractorMoveC(300, 90, 20)
    time.sleep(10)
    robot.TractorMoveC(300, -90, 20)
    time.sleep(1)
    robot.CloseRPC()

激光传感器记录点
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserRecordPoint(coordID)``"
    "描述", "激光传感器记录点"
    "必选参数", "- ``coordID``：激光传感器坐标系"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint``：激光传感器识别点关节位置
    - ``desc``：激光传感器识别点笛卡尔位置
    - ``exaxis``：激光传感器识别点扩展轴位置"

激光传感器记录点代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    direction_point = [0, 0, 0]
    rtn = robot.LaserTrackingSearchStart(2, direction_point, 10, 100, 10000, 2)
    print(f"LaserTrackingSearchStart rtn is {rtn}")
    robot.LaserTrackingSearchStop()
    coord_id = 2
    rtn, joint, desc, exaxis = robot.LaserRecordPoint(coord_id)
    print(f"rtn is {rtn}")
    print(f"desc_pos:{desc[0]},{desc[1]},{desc[2]},"
          f"{desc[3]},{desc[4]},{desc[5]}")
    print(f"joint_pos:{joint[0]},{joint[1]},{joint[2]},{joint[3]},{joint[4]},{joint[5]}")
    print(f"exaxis pos is {exaxis[0]} {exaxis[1]} {exaxis[2]} {exaxis[3]}")
    off = [0] * 6
    robot.MoveJ(joint,tool=1,user=0,vel=100,acc=100,ovl=50,exaxis_pos=exaxis,blendT=-1,offset_flag=0,offset_pos=off)
    robot.CloseRPC()

设置扩展轴与机器人同步运动策略
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExAxisRobotPlan(strategy)``"
    "描述", "设置扩展轴与机器人同步运动策略"
    "必选参数", "- ``strategy``：策略；0-以机器人为主；1-扩展轴与机器人同步"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展轴与机器人同步运动策略代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    joint_pos1 = [-22.016, -49.217, 124.714, -161.100, -85.108, -0.333]
    joint_pos2 = [-21.083, -46.613, 110.079, -147.796, -80.757, -0.330]
    joint_pos3 = [-25.572, -60.090, 135.397, -163.889, -82.489, -0.345]
    desc_pos1 = [2.637, -0.001, 30.673, 178.786, -4.134, 68.326]
    desc_pos2 = [213.812, -1.440, 47.311, 177.410, 0.166, 68.946]
    desc_pos3 = [444.342, -12.723, 82.470, -177.701, -1.325, 65.151]
    epos1 = [0.001, 0.000, 0.000, 0.000]
    epos2 = [299.977, 0.000, 0.000, 0.000]
    epos3 = [399.969, 0.000, 0.000, 0.000]
    offset_pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SetExAxisRobotPlan(0)
    print(f"SetExAxisRobotPlan rtn is {rtn}")
    time.sleep(1)
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos1,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos1,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 1 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos2,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos2,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 2 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos3,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos3,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 3 rtn is {rtn}")
    time.sleep(8)
    robot.CloseRPC()

UDP扩展轴定位完成时间设置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExAxisCmdDoneTime(time)``"
    "描述", "UDP扩展轴定位完成时间设置"
    "必选参数", "- ``time``：定位完成时间[ms]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
