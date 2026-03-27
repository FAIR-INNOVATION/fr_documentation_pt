机器人力控
============

.. toctree:: 
    :maxdepth: 5

配置力传感器
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置力传感器
    * @param  config company:力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯，23-NBIT，24-鑫精诚(XJC)，26-NSR
    * @param  config device: 设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精诚XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)
    * @param  config softvesion:软件版本号，暂不使用，默认为0
    * @param  config bus:设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int FT_SetConfig(DeviceConfig config); 

获取力传感器配置 
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取力传感器配置 
    * @param [out] config company:力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯
    * @param [out] config device:设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)
    * @param [out] config softvesion:软件版本号，暂不使用，默认为0
    * @param [out] config bus:设备挂在末端总线位置，暂不使用，默认为0
    * @return 错误码 
    */ 
    int FT_GetConfig(DeviceConfig config); 

力传感器激活
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力传感器激活
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int FT_Activate(int act); 

力传感器校零
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力传感器校零
    * @param  [in] act  0-去除零点，1-零点矫正
    * @return  错误码
    */
    int FT_SetZero(int act); 

设置力传感器参考坐标系
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置力传感器参考坐标系
    * @param  [in] type  0-工具坐标系，1-基坐标系, 2-自由坐标系
    * @param  [in] coord  自由坐标系值
    * @return  错误码
    */
    int FT_SetRCS(int type, DescPose coord);

设置力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置力传感器下负载重量
    * @param [in] weight 负载重量 kg
    * @return 错误码
    */
    int SetForceSensorPayLoad(double weight);

设置力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置力传感器下负载质心
    * @param [in] cog 负载质心 mm
    * @return 错误码
    */
    int SetForceSensorPayLoadCog(DescTran cog);

获取力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器下负载重量
    * @return List[0]:错误码; List[1] : weight 负载重量 kg
    */
    List<Number> GetForceSensorPayLoad();

获取力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器下负载质心
    * @param [out] cog 负载质心 mm
    * @return 错误码
    */
    int GetForceSensorPayLoadCog(DescTran cog);

力传感器自动校零
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器自动校零
    * @param [in] massCenter 传感器质量(kg) 及 质心(mm)
    * @return 错误码
    */
    int ForceSensorAutoComputeLoad(MassCenter massCenter);

获取参考坐标系下力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取参考坐标系下力/扭矩数据
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueRCS(int flag, ForceTorque ft); 

获取力传感器原始力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取力传感器原始力/扭矩数据
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueOrigin(int flag, ForceTorque ft); 

力传感器配置及自动校零代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTInit(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company,device,softversion,bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose ftCoord = new DescPose();
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayload(0.824);

        DescTran tr=new DescTran(0.778, 2.554, 48.765);
        robot.SetForceSensorPayloadCog(tr);
        List<Number> weight = new ArrayList<>();
        double x = 0, y = 0, z = 0;
        weight=robot.GetForceSensorPayload();
        robot.GetForceSensorPayloadCog(tr);
        tr.x=0;
        tr.y=0;
        tr.z=0;
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr);

        double computeWeight = 0;
        DescTran tran = new DescTran();
        MassCenter mass=new MassCenter();
        mass.weight=weight.get(1).doubleValue();
        mass.cog=tran;
        robot.ForceSensorAutoComputeLoad(mass);
        return 0;
    }

负载重量辨识记录
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载重量辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @return  错误码
    */
    int FT_PdIdenRecord(int id);

负载重量辨识计算
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载重量辨识计算
    * @return  List[0]:错误码; List[1] : double weight  负载重量，单位kg
    */   
    List<Number> FT_PdIdenCompute();

负载质心辨识记录
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载质心辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @param  [in] index 点编号，范围[1~3]
    * @return  错误码
    */
    int FT_PdCogIdenRecord(int id, int index); 

负载质心辨识计算
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载质心辨识计算
    * @param  [out] cog  负载质心，单位mm
    * @return  错误码
    */   
    int FT_PdCogIdenCompute(DescTran cog);

力传感器负载辨识代码示例
+++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTLoadCompute(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose tcoord = new DescPose();
        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        robot.Sleep(1000);

        List<Number> weight =new ArrayList<>();
        weight=robot.FT_PdIdenCompute();

        DescPose desc_p1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3=new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart(desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);
        robot.Sleep(1000);
        DescTran cog=new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(cog);

        robot.CloseRPC();
        return 0;
    }

