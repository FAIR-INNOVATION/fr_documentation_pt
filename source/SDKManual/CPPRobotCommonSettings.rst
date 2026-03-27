机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工具参考点-六点法
     * @param [in] point_num 点编号,范围[1~6] 
     * @return 错误码
     */
    errno_t SetToolPoint(int point_num);

计算工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算工具坐标系
     * @param [out] tcp_pose 工具坐标系
     * @return 错误码
     */
    errno_t ComputeTool(DescPose *tcp_pose);

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工具参考点-四点法
     * @param [in] point_num 点编号,范围[1~4] 
     * @return 错误码
     */
    errno_t SetTcp4RefPoint(int point_num);

计算工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算工具坐标系
     * @param [out] tcp_pose 工具坐标系
     * @return 错误码
     */
    errno_t ComputeTcp4(DescPose *tcp_pose);

根据点位信息计算工具坐标系
+++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 根据点位信息计算工具坐标系
	 * @param [in] method 计算方法；0-四点法；1-六点法
	 * @param [in] pos 关节位置组，四点法时数组长度为4个，六点法时数组长度为6个
	 * @param [out] coord 工具坐标系结果
	 * @return 错误码
    */
	errno_t ComputeToolCoordWithPoints(int method, JointPos pos[], DescPose& coord);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  设置工具坐标系
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工具中心点相对于末端法兰中心位姿
	 * @param  [in] type  0-工具坐标系，1-传感器坐标系
	 * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
	 * @param  [in] toolID 工具ID
	 * @param  [in] loadNum 负载编号
	 * @return  错误码
	 */
	errno_t SetToolCoord(int id, DescPose *coord, int type, int install, int toolID, int loadNum);

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
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
	errno_t SetToolList(int id, DescPose *coord, int type, int install, int loadNum);

获取当前工具坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取当前工具坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐标系位姿
    * @return  错误码
    */
    errno_t  GetTCPOffset(uint8_t flag, DescPose *desc_pos);

机器人工具坐标系操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestTCPCompute(void)
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
         DescPose p1Desc(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
         JointPos p1Joint(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);
         DescPose p2Desc(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
         JointPos p2Joint(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);
         DescPose p3Desc(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
         JointPos p3Joint(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);
         DescPose p4Desc(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
         JointPos p4Joint(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);
         DescPose p5Desc(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
         JointPos p5Joint(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);
         DescPose p6Desc(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
         JointPos p6Joint(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         JointPos posJ[6] = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
         DescPose coordRtn = {};
         rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);
         printf("ComputeToolCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(3);
         robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(4);
         robot.MoveJ(&p5Joint, &p5Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(5);
         robot.MoveJ(&p6Joint, &p6Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetToolPoint(6);
         rtn = robot.ComputeTool(&coordRtn);
         printf("6 Point ComputeTool        %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetToolList(1, &coordRtn, 0, 0, 0);
         robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(3);
         robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetTcp4RefPoint(4);
         rtn = robot.ComputeTcp4(&coordRtn);
         printf("4 Point ComputeTool        %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetToolCoord(2, &coordRtn, 0, 0, 1, 0);
         DescPose getCoord = {};
         rtn = robot.GetTCPOffset(0, &getCoord);
         printf("GetTCPOffset    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.CloseRPC();
         return 0;
     }

设置外部工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置外部工具参考点-六点法
     * @param [in] point_num 点编号,范围[1~4] 
     * @return 错误码
     */
    errno_t SetExTCPPoint(int point_num);

计算外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算外部工具坐标系
     * @param [out] tcp_pose 外部工具坐标系
     * @return 错误码
     */
    errno_t ComputeExTCF(DescPose *tcp_pose);  

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  设置外部工具坐标系
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    errno_t  SetExToolCoord(int id, DescPose *etcp, DescPose *etool);

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    errno_t  SetExToolList(int id, DescPose *etcp, DescPose *etool);

机器人外部工具坐标系操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestExtCoord(void)
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
       DescPose p1Desc(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
       JointPos p1Joint(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);
       DescPose p2Desc(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
       JointPos p2Joint(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);
       DescPose p3Desc(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
       JointPos p3Joint(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);
       ExaxisPos exaxisPos(0, 0, 0, 0);
       DescPose offdese(0, 0, 0, 0, 0, 0);
       DescPose posTCP[3] = { p1Desc , p2Desc , p3Desc };
       DescPose coordRtn = {};
       robot.MoveJ(&p1Joint, &p1Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(1);
       robot.MoveJ(&p2Joint, &p2Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(2);
       robot.MoveJ(&p3Joint, &p3Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.SetExTCPPoint(3);
       rtn = robot.ComputeExTCF(&coordRtn);
       printf("ComputeExTCF          %d coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
       robot.SetExToolCoord(1, &coordRtn, &offdese);
       robot.SetExToolList(1, &coordRtn, &offdese);
       robot.CloseRPC();
       return 0;
    }

设置工件参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工件参考点-三点法
     * @param [in] point_num 点编号,范围[1~3] 
     * @return 错误码
     */
    errno_t SetWObjCoordPoint(int point_num);

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  计算工件坐标系
	 * @param [in] method 计算方法 0：原点-x轴-z轴  1：原点-x轴-xy平面
	 * @param [in] refFrame 参考坐标系
	 * @param [out] wobj_pose 工件坐标系
	 * @return 错误码
	 */
	errno_t ComputeWObjCoord(int method, int refFrame, DescPose *wobj_pose);

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  设置工件坐标系
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
	 * @param  [in] refFrame 参考坐标系
	 * @return  错误码
	 */
	errno_t SetWObjCoord(int id, DescPose *coord, int refFrame);

设置工件坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	 * @brief  设置工件坐标系列表
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
	 * @param  [in] refFrame 参考坐标系
	 * @return  错误码
	 */
	errno_t SetWObjList(int id, DescPose *coord, int refFrame);

根据点位信息计算工件坐标系
+++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 根据点位信息计算工件坐标系
	 * @param [in] method 计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
	 * @param [in] pos 三个TCP位置组
	 * @param [in] refFrame 参考坐标系
	 * @param [out] coord 工具坐标系结果
	 * @return 错误码
    */
	errno_t ComputeWObjCoordWithPoints(int method, DescPose pos[], int refFrame, DescPose& coord);

获取当前工件坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取当前工件坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件坐标系位姿
    * @return  错误码
    */   
    errno_t  GetWObjOffset(uint8_t flag, DescPose *desc_pos);

机器人工件坐标系操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestWobjCoord(void)
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
         DescPose p1Desc(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
         JointPos p1Joint(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);
         DescPose p2Desc(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
         JointPos p2Joint(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);
         DescPose p3Desc(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
         JointPos p3Joint(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         DescPose posTCP[3] = { p1Desc , p2Desc , p3Desc };
         DescPose coordRtn = {};
         rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);
         printf("ComputeWObjCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.MoveJ(&p1Joint, &p1Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(1);
         robot.MoveJ(&p2Joint, &p2Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(2);
         robot.MoveJ(&p3Joint, &p3Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.SetWObjCoordPoint(3);
         rtn = robot.ComputeWObjCoord(1, 0, &coordRtn);
         printf("ComputeWObjCoord                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.SetWObjCoord(1, &coordRtn, 0);
         robot.SetWObjList(1, &coordRtn, 0);
         DescPose getWobjDesc = {};
         rtn = robot.GetWObjOffset(0, &getWobjDesc);
         printf("GetWObjOffset                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
         robot.CloseRPC();
         return 0;
     }

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    errno_t  SetSpeed(int vel);

设置机器人加速度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

	/**
	 * @brief 设置机器人加速度
	 * @param [in] acc 机器人加速度百分比
	 * @return 错误码
	 */
	errno_t SetOaccScale(double acc);

获取机器人默认速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取机器人默认速度
    * @param  [out]  vel  速度，单位mm/s
    * @return  错误码
    */   
    errno_t  GetDefaultTransVel(float *vel);
    
设置末端负载重量
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief  设置末端负载重量
	 * @param  [in] loadNum 负载编号
	 * @param  [in] weight  负载重量，单位kg
	 * @return  错误码
    */
    errno_t SetLoadWeight(int loadNum = 0, float weight);

设置末端负载质心坐标
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端负载质心坐标
    * @param [in] loadNum 负载编号
    * @param [in] coord 质心坐标，单位mm
    * @return 错误码
    */
    errno_t SetLoadCoord(int loadNum, DescTran* coord);

获取当前负载的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取当前负载的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 负载重量，单位kg
    * @return  错误码
    */
    errno_t  GetTargetPayload(uint8_t flag, float *weight);

获取当前负载的质心
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取当前负载的质心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 负载质心，单位mm
    * @return  错误码
    */   
    errno_t  GetTargetPayloadCog(uint8_t flag, DescTran *cog);

设置机器人安装方式
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in] install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    errno_t  SetRobotInstallPos(uint8_t install);   

设置机器人安装角度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    errno_t  SetRobotInstallAngle(double yangle, double zangle);

获取机器人安装角度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取机器人安装角度
    * @param  [out] yangle 倾斜角
    * @param  [out] zangle 旋转角
    * @return  错误码
    */
    errno_t  GetRobotInstallAngle(float *yangle, float *zangle);

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    errno_t  SetSysVarValue(int id, float value);

获取系统变量值
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取系统变量值
    * @param  [in] id 系统变量编号，范围[1~20]
    * @param  [out] value  系统变量值
    * @return  错误码
    */
    errno_t  GetSysVarValue(int id, float *value);

机器人常用设置代码示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestLoadInstall(void)
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
         for (int i = 1; i < 100; i++)
         {
             robot.SetSpeed(i);
             robot.SetOaccScale(i);
             robot.Sleep(30);
         }
         float defaultVel = 0.0;
         robot.GetDefaultTransVel(&defaultVel);
         printf("GetDefaultTransVel is %f\n", defaultVel);
         for (int i = 1; i < 21; i++)
         {
             robot.SetSysVarValue(i, i + 0.5);
             robot.Sleep(100);
         }
         for (int i = 1; i < 21; i++)
         {
             float value = 0;
             robot.GetSysVarValue(i, &value);
             printf("sys value  %d is :%f\n", i, value);
             robot.Sleep(100);
         }
         robot.SetLoadWeight(0, 2.5);
         DescTran loadCoord = {};
         loadCoord.x = 3.0;
         loadCoord.y = 4.0;
         loadCoord.z = 5.0;
         robot.SetLoadCoord(&loadCoord);
         robot.Sleep(1000);
         float getLoad = 0.0;
         robot.GetTargetPayload(0, &getLoad);
         DescTran getLoadTran = {};
         robot.GetTargetPayloadCog(0, &getLoadTran);
         printf("get load is %f; get load cog is %f %f %f\n", getLoad, getLoadTran.x, getLoadTran.y, getLoadTran.z);
         robot.SetRobotInstallPos(0);
         robot.SetRobotInstallAngle(15.0, 25.0);
         float anglex = 0.0;
         float angley = 0.0;
         robot.GetRobotInstallAngle(&anglex, &angley);
         printf("GetRobotInstallAngle x:  %f;  y:  %f\n", anglex, angley);
         robot.CloseRPC();
         return 0;
     }

关节摩擦力补偿开关
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  关节摩擦力补偿开关
    * @param  [in]  state  0-关，1-开
    * @return  错误码
    */
    errno_t  FrictionCompensationOnOff(uint8_t state);

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-正装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    errno_t  SetFrictionValue_level(float coeff[6]);

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-侧装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    errno_t  SetFrictionValue_wall(float coeff[6]);

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-倒装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    errno_t  SetFrictionValue_ceiling(float coeff[6]);

设置关节摩擦力补偿系数-自由安装
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-自由安装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    errno_t  SetFrictionValue_freedom(float coeff[6]);

机器人设置关节摩擦力补偿代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFriction(void)
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
       float lcoeff[6] = { 0.9,0.9,0.9,0.9,0.9,0.9 };
       float wcoeff[6] = { 0.4,0.4,0.4,0.4,0.4,0.4 };
       float ccoeff[6] = { 0.6,0.6,0.6,0.6,0.6,0.6 };
       float fcoeff[6] = { 0.5,0.5,0.5,0.5,0.5,0.5 };
       rtn = robot.FrictionCompensationOnOff(1);
       printf("FrictionCompensationOnOff rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_level(lcoeff);
       printf("SetFrictionValue_level rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_wall(wcoeff);
       printf("SetFrictionValue_wall rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_ceiling(ccoeff);
       printf("SetFrictionValue_ceiling rtn is %d\n", rtn);
       rtn = robot.SetFrictionValue_freedom(fcoeff);
       printf("SetFrictionValue_freedom rtn is %d\n", rtn);
       robot.CloseRPC();
       return 0;
    }

查询机器人错误码
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查询机器人错误码
     * @param  [out]  maincode  主错误码
     * @param  [out]  subcode   子错误码
     * @return  错误码
     */ 
    errno_t  GetRobotErrorCode(int *maincode, int *subcode);

错误状态清除
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  错误状态清除
    * @return  错误码
    */
    errno_t  ResetAllError();

机器人故障状态获取及清除错误代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGetError(void)
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
       int maincode, subcode;
       robot.GetRobotErrorCode(&maincode, &subcode);
       printf("robot maincode is %d; subcode is %d\n", maincode, subcode);
       robot.ResetAllError();
       robot.Sleep(1000);
       robot.GetRobotErrorCode(&maincode, &subcode);
       printf("robot maincode is %d; subcode is %d\n", maincode, subcode);
       robot.CloseRPC();
       return 0;
    }

设置宽电压控制箱温度及风扇电流监控参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置宽电压控制箱温度及风扇电流监控参数
    * @param [in] enable 0-不使能监测；1-使能监测
    * @param [in] period 监测周期(s),范围1-100
    * @return 错误码
    */
    errno_t SetWideBoxTempFanMonitorParam(int enable, int period);
    
获取宽电压控制箱温度及风扇电流监控参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取宽电压控制箱温度及风扇电流监控参数
    * @param [out] enable 0-不使能监测；1-使能监测
    * @param [out] period 监测周期(s),范围1-100
    * @return 错误码
    */
    errno_t GetWideBoxTempFanMonitorParam(int &enable, int &period);
    
宽电压控制箱温度和风扇电流状态获取代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestWideVoltageCtrlBoxtemp(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         printf("robot rpc rtn is %d\n", rtn);
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         robot.SetWideBoxTempFanMonitorParam(1, 2);
         int enable = 0;
         int period = 0;
         robot.GetWideBoxTempFanMonitorParam(enable, period);
         printf("GetWideBoxTempFanMonitorParam enable is %d   period is %d\n", enable, period);
         for (int i = 0; i < 100; i++)
         {
             robot.GetRobotRealTimeState(&pkg);
             printf("robot ctrl box temp is %f,  fan current is %d\n", pkg.wideVoltageCtrlBoxTemp, pkg.wideVoltageCtrlBoxFanCurrent);
             robot.Sleep(100);
         }
         rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
         printf("SetWideBoxTempFanMonitorParam rtn is %d\n", rtn);
         enable = 0;
         period = 0;
         robot.GetWideBoxTempFanMonitorParam(enable, period);
         printf("GetWideBoxTempFanMonitorParam enable is %d   period is %d\n", enable, period);
         for (int i = 0; i < 100; i++)
         {
             robot.GetRobotRealTimeState(&pkg);
             printf("robot ctrl box temp is %f,  fan current is %d\n", pkg.wideVoltageCtrlBoxTemp, pkg.wideVoltageCtrlBoxFanCurrent);
             robot.Sleep(100);
         }
         robot.CloseRPC();
         robot.Sleep(2000);
         return 0;
     }
         
计算焦点标定结果
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 计算焦点标定结果
    * @param [in] pointNum 标定点个数
    * @param [out] resultPos 标定结果XYZ
    * @param [out] accuracy 标定精度误差
    * @return 错误码
    */
    errno_t ComputeFocusCalib(int pointNum, DescTran& resultPos, float& accuracy);
         
设置焦点坐标
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焦点坐标
    * @param [in] pos 焦点坐标XYZ
    * @return 错误码
    */
    errno_t SetFocusPosition(DescTran pos);
         
开启焦点跟随
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
    errno_t FocusStart(double kp, double kpredict, double aMax, double vMax, int type);
         
停止焦点跟随
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 停止焦点跟随
    * @return 错误码
    */
    errno_t FocusEnd();

机器人焦点跟随代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestFocus()
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
      DescPose p1Desc(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
      JointPos p1Joint(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);
      DescPose p2Desc(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
      JointPos p2Joint(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);
      DescPose p3Desc(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
      JointPos p3Joint(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);
      DescPose p4Desc(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
      JointPos p4Joint(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);
      DescPose p5Desc(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
      JointPos p5Joint(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);
      DescPose p6Desc(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
      JointPos p6Joint(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 100, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(1);
      robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(2);
      robot.MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(3);
      robot.MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.SetTcp4RefPoint(4);
      DescPose coordRtn = {};
      rtn = robot.ComputeTcp4(&coordRtn);
      printf("4 Point ComputeTool    %d coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
      robot.SetToolCoord(1, &coordRtn, 0, 0, 1, 0);
      robot.GetForwardKin(&p1Joint, &p1Desc);
      robot.GetForwardKin(&p2Joint, &p2Desc);
      robot.GetForwardKin(&p3Joint, &p3Desc);
      robot.SetFocusCalibPoint(1, p1Desc);
      robot.SetFocusCalibPoint(2, p2Desc);
      robot.SetFocusCalibPoint(3, p3Desc);
      DescTran resultPos = {};
      float accuracy = 0.0;
      rtn = robot.ComputeFocusCalib(3, resultPos, accuracy);
      printf("ComputeFocusCalib coord is %d %f %f %f accuracy is %f\n", rtn, resultPos.x, resultPos.y, resultPos.z, accuracy);
      rtn = robot.SetFocusPosition(resultPos);
      robot.GetForwardKin(&p5Joint, &p5Desc);
      robot.GetForwardKin(&p6Joint, &p6Desc);
      robot.MoveL(&p5Joint, &p5Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.MoveL(&p6Joint, &p6Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.FocusStart(50, 19, 710, 90, 0);
      robot.MoveL(&p5Joint, &p5Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.MoveL(&p6Joint, &p6Desc, 1, 0, 10, 100, 100, -1, 0, &exaxisPos, 0, 1, &offdese);
      robot.FocusEnd();
      robot.CloseRPC();
      return 0;
    }

关节扭矩传感器灵敏度标定功能开启
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度标定功能开启
    * @param [in] status 0-关闭；1-开启
    * @return  错误码
    */
    errno_t JointSensitivityEnable(int status);

关节扭矩传感器灵敏度数据采集
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩传感器灵敏度数据采集
    * @return 错误码
    */
    errno_t JointSensitivityCollect();
    

获取关节扭矩传感器灵敏度标定结果
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取关节扭矩传感器灵敏度标定结果
    * @param [out] calibResult j1~j6关节灵敏度[0-1]
    * @param [out] linearityn j1~j6关节线性度[0-1]
    * @return 错误码
    */
    errno_t JointSensitivityCalibration(double calibResult[6], double linearity[6]);

获取关节扭矩传感器迟滞误差
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取关节扭矩传感器迟滞误差
    * @param [out] hysteresisError j1~j6关节迟滞误差
    * @return 错误码
    */
    errno_t JointHysteresisError(double hysteresisError[6]);
    
获取关节扭矩传感器重复精度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @brief 获取关节扭矩传感器重复精度
    * @param [out] repeatability j1~j6关节扭矩传感器重复精度
    * @return 错误码
    */
    errno_t JointRepeatability(double repeatability[6]);
    
设置关节力传感器参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
    errno_t SetAdmittanceParams(double M[6], double B[6], double K[6], double threshold[6], double sensitivity[6], int setZeroFlag);

关节扭矩传感器灵敏度自动标定代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSensitivityCalib()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 30000, 500);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return 0;
        }
        rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        printf("JointSensitivityEnable rtn is %d\n", rtn);
        JointPos curJPos = {};
        robot.GetActualJointPosDegree(0, &curJPos);
        ExaxisPos epos = { 0,0,0,0 };
        DescPose offset_pos = { 0,0,0,0,0,0 };
        JointPos jointPos1 = { curJPos.jPos[0], 0, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos1 = {};
        robot.GetForwardKin(&jointPos1, &descPos1);
        robot.MoveJ(&jointPos1, &descPos1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 1 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos2 = { curJPos.jPos[0], -30, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos2 = {};
        robot.GetForwardKin(&jointPos2, &descPos2);
        robot.MoveJ(&jointPos2, &descPos2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 2 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos3 = { curJPos.jPos[0], -60, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos3 = {};
        robot.GetForwardKin(&jointPos3, &descPos3);
        robot.MoveJ(&jointPos3, &descPos3, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 3 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos4 = { curJPos.jPos[0], -90, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos4 = {};
        robot.GetForwardKin(&jointPos4, &descPos4);
        robot.MoveJ(&jointPos4, &descPos4, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 4 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos5 = { curJPos.jPos[0], -120, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos5 = {};
        robot.GetForwardKin(&jointPos5, &descPos5);
        robot.MoveJ(&jointPos5, &descPos5, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 5 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos6 = { curJPos.jPos[0], -150, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos6 = {};
        robot.GetForwardKin(&jointPos6, &descPos6);
        robot.MoveJ(&jointPos6, &descPos6, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 6 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos7 = { curJPos.jPos[0], -180, 0, -90, 0.02, curJPos.jPos[5] };
        DescPose descPos7 = {};
        robot.GetForwardKin(&jointPos7, &descPos7);
        robot.MoveJ(&jointPos7, &descPos7, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 7 rtn is %d\n", rtn);
        robot.Sleep(100);
        //-------------------
        robot.MoveJ(&jointPos6, &descPos6, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 8 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos5, &descPos5, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 9 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos4, &descPos4, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 10 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos3, &descPos3, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 11 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos2, &descPos2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 12 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(&jointPos1, &descPos1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        printf("JointSensitivityCollect 13 rtn is %d\n", rtn);
        robot.Sleep(100);
        double calibResult[6] = { 0.0 };
        double linearity[6] = { 0.0 };
        rtn = robot.JointSensitivityCalibration(calibResult, linearity);
        printf("JointSensitivityCalibration rtn is %d\n", rtn);
        rtn = robot.JointSensitivityEnable(0);
        printf("JointSensitivityEnable rtn is %d\n", rtn);
        printf("jointSensor Calib result is %f %f %f %f %f %f\njointSensor linearity is %f %f %f %f %f %f\n", 
            calibResult[0], calibResult[1], calibResult[2], 
            calibResult[3], calibResult[4], calibResult[5], 
            linearity[0], linearity[1], linearity[2],
            linearity[3], linearity[4], linearity[5]);
        double hysteresisError[6] = { 0.0 };
        rtn = robot.JointHysteresisError(hysteresisError);
        printf("JointHysteresisError result is %f %f %f %f %f %f\n",
            hysteresisError[0], hysteresisError[1], hysteresisError[2],
            hysteresisError[3], hysteresisError[4], hysteresisError[5]);
        double repeatability[6] = { 0.0 };
        rtn = robot.JointRepeatability(repeatability);
        printf("JointRepeatability result is %f %f %f %f %f %f\n",
            repeatability[0], repeatability[1], repeatability[2],
            repeatability[3], repeatability[4], repeatability[5]);
        double M[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double B[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double K[6] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double threshold[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        printf("SetAdmittanceParams rtn is %d\n", rtn);
        robot.CloseRPC();
    }
    
获取机器人8个从站端口错误帧数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
    errno_t GetSlavePortErrCounter(int inRecvErr[8], int inCRCErr[8], int inTransmitErr[8], int inLinkErr[8], int outRecvErr[8], int outCRCErr[8], int outTransmitErr[8], int outLinkErr[8]);

从站端口错误帧清零
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 从站端口错误帧清零
    * @param [in] slaveID 从站编号0~7
    * @return 错误码
    */
    errno_t SlavePortErrCounterClear(int slaveID);
    
获取从站端口错误帧代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSlavePortErr()
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
        int inRecvErr[8] = {0.0}; 
        int inCRCErr[8] = { 0.0 };
        int inTransmitErr[8] = { 0.0 };
        int inLinkErr[8] = { 0.0 };
        int outRecvErr[8] = { 0.0 };
        int outCRCErr[8] = { 0.0 };
        int outTransmitErr[8] = { 0.0 };
        int outLinkErr[8] = { 0.0 };
        robot.GetSlavePortErrCounter(inRecvErr,  inCRCErr, inTransmitErr, inLinkErr,
            outRecvErr, outCRCErr, outTransmitErr, outLinkErr);
        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inRecvErr[i]);
            }
            if (inCRCErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inCRCErr[i]);
            }
            if (inTransmitErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inTransmitErr[i]);
            }
            if (inLinkErr[i] != 0)
            {
                printf("inRecvErr %d is %d\n", i, inLinkErr[i]);
            }
            if (outRecvErr[i] != 0)
            {
                printf("outRecvErr %d is %d\n", i, outRecvErr[i]);
            }
            if (outCRCErr[i] != 0)
            {
                printf("outCRCErr %d is %d\n", i, outCRCErr[i]);
            }
            if (outTransmitErr[i] != 0)
            {
                printf("outTransmitErr %d is %d\n", i, outTransmitErr[i]);
            }
            if (outLinkErr[i] != 0)
            {
                printf("outLinkErr %d is %d\n", i, outLinkErr[i]);
            }
        }
        printf("others has no err!\n");
        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }
        robot.CloseRPC();
        return 0;
    }

设置各轴速度前馈系数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置各轴速度前馈系数
    * @param [in] radio 各轴速度前馈系数
    * @return 错误码
    */
    errno_t SetVelFeedForwardRatio(double radio[6]);

获取各轴速度前馈系数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取各轴速度前馈系数
    * @param [out] radio 各轴速度前馈系数
    * @return 错误码
    */
    errno_t GetVelFeedForwardRatio(double radio[6]);

机器人速度前馈系数代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestVelFeedForwardRatio()
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
        double setRadio[6] = { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double getRadio[6] = { 0.0 };
        robot.GetVelFeedForwardRatio(getRadio);
        printf(" %f %f %f %f %f %f\n", getRadio[0], getRadio[1], getRadio[2], getRadio[3], getRadio[4], getRadio[5]);
        robot.CloseRPC();
        return 0;
    }

光电传感器TCP标定-计算工具RPY
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
    errno_t TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, Rpy& TCPRPY);

光电传感器TCP标定-计算工具XYZ
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
    errno_t TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2, DescTran pos3, DescTran pos4, DescTran& TCP);

光电传感器TCP标定-开始记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 光电传感器TCP标定-开始记录末端法兰中心位置
    * @return 错误码
    */
    errno_t TCPRecordFlangePosStart();

光电传感器TCP标定-停止记录末端法兰中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 光电传感器TCP标定-停止记录末端法兰中心位置
    * @return 错误码
    */
    errno_t TCPRecordFlangePosEnd();

光电传感器TCP标定-获取末端工具中心点位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 光电传感器TCP标定-获取末端工具中心点位置
    * @param [out] TCP 工具中心点位置(x,y,z)
    * @return 错误码
    */
    errno_t TCPGetRecordFlangePos(DescTran& TCP);

光电传感器TCP标定
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 光电传感器TCP标定
    * @param [in] luaPath 自动标定lua程序路径：QX版本机器人-"/fruser/FR_CalibrateTheToolTcp.lua";LA版本机器人-"/usr/local/etc/controller/lua/FR_CalibrateTheToolTcp.lua"
    * @param [in] offsetX 示教点偏移(x,y,z)mm
    * @param [out] TCP 标定后的工具坐标系(x,y,z,rx,ry,rz)
    * @return 错误码
    */
    errno_t PhotoelectricSensorTCPCalibration(std::string luaPath, DescTran offset, DescPose& TCP);

光电传感器TCP标定代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestPhotoelectricSensorTCPCalib(void)
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
        DescTran offset = { 10.0, 10.0, 3.0 };
        DescPose TCP = {};
        rtn = robot.PhotoelectricSensorTCPCalibration("/fruser/FR_CalibrateTheToolTcp.lua", offset, TCP);
        printf("PhotoelectricSensorTCPCalibration rtn is  %d %f %f %f %f %f %f \n", rtn, TCP.tran.x, TCP.tran.y, TCP.tran.z, TCP.rpy.rx, TCP.rpy.ry, TCP.rpy.rz);
        robot.CloseRPC();
        robot.Sleep(9999999);
        return 0;
    }