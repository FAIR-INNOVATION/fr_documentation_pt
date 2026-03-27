机器人运动
============

.. toctree:: 
    :maxdepth: 5


jog点动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog点动
    * @param  [in]  ref 0-关节点动，2-基坐标系下点动，4-工具坐标系下点动，8-工件坐标系下点动
    * @param  [in]  nb 1-关节1(或x轴)，2-关节2(或y轴)，3-关节3(或z轴)，4-关节4(或绕x轴旋转)，5-关节5(或绕y轴旋转)，6-关节6(或绕z轴旋转)
    * @param  [in]  dir 0-负方向，1-正方向
    * @param  [in]  vel 速度百分比，[0~100]
    * @param  [in]  acc 加速度百分比， [0~100]
    * @param  [in]  max_dis 单次点动最大角度，单位[°]或距离，单位[mm]
    * @return  错误码
    */
    errno_t  StartJOG(uint8_t ref, uint8_t nb, uint8_t dir, float vel, float acc, float max_dis);

jog点动减速停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog点动减速停止
    * @param  [in]  ref  1-关节点动停止，3-基坐标系下点动停止，5-工具坐标系下点动停止，9-工件坐标系下点动停止
    * @return  错误码
    */
    errno_t  StopJOG(uint8_t ref);

jog点动立即停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief jog点动立即停止
    * @return  错误码
    */
    errno_t  ImmStopJOG(); 

机器人点动控制代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestJOG(void)
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
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.ImmStopJOG();
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.ImmStopJOG();
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.StopJOG(5);
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.StopJOG(9);
             robot.Sleep(1000);
         }
         robot.CloseRPC();
         return 0;
     }

关节空间运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  关节空间运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    errno_t  MoveJ(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos *epos, float blendT, uint8_t offset_flag, DescPose *offset_pos);

关节空间运动(自动正运动学计算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节空间运动(自动正运动学计算)
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 错误码
    */
    errno_t MoveJ(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos* epos, float blendT, uint8_t offset_flag, DescPose* offset_pos);
   
笛卡尔空间直线运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] desc_pos 目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子[0~100]/物理速度(mm/s)
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] search 0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    * @param [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param [in] overSpeedStrategy 超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param [in] speedPercent 允许降速阈值百分比[0-100]，默认10%
    * @return 错误码
    */
    errno_t MoveL(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos, float oacc = 100.0, int velAccParamMode = 0, int overSpeedStrategy = 0, int speedPercent = 10);

笛卡尔空间直线运动(自动逆运动学计算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间直线运动(自动逆运动学计算)
    * @param [in] desc_pos  目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] search 0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param [in] overSpeedStrategy 超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param [in] speedPercent 允许降速阈值百分比[0-100]，默认10%
    * @return 错误码
    */
    errno_t MoveL(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos* epos, uint8_t search, uint8_t offset_flag, DescPose* offset_pos, int config = -1, int overSpeedStrategy = 0, int speedPercent = 10);

笛卡尔空间圆弧运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动
    * @param  [in] joint_pos_p  路径点关节位置,单位deg
    * @param  [in] desc_pos_p   路径点笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目标点关节位置,单位deg
    * @param  [in] desc_pos_t   目标点笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度缩放因子[0~100]/物理速度(mm/s)
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    errno_t MoveC(JointPos *joint_pos_p, DescPose *desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos *epos_p, uint8_t poffset_flag, DescPose *offset_pos_p, JointPos *joint_pos_t, DescPose *desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos *epos_t, uint8_t toffset_flag, DescPose *offset_pos_t, float ovl, float blendR, float oacc = 100.0, int velAccParamMode = 0);

笛卡尔空间圆弧运动 (自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间圆弧运动 (自动逆运动学计算)
    * @param [in] desc_pos_p  路径点笛卡尔位姿
    * @param [in] ptool 工具坐标号，范围[0~14]
    * @param [in] puser 工件坐标号，范围[0~14]
    * @param [in] pvel 速度百分比，范围[0~100]
    * @param [in] pacc 加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p 扩展轴位置，单位mm
    * @param [in] poffset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_p 位姿偏移量
    * @param [in] desc_pos_t  目标点笛卡尔位姿
    * @param [in] ttool 工具坐标号，范围[0~14]
    * @param [in] tuser 工件坐标号，范围[0~14]
    * @param [in] tvel 速度百分比，范围[0~100]
    * @param [in] tacc 加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t 扩展轴位置，单位mm
    * @param [in] toffset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_t 位姿偏移量
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return 错误码
    */
    errno_t MoveC(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, uint8_t poffset_flag, DescPose* offset_pos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, uint8_t toffset_flag, DescPose* offset_pos_t, float ovl, float blendR, int config = -1);

笛卡尔空间整圆运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡尔空间整圆运动
    * @param  [in] joint_pos_p  路径点1关节位置,单位deg
    * @param  [in] desc_pos_p   路径点1笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] joint_pos_t  路径点2关节位置,单位deg
    * @param  [in] desc_pos_t   路径点2笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] ovl  速度缩放因子[0~100]/物理速度(mm/s)
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    * @param  [in] blendR -1：阻塞；0~1000：平滑半径
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    errno_t Circle(JointPos* joint_pos_p, DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, JointPos* joint_pos_t, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int velAccParamMode = 0);

笛卡尔空间整圆运动(自动逆运动学计算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间整圆运动(自动逆运动学计算)
    * @param [in] desc_pos_p  路径点1笛卡尔位姿
    * @param [in] ptool 工具坐标号，范围[0~14]
    * @param [in] puser 工件坐标号，范围[0~14]
    * @param [in] pvel 速度百分比，范围[0~100]
    * @param [in] pacc 加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p 扩展轴位置，单位mm
    * @param [in] desc_pos_t  路径点2笛卡尔位姿
    * @param [in] ttool 工具坐标号，范围[0~14]
    * @param [in] tuser 工件坐标号，范围[0~14]
    * @param [in] tvel 速度百分比，范围[0~100]
    * @param [in] tacc 加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t 扩展轴位置，单位mm
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] oacc 加速度百分比
    * @param [in] blendR -1：阻塞；0~1000：平滑半径
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return 错误码
    */
    errno_t Circle(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int config = -1);
    
笛卡尔空间点到点运动
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡尔空间点到点运动
    * @param  [in]  desc_pos  目标笛卡尔位姿或位姿增量
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms 
    * @param  [in] config  关节空间配置，[-1]-参考当前关节位置解算，[0~7]-参考特定关节空间配置解算，默认为-1   
    * @return  错误码
    */
    errno_t  MoveCart(DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

机器人基本运动指令代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMove(void)
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

        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float oacc = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, oacc, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&j3, &desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &j4, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, oacc, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&j3, &desc_pos3, tool, user, vel, acc, &epos, &j1, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(&desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, -1, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, -1, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&desc_pos3, tool, user, vel, acc, &epos, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, blendR, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        robot.CloseRPC();
        return 0;
    }

笛卡尔空间螺旋线运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡尔空间螺旋线运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] ovl  速度缩放因子，范围[0~100]    
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] spiral_param  螺旋参数
    * @return  错误码
    */
    errno_t  NewSpiral(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, ExaxisPos *epos, float ovl, uint8_t offset_flag, DescPose *offset_pos, SpiralParam spiral_param);  

笛卡尔空间螺旋线运动 (自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间螺旋线运动 (自动逆运动学计算)
    * @param [in] desc_pos  目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] spiral_param 螺旋参数
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return 错误码
    */
    errno_t NewSpiral(DescPose* desc_pos, int tool, int user, float vel, float acc, ExaxisPos* epos, float ovl, uint8_t offset_flag, DescPose* offset_pos, SpiralParam spiral_param, int config = -1);

螺旋线运动代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSpiral(void)
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
      JointPos j(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      DescPose desc_pos(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose offset_pos1(50, 0, 0, -30, 0, 0);
      DescPose offset_pos2(50, 0, 0, -5, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      SpiralParam sp;
      sp.circle_num = 5;
      sp.circle_angle = 5.0;
      sp.rad_init = 50.0;
      sp.rad_add = 10.0;
      sp.rotaxis_add = 10.0;
      sp.rot_direction = 0;
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = 0.0;
      uint8_t flag = 2;
      robot.SetSpeed(20);
      rtn = robot.MoveJ(&j, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos1);
      printf("movej errcode:%d\n", rtn);
      rtn = robot.NewSpiral(&desc_pos, tool, user, vel, acc, &epos, ovl, flag, &offset_pos2, sp);
      printf("newspiral errcode:%d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

伺服运动开始
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 伺服运动开始，配合ServoJ、ServoCart指令使用
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoMoveStart(int comType = 0);

伺服运动结束
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 伺服运动结束，配合ServoJ、ServoCart指令使用
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoMoveEnd(int comType = 0);

关节空间伺服模式运动
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节空间伺服模式运动
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] axisPos 外部轴位置,单位mm
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放，默认为0
    * @param [in] vel 速度百分比，范围[0~100]，暂不开放，默认为0
    * @param [in] cmdT 指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param [in] filterT 滤波时间，单位s，暂不开放，默认为0
    * @param [in] gain 目标位置的比例放大器，暂不开放，默认为0
    * @param [in] id servoJ指令ID,默认为0
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoJ(JointPos *joint_pos, ExaxisPos* axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id = 0, int comType = 0);

关节空间伺服模式运动示例程序
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoJ(void)
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
        JointPos j(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.008;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 500;
        float dt = 0.1;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, &j);
        if (ret == 0)
        {
            robot.ServoMoveStart();
            while (count)
            {
                robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID);
                j.jPos[0] += dt;
                count -= 1;
                robot.WaitMs(cmdT * 1000);
            }
            robot.ServoMoveEnd();
        }
        else
        {
            printf("GetActualJointPosDegree errcode:%d\n", ret);
        }
        robot.CloseRPC();
        return 0;
    }

基于UDP通信的机器人关节空间伺服模式运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    void UDPFrameCallBack(int srcType, int count, int cmdID, int len, std::string content)
    {
        cout << "recv cmd: cmdID:  " << to_string(cmdID) << "  content is " << content << "  count is " << count << endl;;
            return;
    }

    int TestServoJUDP(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        int rtn = 0;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        rtn = robot.SetCmdRpyCallback(UDPFrameCallBack);
        printf("SetCmdRpyCallback rtn is %d\n", rtn);
        rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 50);
        JointPos j(0, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        while (true)
        {
            robot.MoveJ(&j, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
            float vel = 0.0;
            float acc = 0.0;
            float cmdT = 0.016;
            float filterT = 0.0;
            float gain = 0.0;
            uint8_t flag = 0;
            float dt = 0.1;
            int cmdID = 0;
            int ret = robot.GetActualJointPosDegree(flag, &j);
            if (ret != 0)
            {
                printf("GetActualJointPosDegree errcode:%d\n", ret);
            }
            int comType = 1;
            int count = 300;
            rtn = robot.ServoMoveStart(comType);
            printf("ServoMoveStart rtn is %d\n", rtn);
            while (count)
            {
                rtn = robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                printf("ServoJ rtn is %d\n", rtn);
                j.jPos[0] += dt;
                j.jPos[1] += dt;
                j.jPos[2] += dt;
                j.jPos[3] += dt;
                j.jPos[4] += dt;
                j.jPos[5] += dt;
                epos.ePos[0] += dt;
                count -= 1;
                robot.Sleep(15);
            }
            robot.ServoMoveEnd(comType);
            printf("ServoMoveEnd rtn is %d\n", rtn);
            count = 300;
            robot.ServoMoveStart(comType);
            printf("ServoMoveStart rtn is %d\n", rtn);
            while (count)
            {
                robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                printf("ServoJ rtn is %d\n", rtn);
                j.jPos[0] -= dt;
                j.jPos[1] -= dt;
                j.jPos[2] -= dt;
                j.jPos[3] -= dt;
                j.jPos[4] -= dt;
                j.jPos[5] -= dt;
                epos.ePos[0] -= dt;
                count -= 1;
                robot.Sleep(15);
            }
            robot.ServoMoveEnd(comType);
            printf("ServoMoveEnd rtn is %d\n", rtn);
        }
        robot.Sleep(4000);
        robot.CloseRPC();
        return 0;
    }

关节扭矩控制开始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制开始
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoJTStart(int comType = 0);

关节扭矩控制
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制
    * @param [in] torque j1~j6关节扭矩，单位Nm
    * @param [in] interval 指令周期，单位s，范围[0.001~0.008]
    * @param [in] checkFlag 检测策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同时限制
    * @param [in] jPowerLimit 关节最大功率限制(W)
    * @param [in] jVelLimit 关节最大速度(°/s)
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoJT(float torque[], double interval, int checkFlag, double jPowerLimit[6], double jVelLimit[6], int comType = 0);

关节扭矩控制结束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制结束
    * @param [in] comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    errno_t ServoJTEnd(int comType = 0);

关节扭矩控制代码示例
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestServoJT(void)
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

具有超速保护的关节扭矩控制代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int ServoJTWithSafety(FRRobot* robot)
    {
        robot->ResetAllError();
        robot->Sleep(500);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot->GetJointTorques(1, torques);
        robot->ServoJTStart(); 
        ROBOT_STATE_PKG pkg = {};
        robot->DragTeachSwitch(1);
        int checkFlag = 3;
        //double jPowerLimit[6] = {1, 1, 1, 1, 1, 1}; 
        double jPowerLimit[6] = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double jVelLimit[6] = { 181, 80, 80, 80, 80, 80 };
        int count = 800000;
        int error = 0;
        while (count > 0)
        {
            torques[2] = torques[2] + 0.01;
            error = robot->ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit); 
            if (error != 0)
            {
                robot->ServoJTEnd();
            }
            printf("ServoJT rtn is %d\n", error);
            count = count - 1;
            robot->Sleep(1);
            robot->GetRobotRealTimeState(&pkg);
            printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
        }
        robot->DragTeachSwitch(0);
        error = robot->ServoJTEnd();  
        return 0;
    }

基于UDP通信的机器人关节扭矩控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    void UDPFrameCallBack(int srcType, int count, int cmdID, int len, std::string content)
    {
        cout << "recv cmd: cmdID:  " << to_string(cmdID) << "  content is " << content << "  count is " << count << endl;
        
        return;
    }
    int TestServoJTUDP(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetCmdRpyCallback(UDPFrameCallBack);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
        	return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        JointPos j(0, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        robot.MoveJ(&j, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);
        int comType = 1;
        int count = 100;
        int checkFlag = 3;
        double jPowerLimit[6] = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double jVelLimit[6] = { 80, 80, 80, 80, 80, 80 };
        rtn = robot.ServoJTStart(comType);
        printf("ServoJTStart rtn is %d\n", rtn);
        while (true)
        {
            torques[0] = 0.05;
            rtn = robot.ServoJT(torques, 0.001, checkFlag, jPowerLimit, jVelLimit, comType);
            printf("ServoJT rtn is %d\n", rtn);
            robot.Sleep(1);
            robot.GetRobotRealTimeState(&pkg);
            if (pkg.jt_cur_pos[0] > 30)
            {
                break;
            }
        }
        while (true)
        {
            torques[0] = -0.03;
            rtn = robot.ServoJT(torques, 0.001, checkFlag, jPowerLimit, jVelLimit, comType);
            printf("ServoJT rtn is %d\n", rtn);
            robot.Sleep(1);
            robot.GetRobotRealTimeState(&pkg);
            if (pkg.jt_cur_pos[0] < 0 || pkg.jt_cur_pos[1] < -110)
            {
                break;
            }
        }
        rtn = robot.ServoJTEnd(comType);
        printf("ServoJTEnd rtn is %d\n", rtn);
        robot.DragTeachSwitch(0);
        robot.Sleep(1000);
        robot.CloseRPC();
        return 0;
    }

笛卡尔空间伺服模式运动
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间伺服模式运动
    * @param [in] mode 0-绝对运动(基坐标系)，1-增量运动(基坐标系)，2-增量运动(工具坐标系)
    * @param [in] desc_pos 目标笛卡尔位姿或位姿增量
    * @param [in] exaxis 扩展轴位置
    * @param [in] pos_gain 位姿增量比例系数，仅在增量运动下生效，范围[0~1]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放，默认为0
    * @param [in] vel 速度百分比，范围[0~100]，暂不开放，默认为0
    * @param [in] cmdT 指令下发周期，单位s，建议范围[0.001~0.016]
    * @param [in] filterT 滤波时间，单位s，暂不开放，默认为0
    * @param [in] gain 目标位置的比例放大器，暂不开放，默认为0
    * @return 错误码
    */
    errno_t ServoCart(int mode, DescPose *desc_pose, ExaxisPos exaxis, float pos_gain[6], float acc, float vel, float cmdT, float filterT, float gain);

笛卡尔空间伺服模式运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoCart(void)
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
        DescPose desc_pos_dt = { 83.00800, 50.525000 , 29.246 , 179.629 , -7.138 , -166.975 };
        ExaxisPos exaxis = { 100.0, 0.0, 0.0, 0.0 };
        float pos_gain[6] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int mode = 0;
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.001;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 5000;
        robot.SetSpeed(20);
        while (count)
        {
            rtn = robot.ServoCart(mode, &desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            printf("ServoCart rtn is %d\n", rtn);
            count -= 1;
            desc_pos_dt.tran.x += 0.01;
            exaxis.ePos[0] += 0.01;
        }
        robot.CloseRPC();
        return 0;
    }

样条运动开始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  样条运动开始
    * @return  错误码
    */
    errno_t  SplineStart();

关节空间样条运动(自动正运动学计算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节空间样条运动(自动正运动学计算)
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @return 错误码
    */
    errno_t SplinePTP(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl);

样条运动PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  关节空间样条运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]   
    * @return  错误码
    */
    errno_t  SplinePTP(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl);

样条运动结束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  样条运动结束
    * @return  错误码
    */
    errno_t  SplineEnd();

样条运动代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSpline(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
      JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = -1.0;
      uint8_t flag = 0;
      robot.SetSpeed(20);
      int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.SplineStart();
      robot.SplinePTP(&j1, &desc_pos1, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j2, &desc_pos2, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j3, &desc_pos3, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j4, &desc_pos4, tool, user, vel, acc, ovl);
      robot.SplineEnd();
      err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.SplineStart();
      robot.SplinePTP(&j1, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j2, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j3, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j4, tool, user, vel, acc, ovl);
      robot.SplineEnd();
      robot.CloseRPC();
      return 0;
    }

新样条运动开始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 新样条运动开始
    * @param [in] type  0-圆弧过渡，1-给定点位为路径点
    * @param [in] averageTime 全局平均衔接时间(ms)(10 ~ )，默认2000
    * @return 错误码
    */
    errno_t NewSplineStart(int type, int averageTime=2000);

新样条指令点
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 新样条指令点
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] desc_pos  目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm 
    * @param  [in] lastFlag 是否为最后一个点，0-否，1-是
    * @return 错误码
    */ 
    errno_t NewSplinePoint(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新样条指令点(自动逆运动学计算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 新样条指令点(自动逆运动学计算)
    * @param [in] desc_pos  目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] lastFlag 是否为最后一个点，0-否，1-是
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return 错误码
    */
    errno_t NewSplinePoint(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag, int config = -1);

新样条运动结束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 新样条运动结束
    * @return 错误码
    */
    errno_t NewSplineEnd();

新样条运动代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestNewSpline(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
      JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
      JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
      DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = -1.0;
      uint8_t flag = 0;
      robot.SetSpeed(20);
      int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.NewSplineStart(1, 2000);
      robot.NewSplinePoint(&j1, &desc_pos1, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j2, &desc_pos2, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j3, &desc_pos3, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j4, &desc_pos4, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j5, &desc_pos5, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplineEnd();
      err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.NewSplineStart(1, 2000);
      robot.NewSplinePoint(&desc_pos1, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos2, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos3, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos4, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos5, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplineEnd();
      robot.CloseRPC();
      return 0;
    }

终止运动
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 终止运动
    * @return  错误码
    */
    errno_t  StopMotion();

暂停运动
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 暂停运动
    * @return 错误码
    */
    errno_t PauseMotion(); 

恢复运动
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:
    
    /**
    * @brief 恢复运动
    * @return 错误码
    */
    errno_t ResumeMotion();

运动暂停、恢复、停止代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestPause(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         rtn = robot.MoveJ(&j5, &desc_pos5, tool, user, vel, acc, ovl, &epos, 1, flag, &offset_pos);
         robot.Sleep(1000);
         robot.PauseMotion();
         robot.Sleep(1000);
         robot.ResumeMotion();
         robot.Sleep(1000);
         robot.StopMotion();
         robot.Sleep(1000);
         robot.CloseRPC();
         return 0;
     }

点位整体偏移开始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  点位整体偏移开始
    * @param  [in]  flag  0-基坐标系下/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    errno_t  PointsOffsetEnable(int flag, DescPose *offset_pos);

点位整体偏移结束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  点位整体偏移结束
    * @return  错误码
    */
    errno_t  PointsOffsetDisable();

点位偏移代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestOffset(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         DescPose offset_pos1(0, 0, 50, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.Sleep(1000);
         robot.PointsOffsetEnable(0, &offset_pos1);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.PointsOffsetDisable();
         robot.CloseRPC();
         return 0;
     }

控制箱AO飞拍开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飞拍开始
    * @param [in] AONum 控制箱AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    errno_t MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飞拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飞拍停止
    * @return 错误码
    */
    errno_t MoveAOStop();
    
末端AO飞拍开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飞拍开始
    * @param [in] AONum 末端AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    errno_t MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飞拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飞拍停止
    * @return 错误码
    */
    errno_t MoveToolAOStop();

AO飞拍代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestMoveAO(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         DescPose offset_pos1(0, 0, 50, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 20.0;
         float acc = 20.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         robot.MoveAOStart(0, 100, 100, 20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveAOStop();
         robot.Sleep(1000);
         robot.MoveToolAOStart(0, 100, 100, 20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveToolAOStop();
         robot.CloseRPC();
         return 0;
     }

开始Ptp运动FIR滤波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 开始Ptp运动FIR滤波
    * @param [in] maxAcc 最大加速度极值(deg/s2)
    * @param [in] maxJek 统一关节急动度极值(deg/s3)
    * @return 错误码
    */
    errno_t PtpFIRPlanningStart(double maxAcc, double maxJek = 1000);

关闭Ptp运动FIR滤波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 关闭Ptp运动FIR滤波
	* @return 错误码
	*/
	errno_t PtpFIRPlanningEnd();

开始LIN、ARC运动FIR滤波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 开始LIN、ARC运动FIR滤波
	* @param [in] maxAccLin 线加速度极值(mm/s2)
	* @param [in] maxAccDeg 角加速度极值(deg/s2)
	* @param [in] maxJerkLin 线加加速度极值(mm/s3)
	* @param [in] maxJerkDeg 角加加速度极值(deg/s3)
	* @return 错误码
	*/
	errno_t LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

关闭LIN、ARC运动FIR滤波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 关闭LIN、ARC运动FIR滤波
	* @return 错误码
	*/
	errno_t LinArcFIRPlanningEnd();

FIR滤波代码示例
+++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestFIR(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos midjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         JointPos endjointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose middescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose enddescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.PtpFIRPlanningStart(1000, 1000);
         cout << "PtpFIRPlanningStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.PtpFIRPlanningEnd();
         cout << "PtpFIRPlanningEnd rtn is " << rtn << endl;
         robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
         cout << "LinArcFIRPlanningStart rtn is " << rtn << endl;
         robot.MoveL(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
         robot.MoveC(&midjointPos, &middescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, &endjointPos, &enddescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, 100, -1);
         robot.LinArcFIRPlanningEnd();
         cout << "LinArcFIRPlanningEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

加速度平滑开启
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑开启
    * @param [in] saveFlag 是否断电保存
    * @return 错误码
    */
    errno_t AccSmoothStart(bool saveFlag);

加速度平滑关闭
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑关闭
    * @param [in] saveFlag 是否断电保存
    * @return 错误码
    */
    errno_t AccSmoothEnd(bool saveFlag);

加速度平滑代码示例
+++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAccSmooth(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.AccSmoothStart(0);
         cout << "AccSmoothStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.AccSmoothEnd(0);
         cout << "AccSmoothEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }


指定姿态速度开启
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿态速度开启
    * @param [in] ratio 姿态速度百分比[0-300]
    * @return 错误码
    */
    errno_t AngularSpeedStart(int ratio);

指定姿态速度关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿态速度关闭
    * @return 错误码
    */
    errno_t AngularSpeedEnd();

机器人指定姿态速度代码示例
++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.AngularSpeedStart(50);
         cout << "AngularSpeedStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.AngularSpeedEnd();
         cout << "AngularSpeedEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

开始奇异位姿保护
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 开始奇异位姿保护
	* @param [in] protectMode 奇异保护模式，0：关节模式；1-笛卡尔模式
	* @param [in] minShoulderPos 肩奇异调整范围(mm), 默认100
	* @param [in] minElbowPos 肘奇异调整范围(mm), 默认50
	* @param [in] minWristPos 腕奇异调整范围(°), 默认10
	* @return 错误码
	*/
	errno_t SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇异位姿保护
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 停止奇异位姿保护
	* @return 错误码
	*/
	errno_t SingularAvoidEnd();

机器人奇异位姿保护代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.SingularAvoidStart(2, 10, 5, 5);
         cout << "SingularAvoidStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.SingularAvoidEnd();
         cout << "SingularAvoidEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }
    
清空运动指令队列
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 清空运动指令队列
    * @return 错误码
    */
    errno_t MotionQueueClear();
        
移动到相贯线起始点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 移动到相贯线起始点
    * @param [in] mainPoint 主管6个示教点的笛卡尔位姿
    * @param [in] mainExaxisPos 主管6个示教点扩展轴位置
    * @param [in] piecePoint 辅管6个示教点的笛卡尔位姿
    * @param [in] pieceExaxisPos 拼接管6个示教点扩展轴位置
    * @param [in] extAxisFlag 是否启用扩展轴；0-不启用；1-启用
    * @param [in] exaxisPos 起点扩展轴位置
    * @param [in] tool 工具坐标系编号
    * @param [in] wobj 工件坐标系编号
    * @param [in] vel 速度百分比
    * @param [in] acc 加速度百分比
    * @param [in] ovl 速度缩放因子
    * @param [in] oacc 加速度缩放因子
    * @param [in] moveType 运动类型; 0-PTP；1-LIN
    * @param [in] moveDirection 运动方向；0-顺时针；1-逆时针
    * @param [in] offset 偏移量
    * @return 错误码
    */
    errno_t MoveToIntersectLineStart(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);
            
相贯线运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 相贯线运动
    * @param [in] mainPoint 主管6个示教点的笛卡尔位姿
    * @param [in] mainExaxisPos 主管6个示教点扩展轴位置
    * @param [in] piecePoint 辅管6个示教点的笛卡尔位姿
    * @param [in] pieceExaxisPos 拼接管6个示教点扩展轴位置
    * @param [in] extAxisFlag 是否启用扩展轴；0-不启用；1-启用
    * @param [in] exaxisPos 起点扩展轴位置
    * @param [in] tool 工具坐标系编号
    * @param [in] wobj 工件坐标系编号
    * @param [in] vel 速度百分比
    * @param [in] acc 加速度百分比
    * @param [in] ovl 速度缩放因子
    * @param [in] oacc 加速度缩放因子
    * @param [in] moveDirection 运动方向; 0-顺时针；1-逆时针
    * @param [in] offset 偏移量
    * @return 错误码
    */
    errno_t MoveIntersectLine(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos[4], int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);
                
机器人相贯线运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    void TestIntersectLineMove()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(3);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return ;
        }
        robot.SetReConnectParam(true, 30000, 500);
        DescPose mainPoint[6] = {};
        DescPose piecePoint[6] = {};
        ExaxisPos mainExaxisPos[6] = {};
        ExaxisPos pieceExaxisPos[6] = {};
        int extAxisFlag = 1;
        ExaxisPos exaxisPos[4] = {};
        DescPose offset = { 0.0, 2.0 ,30.0, -2.0, 0.0, 0.0 };
        mainPoint[0] = {490.004, -383.194, 402.735, -9.332, -1.528, 69.594};
        mainPoint[1] = {444.950, -407.117, 389.011, -5.546, -2.196, 65.279};
        mainPoint[2] = {445.168, -463.605, 355.759, -1.544, -10.886, 57.104};
        mainPoint[3] = {507.529, -485.385, 343.013, -0.786, -4.834, 61.799};
        mainPoint[4] = {554.390, -442.647, 367.701, -4.761, -10.181, 64.925};
        mainPoint[5] = {532.552, -394.003, 396.467, -13.732, -13.592, 67.411};
        mainExaxisPos[0] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[1] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[2] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[3] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[4] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[5] = { -29.996, 0.000, 0.000, 0.000 };
        piecePoint[0] = { 505.571, -192.408, 316.759, 38.098, 37.051, 139.447 };
        piecePoint[1] = {533.837, -201.558, 332.340, 34.644, 42.339, 137.748};
        piecePoint[2] = {530.386, -225.085, 373.808, 35.431, 45.111, 137.560};
        piecePoint[3] = {485.646, -229.195, 383.778, 33.870, 45.173, 137.064};
        piecePoint[4] = {460.551, -212.161, 354.256, 28.856, 45.602, 135.930};
        piecePoint[5] = {474.217, -197.124, 324.611, 42.469, 41.133, 148.167};
        pieceExaxisPos[0] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[1] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[2] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[3] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[4] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[5] = { -29.996, -0.000, 0.000, 0.000 };
        exaxisPos[0] = {-29.996, -0.000, 0.000, 0.000};
        exaxisPos[1] = {-44.994, 90.000, 0.000, 0.000};
        exaxisPos[2] = {-59.992, 0.002, 0.000, 0.000};
        exaxisPos[3] = {-44.994, -89.997, 0.000, 0.000};
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0; 
        int moveType = 1;
        int moveDirection = 1;
        rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return ;
    }

原地空运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 原地空运动
    * @return 错误码
    */
    errno_t MoveStationary();

原地空运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLaserStationary(void)
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
        rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 0, 10, 100);
        printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        rtn = robot.MoveStationary();
        printf("MoveStationary rtn is %d\n", rtn);
        rtn = robot.LaserSensorRecord1(0, 10);
        printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(9999999);
        return 0;
    }

定点摆动开始
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 定点摆动开始
    * @param [in] weaveNum 摆动编号[0-7]
    * @param [in] mode 0-工具坐标系；1-参考点
    * @param [in] refPoint 参考点笛卡尔坐标[x,y,z,a,b,c]
    * @param [in] weaveTime 摆动时间[s]
    * @return 错误码
    */
    errno_t OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime);
    
定点摆动结束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 定点摆动结束
    * @return 错误码
    */
    errno_t OriginPointWeaveEnd();
        
定点摆动的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestOriginPointWeave()
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
        JointPos j(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        DescPose refPoint = { 400.021,300.022,299.996,179.997,-0.003,-90.956 };
        robot.MoveJ(&j, 1, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
        robot.Sleep(2000);
        robot.MoveJ(&j, 1, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }