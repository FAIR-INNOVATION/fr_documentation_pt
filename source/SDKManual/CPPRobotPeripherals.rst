机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  SetGripperConfig(int company, int device, int softvesion, int bus);

获取夹爪配置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夹爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    errno_t  ActGripper(int index, uint8_t act);

控制夹爪
++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
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
	 * @return  错误码
	 */
	errno_t MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block, int type, double rotNum, int rotVel, int rotTorque);



获取夹爪运动状态
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪运动状态
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] staus  0-运动未完成，1-运动完成
     * @return  错误码
     */
    errno_t  GetGripperMotionDone(uint16_t *fault, uint8_t *status);

获取夹爪激活状态
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪激活状态
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
     * @return  错误码
     */
    errno_t  GetGripperActivateStatus(uint16_t *fault, uint16_t *status);

获取夹爪位置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪位置
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] position  位置百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurPosition(uint16_t *fault, uint8_t *position);

获取夹爪速度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪速度
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] speed  速度百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurSpeed(uint16_t *fault, int8_t *speed);

获取夹爪电流
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪电流
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] current  电流百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurCurrent(uint16_t *fault, int8_t *current);

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪电压
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] voltage  电压,单位0.1V
     * @return  错误码
     */
    errno_t  GetGripperVoltage(uint16_t *fault, int *voltage);

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪温度
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] temp  温度，单位℃
     * @return  错误码
     */
    errno_t  GetGripperTemp(uint16_t *fault, int *temp);

计算预抓取点-视觉
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算预抓取点-视觉
     * @param  [in] desc_pos  抓取点笛卡尔位姿
     * @param  [in] zlength  z轴偏移量
     * @param  [in] zangle   绕z轴旋转偏移量
     * @return  错误码 
     */
    errno_t  ComputePrePick(DescPose *desc_pos, double zlength, double zangle, DescPose *pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算撤退点-视觉
     * @param  [in] desc_pos  抓取点笛卡尔位姿
     * @param  [in] zlength  z轴偏移量
     * @param  [in] zangle   绕z轴旋转偏移量
     * @return  错误码 
     */
    errno_t  ComputePostPick(DescPose *desc_pos, double zlength, double zangle, DescPose *post_pos);

机器人夹爪操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGripper(void)
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
      int company = 4;
      int device = 0;
      int softversion = 0;
      int bus = 2;
      int index = 2;
      int act = 0;
      int max_time = 30000;
      uint8_t block = 0;
      uint8_t status;
      uint16_t fault;
      uint16_t active_status = 0;
      uint8_t current_pos = 0;
      int8_t current = 0;
      int voltage = 0;
      int temp = 0;
      int8_t speed = 0;
      robot.SetGripperConfig(company, device, softversion, bus);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.GetGripperConfig(&company, &device, &softversion, &bus);
      printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      act = 1;
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);
      robot.GetGripperMotionDone(&fault, &status);
      printf("motion status:%u,%u\n", fault, status);
      robot.GetGripperActivateStatus(&fault, &active_status);
      printf("gripper active fault is: %u, status is: %u\n", fault, active_status);
      robot.GetGripperCurPosition(&fault, &current_pos);
      printf("fault is:%u, current position is: %u\n", fault, current_pos);
      robot.GetGripperCurCurrent(&fault, &current);
      printf("fault is:%u, current current is: %d\n", fault, current);
      robot.GetGripperVoltage(&fault, &voltage);
      printf("fault is:%u, current voltage is: %d \n", fault, voltage);
      robot.GetGripperTemp(&fault, &temp);
      printf("fault is:%u, current temperature is: %d\n", fault, temp);
      robot.GetGripperCurSpeed(&fault, &speed);
      printf("fault is:%u, current speed is: %d\n", fault, speed);
      int retval = 0;
      DescPose prepick_pose = {};
      DescPose postpick_pose = {};
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.ComputePrePick(&p1Desc, 10, 0, &prepick_pose);
      printf("ComputePrePick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z, prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);
      retval = robot.ComputePostPick(&p2Desc, -10, 0, &postpick_pose);
      printf("ComputePostPick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z, postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);
      robot.CloseRPC();
      return 0;
    }

获取旋转夹爪的旋转圈数
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 3.7.6版本加入

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转圈数
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] num  旋转圈数
	 * @return  错误码
	 */
	errno_t GetGripperRotNum(uint16_t* fault, double* num);

获取旋转夹爪的旋转速度
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转速度
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] speed  旋转速度百分比
	 * @return  错误码
	 */
	errno_t GetGripperRotSpeed(uint16_t* fault, int* speed);

获取旋转夹爪的旋转力矩
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转力矩
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] torque  旋转力矩百分比
	 * @return  错误码
	 */
	errno_t GetGripperRotTorque(uint16_t* fault, int* torque);

获取旋转夹爪状态代码示例
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestRotGripperState(void)
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
      uint16_t fault = 0;
      double rotNum = 0.0;
      int rotSpeed = 0;
      int rotTorque = 0;
      robot.GetGripperRotNum(&fault, &rotNum);
      robot.GetGripperRotSpeed(&fault, &rotSpeed);
      robot.GetGripperRotTorque(&fault, &rotTorque);
      printf("gripper rot num : %lf, gripper rotSpeed : %d, gripper rotTorque : %d\n", rotNum, rotSpeed, rotTorque);
      robot.CloseRPC();
      return 0;
    }


传动带启动、停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 传动带启动、停止
    * @param [in] status 状态，1-启动，0-停止 
    * @return 错误码
    */
    errno_t ConveyorStartEnd(uint8_t status);

记录IO检测点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 记录IO检测点
    * @return 错误码
    */
    errno_t ConveyorPointIORecord();

记录A点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 记录A点
    * @return 错误码
    */
    errno_t ConveyorPointARecord();

记录参考点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 记录参考点
    * @return 错误码
    */
    errno_t ConveyorRefPointRecord();

记录B点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 记录B点
    * @return 错误码
    */
    errno_t ConveyorPointBRecord();

传送带工件IO检测
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 传送带工件IO检测
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码
    */
    errno_t ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取物体当前位置
    * @param [in] mode 
    * @return 错误码
    */
    errno_t ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 传动带跟踪开始
    * @param [in] status 状态，1-启动，0-停止 
    * @return 错误码
    */
    errno_t ConveyorTrackStart(uint8_t status);

传动带跟踪停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 传动带跟踪停止
    * @return 错误码
    */
    errno_t ConveyorTrackEnd();

传动带参数配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 传动带参数配置
    * @param [in] para[0] 编码器通道 1~2
    * @param [in] para[1] 编码器转一圈的脉冲数
    * @param [in] para[2] 编码器转一圈传送带行走距离
    * @param [in] para[3] 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] para[4] 是否配视觉 0 不配 1 配
    * @param [in] para[5] 速度比 针对传送带跟踪抓取选项（1-100） 其他选项默认为1 
    * @param [in] followType 跟踪运动类型，0-跟踪运动；1-追检运动
    * @param [in] startDis 追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    * @param [in] endDis 追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100
    * @return 错误码
    */
    errno_t ConveyorSetParam(float para[6], int followType = 0, int startDis = 0, int endDis = 100);

传动带抓取点补偿
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief 传动带抓取点补偿
	 * @param [in] cmp 补偿位置 double[3]{x, y, z}
	 * @return 错误码
	 */
    errno_t ConveyorCatchPointComp(double cmp[3]);

传送带直线运动
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 传送带直线运动
    * @param [in] status 状态，1-启动，0-停止 
    * @return 错误码
    */
    errno_t TrackMoveL(char name[32], int tool, int wobj, float vel, float acc, float ovl, float blendR, uint8_t flag, uint8_t type);

传送带通讯输入检测
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 传送带通讯输入检测
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    errno_t ConveyorComDetect(int timeout);

传送带通讯输入检测触发
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 传送带通讯输入检测触发
    * @return 错误码
    */
    errno_t ConveyorComDetectTrigger();