碰撞守护
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  碰撞守护
    * @param  [in] flag 0-关闭碰撞守护，1-开启碰撞守护
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大阈值
    * @param  [in] min_threshold 最小阈值
    * @note   力/扭矩检测范围：(ft-min_threshold, ft+max_threshold)
    * @return  错误码
    */   
    int FT_Guard(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] max_threshold, Object[] min_threshold); 

碰撞守护代码示例
+++++++++++++++++++++++++++++++++++++++++++++
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
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 1, 0, 0, 0, 0, 0 };//只启用x轴碰撞守护
        Object[] max_threshold = { 5.0, 0.01, 0.01, 0.01, 0.01, 0.01 };
        Object[] min_threshold = { 3.0, 0.01, 0.01, 0.01, 0.01, 0.01 };

        ForceTorque ft = new ForceTorque(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        DescPose  desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(-14.404,-455.283,319.847,-172.935,25.141,-68.097);
        desc_p2 = new DescPose(-107.999,-599.174,285.939,153.472,12.686,-71.284);
        desc_p3 = new DescPose(6.586,-704.897,309.638,178.909,-27.759,-70.479);

        int rtn =  robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        System.out.println("FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
    }

恒力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恒力控制
    * @param  flag 0-关闭恒力控制，1-开启恒力控制
    * @param  sensor_id 力传感器编号
    * @param  select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  ft_pid 力pid参数，力矩pid参数
    * @param  adj_sign 自适应启停控制，0-关闭，1-开启
    * @param  ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
    * @param  max_dis 最大调整距离，单位mm
    * @param  max_ang 最大调整角度，单位deg
    * @param  M rx、ry质量参数[0.1-10],默认2
    * @param  B rx、ry阻尼参数[0.1-50],默认8
    * @param  threshold rx、ry启动阈值[0-10],默认0.2
    * @param  adjustCoeff rx、ry力矩调节系数[0-1],默认1
    * @param  polishRadio 打磨半径，单位mm
    * @param  filter_Sign 滤波开启标志 0-关；1-开，默认关闭
    * @param  posAdapt_sign 姿态顺应开启标志 0-关；1-开，默认关闭
    * @param  isNoBlock 阻塞标志，0-阻塞；1-非阻塞
    * @return  错误码
    */
    public int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang,double[] M,double[] B, double[] threshold, double[] adjustCoeff, double polishRadio,int filter_Sign, int posAdapt_sign, int isNoBlock)

具有阻尼的恒力控制代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTControlWithAdjustCoeff(Robot robot)
    {
        int sensor_id = 10;
        int[] select = { 0,0,1,0,0,0 };
        double[] ft_pid = { 0.0008, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 1000.0;
        double max_ang = 20;
        ForceTorque ft = new ForceTorque(0.0,0,0,0,0,0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        JointPos j1=new JointPos(80.765, -98.795, 106.548, -97.734, -89.999, 94.842);
        JointPos j2=new JointPos(43.067, -84.429, 92.620, -98.175, -90.011, 57.144);
        DescPose desc_p1=new DescPose(5.009, -547.463, 262.053, -179.999, -0.019, 75.923);
        DescPose desc_p2=new DescPose(-347.966, -547.463, 262.048, -180.000, -0.019, 75.923);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        double[] M = { 2.0, 2.0 };
        double[] B = { 15.0, 15.0 };
        double[] threshold = {1.0, 1.0};
        double[] adjustCoeff = {1.0, 0.8};
        double polishRadio = 0.0;
        int filter_Sign = 0;
        int posAdapt_sign = 1;
        int isNoBlock;
        ft.fz = -10.0;
        while(true)
        {
            int rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control start rtn is %d\n", rtn);
            robot.MoveL(j1, desc_p1, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            robot.MoveL(j2, desc_p2, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control end rtn is %d\n", rtn);
        }
    }

旋转插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 旋转插入
    * @param rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param angVelRot 旋转角速度，单位deg/s
    * @param ft  力/扭矩阈值，fx,fy,fz,tx,ty,tz，范围[0~100]
    * @param max_angle 最大旋转角度，单位deg
    * @param orn 力/扭矩方向，1-沿z轴方向，2-绕z轴方向
    * @param max_angAcc 最大旋转加速度，单位deg/s^2，暂不使用，默认为0
    * @param rotorn  旋转方向，1-顺时针，2-逆时针
    * @param strategy 未检测到力/力矩的处理策略，0-报错；1-警告，继续运动
    * @return  错误码
    */
    public int FT_RotInsertion(int rcs, double angVelRot, double ft, double max_angle, int orn, double max_angAcc, int rotorn, int strategy)

机器人力传感器旋转插入代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn=-1;
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4=new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4=new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

柔顺控制开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔顺控制开启
    * @param  [in] p 位置调节系数或柔顺系数
    * @param  [in] force 柔顺开启力阈值，单位N
    * @return  错误码
    */   
    int FT_ComplianceStart(double p, double force);

柔顺控制关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔顺控制关闭
    * @return  错误码
    */   
    int FT_ComplianceStop(); 

柔顺控制代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCompliance(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);

        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        int flag = 1;
        int sensor_id = 1;
        Object[] select =new Object[] { 1,1,1,0,0,0 };
        Object[] ft_pid =new Object[] { 0.0005,0.0,0.0,0.0,0.0,0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 100.0;
        double max_ang = 0.0;

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        DescPose  offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);


        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        double p = 0.00005;
        double force = 30.0;
        int rtn = robot.FT_ComplianceStart(p, force);

        int count = 15;
        while (count>0)
        {
            robot.MoveL(j1, desc_p1, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 1, offset_pos,0,10);
            robot.MoveL(j2, desc_p2, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 0, offset_pos,0,10);
            count -= 1;
        }
        robot.FT_ComplianceStop();
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);

        robot.CloseRPC();
        return 0;
    }

负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识初始化
    * @return 错误码
    */
    int LoadIdentifyDynFilterInit();

负载辨识变量初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识变量初始化
    * @return 错误码
    */
    int LoadIdentifyDynVarInit();

负载辨识主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识主程序
    * @param [in] joint_torque 关节扭矩
    * @param [in] joint_pos 关节位置
    * @param [in] t 采样周期
    * @return 错误码
    */
    int LoadIdentifyMain(Object[] joint_torque, Object[] joint_pos, double t);

获取负载辨识结果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取负载辨识结果
    * @param [in] gain
    * @return List[0]:错误码; List[1] : double weight 负载重量; List[2]: x 负载质心X mm; List[3] : y 负载质心Y mm; List[2]: z 负载质心Z mm
    */
    List<Number> LoadIdentifyGetResult(Object[] gain);

机器人负载辨识代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestIdentify(Robot robot)
    {
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();

        retval = robot.LoadIdentifyDynVarInit();

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0,0,0,0,0,0);
        List<Number> joint_toq=new ArrayList<>();
        robot.GetActualJointPosDegree( posJ);
        posJ.J2 = posJ.J2 + 10;
        joint_toq=robot.GetJointTorques(0);

        Object[] gain =new Object[] { 0,0.05,0,0,0,0,0,0.02,0,0,0,0 };
        double weight = 0;
        DescTran load_pos=new DescTran(0,0,0);
        List<Number> num=new ArrayList<>();
        num = robot.LoadIdentifyGetResult(gain);

        robot.CloseRPC();
        return 0;

    }

力传感器辅助拖动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器辅助拖动
    * @param [in] status 控制状态，0-关闭；1-开启
    * @param [in] asaptiveFlag 自适应开启标志，0-关闭；1-开启
    * @param [in] interfereDragFlag 干涉区拖动标志，0-关闭；1-开启
    * @param [in] ingularityConstraintsFlag 奇异点策略，0-规避；1-穿越
    * @param [in] forceCollisionFlag 辅助拖动时机器人碰撞检测标志；0-关闭；1-开启
    * @param [in] M 惯性系数
    * @param [in] B 阻尼系数
    * @param [in] K 刚度系数
    * @param [in] F 拖动六维力阈值
    * @param [in] Fmax 最大拖动力限制 Nm
    * @param [in] Vmax 最大关节速度限制 °/s
    * @return 错误码
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag, int forceCollisionFlag, Object[] M, Object[] B, Object[] K, Object[] F, double Fmax, double Vmax)

