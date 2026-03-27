机器人焊接
======================

.. toctree:: 
    :maxdepth: 5

设置焊接工艺曲线参数
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置焊接工艺曲线参数
     * @param [in] id 焊接工艺编号(1-99)
     * @param [in] startCurrent 起弧电流(A)
     * @param [in] startVoltage 起弧电压(V)
     * @param [in] startTime 起弧时间(ms)
     * @param [in] weldCurrent 焊接电流(A)
     * @param [in] weldVoltage 焊接电压(V)
     * @param [in] endCurrent 收弧电流(A)
     * @param [in] endVoltage 收弧电压(V)
     * @param [in] endTime 收弧时间(ms)
     * @return 错误码
     */
    errno_t WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

获取焊接工艺曲线参数
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取焊接工艺曲线参数
     * @param [in] id 焊接工艺编号(1-99)
     * @param [out] startCurrent 起弧电流(A)
     * @param [out] startVoltage 起弧电压(V)
     * @param [out] startTime 起弧时间(ms)
     * @param [out] weldCurrent 焊接电流(A)
     * @param [out] weldVoltage 焊接电压(V)
     * @param [out] endCurrent 收弧电流(A)
     * @param [out] endVoltage 收弧电压(V)
     * @param [out] endTime 收弧时间(ms)
     * @return 错误码
     */
    errno_t WeldingGetProcessParam(int id, double& startCurrent, double& startVoltage, double& startTime, double& weldCurrent, double& weldVoltage, double& endCurrent, double& endVoltage, double& endTime);

设置焊接电流与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电流与输出模拟量对应关系
    * @param [in] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [in] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [in] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

设置焊接电压与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电压与输出模拟量对应关系
    * @param [in] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [in] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [in] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

获取焊接电流与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取焊接电流与输出模拟量对应关系
    * @param [out] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [out] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [out] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingGetCurrentRelation(double *currentMin, double *currentMax, double *outputVoltageMin, double *outputVoltageMax);

获取焊接电压与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取焊接电压与输出模拟量对应关系
    * @param [out] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [out] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [out] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingGetVoltageRelation(double *weldVoltageMin, double *weldVoltageMax, double *outputVoltageMin, double *outputVoltageMax);

设置焊接电流
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电流
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] current 焊接电流值(A)
    * @param [in] AOIndex 焊接电流控制箱模拟量输出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 错误码
    */
    errno_t WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

设置焊接电压
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电压
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] voltage 焊接电压值(A)
    * @param [in] AOIndex 焊接电压控制箱模拟量输出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 错误码
    */
    errno_t WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

设置摆动参数
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief 设置摆动参数
     * @param [in] weaveNum 摆焊参数配置编号
     * @param [in] weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
     * @param [in] weaveFrequency 摆动频率(Hz)
     * @param [in] weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
     * @param [in] weaveRange 摆动幅度(mm)
     * @param [in] weaveLeftRange 垂直三角摆动左弦长度(mm)
     * @param [in] weaveRightRange 垂直三角摆动右弦长度(mm)
     * @param [in] additionalStayTime 垂直三角摆动垂三角点停留时间(mm)
     * @param [in] weaveLeftStayTime 摆动左停留时间(ms)
     * @param [in] weaveRightStayTime 摆动右停留时间(ms)
     * @param [in] weaveCircleRadio 圆形摆动-回调比率(0-100%)
     * @param [in] weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
     * @param [in] weaveYawAngle 摆动方向方位角(绕摆动Z轴旋转)，单位°
     * @param [in] weaveRotAngle 摆动方向侧倾角(绕摆动X轴偏转)，单位°
     * @return 错误码
     */
      errno_t WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle = 0);

设置焊接参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSetWeldParam(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000);
      robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333);
      double startCurrent = 0;
      double startVoltage = 0;
      double startTime = 0;
      double weldCurrent = 0;
      double weldVoltage = 0;
      double endCurrent = 0;
      double endVoltage = 0;
      double endTime = 0;
      robot.WeldingGetProcessParam(1, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
      cout << "the Num 1 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
      robot.WeldingGetProcessParam(2, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
      cout << "the Num 2 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
      rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
      cout << "WeldingSetCurrentRelation rtn is: " << rtn << endl;
      rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
      cout << "WeldingSetVoltageRelation rtn is: " << rtn << endl;
      double current_min = 0;
      double current_max = 0;
      double vol_min = 0;
      double vol_max = 0;
      double output_vmin = 0;
      double output_vmax = 0;
      int curIndex = 0;
      int volIndex = 0;
      rtn = robot.WeldingGetCurrentRelation(&current_min, &current_max, &output_vmin, &output_vmax, &curIndex);
      cout << "WeldingGetCurrentRelation rtn is: " << rtn << endl;
      cout << "current min " << current_min << " current max " << current_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
      rtn = robot.WeldingGetVoltageRelation(&vol_min, &vol_max, &output_vmin, &output_vmax, &volIndex);
      cout << "WeldingGetVoltageRelation rtn is: " << rtn << endl;
      cout << "vol min " << vol_min << " vol max " << vol_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
      rtn = robot.WeldingSetCurrent(1, 100, 0, 0);
      cout << "WeldingSetCurrent rtn is: " << rtn << endl;
      this_thread::sleep_for(chrono::seconds(3));
      rtn = robot.WeldingSetVoltage(1, 10, 0, 0);
      cout << "WeldingSetVoltage rtn is: " << rtn << endl;
      rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
      cout << "rtn is: " << rtn << endl;
      robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);
      rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
      printf("WeldingSetCheckArcInterruptionParam  %d\n", rtn);
      rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
      printf("WeldingSetReWeldAfterBreakOffParam  %d\n", rtn);
      int enable = 0;
      double length = 0;
      double velocity = 0;
      int moveType = 0;
      int checkEnable = 0;
      int arcInterruptTimeLength = 0;
      rtn = robot.WeldingGetCheckArcInterruptionParam(&checkEnable, &arcInterruptTimeLength);
      printf("WeldingGetCheckArcInterruptionParam checkEnable %d  arcInterruptTimeLength %d\n", checkEnable, arcInterruptTimeLength);
      rtn = robot.WeldingGetReWeldAfterBreakOffParam(&enable, &length, &velocity, &moveType);
      printf("WeldingGetReWeldAfterBreakOffParam enable = %d, length = %lf, velocity = %lf, moveType = %d\n", enable, length, velocity, moveType);
      robot.SetWeldMachineCtrlModeExtDoNum(17);
      for (int i = 0; i < 5; i++)
      {
        robot.SetWeldMachineCtrlMode(0);
        robot.Sleep(1000);
        robot.SetWeldMachineCtrlMode(1);
        robot.Sleep(1000);
      }
      robot.CloseRPC();
      return 0;
    }

即时设置摆动参数
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 即时设置摆动参数
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    * @param [in] weaveFrequency 摆动频率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
    * @param [in] weaveRange 摆动幅度(mm)
    * @param [in] weaveLeftStayTime 摆动左停留时间(ms)
    * @param [in] weaveRightStayTime 摆动右停留时间(ms)
    * @param [in] weaveCircleRadio 圆形摆动-回调比率(0-100%)
    * @param [in] weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
    * @return 错误码
    */
    errno_t WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

设置机器人焊接电弧意外中断检测参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 设置机器人焊接电弧意外中断检测参数
	 * @param [in] checkEnable 是否使能检测；0-不使能；1-使能
	 * @param [in] arcInterruptTimeLength 电弧中断确认时长(ms)
	 * @return 错误码
    */
	errno_t WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

获取机器人焊接电弧意外中断检测参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 获取机器人焊接电弧意外中断检测参数
	 * @param [out] checkEnable 是否使能检测；0-不使能；1-使能
	 * @param [out] arcInterruptTimeLength 电弧中断确认时长(ms)
	 * @return 错误码
    */
	errno_t WeldingGetCheckArcInterruptionParam(int* checkEnable, int* arcInterruptTimeLength);

设置机器人焊接中断恢复参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 设置机器人焊接中断恢复参数
	 * @param [in] enable 是否使能焊接中断恢复
	 * @param [in] length 焊缝重叠距离(mm)
	 * @param [in] velocity 机器人回到再起弧点速度百分比(0-100)
	 * @param [in] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
	 * @return 错误码
    */
	errno_t WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);
    
获取机器人焊接中断恢复参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 获取机器人焊接中断恢复参数
	 * @param [out] enable 是否使能焊接中断恢复
	 * @param [out] length 焊缝重叠距离(mm)
	 * @param [out] velocity 机器人回到再起弧点速度百分比(0-100)
	 * @param [out] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
	 * @return 错误码
    */
	errno_t WeldingGetReWeldAfterBreakOffParam(int* enable, double* length, double* velocity, int* moveType);

设置焊机控制模式扩展DO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊机控制模式扩展DO端口
    * @param DONum 焊机控制模式DO端口(0-127)
    * @return 错误码
    */
    errno_t SetWeldMachineCtrlModeExtDoNum(int DONum);