机器人传送带操作示例程序
++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestConveyor(void)
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
      int retval = 0;
      retval = robot.ConveyorStartEnd(1);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = robot.ConveyorPointIORecord();
      printf("ConveyorPointIORecord retval is: %d\n", retval);
      retval = robot.ConveyorPointARecord();
      printf("ConveyorPointARecord retval is: %d\n", retval);
      retval = robot.ConveyorRefPointRecord();
      printf("ConveyorRefPointRecord retval is: %d\n", retval);
      retval = robot.ConveyorPointBRecord();
      printf("ConveyorPointBRecord retval is: %d\n", retval);
      retval = robot.ConveyorStartEnd(0);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = 0;
      float param[6] = { 1,10000,200,0,0,20 };
      retval = robot.ConveyorSetParam(param);
      printf("ConveyorSetParam retval is: %d\n", retval);
      double cmp[3] = { 0.0, 0.0, 0.0 };
      retval = robot.ConveyorCatchPointComp(cmp);
      printf("ConveyorCatchPointComp retval is: %d\n", retval);
      int index = 1;
      int max_time = 30000;
      uint8_t block = 0;
      retval = 0;
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.MoveCart(&p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      printf("MoveCart retval is: %d\n", retval);
      retval = robot.WaitMs(1);
      printf("WaitMs retval is: %d\n", retval);
      retval = robot.ConveyorIODetect(10000);
      printf("ConveyorIODetect retval is: %d\n", retval);
      retval = robot.ConveyorGetTrackData(1);
      printf("ConveyorGetTrackData retval is: %d\n", retval);
      retval = robot.ConveyorTrackStart(1);
      printf("ConveyorTrackStart retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.ConveyorTrackEnd();
      printf("ConveyorTrackEnd retval is: %d\n", retval);
      robot.MoveCart(&p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      rtn = robot->ConveyorComDetect(1000 * 10);
      printf("ConveyorComDetect rtn is: %d\n", rtn);
      robot.Sleep(2000);
      rtn = robot->ConveyorComDetectTrigger();
      printf("ConveyorComDetectTrigger rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }


末端传感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端传感器配置
    * @param [in] idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [in] idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param [in] idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param [in] idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return 错误码
    */
    errno_t AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

获取末端传感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取末端传感器配置
     * @param [out] idCompany 厂商，18-JUNKONG；25-HUIDE
     * @param [out] idDevice 类型，0-JUNKONG/RYR6T.V1.0
     * @return 错误码
     */
    errno_t AxleSensorConfigGet(int& idCompany, int& idDevice);

末端传感器激活
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 末端传感器激活
     * @param [in] actFlag 0-复位；1-激活
     * @return 错误码
     */
    errno_t AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 末端传感器寄存器写入
     * @param [in] devAddr 设备地址编号 0-255
     * @param [in] regHAddr 寄存器地址高8位
     * @param [in] regLAddr 寄存器地址低8位
     * @param [in] regNum 寄存器个数 0-255
     * @param [in] data1 写入寄存器数值1
     * @param [in] data2 写入寄存器数值2
     * @param [in] isNoBlock 0-阻塞；1-非阻塞
     * @return 错误码
     */
    errno_t AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端传感器代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestAxleSensor(void)
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
      robot.AxleSensorConfig(18, 0, 0, 1);
      int company = -1;
      int type = -1;
      robot.AxleSensorConfigGet(company, type);
      printf("company is %d, type is %d\n", company, type);
      rtn = robot.AxleSensorActivate(1);
      printf("AxleSensorActivate rtn is %d\n", rtn);
      robot.Sleep(1000);
      rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
      printf("AxleSensorRegWrite rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }
        
获取机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人外设协议
    * @param [out] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t GetExDevProtocol(int *protocol);

设置机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t SetExDevProtocol(int protocol);

设置机器人外设协议示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    int TestExDevProtocol(void)
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
      int protocol = 4096;
      rtn = robot.SetExDevProtocol(protocol);
      std::cout << "SetExDevProtocol rtn " << rtn << std::endl;
      rtn = robot.GetExDevProtocol(&protocol);
      std::cout << "GetExDevProtocol rtn " << rtn << " protocol is: " << protocol << std::endl;
      robot.CloseRPC();
      return 0;
    }

获取末端通讯参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取末端通讯参数
    * @param param 末端通讯参数
    * @return  错误码
    */
    errno_t GetAxleCommunicationParam(AxleComParam* param);

设置末端通讯参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端通讯参数
    * @param param  末端通讯参数
    * @return  错误码
    */
    errno_t SetAxleCommunicationParam(AxleComParam param);

设置末端文件传输类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端文件传输类型
    * @param type 1-MCU升级文件；2-LUA文件
    * @return  错误码
    */
    errno_t SetAxleFileType(int type);

设置启用末端LUA执行
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置启用末端LUA执行
    * @param enable 0-不启用；1-启用
    * @return  错误码
    */
    errno_t SetAxleLuaEnable(int enable);

末端LUA文件异常错误恢复
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 末端LUA文件异常错误恢复
    * @param status 0-不恢复；1-恢复
    * @return  错误码
    */
    errno_t SetRecoverAxleLuaErr(int status);

末端LUA文件异常错误恢复
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取末端LUA执行使能状态
    * @param status status[0]: 0-未使能；1-已使能
    * @return  错误码
    */
    errno_t GetAxleLuaEnableStatus(int status[]);

设置末端LUA末端设备启用类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端LUA末端设备启用类型
    * @param forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    errno_t SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable);

设置末端LUA末端设备启用类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:
        
    /**
    * @brief 获取末端LUA末端设备启用类型
    * @param enable enable[0]:forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param enable enable[1]:gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param enable enable[2]:IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    errno_t GetAxleLuaEnableDeviceType(int* forceSensorEnable, int* gripperEnable, int* IOEnable);

获取当前配置的末端设备
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取当前配置的末端设备
    * @param forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
    * @param gripperEnable 夹爪启用设备编号，0-不启用；1-启用
    * @param IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
    * @return  错误码
    */
    errno_t GetAxleLuaEnableDevice(int forceSensorEnable[], int gripperEnable[], int IODeviceEnable[]);

设置启用夹爪动作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置启用夹爪动作控制功能
    * @param id 夹爪设备编号
    * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    errno_t SetAxleLuaGripperFunc(int id, int func[]);

获取启用夹爪动作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取启用夹爪动作控制功能
    * @param id 夹爪设备编号
    * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    errno_t GetAxleLuaGripperFunc(int id, int func[]);

机器人Ethercat从站文件写入
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人Ethercat从站文件写入
    * @param type 从站文件类型，1-升级从站文件；2-升级从站配置文件
    * @param slaveID 从站号
    * @param fileName 上传文件名
    * @return  错误码
    */
    errno_t SlaveFileWrite(int type, int slaveID, std::string fileName);

上传末端Lua开放协议文件
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传末端Lua开放协议文件
    * @param filePath 本地lua文件路径名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 错误码
    */
    errno_t AxleLuaUpload(std::string filePath);

机器人Ethercat从站进入boot模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人Ethercat从站进入boot模式
    * @return  错误码
    */
    errno_t SetSysServoBootMode();

机器人末端LUA文件操作代码示例
++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAxleLua(void)
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
      robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");
      AxleComParam param(7, 8, 1, 0, 5, 3, 1);
      robot.SetAxleCommunicationParam(param);
      AxleComParam getParam;
      robot.GetAxleCommunicationParam(&getParam);
      printf("GetAxleCommunicationParam param is %d %d %d %d %d %d %d\n", getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify, getParam.timeout, getParam.timeoutTimes, getParam.period);
      robot.SetAxleLuaEnable(1);
      int luaEnableStatus = 0;
      robot.GetAxleLuaEnableStatus(&luaEnableStatus);
      robot.SetAxleLuaEnableDeviceType(0, 1, 0);
      int forceEnable = 0;
      int gripperEnable = 0;
      int ioEnable = 0;
      robot.GetAxleLuaEnableDeviceType(&forceEnable, &gripperEnable, &ioEnable);
      printf("GetAxleLuaEnableDeviceType param is %d %d %d\n", forceEnable, gripperEnable, ioEnable);
      int func[16] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
      robot.SetAxleLuaGripperFunc(1, func);
      int getFunc[16] = { 0 };
      robot.GetAxleLuaGripperFunc(1, getFunc);
      int getforceEnable[16] = { 0 };
      int getgripperEnable[16] = { 0 };
      int getioEnable[16] = { 0 };
      robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
      printf("\ngetforceEnable status : ");
      for (int i = 0; i < 16; i++)
      {
        printf("%d,", getforceEnable[i]);
      }
      printf("\ngetgripperEnable status : ");
      for (int i = 0; i < 16; i++)
      {
        printf("%d,", getgripperEnable[i]);
      }
      printf("\ngetioEnable status : ");
      for (int i = 0; i < 16; i++)
      {
        printf("%d,", getioEnable[i]);
      }
      printf("\n");
      robot.ActGripper(1, 0);
      robot.Sleep(2000);
      robot.ActGripper(1, 1);
      robot.Sleep(2000);
      robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
      int pos = 0;
      while (true)
      {
        robot.GetRobotRealTimeState(&pkg);
        printf("gripper pos is %u\n", pkg.gripper_position);
        robot.Sleep(100);
      }
      robot.CloseRPC();
      return 0;
    }

获取SmartTool按钮状态
++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取SmartTool按钮状态
    * @param [out] state SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；
    bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)
    * @return 错误码
    */
    errno_t GetSmarttoolBtnState(int& state);
    
SmartTool按钮代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int main(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;

      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      robot.SetReConnectParam(true, 30000, 500);

      while (true)
      {
        int btn = 0;
        robot.GetSmarttoolBtnState(btn);
        cout << "smarttool " << std::bitset<sizeof(btn) * 8>(btn) << endl;

        Sleep(100);
      }
    }

控制阵列式吸盘
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制阵列式吸盘
    * @param [in] slaveID 从站号
    * @param [in] len 长度
    * @param [in] ctrlValue 控制值
    * @return 错误码
    */
    errno_t FRRobot::SetSuckerCtrl(uint8_t slaveID, uint8_t len, uint8_t ctrlValue[20]);

获取阵列式吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取阵列式吸盘状态
    * @param [in] slaveID 从站号
    * @param [out] state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param [out] pressValue 当前真空度 单位kpa 
    * @param [out] error 吸盘当前的错误码
    * @return 错误码
    */
	errno_t FRRobot::GetSuckerState(uint8_t slaveID, uint8_t* state, int* pressValue, int* error);

等待吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待吸盘状态
    * @param [in] slaveID 从站号
    * @param [in] state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param [in] ms 等待最大时间
    * @return 错误码
    */
    errno_t FRRobot::WaitSuckerState(uint8_t slaveID, uint8_t state, int ms);

阵列式吸盘控制指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testSucker()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //上传并加载开放协议文件
        robot.OpenLuaUpload("E://项目/外设SDK/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(1, "CtrlDev_sucker.lua");
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);

        //控制吸盘广播模式下，按照最大能力吸附
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);

        //循环监控1号吸盘和12号吸盘的状态
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, &state, &pressVlaue, &error);
            printf("sucker1 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.GetSuckerState(12, &state, &pressVlaue, &error);
            printf("sucker12 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.Sleep(100);
        }

        //等待1号吸盘是否为吸附到物体的状态，等待时间100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        printf("WaitSuckerState result is  %d\n", ret);

        //单播模式关闭1号和12号吸盘
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);

        robot.CloseRPC();
    }

上传外设开放协议LUA文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

	/**
	 * @brief 上传Lua文件
	 * @param [in] filePath 本地lua文件路径名
	 * @return 错误码
	 */
    errno_t OpenLuaUpload(std::string filePath);

获取从站板卡参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  获取从站板卡参数
    * @param  [out] type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  [out] version  协议版本
    * @param  [out] connState  0-未连接 1-已连接
    * @return  错误码
    */
    errno_t GetFieldBusConfig(uint8_t* type, uint8_t* version, uint8_t* connState);

写入从站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  写入从站DO
    * @param  [in] DOIndex  DO编号
    * @param  [in] wirteNum  写入的数量
    * @param  [in] status[8] 写入的数值，最多写8个
    * @return  错误码
    */
    errno_t FieldBusSlaveWriteDO(uint8_t DOIndex, uint8_t wirteNum, uint8_t status[8]);

写入从站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  写入从站AO
    * @param  [in] AOIndex  AO编号
    * @param  [in] wirteNum  写入的数量
    * @param  [in] status[8] 写入的数值，最多写8个
    * @return  错误码
    */
    errno_t FieldBusSlaveWriteAO(uint8_t AOIndex, uint8_t wirteNum, int status[8]);

读取从站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  读取从站DI
    * @param  [in] DOIndex  DI编号
    * @param  [in] readeNum  读取的数量
    * @param  [out] status[8] 读取到的数值，最多读8个
    * @return  错误码
    */
    errno_t FieldBusSlaveReadDI(uint8_t DOIndex, uint8_t readNum, uint8_t status[8]);

读取从站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  读取从站AI
    * @param  [in] AOIndex  AI编号
    * @param  [in] readeNum  读取的数量
    * @param  [out] status[8] 读取到的数值，最多读8个
    * @return  错误码
    */
    errno_t FieldBusSlaveReadAI(uint8_t AIIndex, uint8_t readNum, int status[8]);

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param [in] DIIndex DI编号
    * @param [in] status 0-低电平；1-高电平
    * @param [in] waitMs 最大等待时间(ms)
    * @return 错误码
    */
    errno_t FRRobot::FieldBusSlaveWaitDI(uint8_t DIIndex, bool status, int waitMs);

等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param [in] AIIndex AI编号
    * @param [in] waitType 0-大于；1-小于
    * @param [in] value AI值
    * @param [in] waitMs 最大等待时间(ms)
    * @return 错误码
    */
    errno_t FRRobot::FieldBusSlaveWaitAI(uint8_t AIIndex, uint8_t waitType, double value, int waitMs);

从站模式相关接口指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testFieldBusBoard()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t type = 0, version = 0, connState = 0;
        uint8_t ctrl[8];
        int ctrlAO[8];
        static uint8_t DI[8];
        static int AI[8];

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //上传并加载开放协议文件
        robot.OpenLuaUpload("E://项目/外设SDK/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);

        //获取从站板卡的协议类型、软件版本、与PLC的连接状态
        robot.GetFieldBusConfig(&type, &version, &connState);
        printf("type is %d, version is %d,connState is %d\n", type, version, connState);

        //写入DO0 = 1、DO1 = 0、DO2 = 1
        ctrl[0] = 0;
        ctrl[1] = 1;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);

        //写入AO2 = 0x1000
        ctrlAO[0] = 0x1005;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        //循环监控DI0~DI3 AI0~AI2
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            printf("DI0 is %d, DI1 is %d,DI2 is %d,DI3 is %d\n", DI[0], DI[1], DI[2], DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            printf("AI0 is %d, AI1 is %d,AI2 is %d\n", AI[0], AI[1], AI[2]);
            robot.Sleep(10);
        }

        //等待DI0是否为1，等待时间100ms，并打印结果
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        printf("FieldBusSlaveWaitDI result is  %d\n", ret);

        //等待AI0是否大于400，等待时间100ms，并打印结果
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        printf("FieldBusSlaveWaitAI result is  %d\n", ret);

        robot.CloseRPC();
    }

