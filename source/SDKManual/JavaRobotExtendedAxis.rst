扩展轴
=================

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴参数
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] param 485扩展轴参数
    * @return 错误码 
    */
    int AuxServoSetParam(int servoId, Axis485Param param)
    
获取485扩展轴参数
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取485扩展轴配置参数
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [out] param 485扩展轴参数
    * @return 错误码 
    */
    int AuxServoGetParam(int servoId, Axis485Param param);

设置485扩展轴使能/去使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码 
    */
    int AuxServoEnable(int servoId, int status);
        
设置485扩展轴控制模式
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码 
    */
    int AuxServoSetControlMode(int servoId, int mode);

设置485扩展轴目标位置(位置模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed, double acc);
    
设置485扩展轴目标转矩(力矩模式)-暂未开放
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标转矩(力矩模式)-暂未开放
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] torque 目标力矩，Nm
    * @return 错误码 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
设置485扩展轴回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] mode 回零模式，1-当前位置回零；2-负限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

清除485扩展轴错误信息
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @return 错误码 
    */
    int AuxServoClearError(int servoId);

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取485扩展轴伺服状态
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] servoErrCode 伺服驱动器故障码
    * @param [in] servoState 伺服驱动器状态 bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成
    * @param [in] servoPos 伺服当前位置 mm或°
    * @param [in] servoSpeed 伺服当前速度 mm/s或°/s
    * @param [in] servoTorque 伺服当前转矩Nm
    * @return 错误码 
    */
    int AuxServoGetStatus(int servoId, int[] servoErrCode, int[] servoState, double[] servoPos, double[] servoSpeed, double[] servoTorque)

设置485扩展轴目标速度(速度模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] speed 目标速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed, double acc);

设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @return 错误码 
    */
    int AuxServosetStatusID(int servoId);

设置485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴运动加减速度
    * @param [in] acc 485扩展轴运动加速度
    * @param [in] dec 485扩展轴运动减速度
    * @return 错误码 
    */
    int AuxServoSetAcc(double acc, double dec)

设置485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴急停加减速度
    * @param [in] acc 485扩展轴急停加速度
    * @param [in] dec 485扩展轴急停减速度
    * @return 错误码 
    */
    int AuxServoSetEmergencyStopAcc(double acc, double dec)

获取485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取485扩展轴运动加减速度
    * @return List[0]:错误码; List[1]:485扩展轴运动加速度; List[2]:485扩展轴运动减速度 
    */
    List<Number> AuxServoGetAcc()

获取485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取485扩展轴急停加减速度
    * @return List[0]:错误码; List[1]:485扩展轴急停加速度; List[2]:485扩展轴急停减速度
    */
    List<Number> AuxServoGetEmergencyStopAcc()

扩展轴控制代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int Test485Auxservo(Robot robot)
    {
        Axis485Param ax=new Axis485Param(1, 1, 1, 131072, 15.45);
        int retval = robot.AuxServoSetParam(1, ax);

        Axis485Param ax2=new Axis485Param();
        retval = robot.AuxServoGetParam(1, ax2);

        ax.servoCompany=10;
        ax.servoModel=11;
        ax.servoSoftVersion=12;
        ax.servoResolution=13;
        ax.axisMechTransRatio=14;

        retval = robot.AuxServoSetParam(1, ax);

        retval = robot.AuxServoGetParam(1,ax2);

        ax.servoCompany=1;
        ax.servoModel=1;
        ax.servoSoftVersion=1;
        ax.servoResolution=131072;
        ax.axisMechTransRatio=36;

        retval = robot.AuxServoSetParam(1, ax);
        robot.Sleep(3000);

        robot.AuxServoSetAcc(3000, 3000);
        robot.AuxServoSetEmergencyStopAcc(5000, 5000);
        robot.Sleep(1000);
        double emagacc = 0, acc = 0;
        double emagdec = 0, dec = 0;

        List<Number> aux=new ArrayList<>();

        aux=robot.AuxServoGetEmergencyStopAcc();
        aux=robot.AuxServoGetAcc();

        robot.AuxServoSetControlMode(1, 0);
        robot.Sleep(2000);

        retval = robot.AuxServoEnable(1, 0);
        robot.Sleep(1000);
        int[] servoerrcode =new int[]{0};
        int[] servoErrCode=new int[]{0};
        int[] servoState=new int[]{0};
        double[] servoPos=new double[]{0};
        double[] servoSpeed=new double[]{0};
        double[] servoTorque=new double[]{0};
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(1000);;

        retval = robot.AuxServoEnable(1, 1);
        robot.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(1000);

        retval = robot.AuxServoHoming(1, 1, 5, 1,100);
        robot.Sleep(3000);

        retval = robot.AuxServoSetTargetPos(1, 200, 30,100);
        robot.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(8000);


        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);

        robot.AuxServoEnable(1, 0);
        robot.Sleep(1000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(1000);
        robot.AuxServoSetTargetSpeed(1, 100, 80);

        robot.Sleep(5000);
        robot.AuxServoSetTargetSpeed(1, 0, 80);

        robot.CloseRPC();
        return 0;
    }