获取力传感器拖动开关状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器拖动开关状态
    * @return List[0]:错误码; List[1] : dragState 力传感器辅助拖动控制状态，0-关闭；1-开启; List[1] : sixDimensionalDragState 六维力辅助拖动控制状态，0-关闭；1-开启
    */
    List<Integer> GetForceAndTorqueDragState();

报错清除后力传感器自动开启
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 报错清除后力传感器自动开启
    * @param [in] status 控制状态，0-关闭；1-开启
    * @return 错误码
    */
    int SetForceSensorDragAutoFlag(int status)

力传感器辅助拖动代码示例
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestEndForceDragCtrl(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        robot.SetForceSensorDragAutoFlag(1);

        Object[] M =new Object[] { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        Object[] B =new Object[] { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        Object[] K =new Object[] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] F =new Object[] { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);

        robot.Sleep(10000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        List<Integer> state=new ArrayList<>();
        state=robot.GetForceAndTorqueDragState();

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
        return 0;
    }

设置六维力和关节阻抗混合拖动开关及参数
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置六维力和关节阻抗混合拖动开关及参数
    * @param [in] status 控制状态，0-关闭；1-开启
    * @param [in] impedanceFlag 阻抗开启标志，0-关闭；1-开启
    * @param [in] lamdeGain 拖动增益
    * @param [in] KGain 刚度增益
    * @param [in] BGain 阻尼增益
    * @param [in] dragMaxTcpVel 拖动末端最大线速度限制
    * @param [in] dragMaxTcpOriVel 拖动末端最大角速度限制
    * @return 错误码
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, Object[] lamdeGain, Object[] KGain, Object[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

六维力和关节阻抗混合拖动代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestForceAndJointImpedance(Robot robot)
    {
        robot.DragTeachSwitch(1);
        Object[] lamdeDain =new Object[] { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        Object[] KGain = new Object[]{ 0, 0, 0, 0, 0, 0 };
        Object[] BGain =new Object[] { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.Sleep(10000);

        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.CloseRPC();
        return 0;
    }

阻抗启停控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 阻抗启停控制
    * @param [in] status 0：关闭；1-开启
    * @param [in] workSpace 0-关节空间；1-迪卡尔空间
    * @param [in] forceThreshold 触发力阈值(N)
    * @param [in] m 质量参数
    * @param [in] b 阻尼参数
    * @param [in] k 刚度参数
    * @param [in] maxV 最大线速度(mm/s)
    * @param [in] maxVA 最大线加速度(mm/s2)
    * @param [in] maxW 最大角速度(°/s)
    * @param [in] maxWA 最大角加速度(°/s2)
    * @return 错误码
    */
    public int ImpedanceControlStartStop(int status, int workSpace, double[] forceThreshold, double[] m, double[] b, double[] k, double maxV, double maxVA, double maxW, double maxWA)


机器人阻抗启停控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestImpedanceControl(Robot robot)
    {
        JointPos j1=new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2=new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1=new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2=new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 200.0;
        double ovl = 100.0;
        double blendT = -1.0;
        double blendR = -1.0;
        int flag = 0;
        int search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        System.out.println("FT config:"+con.company+","+con.device+","+con.softwareVersion+"con"+ con.bus);
        robot.Sleep(1000);
        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);
        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);
        robot.FT_SetZero(1);
        robot.Sleep(1000);
        double[] forceThreshold = { 30,30,30,5,5,5 };
        double[] m= { 0.1,0.1,0.1,0.02,0.02,0.02 };
        double[] b = { 1,1,1,0.08,0.08,0.08 };
        double[] k = { 0,0,0,0,0,0 };
        int rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        System.out.println("ImpedanceControlStartStop errcode:"+ rtn);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        System.out.println("movel errcode:"+ rtn);
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        robot.CloseRPC();
        return 0;
    }

开启力矩补偿功能及补偿系数
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 开启力矩补偿功能及补偿系数
    * @param  status 开关，0-关闭；1-开启
    * @param  torqueCoeff J1-J6力矩补偿系数[0-1]
    * @return 错误码
    */
    public int SerCoderCompenParams(int status, double[] torqueCoeff)