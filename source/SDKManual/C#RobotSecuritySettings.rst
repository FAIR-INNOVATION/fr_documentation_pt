机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置碰撞等级
    * @param  [in]  mode  0-等级，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应范围[],百分比对应范围[0~1]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  错误码
    */
    int SetAnticollision(int mode, double[] level, int config); 

设置碰撞后策略
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置碰撞后策略
    * @param  [in] strategy  0-报错暂停；1-继续运行；2-报错停止；3-重力矩模式；4-震荡相应模式；5-碰撞回弹模式
    * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距离[1-150]mm
    * @param  [in] safeVel  tcp安全停止速度 [50-250]mm/s
    * @param  [in] safetyMargin  j1-j6安全系数[1-10]
    * @return  错误码
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel,int[] safetyMargin);

自定义碰撞检测阈值功能开始
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  自定义碰撞检测阈值功能开始，设置关节端和TCP端的碰撞检测阈值
    * @param  [in] flag 1-仅关节检测开启；2-仅TCP检测开启；3-关节和TCP检测同时开启
    * @param  [in] jointDetectionThreshould 关节碰撞检测阈值 j1-j6
    * @param  [in] tcpDetectionThreshould TCP碰撞检测阈值，xyzabc
    * @param  [in] block 0-非阻塞；1-阻塞
    * @return  错误码
    */
    int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

自定义碰撞检测阈值功能关闭
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  自定义碰撞检测阈值功能关闭
    * @return  错误码
    */
    int CustomCollisionDetectionEnd()

机器人碰撞等级设置代码示例
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button24_Click(object sender, EventArgs e)
    {
        int mode = 0;
        int config = 1;
        double[] level1 = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f };
        double[] level2 = { 50.0f, 20.0f, 30.0f, 40.0f, 50.0f, 60.0f };

        int rtn = robot.SetAnticollision(mode, level1, config);
        Console.WriteLine($"SetAnticollision mode 0 rtn is {rtn}");
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        Console.WriteLine($"SetAnticollision mode 1 rtn is {rtn}");

        JointPos p1Joint = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos p2Joint = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0.0f, 0.0f, 0.0f, 0.0f);
        DescPose offdese = new DescPose(0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, 2,  exaxisPos, 0, 0,  offdese);
        robot.ResetAllError();
        int[] safety = { 5, 5, 5, 5, 5, 5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        Console.WriteLine($"SetCollisionStrategy rtn is {rtn}");

        double[] jointDetectionThreshould = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould = { 60, 60, 60, 60, 60, 60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        Console.WriteLine($"CustomCollisionDetectionStart rtn is {rtn}");

        robot.MoveL( p1Joint,  p1Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        rtn = robot.CustomCollisionDetectionEnd();
        Console.WriteLine($"CustomCollisionDetectionEnd rtn is {rtn}");
    }

设置正限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置正限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitPositive(double[] limit); 

设置负限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置负限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitNegative(double[] limit); 

获取关节软限位角度
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取关节软限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞	 
    * @param  [out] negative  负限位角度，单位deg
    * @param  [out] positive  正限位角度，单位deg
    * @return  错误码
    */
    int GetJointSoftLimitDeg(byte flag, ref double[] negative, ref double[] positive);

机器人限位设置代码示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] plimit = { 170.0f, 80.0f, 150.0f, 80.0f, 170.0f, 160.0f };
        robot.SetLimitPositive(plimit);
        double[] nlimit = { -170.0f, -260.0f, -150.0f, -260.0f, -170.0f, -160.0f };
        robot.SetLimitNegative(nlimit);

        double[] neg_deg = new double[6] {0,0,0,0,0,0 };
        double[] pos_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        robot.GetJointSoftLimitDeg(0, ref neg_deg,ref pos_deg);
        Console.WriteLine($"neg limit deg:{neg_deg[0]},{neg_deg[1]},{neg_deg[2]},{neg_deg[3]},{neg_deg[4]},{neg_deg[5]}");
        Console.WriteLine($"pos limit deg:{pos_deg[0]},{pos_deg[1]},{pos_deg[2]},{pos_deg[3]},{pos_deg[4]},{pos_deg[5]}");
    }

设置机器人碰撞检测方法
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人碰撞检测方法
    * @param  [in] method 碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
    * @param [in] thresholdMode 碰撞等级阈值方式；0-碰撞等级固定阈值方式；1-自定义碰撞检测阈值
    * @return  错误码
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode=0);


设置静态下碰撞检测开始关闭
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置静态下碰撞检测开始关闭
    * @param  [in] status 0-关闭；1-开启
    * @return  错误码
    */
    int SetStaticCollisionOnOff(int status);

设置机器人碰撞检测方法代码示例
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        int rtn = robot.SetCollisionDetectionMethod(0, 0);

        rtn = robot.SetStaticCollisionOnOff(1);
        Console.WriteLine($"SetStaticCollisionOnOff On rtn is {rtn}");
        Thread.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        Console.WriteLine($"SetStaticCollisionOnOff Off rtn is {rtn}");
    }

关节扭矩功率检测
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 关节扭矩功率检测
    * @param  [in] status 0-关闭；1-开启
    * @param  [in] power 设定最大功率(W)
    * @return  错误码
    */
    int SetPowerLimit(int status, double power);

关节扭矩功率检测代码示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }

设置安全速度参数
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置安全速度参数
    * @param [in] enable 0-关；1-手动模式启用；2-所有模式启用(不支持自动限速)
    * @param [in] maxTCPVel 限制最大TCP速度;[0-1000]mm/s
    * @param [in] strategy 超速后策略；0-停止报警；1-自动限速；2-停止报警并去使能
    * @return 错误码
    */
    public int SetVelReducePara(int enable, double maxTCPVel, int strategy)
    
设置安全速度参数的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int TestSetVelReducePara()
    {
        int rtn = 0;
        JointPos j1 = new JointPos(0, -90, 90, 0, 0, 0);
        JointPos j2 = new JointPos(90, -90, 90, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        robot.SetSpeed(80);

        // 测试参数错误
        rtn = robot.SetVelReducePara(2, 30, 1);
        Console.WriteLine($"SetVelReducePara param error rtn is {rtn}");

        // 禁用减速
        rtn = robot.SetVelReducePara(0, 30, 1);
        Console.WriteLine($"SetVelReducePara disable reduce vel rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // 启用减速（手动模式）
        rtn = robot.SetVelReducePara(1, 30, 1);
        Console.WriteLine($"SetVelReducePara reduce vel rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // 所有模式启用，策略为停止报警并去使能
        rtn = robot.SetVelReducePara(2, 30, 2);
        Console.WriteLine($"SetVelReducePara disable robot rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        Thread.Sleep(2000);
        robot.ResetAllError();
        robot.RobotEnable(1);
        Thread.Sleep(1000);

        // 所有模式启用，策略为停止报警（正常参数）
        rtn = robot.SetVelReducePara(2, 30, 0);
        Console.WriteLine($"SetVelReducePara report error rtn is {rtn}");
        robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        Thread.Sleep(1000);
        return 0;
    }