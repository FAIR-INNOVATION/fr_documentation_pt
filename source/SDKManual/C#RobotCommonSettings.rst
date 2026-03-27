机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法 
    * @param [in] point_num 点编号,范围[1~6] 
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num); 

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(ref DescPose tcp_pose); 

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法 
    * @param [in] point_num 点编号,范围[1~4] 
    * @return 错误码 
    */ 
    int SetTcp4RefPoint(int point_num);

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(ref DescPose tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具坐标系
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * param   [in] toolID 工具ID
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);

根据点位信息计算工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 根据点位信息计算工具坐标系
    * @param [in] method 计算方法；0-四点法；1-六点法
    * @param [in] pos 关节位置组，四点法时数组长度为4个，六点法时数组长度为6个
    * @return 错误码
    */

    int ComputeToolCoordWithPoints(int method, JointPos[] pos, ref DescPose coordRtn)  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐标系位姿
    * @return  错误码
    */
    int GetTCPOffset(byte flag, ref DescPose desc_pos); 

机器人工具坐标系操作代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button18_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(186.331f, 487.913f, 209.850f, 149.030f, 0.688f, -114.347f);
        JointPos p1Joint = new JointPos(-127.876f, -75.341f, 115.417f, -122.741f, -59.820f, 74.300f);

        DescPose p2Desc = new DescPose(69.721f, 535.073f, 202.882f, -144.406f, -14.775f, -89.012f);
        JointPos p2Joint = new JointPos(-101.780f, -69.828f, 110.917f, -125.740f, -127.841f, 74.300f);

        DescPose p3Desc = new DescPose(146.861f, 578.426f, 205.598f, 175.997f, -36.178f, -93.437f);
        JointPos p3Joint = new JointPos(-112.851f, -60.191f, 86.566f, -80.676f, -97.463f, 74.300f);

        DescPose p4Desc = new DescPose(136.284f, 509.876f, 225.613f, 178.987f, 1.372f, -100.696f);
        JointPos p4Joint = new JointPos(-116.397f, -76.281f, 113.845f, -128.611f, -88.654f, 74.299f);

        DescPose p5Desc = new DescPose(138.395f, 505.972f, 298.016f, 179.134f, 2.147f, -101.110f);
        JointPos p5Joint = new JointPos(-116.814f, -82.333f, 109.162f, -118.662f, -88.585f, 74.302f);

        DescPose p6Desc = new DescPose(105.553f, 454.325f, 232.017f, -179.426f, 0.444f, -99.952f);
        JointPos p6Joint = new JointPos(-115.649f, -84.367f, 122.447f, -128.663f, -90.432f, 74.303f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = new JointPos[] { p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, ref coordRtn);
        Console.WriteLine($"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(4);
        robot.MoveJ( p5Joint,  p5Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(5);
        robot.MoveJ( p6Joint,  p6Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(6);
        rtn = robot.ComputeTool(ref coordRtn);
        Console.WriteLine($"6 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
        robot.SetToolList(1,  coordRtn, 0, 0, 0);

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose();
        rtn = robot.GetTCPOffset(0, ref getCoord);
        Console.WriteLine($"GetTCPOffset    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
    }

设置外部工具坐标参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3] 
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14] 
    * @param [in] etcp 工具中心点相对末端法兰中心位姿 
    * @param [in] etool 待定 
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

根据点位信息计算工件坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 根据点位信息计算工件坐标系
    * @param [in] method 计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] pos 三个TCP位置组
    * @param [in] refFrame 参考坐标系
    * @return 错误码
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, ref DescPose coordRtn)

机器人外部工具坐标系操作代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button20_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606f, 779.517f, 193.516f, 178.000f, 0.476f, -92.484f);
        JointPos p1Joint = new JointPos(-108.145f, -50.137f, 85.818f, -125.599f, -87.946f, 74.329f);

        DescPose p2Desc = new DescPose(-24.656f, 850.384f, 191.361f, 177.079f, -2.058f, -95.355f);
        JointPos p2Joint = new JointPos(-111.024f, -41.538f, 69.222f, -114.913f, -87.743f, 74.329f);

        DescPose p3Desc = new DescPose(-99.813f, 766.661f, 241.878f, -176.817f, 1.917f, -91.604f);
        JointPos p3Joint = new JointPos(-107.266f, -56.116f, 85.971f, -122.560f, -92.548f, 74.331f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(ref coordRtn);
        Console.WriteLine($"ComputeExTCF                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetExToolCoord(1,  coordRtn,  offdese);
        robot.SetExToolList(1,  coordRtn,  offdese);
    }

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]  
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num); 

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  计算工件坐标系
    * @param [in] method 计算方法 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] refFrame 参考坐标系
    * @param [out] wobj_pose 工件坐标系
    * @return 错误码
    */
    int ComputeWObjCoord(int method, int refFrame, ref DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

获取当前工件坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工件坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件坐标系位姿
    * @return  错误码
    */   
    int GetWObjOffset(byte flag, ref DescPose desc_pos); 

机器人工件坐标系操作代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button19_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint = new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc = new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint = new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc = new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint = new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint,ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoord                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetWObjCoord(1,  coordRtn, 0);
        robot.SetWObjList(1,  coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, ref getWobjDesc);
        Console.WriteLine($"GetWObjOffset                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");   
    } 

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置机器人加速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc)

获取机器人默认速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人默认速度
    * @param  [out]  vel  速度，单位mm/s
    * @return  错误码
    */   
    int GetDefaultTransVel(ref double vel); 

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] loadNum 负载编号
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(int loadNum, float weight)

设置末端负载质心坐标
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

获取当前负载的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前负载的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 负载重量，单位kg
    * @return  错误码
    */
    int GetTargetPayload(byte flag, ref double weight); 

获取当前负载的质心
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前负载的质心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 负载质心，单位mm
    * @return  错误码
    */   
    int GetTargetPayloadCog(byte flag, ref DescTran cog);

设置机器人安装方式
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in] install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(byte install); 

设置机器人安装角度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

获取机器人安装角度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人安装角度
    * @param  [out] yangle 倾斜角
    * @param  [out] zangle 旋转角
    * @return  错误码
    */
    int GetRobotInstallAngle(ref double yangle, ref double zangle); 

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    int SetSysVarValue(int id, double value); 

获取系统变量值
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取系统变量值
    * @param  [in] id 系统变量编号，范围[1~20]
    * @param  [out] value  系统变量值
    * @return  错误码
    */
    int GetSysVarValue(int id, ref double value); 

机器人常用设置代码示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button21_Click(object sender, EventArgs e)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            Thread.Sleep(30);
        }

        double defaultVel = 0.0f;
        robot.GetDefaultTransVel(ref defaultVel);
        Console.WriteLine($"GetDefaultTransVel is {defaultVel}");

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5f);
            Thread.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            double value = 0;
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value  {i} is :{value}");
            Thread.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5f);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0f;
        loadCoord.y = 4.0f;
        loadCoord.z = 5.0f;
        robot.SetLoadCoord( loadCoord);

        Thread.Sleep(1000);

        double getLoad = 0.0f;
        robot.GetTargetPayload(0, ref getLoad);

        DescTran getLoadTran = new DescTran();
        robot.GetTargetPayloadCog(0, ref getLoadTran);
        Console.WriteLine($"get load is {getLoad}; get load cog is {getLoadTran.x} {getLoadTran.y} {getLoadTran.z}");

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0f, 25.0f);

        double anglex = 0.0f;
        double angley = 0.0f;
        robot.GetRobotInstallAngle(ref anglex, ref angley);
        Console.WriteLine($"GetRobotInstallAngle x:  {anglex};  y:  {angley}");
    }

关节摩擦力补偿开关
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 关节摩擦力补偿开关 
    * @param [in] state 0-关，1-开 
    * @return 错误码 
    */ 
    int FrictionCompensationOnOff(byte state); 

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-正装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_level(double[] coeff);

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-侧装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_wall(double[] coeff); 

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-倒装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_ceiling(double[] coeff);

设置关节摩擦力补偿系数-自由安装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-自由安装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_freedom(double[] coeff);
       
机器人设置关节摩擦力补偿代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] lcoeff = { 0.9f, 0.9f, 0.9f, 0.9f, 0.9f, 0.9f };
        double[] wcoeff = { 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f };
        double[] ccoeff = { 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f };
        double[] fcoeff = { 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f };

        int rtn = robot.FrictionCompensationOnOff(1);
        Console.WriteLine($"FrictionCompensationOnOff rtn is{rtn}");

        rtn = robot.SetFrictionValue_level(lcoeff);
        Console.WriteLine($"SetFrictionValue_level rtn is {rtn}");

        rtn = robot.SetFrictionValue_wall(wcoeff);
        Console.WriteLine($"SetFrictionValue_wall rtn is{rtn}");

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        Console.WriteLine($"SetFrictionValue_ceiling rtn is {rtn}");

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        Console.WriteLine($"SetFrictionValue_freedom rtn is {rtn}");
    }

查询机器人错误码
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人错误码 
    * @param [out] maincode   主错误码
    * @param [out] subcode    子错误码
    * @return 错误码 
    */ 
    int GetRobotErrorCode(ref int maincode, ref int subcode);

错误状态清除
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  错误状态清除
    * @return  错误码
    */
    int ResetAllError(); 

机器人故障状态获取及清除错误代码示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        int maincode=0, subcode=0;
        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is {subcode}" );

        robot.ResetAllError();

        Thread.Sleep(1000);

        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is{subcode}");
    }

设置宽电压控制箱温度及风扇转速监控参数
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置宽电压控制箱温度及风扇转速监控参数
    * @param [in] enable 0-不使能监测；1-使能监测
    * @param [in] period 监测周期(s),范围1-100
    * @return 错误码
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

获取宽电压控制箱温度及风扇转速监控参数
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取宽电压控制箱温度及风扇转速监控参数
    * @param [out] enable 0-不使能监测；1-使能监测
    * @param [out] period 监测周期(s),范围1-100
    * @return 错误码
    */
    int GetWideBoxTempFanMonitorParam(ref int enable, ref int period);

代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        var pkg = new ROBOT_STATE_PKG(); 
        robot.SetWideBoxTempFanMonitorParam(1, 2);    
        int enable = 0;
        int period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }       
        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
        Console.WriteLine($"SetWideBoxTempFanMonitorParam rtn is {rtn}");       
        enable = 0;
        period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($" robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }
    }

设置焦点标定点
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焦点标定点
    * @param [in] pointNum 焦点标定点编号 1-8
    * @param [in] point 标定点坐标
    * @return 错误码
    */
    int SetFocusCalibPoint(int pointNum, DescPose point);

设置焦点坐标
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焦点坐标
    * @param [in] pos 焦点坐标XYZ
    * @return 错误码
    */
    int SetFocusPosition(DescTran pos);

开启焦点跟随
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 开启焦点跟随
    * @param [in] kp 比例参数，默认50.0
    * @param [in] kpredict 前馈参数，默认19.0
    * @param [in] aMax 最大角加速度限制，默认1440°/s^2
    * @param [in] vMax 最大角速度限制，默认180°/s
    * @param [in] type 锁定X轴指向(0-参考输入矢量；1-水平；2-垂直)
    * @return 错误码
    */
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type);

停止焦点跟随
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 停止焦点跟随
    * @return 错误码
    */
    int FocusEnd();

焦点跟随代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    private void button81_Click(object sender, EventArgs e)
    {
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
        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.GetForwardKin(p4Joint, ref p4Desc);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool      {rtn} coord is {coordRtn.tran.x} ,{coordRtn.tran.y} ,{coordRtn.tran.z} ,{coordRtn.rpy.rx} ,{coordRtn.rpy.ry} ,{coordRtn.rpy.rz} ");
        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);
        robot.GetForwardKin(p1Joint, ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);
        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double accuracy = 0.0;
        rtn = robot.ComputeFocusCalib(3, ref resultPos, ref accuracy);
        Console.WriteLine($"ComputeFocusCalib coord is  {rtn},{ resultPos.x} ,{ resultPos.y}, { resultPos.z}, accuracy is {accuracy} ");
        rtn = robot.SetFocusPosition(resultPos);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusEnd();
    }

关节扭矩传感器灵敏度标定功能开启
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度标定功能开启
    * @param [in] status 0-关闭；1-开启
    * @return  错误码
    */
    public int JointSensitivityEnable(int status);

关节扭矩传感器灵敏度数据采集
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度数据采集
    * @return 错误码
    */
    public int JointSensitivityCollect();

获取关节扭矩传感器灵敏度标定结果
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取关节扭矩传感器灵敏度标定结果
    * @param [out] calibResult j1~j6关节灵敏度[0-1]
    * @param [out] linearityn j1~j6关节线性度[0-1]
    * @return 错误码
    */
    public int JointSensitivityCalibration(double calibResult[6], double linearity[6]);

获取关节扭矩传感器迟滞误差
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取关节扭矩传感器迟滞误差
    * @param [out] hysteresisError j1~j6关节迟滞误差
    * @return 错误码
    */
    public int JointHysteresisError(ref double[] hysteresisError);
    
获取关节扭矩传感器重复精度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:
    
    /**
    * @brief 获取关节扭矩传感器重复精度
    * @param [out] repeatability j1~j6关节扭矩传感器重复精度
    * @return 错误码
    */
    public int JointRepeatability(ref double[] repeatability);
    
设置关节力传感器参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置关节力传感器参数
    * @param [in] M J1-J6质量系数[0.001 ~ 10]
    * @param [in] B J1-J6阻尼系数[0.001 ~ 10]
    * @param [in] K J1-J6刚度系数[0.001 ~ 10]
    * @param [in] threshold 力控制阈值，Nm
    * @param [in] sensitivity 灵敏度,Nm/V,[0 ~ 10]
    * @param [in] setZeroFlag 功能开启标志位；0-关闭；1-开启；2-位置1记录零点；3-位置2记录零点
    * @return 错误码
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

关节扭矩传感器灵敏度自动标定代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public int TestSensitivityCalib()
    {
        int rtn; 
        rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");

        JointPos curJPos = new JointPos(0, 0, 0, 0, 0, 0);
        robot.GetActualJointPosDegree(0, ref curJPos);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        JointPos[] jointPoses = new JointPos[]
        {
            new JointPos(curJPos.jPos[0], 0, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -30, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -60, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -90, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -120, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -150, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -180, 0, -90, 0.02, curJPos.jPos[5])
        };
        for (int i = 0; i < jointPoses.Length; i++)
        {
            DescPose descPos = new DescPose(0, 0, 0, 0, 0, 0);
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            Thread.Sleep(i == 0 ? 200 : 100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {i + 1} rtn is {rtn}");
            Thread.Sleep(100);
        }

        for (int i = jointPoses.Length - 2; i >= 0; i--)
        {
            DescPose descPos = new DescPose();
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            Thread.Sleep(100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {jointPoses.Length + (jointPoses.Length - 1 - i)} rtn is {rtn}");
            Thread.Sleep(100);
        }
        double[] calibResult = new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(ref calibResult, ref linearity);
        Console.WriteLine($"JointSensitivityCalibration rtn is {rtn}");
        rtn = robot.JointSensitivityEnable(0);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");
        Console.WriteLine($"jointSensor Calib result is {calibResult[0]:F6} {calibResult[1]:F6} {calibResult[2]:F6} {calibResult[3]:F6} {calibResult[4]:F6} {calibResult[5]:F6}");
        Console.WriteLine($"jointSensor linearity is {linearity[0]:F6} {linearity[1]:F6} {linearity[2]:F6} {linearity[3]:F6} {linearity[4]:F6} {linearity[5]:F6}"); 
        double[] hysteresisError = new double[6];
        rtn = robot.JointHysteresisError(ref hysteresisError);
        Console.WriteLine($"JointHysteresisError result is {hysteresisError[0]:F6} {hysteresisError[1]:F6} {hysteresisError[2]:F6} {hysteresisError[3]:F6} {hysteresisError[4]:F6} {hysteresisError[5]:F6}");   
        double[] repeatability = new double[6];
        rtn = robot.JointRepeatability(ref repeatability);
        Console.WriteLine($"JointRepeatability result is {repeatability[0]:F6} {repeatability[1]:F6} {repeatability[2]:F6} {repeatability[3]:F6} {repeatability[4]:F6} {repeatability[5]:F6}");
        double[] M = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] B = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] K = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] threshold = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        Console.WriteLine($"SetAdmittanceParams rtn is {rtn}");
        robot.CloseRPC();
        return 0;
    }

获取机器人8个从站端口错误帧数
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人8个从站端口错误帧数
    * @param [out] inRecvErr 输入接收错误帧数 
    * @param [out] inCRCErr 输入CRC错误帧数 
    * @param [out] inTransmitErr 输入转发错误帧数 
    * @param [out] inLinkErr 输入链接错误帧数 
    * @param [out] outRecvErr 输出接收错误帧数
    * @param [out] outCRCErr 输出CRC错误帧数
    * @param [out] outTransmitErr 输出转发错误帧数
    * @param [out] outLinkErr 输出链接错误帧数
    * @return 错误码
    */
    public int GetSlavePortErrCounter(ref int[] inRecvErr,ref int[] inCRCErr,ref int[] inTransmitErr,ref int[] inLinkErr,ref int[] outRecvErr,ref int[] outCRCErr,ref int[] outTransmitErr,ref int[] outLinkErr);

从站端口错误帧清零
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 从站端口错误帧清零
    * @param [in] slaveID 从站编号0~7
    * @return 错误码
    */
    public int SlavePortErrCounterClear(int slaveID);

获取从站端口错误帧代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public void TestSlavePortErr()
    {
        int[] inRecvErr = new int[8];
        int[] inCRCErr = new int[8];
        int[] inTransmitErr = new int[8];
        int[] inLinkErr = new int[8];
        int[] outRecvErr = new int[8];
        int[] outCRCErr = new int[8];
        int[] outTransmitErr = new int[8];
        int[] outLinkErr = new int[8];

        robot.GetSlavePortErrCounter(ref inRecvErr, ref inCRCErr, ref inTransmitErr, ref inLinkErr,
            ref outRecvErr, ref outCRCErr, ref outTransmitErr, ref outLinkErr);

        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                Console.WriteLine($"inRecvErr {i} is {inRecvErr[i]}");
            }

            if (inCRCErr[i] != 0)
            {
                Console.WriteLine($"inCRCErr {i} is {inCRCErr[i]}");
            }

            if (inTransmitErr[i] != 0)
            {
                Console.WriteLine($"inTransmitErr {i} is {inTransmitErr[i]}");
            }

            if (inLinkErr[i] != 0)
            {
                Console.WriteLine($"inLinkErr {i} is {inLinkErr[i]}");
            }

            if (outRecvErr[i] != 0)
            {
                Console.WriteLine($"outRecvErr {i} is {outRecvErr[i]}");
            }

            if (outCRCErr[i] != 0)
            {
                Console.WriteLine($"outCRCErr {i} is {outCRCErr[i]}");
            }

            if (outTransmitErr[i] != 0)
            {
                Console.WriteLine($"outTransmitErr {i} is {outTransmitErr[i]}");
            }

            if (outLinkErr[i] != 0)
            {
                Console.WriteLine($"outLinkErr {i} is {outLinkErr[i]}");
            }
        }
        Console.WriteLine("others has no err!");

        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }

        robot.CloseRPC();
    }

设置各轴速度前馈系数
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置各轴速度前馈系数
    * @param [in] radio 各轴速度前馈系数
    * @return 错误码
    */
    public int SetVelFeedForwardRatio(double radio[6]);

获取各轴速度前馈系数
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取各轴速度前馈系数
    * @param [out] radio 各轴速度前馈系数
    * @return 错误码
    */
    public int GetVelFeedForwardRatio(ref double radio[6]);

获取从站端口错误帧代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public void TestVelFeedForwardRatio()
    {

        double[] setRadio = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        robot.GetVelFeedForwardRatio(ref getRadio);
        Console.WriteLine($" {getRadio[0]:F6} {getRadio[1]:F6} {getRadio[2]:F6} {getRadio[3]:F6} {getRadio[4]:F6} {getRadio[5]:F6}");
    }

光电传感器TCP标定-计算工具RPY
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定-计算工具RPY
    * @param [in] Btool 机器人笛卡尔位置
    * @param [in] Etool 当前工具坐标系数值
    * @param [in] senser 当前传感器坐标系数值(暂未开放)
    * @param [in] radius 圆周运动半径mm(暂未开放)
    * @param [in] dz 沿基座标系z轴负方向运动距离；当dz = 10000时，函数直接返回工具RPY
    * @param [out] TCPRPY 工具RPY数值
    * @return 错误码
    */
    public int TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, out Rpy TCPRPY);

光电传感器TCP标定-计算工具XYZ
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定-计算工具XYZ
    * @param [in] select 0-计算工具TCP；1-计算传感器原点；2-计算传感器姿态；3-直接返回工具TCP；4-记录当前工件坐标系和工具坐标系
    * @param [in] originDirection 0-X方向；1-Y方向；2-Z方向
    * @param [in] pos1 机器人笛卡尔位置1
    * @param [in] pos2 机器人笛卡尔位置2
    * @param [in] pos3 机器人笛卡尔位置3
    * @param [in] pos4 机器人笛卡尔位置4
    * @param [out] TCP 工具XYZ数值
    * @return 错误码
    */
    public int TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2,DescTran pos3, DescTran pos4, out DescTran TCP);

光电传感器TCP标定-开始记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定-开始记录末端法兰中心位置
    * @return 错误码
    */
    errno_t TCPRecordFlangePosStart();

光电传感器TCP标定-停止记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定-停止记录末端法兰中心位置
    * @return 错误码
    */
    public int TCPRecordFlangePosEnd();

光电传感器TCP标定-获取末端工具中心点位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定-获取末端工具中心点位置
    * @param [out] TCP 工具中心点位置(x,y,z)
    * @return 错误码
    */
    public int TCPGetRecordFlangePos(out DescTran TCP);

光电传感器TCP标定
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光电传感器TCP标定
    * @param [in] luaPath 自动标定lua程序路径：QX版本机器人-"/fruser/FR_CalibrateTheToolTcp.lua";LA版本机器人-"/usr/local/etc/controller/lua/FR_CalibrateTheToolTcp.lua"
    * @param [in] offsetX 示教点偏移(x,y,z)mm
    * @param [out] TCP 标定后的工具坐标系(x,y,z,rx,ry,rz)
    * @return 错误码
    */
    public int PhotoelectricSensorTCPCalibration(string luaPath, DescTran offset, out DescPose TCP);

光电传感器TCP标定代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestPhotoelectricSensorTCPCalib()
    {
        ROBOT_STATE_PKG pkg =new ROBOT_STATE_PKG();
        DescTran offset = new DescTran( 10.0, 10.0, 3.0 );
        DescPose TCP = new DescPose();
        int rtn = robot.PhotoelectricSensorTCPCalibration("/fruser/FR_CalibrateTheToolTcp.lua", offset, out TCP);
        Console.WriteLine($"PhotoelectricSensorTCPCalibration : {rtn}");
        Console.WriteLine($"工具TCP坐标: X={TCP.tran.x:F3}, Y={TCP.tran.y:F3}, Z={TCP.tran.z:F3}");
        Console.WriteLine($"工具RPY姿态: RX={TCP.rpy.rx:F3}, RY={TCP.rpy.ry:F3}, RZ={TCP.rpy.rz:F3}");
    }