UDP扩展轴通讯参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通讯参数配置
    * @param [in] param 通讯参数
    * @return 错误码
    */
    int ExtDevSetUDPComParam(UDPComParam param);     

获取UDP扩展轴通讯参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取UDP扩展轴通讯参数
    * @param [out] ip PLC IP地址
    * @param [out] port	端口号
    * @param [out] period	通讯周期(ms，默认为2，请勿修改此参数)
    * @param [out] lossPkgTime	丢包检测时间(ms)
    * @param [out] lossPkgNum	丢包次数
    * @param [out] disconnectTime	通讯断开确认时长
    * @param [out] reconnectEnable	通讯断开自动重连使能 0-不使能 1-使能
    * @param [out] reconnectPeriod	重连周期间隔(ms)
    * @param [out] reconnectNum	重连次数
    * @param [out] selfConnect 重启控制箱后是否自动重连；0-不重连；1-重连
    * @return 错误码
    */
    public int ExtDevGetUDPComParam(ref string ip, ref int port, ref int period, ref int lossPkgTime, ref int lossPkgNum, ref int disconnectTime, ref int reconnectEnable, ref int reconnectPeriod, ref int reconnectNum, ref int selfConnect)    

加载UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 加载UDP通信
    * @return 错误码
    */
    int ExtDevLoadUDPDriver();

卸载UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 卸载UDP通信
    * @return 错误码
    */
    int ExtDevUnloadUDPDriver();

UDP扩展轴通信异常断开后恢复连接
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后恢复连接
    * @return 错误码
    */
    int ExtDevUDPClientComReset();

UDP扩展轴通信异常断开后关闭通讯
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后关闭通讯
    * @return 错误码
    */
    int ExtDevUDPClientComClose();

UDP扩展轴参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴参数配置
    * @param [in] axisID 轴号
    * @param [in] axisType 扩展轴类型 0-平移；1-旋转
    * @param [in] axisDirection 扩展轴方向 0-正向；1-方向
    * @param [in] axisMax 扩展轴最大位置 mm
    * @param [in] axisMin 扩展轴最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 导程mm
    * @param [in] encResolution 编码器分辨率
    * @param [in] axisOffect 焊缝起始点扩展轴偏移量
    * @param [in] axisCompany 驱动器厂家 1-禾川；2-汇川；3-松下
    * @param [in] axisModel 驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 编码器类型  0-增量；1-绝对值
    * @return 错误码
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, int encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

设置扩展轴安装位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展轴安装位置
    * @param [in] installType 0-机器人安装在外部轴上，1-机器人安装在外部轴外
    * @return 错误码
    */
    int SetRobotPosToAxis(int installType);

设置扩展轴系统DH参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展轴系统DH参数配置
    * @param [in]  axisConfig 外部轴构型，0-单自由度直线滑轨，1-两自由度L型变位机，2-三自由度，3-四自由度，4-单自由度变位机
    * @param [in]  axisDHd1 外部轴DH参数d1 mm
    * @param [in]  axisDHd2 外部轴DH参数d2 mm
    * @param [in]  axisDHd3 外部轴DH参数d3 mm
    * @param [in]  axisDHd4 外部轴DH参数d4 mm
    * @param [in]  axisDHa1 外部轴DH参数11 mm
    * @param [in]  axisDHa2 外部轴DH参数a2 mm
    * @param [in]  axisDHa3 外部轴DH参数a3 mm
    * @param [in]  axisDHa4 外部轴DH参数a4 mm
    * @return 错误码
    */
    int SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

UDP扩展轴使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴使能
    * @param [in] axisID 轴号[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 错误码
    */
    int ExtAxisServoOn(int axisID, int status);

UDP扩展轴回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴回零
    * @param [in] axisID 轴号[1-4]
    * @param [in] mode 回零方式 0-当前位置回零，1-负限位回零，2-正限位回零
    * @param [in] searchVel 寻零速度(mm/s)
    * @param [in] latchVel 寻零箍位速度(mm/s)
    * @return 错误码
    */
    int ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP扩展轴点动开始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴点动开始
    * @param [in] axisID 轴号[1-4]
    * @param [in] direction 转动方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc (加速度 mm/s2)
    * @param [in] maxDistance 最大点动距离
    * @return 错误码
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP扩展轴点动停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴点动停止
    * @param [in] axisID 轴号[1-4]
    * @return 错误码
    */
    int ExtAxisStopJog(int axisID);

UDP扩展轴配置与点动代码示例
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static int TestUDPAxis(Robot robot)//UDP
    {
        UDPComParam para1=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
        int rtn = robot.ExtDevSetUDPComParam(para1);
        String ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        UDPComParam para2=new UDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum,0);
        rtn = robot.ExtDevGetUDPComParam(para2);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        rtn = robot.ExtAxisServoOn(2, 1);
        robot.Sleep(3000);

        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.Sleep(3000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);

        robot.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);

        robot.Sleep(4000);
        robot.ExtAxisStartJog(1, 0, 10, 10, 30);
        robot.Sleep(4000);
        robot.ExtAxisStopJog(1);
        robot.Sleep(4000);
        robot.ExtAxisServoOn(1, 0);

        robot.Sleep(4000);
        robot.ExtAxisStartJog(2, 0, 10, 10, 30);
        robot.Sleep(4000);
        robot.ExtAxisStopJog(2);
        robot.Sleep(4000);
        robot.ExtAxisServoOn(2, 0);
        robot.Sleep(4000);
        robot.ExtDevUnloadUDPDriver();

        return 0;
    }

设置扩展轴坐标系参考点-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展轴坐标系参考点-四点法
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int ExtAxisSetRefPoint(int pointNum);

计算扩展轴坐标系-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 计算扩展轴坐标系-四点法
    * @param [out]  coord 坐标系值
    * @return 错误码
    */
    int ExtAxisComputeECoordSys(DescPose coord);

变位机坐标系参考点设置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 变位机坐标系参考点设置
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int PositionorSetRefPoint(int pointNum);

变位机坐标系计算-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 变位机坐标系计算-四点法
    * @param [out] coord 坐标系值
    * @return 错误码
    */
    int PositionorComputeECoordSys(DescPose coord);

设置标定参考点在变位机末端坐标系下位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置标定参考点在变位机末端坐标系下位姿
    * @param [in] pos 位姿值
    * @return 错误码
    */
    int SetRefPointInExAxisEnd(DescPose pos);

应用扩展轴坐标系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 应用扩展轴坐标系
    * @param [in]  applyAxisId 扩展轴编号 bit0-bit3对应扩展轴编号1-4，如应用扩展轴1和3，则是 0b 0000 0101；也就是5
    * @param [in]  axisCoordNum 扩展轴坐标系编号
    * @param [in]  coord 坐标系值
    * @param [in]  calibFlag 标定标志 0-否，1-是
    * @return 错误码
    */
    int ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

获取扩展轴坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取扩展轴坐标系
    * @param [out] coord 扩展轴坐标系
    * @return 错误码
    */
    int ExtAxisGetCoord(DescPose coord);

扩展轴坐标系标定代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUDPAxisCalib(Robot robot)
    {
        UDPComParam para1=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);

        int rtn = robot.ExtDevSetUDPComParam(para1);
        String ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        UDPComParam para2=new UDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum,0);

        rtn = robot.ExtDevGetUDPComParam(para2);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        rtn = robot.ExtAxisServoOn(2, 1);

        robot.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4,  0, 0, 0, 0, 0, 0);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);

        DescPose toolCoord=new DescPose(0, 0, 210, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);

        JointPos jSafe=new JointPos(115.193, -96.149, 92.489, -87.068, -89.15, -83.488);
        JointPos j1=new JointPos(117.559, -92.624, 100.329, -96.909, -94.057, -83.488);
        JointPos j2=new JointPos(112.239, -90.096, 99.282, -95.909, -89.824, -83.488);
        JointPos j3=new JointPos(110.839, -83.473, 93.166, -89.22, -90.499, -83.487);
        JointPos j4=new JointPos(107.935, -83.572, 95.424, -92.873, -87.933, -83.488);

        DescPose descSafe =new DescPose(0,0,0,0,0,0);
        DescPose desc1 = new DescPose(0,0,0,0,0,0);
        DescPose desc2 = new DescPose(0,0,0,0,0,0);
        DescPose desc3 = new DescPose(0,0,0,0,0,0);
        DescPose desc4 = new DescPose(0,0,0,0,0,0);
        ExaxisPos exaxisPos =new ExaxisPos(0,0,0,0);
        DescPose offdese =new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(jSafe, descSafe);
        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.Sleep(2000);

        robot.GetForwardKin(j1, desc1);
        robot.MoveJ(j1, desc1, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.Sleep(2000);

        DescPose actualTCPPos =new DescPose(0,0,0,0,0,0);

        robot.GetActualTCPPose(actualTCPPos);
        robot.SetRefPointInExAxisEnd(actualTCPPos);
        rtn = robot.PositionorSetRefPoint(1);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j2, desc2);
        rtn = robot.MoveJ(j2, desc2, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(2);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j3, desc3);
        robot.MoveJ(j3, desc3, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(3);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j4, desc4);
        robot.MoveJ(j4, desc4, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(4);
        robot.Sleep(2000);

        DescPose axisCoord = new DescPose();
        robot.PositionorComputeECoordSys(axisCoord);
        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1);

        robot.CloseRPC();
        return 0;
    }

UDP扩展轴运动
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴运动
    * @param [in] pos 目标位置
    * @param [in] ovl 速度百分比
    * @param [in] blend 平滑参数(mm或ms)
    * @return 错误码
    */
    int ExtAxisMove(ExaxisPos pos, double ovl, double blend)

UDP扩展轴运动代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUDPAxisCalib(Robot robot)
    {
        ExaxisPos exaxisPos = new ExaxisPos( 20, 0, 0, 0 );
        robot.ExtAxisMove(exaxisPos,40);
        robot.CloseRPC();
        return 0;
    }

UDP扩展轴与机器人关节运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴与机器人关节运动同步运动
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] ffset_pos  位姿偏移量
    * @return 错误码
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

UDP扩展轴与机器人关节运动同步运动 (自动正运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  UDP扩展轴与机器人关节运动同步运动 (自动正运动学计算)
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos) 

UDP扩展轴与机器人关节运动同步运动代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveJ(Robot robot)
    {
        //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //  int SetToolPoint(int point_num); //设置工具参考点-六点法
        //  int ComputeTool(ref DescPose tcp_pose); //计算工具坐标系
        //  int SetTcp4RefPoint(int point_num);  //设置工具参考点-四点法
        //  int ComputeTcp4(ref DescPose tcp_pose);  //计算工具坐标系-四点法
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //设置应用工具坐标系
        //  int SetToolList(int id, DescPose coord, int type, int install);  //设置应用工具坐标系列表
        //2.设置UDP通信参数，并加载UDP通信
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1); //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数
        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5.进行扩展轴坐标系标定及应用
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //将标定结果应用到扩展轴坐标系
        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7.记录您的同步关节运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/ );
        JointPos startjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */ );
        //8.记录您的同步关节运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/ );
        JointPos endjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos endexaxisPos =new ExaxisPos(/* 输入您的扩展轴终点坐标 */);
        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveJ(endjointPos, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
        robot.CloseRPC();
        return 0;
    }