激光外设打开关闭
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光外设打开关闭函数
	 * @param [in] OnOff 0-关闭 1-打开
	 * @param [in] weldId 焊缝ID 默认为0
	 * @return 错误码
	 */
	errno_t LaserTrackingLaserOnOff(int OnOff,int weldId);
        
激光跟踪开始结束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光跟踪开始结束函数
	 * @param [in] OnOff 0-结束 1-开始
	 * @param [in] coordId 激光外设工具坐标系编号
	 * @return 错误码
	 */
 	errno_t LaserTrackingTrackOnOff(int OnOff, int coordId); 
            
激光寻位开始-固定方向
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 激光寻位-固定方向
    * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    * @param [in] vel 速度 单位%
    * @param [in] distance 最大寻位距离 单位mm
    * @param [in] distance 寻位超时时间 单位ms
    * @param [in] posSensorNum 激光标定的工具坐标编号
    * @return 错误码
    */
    errno_t LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum);
                
激光寻位开始-任意点方向
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光寻位-任意方向
	 * @param [in] directionPoint 寻位输入的点的xyz左边
	 * @param [in] vel 速度 单位%
	 * @param [in] distance 最大寻位距离 单位mm
	 * @param [in] distance 寻位超时时间 单位ms
	 * @param [in] posSensorNum 激光标定的工具坐标编号
	 * @return 错误码
	 */
    errno_t LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum);
                    
激光寻位结束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光寻位结束
	 * @return 错误码
	 */
    errno_t LaserTrackingSearchStop();

激光网络参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光网络参数配置
	 * @param [in] ip 激光外设的ip地址
	 * @param [in] port 激光外设的端口号
	 * @return 错误码
	 */
    errno_t LaserTrackingSensorConfig(std::string ip, int port);
    
激光外设采样周期配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 激光外设采样周期配置
    * @param [in] period 激光外设采样周期 单位ms
    * @return 错误码
    */
    errno_t LaserTrackingSensorSamplePeriod(int period);
        
激光外设驱动加载
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光外设驱动加载
	 * @param [in] type 激光外设驱动的协议类型 101-睿牛 102-创想 103-全视 104-同舟 105-奥太
	 * @return 错误码
	 */
    errno_t LoadPosSensorDriver(int type);
            
激光外设驱动卸载
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光外设驱动卸载
	 * @return 错误码
	 */
    errno_t UnLoadPosSensorDriver();
                
激光焊缝轨迹记录
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 激光焊缝轨迹记录
    * @param [in] status 0-停止记录 1-实时跟踪  2-开始记录
    * @param [in] delayTime 延时时间 单位ms
    * @return 错误码
    */
    errno_t LaserSensorRecord1(int status, int delayTime); 
                    
激光焊缝轨迹复现
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光焊缝轨迹复现
	 * @param [in] delayTime 延时时间 单位ms
	 * @param [in] speed 速度 单位%
	 * @return 错误码
	 */
    errno_t LaserSensorReplay(int delayTime, double speed);
                        
激光跟踪复现
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 激光跟踪复现
	 * @return 错误码
	 */
    errno_t MoveLTR();
                            
激光焊缝轨迹记录及复现
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 激光焊缝轨迹记录及复现
    * @param [in] delayMode 模式 0-延时时间 1-延时距离
    * @param [in] delayTime 延时时间 单位ms
    * @param [in] delayDisExAxisNum 扩展轴编号
    * @param [in] delayDis 延时距离 单位mm
    * @param [in] sensitivePara 补偿灵敏系数
    * @param [in] trackMode 定点跟踪类型。0-扩展轴异步运动；1-机器人
    * @param [in] triggerMode 定点跟踪触发方式。0-跟踪时长；1-IO
    * @param [in] runTime 机器人定点跟踪时长(s)
    * @param [in] speed 速度 单位%
    * @return 错误码
    */
    errno_t LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum, double delayDis, double sensitivePara, int trackMode, int triggerMode, double runTime, double speed);
                                
运动到焊缝记录的起点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 运动到焊缝记录的起点
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl 速度 单位%
    * @return 错误码
    */
    errno_t MoveToLaserRecordStart(int moveType, double ovl);
                                    
运动到焊缝记录的终点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 运动到焊缝记录的终点
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl 速度 单位%
    * @return 错误码
    */
    errno_t MoveToLaserRecordEnd(int moveType, double ovl);
                                        
运动到激光传感器寻位点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
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
    errno_t MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset);
                                            
获取激光传感器寻位点坐标
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
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
    errno_t GetLaserSeamPos(int trackOffectType, DescPose offset, JointPos& jPos, DescPose& descPos, int& tool, int& user, ExaxisPos& exaxis); 
                                                
激光外设传感器参数配置及调试代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserConfig()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //设置IP地址和端口号
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        //设置采样周期
        robot.LaserTrackingSensorSamplePeriod(20);
        //加载驱动
        robot.LoadPosSensorDriver(101);
        //关闭激光外设
        robot.LaserTrackingLaserOnOff(0,0);
        robot.Sleep(3000);
        //打开激光外设
        robot.LaserTrackingLaserOnOff(1, 0);
        robot.CloseRPC();
    }
                                                    
激光轨迹扫描及轨迹复现的代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserRecordAndReplay()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //上传并加载开放协议文件
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while(cnt<31)
        { 
            //运动到扫描的起点
            JointPos startjointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //开始轨迹记录
            robot.LaserSensorRecord1(2, 10);
            //运动到需要记录的终点
            JointPos endjointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(&endjointPos, &enddescPose, 1, 0, 30, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //停止记录
            robot.LaserSensorRecord1(0, 10);
            //运动到记录的焊缝起点
            robot.MoveToLaserRecordStart(1, 30);
            //开始轨迹复现
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            //停止轨迹复现
            robot.LaserSensorRecord1(0, 10);
            printf("激光扫描+轨迹复现稳定性测试第%d次\n", cnt);
            cnt++;
        }
        robot.CloseRPC();
    }
                                                        
激光寻位及实时跟踪的代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrack()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //上传并加载开放协议文件
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while (cnt < 2)
        {
            //运动到需要寻位的起始点
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            DescTran directionPoint;
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);

            //沿着-y方向开始寻位
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            //如果寻位成功
            if (ret == 0)
            {
                //运动到寻位点
                robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);
                //开始沿着寻位点进行激光跟踪
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.MoveL(&endjointPos, &enddescPose, 1, 0, 20, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
                //停止跟踪
                robot.LaserTrackingTrackOnOff(0, 2);

            }
            cnt++;
        }
        robot.CloseRPC();
    }
                                                            
扩展轴与机器人同步进行激光跟踪的代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrackandExitAxis()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        ExaxisPos startexaxisPos = { 0,0,0,0 };
        ExaxisPos seamexaxisPos = { -10,0,0,0 };
        ExaxisPos endexaxisPos = { -30, 0, 0, 0 };
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        JointPos seamjointPos(0, 0, 0, 0, 0, 0);
        DescPose seamdescPose(0, 0, 0, 0, 0, 0);
        
        int cnt = 1;
        while (cnt < 31)
        {
            //运动到需要寻位的起始点
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);

            //沿着-y方向开始寻位
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            int tool = 0;
            int user = 0;
            robot.GetLaserSeamPos(0, offdese, seamjointPos, seamdescPose, tool, user, startexaxisPos);
            printf("%f, %f, %f,%f, %f, %f,%f, %f, %f,%f, %f, %f\n", seamjointPos.jPos[0], seamjointPos.jPos[1], seamjointPos.jPos[2], seamjointPos.jPos[3], seamjointPos.jPos[4], seamjointPos.jPos[5], seamdescPose.tran.x, seamdescPose.tran.y, seamdescPose.tran.z, seamdescPose.rpy.rx, seamdescPose.rpy.ry, seamdescPose.rpy.rz);

            //如果寻位成功
            if (ret == 0)
            {
                //机器人和扩展轴同步运动到寻位点
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);

                //开始沿着寻位点进行激光跟踪并与扩展轴同步运动
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);;
                //停止跟踪
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            cnt++;
            printf("扩展轴与机器人同步进行激光跟踪  第%d次\n", cnt);
        }
        robot.CloseRPC();
    } 
                                                            
末端透传功能打开关闭
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端透传功能打开关闭
    * @param [in] 使能，0-关闭，1-开启
    * @return 错误码
    */
    errno_t SetAxleGenComEnable(int mode);
                                                            
末端透传功能非周期数据收发
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:
    
    /**
    * @brief 末端透传功能非周期数据收发
    * @param [in] len_snd 发送的长度
    * @param [in] sndBuff 发送数据
    * @param [in] len_rcv 选择接受的长度
    * @param [out] rcvBuff 应答的数据
    * @return 错误码
    */
    errno_t SndRcvAxleGenComCmdData(int lenSnd, int sndBuff[130], int lenRcv, int rcvData[130]);
                                                                
基于末端透传功能倍益康艾灸头非周期数据通信代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int testAxleGenCom()
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
      int led_on[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
      int led_off[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int version[5] = { 0xAB, 0xBA, 0x11, 0x00, 0x76 };
      int state[6] = { 0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B };
      int cycleState[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int rcvdata[16] = {0};
      int ret = 0;
      int cnt = 1;
      JointPos p1Joint(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
      DescPose p1Desc(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);
      JointPos p2Joint(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
      DescPose p2Desc(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      //开启末端透传功能
      robot.SetAxleGenComEnable(1);
      robot.SetAxleLuaEnable(1);
      while (cnt <= 10000)
      {
        //读取版本号
        ret = robot.SndRcvAxleGenComCmdData(5, version, 10, rcvdata);
        printf(" hard version : %d,hard code:%d, soft version:%d %d, soft code:%d \n", rcvdata[4], rcvdata[5], rcvdata[6] ,rcvdata[7], rcvdata[8]);
        if (ret != 0)
        {
          break;
        }
        robot.Sleep(1000);
        //读取艾灸头在位状态
        ret = robot.SndRcvAxleGenComCmdData(6, state, 6, rcvdata);
        printf(" state : %d \n", rcvdata[4]);
        robot.Sleep(1000);
        //开启艾灸头激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, rcvdata);
        printf("led on rcv data is: %d, %d, %d, %d, %d, %d  \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(4000);
        //关闭艾灸头激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, rcvdata);
        printf("led off rcv data is: %d, %d, %d, %d, %d, %d \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(1000);
        printf("***********************complate No. %d SDK test*****************************\n", cnt);
        cnt++;
      }
      robot.CloseRPC();
    }

下载开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 下载开放协议Lua文件
    * @param [in] fileName 开放协议文件名称“CtrlDev_XXX.lua”
    * @param [in] savePath 开放协议保存文件路径
    * @return 错误码
    */
    errno_t OpenLuaDownload(std::string fileName, std::string savePath);
    
删除开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 删除开放协议Lua文件
    * @param [in] fileName 要删除的开放协议lua文件名“CtrlDev_XXX.lua”
    * @return 错误码
    */
    errno_t OpenLuaDelete(std::string fileName);
        
删除所有开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 删除所有开放协议Lua文件
    * @return 错误码
    */
    errno_t AllOpenLuaDelete();

控制器外设开放协议上传下载删除代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestCtrlOpenLuaOperate()
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
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        std::string name[4] = {};
        rtn = robot.GetCtrlOpenLUAName(name);
        printf("ctrl open lua names : %s, %s, %s, %s\n", name[0].c_str(), name[1].c_str(), name[2].c_str(), name[3].c_str());
        rtn = robot.LoadCtrlOpenLUA(1);
        printf("LoadCtrlOpenLUA rtn is %d\n", rtn);
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        printf("UnloadCtrlOpenLUA rtn is %d\n", rtn);
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        printf("OpenLuaDelete rtn is %d\n", rtn);
        rtn = robot.AllOpenLuaDelete();
        printf("AllOpenLuaDelete rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }