机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法
    * @param [in] point_num 点编号,范围[1~6]
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num);

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(DescPose tcp_pose);

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法
    * @param [in] point_num 点编号,范围[1~4]
    * @return 错误码 
    */ 
    int SetTcp4RefPoint(int point_num);

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(DescPose tcp_pose);

根据点位信息计算工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 根据点位信息计算工具坐标系
    * @param [in] method 计算方法；0-四点法；1-六点法
    * @param [in] pos 关节位置组，四点法时数组长度为4个，六点法时数组长度为6个
    * @param [out] tool_pose 输出的工具坐标系
    * @return 错误码 
    */ 
    int ComputeToolCoordWithPoints(int method, JointPos[] pos,DescPose tool_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] coord  工具中心点相对于末端法兰中心位姿
    * @param [in] type  0-工具坐标系，1-传感器坐标系
    * @param [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param [in] toolID  工具ID
    * @param [in] loadNum  负载编号
    * @return 错误码 
    */ 
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

获取当前工具坐标系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工具坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐标系位姿
    * @return  错误码
    */
    int GetTCPOffset(int flag, DescPose desc_pos); 

机器人工具坐标系操作代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTCPCompute(Robot robot)
    {
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint=new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);

        DescPose p2Desc=new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint=new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);

        DescPose p3Desc=new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint=new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);

        DescPose p4Desc=new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint=new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);

        DescPose p5Desc=new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint=new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);

        DescPose p6Desc=new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint=new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
        DescPose coordRtn =new DescPose() {};
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(4);
        robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(5);
        robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(6);
        rtn = robot.ComputeTool(coordRtn);
        robot.SetToolList(3, coordRtn, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(coordRtn);

        robot.SetToolCoord(4, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose(){};
        rtn = robot.GetTCPOffset(0, getCoord);
        return 0;
    }

设置外部工具坐标参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] etcp  工具中心点相对末端法兰中心位姿
    * @param [in] etool  待定
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

机器人外部工具坐标系操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExtCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = { p1Desc , p2Desc , p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(coordRtn);

        robot.SetExToolCoord(1, coordRtn, offdese);
        robot.SetExToolList(1, coordRtn, offdese);
        return 0;
    }

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num);


计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工件坐标系
    * @param [in]  method 计算方式 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in]  refFrame 参考坐标系
    * @param [out]  wobj_pose 工件坐标系
    * @return 错误码 
    */ 
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工件坐标系
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjCoord(int id, DescPose coord, int refFrame);

设置工件坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

根据点位信息计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 根据点位信息计算工件坐标系
    * @param [in] method 计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] pos 三个TCP位置组
    * @param [in] refFrame 参考坐标系
    * @param [in] tcp_pose 输出工件坐标系
    * @return 错误码 
    */ 
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame,DescPose tcp_pose);

获取当前工件坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工件坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件坐标系位姿
    * @return  错误码
    */   
    int GetWObjOffset(int flag, DescPose desc_pos);

机器人工件坐标系操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWobjCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP =new DescPose[]{p1Desc , p2Desc , p3Desc };
        DescPose coordRtn =new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, coordRtn);

        robot.SetWObjCoord(1, coordRtn, 0);
        robot.SetWObjList(1, coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, getWobjDesc);
        return 0;
    }
    
设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置机器人加速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc);

获取机器人默认速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人默认速度
    * @return  List[0]:int 错误码; List[1]: double vel 速度，单位mm/s
    */   
    List<Number> GetDefaultTransVel(); 

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] loadNum 负载编号
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(int loadNum,double weight);

设置末端负载质心坐标
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

设置末端负载质心坐标
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief  设置末端负载质心坐标
     * @param  [in] loadNum 负载编号
     * @param  [in] coord 质心坐标，单位mm
     * @return  错误码
     */
    public int SetLoadCoord(int loadNum, DescTran coord)

获取当前负载的重量
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前负载的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @return  List[0]:int 错误码; List[1]: double weight  负载重量，单位kg
    */
    List<Number> GetTargetPayload(int flag); 

获取当前负载的质心
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前负载的质心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 负载质心，单位mm
    * @return  错误码
    */   
    int GetTargetPayloadCog(int flag, DescTran cog);

设置机器人安装方式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in]  install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(int install); 

设置机器人安装角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

获取机器人安装角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人安装角度
    * @return  List[0]:错误码; List[1]:double yangle 倾斜角; List[2]:double zangle 旋转角
    */
    public List<Number> GetRobotInstallAngle()

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    int SetSysVarValue(int id, double value); 

获取系统变量值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取系统变量值
    * @param  [in] id 系统变量编号，范围[1~20]
    * @return  List[0]:错误码; List[1]:double value 系统变量值
    */
    List<Number> GetSysVarValue(int id); 

机器人常用设置代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadInstall(Robot robot)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            robot.Sleep(30);
        }

        List<Number> defaultVel=new ArrayList<>();

        defaultVel=robot.GetDefaultTransVel();
        System.out.println("GetDefaultTransVel is:"+ defaultVel.get(1));

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5);
            robot.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            float value = 0;
            defaultVel=robot.GetSysVarValue(i);
            System.out.println("sys value :"+i+", is :"+defaultVel.get(1));
            robot.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0;
        loadCoord.y = 4.0;
        loadCoord.z = 5.0;
        robot.SetLoadCoord(loadCoord);

        robot.Sleep(1000);

        List<Number> getLoad = new ArrayList<>();

        getLoad=robot.GetTargetPayload(0);

        DescTran getLoadTran =new DescTran();
        robot.GetTargetPayloadCog(0, getLoadTran);
        System.out.println("get load is:"+getLoad.get(1)+", get load cog is: "+getLoadTran.x+","+getLoadTran.y+","+getLoadTran.z);

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0, 25.0);

        List<Number> angle=new ArrayList<>();
        angle=robot.GetRobotInstallAngle();
        System.out.println("GetRobotInstallAngle x:"+angle.get(1)+";  y:"+angle.get(2));

        robot.CloseRPC();
        return 0;
    }

关节摩擦力补偿开关
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 关节摩擦力补偿开关 
    * @param [in] state  0-关，1-开
    * @return 错误码 
    */ 
    int FrictionCompensationOnOff(int state); 

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-正装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_level(Object[] coeff);

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-侧装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_wall(Object[] coeff); 

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-倒装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_ceiling(Object[] coeff);

设置关节摩擦力补偿系数-自由安装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-自由安装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_freedom(Object[] coeff);

机器人设置关节摩擦力补偿代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFriction(Robot robot)
    {

        Object[] lcoeff = { 0.9,0.9,0.9,0.9,0.9,0.9 };
        Object[] wcoeff = { 0.4,0.4,0.4,0.4,0.4,0.4 };
        Object[] ccoeff = { 0.6,0.6,0.6,0.6,0.6,0.6 };
        Object[] fcoeff = { 0.5,0.5,0.5,0.5,0.5,0.5 };

        int rtn = robot.FrictionCompensationOnOff(1);
        System.out.println("FrictionCompensationOnOff rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_level(lcoeff);
        System.out.println("SetFrictionValue_level rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_wall(wcoeff);
        System.out.println("SetFrictionValue_wall rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        System.out.println("SetFrictionValue_ceiling rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        System.out.println("SetFrictionValue_freedom rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

查询机器人错误码
++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief  查询机器人错误码
     * @param  [out]  maincode  主错误码
     * @param  [out]  subcode   子错误码
     * @return  错误码
     */ 
    int GetRobotErrorCode(int[] maincode, int[] subcode);

错误状态清除
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  错误状态清除
    * @return  错误码
    */
    int ResetAllError(); 

机器人故障状态获取及清除错误代码示例
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetError(Robot robot)
    {
        int[] maincode={0}, subcode={0};
        robot.GetRobotErrorCode(maincode, subcode);

        robot.ResetAllError();

        robot.Sleep(1000);

        robot.GetRobotErrorCode(maincode, subcode);
        return 0;
    }

设置宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置宽电压控制箱温度及风扇转速监控参数
    * @param [in] enable 0-不使能监测；1-使能监测
    * @param [in] period 监测周期(s),范围1-100
    * @return 错误码
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

获取宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取宽电压控制箱温度及风扇转速监控参数
    * @return List[0]-错误码,List[1]-enable 0-不使能监测；1-使能监测,List[2]-period 监测周期(s),范围1-100
    */
    List<Number> GetWideBoxTempFanMonitorParam()

宽电压控制箱温度和风扇电流状态获取代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestWideVoltageCtrlBoxtemp(Robot robot)
    {
        robot.SetWideBoxTempFanMonitorParam(1, 2);
        List<Number> list=robot.GetWideBoxTempFanMonitorParam();
        System.out.println("GetWideBoxTempFanMonitorParam enable is:"+list.get(1)+", period is:"+list.get(2));
        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+",fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);

        list=robot.GetWideBoxTempFanMonitorParam();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+" ,fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        robot.CloseRPC();
        robot.Sleep(2000);
        return 0;
    }

设置焦点标定点
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置焦点标定点
    * @param [in] pointNum 焦点标定点编号 1-8
    * @param [in] point    标定点坐标
    * @return 错误码
    */
    int SetFocusCalibPoint(int pointNum, DescPose point)

计算焦点标定结果
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 计算焦点标定结果
    * @param [in] pointNum  标定点个数
    * @param [in] resultPos 标定结果XYZ
    * @param [out] accuracy  标定精度误差
    * @return 错误码
    */
    int ComputeFocusCalib(int pointNum, DescTran resultPos, double[] accuracy)

开启焦点跟随
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 开启焦点跟随
    * @param [in] kp       比例参数，默认50.0
    * @param [in] kpredict 前馈参数，默认19.0
    * @param [in] aMax     最大角加速度限制，默认1440°/s^2
    * @param [in] vMax     最大角速度限制，默认180°/s
    * @param [in] type     锁定X轴指向(0-参考输入矢量；1-水平；2-垂直)
    * @return 错误码
    */
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type)

停止焦点跟随
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 停止焦点跟随
    * @return 错误码
    */
    int FocusEnd()

设置焦点坐标
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:
    
    /**
    * @brief 设置焦点坐标
    * @param pos 焦点坐标XYZ
    * @return 错误码
    */
    public int SetFocusPosition(DescTran pos)

焦点跟随代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFocus(Robot robot){
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint = new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);

        DescPose p2Desc = new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint = new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);

        DescPose p3Desc = new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint = new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);

        DescPose p4Desc = new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint = new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);

        DescPose p5Desc = new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint = new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);

        DescPose p6Desc = new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint = new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 100, 0, 0, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint,  p2Desc);
        robot.GetForwardKin(p3Joint,  p3Desc);
        robot.GetForwardKin(p4Joint,  p4Desc);
        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);

        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4( coordRtn);

        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint, p2Desc);
        robot.GetForwardKin(p3Joint, p3Desc);

        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);

        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double[] accuracy = {0.0};
        rtn = robot.ComputeFocusCalib(3,  resultPos,  accuracy);
        rtn = robot.SetFocusPosition(resultPos);

        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);

        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.FocusEnd();
    }

关节扭矩传感器灵敏度标定功能开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度标定功能开启
    * @param status 0-关闭；1-开启
    * @return 错误码
    */
    public int JointSensitivityEnable(int status)

关节扭矩传感器灵敏度数据采集
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度数据采集
    * @return 错误码
    */
    public int JointSensitivityCollect()

获取关节扭矩传感器灵敏度标定结果
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取关节扭矩传感器灵敏度标定结果
    * @param calibResult j1~j6关节灵敏度[0-1]
    * @param linearityn j1~j6关节线性度[0-1]
    * @return 错误码
    */
    public int JointSensitivityCalibration(double calibResult[6], double linearity[6])

获取关节扭矩传感器迟滞误差
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief 获取关节扭矩传感器迟滞误差
    * @param hysteresisError j1~j6关节迟滞误差
    * @return 错误码
    */
    public int JointHysteresisError(double[] hysteresisError);
    
获取关节扭矩传感器重复精度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:
    
    /**
    * @brief 获取关节扭矩传感器重复精度
    * @param repeatability j1~j6关节扭矩传感器重复精度
    * @return 错误码
    */
    public int JointRepeatability(double[] repeatability);
    
设置关节力传感器参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置关节力传感器参数
    * @param 必选参数 M J1-J6质量系数[]
    * @param 必选参数 B J1-J6阻尼系数[]
    * @param 必选参数 K J1-J6刚度系数[]
    * @param 默认参数 threshold 力控制阈值，Nm
    * @param 默认参数 sensitivity 灵敏度,Nm/V,[]
    * @param 默认参数 setZeroFlag 功能开启标志位；0-关闭；1-开启；2-位置1记录零点；3-位置2记录零点
    * @return 错误码
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

关节扭矩传感器灵敏度自动标定代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSensitivityCalib(Robot robot)
    {
        int rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        JointPos curJPos = new JointPos();
        robot.GetActualJointPosDegree(curJPos);
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos =new DescPose(0,0,0,0,0,0 );
        JointPos jointPos1 = new JointPos(curJPos.J1, 0, 0, -90, 0.02, curJPos.J6);
        DescPose descPos1 = new DescPose();
        robot.GetForwardKin(jointPos1, descPos1);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 1 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos2 =new JointPos( curJPos.J1, -30, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos2 =new DescPose();
        robot.GetForwardKin(jointPos2, descPos2);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 2 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos3 = new JointPos( curJPos.J1, -60, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos3 =new DescPose();
        robot.GetForwardKin(jointPos3, descPos3);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 3 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos4 = new JointPos(curJPos.J1, -90, 0, -90, 0.02, curJPos.J6);
        DescPose descPos4 = new DescPose();
        robot.GetForwardKin(jointPos4, descPos4);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 4 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos5 = new JointPos(curJPos.J1, -120, 0, -90, 0.02, curJPos.J6);
        DescPose descPos5 = new DescPose();
        robot.GetForwardKin(jointPos5, descPos5);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 5 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos6 = new JointPos(curJPos.J1, -150, 0, -90, 0.02, curJPos.J6);
        DescPose descPos6 = new DescPose();
        robot.GetForwardKin(jointPos6, descPos6);
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 6 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos7 = new JointPos(curJPos.J1, -180, 0, -90, 0.02, curJPos.J6);
        DescPose descPos7 = new DescPose();
        robot.GetForwardKin(jointPos7, descPos7);
        robot.MoveJ(jointPos7, descPos7, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 7 rtn is %d\n", rtn);
        robot.Sleep(100);
        //反向行程
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 8 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 9 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 10 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 11 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 12 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 13 rtn is %d\n", rtn);
        robot.Sleep(100);
        double[] calibResult =new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(calibResult, linearity);
        System.out.printf("JointSensitivityCalibration rtn is %d\n", rtn);
        rtn = robot.JointSensitivityEnable(0);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        System.out.printf("jointSensor Calib result is %f %f %f %f %f %f\njointSensor linearity is %f %f %f %f %f %f\n",
                calibResult[0], calibResult[1], calibResult[2],
                calibResult[3], calibResult[4], calibResult[5],
                linearity[0], linearity[1], linearity[2],
                linearity[3], linearity[4], linearity[5]);
        double[] hysteresisError = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointHysteresisError(hysteresisError);
        System.out.printf("JointHysteresisError result is %f %f %f %f %f %f\n",
                hysteresisError[0], hysteresisError[1], hysteresisError[2],
                hysteresisError[3], hysteresisError[4], hysteresisError[5]);
        double[] repeatability = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointRepeatability(repeatability);
        System.out.printf("JointRepeatability result is %f %f %f %f %f %f\n",
                repeatability[0], repeatability[1], repeatability[2],
                repeatability[3], repeatability[4], repeatability[5]);
        double[] M = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] B = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] K = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double[] threshold = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        System.out.printf("SetAdmittanceParams rtn is %d\n", rtn);
    }

获取机器人8个从站端口错误帧数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人8个从站端口错误帧数
    * @param  inRecvErr 输入接收错误帧数
    * @param  inCRCErr 输入CRC错误帧数
    * @param  inTransmitErr 输入转发错误帧数
    * @param  inLinkErr 输入链接错误帧数
    * @param  outRecvErr 输出接收错误帧数
    * @param  outCRCErr 输出CRC错误帧数
    * @param  outTransmitErr 输出转发错误帧数
    * @param  outLinkErr 输出链接错误帧数
    * @return 错误码
    */
    public int GetSlavePortErrCounter(int[] inRecvErr, int[] inCRCErr, int[] inTransmitErr, int[] inLinkErr, int[] outRecvErr, int[] outCRCErr, int[] outTransmitErr, int[] outLinkErr)

从站端口错误帧清零
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 从站端口错误帧清零
    * @param slaveID 从站编号0~7
    * @return 错误码
    */
    public int SlavePortErrCounterClear(int slaveID)

获取从站端口错误帧代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSlavePortErr(Robot robot)
    {
        ROBOT_STATE_PKG pkg =new ROBOT_STATE_PKG();
        int[] inRecvErr =new int[8];
        int[] inCRCErr =new int[8];
        int[] inTransmitErr =new int[8];
        int[] inLinkErr =new int[8];
        int[] outRecvErr =new int[8];
        int[] outCRCErr =new int[8];
        int[] outTransmitErr =new int[8];
        int[] outLinkErr =new int[8];
        robot.GetSlavePortErrCounter(inRecvErr,  inCRCErr, inTransmitErr, inLinkErr,
                outRecvErr, outCRCErr, outTransmitErr, outLinkErr);
        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inRecvErr[i]);
            }
            if (inCRCErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inCRCErr[i]);
            }
            if (inTransmitErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inTransmitErr[i]);
            }
            if (inLinkErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inLinkErr[i]);
            }
            if (outRecvErr[i] != 0)
            {
                System.out.printf("outRecvErr %d is %d\n", i, outRecvErr[i]);
            }
            if (outCRCErr[i] != 0)
            {
                System.out.printf("outCRCErr %d is %d\n", i, outCRCErr[i]);
            }
            if (outTransmitErr[i] != 0)
            {
                System.out.printf("outTransmitErr %d is %d\n", i, outTransmitErr[i]);
            }
            if (outLinkErr[i] != 0)
            {
                System.out.printf("outLinkErr %d is %d\n", i, outLinkErr[i]);
            }
        }
        System.out.printf("others has no err!\n");
        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }
        robot.CloseRPC();
    }

设置各轴速度前馈系数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置各轴速度前馈系数
    * @param  radio 各轴速度前馈系数
    * @return 错误码
    */
    public int SetVelFeedForwardRatio(double[] radio)

获取各轴速度前馈系数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取各轴速度前馈系数
    * @param  radio 各轴速度前馈系数
    * @return 错误码
    */
    public int GetVelFeedForwardRatio(double[] radio)

机器人速度前馈系数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestVelFeedForwardRatio(Robot robot)
    {
        double[] setRadio =new double[] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[]{ 0.0 };
        robot.GetVelFeedForwardRatio(getRadio);
        System.out.printf(" %f %f %f %f %f %f\n", getRadio[0], getRadio[1], getRadio[2], getRadio[3], getRadio[4], getRadio[5]);
        robot.CloseRPC();
    }

光电传感器TCP标定-计算工具RPY
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定-计算工具RPY
    * @param  Btool 机器人笛卡尔位置
    * @param  Etool 当前工具坐标系数值
    * @param  sensor 当前传感器坐标系数值(暂未开放)
    * @param  radius 圆周运动半径mm(暂未开放)
    * @param  dz 沿基座标系z轴负方向运动距离；当dz = 10000时，函数直接返回工具RPY
    * @param  TCPRPY 工具RPY数值
    * @return 错误码
    */
    public int TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, Rpy TCPRPY)

光电传感器TCP标定-计算工具XYZ
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定-计算工具XYZ
    * @param  select 0-计算工具TCP；1-计算传感器原点；2-计算传感器姿态；3-直接返回工具TCP；4-记录当前工件坐标系和工具坐标系
    * @param  originDirection 0-X方向；1-Y方向；2-Z方向
    * @param  pos1 机器人笛卡尔位置1
    * @param  pos2 机器人笛卡尔位置2
    * @param  pos3 机器人笛卡尔位置3
    * @param  pos4 机器人笛卡尔位置4
    * @param  TCP 工具XYZ数值
    * @return 错误码
    */
    public int TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2, DescTran pos3, DescTran pos4, DescTran TCP)

光电传感器TCP标定-开始记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定-开始记录末端法兰中心位置
    * @return 错误码
    */
    public int TCPRecordFlangePosStart()

光电传感器TCP标定-停止记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定-停止记录末端法兰中心位置
    * @return 错误码
    */
    public int TCPRecordFlangePosEnd()

光电传感器TCP标定-获取末端工具中心点位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定-获取末端工具中心点位置
    * @param  TCP 工具中心点位置(x,y,z)
    * @return 错误码
    */
    public int TCPGetRecordFlangePos(DescTran TCP)

光电传感器TCP标定
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 光电传感器TCP标定
    * @param luaPath 自动标定lua程序路径：QX版本机器人-"/fruser/FR_CalibrateTheToolTcp.lua";LA版本机器人-"/usr/local/etc/controller/lua/FR_CalibrateTheToolTcp.lua"
    * @param offset 示教点偏移(x,y,z)mm
    * @param TCP 标定后的工具坐标系(x,y,z,rx,ry,rz)
    * @return 错误码
    */
    public int PhotoelectricSensorTCPCalibration(String luaPath, DescTran offset, DescPose TCP)

光电传感器TCP标定代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestPhotoelectricSensorTCPCalib(Robot robot)
    {
        DescTran offset = new DescTran(10.0, 10.0, 3.0 );
        DescPose TCP = new DescPose();
        int rtn = robot.PhotoelectricSensorTCPCalibration("/fruser/FR_CalibrateTheToolTcp.lua", offset, TCP);
        System.out.printf("PhotoelectricSensorTCPCalibration rtn is %d %f %f %f %f %f %f \n", rtn, TCP.tran.x, TCP.tran.y, TCP.tran.z, TCP.rpy.rx, TCP.rpy.ry, TCP.rpy.rz);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }