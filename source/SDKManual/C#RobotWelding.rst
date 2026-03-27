机器人焊接
=============

.. toctree:: 
    :maxdepth: 5

设置焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置焊接工艺曲线参数
    * @param  [in] id 焊接工艺编号(1-99)
    * @param  [in] startCurrent 起弧电流(A)
    * @param  [in] startVoltage 起弧电压(V)
    * @param  [in] startTime 起弧时间(ms)
    * @param  [in] weldCurrent 焊接电流(A)
    * @param  [in] weldVoltage 焊接电压(V)
    * @param  [in] endCurrent 收弧电流(A)
    * @param  [in] endVoltage 收弧电压(V)
    * @param  [in] endTime 收弧时间(ms)
    * @return  错误码
    */
    int WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

获取焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取焊接工艺曲线参数
    * @param  [in] id 焊接工艺编号(1-99)
    * @param  [out] startCurrent 起弧电流(A)
    * @param  [out] startVoltage 起弧电压(V)
    * @param  [out] startTime 起弧时间(ms)
    * @param  [out] weldCurrent 焊接电流(A)
    * @param  [out] weldVoltage 焊接电压(V)
    * @param  [out] endCurrent 收弧电流(A)
    * @param  [out] endVoltage 收弧电压(V)
    * @param  [out] endTime 收弧时间(ms)
    * @return  错误码
    */
    int WeldingGetProcessParam(int id, ref double startCurrent, ref double startVoltage, ref double startTime, ref double weldCurrent, ref double weldVoltage, ref double endCurrent, ref double endVoltage, ref double endTime);

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电流与输出模拟量对应关系
    * @param [in] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [in] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [in] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电压与输出模拟量对应关系
    * @param [in] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [in] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [in] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取焊接电流与输出模拟量对应关系
    * @param [out] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [out] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [out] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingGetCurrentRelation(ref double currentMin, ref double currentMax, ref double outputVoltageMin, ref double outputVoltageMax);

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取焊接电压与输出模拟量对应关系
    * @param [out] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [out] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [out] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingGetVoltageRelation(ref double weldVoltageMin, ref double weldVoltageMax, ref double outputVoltageMin, ref double outputVoltageMax);

设置焊接电流
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电流
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] current 焊接电流值(A)
    * @param [in] AOIndex 焊接电流控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex);

设置焊接电压
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电压
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] voltage 焊接电压值(A)
    * @param [in] AOIndex 焊接电压控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex);

设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    * @return 错误码 
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle=0);

设置焊接参数代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
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

        robot.WeldingGetProcessParam(1, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 1 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);
        robot.WeldingGetProcessParam(2, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 2 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);

        int rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
        Console.WriteLine("WeldingSetCurrentRelation rtn is: " + rtn);

        rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
        Console.WriteLine("WeldingSetVoltageRelation rtn is: " + rtn);

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;
        int curIndex = 0;
        int volIndex = 0;
        rtn = robot.WeldingGetCurrentRelation(ref current_min, ref current_max, ref output_vmin, ref output_vmax, ref curIndex);
        Console.WriteLine("WeldingGetCurrentRelation rtn is: " + rtn);
        Console.WriteLine("current min " + current_min + " current max " + current_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingGetVoltageRelation(ref vol_min, ref vol_max, ref output_vmin, ref output_vmax, ref volIndex);
        Console.WriteLine("WeldingGetVoltageRelation rtn is: " + rtn);
        Console.WriteLine("vol min " + vol_min + " vol max " + vol_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingSetCurrent(1, 100, 0, 0);
        Console.WriteLine("WeldingSetCurrent rtn is: " + rtn);

        System.Threading.Thread.Sleep(3000);

        rtn = robot.WeldingSetVoltage(1, 10, 0, 0);
        Console.WriteLine("WeldingSetVoltage rtn is: " + rtn);

        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
        Console.WriteLine("rtn is: " + rtn);

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);

        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        Console.WriteLine("WeldingSetCheckArcInterruptionParam    " + rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        Console.WriteLine("WeldingSetReWeldAfterBreakOffParam    " + rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(ref checkEnable, ref arcInterruptTimeLength);
        Console.WriteLine("WeldingGetCheckArcInterruptionParam  checkEnable  " + checkEnable + "   arcInterruptTimeLength  " + arcInterruptTimeLength);
        rtn = robot.WeldingGetReWeldAfterBreakOffParam(ref enable, ref length, ref velocity, ref moveType);
        Console.WriteLine("WeldingGetReWeldAfterBreakOffParam  enable = " + enable + ", length = " + length + ", velocity = " + velocity + ", moveType = " + moveType);

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(1000);
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(1000);
        }

    }

即时设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

设置机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接电弧意外中断检测参数
    * @param [in] checkEnable 是否使能检测；0-不使能；1-使能
    * @param [in] arcInterruptTimeLength 电弧中断确认时长(ms)
    * @return 错误码
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength)

获取机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人焊接电弧意外中断检测参数
    * @param [out] checkEnable 是否使能检测；0-不使能；1-使能
    * @param [out] arcInterruptTimeLength 电弧中断确认时长(ms)
    * @return 错误码
    */
    int WeldingGetCheckArcInterruptionParam(ref int checkEnable, ref int arcInterruptTimeLength)

设置机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断恢复参数
    * @param[in] enable 是否使能焊接中断恢复
    * @param[in] length 焊缝重叠距离(mm)
    * @param[in] velocity 机器人回到再起弧点速度百分比(0-100)
    * @param[in] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
    * @return 错误码
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType)

获取机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人焊接中断恢复参数
    * @param [out] enable 是否使能焊接中断恢复
    * @param [out] length 焊缝重叠距离(mm)
    * @param [out] velocity 机器人回到再起弧点速度百分比(0-100)
    * @param [out] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
    * @return 错误码
    */
    int WeldingGetReWeldAfterBreakOffParam(ref int enable, ref double length, ref double velocity, ref int moveType)

设置焊机控制模式扩展DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊机控制模式扩展DO端口
    * @param DONum 焊机控制模式DO端口(0-127)
    * @return 错误码
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

设置焊机控制模式
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊机控制模式
    * @param [in] mode 焊机控制模式;0-直流一元模式；1-脉冲一元模式；2-JOB模式；3-近控模式；4-分别模式；5-CC/CV模式；6-TIG；7-CMT
    * @param [in] ioType 控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    * @return 错误码
    */
    public int SetWeldMachineCtrlMode(int mode,int ioType = 1)

焊接开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接开始
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 起弧超时时间
    * @return 错误码
    */
    int ARCStart(int ioType, int arcNum, int timeout);

焊接结束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接结束
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 熄弧超时时间
    * @return 错误码
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

摆动开始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 摆动开始
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveStart(int weaveNum);

摆动结束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 摆动结束
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveEnd(int weaveNum);

正向送丝
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 正向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

反向送丝
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 反向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

送气
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 送气
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] airControl 送气控制  0-停止送气；1-送气
    * @return 错误码
    */
    int SetAspirated(int ioType, int airControl);

设置机器人焊接中断后恢复焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断后恢复焊接
    * @return 错误码
    */
    int WeldingStartReWeldAfterBreakOff()

设置机器人焊接中断后退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断后退出焊接
    * @return 错误码
    */
    int WeldingAbortWeldAfterBreakOff()

代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL (p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(1, 0, 10000);
        robot.WeaveEnd(0);
    }

段焊开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    * @param [in] tool 工具号
    * @param [in] user 工件号
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm	 
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout,bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos);

机器人段焊代码示例
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.SegmentWeldStart( p1Desc,  p2Desc,  p1Joint,  p2Joint, 20, 20, 0, 0, 5000, false, 0, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        Console.WriteLine("SegmentWeldStart rtn is {0}", rtn);
    }

仿真摆动开始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真摆动开始
    * @param  [in] weaveNum  摆动参数编号
    * @return  错误码
    */
    int WeaveStartSim(int weaveNum);

仿真摆动结束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真摆动结束
    * @param  [in] weaveNum  摆动参数编号
    * @return  错误码
    */
    int WeaveEndSim(int weaveNum);

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  开始轨迹检测预警(不运动)
    * @param  [in] weaveNum   摆动参数编号
    * @return  错误码
    */
    int WeaveInspectStart(int weaveNum);

结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 结束轨迹检测预警(不运动)
    * @param  [in] weaveNum   摆动参数编号
    * @return  错误码
    */
    int WeaveInspectEnd(int weaveNum);

摆动渐变开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  摆动渐变开始
    * @param [in] weaveChangeFlag 1-变摆动参数；2-变摆动参数+焊接速度
    * @param [in] weaveNum 摆动编号 
    * @param [in] velStart 焊接开始速度，(cm/min)
    * @param [in] velEnd 焊接结束速度，(cm/min)
    * @return  错误码
    */
    int WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

摆动渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  摆动渐变结束
    * @return  错误码
    */
    int WeaveChangeEnd()

机器人摆动渐变焊接代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveStartSim(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveEndSim(0);
        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveInspectStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveInspectEnd(0);

        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveL( p1Joint,  p1Desc, 1, 1, 100, 100, 50, -1,  exaxisPos, 0, 0,  offdese);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1, 0, 50, 30);
        robot.MoveL( p2Joint,  p2Desc, 1, 1, 100, 100, 1, -1,  exaxisPos, 0, 0,  offdese);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
    }

扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机气体检测信号
    * @param  [in] DONum  气体检测信号扩展DO编号
    * @return  错误码
    */
    int SetAirControlExtDoNum(int DONum);

扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机起弧信号
    * @param  [in] DONum  焊机起弧信号扩展DO编号
    * @return  错误码
    */
    int SetArcStartExtDoNum(int DONum);

扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机反向送丝信号
    * @param  [in] DONum  反向送丝信号扩展DO编号
    * @return  错误码
    */
    int SetWireReverseFeedExtDoNum(int DONum);

扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机正向送丝信号
    * @param  [in] DONum  正向送丝信号扩展DO编号
    * @return  错误码
    */
    int SetWireForwardFeedExtDoNum(int DONum);

扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机起弧成功信号
    * @param  [in] DINum  起弧成功信号扩展DI编号
    * @return  错误码
    */
    int SetArcDoneExtDiNum(int DINum);

扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机准备信号
    * @param  [in] DINum  焊机准备信号扩展DI编号
    * @return  错误码
    */
    int SetWeldReadyExtDiNum(int DINum);

扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊接中断恢复信号
    * @param  [in] reWeldDINum  焊接中断后恢复焊接信号扩展DI编号
    * @param  [in] abortWeldDINum  焊接中断后退出焊接信号扩展DI编号
    * @return  错误码
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

设置扩展IO焊接信号代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button51_Click(object sender, EventArgs e)
    {
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);

        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);
    }

电弧跟踪控制
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  电弧跟踪控制
    * @param  [in] flag 开关，0-关；1-开
    * @param  [in] dalayTime 滞后时间，单位ms
    * @param  [in] isLeftRight 左右偏差补偿
    * @param  [in] klr 左右调节系数(灵敏度)
    * @param  [in] tStartLr 左右开始补偿时间cyc
    * @param  [in] stepMaxLr 左右每次最大补偿量 mm
    * @param  [in] sumMaxLr 左右总计最大补偿量 mm
    * @param  [in] isUpLow 上下偏差补偿
    * @param  [in] kud 上下调节系数(灵敏度)
    * @param  [in] tStartUd 上下开始补偿时间cyc
    * @param  [in] stepMaxUd 上下每次最大补偿量 mm
    * @param  [in] sumMaxUd 上下总计最大补偿量
    * @param  [in] axisSelect 上下坐标系选择，0-摆动；1-工具；2-基座
    * @param  [in] referenceType 上下基准电流设定方式，0-反馈；1-常数
    * @param  [in] referSampleStartUd 上下基准电流采样开始计数(反馈)，cyc
    * @param  [in] referSampleCountUd 上下基准电流采样循环计数(反馈)，cyc
    * @param  [in] referenceCurrent 上下基准电流mA
    *  @param  [in] offsetType 偏置跟踪类型，0-不偏置；1-采样；2-百分比  /version 3.7.9
    * @param  [in] offsetParameter 偏置参数；采样(偏置采样开始时间，默认采一周期)；百分比(偏置百分比(-100 ~ 100)) /version 3.7.9
    * @return  错误码
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

电弧跟踪AI通带选择
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  电弧跟踪AI通带选择
    * @param  [in] channel 电弧跟踪AI通带选择,[0-3]
    * @return  错误码
    */
    int ArcWeldTraceExtAIChannelConfig(int channel);

电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 电弧追踪 + 多层多道补偿开启
    * @return 错误码
    */
    int ArcWeldTraceReplayStart();

电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

        /**
         * @brief 电弧追踪 + 多层多道补偿关闭
         * @return 错误码
         */
    int ArcWeldTraceReplayEnd();

偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
     * @brief 偏移量坐标变化-多层多道焊
     * @param [in] pointO 基准点笛卡尔位姿
     * @param [in] pointX 基准点X向偏移方向点笛卡尔位姿
     * @param [in] pointZ 基准点Z向偏移方向点笛卡尔位姿
     * @param [in] dx x方向偏移量(mm)
     * @param [in] z方向偏移量(mm)
     * @param [in] 绕y轴偏移量(°)
     * @param [out] 计算结果偏移量
     * @return 错误码
     */
    int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, ref DescPose offset);

多层多道焊电弧跟踪代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    private void button52_Click(object sender, EventArgs e)
    {
        JointPos mulitilineorigin1_joint = new JointPos(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
        DescPose mulitilineorigin1_desc = new DescPose(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);

        DescTran mulitilineX1_desc = new DescTran();
        mulitilineX1_desc.x = -677.556;
        mulitilineX1_desc.y = 211.949;
        mulitilineX1_desc.z = -1.206;

        DescTran mulitilineZ1_desc = new DescTran();
        mulitilineZ1_desc.x = -677.564;
        mulitilineZ1_desc.y = 190.956;
        mulitilineZ1_desc.z = 19.817;

        JointPos mulitilinesafe_joint = new JointPos(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
        DescPose mulitilinesafe_desc = new DescPose(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
        JointPos mulitilineorigin2_joint = new JointPos(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
        DescPose mulitilineorigin2_desc = new DescPose(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);

        DescTran mulitilineX2_desc = new DescTran();
        mulitilineX2_desc.x = -563.965;
        mulitilineX2_desc.y = 220.355;
        mulitilineX2_desc.z = -0.680;

        DescTran mulitilineZ2_desc = new DescTran();
        mulitilineZ2_desc.x = -563.968;
        mulitilineZ2_desc.y = 215.362;
        mulitilineZ2_desc.z = 4.331;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset = new DescPose(0, 0, 0, 0, 0, 0);

        Thread.Sleep(10);
        int error = robot.MoveJ( mulitilinesafe_joint,  mulitilinesafe_desc, 13, 0, 10, 100, 100,  epos, -1, 0,  offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.WeaveStart(0);
        Console.WriteLine("WeaveStart return: {0}", error);

        error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.WeaveEnd(0);
        Console.WriteLine("WeaveEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("ArcWeldTraceReplayStart return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 1, 2, 100, 100, -1, epos, 1, 1, offset, 1, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 3000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);
    }

电弧跟踪焊机电流反馈AI通道选择
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 电弧跟踪焊机电流反馈AI通道选择
    * @param [in]  channel 通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 错误码
    */
    int ArcWeldTraceAIChannelCurrent(int channel);

电弧跟踪焊机电压反馈AI通道选择
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 电弧跟踪焊机电压反馈AI通道选择
    * @param [in]  channel 通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 错误码
    */
    int ArcWeldTraceAIChannelVoltage(int channel);

电弧跟踪焊机电流反馈转换参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 电弧跟踪焊机电流反馈转换参数
    * @param [in] AILow AI通道下限，默认值0V，范围[0-10V]
    * @param [in] AIHigh AI通道上限，默认值10V，范围[0-10V]
    * @param [in] currentLow AI通道下限对应焊机电流值，默认值0V，范围[0-200V]
    * @param [in] currentHigh AI通道上限对应焊机电流值，默认值100V，范围[0-200V]
    * @return 错误码
    */
    int ArcWeldTraceCurrentPara(float AILow, float AIHigh, float currentLow, float currentHigh);

电弧跟踪焊机电压反馈转换参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 电弧跟踪焊机电压反馈转换参数
    * @param [in] AILow AI通道下限，默认值0V，范围[0-10V]
    * @param [in] AIHigh AI通道上限，默认值10V，范围[0-10V]
    * @param [in] voltageLow AI通道下限对应焊机电压值，默认值0V，范围[0-200V]
    * @param [in] voltageHigh AI通道上限对应焊机电压值，默认值100V，范围[0-200V]
    * @return 错误码
    */
    int ArcWeldTraceVoltagePara(float AILow, float AIHigh, float voltageLow, float voltageHigh);

电弧跟踪代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose safetydescPose = new DescPose(-504.043, 275.181, 40.908, -28.002, -42.025, -14.044);
        JointPos safetyjointPos = new JointPos(-39.078, -76.732, 87.227, -99.47, -94.301, 18.714);
        DescPose startdescPose = new DescPose(-473.86, 257.879, -20.849, -37.317, -42.021, 2.543);
        JointPos startjointPos = new JointPos(-43.487, -76.526, 95.568, -104.445, -89.356, 3.72);



        DescPose enddescPose = new DescPose(-499.844, 141.225, 7.72, -34.856, -40.17, 13.13);
        JointPos endjointPos = new JointPos(-31.305, -82.998, 99.401, -104.426, -89.35, 3.696);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);
        robot.WeldingSetVoltage(0, 25, 1, 0);// ----设置电压
        robot.WeldingSetCurrent(0, 260, 0, 0);// ----设置电流

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        Console.WriteLine("ArcWeldTraceAIChannelCurrent rtn is " + rtn);
        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        Console.WriteLine("ArcWeldTraceAIChannelVoltage rtn is " + rtn);
        rtn = robot.ArcWeldTraceCurrentPara((float)0, (float)5, (float)0, (float)500);
        Console.WriteLine("ArcWeldTraceCurrentPara rtn is " + rtn);
        rtn = robot.ArcWeldTraceVoltagePara((float)1.018, (float)10, (float)0, (float)50);
        Console.WriteLine("ArcWeldTraceVoltagePara rtn is " + rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        // robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
    }

设置焊丝寻位扩展IO端口
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊丝寻位扩展IO端口
    * @param searchDoneDINum 焊丝寻位成功DO端口(0-127)
    * @param searchStartDONum 焊丝寻位启停控制DO端口(0-127)
    * @return 错误码
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

焊丝寻位开始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位开始
    * @param  [in] refPos  1-基准点 0-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；0-示教点寻位
    * @return  错误码
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊丝寻位结束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位结束
    * @param  [in] refPos  1-基准点 2-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return  错误码
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

计算焊丝寻位偏移量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  计算焊丝寻位偏移量
    * @param  [in] seamType  焊缝类型
    * @param  [in] method   计算方法
    * @param  [in] varNameRef 基准点1-6，“#”表示无点变量
    * @param  [in] varNameRes 接触点1-6，“#”表示无点变量
    * @param  [out] offectFlag 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
    * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
    * @return  错误码
    */
    int GetWireSearchOffset(int seamType, int method, string[] varNameRef, string[] varNameRes, ref int offsetFlag, ref DescPose offset);

等待焊丝寻位完成
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待焊丝寻位完成
    * @return  错误码
    */
    int WireSearchWait(string name);

焊丝寻位接触点写入数据库
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位接触点写入数据库
    * @param  [in] varName  接触点名称 “RES0” ~ “RES99”
    * @param  [in] pos  接触点数据[x, y, x, a, b, c]
    * @return  错误码
    */
    int SetPointToDatabase(string varName, DescPose pos);

机器人焊丝寻位代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button53_Click(object sender, EventArgs e)
    {
        DescPose toolCoord=new DescPose(0, 0, 200, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);
        DescPose wobjCoord=new DescPose(0, 0, 0, 0, 0, 0);
        robot.SetWObjCoord(1, wobjCoord, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(216.543, 445.175, 93.465, 179.683, 1.757, -112.641);
        JointPos jointStart = new JointPos(-128.345, -86.660, 114.679, -119.625, -89.219, 74.303);

        DescPose descEnd = new DescPose(111.143, 523.384, 87.659, 179.703, 1.835, -97.750);
        JointPos jointEnd = new JointPos(-113.454, -81.060, 109.328, -119.954, -89.218, 74.302);

        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

        DescPose descREF0A = new DescPose(142.135, 367.604, 86.523, 179.728, 1.922, -111.089);
        JointPos jointREF0A = new JointPos(-126.794, -100.834, 128.922, -119.864, -89.218, 74.302);

        DescPose descREF0B = new DescPose(254.633, 463.125, 72.604, 179.845, 2.341, -114.704);
        JointPos jointREF0B = new JointPos(-130.413, -81.093, 112.044, -123.163, -89.217, 74.303);

        DescPose descREF1A = new DescPose(92.556, 485.259, 47.476, -179.932, 3.130, -97.512);
        JointPos jointREF1A = new JointPos(-113.231, -83.815, 119.877, -129.092, -89.217, 74.303);

        DescPose descREF1B = new DescPose(203.103, 583.836, 63.909, 179.991, 2.854, -103.372);
        JointPos jointREF1B = new JointPos(-119.088, -69.676, 98.692, -121.761, -89.219, 74.303);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        string[] varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
        string[] varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
        int offectFlag = 0;
        DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, ref offectFlag, ref offectPos);
        robot.PointsOffsetEnable(0, offectPos);
        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);
        robot.PointsOffsetDisable();
    }

设置焊接电压渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

设置焊接电压渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电压渐变结束
    * @return 错误码
    */
    int WeldingSetVoltageGradualChangeEnd();

设置焊接电流渐变开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

设置焊接电流渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电流渐变结束
    * @return 错误码
    */
    int WeldingSetCurrentGradualChangeEnd();

机器人焊接电流电压渐变代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(-319.303, -240.689, 116.379, -175.879, -0.337, 148.239);
        JointPos startjointPos = new JointPos(20.474, -103.554, 126.774, -116.682, -87.746, -37.709);

        DescPose enddescPose = new DescPose(-454.166, -327.159, 62.217, 177.199, -2.276, 154.955);
        JointPos endjointPos = new JointPos(27.176, -74.423, 104.557, -119.315, -93.514, -37.698);

        DescPose safedescPose = new DescPose(-375.533, -543.319, 19.798, 177.486, -2.489, 175.825);
        JointPos safejointPos = new JointPos(48.074, -59.714, 89.955, -119.777, -93.508, -37.683);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);

        robot.WeldingSetVoltage(0, 25, 1, 0);//
        robot.WeldingSetCurrent(0, 260, 0, 0);// 

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        int rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        Console.WriteLine($"WeldingSetCurrentGradualChangeStart rtn is {rtn}");
        rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        Console.WriteLine($"WeldingSetVoltageGradualChangeStart rtn is {rtn}");

        rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        Console.WriteLine($"ArcWeldTraceControl rtn is {rtn}");

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        rtn = robot.WeaveChangeStart(2, 1, 24, 36);
        Console.WriteLine($"WeaveChangeStart rtn is {rtn}");
        //robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }

设置自定义摆动参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
     * @return  错误码
     */
    public int CustomWeaveSetPara(int id, int pointNum, DescTran[] points, double[] stayTimes, double frequency, int incStayType, int stationary)

获取自定义摆动参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
     * @return  错误码
     */
    public int CustomWeaveGetPara(int id, ref int pointNum, ref DescTran[] points, ref double[] stayTimes, ref double frequency, ref int incStayType, ref int stationary)

自定义摆动参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestCoordMain5()
    {  
        DescTran[] points = new DescTran[10];
        for (int i = 0; i < 10; i++)
        {
            points[i] = new DescTran();
        }
        points[0].x = -3;
        points[0].y = -3;
        points[0].z = 0;
        points[1].x = -6;
        points[1].y = 0;
        points[1].z = 0;
        points[2].x = -3;
        points[2].y = 3;
        points[2].z = 0;
        points[3].x = 0;
        points[3].y = 0;
        points[3].z = 0;
        double[] stayTimes = new double[10] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        int rtn = robot.CustomWeaveSetPara(2, 4, points, stayTimes, 1.000, 0, 0);
        Console.WriteLine($"CustomWeaveSetPara rtn is {rtn}");
        System.Threading.Thread.Sleep(1000);
        int pointNum = 0;
        double frequency = 0;
        int incStayType = 0;
        int stationary = 0;
        rtn = robot.CustomWeaveGetPara(2, ref pointNum, ref points, ref stayTimes, ref frequency, ref incStayType, ref stationary);
        Console.WriteLine($"pointNum is {pointNum}");
        for (int i = 0; i < pointNum; i++)
        {
            Console.WriteLine($"point {i}, point x y z {points[i].x:F6} {points[i].y:F6} {points[i].z:F6}");
        }
        Console.WriteLine($"fre is {frequency:F6}, stay is {incStayType} {stationary}");
        robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
        DescPose desc_p1 = new DescPose(-288.650, 367.807, 288.404, 0.000, -0.001, 0.001);
        DescPose desc_p2 = new DescPose(-431.714, 367.815, 288.415, 0.001, 0.001, 0.000);    
        DescPose desc_p3 = new DescPose(-348.666, 427.798, 288.404, -0.000, -0.000, 0.001);
        JointPos j1 = new JointPos(140.656,  -84.560,  -91.707, -93.734,  90.000,50.655 );
        JointPos j2 = new JointPos ( 149.873, -98.298, -77.599,  -94.103,  90.000,  59.873 );
        JointPos j3 = new JointPos (139.773,  -96.173, -80.014,  -93.814,  90.000,  49.772 );
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos = new DescPose(0,0,0,0,0,0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.Circle(j3, desc_p3, 3, 0, 100, 100, epos, j2, desc_p2, 3, 0, 100, 100, epos, 10, -1, offset_pos, 100, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveC(j3, desc_p3, 3, 0, 100, 100, epos, 0, offset_pos, j2, desc_p2, 3, 0, 100, 100, epos, 0, offset_pos, 10, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2, 3, 0, 100, 100, 10, -1, epos, 0, 0, offset_pos, 0, 0, 10);
        robot.WeaveEnd(0);
    }