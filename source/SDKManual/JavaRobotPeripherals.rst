机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [in] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [in] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int SetGripperConfig(DeviceConfig config);

获取夹爪配置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [out] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [out] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [out] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [out] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int GetGripperConfig(DeviceConfig config);

激活夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int ActGripper(int index, int act); 

控制夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] pos  位置百分比，范围[0~100]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] force  力矩百分比，范围[0~100]
    * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [in] type 夹爪类型，0-平行夹爪；1-旋转夹爪
    * @param  [in] rotNum 旋转圈数
    * @param  [in] rotVel 旋转速度百分比[0-100]
    * @param  [in] rotTorque 旋转力矩百分比[0-100]
    * @return 错误码
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, int block, int type, double rotNum, int rotVel, int rotTorque); 

获取夹爪运动状态
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪运动状态
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: staus  0-运动未完成，1-运动完成
    */
    List<Integer> GetGripperMotionDone(); 

获取夹爪激活状态
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪激活状态
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
    */
    List<Number> GetGripperActivateStatus()

获取夹爪位置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪位置
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: position  位置百分比，范围0~100%
    */
    List<Number> GetGripperCurPosition()

获取夹爪速度
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪速度
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: speed  速度百分比，范围0~100%
    */
    List<Number> GetGripperCurSpeed()

获取夹爪电流
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪电流
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: current  电流百分比，范围0~100%
    */
    List<Number> GetGripperCurCurrent()

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪电压
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]:voltage  电压,单位0.1V
    */
    List<Number> GetGripperVoltage()

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪温度
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]:temp  温度，单位℃
    */
    List<Number> GetGripperTemp()

计算预抓取点-视觉
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算预抓取点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] pre_pos  获取点
    * @return 错误码 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, DescPose pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算撤退点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量 
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] post_poss 撤退点
    * @return 错误码 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, DescPose post_pos);

机器人夹爪操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGripper(Robot robot)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        int act = 0;
        int max_time = 30000;
        int block = 0;

        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        DeviceConfig cnn=new DeviceConfig(company,device,softversion,bus);
        robot.SetGripperConfig(cnn);
        robot.GetGripperConfig(cnn);

        robot.ActGripper(index, act);
        robot.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        robot.Sleep(1000);

        robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
        robot.Sleep(1000);
        robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);

        List<Integer> stat=new ArrayList<>();
        stat=robot.GetGripperMotionDone();

        List<Number> list=new ArrayList<>();
        list=robot.GetGripperActivateStatus();

        list=robot.GetGripperCurPosition();

        list=robot.GetGripperCurCurrent();

        list=robot.GetGripperVoltage();

        list=robot.GetGripperTemp();

        list=robot.GetGripperCurSpeed();

        int retval = 0;
        DescPose prepick_pose = new DescPose(){};
        DescPose postpick_pose = new DescPose(){};

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        retval = robot.ComputePrePick(p1Desc, 10, 0, prepick_pose);

        retval = robot.ComputePostPick(p2Desc, -10, 0, postpick_pose);
        return 0;
    }

获取旋转夹爪的旋转圈数
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转圈数
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转圈数
    */
    List<Number> GetGripperRotNum(); 

获取旋转夹爪的旋转速度百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转速度百分比
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转速度百分比
    */
    List<Number> GetGripperRotSpeed(); 

获取旋转夹爪的旋转力矩百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转力矩百分比
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转力矩百分比
    */
    List<Number> GetGripperRotTorque(); 

代码示获取旋转夹爪状态代码示例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRotGripperState(Robot robot)
    {
        int fault = 0;
        List<Number> rotNum=new ArrayList<>();
        List<Number> rotSpeed=new ArrayList<>();
        List<Number> rotTorque=new ArrayList<>();

        rotNum=robot.GetGripperRotNum();
        rotSpeed=robot.GetGripperRotSpeed();
        rotTorque=robot.GetGripperRotTorque();
        System.out.println("gripper rot num :"+rotNum.get(2)+ ", gripper rotSpeed :"+rotSpeed.get(2)+",gripper rotTorque : "+rotTorque.get(2));

        return 0;
    }

传动带启动、停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带启动、停止
    * @param  [in] status 状态，1-启动，0-停止
    * @return  错误码
    */
    int ConveyorStartEnd(int status);

记录IO检测点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录IO检测点
    * @return  错误码
    */
    int ConveyorPointIORecord();

记录A点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录A点
    * @return  错误码
    */
    int ConveyorPointARecord(); 

记录参考点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录参考点
    * @return  错误码
    */
    int ConveyorRefPointRecord();

记录B点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录B点
    * @return 错误码
    */
    int ConveyorPointBRecord(); 

传送带工件IO检测
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带工件IO检测
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码 
    */ 
    int ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取物体当前位置
    * @param [in] mode 1-跟踪抓取，2-跟踪运动，3-TPD跟踪
    * @return 错误码 
    */ 
    int ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪开始
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */ 
    int ConveyorTrackStart(int status);

传动带跟踪停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪停止
    * @return 错误码 
    */ 
    int ConveyorTrackEnd();

传动带参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带参数配置
    * @param [in] encChannel 编码器通道 1~2
    * @param [in] resolution 编码器转一圈的脉冲数
    * @param [in] lead 编码器转一圈传送带行走距离
    * @param [in] wpAxis 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] vision 是否配视觉  0 不配  1 配
    * @param [in] speedRadio 速度比  针对传送带跟踪抓取选项（1-100）  其他选项默认为1
    * @param [in] followType 跟踪运动类型，0-跟踪运动；1-追检运动
    * @param [in] startDis 追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    * @param [in] endDis 追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100
    * @return 错误码
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis, int endDis); 

设置传动带抓取点补偿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置传动带抓取点补偿
    * @param [in] cmp 补偿位置 double[3]{x, y, z}
    * @return 错误码 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

传动带直线运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 直线运动
    * @param [in] name 运动点描述
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] wobj 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码 
    */ 
    int ConveyorTrackMoveL(String name, int tool, int wobj, double vel, double acc, double ovl, double blendR);   

传送带通讯输入检测
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带通讯输入检测
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    int ConveyorComDetect(int timeout);

传送带通讯输入检测触发
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带通讯输入检测触发
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    int ConveyorComDetectTrigger();

机器人传送带操作示例程序
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestConveyor(Robot robot)
    {
        int retval = 0;

        retval = robot.ConveyorStartEnd(1);

        retval = robot.ConveyorPointIORecord();

        retval = robot.ConveyorPointARecord();

        retval = robot.ConveyorRefPointRecord();

        retval = robot.ConveyorPointBRecord();

        retval = robot.ConveyorStartEnd(0);

        retval = 0;

        retval = robot.ConveyorSetParam(1,10000,200,0,0,20,0,0,100);

        Object[] cmp = new Object[]{ 0.0, 0.0, 0.0 };
        retval = robot.ConveyorCatchPointComp(cmp);

        int index = 1;
        int max_time = 30000;
        int block = 0;
        retval = 0;

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);


        retval = robot.MoveCart(p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.WaitMs(1);

        retval = robot.ConveyorTrackStart(1);

        retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);

        retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.ConveyorTrackEnd();

        robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);

        return 0;
    }

末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器配置
    * @param [in] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [in] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param [in] config idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return 错误码
    */
    int AxleSensorConfig(DeviceConfig config);

获取末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取末端传感器配置
    * @param [out] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [out] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @return 错误码
    */
    int AxleSensorConfigGet(DeviceConfig config);

末端传感器激活
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器激活
    * @param [in] actFlag 0-复位；1-激活
    * @return 错误码
    */
    int AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器寄存器写入
    * @param [in] devAddr  设备地址编号 0-255
    * @param [in] regHAddr 寄存器地址高8位
    * @param [in] regLAddr 寄存器地址低8位
    * @param [in] regNum  寄存器个数 0-255
    * @param [in] data1 写入寄存器数值1
    * @param [in] data2 写入寄存器数值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 错误码
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端传感器代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleSensor(Robot robot)
    {
        DeviceConfig con=new DeviceConfig(18,0,0,1);
        robot.AxleSensorConfig(con);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(con);

        int rtn = robot.AxleSensorActivate(1);

        robot.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        return 0;
    }

获取机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人外设协议
    * @return List[0]:错误码; List[1] : int protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

设置机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int SetExDevProtocol(int protocol);

设置机器人外设协议示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExDevProtocol(Robot robot)
    {
        int protocol = 4096;
        int rtn = robot.SetExDevProtocol(protocol);
        List<Integer> integer=new ArrayList<>();
        integer = robot.GetExDevProtocol();

        return 0;
    }

获取末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取末端通讯参数
    * @param [out] param 末端通讯参数
    * @return 错误码 
    */
    int GetAxleCommunicationParam(AxleComParam param)

设置末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置末端通讯参数
    * @param [in] param 末端通讯参数
    * @return 错误码 
    */
    int SetAxleCommunicationParam(AxleComParam param)

设置末端文件传输类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置末端文件传输类型
    * @param [in] type 1-MCU升级文件；2-LUA文件
    * @return  错误码
    */
    public int SetAxleFileType(int type)

设置启用末端LUA执行
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置启用末端LUA执行
    * @param [in] enable 0-不启用；1-启用
    * @return  错误码
    */
    public int SetAxleLuaEnable(int enable)

末端LUA文件异常错误恢复
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端LUA文件异常错误恢复
    * @param [in] status 0-不恢复；1-恢复
    * @return  错误码
    */
    public int SetRecoverAxleLuaErr(int status)

获取末端LUA执行使能状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取末端LUA执行使能状态
    * @param [out] status[0]: 0-未使能；1-已使能
    * @return  错误码
    */
    int GetAxleLuaEnableStatus(int[] status)

设置末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置末端LUA末端设备启用类型
    * @param forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable)

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取末端LUA末端设备启用类型
     * @param enable enable[0]:forceSensorEnable 力传感器启用状态，0-不启用；1-启用
     * @param enable enable[1]:gripperEnable 夹爪启用状态，0-不启用；1-启用
     * @param enable enable[2]:IOEnable IO设备启用状态，0-不启用；1-启用
     * @return  错误码
     */
    public int GetAxleLuaEnableDeviceType(int[] enable)

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前配置的末端设备
     * @param forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
     * @param gripperEnable 夹爪启用设备编号，0-不启用；1-启用
     * @param IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
     * @return  错误码
     */
    public int GetAxleLuaEnableDevice(int[] forceSensorEnable, int[] gripperEnable, int[] IODeviceEnable)

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 设置启用夹爪动作控制功能
     * @param id 夹爪设备编号
     * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
     * @return  错误码
     */
    public int SetAxleLuaGripperFunc(int id, int[] func)

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取启用夹爪动作控制功能
     * @param id 夹爪设备编号
     * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
     * @return  错误码
     */
    public int GetAxleLuaGripperFunc(int id, int[] func)

机器人Ethercat从站文件写入
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人Ethercat从站文件写入
     * @param type 从站文件类型，1-升级从站文件；2-升级从站配置文件
     * @param slaveID 从站号
     * @param fileName 上传文件名
     * @return  错误码
     */
    public int SlaveFileWrite(int type, int slaveID, String fileName)

上传末端Lua开放协议文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 上传末端Lua开放协议文件
     * @param filePath 本地lua文件路径名 ".../AXLE_LUA_End_DaHuan.lua"
     * @return 错误码
     */
    public int AxleLuaUpload(String filePath)

机器人Ethercat从站进入boot模式
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人Ethercat从站进入boot模式
     * @return  错误码
     */
    public int SetSysServoBootMode()

机器人末端LUA文件操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleLua(Robot robot)
    {
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");

        AxleComParam param=new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        robot.GetAxleCommunicationParam(param);

        robot.SetAxleLuaEnable(1);
        int[] luaEnableStatus = new int[]{0};
        robot.GetAxleLuaEnableStatus(luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int [] enable=new int[]{0,0,0};
        robot.GetAxleLuaEnableDeviceType(enable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        robot.GetAxleLuaGripperFunc(1, getFunc);
        int[] getforceEnable = { 0,0,0,0,0,0,0,0};
        int[] getgripperEnable = { 0,0,0,0,0,0,0,0};
        int[] getioEnable = { 0,0,0,0,0,0,0,0};
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getforceEnable[i]);
        }
        System.out.println("getgripperEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getgripperEnable[i]);
        }
        System.out.println("getioEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getioEnable[i]);
        }
        robot.ActGripper(1, 0);
        robot.Sleep(2000);
        robot.ActGripper(1, 1);
        robot.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
            pkg=robot.GetRobotRealTimeState();
            System.out.println("gripper pos is:"+pkg.gripper_position);
            robot.Sleep(100);
        }

    }

获取SmartTool按钮状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 获取SmartTool按钮状态
    * @param [out] state SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)
    * @return 错误码
    */
    int GetSmarttoolBtnState(int[] state)

SmartTool按钮代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args) 
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn == 0) {
            System.out.println("rpc连接 success");
        } else {
            System.out.println("rpc连接 fail");
            return;
        }

        int[] state = {0};
        while (true)
        {
            robot.GetSmarttoolBtnState(state);

            String binaryString = String.format("%32s", Integer.toBinaryString(state[0])).replace(' ', '0');
            System.out.println("GetSmarttoolBtnState:"+binaryString);
            robot.Sleep(100);
        }
    }

上传开放协议的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 上传开放协议的Lua文件
    * @param  filePath 本地开放协议lua文件路径名
    * @return 错误码
    */
    public int OpenLuaUpload(String filePath)


获取从站板卡参数
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  获取从站板卡参数
    * @param  type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  version  协议版本
    * @param  connState  0-未连接 1-已连接
    * @return  错误码
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

写入从站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  写入从站DO
    * @param   DOIndex  DO编号
    * @param   wirteNum  写入的数量
    * @param   status 写入的数值，最多写8个
    * @return  错误码
    */
    public int FieldBusSlaveWriteDO(int DOIndex, int wirteNum, int[] status)

写入从站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  写入从站AO
    * @param  AOIndex  AO编号
    * @param  wirteNum  写入的数量
    * @param  status 写入的数值，最多写8个
    * @return  错误码
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int wirteNum, int[] status)

读取从站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  读取从站DI
    * @param  DOIndex  DI编号
    * @param  readNum  读取的数量
    * @param  status 读取到的数值，最多读8个
    * @return  错误码
    */
    public int FieldBusSlaveReadDI(int DOIndex, int readNum, int[] status)

读取从站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  读取从站AI
    * @param  AIIndex  AI编号
    * @param  readNum  读取的数量
    * @param  status 读取到的数值，最多读8个
    * @return  错误码
    */
    public int FieldBusSlaveReadAI(int AIIndex, int readNum, double[] status)

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param  DIIndex DI编号
    * @param  status 0-低电平；1-高电平
    * @param  waitMs 最大等待时间(ms)
    * @return 错误码
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param  AIIndex AI编号
    * @param  waitType 0-大于；1-小于
    * @param  value AI值
    * @param  waitMs 最大等待时间(ms)
    * @return 错误码
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

从站模式相关接口指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testFieldBusBoard(Robot robot)
    {
        //上传并加载开放协议文件
        robot.OpenLuaUpload("D://zUP/1111/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);
        int[] type=new int[1];
        int[] version=new int[1];
        int[] connState=new int[1];
        //获取从站板卡的协议类型、软件版本、与PLC的连接状态
        robot.GetFieldBusConfig(type, version, connState);
        System.out.println("type is: "+type[0]+", version is : "+version[0]+", connState is : "+connState[0]);
        //写入DO0 = 1、DO1 = 0、DO2 = 1
        int[] ctrl =new int[8];
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
        //写入AO2 = 0x1000
        int[] ctrlAO =new int[8];
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);
        int[] DI=new int[4];
        double[] AI=new double[3];
        //循环监控DI0~DI3 AI0~AI2
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            System.out.println("DI0 is: "+DI[0]+", DI1 is: "+DI[1]+",DI2 is: "+DI[2]+",DI3 is: "+DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            System.out.println("AI0 is: "+AI[0]+ ",AI1 is: "+AI[1]+",AI2 is: "+AI[2]);
            robot.Sleep(10);
        }
        //等待DI0是否为1，等待时间100ms，并打印结果
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        System.out.println("FieldBusSlaveWaitDI result is: "+ ret);
        //等待AI0是否大于400，等待时间100ms，并打印结果
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        System.out.println("FieldBusSlaveWaitAI result is: "+ ret);
        robot.CloseRPC();
    }

控制阵列式吸盘
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 控制阵列式吸盘
    * @param  slaveID 从站号
    * @param  len 长度
    * @param  ctrlValue 控制值 1-按最大真空度吸取 2-按设定真空度吸取 3-停止吸取
    * @return 错误码
    */
    public int SetSuckerCtrl(int slaveID, int len, int[] ctrlValue)

获取阵列式吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 获取阵列式吸盘状态
    * @param  slaveID 从站号
    * @param  state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param  pressValue 当前真空度 单位kpa
    * @param  error 吸盘当前的错误码
    * @return 错误码
    */
    public int GetSuckerState(int slaveID, int[] state, int[] pressValue, int[] error)

等待吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待吸盘状态
    * @param  slaveID 从站号
    * @param  state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param  ms 等待最大时间
    * @return 错误码
    */
    public int WaitSuckerState(int slaveID, int state, int ms)

阵列式吸盘控制指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testSucker(Robot robot)
    {
        //上传并加载开放协议文件
        robot.OpenLuaUpload("C：//项目/外设SDK/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);
        //控制吸盘广播模式下，按照最大能力吸附
        int[] ctrl = {1};
        robot.SetSuckerCtrl(0, 1, ctrl);
        int[] state=new int[1];
        int[] pressVlaue=new int[1];
        int[] error=new int[1];
        //循环监控1号吸盘和12号吸盘的状态
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, state,pressVlaue, error);
            System.out.println("sucker1 state is:"+state[0]+",pressVlaue is:"+pressVlaue[0]+",error num is"+error[0]);
            robot.GetSuckerState(12, state, pressVlaue, error);
            System.out.println("sucker12 state is :"+state[0]+", pressVlaue is:"+pressVlaue[0]+",error num is:"+error[0]);
            robot.Sleep(100);
        }
        //等待1号吸盘是否为吸附到物体的状态，等待时间100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        System.out.println("WaitSuckerState result is:"+ ret);
        //单播模式关闭1号和12号吸盘
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
        robot.CloseRPC();
    }

激光外设打开关闭函数
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光外设打开关闭函数
     * @param [in] OnOff 0-关闭 1-打开
     * @param [in] weldId 焊缝ID 默认为0
     * @return 错误码
     */
    public int LaserTrackingLaserOnOff(int OnOff, int weldId)
    
激光跟踪开始结束函数
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:
    
    /**
     * @brief 激光跟踪开始结束函数
     * @param [in] OnOff 0-结束 1-开始
     * @param [in] coordId 激光外设工具坐标系编号
     * @return 错误码
     */
    public int LaserTrackingTrackOnOff(int OnOff, int coordId)

激光寻位-固定反向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光寻位-固定反向
     * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
     * @param [in] vel 速度 单位%
     * @param [in] distance 最大寻位距离 单位mm
     * @param [in] timeout 寻位超时时间 单位ms
     * @param [in] posSensorNum 激光标定的工具坐标编号
     * @return 错误码
     */
    public int LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum)
    
激光寻位-任意方向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光寻位-任意方向
     * @param [in] directionPoint 寻位输入的点的xyz左边
     * @param [in] vel 速度 单位%
     * @param [in] distance 最大寻位距离 单位mm
     * @param [in] timeout 寻位超时时间 单位ms
     * @param [in] posSensorNum 激光标定的工具坐标编号
     * @return 错误码
     */
    public int LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum)
   
激光寻位结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
   :linenos:

   /**
    * @brief  激光寻位结束
    * @return 错误码
    */
    public int LaserTrackingSearchStop()

激光IP配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
   :linenos:

    /**
     * @brief 激光IP配置
     * @param [in] ip 激光外设的ip地址
     * @param [in] port 激光外设的端口号
     * @return 错误码
     */
    public int LaserTrackingSensorConfig(String ip, int port)

激光外设采样周期配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光外设采样周期配置
     * @param [in] period 激光外设采样周期 单位ms
     * @return 错误码
     */
    public int LaserTrackingSensorSamplePeriod(int period)

激光外设驱动加载
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光外设驱动加载
     * @param [in] type 激光外设驱动的协议类型 101-睿牛 102-创想 103-全视 104-同舟 105-奥太
     * @return 错误码
     */
    public int LoadPosSensorDriver(int type)

激光外设驱动卸载
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光外设驱动卸载
     * @return 错误码
     */
    public int UnLoadPosSensorDriver()

激光焊缝轨迹记录
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光焊缝轨迹记录
     * @param [in] status 0-停止记录 1-实时跟踪  2-开始记录
     * @param [in] delayTime 延时时间 单位ms
     * @return 错误码
     */
    public int LaserSensorRecord1(int status, int delayTime)

激光焊缝轨迹复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光焊缝轨迹复现
     * @param [in] delayTime 延时时间 单位ms
     * @param [in] speed 速度 单位%
     * @return 错误码
     */
    public int LaserSensorReplay(int delayTime, double speed)

激光跟踪复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 激光跟踪复现
     * @return 错误码
     */
    public int MoveLTR()

激光焊缝轨迹复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief 激光焊缝轨迹复现
    * @param delayMode 模式 0-延时时间 1-延时距离
    * @param delayTime 延时时间 单位ms
    * @param delayDisExAxisNum 扩展轴编号
    * @param delayDis 延时距离 单位mm
    * @param sensitivePara 补偿灵敏系数
    * @param trackMode 定点跟踪类型。0-扩展轴异步运动；1-机器人
    * @param triggerMode 定点跟踪触发方式。0-跟踪时长；1-IO
    * @param runTime 机器人定点跟踪时长(s)
    * @param speed 速度 单位%
    * @return 错误码
    */
    public int LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum, double delayDis, double sensitivePara, int trackMode, int triggerMode, double runTime, double speed)
    
运动到焊缝记录的起点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 运动到焊缝记录的起点
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 单位%
     * @return 错误码
     */
    public int MoveToLaserRecordStart(int moveType, double ovl)

运动到焊缝记录的终点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 运动到焊缝记录的终点
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 单位%
     * @return 错误码
     */
    public int MoveToLaserRecordEnd(int moveType, double ovl)

运动到激光传感器寻位点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 运动到激光传感器寻位点
     * @param [in] moveFlag 运动类型：0-PTP；1-LIN
     * @param [in] ovl 速度缩放因子，0-100
     * @param [in] dataFlag 焊缝缓存数据选择：0-执行规划数据；1-执行记录数据
     * @param [in] plateType 板材类型：0-波纹板；1-瓦楞板；2-围栏板；3-油桶；4-波纹甲壳钢
     * @param [in] trackOffectType 激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
     * @param [in] offset 偏移量
     * @return 错误码
     */
    public int MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset)
    
获取激光传感器寻位点坐标信息
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取激光传感器寻位点坐标信息
     * @param [in] trackOffectType 激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
     * @param [in] offset 偏移量
     * @param [out] jPos 关节位置[°]
     * @param [out] descPos 笛卡尔位置[mm]
     * @param [out] tool 工具坐标系
     * @param [out] user 工件坐标系
     * @param [out] exaxis 扩展轴位置[mm]
     * @return 错误码
     */
    public int GetLaserSeamPos(int trackOffectType, DescPose offset, JointPos jPos, DescPose descPos, int[] tool, int[] user, ExaxisPos exaxis)

激光外设传感器参数配置及调试代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLaserConfig(Robot robot)
    {
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);

        robot.LaserTrackingSensorSamplePeriod(20);

        robot.LoadPosSensorDriver(101);
        robot.LaserTrackingLaserOnOff(0,0);

        robot.Sleep(3000);

        robot.LaserTrackingLaserOnOff(1, 0);

        robot.CloseRPC();
    }

激光轨迹扫描及轨迹复现的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLaserRecordAndReplay(Robot robot)
    {
        //上传并加载开放协议文件
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);

        for (int i=0;i<10;++i){
            JointPos startjointPos=new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose=new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
            DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserSensorRecord1(2, 10);

            JointPos endjointPos=new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose=new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 50, 100, 100, -1,0, exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserSensorRecord1(0, 10);

            robot.MoveToLaserRecordStart(1, 30);

            robot.LaserSensorReplay(10, 100);

            robot.MoveLTR();

            robot.LaserSensorRecord1(0, 10);
        }

        robot.CloseRPC();
    }

激光寻位及实时跟踪的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLasertrack(Robot robot)
    {
        //上传并加载开放协议文件
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        for(int i=0;i<10;++i){
            JointPos startjointPos=new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose=new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
            DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
            DescTran directionPoint=new DescTran();
            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3);
            robot.LaserTrackingSearchStop();

            //robot.GetRobotTeachingPoint(name, data);
            robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);
            //printf("%f, %f, %f,%f, %f, %f,%f, %f, %f,%f, %f, %f\n", data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]);

            robot.LaserTrackingTrackOnOff(1, 3);
            //robot.LaserTrackingTrackOn(3);
            JointPos endjointPos=new JointPos(68.809,-87.100,121.120,-127.233,-95.038,-109.555);
            DescPose enddescPose=new DescPose(-103.555,-464.234,13.076,174.179,-1.344,-91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 0,1, 1);

            robot.LaserTrackingTrackOnOff(0, 3);
            System.out.println("当前是第"+(i+1)+"次");
        }
        robot.CloseRPC();
    }

扩展轴与机器人同步进行激光跟踪的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testLasertrackandExitAxis(Robot robot)
    {
        ExaxisPos startexaxisPos =new ExaxisPos( 0,0,0,0 );
        ExaxisPos seamexaxisPos = new ExaxisPos(-10,0,0,0 );
        ExaxisPos endexaxisPos = new ExaxisPos(-30, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0 );
        JointPos seamjointPos=new JointPos(0, 0, 0, 0, 0, 0);
        DescPose seamdescPose=new DescPose(0, 0, 0, 0, 0, 0);

        for(int i =0;i<10;++i) {
            //运动到需要寻位的起始点
            JointPos startjointPos = new JointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose = new DescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);

            System.out.println("11111");
            //沿着-y方向开始寻位
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            System.out.println("2222");
            int[] tool = new int[1];
            int[] user = new int[1];
            robot.GetLaserSeamPos(0, offdese, seamjointPos, seamdescPose, tool, user, startexaxisPos);
            System.out.println(seamjointPos.J1 + ", " + seamjointPos.J2 + ", " +
                    seamjointPos.J3 + ", " + seamjointPos.J4 + ", " +
                    seamjointPos.J5 + ", " + seamjointPos.J6 + ", " +
                    seamdescPose.tran.x + ", " + seamdescPose.tran.y + ", " +
                    seamdescPose.tran.z + ", " + seamdescPose.rpy.rx + ", " +
                    seamdescPose.rpy.ry + ", " + seamdescPose.rpy.rz);
            //如果寻位成功
            if (ret == 0) {
                //机器人和扩展轴同步运动到寻位点
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);

                //开始沿着寻位点进行激光跟踪并与扩展轴同步运动
                System.out.println("3333");
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos = new JointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose = new DescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);
                ;
                //停止跟踪
                robot.LaserTrackingTrackOnOff(0, 2);
                System.out.println("44444");
            }
            System.out.println("当前运行次数为:"+i);
        }
        robot.CloseRPC();
    }

末端透传功能打开关闭SDK接口
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 开启末端通用透传功能
    * @param 使能，0-关闭，1-开启
    * @return 错误码
    */
    public int SetAxleGenComEnable(int mode)

末端透传功能非周期数据收发SDK接口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端发送非周期数据并等待应答
    * @param lenSnd 发送的长度
    * @param sndBuff 发送数据
    * @param lenRcv 选择接受的长度
    * @param [out] rcvData 应答的数据
    * @return 错误码
    */
    public int SndRcvAxleGenComCmdData(int lenSnd, int[] sndBuff, int lenRcv, int[] rcvData)
    
基于末端透传功能倍益康艾灸头非周期数据通信代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testAxleGenCom(Robot robot) {
    int[] led_on = {0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79};
    int[] led_off = {0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78};
    int[] version = {0xAB, 0xBA, 0x11, 0x00, 0x76};
    int[] state = {0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B};

    int[] rcvdata = new int[16];
    int ret = 0;
    int cnt = 1;

    JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
    DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

    JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
    DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

    ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
    DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

    // 开启末端透传功能
    robot.SetAxleGenComEnable(1);
    robot.SetAxleLuaEnable(1);

    while (cnt <= 10000) {
        // 读取版本号
        ret = robot.SndRcvAxleGenComCmdData(5, version, 10, rcvdata);
        if (ret == 0) {
            System.out.printf(" hard version : %d,hard code:%d, soft version:%d %d, soft code:%d \n",
                    rcvdata[4], rcvdata[5], rcvdata[6], rcvdata[7], rcvdata[8]);
        } else {
            System.out.println("SndRcvAxleGenComCmdData version fail: " + ret);
            break;
        }
        robot.Sleep(1000);

        // 读取艾灸头在位状态
        ret = robot.SndRcvAxleGenComCmdData(6, state, 6, rcvdata);
        if (ret == 0) {
            System.out.printf(" state : %d \n", rcvdata[4]);
        }
        robot.Sleep(1000);

        // 开启艾灸头激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, rcvdata);
        if (ret == 0) {
            System.out.printf("led on rcv data is: %d, %d, %d, %d, %d, %d\n",
                    rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        }
        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100.0, 100.0, 100.0, exaxisPos, -1.0, 0, offdese);
        robot.Sleep(4000);

        // 关闭艾灸头激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, rcvdata);
        if (ret == 0) {
            System.out.printf("led off rcv data is: %d, %d, %d, %d, %d, %d \n",
                    rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        }
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100.0, 100.0, 100.0, exaxisPos, -1.0, 0, offdese);
        robot.Sleep(1000);

        System.out.println("***********************complete No. " + cnt + " SDK test*****************************");
        cnt++;
    }
    }  
    
下载开放协议Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 下载开放协议Lua文件
    * @param fileName 开放协议文件名称“CtrlDev_XXX.lua”
    * @param savePath 开放协议保存文件路径
    * @return 错误码
    */
    public int OpenLuaDownload(string fileName, string savePath)

删除开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief 删除开放协议Lua文件
    * @param [in] fileName 要删除的开放协议lua文件名“CtrlDev_XXX.lua”
    * @return 错误码
    */
    public int OpenLuaDelete(string fileName)
        
删除所有开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    /**
    * @brief 删除所有开放协议Lua文件
    * @return 错误码
    */
    public int AllOpenLuaDelete()

控制器外设开放协议上传下载删除代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: Java
    :linenos:

    public static int TestCtrlOpenLuaOperate(Robot robot) {
        int rtn;
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        System.out.println("OpenLuaUpload rtn is " + rtn);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        System.out.println("OpenLuaUpload rtn is " + rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        System.out.println("OpenLuaDownload rtn is " + rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        System.out.println("OpenLuaDownload rtn is " + rtn);

        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        System.out.println("SetCtrlOpenLUAName rtn is " + rtn);
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        System.out.println("SetCtrlOpenLUAName rtn is " + rtn);

        String[] names = new String[4];
        rtn = robot.GetCtrlOpenLUAName(names);
        System.out.println("GetCtrlOpenLUAName rtn is " + rtn + ", names: " +
                names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3]);

        rtn = robot.LoadCtrlOpenLUA(1);
        System.out.println("LoadCtrlOpenLUA rtn is " + rtn);
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        System.out.println("UnloadCtrlOpenLUA rtn is " + rtn);

        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        System.out.println("OpenLuaDelete rtn is " + rtn);
        rtn = robot.AllOpenLuaDelete();
        System.out.println("AllOpenLuaDelete rtn is " + rtn);

        robot.Sleep(1000);
        return 0;
    }