UDP扩展轴与机器人直线运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴与机器人直线运动同步运动
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

UDP扩展轴与机器人直线运动同步运动 (自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  UDP扩展轴与机器人直线运动同步运动 (自动逆运动学计算)
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return  错误码
    */
    int ExtAxisSyncMoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos,int config)

UDP扩展轴与机器人直线运动同步运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveL(Robot robot)
    {
        //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //  int SetToolPoint(int point_num); //设置工具参考点-六点法
        //  int ComputeTool(ref DescPose tcp_pose); //计算工具坐标系
        //  int SetTcp4RefPoint(int point_num);  //设置工具参考点-四点法
        //  int ComputeTcp4(ref DescPose tcp_pose);  //计算工具坐标系-四点法
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //设置应用工具坐标系
        //  int SetToolList(int id, DescPose coord, int type, int install);  //设置应用工具坐标系列表
        //2.设置UDP通信参数，并加载UDP通信
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1); //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数
        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5.进行扩展轴坐标系标定及应用
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //将标定结果应用到扩展轴坐标系
        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7.记录您的同步关节运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/ );
        JointPos startjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */ );
        //8.记录您的同步关节运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/ );
        JointPos endjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos endexaxisPos =new ExaxisPos(/* 输入您的扩展轴终点坐标 */);
        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveL(enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese,-1);
        robot.CloseRPC();
        return 0;
    }

UDP扩展轴与机器人圆弧运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴与机器人圆弧运动同步运动
    * @param [in] joint_pos_p  路径点关节位置,单位deg
    * @param [in] desc_pos_p   路径点笛卡尔位姿
    * @param [in] ptool  工具坐标号，范围[0~14]
    * @param [in] puser  工件坐标号，范围[0~14]
    * @param [in] pvel  速度百分比，范围[0~100]
    * @param [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p  中间点扩展轴位置，单位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] joint_pos_t  目标点关节位置,单位deg
    * @param [in] desc_pos_t   目标点笛卡尔位姿
    * @param [in] ttool  工具坐标号，范围[0~14]
    * @param [in] tuser  工件坐标号，范围[0~14]
    * @param [in] tvel  速度百分比，范围[0~100]
    * @param [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t  扩展轴位置，单位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_t  位姿偏移量
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

UDP扩展轴与机器人圆弧运动同步运动 (自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  UDP扩展轴与机器人圆弧运动同步运动 (自动逆运动学计算)
    * @param  [in] desc_pos_p   路径点笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] desc_pos_t   目标点笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return  错误码
    */
    int ExtAxisSyncMoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR,int config)

UDP扩展轴与机器人圆弧运动同步运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveC(Robot robot)
    {
        //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //  int SetToolPoint(int point_num); //设置工具参考点-六点法
        //  int ComputeTool(ref DescPose tcp_pose); //计算工具坐标系
        //  int SetTcp4RefPoint(int point_num);  //设置工具参考点-四点法
        //  int ComputeTcp4(ref DescPose tcp_pose);  //计算工具坐标系-四点法
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //设置应用工具坐标系
        //  int SetToolList(int id, DescPose coord, int type, int install);  //设置应用工具坐标系列表
        //2.设置UDP通信参数，并加载UDP通信
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1); //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数
        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5.进行扩展轴坐标系标定及应用
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //将标定结果应用到扩展轴坐标系
        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7.记录您的同步圆弧运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/ );
        JointPos startjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */ );
        //8.记录您的同步圆弧运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/ );
        JointPos endjointPos = new JointPos(/*输入您的坐标*/ );
        ExaxisPos endexaxisPos = new ExaxisPos(/* 输入您的扩展轴终点坐标 */ );
        //9.记录您的同步圆弧运动中间点坐标
        DescPose middescPose = new DescPose(/*输入您的坐标*/ );
        JointPos midjointPos =new JointPos(/*输入您的坐标*/ );
        ExaxisPos midexaxisPos = new ExaxisPos(/* 输入机器人圆弧中间点时的扩展轴坐标 */ );
        //10.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //开始同步运动
        robot.ExtAxisSyncMoveC(middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0,-1);
        robot.CloseRPC();
        return 0;
    }

