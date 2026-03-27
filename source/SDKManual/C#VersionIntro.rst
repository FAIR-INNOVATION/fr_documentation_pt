版本更新说明
====================

.. toctree:: 
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **版本号**
     - **日期**
     - **更新描述**

   * - V3.9.4
     - 2026-03-25
     - | 1.ServoJTStart()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 2.ServoJTEnd()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 3.ServoJT()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 4.ServoMoveStart()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 5.ServoMoveEnd()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 6.ServoJ()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 7.SetWeldMachineCtrlMode()接口新增控制模式选择参数；
       | 8.ExtDevGetUDPComParam()接口新增获取UDP通信参数：重启控制箱后是否自动重连；
       | 9.新增SetAxleGenComEnable()开启末端通用透传功能接口；
       | 10.新增SndRcvAxleGenComCmdData()末端发送非周期数据并等待应答接口；
       | 11.新增SetRobotStopOnComDisc()设置端口通讯断开时停止机器人运行接口；
       | 12.新增GetRobotStopOnComDisc()获取端口通讯断开时停止机器人运行参数接口；
       | 13.新增SetDIConfig()设置控制箱可配置 CI 端口功能接口；
       | 14.新增GetDIConfig()获取控制箱可配置 CI 端口功能接口；
       | 15.新增SetDOConfig()设置控制箱可配置 CO 端口功能接口；
       | 16.新增GetDOConfig()获取控制箱可配置 CO 端口功能接口；
       | 17.新增SetToolDIConfig()设置末端可配置 End-CI 端口功能接口；
       | 18.新增GetToolDIConfig()获取末端可配置 End-CI 端口功能接口；
       | 19.新增SetDIConfigLevel()设置控制箱可配置 CI 有效状态接口；
       | 20.新增GetDIConfigLevel()获取控制箱可配置 CI 有效状态接口；
       | 21.新增SetDOConfigLevel()设置控制箱可配置 CO 有效状态接口；
       | 22.新增GetDOConfigLevel()获取控制箱可配置 CO 有效状态接口；
       | 23.新增SetToolDIConfigLevel()设置末端可配置 CI 有效状态接口；
       | 24.新增GetToolDIConfigLevel()获取末端可配置 CI 有效状态接口；
       | 25.新增SetStandardDILevel()设置控制箱标准 DI 有效状态接口；
       | 26.新增GetStandardDILevel()获取控制箱标准 DI 有效状态接口；
       | 27.新增SetStandardDOLevel()设置控制箱标准 DO 有效状态接口；
       | 28.新增GetStandardDOLevel()获取控制箱标准 DO 有效状态接口；
       | 29.新增SetExAxisCmdDoneTimeUDP() 扩展轴定位完成时间设置接口；
       | 30.新增OpenLuaDownload()下载开放协议 Lua 文件接口；
       | 31.新增OpenLuaDelete()删除开放协议 Lua 文件接口；
       | 32.新增AllOpenLuaDelete()删除开放协议 Lua 文件接口；
       | 33.新增SendUDPFrameUDP ()发送指令帧接口；
       | 34.新增SetCmdRpyCallback()设置 SDK 通过 UDP 发送指令的执行结果回调函数接口；
       | 35.新增SetVelReducePara()设置安全速度参数接口；
       | 36.新增OriginPointWeaveStart()定点摆动开始接口；
       | 37.新增OriginPointWeaveEnd()定点摆动结束接口；
       | 38.新增SetUserLEDColor()设置用户自定义机器人末端灯色接口；
       | 39.新增MoveToTPDStart()运动到 TPD 轨迹记录起点接口；
   
   * - V3.9.3
     - 2026-02-11
     - | 1.ServoCart()接口增加扩展轴参数
       | 2.SetOutputResetCtlBoxDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 3.SetOutputResetCtlBoxAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 4.SetOutputResetAxleDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 5.SetOutputResetAxleAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 6.SetOutputResetExtDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 7.SetOutputResetExtAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 8.SetOutputResetSmartToolDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 9.增加GetInverseKinExaxis()包含扩展轴位置的逆运动学求解接口

   * - V3.9.2
     - 2026-01-26
     - | 1.FT_RotInsertion()接口增加未检测到力/力矩的处理策略参数
       | 2.LaserSensorRecordandReplay()接口增加机器人定点跟踪相关参数
       | 3.增加MoveStationary()接口
       | 4.增加TCPComputeRPY()接口
       | 5.增加TCPComputeXYZ()接口
       | 6.增加TCPRecordFlangePosStart()接口
       | 7.增加TCPRecordFlangePosEnd()接口
       | 8.增加TCPGetRecordFlangePos()接口
       | 9.增加PhotoelectricSensorTCPCalibration()接口

   * - V3.9.1
     - 2025-12-25
     - | 1.MoveL()接口增加oacc速度缩放因子参数/物理加速度参数
       | 2.MoveC()接口增加oacc速度缩放因子参数/物理加速度参数
       | 3.Circle()接口优化关于物理速度和物理加速度的参数描述
       | 4.增加FT_Control()重载函数，具有rx、ry启动阈值、力矩调节系数参数
       | 5.增加SerCoderCompenParams()接口

   * - V3.9.0
     - 2025-11-26
     - | 1.JointSensitivityCalibration()接口增加j1~j6关节线性度返回
       | 2.增加JointHysteresisError()接口
       | 3.增加JointRepeatability()接口
       | 4.增加SetAdmittanceParams()接口
       | 5.增加MoveToIntersectLineStart()接口
       | 6.增加MoveIntersectLine()接口
       
   * - V3.8.7
     - 2025-10-21
     - | 1.FT_Control()增加质量参数和阻尼参数接口
       | 2.增加JointSensitivityCalibration()接口
       | 3.增加JointSensitivityCollect()接口
       | 4.增加MotionQueueClear()接口
       | 5.增加GetSlavePortErrCounter()接口
       | 6.增加SlavePortErrCounterClear()接口
       | 7.增加SetVelFeedForwardRatio()接口
       | 8.增加GetVelFeedForwardRatio()接口
       | 9.增加RobotMCULogCollect()接口
       | 10.状态结构体增加ServoJ指令计数及最后一个指令目标位置数据
       | 11.新螺旋线参数结构体SpiralParam增加速度加速度参数模式

   * - V3.8.6
     - 2025-09-19
     - | 1.SetLoadCoord()接口增加负载编号参数
       | 2.增加LaserTrackingLaserOnOff()接口
       | 3.增加LaserTrackingTrackOnOff()接口
       | 4.增加LaserTrackingSearchStart_xyz()接口
       | 5.增加LaserTrackingSearchStart_point()接口
       | 6.增加LaserTrackingSearchStop()接口
       | 7.增加LaserTrackingSensorConfig()接口
       | 8.增加LaserTrackingSensorSamplePeriod()接口
       | 9.增加LoadPosSensorDriver()接口
       | 10.增加UnLoadPosSensorDriver()接口
       | 11.增加LaserSensorRecord1()接口
       | 12.增加LaserSensorReplay()接口
       | 13.增加MoveLTR()接口
       | 14.增加LaserSensorRecordandReplay()接口
       | 15.增加MoveToLaserRecordStart()接口
       | 16.增加MoveToLaserRecordEnd()接口
       | 17.增加MoveToLaserSeamPos()接口
       | 18.增加GetLaserSeamPos()接口
       | 19.增加ImpedanceControlStartStop()接口
       | 20.增加GetToolCoordWithID()接口
       | 21.增加GetWObjCoordWithID()接口
       | 22.增加GetExToolCoordWithID()接口
       | 23.增加GetExAxisCoordWithID()接口
       | 24.增加GetTargetPayloadWithID()接口
       | 25.增加GetExAxisCoordWithID()接口
       | 26.增加GetCurWObjCoord()接口
       | 27.增加GetCurExToolCoord()接口
       | 28.增加GetCurExToolCoord()接口
       | 29.增加KernelUpgrade()接口
       | 30.增加GetKernelUpgradeResult()接口
       | 31.增加CustomWeaveSetPara()接口
       | 32.增加CustomWeaveGetPara()接口
       | 33.状态结构体增加工具、工件、外部工具、扩展轴坐标系和负载质量、质心数据

   * - V3.8.5
     - 2025-08-20
     - | 1.增加OpenLuaUpload()接口
       | 2.增加GetFieldBusConfig()接口
       | 3.增加FieldBusSlaveWriteDO()接口
       | 4.增加FieldBusSlaveWriteAO()接口
       | 5.增加FieldBusSlaveReadDI()接口
       | 6.增加FieldBusSlaveReadAI()接口
       | 7.增加FieldBusSlaveWaitDI()接口
       | 8.增加FieldBusSlaveWaitAI()接口
       | 9.增加SetSuckerCtrl()接口
       | 10.增加GetSuckerState()接口
       | 11.增加WaitSuckerState()接口
       | 12.增加MoveL()速度加速度参数模式velAccParamMode接口
       | 13.增加MoveL()重载函数1接口
       | 14.增加MoveL()重载函数2接口
       | 15.增加MoveC()速度加速度参数模式velAccParamMode接口
       | 16.增加MoveC()重载函数1接口
       | 17.增加Circle()速度加速度参数模式velAccParamMode接口
       | 18.增加Circle()重载函数1接口
       | 19.增加SetExAxisRobotPlan()接口

   * - V3.8.4
     - 2025-07-17
     - | 1.ExtAxisMove()接口增加blend平滑参数
       | 2.增加SetFocusCalibPoint()接口
       | 3.增加ComputeFocusCalib()接口
       | 4.增加SetFocusPosition()接口
       | 5.增加FocusStart()接口
       | 6.增加FocusEnd()接口
       | 7.增加SetEncoderUpgrade()接口
       | 8.增加SetJointFirmwareUpgrade()接口
       | 9.增加SetCtrlFirmwareUpgrade()接口
       | 10.增加SetEndFirmwareUpgrade()接口
       | 11.增加JointAllParamUpgrade()接口
       
   * - V3.8.3
     - 2025-06-24
     - | 1.Circle()接口增加加速度百分比及平滑半径参数
       | 2.EndForceDragControl()接口增加辅助拖动时机器人碰撞检测标志参数
       | 3.ServoJ()接口增加指令ID参数
       | 4.增加SetSSHScpCmd()接口
       | 5.增加SetWideBoxTempFanMonitorParam()接口
       | 6.增加GetWideBoxTempFanMonitorParam()接口
       | 7.状态结构体增加控制箱温度和风扇电流状态数据
              
   * - V3.8.2
     - 2025-06-13
     - | 1.WeaveSetPara()接口增加摆动方向侧倾角(绕摆动X轴偏转)参数
       | 2.WeaveChangeStart()接口增加摆动编号、焊接开始速度、焊接结束速度参数
       | 3.ExtDevSetUDPComParam()接口增加断电重启后是否自动建立连接参数
       | 4.SetCollisionDetectionMethod()接口增加碰撞等级阈值方式选择
       | 5.PtpFIRPlanningStart()接口增加统一关节急动度极值
       | 6.增加WeldingSetVoltageGradualChangeStart()接口
       | 7.增加WeldingSetVoltageGradualChangeEnd()接口
       | 8.增加WeldingSetCurrentGradualChangeStart()接口
       | 9.增加WeldingSetCurrentGradualChangeEnd()接口
       | 10.增加ArcWeldTraceAIChannelCurrent()接口
       | 11.增加ArcWeldTraceAIChannelVoltage()接口
       | 12.增加ArcWeldTraceCurrentPara()接口
       | 13.增加ArcWeldTraceVoltagePara()接口
       | 14.增加GetSmarttoolBtnState()接口
       | 15.增加ExtAxisGetCoord()接口
                     
   * - V3.8.1
     - 2025-04-24
     - | 1.ConveyorSetParam()接口增加跟踪运动类型、跟踪起始距离、跟踪终止距离参数
       | 2.增加AccSmoothStart()接口
       | 3.增加AccSmoothEnd()接口
       | 4.增加RbLogDownload()接口
       | 5.增加AllDataSourceDownload()接口
       | 6.增加DataPackageDownload()接口
       | 7.增加GetRobotSN()接口
       | 8.增加ShutDownRobotOS()接口
       | 9.增加ConveyorComDetect()接口
       | 10.增加ConveyorComDetectTrigger()接口
                     
   * - V3.8.0
     - 2025-02-12
     - | 1.EndForceDragControl()接口增加奇异点规避参数
       | 2.ArcWeldTraceControl()接口增加偏置参数
       | 3.增加WeaveChangeStart()接口
       | 4.增加WeaveChangeEnd()接口
       | 5.增加LoadTrajectoryLA()接口
       | 6.增加MoveTrajectoryLA()接口
       | 7.增加CustomCollisionDetectionStart()接口
       | 8.增加CustomCollisionDetectionEnd()接口