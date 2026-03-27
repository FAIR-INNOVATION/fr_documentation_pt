机器人力控
============

.. toctree:: 
    :maxdepth: 5

力传感器配置
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置力传感器
    * @param  [in] company  力传感器厂商，17-坤维科技
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int FT_SetConfig(int company, int device, int softvesion, int bus); 

获取力传感器配置 
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取力传感器配置 
    * @param [out] deviceID 力传感器编号 
    * @param [out] company 力传感器厂商，，力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯
    * @param [out] device  设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI (0-AXIA80 -M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A) 
    * @param [out] softvesion 软件版本号，暂不使用，默认为 0 
    * @return 错误码 
    */ 
    int FT_GetConfig(ref int deviceID, ref int company, ref int device, ref int softvesion); 

力传感器激活
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器激活
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int FT_Activate(byte act); 

力传感器校零
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器校零
    * @param  [in] act  0-去除零点，1-零点矫正
    * @return  错误码
    */
    int FT_SetZero(byte act); 

设置力传感器参考坐标系
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器参考坐标系
    * @param  [in] ref  0-工具坐标系，1-基坐标系
    * @return  错误码
    */
    int FT_SetRCS(byte type); 

设置力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器下负载重量
    * @param  [in] weight 负载重量 kg
    * @return  错误码
    */
    int SetForceSensorPayLoad(double weight);

设置力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器下负载质心
    * @param  [in] x 负载质心x mm 
    * @param  [in] y 负载质心y mm
    * @param  [in] z 负载质心z mm
    * @return  错误码
    */
    int SetForceSensorPayLoadCog(double x, double y, double z);

获取力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器下负载重量
    * @param  [in] weight 负载重量 kg
    * @return  错误码
    */
    int GetForceSensorPayLoad(ref double weight);

获取力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器下负载质心
    * @param  [out] x 负载质心x mm 
    * @param  [out] y 负载质心y mm
    * @param  [out] z 负载质心z mm
    * @return  错误码
    */
    int GetForceSensorPayLoadCog(ref double x, ref double y, ref double z);

力传感器自动校零
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器自动校零
    * @param  [out] weight 传感器质量 kg 
    * @param  [out] pos 传感器质心 mm
    * @return  错误码
    */
    int ForceSensorAutoComputeLoad(ref double weight, ref DescTran pos);

获取参考坐标系下力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取参考坐标系下力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueRCS(byte flag, ref ForceTorque ft); 

获取力传感器原始力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器原始力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueOrigin(byte flag, ref ForceTorque ft); 

力传感器配置及自动校零代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button54_Click(object sender, EventArgs e)
    {
        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin:{ft.fx},{ft.fy},{ft.fz},{ft.tx},{ft.ty},{ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose ftCoord = new DescPose(0, 0, 0, 0, 0, 0);
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayLoad(0.824);
        robot.SetForceSensorPayLoadCog(0.778, 2.554, 48.765);
        double weight = 0;
        double x = 0, y = 0, z = 0;
        robot.GetForceSensorPayLoad(ref weight);
        robot.GetForceSensorPayLoadCog(ref x, ref y, ref z);
        Console.WriteLine($"the FT load is {weight}, {x} {y} {z}");

        robot.SetForceSensorPayLoad(0);
        robot.SetForceSensorPayLoadCog(0, 0, 0);

        double computeWeight = 0;
        DescTran tran = new DescTran(0, 0, 0);
        robot.ForceSensorAutoComputeLoad(ref weight, ref tran);
        Console.WriteLine($"the result is weight {weight} pos is {tran.x} {tran.y} {tran.z}");

    } 

负载重量辨识记录
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载重量辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @return  错误码
    */
    int FT_PdIdenRecord(int id);

负载重量辨识计算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载重量辨识计算
    * @param  [out] weight  负载重量，单位kg
    * @return  错误码
    */   
    int FT_PdIdenCompute(ref double weight);

负载质心辨识记录
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载质心辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @param  [in] index 点编号，范围[1~3]
    * @return  错误码
    */
    int FT_PdCogIdenRecord(int id, int index); 

负载质心辨识计算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载质心辨识计算
    * @param  [out] cog  负载质心，单位mm
    * @return  错误码
    */   
    int FT_PdCogIdenCompute(ref DescTran cog);

力传感器负载辨识代码示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTPdCog_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin: {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose tcoord = new DescPose(0, 0, 35.0, 0, 0, 0);
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        Thread.Sleep(1000);

        double weight = 0.0f;
        robot.FT_PdIdenCompute(ref weight);
        Console.WriteLine($"payload weight: {weight}");

        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);

        DescTran cog = new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(ref cog);
        Console.WriteLine($"cog: {cog.x}, {cog.y}, {cog.z}");
    }

碰撞守护
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int FT_Guard(int flag, int sensor_id, int[] select, ForceTorque ft, double[] max_threshold, double[] min_threshold); 

碰撞守护代码示例
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTGuard_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte sensor_id = 1;
        int[] select = { 1, 1, 1, 1, 1, 1 };
        double[] max_threshold = { 10.0f, 10.0f, 10.0f, 10.0f, 10.0f, 10.0f };
        double[] min_threshold = { 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f };

        ForceTorque ft = new ForceTorque();
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.FT_Guard(1, sensor_id, select,  ft, max_threshold, min_threshold);
        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);

        robot.FT_Guard(0, sensor_id, select, ft, max_threshold, min_threshold);
    }

恒力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  恒力控制
    * @param  [in] flag 0-关闭恒力控制，1-开启恒力控制
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid参数，力矩pid参数
    * @param  [in] adj_sign 自适应启停控制，0-关闭，1-开启
    * @param  [in] ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
    * @param  [in] max_dis 最大调整距离，单位mm
    * @param  [in] max_ang 最大调整角度，单位deg
    * @param  [in] M rx、ry质量参数[0.1-10],默认2
    * @param  [in] B rx、ry阻尼参数[0.1-50],默认8
    * @param  [in] threshold rx、ry启动阈值[0-10],默认0.2
    * @param  [in] adjustCoeff rx、ry力矩调节系数[0-1],默认1
    * @param  [in] polishRadio 打磨半径，单位mm
    * @param  [in] filter_Sign 滤波开启标志 0-关；1-开，默认关闭
    * @param  [in] posAdapt_sign 姿态顺应开启标志 0-关；1-开，默认关闭
    * @param  [in] isNoBlock 阻塞标志，0-阻塞；1-非阻塞
    * @return  错误码
    */
    public int FT_Control(byte flag, int sensor_id, byte[] select, ForceTorque ft, float[] ft_pid,byte adj_sign, byte ILC_sign, float max_dis, float max_ang,double[] M, double[] B, double[] threshold, double[] adjustCoeff,double polishRadio, int filter_Sign, int posAdapt_sign, int isNoBlock)

具有阻尼的恒力控制代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public void TestFTControlWithAdjustCoeff()
    {
        int rtn;
        int sensor_id = 10;
        byte[] select = new byte[6] { 0, 0, 1, 0, 0, 0 };
        float[] ft_pid = new float[6] { 0.0008f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 1000.0f;
        float max_ang = 20.0f;
        ForceTorque ft = new ForceTorque();
        ft.fz = -10.0f;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        JointPos j1 = new JointPos(80.765f, -98.795f, 106.548f, -97.734f, -89.999f, 94.842f);
        JointPos j2 = new JointPos(43.067f, -84.429f, 92.620f, -98.175f, -90.011f, 57.144f);
        DescPose desc_p1 = new DescPose(5.009f, -547.463f, 262.053f, -179.999f, -0.019f, 75.923f);
        DescPose desc_p2 = new DescPose(-347.966f, -547.463f, 262.048f, -180.000f, -0.019f, 75.923f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        double[] M = new double[2] { 2.0, 2.0 };
        double[] B = new double[2] { 15.0, 15.0 };
        double[] threshold = new double[2] { 1.0, 1.0 };
        double[] adjustCoeff = new double[2] { 1.0, 0.8 };
        double polishRadio = 0.0;
        int filter_Sign = 0;
        int posAdapt_sign = 1;
        int isNoBlock = 0;
        while (true)
        {
            rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            Console.WriteLine($"FT_Control start rtn is {rtn}");
            robot.MoveL(j1, desc_p1, 1, 0, 100, 100, 100, -1, 0, epos, 0, 0, offset_pos, 0, 0, 10);
            robot.MoveL(j2, desc_p2, 1, 0, 100, 100, 100, -1, 0, epos, 0, 0, offset_pos, 0, 0, 10);
            rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            Console.WriteLine($"FT_Control end rtn is {rtn}");
        }
    }

旋转插入
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 旋转插入
    * @param [in] rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param [in] angVelRot 旋转角速度，单位deg/s
    * @param [in] ft 力/扭矩阈值，fx,fy,fz,tx,ty,tz，范围[0~100]
    * @param [in] max_angle 最大旋转角度，单位deg
    * @param [in] orn 力/扭矩方向，1-沿z轴方向，2-绕z轴方向
    * @param [in] max_angAcc 最大旋转加速度，单位deg/s^2，暂不使用，默认为0
    * @param [in] rotorn 旋转方向，1-顺时针，2-逆时针
    * @param [in] strategy 未检测到力/力矩的处理策略，0-报错；1-警告，继续运动
    * @return 错误码
    */
    public int FT_RotInsertion(int rcs, double angVelRot, double ft, double max_angle, int orn, double max_angAcc, int rotorn, int strategy)

机器人力传感器旋转插入代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public void TestMove()
    {
        int rtn;
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos j2 = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos j3 = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);
        JointPos j4 = new JointPos(-31.154f, -95.317f, 94.276f, -88.079f, -89.740f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose desc_pos2 = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose desc_pos3 = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);
        DescPose desc_pos4 = new DescPose(-443.165f, 147.881f, 480.951f, 179.511f, -0.775f, -15.409f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float oacc = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos,j1, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        Console.WriteLine($"MoveCart errcode:{rtn}");
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,desc_pos4, tool, user, vel, acc, epos, flag, offset_pos,ovl, blendR, -1, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
    }

柔顺控制开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔顺控制开启
    * @param  [in] p 位置调节系数或柔顺系数
    * @param  [in] force 柔顺开启力阈值，单位N
    * @return  错误码
    */   
    int FT_ComplianceStart(float p, float force);

柔顺控制关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔顺控制关闭
    * @return  错误码
    */   
    int FT_ComplianceStop(); 

柔顺控制代码示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnComplience_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte flag = 1;
        int sensor_id = 1;
        int[] select = { 1, 1, 1, 0, 0, 0 };
        double[] ft_pid = { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0, ILC_sign = 0;
        float max_dis = 100.0f, max_ang = 0.0f;

        ForceTorque ft = new ForceTorque { fx = -10.0, fy = -10.0, fz = -10.0 };
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        float p = 0.00005f;
        float force = 30.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        Console.WriteLine($"FT_ComplianceStart rtn is {rtn}");

        int count = 5;
        while (count-- > 0)
        {
        robot.MoveL(j1, desc_p1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 1, offset_pos);
        robot.MoveL(j2, desc_p2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 0, offset_pos);
        }

        robot.FT_ComplianceStop();
        Console.WriteLine($"FT_ComplianceStop rtn is {rtn}");

        flag = 0;
        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
    }

负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识初始化
    * @return 错误码
    */
    int LoadIdentifyDynFilterInit();

负载辨识变量初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识变量初始化
    * @return 错误码
    */
    int LoadIdentifyDynVarInit();

负载辨识主程序
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识主程序
    * @param [in] joint_torque 关节扭矩
    * @param [in] joint_pos 关节位置
    * @param [in] t 采样周期
    * @return 错误码
    */
    int LoadIdentifyMain(double[] joint_torque, double[] joint_pos, double t);

获取负载辨识结果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取负载辨识结果
    * @param [in] gain  重力项系数double[6]，离心项系数double[6]
    * @param [out] weight 负载重量
    * @param [out] cog 负载质心
    * @return 错误码
    */
    int LoadIdentifyGetResult(double[] gain, ref double weight, ref DescTran cog);

机器人负载辨识代码示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button74_Click(object sender, EventArgs e)
    {
        int rtn;
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();
        Console.WriteLine("LoadIdentifyDynFilterInit retval is: " + retval);

        retval = robot.LoadIdentifyDynVarInit();
        Console.WriteLine("LoadIdentifyDynVarInit retval is: " + retval);

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0, 0, 0, 0, 0, 0);
        double[] joint_toq = new double[6] { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        robot.GetActualJointPosDegree(0, ref posJ);
        posJ.jPos[1] = posJ.jPos[1] + 10;
        robot.GetJointTorques(0, joint_toq);
        joint_toq[1] = joint_toq[1] + 2;

        double[] tmpTorque = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        for (int i = 0; i < 6; i++)
        {
            tmpTorque[i] = joint_toq[i];
        }

        retval = robot.LoadIdentifyMain(tmpTorque, posJ.jPos, 1);
        Console.WriteLine("LoadIdentifyMain retval is: " + retval);

        double[] gain = new double[12] { 0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0 };
        double weight = 0;
        DescTran load_pos = new DescTran(0, 0, 0);
        retval = robot.LoadIdentifyGetResult(gain, ref weight, ref load_pos);
        Console.WriteLine("LoadIdentifyGetResult retval is: {0}; weight is {1} cog is {2} {3} {4}", retval, weight, load_pos.x, load_pos.y, load_pos.z);
    }

力传感器辅助拖动
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器辅助拖动
    * @param  [in] status 控制状态，0-关闭；1-开启
    * @param  [in] asaptiveFlag 自适应开启标志，0-关闭；1-开启
    * @param  [in] interfereDragFlag 干涉区拖动标志，0-关闭；1-开启
    * @param  [in] ingularityConstraintsFlag 奇异点策略，0-规避；1-穿越
    * @param  [in] forceCollisionFlag 辅助拖动时机器人碰撞检测标志；0-关闭；1-开启
    * @param  [in] M 惯性系数
    * @param  [in] B 阻尼系数
    * @param  [in] K 刚度系数
    * @param  [in] F 拖动六维力阈值
    * @param  [in] Fmax 最大拖动力限制 Nm
    * @param  [in] Vmax 最大关节速度限制 °/s
    * @return  错误码
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag,int forceCollisionFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);
    
获取力传感器拖动开关状态
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器拖动开关状态
    * @param  [out] dragState 力传感器辅助拖动控制状态，0-关闭；1-开启
    * @param  [out] sixDimensionalDragState 六维力辅助拖动控制状态，0-关闭；1-开启
    * @return  错误码
    */
    int GetForceAndTorqueDragState(ref int dragState, ref int sixDimensionalDragState);

报错清除后力传感器自动开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  报错清除后力传感器自动开启
    * @param  [in] status 控制状态，0-关闭；1-开启
    * @return  错误码
    */
    int SetForceSensorDragAutoFlag(int status);

力传感器辅助拖动代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button61_Click(object sender, EventArgs e)
    {
        robot.SetForceSensorDragAutoFlag(1);
        double[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        double[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        double[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };

        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);
        robot.WaitMs(5000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        robot.GetForceAndTorqueDragState(ref dragState, ref sixDimensionalDragState);
        Console.WriteLine($"the drag state is {dragState} {sixDimensionalDragState}");

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
    }

设置六维力和关节阻抗混合拖动开关及参数
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置六维力和关节阻抗混合拖动开关及参数
    * @param  [in] status 控制状态，0-关闭；1-开启
    * @param  [in] impedanceFlag 阻抗开启标志，0-关闭；1-开启
    * @param  [in] lamdeDain 拖动增益
    * @param  [in] KGain 刚度增益
    * @param  [in] BGain 阻尼增益
    * @param  [in] dragMaxTcpVel 拖动末端最大线速度限制
    * @param  [in] dragMaxTcpOriVel 拖动末端最大角速度限制
    * @return  错误码
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, double[] lamdeDain, double[] KGain, double[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

力传感器辅助拖动代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button62_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        double[] lambdaGain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        double[] kGain = { 0, 0, 0, 0, 0, 0 };
        double[] bGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
        Thread.Sleep(5000); 
        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
    }

阻抗启停控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestImpedanceControl()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        int rtn;
        JointPos j1 = new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2 = new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1 = new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2 = new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
    
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
    
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 200.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendR = -1.0f;
    
        byte flag = 0;
    
        byte search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);
    
        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);
        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);
        robot.FT_SetZero(1);
        Thread.Sleep(1000);
    
        double[] forceThreshold = new double[] { 30, 30, 30, 5, 5, 5 };
        double[] m = new double[] { 0.1, 0.1, 0.1, 0.02, 0.02, 0.02 };
        double[] b = new double[] { 1, 1, 1, 0.08, 0.08, 0.08 };
        double[] k = new double[] { 0, 0, 0, 0, 0, 0 };
        rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        Console.WriteLine($"ImpedanceControlStartStop errcode:{rtn}");
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        Console.WriteLine($"movel errcode:{rtn}");
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
    }

开启力矩补偿功能及补偿系数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 开启力矩补偿功能及补偿系数
    * @param [in] status 开关，0-关闭；1-开启
    * @param [in] torqueCoeff J1-J6力矩补偿系数[0-1]
    * @return 错误码
    */
    public int SerCoderCompenParams(int status, double[] torqueCoeff)