设置扩展DO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展DO
    * @param [in] DONum DO编号
    * @param [in] bOpen 开关 true-开；false-关
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxDO(int DONum, boolean bOpen, boolean smooth, boolean block);

设置扩展AO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展AO
    * @param [in] AONum AO编号
    * @param [in] value 模拟量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxAO(int AONum, double value, boolean block);

设置扩展DI输入滤波时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展DI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return  错误码
    */
    int SetAuxDIFilterTime(int filterTime);

设置扩展AI输入滤波时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展AI输入滤波时间
    * @param [in] AONum AO编号
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    int SetAuxAIFilterTime(int AONum, int filterTime);

等待扩展DI输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param [in] DINum DI编号
    * @param [in] bOpen 开关 0-关；1-开
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    int WaitAuxDI(int DINum, boolean bOpen, int time, boolean errorAlarm);

等待扩展AI输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param [in] AINum AI编号
    * @param [in] sign 0-大于；1-小于
    * @param [in] value AI值
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    int WaitAuxAI(int AINum, int sign, int value, int time, boolean errorAlarm);
    
获取扩展DI值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取扩展DI值
    * @param [in] DINum DI编号
    * @param [in] isNoBlock 是否阻塞
    * @return List[0]:错误码; List[1] : isOpen 0-关；1-开
    */
    List<Integer> GetAuxDI(int DINum, boolean isNoBlock)

获取扩展AI值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取扩展AI值
    * @param [in] AINum AI编号
    * @param [in] isNoBlock 是否阻塞
    * @return List[0]:错误码; List[1] : value 输入值
    */
    List<Integer> GetAuxAI(int AINum, boolean isNoBlock);

扩展IO代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAuxDOAO(Robot robot)
    {
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, true, false, true);
            robot.Sleep(100);
        }
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, false, false, true);
            robot.Sleep(100);
        }

        for (int i = 0; i < 409; i++)
        {
            robot.SetAuxAO(0, i * 10, true);
            robot.SetAuxAO(1, 4095 - i * 10, true);
            robot.SetAuxAO(2, i * 10, true);
            robot.SetAuxAO(3, 4095 - i * 10, true);
            robot.Sleep(10);
        }

        robot.SetAuxDIFilterTime(10);
        robot.SetAuxAIFilterTime(0, 10);


        int curValue = -1;
        List<Integer> liter=new ArrayList<>();
        for (int i = 0; i < 4; i++)
        {
            liter = robot.GetAuxAI(i, true);
        }

        robot.WaitAuxDI(1, false, 1000, false);
        robot.WaitAuxAI(1, 1, 132, 1000, false);

        robot.CloseRPC();
        return 0;
    }

可移动装置使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置使能
    * @param [in] enable false-去使能；true-使能
    * @return 错误码
    */
    int TractorEnable(Boolean enable);

可移动装置回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置回零
    * @return 错误码
    */
    int TractorHoming();

可移动装置直线运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置直线运动
    * @param [in] distance 直线运动距离（mm）
    * @param [in] vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveL(double distance, double vel);

可移动装置圆弧运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置圆弧运动
    * @param [in] radio 圆弧运动半径（mm）
    * @param [in] angle 圆弧运动角度（°）
    * @param [in] vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveC(double radio, double angle, double vel);

可移动装置停止运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置停止运动
    * @return 错误码
    */
    int TractorStop();

可移动装置代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//udp扩展轴通讯
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);

        robot.TractorEnable(false);
        robot.Sleep(2000);
        robot.TractorEnable(true);
        robot.Sleep(2000);
        robot.TractorHoming();

        robot.Sleep(2000);
        robot.TractorMoveL(100, 20);
        robot.Sleep(5000);
        robot.TractorMoveL(-100, 20);
        robot.Sleep(5000);
        robot.TractorMoveC(300, 90, 20);
        robot.Sleep(2000);
        robot.TractorStop();//小车停止
        robot.TractorMoveC(300, -90, 20);
    }
    
UDP扩展轴定位完成时间设置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴定位完成时间设置
    * @param time 定位完成时间[ms]
    * @return 错误码
    */
    public int SetExAxisCmdDoneTime(double time)