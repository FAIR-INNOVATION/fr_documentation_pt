机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置TPD轨迹记录参数
++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDParam(int type, String name, int period_ms, int di_choose, int do_choose);

开始TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  开始轨迹开始TPD轨迹记录记录
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    int SetTPDStart(int type, String name, int period_ms, int di_choose, int do_choose);

停止TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: java
    :linenos:

    /**
    * @brief  停止TPD轨迹记录
    * @return  错误码
    */
    int SetWebTPDStop(); 

删除TPD轨迹记录
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  删除TPD轨迹记录
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */   
    int SetTPDDelete(string name); 

TPD轨迹预加载
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  轨迹预加载
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */      
    int LoadTPD(String name);

TPD轨迹复现
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  轨迹复现
    * @param  [in] name  轨迹文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度缩放百分比，范围[0~100]
    * @return  错误码
    */
    int MoveTPD(String name, int blend, double ovl); 

获取TPD起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取轨迹起始位姿 
    * @param [in] name  轨迹文件名,不需要文件后缀
    * @param [out] desc_pose 获取的轨迹起始位姿
    * @return 错误码 
    */ 
    int GetTPDStartPose(String name, DescPose desc_pose); 

机器人TPD轨迹记录代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTPD(Robot robot)
    {
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        double ovl = 100.0;
        int blend = 0;

        DescPose start_pose =new DescPose() {};

        int rtn = robot.LoadTPD(name);
        System.out.println("LoadTPD rtn is:"+ rtn);

        robot.GetTPDStartPose(name, start_pose);
        robot.MoveCart(start_pose, 0, 0, 100, 100, ovl, -1, -1);
        robot.Sleep(1000);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.println("MoveTPD rtn is: "+ rtn);
        robot.Sleep(5000);

        robot.SetTPDDelete(name);
        return 0;
    }

轨迹预处理
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部轨迹文件预处理 
    * @param [in] name 轨迹文件名  
    * @param [in] ovl 速度缩放百分比，范围[0~100]
    * @param [in] opt 1-控制点，默认为1 
    * @return 错误码 
    */ 
    int LoadTrajectoryJ(String name, double ovl, int opt); 

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部轨迹文件轨迹复现  
    * @return 错误码 
    */
    int MoveTrajectoryJ();

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取轨迹起始位姿 
    * @param [in] name 轨迹文件名  
    * @param [out] desc_pose 获取的轨迹起始位姿
    * @return 错误码 
    */ 
    int GetTrajectoryStartPose(String name, DescPose desc_pose);

获取轨迹点编号
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取轨迹点编号
    * @return  错误码
    */
    public int GetTrajectoryPointNum(int pnum)

设置轨迹运行中的速度
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置轨迹运行中的速度
    * @param  [in] ovl 速度百分比
    * @return  错误码
    */
    public int SetTrajectoryJSpeed(double ovl)

设置轨迹运行中的力和扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置轨迹运行中的力和扭矩
    * @param  [in] ft 三个方向的力和扭矩，单位N和Nm
    * @return  错误码
    */
    public int SetTrajectoryJForceTorque(ForceTorque ft)

设置轨迹运行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿x方向的力  
    * @param [in] fx 沿x方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFx(double fx);

设置轨迹运行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿y方向的力
    * @param [in] fy 沿y方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFy(double fy);

设置轨迹运行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFz(double fz);

设置轨迹运行中的绕x轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕x轴的扭矩  
    * @param [in] tx 绕x轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTx(double tx);

设置轨迹运行中的绕y轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕y轴的扭矩  
    * @param [in] ty 绕y轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTy(double ty);

设置轨迹运行中的绕z轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕z轴的扭矩  
    * @param [in] tz 绕z轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTz(double tz);

上传轨迹J文件
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上传轨迹J文件  
    * @param [in] filePath 上传轨迹文件的全路径名   C://test/testJ.txt
    * @return 错误码 
    */
    int TrajectoryJUpLoad(String filePath);

删除轨迹J文件
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 删除轨迹J文件  
    * @param [in] fileName 文件名称 testJ.txt
    * @return 错误码 
    */
    int TrajectoryJDelete(String fileName);

机器人轨迹J文件复现代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTraj(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");
        System.out.println("Upload TrajectoryJ A :"+ rtn);

        String traj_file_name = "/fruser/traj/traj.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        System.out.println("LoadTrajectoryJ:"+traj_file_name+", rtn is:"+ rtn);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);


        ExaxisPos epos=new ExaxisPos(0,0,0,0);
        DescPose po=new DescPose(0,0,0,0,0,0);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(traj_num);

        rtn = robot.SetTrajectoryJSpeed(50.0);
        System.out.println("SetTrajectoryJSpeed is:"+ rtn);

        ForceTorque traj_force=new ForceTorque(0,0,0,0,0,0);
        traj_force.fx = 10;
        rtn = robot.SetTrajectoryJForceTorque(traj_force);
        System.out.println("SetTrajectoryJForceTorque rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJForceFx(10.0);
        System.out.println("SetTrajectoryJForceFx rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFy(0.0);
        System.out.println("SetTrajectoryJForceFy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFz(0.0);
        System.out.println("SetTrajectoryJForceFz rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTx(10.0);
        System.out.println("SetTrajectoryJTorqueTx rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTy(10.0);
        System.out.println("SetTrajectoryJTorqueTy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJTorqueTz(10.0);
        System.out.println("SetTrajectoryJTorqueTz rtn is:"+ rtn);

        rtn = robot.MoveTrajectoryJ();
        System.out.println("MoveTrajectoryJ rtn is: "+ rtn);

        return 0;
    }

轨迹预处理(轨迹前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 轨迹预处理(轨迹前瞻) 
    * @param [in] name  轨迹文件名
    * @param [in] mode 采样模式，0-不进行采样；1-等数据间隔采样；2-等误差限制采样
    * @param [in] errorLim 误差限制，使用直线拟合生效
    * @param [in] type 平滑方式，0-贝塞尔平滑
    * @param [in] precision 平滑精度，使用贝塞尔平滑时生效
    * @param [in] vamx 设定的最大速度，mm/s
    * @param [in] amax 设定的最大加速度，mm/s2
    * @param [in] jmax 设定的最大加加速度，mm/s3
    * @return 错误码 
    */ 
    int LoadTrajectoryLA(String name, int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax); 

轨迹复现(轨迹前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 轨迹复现(轨迹前瞻)  
    * @return 错误码 
    */
    int MoveTrajectoryLA();

轨迹复现(轨迹前瞻)代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadTrajLA(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");

        String traj_file_name = "/fruser/traj/traj.txt";
        rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        rtn = robot.MoveTrajectoryLA();

        robot.CloseRPC();
        return 0;
    }

运动到TPD轨迹记录起点
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 运动到TPD轨迹记录起点
    * @param name 轨迹文件名
    * @param moveType 运动类型；0-PTP; 1-LIN
    * @param ovl 速度缩放百分比，范围[0~100]
    * @return 错误码
    */
    public int MoveToTPDStart(string name, int moveType, double ovl)

运动到TPD轨迹记录起点的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testTPDmove (Robot robot)
    {
        int rtn = 0;
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(3000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        robot.Sleep(1000);
        double ovl = 100.0;
        int blend = 0;
        DescPose start_pose = new DescPose();
        rtn = robot.LoadTPD(name);
        System.out.printf("LoadTPD rtn is: %d\n", rtn);

        robot.GetTPDStartPose(name, start_pose);
        System.out.printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        //robot.MoveCart(&start_pose, 0, 0, 100, 100, ovl, -1, -1);
        //robot.Sleep(1000);

        rtn = robot.MoveToTPDStart(name, 0, 100);
        System.out.printf("MoveToTPDStart rtn is: %d\n", rtn);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.printf("MoveTPD rtn is: %d\n", rtn);

        robot.Sleep(5000);

        robot.SetTPDDelete(name);

        return ;
    }