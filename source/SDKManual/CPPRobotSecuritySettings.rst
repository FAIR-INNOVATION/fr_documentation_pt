机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置碰撞等级
    * @param  [in]  mode  0-等级，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应范围[],百分比对应范围[0~1]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  错误码
    */
    errno_t  SetAnticollision(int mode, float level[6], int config);

设置碰撞后策略
++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  设置碰撞后策略
	 * @param  [in] strategy  0-报错暂停；1-继续运行;2-报错停止；3-重力矩模式；4-震荡相应模式；5-碰撞回弹模式 
	 * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
	 * @param  [in] safeDistance  安全停止距离[1-150]mm
	 * @param  [in] safetyMargin  j1-j6安全系数[1-10]
	 * @return  错误码
	 */
	errno_t SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]);

自定义碰撞检测阈值功能开始
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

	 /**
	 * @brief  自定义碰撞检测阈值功能开始，设置关节端和TCP端的碰撞检测阈值
	 * @param  [in] flag 1-仅关节检测开启；2-仅TCP检测开启；3-关节和TCP检测同时开启
	 * @param  [in] jointDetectionThreshould 关节碰撞检测阈值 j1-j6
	 * @param  [in] tcpDetectionThreshould TCP碰撞检测阈值，xyzabc
	 * @param  [in] block 0-非阻塞；1-阻塞
	 * @return  错误码
	 */
	errno_t CustomCollisionDetectionStart(int flag, double jointDetectionThreshould[6], double tcpDetectionThreshould[6], int block);

自定义碰撞检测阈值功能结束
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  自定义碰撞检测阈值功能关闭
	 * @return  错误码
	 */
	errno_t CustomCollisionDetectionEnd();

机器人碰撞等级设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestCollision(void)
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
         int mode = 0;
         int config = 1;
         float level1[6] = { 1.0,2.0,3.0,4.0,5.0,6.0 };
         float level2[6] = { 50.0,20.0,30.0,40.0,50.0,60.0 };
         rtn = robot.SetAnticollision(mode, level1, config);
         printf("SetAnticollision mode 0 rtn is %d\n", rtn);
         mode = 1;
         rtn = robot.SetAnticollision(mode, level2, config);
         printf("SetAnticollision mode 1 rtn is %d\n", rtn);
         JointPos p1Joint(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos p2Joint(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0.0, 0.0, 0.0, 0.0);
         DescPose offdese(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
         robot.MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, 2, &exaxisPos, 0, 0, &offdese);
         robot.ResetAllError();
         int safety[6] = { 5,5,5,5,5,5 };
         rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
         printf("SetCollisionStrategy rtn is %d\n", rtn);
         double jointDetectionThreshould[6] = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
         double tcpDetectionThreshould[6] = { 60,60,60,60,60,60 };
         rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
         cout << "CustomCollisionDetectionStart rtn is " << rtn << endl;
         robot.MoveL(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
         robot.MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
         rtn = robot.CustomCollisionDetectionEnd();
         cout << "CustomCollisionDetectionEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

设置正限位
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置正限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    errno_t  SetLimitPositive(float limit[6]);

设置负限位
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置负限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    errno_t  SetLimitNegative(float limit[6]);   

获取关节软限位角度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取关节软限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞    
    * @param  [out] negative  负限位角度，单位deg
    * @param  [out] positive  正限位角度，单位deg
    * @return  错误码
    */
    errno_t  GetJointSoftLimitDeg(uint8_t flag, float negative[6], float positive[6]);
    
机器人限位设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLimit(void)
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
      float plimit[6] = { 170.0,80.0,150.0,80.0,170.0,160.0 };
      robot.SetLimitPositive(plimit);
      float nlimit[6] = { -170.0,-260.0,-150.0,-260.0,-170.0,-160.0 };
      robot.SetLimitNegative(nlimit);
      float neg_deg[6] = { 0.0 }, pos_deg[6] = { 0.0 };
      robot.GetJointSoftLimitDeg(0, neg_deg, pos_deg);
      printf("neg limit deg:%f,%f,%f,%f,%f,%f\n", neg_deg[0], neg_deg[1], neg_deg[2], neg_deg[3], neg_deg[4], neg_deg[5]);
      printf("pos limit deg:%f,%f,%f,%f,%f,%f\n", pos_deg[0], pos_deg[1], pos_deg[2], pos_deg[3], pos_deg[4], pos_deg[5]);
      robot.CloseRPC();
      return 0;
    }

设置机器人碰撞检测方法
++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置机器人碰撞检测方法
    * @param [in] method 碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
    * @param [in] thresholdMode 碰撞等级阈值方式；0-碰撞等级固定阈值方式；1-自定义碰撞检测阈值
    * @return  错误码
    */
    errno_t SetCollisionDetectionMethod(int method, int thresholdMode = 0);

设置静态下碰撞检测开始关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置静态下碰撞检测开始关闭
     * @param [in] status 0-关闭；1-开启
     * @return 错误码
     */
    errno_t SetStaticCollisionOnOff(int status);

设置机器人碰撞检测方法代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestCollisionMethod(void)
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
      rtn = robot.SetCollisionDetectionMethod(0, 0);
      printf("SetCollisionDetectionMethod rtn is %d\n", rtn);
      rtn = robot.SetStaticCollisionOnOff(1);
      printf("SetStaticCollisionOnOff On rtn is %d\n", rtn);
      rtn = robot.Sleep(5000);
      rtn = robot.SetStaticCollisionOnOff(0);
      printf("SetStaticCollisionOnOff Off rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

关节扭矩功率检测
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 关节扭矩功率检测
     * @param [in] status 0-关闭；1-开启
     * @param [in] power 设定最大功率(W);
     * @return 错误码
     */
    errno_t SetPowerLimit(int status, double power);

关节扭矩功率检测代码示例
++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestPowerLimit(void)
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
       robot.DragTeachSwitch(1);
       robot.SetPowerLimit(1, 200);
       float torques[] = { 0, 0, 0, 0, 0, 0 };
       robot.GetJointTorques(1, torques);
       int count = 100;
       robot.ServoJTStart(); 
       int error = 0;
       while (count > 0)
       {
          error = robot.ServoJT(torques, 0.001);
          count = count - 1;
          robot.Sleep(1);
       }
       error = robot.ServoJTEnd();
       robot.DragTeachSwitch(0);
       robot.CloseRPC();
       return 0;
    }
    
设置安全速度参数
++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置安全速度参数
    * @param [in] enable 0-关；1-手动模式启用；2-所有模式启用
    * @param [in] maxTCPVel 限制最大TCP速度;[0-1000]mm/s
    * @param [in] strategy 超速后策略；0-停止报警；1-自动限速；2-停止报警并去使能
    * @return 错误码
    */
    errno_t SetVelReducePara(int enable, double maxTCPVel, int strategy);
        
设置安全速度参数的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSetVelReducePara()
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
        JointPos j1(0, -90, 90, 0, 0, 0);
        JointPos j2(90, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        robot.SetSpeed(80);
        rtn = robot.SetVelReducePara(2, 30, 1);
        printf("SetVelReducePara param error rtn is %d\n", rtn);
        rtn = robot.SetVelReducePara(0, 30, 1);
        printf("SetVelReducePara disable reduce vel rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        rtn = robot.SetVelReducePara(1, 30, 1);
        printf("SetVelReducePara reduce vel rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        rtn = robot.SetVelReducePara(2, 30, 2);
        printf("SetVelReducePara disable robot rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(2000);
        robot.ResetAllError();
        robot.RobotEnable(1);
        robot.Sleep(1000);
        rtn = robot.SetVelReducePara(2, 30, 0);
        printf("SetVelReducePara report error rtn is %d\n", rtn);
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }