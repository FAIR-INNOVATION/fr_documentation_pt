机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置TPD轨迹记录参数
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置TPD轨迹记录参数
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    errno_t  SetTPDParam(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose);

开始TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  开始TPD轨迹记录
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    errno_t  SetTPDStart(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose); 

停止TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  停止TPD轨迹记录
    * @return  错误码
    */
    errno_t  SetWebTPDStop();

删除TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  删除TPD轨迹记录
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */   
    errno_t  SetTPDDelete(char name[30]);

TPD轨迹预加载
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD轨迹预加载
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */      
    errno_t  LoadTPD(char name[30]);

TPD轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD轨迹复现
    * @param  [in] name  轨迹文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度缩放百分比，范围[0~100]
    * @return  错误码
    */
    errno_t  MoveTPD(char name[30], uint8_t blend, float ovl);

获取TPD起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取TPD起始位姿
    * @param [in] name TPD文件名,不需要文件后缀
    * @return 错误码
    */   
    errno_t GetTPDStartPose(char name[30], DescPose *desc_pose);

运动到TPD轨迹记录起点
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 运动到TPD轨迹记录起点
    * @param [in] name 轨迹文件名
    * @param [in] moveType 运动类型；0-PTP; 1-LIN
    * @param [in] ovl 速度缩放百分比，范围[0~100]
    * @return 错误码
    */
    errno_t MoveToTPDStart(char name[30], uint8_t moveType, float ovl);
    
机器人TPD轨迹记录代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTPD(void)
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
    int type = 1;
    char name[30] = "tpd2025";
    int period_ms = 4;
    uint16_t di_choose = 0;
    uint16_t do_choose = 0;
    robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);
    robot.Mode(1);
    robot.Sleep(1000);
    robot.DragTeachSwitch(1);
    robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
    robot.Sleep(3000);
    robot.SetWebTPDStop();
    robot.DragTeachSwitch(0);
    robot.Sleep(1000);
    float ovl = 100.0;
    uint8_t blend = 0;
    DescPose start_pose = {};
    rtn = robot.LoadTPD(name);
    printf("LoadTPD rtn is: %d\n", rtn);
    robot.GetTPDStartPose(name, &start_pose);
    printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
    rtn = robot.MoveToTPDStart(name, 0, 100);
    printf("MoveToTPDStart rtn is: %d\n", rtn);
    rtn = robot.MoveTPD(name, blend, ovl);
    printf("MoveTPD rtn is: %d\n", rtn);
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    robot.SetTPDDelete(name);
    robot.CloseRPC();
    return 0;
    }

轨迹预处理
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 轨迹预处理
    * @param [in] name 轨迹文件名
    * @param [in] ovl 速度缩放百分比，范围[0~100]
    * @param [in] opt 1-控制点，默认为1
    * @return 错误码
    */   
    errno_t LoadTrajectoryJ(char name[30], float ovl, int opt);

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 轨迹复现
    * @return 错误码
    */   
    errno_t MoveTrajectoryJ();

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取轨迹起始位姿
    * @param [in] name 轨迹文件名
    * @return 错误码
    */   
    errno_t GetTrajectoryStartPose(char name[30], DescPose *desc_pose);

获取轨迹点编号
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取轨迹点编号
    * @return 错误码
    */   
    errno_t GetTrajectoryPointNum(int *pnum);

设置轨迹运行中的速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的速度
    * @param [in] ovl 速度百分比
    * @return 错误码
    */   
    errno_t SetTrajectoryJSpeed(float ovl);

设置轨迹运行中的力和扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的力和扭矩
    * @param [in] ft 三个方向的力和扭矩，单位N和Nm
    * @return 错误码
    */   
    errno_t SetTrajectoryJForceTorque(ForceTorque *ft);

设置轨迹运行中的沿x方向的力
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的沿x方向的力
    * @param [in] fx 沿x方向的力，单位N
    * @return 错误码
    */   
    errno_t SetTrajectoryJForceFx(double fx);

设置轨迹运行中的沿y方向的力
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的沿y方向的力
    * @param [in] fy 沿y方向的力，单位N
    * @return 错误码
    */   
    errno_t SetTrajectoryJForceFy(double fy);

设置轨迹运行中的沿z方向的力
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的沿z方向的力
    * @param [in] fz 沿x方向的力，单位N
    * @return 错误码
    */   
    errno_t SetTrajectoryJForceFz(double fz);

设置轨迹运行中的绕x轴的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的绕x轴的扭矩
    * @param [in] tx 绕x轴的扭矩，单位Nm
    * @return 错误码
    */   
    errno_t SetTrajectoryJTorqueTx(double tx);

设置轨迹运行中的绕y轴的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的绕y轴的扭矩
    * @param [in] ty 绕y轴的扭矩，单位Nm
    * @return 错误码
    */   
    errno_t SetTrajectoryJTorqueTy(double ty);

设置轨迹运行中的绕z轴的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置轨迹运行中的绕z轴的扭矩
    * @param [in] tz 绕z轴的扭矩，单位Nm
    * @return 错误码
    */   
    errno_t SetTrajectoryJTorqueTz(double tz);

上传轨迹J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 上传轨迹J文件
	 * @param [in] filePath 上传轨迹文件的全路径名   C://test/testJ.txt
	 * @return 错误码
	 */
	errno_t TrajectoryJUpLoad(const std::string& filePath);

删除轨迹J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 删除轨迹J文件
	 * @param [in] fileName 文件名称 testJ.txt
	 * @return 错误码
	 */
	errno_t TrajectoryJDelete(const std::string& fileName);

机器人轨迹J文件复现代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTraj(void)
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
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj1.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj1.txt";
      rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
      printf("LoadTrajectoryJ %s, rtn is: %d\n", traj_file_name, rtn);
      DescPose traj_start_pose;
      memset(&traj_start_pose, 0, sizeof(DescPose));
      rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
      printf("GetTrajectoryStartPose is: %d\n", rtn);
      printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
      std::this_thread::sleep_for(std::chrono::seconds(1));
      robot.SetSpeed(50);
      robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
      int traj_num = 0;
      rtn = robot.GetTrajectoryPointNum(&traj_num);
      printf("GetTrajectoryStartPose rtn is: %d, traj num is: %d\n", rtn, traj_num);
      rtn = robot.SetTrajectoryJSpeed(50.0);
      printf("SetTrajectoryJSpeed is: %d\n", rtn);
      ForceTorque traj_force;
      memset(&traj_force, 0, sizeof(ForceTorque));
      traj_force.fx = 10;
      rtn = robot.SetTrajectoryJForceTorque(&traj_force);
      printf("SetTrajectoryJForceTorque rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFx(10.0);
      printf("SetTrajectoryJForceFx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFy(0.0);
      printf("SetTrajectoryJForceFy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFz(0.0);
      printf("SetTrajectoryJForceFz rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTx(10.0);
      printf("SetTrajectoryJTorqueTx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTy(10.0);
      printf("SetTrajectoryJTorqueTy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTz(10.0);
      printf("SetTrajectoryJTorqueTz rtn is: %d\n", rtn);
      rtn = robot.MoveTrajectoryJ();
      printf("MoveTrajectoryJ rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

轨迹预处理(轨迹前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 轨迹预处理(轨迹前瞻)
    * @param [in] name 轨迹文件名
    * @param [in] mode 采样模式，0-不进行采样；1-等数据间隔采样；2-等误差限制采样
    * @param [in] errorLim 误差限制，使用直线拟合生效
    * @param [in] type 平滑方式，0-贝塞尔平滑
    * @param [in] precision 平滑精度，使用贝塞尔平滑时生效
    * @param [in] vamx 设定的最大速度，mm/s
    * @param [in] amax 设定的最大加速度，mm/s2
    * @param [in] jmax 设定的最大加加速度，mm/s3
    * @param [in] flag 匀速前瞻开启开关 0-不开启；1-开启
    * @return 错误码
    */
    errno_t LoadTrajectoryLA(char name[30], int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax, int flag = 0);

轨迹复现(轨迹前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  轨迹复现(轨迹前瞻)
    * @return  错误码
    */
    errno_t MoveTrajectoryLA();

轨迹复现(轨迹前瞻)代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLoadTrajLA(void)
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
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj.txt";
      rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);
      printf("LoadTrajectoryLA %s, rtn is: %d\n", traj_file_name, rtn);
      DescPose traj_start_pose;
      memset(&traj_start_pose, 0, sizeof(DescPose));
      rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
      printf("GetTrajectoryStartPose is: %d\n", rtn);
      printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
      std::this_thread::sleep_for(std::chrono::seconds(1));
      robot.SetSpeed(50);
      robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
      rtn = robot.MoveTrajectoryLA();
      printf("MoveTrajectoryLA rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }