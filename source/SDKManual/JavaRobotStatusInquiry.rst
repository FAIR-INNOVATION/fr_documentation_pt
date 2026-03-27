机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取当前关节位置(角度)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前关节位置(角度)
    * @param  [out] jPos 获取的六个关节位置，单位deg
    * @return  错误码
    */
    int GetActualJointPosDegree(JointPos jPos); 

获取关节反馈速度-deg/s
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取关节反馈速度-deg/s 
    * @param [out] speed 六个关节速度
    * @return 错误码 
    */
    int GetActualJointSpeedsDegree(Object[] speed);

获取关节反馈加速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取关节反馈加速度-deg/s^2
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] acc 六个关节加速度
    * @return  错误码
    */
    public int GetActualJointAccDegree(int flag, Object[] acc)

获取TCP指令合速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取TCP指令速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] tcp_speed 线性速度
    * @param  [out] ori_speed 姿态速度
    * @return  错误码
    */
    public int GetTargetTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

获取TCP反馈合速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取TCP反馈合速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] tcp_speed 线性速度
    * @param  [out] ori_speed 姿态速度
    * @return  错误码
    */
    public int GetActualTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

获取TCP指令速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取TCP指令速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] speed [x,y,z,rx,ry,rz]速度
    * @return  错误码
    */
    public int GetTargetTCPSpeed(int flag, Object[] speed)

获取TCP反馈速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取TCP反馈速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] speed [x,y,z,rx,ry,rz]速度
    * @return  错误码
    */
    public int GetActualTCPSpeed(int flag, Object[] speed)

获取当前工具位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工具位姿
    * @param  [out] desc_pos  工具位姿
    * @return  错误码
    */
    int GetActualTCPPose(DescPose desc_pos); 

获取当前工具坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工具坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具坐标系编号
    * @return  错误码
    */
    int GetActualTCPNum(int flag, int[] id)

获取当前工件坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工件坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件坐标系编号
    * @return  错误码
    */
    public int GetActualWObjNum(int flag, int[] id)

获取当前末端法兰位姿
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前末端法兰位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法兰位姿
    * @return  错误码
    */
    public int GetActualToolFlangePose(int flag, DescPose desc_pos)

获取当前关节转矩
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取当前关节转矩
    * @param  [in]  flag 0-阻塞，1-非阻塞
    * @param  [out]  torques 关节转矩
    * @return  错误码
    */
    int GetJointTorques(int flag, Object[] torques);

获取系统时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取系统时间
    * @return  List[0]:int 错误码; List[1]:double t_ms 单位ms
    */
    List<Number> GetSystemClock();

查询机器人运动是否完成
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查询机器人运动是否完成
    * @param   [out] state  0-未完成，1-完成
    * @return  错误码
    */
    public int GetRobotMotionDone(int[] state)

查询机器人运动队列缓存长度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查询机器人运动队列缓存长度
    * @param   [out] len  缓存长度
    * @return  错误码
    */
    public int GetMotionQueueLength(int[] len)

获取机器人急停状态
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人急停状态
    * @param [out] state 急停状态，0-非急停，1-急停
    * @return 错误码
    */
    public int GetRobotEmergencyStopState(int[] state)

获取SDK与机器人的通讯状态
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取SDK与机器人的通讯状态
    * @return state 通讯状态，0-通讯正常，1-通讯异常
    */
    public int GetSDKComState()

获取安全停止信号
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取安全停止信号
    * @param  [out] si0_state 安全停止信号SI0，0-无效，1-有效
    * @param  [out] si1_state 安全停止信号SI1，0-无效，1-有效
    * @return 错误码
    */
    public int GetSafetyStopState(int[] si0_state, int[] si1_state)

获取机器人关节驱动器温度(℃)
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人关节驱动器温度(℃)
    * @param  [out] temperature 温度
    * @return 错误码
    */
    public int GetJointDriverTemperature(double[] temperature)

获取机器人关节驱动器扭矩(Nm)
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人关节驱动器扭矩(Nm)
    * @param  [out] torque 扭矩
    * @return 错误码
    */
    public int GetJointDriverTorque(double[] torque)