设置焊机控制模式
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊机控制模式
    * @param [in] mode 焊机控制模式;0-直流一元模式；1-脉冲一元模式；2-JOB模式；3-近控模式；4-分别模式；5-CC/CV模式；6-TIG；7-CMT
    * @param [in] ioType 控制类型；0-控制箱IO;1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    * @return 错误码
    */
    errno_t SetWeldMachineCtrlMode(int mode, int ioType = 1);

焊接开始
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接开始
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 起弧超时时间
    * @return 错误码
    */
    errno_t ARCStart(int ioType, int arcNum, int timeout);

焊接结束
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接结束
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 熄弧超时时间
    * @return 错误码
    */
    errno_t ARCEnd(int ioType, int arcNum, int timeout);

摆动开始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 摆动开始
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    errno_t WeaveStart(int weaveNum);

摆动结束
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 摆动结束
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    errno_t WeaveEnd(int weaveNum);

正向送丝
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 正向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    errno_t SetForwardWireFeed(int ioType, int wireFeed);

反向送丝
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 反向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    errno_t SetReverseWireFeed(int ioType, int wireFeed);

送气
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 送气
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] airControl 送气控制  0-停止送气；1-送气
    * @return 错误码
    */
    errno_t SetAspirated(int ioType, int airControl);

设置机器人焊接中断后恢复焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 设置机器人焊接中断后恢复焊接
	 * @return 错误码
    */
	errno_t WeldingStartReWeldAfterBreakOff();

设置机器人焊接中断后退出焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 设置机器人焊接中断后退出焊接
	 * @return 错误码
	 */
	errno_t WeldingAbortWeldAfterBreakOff();

机器人焊接控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestWelding(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SetForwardWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetForwardWireFeed(0, 0);
      robot.SetReverseWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetReverseWireFeed(0, 0);
      robot.SetAspirated(0, 1);
      robot.Sleep(1000);
      robot.SetAspirated(0, 0);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.WeaveStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.ARCEnd(1, 0, 10000);
      robot.WeaveEnd(0);
      robot.WeldingStartReWeldAfterBreakOff();
      robot.WeldingAbortWeldAfterBreakOff();
      robot.CloseRPC();
      return 0;
    }


段焊开始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 段焊开始
    * @param [in] startDesePos 起始点笛卡尔位置
    * @param [in] endDesePos 结束点笛卡尔位姿
    * @param [in] startJPos 起始点关节位姿
    * @param [in] endJPos 结束点关节位姿
    * @param [in] weldLength 焊接段长度(mm)
    * @param [in] noWeldLength 非焊接段长度(mm)
    * @param [in] weldIOType 焊接IO类型(0-控制箱IO；1-扩展IO)
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] weldTimeout 起/收弧超时时间
    * @param [in] isWeave 是否摆动
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] search 0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 错误码
    */
    errno_t SegmentWeldStart(DescPose *startDesePos, DescPose *endDesePos, JointPos *startJPos, JointPos *endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

机器人段焊代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    int TestSegWeld(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      rtn = robot.SegmentWeldStart(&p1Desc, &p2Desc, &p1Joint, &p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      printf("SegmentWeldStart rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }


仿真摆动开始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 仿真摆动开始
     * @param [in] weaveNum 摆动参数编号
     * @return 错误码
     */
    errno_t WeaveStartSim(int weaveNum);

仿真摆动结束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 仿真摆动结束
     * @param [in] weaveNum 摆动参数编号
     * @return 错误码
     */
    errno_t WeaveEndSim(int weaveNum);

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 开始轨迹检测预警(不运动)
     * @param [in] weaveNum  摆动参数编号
     * @return 错误码
     */
    errno_t WeaveInspectStart(int weaveNum);

结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 结束轨迹检测预警(不运动)
     * @param [in] weaveNum  摆动参数编号
     * @return 错误码
     */
    errno_t WeaveInspectEnd(int weaveNum);

摆动渐变开始
+++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief 摆动渐变开始
     * @param [in] weaveChangeFlag 1-变摆动参数；2-变摆动参数+焊接速度
     * @param [in] weaveNum 摆动编号 
     * @param [in] velStart 焊接开始速度，(cm/min)
     * @param [in] velEnd 焊接结束速度，(cm/min)
     * @return 错误码
     */
     errno_t WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

机器人摆动渐变焊接代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    int TestWeave(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveStartSim(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveEndSim(0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveInspectStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveInspectEnd(0);
      robot.WeldingSetVoltage(1, 19, 0, 0);
      robot.WeldingSetCurrent(1, 190, 0, 0);
      robot.MoveL(&p1Joint, &p1Desc, 1, 1, 100, 100, 50, -1, &exaxisPos, 0, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.WeaveStart(0);
      robot.WeaveChangeStart(1, 0, 50, 30);
      robot.MoveL(&p2Joint, &p2Desc, 1, 1, 100, 100, 1, -1, &exaxisPos, 0, 0, &offdese);
      robot.WeaveChangeEnd();
      robot.WeaveEnd(0);
      robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.ARCEnd(1, 0, 10000);
      robot.CloseRPC();
      return 0;
    }

摆动渐变结束
+++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  摆动渐变结束
	 * @return  错误码
	 */
    errno_t WeaveChangeEnd();

扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机气体检测信号
     * @param [in] DONum 气体检测信号扩展DO编号
     * @return 错误码
     */
    errno_t SetAirControlExtDoNum(int DONum);

扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机起弧信号
     * @param [in] DONum 焊机起弧信号扩展DO编号
     * @return 错误码
     */
    errno_t SetArcStartExtDoNum(int DONum);

扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机反向送丝信号
     * @param [in] DONum 反向送丝信号扩展DO编号
     * @return 错误码
     */
    errno_t SetWireReverseFeedExtDoNum(int DONum);

扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机正向送丝信号
     * @param [in] DONum 正向送丝信号扩展DO编号
     * @return 错误码
     */
    errno_t SetWireForwardFeedExtDoNum(int DONum);

扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机起弧成功信号
     * @param [in] DINum 起弧成功信号扩展DI编号
     * @return 错误码
     */
    errno_t SetArcDoneExtDiNum(int DINum);

扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊机准备信号
     * @param [in] DINum 焊机准备信号扩展DI编号
     * @return 错误码
     */
    errno_t SetWeldReadyExtDiNum(int DINum);

扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 扩展IO-配置焊接中断恢复信号
     * @param [in] reWeldDINum 焊接中断后恢复焊接信号扩展DI编号
     * @param [in] abortWeldDINum 焊接中断后退出焊接信号扩展DI编号
     * @return 错误码
     */
    errno_t SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

设置扩展IO焊接信号代码示例
+++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestExtDIConfig(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SetArcStartExtDoNum(10);
      robot.SetAirControlExtDoNum(20);
      robot.SetWireForwardFeedExtDoNum(30);
      robot.SetWireReverseFeedExtDoNum(40);
      robot.SetWeldReadyExtDiNum(50);
      robot.SetArcDoneExtDiNum(60);
      robot.SetExtDIWeldBreakOffRecover(70, 80);
      robot.SetWireSearchExtDIONum(0, 1);
      robot.CloseRPC();
      return 0;
    }

电弧跟踪控制
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

      /**
      * @brief  电弧跟踪控制
   	  * @param  [in] flag 开关，0-关；1-开
  	  * @param  [in] dalayTime 滞后时间，单位ms
  	  * @param  [in] isLeftRight 左右偏差补偿
  	  * @param  [in] klr 左右调节系数(灵敏度);
  	  * @param  [in] tStartLr 左右开始补偿时间cyc
  	  * @param  [in] stepMaxLr 左右每次最大补偿量 mm
  	  * @param  [in] sumMaxLr 左右总计最大补偿量 mm
  	  * @param  [in] isUpLow 上下偏差补偿
  	  * @param  [in] kud 上下调节系数(灵敏度);
  	  * @param  [in] tStartUd 上下开始补偿时间cyc
  	  * @param  [in] stepMaxUd 上下每次最大补偿量 mm
  	  * @param  [in] sumMaxUd 上下总计最大补偿量
  	  * @param  [in] axisSelect 上下坐标系选择，0-摆动；1-工具；2-基座
  	  * @param  [in] referenceType 上下基准电流设定方式，0-反馈；1-常数
  	  * @param  [in] referSampleStartUd 上下基准电流采样开始计数(反馈);，cyc
  	  * @param  [in] referSampleCountUd 上下基准电流采样循环计数(反馈);，cyc
  	  * @param  [in] referenceCurrent 上下基准电流mA
  	  * @param  [in] offsetType 偏置跟踪类型，0-不偏置；1-采样；2-百分比
  	  * @param  [in] offsetParameter 偏置参数；采样(偏置采样开始时间，默认采一周期)；百分比(偏置百分比(-100 ~ 100))
  	  * @return  错误码
  	  */
	 errno_t ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType = 0, int offsetParameter = 0);

设置电弧跟踪输入信号端口
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置电弧跟踪输入信号端口
      * @param  [in] channel 电弧跟踪AI通带选择,[0-3]
      * @return  错误码
      */
     errno_t ArcWeldTraceExtAIChannelConfig(int channel);


电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 电弧追踪 + 多层多道补偿开启
    * @return 错误码
    */
    errno_t ArcWeldTraceReplayStart();

电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 电弧追踪 + 多层多道补偿关闭
    * @return 错误码
    */
    errno_t ArcWeldTraceReplayEnd();

偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 偏移量坐标变化-多层多道焊
    * @return 错误码
    */
    errno_t MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, DescPose& offset);

多层多道焊电弧跟踪代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestArcWeldTrace(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      JointPos mulitilineorigin1_joint(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
      DescPose mulitilineorigin1_desc(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);
      DescTran mulitilineX1_desc;
      mulitilineX1_desc.x = -677.556;
      mulitilineX1_desc.y = 211.949;
      mulitilineX1_desc.z = -1.206;
      DescTran mulitilineZ1_desc;
      mulitilineZ1_desc.x = -677.564;
      mulitilineZ1_desc.y = 190.956;
      mulitilineZ1_desc.z = 19.817;
      JointPos mulitilinesafe_joint(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
      DescPose mulitilinesafe_desc(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
      JointPos mulitilineorigin2_joint(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
      DescPose mulitilineorigin2_desc(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);
      DescTran mulitilineX2_desc;
      mulitilineX2_desc.x = -563.965;
      mulitilineX2_desc.y = 220.355;
      mulitilineX2_desc.z = -0.680;
      DescTran mulitilineZ2_desc;
      mulitilineZ2_desc.x = -563.968;
      mulitilineZ2_desc.y = 215.362;
      mulitilineZ2_desc.z = 4.331;
      ExaxisPos epos(0, 0, 0, 0);
      DescPose offset(0, 0, 0, 0, 0, 0);
      robot.Sleep(10);
      int error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.WeaveStart(0);
      printf("WeaveStart return: %d\n", error);
      error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.WeaveEnd(0);
      printf("WeaveEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("ArcWeldTraceReplayStart return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 3000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      robot.CloseRPC();
      return 0;
    }

电弧跟踪焊机电流反馈AI通道选择
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 电弧跟踪焊机电流反馈AI通道选择
     * @param [in]  channel 通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1
     * @return 错误码
     */
     errno_t ArcWeldTraceAIChannelCurrent(int channel);

电弧跟踪焊机电压反馈AI通道选择
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 电弧跟踪焊机电压反馈AI通道选择
     * @param [in]  channel 通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1
     * @return 错误码
     */
     errno_t ArcWeldTraceAIChannelVoltage(int channel);

电弧跟踪焊机电流反馈转换参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
      * @brief 电弧跟踪焊机电流反馈转换参数
      * @param [in] AILow AI通道下限，默认值0V，范围[0-10V]
      * @param [in] AIHigh AI通道上限，默认值10V，范围[0-10V]
      * @param [in] currentLow AI通道下限对应焊机电流值，默认值0V，范围[0-200V]
      * @param [in] currentHigh AI通道上限对应焊机电流值，默认值100V，范围[0-200V]
      * @return 错误码
      */
     errno_t ArcWeldTraceCurrentPara(float AILow, float AIHigh, float currentLow, float currentHigh);

电弧跟踪焊机电压反馈转换参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
    * @brief 电弧跟踪焊机电压反馈转换参数
    * @param [in] AILow AI通道下限，默认值0V，范围[0-10V]
    * @param [in] AIHigh AI通道上限，默认值10V，范围[0-10V]
    * @param [in] voltageLow AI通道下限对应焊机电压值，默认值0V，范围[0-200V]
    * @param [in] voltageHigh AI通道上限对应焊机电压值，默认值100V，范围[0-200V]
    * @return 错误码
    */
    errno_t ArcWeldTraceVoltagePara(float AILow, float AIHigh, float voltageLow, float voltageHigh);

电弧跟踪代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int WeldTraceControlWithCtrlBoxAI(FRRobot* robot)
    {
      DescPose startdescPose = { -473.86, 257.879, -20.849, -37.317, -42.021, 2.543 };
      JointPos startjointPos = { -43.487, -76.526, 95.568, -104.445, -89.356, 3.72 };

      DescPose enddescPose = { -499.844, 141.225, 7.72, -34.856, -40.17, 13.13 };
      JointPos endjointPos = { -31.305, -82.998, 99.401, -104.426, -89.35, 3.696 };

      DescPose safedescPose = { -504.043, 275.181, 40.908, -28.002, -42.025, -14.044 };
      JointPos safejointPos = { -39.078, -76.732, 87.227, -99.47, -94.301, 18.714 };

      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);

      robot->WeldingSetVoltage(0, 25, 1, 0);// ----设置电压
      robot->WeldingSetCurrent(0, 260, 0, 0);// ----设置电流

      int rtn = robot->ArcWeldTraceAIChannelCurrent(4);
      cout << "ArcWeldTraceAIChannelCurrent rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceAIChannelVoltage(5);
      cout << "ArcWeldTraceAIChannelVoltage rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceCurrentPara(0, 5, 0, 500);
      cout << "ArcWeldTraceCurrentPara rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceVoltagePara(1.018, 10, 0, 50);
      cout << "ArcWeldTraceVoltagePara rtn is " << rtn << endl;
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      return 0;
    }


设置焊丝寻位扩展IO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊丝寻位扩展IO端口
    * @param searchDoneDINum 焊丝寻位成功DO端口(0-127)
    * @param searchStartDONum 焊丝寻位启停控制DO端口(0-127)
    * @return 错误码
    */
    errno_t SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

示例程序
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void TestUDPWireSearch(FRRobot* robot)
    {
    robot->ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
    robot->ExtDevLoadUDPDriver();

    robot->SetWireSearchExtDIONum(0, 0);

    int rtn0, rtn1, rtn2 = 0;
    ExaxisPos exaxisPos = { 0.0, 0.0, 0.0, 0.0 };
    DescPose offdese = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
    
    DescPose descStart = { -158.767, -510.596, 271.709, -179.427, -0.745, -137.349 };
    JointPos jointStart = { 61.667, -79.848, 108.639, -119.682, -89.700, -70.985 };
    
    DescPose descEnd = { 0.332, -516.427, 270.688, 178.165, 0.017, -119.989 };
    JointPos jointEnd = { 79.021, -81.839, 110.752, -118.298, -91.729, -70.981 };

    robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    
    DescPose descREF0A = { -66.106, -560.746, 270.381, 176.479, -0.126, -126.745 };
    JointPos jointREF0A = { 73.531, -75.588, 102.941, -116.250, -93.347, -69.689 };
    
    DescPose descREF0B = { -66.109, -528.440, 270.407, 176.479, -0.129, -126.744 };
    JointPos jointREF0B = { 72.534, -79.625, 108.046, -117.379, -93.366, -70.687 };
    
    DescPose descREF1A = { 72.975, -473.242, 270.399, 176.479, -0.129, -126.744 };
    JointPos jointREF1A = { 87.169, -86.509, 115.710, -117.341, -92.993, -56.034 };
    
    DescPose descREF1B = { 31.355, -473.238, 270.405, 176.480, -0.130, -126.745 };
    JointPos jointREF1B = { 82.117, -87.146, 116.470, -117.737, -93.145, -61.090 };

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
    rtn1 = robot->WireSearchWait("REF0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
    rtn1 = robot->WireSearchWait("REF1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
    rtn1 = robot->WireSearchWait("RES0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
    rtn1 = robot->WireSearchWait("RES1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
    vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
    int offectFlag = 0;
    DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
    rtn0 = robot->GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
    robot->PointsOffsetEnable(0, &offectPos);
    robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->PointsOffsetDisable();
    }

焊丝寻位开始
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  焊丝寻位开始
    * @param  [in] refPos  1-基准点 0-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；0-示教点寻位
    * @return  错误码
    */
     errno_t WireSearchStart(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

焊丝寻位结束
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  焊丝寻位结束
      * @param  [in] refPos  1-基准点 2-接触点
      * @param  [in] searchVel   寻位速度 %
      * @param  [in] searchDis  寻位距离 mm
      * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
      * @param  [in] autoBackVel  自动返回速度 %
      * @param  [in] autoBackDis  自动返回距离 mm
      * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
      * @return  错误码
      */
     errno_t WireSearchEnd(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

计算焊丝寻位偏移量
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  计算焊丝寻位偏移量
      * @param  [in] seamType  焊缝类型
      * @param  [in] method   计算方法
      * @param  [in] varNameRef 基准点1-6，“#”表示无点变量
      * @param  [in] varNameRes 接触点1-6，“#”表示无点变量
      * @param  [out] offectFlag 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
      * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
      * @return  错误码
      */
     errno_t GetWireSearchOffset(int seamType, int method, std::vector<std::string> varNameRef, std::vector<std::string> varNameRes, int& offectFlag, DescPose& offect);

等待焊丝寻位完成
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  等待焊丝寻位完成
      * @return  错误码
      */
     errno_t WireSearchWait(std::string varName);

焊丝寻位接触点写入数据库
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  焊丝寻位接触点写入数据库
      * @param  [in] varName  接触点名称 “RES0” ~ “RES99”
      * @param  [in] pos  接触点数据[x, y, x, a, b, c]
      * @return  错误码
      */
     errno_t SetPointToDatabase(std::string varName, DescPose pos);

机器人焊丝寻位代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestWireSearch(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose toolCoord(0, 0, 200, 0, 0, 0);
      robot.SetToolCoord(1, &toolCoord, 0, 0, 1, 0);
      DescPose wobjCoord(0, 0, 0, 0, 0, 0);
      robot.SetWObjCoord(1, &wobjCoord, 0);
      int rtn0, rtn1, rtn2 = 0;
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      DescPose descStart = { 216.543, 445.175, 93.465, 179.683, 1.757, -112.641 };
      JointPos jointStart = { -128.345, -86.660, 114.679, -119.625, -89.219, 74.303 };
      DescPose descEnd = { 111.143, 523.384, 87.659, 179.703, 1.835, -97.750 };
      JointPos jointEnd = { -113.454, -81.060, 109.328, -119.954, -89.218, 74.302 };
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      DescPose descREF0A = { 142.135, 367.604, 86.523, 179.728, 1.922, -111.089 };
      JointPos jointREF0A = { -126.794, -100.834, 128.922, -119.864, -89.218, 74.302 };
      DescPose descREF0B = { 254.633, 463.125, 72.604, 179.845, 2.341, -114.704 };
      JointPos jointREF0B = { -130.413, -81.093, 112.044, -123.163, -89.217, 74.303 };
      DescPose descREF1A = { 92.556, 485.259, 47.476, -179.932, 3.130, -97.512 };
      JointPos jointREF1A = { -113.231, -83.815, 119.877, -129.092, -89.217, 74.303 };
      DescPose descREF1B = { 203.103, 583.836, 63.909, 179.991, 2.854, -103.372 };
      JointPos jointREF1B = { -119.088, -69.676, 98.692, -121.761, -89.219, 74.303 };
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
      rtn1 = robot.WireSearchWait("REF0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
      rtn1 = robot.WireSearchWait("REF1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
      rtn1 = robot.WireSearchWait("RES0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起点
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向点
      rtn1 = robot.WireSearchWait("RES1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
      vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
      int offectFlag = 0;
      DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
      rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
      robot.PointsOffsetEnable(0, &offectPos);
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);
      robot.PointsOffsetDisable();
      robot.CloseRPC();
      return 0;

设置焊接电压渐变开始
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
    * @brief 设置焊接电压渐变开始
    * @param [in] IOType 控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    * @param [in] voltageStart 起始焊接电压(V)
    * @param [in] voltageEnd 终止焊接电压(V)
    * @param [in] AOIndex 控制箱AO端口号(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 错误码
    */
    errno_t WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

设置焊接电压渐变结束
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 设置焊接电压渐变结束
      * @return 错误码
      */
     errno_t WeldingSetVoltageGradualChangeEnd();

设置焊接电流渐变开始
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 设置焊接电流渐变开始
      * @param [in] IOType 控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
      * @param [in] voltageStart 起始焊接电流(A)
      * @param [in] voltageEnd 终止焊接电流(A)
      * @param [in] AOIndex 控制箱AO端口号(0-1)
      * @param [in] blend 是否平滑 0-不平滑；1-平滑
      * @return 错误码
      */
     errno_t WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

设置焊接电流渐变结束
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置焊接电流渐变结束
     * @return 错误码
     */
    errno_t WeldingSetCurrentGradualChangeEnd();
    
机器人焊接电流电压渐变代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int WeldparamChange(FRRobot* robot)
    {
      DescPose startdescPose = { -484.707, 276.996, -14.013, -37.657, -40.508, -1.548 };
      JointPos startjointPos = { -45.421, -75.673, 93.627, -104.302, -87.938, 6.005 };
      
      DescPose enddescPose = { -508.767, 137.109, -13.966, -37.639, -40.508, -1.559 };
      JointPos endjointPos = { -32.768, -80.947, 100.254, -106.201, -87.201, 18.648 };

      DescPose safedescPose = { -484.709, 294.436, 13.621, -37.660, -40.508, -1.545 };
      JointPos safejointPos = { -46.604, -75.410, 89.109, -100.003, -88.012, 4.823 };
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      int rtn = robot->WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
      cout << "WeldingSetCurrentGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
      cout << "WeldingSetVoltageGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      
      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->WeaveChangeStart(2, 1, 24, 36);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveChangeEnd();
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      robot->WeldingSetCurrentGradualChangeEnd();
      robot->WeldingSetVoltageGradualChangeEnd();
      return 0;
    }

设置自定义摆动参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置自定义摆动参数
    * @param [in] id 自定义摆动编号：0-2
    * @param [in] pointNum 摆动点位个数 0-10
    * @param [in] point 移动端点数据x,y,z
    * @param [in] stayTime 摆动停留时间ms
    * @param [in] frequency 摆动频率 Hz
    * @param [in] incStayType 等待模式：0-周期不包含等待时间；1-周期包含等待时间
    * @param [in] stationary 摆动位置等待：0-等待时间内继续运动；1-等待时间内位置静止
    * @return 错误码
    */
    errno_t CustomWeaveSetPara(int id, int pointNum, DescTran point[10], double stayTime[10], double frequency, int incStayType, int stationary);
                
获取自定义摆动参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取自定义摆动参数
    * @param [in] id 自定义摆动编号：0-2
    * @param [out] pointNum 摆动点位个数 0-10
    * @param [out] point 移动端点数据x,y,z
    * @param [out] stayTime 摆动停留时间ms
    * @param [out] frequency 摆动频率 Hz
    * @param [out] incStayType 等待模式：0-周期不包含等待时间；1-周期包含等待时间
    * @param [out] stationary 摆动位置等待：0-等待时间内继续运动；1-等待时间内位置静止
    * @return 错误码
    */
    errno_t CustomWeaveGetPara(int id, int& pointNum, DescTran point[10], double stayTime[10], double& frequency, int& incStayType, int& stationary);
                    
自定义摆动参数代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    int TestCustomWeaveSetPara()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescTran point[10] = {}; 
      point[0].x = -3;
      point[0].y = -3;
      point[0].z = 0;
      point[1].x = -6;
      point[1].y = 0;
      point[1].z = 0;
      point[2].x = -3;
      point[2].y = 3;
      point[2].z = 0;
      point[3].x = 0;
      point[3].y = 0;
      point[3].z = 0;
      double stayTime[10] = { 0,0,0,0,0,0,0,0,0,0 };
      rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0);
      printf("CustomWeaveSetPara rtn is %d\n", rtn);
      robot.Sleep(1000);
      int pointNum = 0;
      double frequency;
      int incStayType;
      int stationary;
      robot.CustomWeaveGetPara(2, pointNum, point, stayTime, frequency, incStayType, stationary);
      printf("pointNum is %d\n", pointNum);
      for (int i = 0; i < pointNum; i++)
      {
        printf("point %d, point x y z %f %f %f\n", i, point[i].x, point[i].y, point[i].z);
      }
      printf("fre is %f, stay is %d %d \n", frequency, incStayType, stationary);
      robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
      DescPose desc_p1 = { -288.650, 367.807, 288.404, 0.000, -0.001, 0.001 };
      DescPose desc_p2 = { -431.714, 367.815, 288.415, 0.001, 0.001, 0.000 };
      DescPose desc_p3 = { -348.666, 427.798, 288.404, -0.000, -0.000, 0.001 };
      JointPos j1 = { 140.656, -84.560, -91.707, -93.734, 90.000, 50.655 };
      JointPos j2 = { 149.873, -98.298, -77.599, -94.103, 90.000, 59.873 };
      JointPos j3 = { 139.773, -96.173, -80.014, -93.814, 90.000, 49.772 };
      ExaxisPos epos = {};
      DescPose offset_pos = {};
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.Circle(&j3, &desc_p3, 3, 0, 100, 100, &epos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 10, -1, &offset_pos);
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveC(&j3, &desc_p3, 3, 0, 100, 100, &epos, 0, &offset_pos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 0, &offset_pos, 10, -1); 
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveL(&j2, &desc_p2, 3, 0, 100, 100, 10, -1, &epos, 0, 0, &offset_pos, 0, 100);
      robot.WeaveEnd(0);
      robot.CloseRPC();
    }