获取机器人实时状态结构体
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人实时状态结构体
    * @return 实时状态结构体
    */
    public ROBOT_STATE_PKG GetRobotRealTimeState()

机器人状态查询代码示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetStatus(Robot robot)
    {
        List<Number> angle=new ArrayList<>();
        angle=robot.GetRobotInstallAngle();
        System.out.println("yangle:"+angle.get(1)+",zangle:"+angle.get(2));

        JointPos j_deg =new JointPos(){};
        robot.GetActualJointPosDegree( j_deg);

        Object[] jointSpeed =new Object[] { 0,0,0,0,0,0 };
        robot.GetActualJointSpeedsDegree(jointSpeed);

        Object[] jointAcc = new Object[]{0,0,0,0,0,0 };
        robot.GetActualJointAccDegree(0, jointAcc);

        double tcp_speed = 0.0;
        double ori_speed = 0.0;
        robot.GetTargetTCPCompositeSpeed(0, tcp_speed, ori_speed);

        robot.GetActualTCPCompositeSpeed(0, tcp_speed, ori_speed);

        Object[] targetSpeed =new Object[] { 0,0,0,0,0,0 };
        robot.GetTargetTCPSpeed(0, targetSpeed);

        Object[] actualSpeed =new Object[] {0,0,0,0,0,0 };
        robot.GetActualTCPSpeed(0, actualSpeed);

        DescPose tcp = new DescPose(){};
        robot.GetActualTCPPose(tcp);

        DescPose flange = new DescPose(){};
        robot.GetActualToolFlangePose(0, flange);

        int[] id = {};
        robot.GetActualTCPNum(0, id);

        robot.GetActualWObjNum(0, id);

        List<Number> jtorque=new ArrayList<>();
        jtorque=robot.GetJointTorques(0);

        List<Number> t_ms = new ArrayList<>();
        t_ms=robot.GetSystemClock();

        List<Integer> config = new ArrayList<>();
        config=robot.GetRobotCurJointsConfig();

        int motionDone = 0;
        robot.GetRobotMotionDone(motionDone);

        int[] len ={0 };
        robot.GetMotionQueueLength(len);

        int[] emergState = {0};
        robot.GetRobotEmergencyStopState(emergState);

        int comstate = 0;
        comstate=robot.GetSDKComState();

        int[] si0_state=new int[]{0}, si1_state=new int[]{0};
        robot.GetSafetyStopState(si0_state, si1_state);

        double[] temp =new double[] { 0,0,0,0,0,0 };
        robot.GetJointDriverTemperature(temp);

        double[] torque = new double[]{ 0,0,0,0,0,0 };
        robot.GetJointDriverTorque(torque);

        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        pkg=robot.GetRobotRealTimeState();

        return 0;
    }

逆运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] config 关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, JointPos joint_pos);

逆运动学求解(参考位置)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置求解
    * @param  [in] posMode 0绝对位姿， 1相对位姿-基坐标系   2相对位姿-工具坐标系
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, JointPos joint_pos); 

逆运动学求解，笛卡尔空间包含扩展轴位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 逆运动学求解，笛卡尔空间包含扩展轴位置
    * @param  type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  desc_pos 笛卡尔位姿
    * @param  exaxis 扩展轴位置
    * @param  tool 工具号
    * @param  workPiece 工件号
    * @param  joint_pos 关节位置
    * @return 错误码
    */
    public int GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, JointPos joint_pos)
    
逆运动学求解包含扩展轴位置代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void  TestInverseKinExaxis(Robot robot)
    {
        DescPose desc=new DescPose(99.957, -0.002, 29.994, -176.569, -6.757, -167.462);
        ExaxisPos exaxis=new ExaxisPos(100.0, 0.0, 0.0, 0.0);
        JointPos jointPos =new JointPos();
        DescPose offsetPos =new DescPose();
        ROBOT_STATE_PKG pkg=robot.GetRobotRealTimeState();
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;
        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, jointPos);
        System.out.printf("GetInverseKinExaxis joint is %f, %f, %f, %f, %f, %f\n", jointPos.J1, jointPos.J2, jointPos.J3, jointPos.J4, jointPos.J5, jointPos.J6);
        robot.ExtAxisMove(exaxis, 100, -1);
        robot.MoveJ(jointPos, desc, toolnum, workPcsNum, 100.0, 100.0, 100.0, exaxis, -1, 0, offsetPos);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }

获取逆运动学是否有解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置判断是否有解
    * @param  [in] posMode 0绝对位姿， 1相对位姿-基坐标系   2相对位姿-工具坐标系
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @return  错误码  List[0]:错误码; List[1]: int hasResult 0-无解，1-有解
    */   
    List<Integer> GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref);  

正运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  正运动学求解
    * @param  [in] joint_pos 关节位置
    * @param  [out] desc_pos 笛卡尔位姿
    * @return  错误码
    */
    int GetForwardKin(JointPos joint_pos, DescPose desc_pos); 

机器人正逆运动学计算代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestInverseKin(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        JointPos inverseRtn = new JointPos(){};

        robot.GetInverseKin(0, desc_pos1, -1, inverseRtn);
        robot.GetInverseKinRef(0, desc_pos1, j1, inverseRtn);

        int hasResut = 0;
        robot.GetInverseKinHasSolution(0, desc_pos1, j1);

        DescPose forwordResult = new DescPose(){};
        robot.GetForwardKin(j1, forwordResult);

        return 0;
    }

查询机器人示教管理点数据
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 查询机器人示教管理点位数据 
    * @param [in]  name  点位名
    * @return  List[0]:错误码; List[1] - List[20] : 点位数据double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4} 
    */ 
    List<Number> GetRobotTeachingPoint(String name); 

获取机器人DH参数补偿值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取机器人DH参数补偿值
    * @param dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码
    */
    public int GetDHCompensation(Object[] dhCompensation)

获取控制箱SN码
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 获取控制箱SN码
    * @param [out] SNCode 控制箱SN码
    * @return 错误码
    */
    int GetRobotSN(String[] SNCode);

查询机器人示教管理点位数据代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetTeachPoint(Robot robot)
    {
        String name = "P1";
        List<Number> data=new ArrayList<>();
        data = robot.GetRobotTeachingPoint(name);
        System.out.println(name+" name is: "+data.get(0));
        for (int i = 0; i < 20; i++)
        {
            System.out.println("data is: "+ data.get(i+1));
        }

        int[] que_len = {0};
        int rtn = robot.GetMotionQueueLength(que_len);
        System.out.println("GetMotionQueueLength rtn is:"+rtn+", queue length is:"+ que_len[0]);

        Object[] dh = new Object[]{ 0,0,0,0,0,0 };
        int retval = 0;
        retval = robot.GetDHCompensation(dh);
        System.out.println("retval is: "+retval);

        String[] SN = new String[]{""};
        robot.GetRobotSN(SN);
        System.out.println("robot SN is "+SN[0]);
        return 0;
    }

根据编号获取工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief 根据编号获取工具坐标系
    * @param [in] id 工具坐标系编号
    * @param [out] coord 坐标系数值
    * @return 错误码
    */
    int GetToolCoordWithID(int id, DescPose coord)

根据编号获取工件坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief 根据编号获取工件坐标系
    * @param [in]  id 工件坐标系编号
    * @param [out] coord 坐标系数值
    * @return 错误码
    */
    public int GetWObjCoordWithID(int id, DescPose coord)

根据编号获取外部工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief 根据编号获取外部工具坐标系
    * @param [in]  id 外部工具坐标系编号
    * @param [out] coord 坐标系数值
    * @return 错误码
    */
    public int GetExToolCoordWithID(int id, DescPose coord)

根据编号获取扩展轴坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
    * @brief 根据编号获取扩展轴坐标系
    * @param [in]  id 外部工具坐标系编号
    * @param [out] coord 坐标系数值
    * @return 错误码
    */
    public int GetExAxisCoordWithID(int id, DescPose coord)

获取当前工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前工具坐标系
     * @param [out] coord 坐标系数值
     * @return 错误码
     */
    public int GetCurToolCoord(DescPose coord)

获取当前工件坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前工件坐标系
     * @param [out] coord 坐标系数值
     * @return 错误码
     */
    public int GetCurWObjCoord(DescPose coord)

获取当前外部工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前外部工具坐标系
     * @param  [out] coord 坐标系数值
     * @return 错误码
     */
    public int GetCurExToolCoord(DescPose coord)

获取当前扩展轴坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前扩展轴坐标系
     * @param [out] coord 坐标系数值
     * @return 错误码
     */
    public int GetCurExAxisCoord(DescPose coord)

获取机器人坐标系及负载代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestCoord(Robot robot)
    {
        int id = 1;
        int rtn = 0;
        DescPose toolCoord = new DescPose();
        DescPose extoolCoord = new DescPose();
        DescPose wobjCoord = new DescPose();
        DescPose exAxisCoord = new DescPose();


        robot.GetCurToolCoord(toolCoord);//工具
        System.out.println("GetToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);


        robot.GetCurWObjCoord(toolCoord);//工件
        System.out.println("GetCurWObjCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetCurExToolCoord(toolCoord);//外部工具
        System.out.println("GetCurExToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);


        robot.GetCurExAxisCoord(toolCoord);//扩展轴
        System.out.println("GetCurExToolCoord:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);


        List<Number> weightT = new ArrayList<>();//质心
        DescTran cogT=new DescTran();
        weightT=robot.GetTargetPayload(0);
        robot.GetTargetPayloadCog(0,cogT);
        System.out.println("GetTargetPayload :"+weightT.get(1).doubleValue()+", "+
                cogT.x+", "+cogT.y+", "+cogT.z);


        robot.GetToolCoordWithID(id, toolCoord);
        System.out.println("GetToolCoordWithID:"+id+","+
                toolCoord.tran.x+","+ toolCoord.tran.y+","+ toolCoord.tran.z+","+
                toolCoord.rpy.rx+","+ toolCoord.rpy.ry+","+ toolCoord.rpy.rz);

        robot.GetWObjCoordWithID(id, wobjCoord);
        System.out.println("GetWObjCoordWithID "+id+", "+
                wobjCoord.tran.x+","+ wobjCoord.tran.y+","+ wobjCoord.tran.z+","+
                wobjCoord.rpy.rx+","+ wobjCoord.rpy.ry+","+ wobjCoord.rpy.rz);


        robot.GetExToolCoordWithID(id, extoolCoord);//外部工具
        System.out.println("GetExToolCoordWithID :"+ id+","+
                extoolCoord.tran.x+","+ extoolCoord.tran.y+","+ extoolCoord.tran.z+","+
                extoolCoord.rpy.rx+","+ extoolCoord.rpy.ry+","+ extoolCoord.rpy.rz);

        robot.GetExAxisCoordWithID(id, exAxisCoord);//扩展轴
        System.out.println("GetExAxisCoordWithID "+id+","+
                exAxisCoord.tran.x+","+ exAxisCoord.tran.y+","+ exAxisCoord.tran.z+","+
                exAxisCoord.rpy.rx+","+ exAxisCoord.rpy.ry+","+ exAxisCoord.rpy.rz);


        double[] weight = new double[1];//负载质心
        DescTran getCog = new DescTran();
        robot.GetTargetPayloadWithID(id, weight, getCog);
        System.out.println("GetTargetPayloadWithID :"+ id+","+ weight[0]+","+
                getCog.x+","+ getCog.y+","+ getCog.z);

        DescPose coordSet0 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose coordSet = new DescPose(1, 2, 3, 4, 5, 6);
        DescPose etcp = new DescPose(10, 20, 30, 40, 50, 60);
        DescPose etool = new DescPose(0.1, 0.2, 0.3, 0.4, 0.5, 0.6);
        DescTran cog = new DescTran(1, 2, 3);

        robot.SetToolCoord(id, coordSet, 0, 0, 1, 0);
        robot.Sleep(100);
        robot.SetWObjCoord(id, coordSet, 0);
        robot.Sleep(100);
        robot.ExtAxisActiveECoordSys(id, 1, coordSet, 1); //将标定结果应用到扩展轴坐标系
        robot.Sleep(100);
        rtn = robot.SetExToolCoord(id, etcp, etool);
        robot.Sleep(100);
        rtn = robot.SetLoadWeight(id, 1.5);
        robot.Sleep(500);
        rtn = robot.SetLoadCoord(id, cog);
        robot.Sleep(100);
    }