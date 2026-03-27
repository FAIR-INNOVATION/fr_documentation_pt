机器人运动
============

.. toctree:: 
    :maxdepth: 5


jog点动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief jog 点动 
    * @param [in] refType 0-关节点动，2-基坐标系下点动，4-工具坐标系下点动，8-工件坐标系下点动
    * @param [in] nb 1-关节1(或x轴)，2-关节2(或y轴)，3-关节3(或z轴)，4-关节4(或绕x轴旋转)，5-关节5(或绕y轴旋转)，6-关节6(或绕z轴旋转)
    * @param [in] dir 0-负方向，1-正方向
    * @param [in] vel 速度百分比，[0~100]
    * @param [in] acc 加速度百分比， [0~100]
    * @param [in] max_dis 单次点动最大角度，单位[°]或距离，单位[mm]
    * @return 错误码 
    */ 
    int StartJOG(int refType, int nb, int dir, double vel, double acc, double max_dis);

jog点动减速停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  jog点动减速停止
    * @param  [in]  stopType  1-关节点动停止，3-基坐标系下点动停止，5-工具坐标系下点动停止，9-工件坐标系下点动停止
    * @return  错误码
    */
    int StopJOG(int stopType);

jog点动立即停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief jog点动立即停止
    * @return  错误码
    */
    int ImmStopJOG(); 

机器人点动控制代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static  int TestJOG(Robot robot)
    {
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
        return 0;
    }

关节空间运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos  目标笛卡尔位姿
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

关节空间运动(自动正运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief  关节空间运动(自动正运动学计算)
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return 错误码 
    */ 
    int MoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos)

笛卡尔空间直线运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动(重载函数1 增加blendMode)
    * @param  joint_pos  目标关节位置,单位deg
    * @param  desc_pos   目标笛卡尔位姿
    * @param  tool  工具坐标号，范围[1~15]
    * @param  user  工件坐标号，范围[1~15]
    * @param  vel  速度百分比，范围[0~100]
    * @param  acc  加速度百分比，范围[0~100],暂不开放
    * @param  ovl  速度缩放因子[0~100]/物理速度(mm/s)
    * @param  blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param  epos  扩展轴位置，单位mm
    * @param  search  0-不焊丝寻位，1-焊丝寻位
    * @param  offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  offset_pos  位姿偏移量
    * @param  oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    * @param  velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param  speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, double oacc,int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡尔空间直线运动(自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动(自动逆运动学计算)
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[1~15]
    * @param [in] user  工件坐标号，范围[1~15]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param [in] overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param [in] speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */
    int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int overSpeedStrategy, int speedPercent)

笛卡尔空间直线运动（增加速度加速度参数模式velAccParamMode参数）
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动（增加速度加速度参数模式velAccParamMode参数）
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[1~15]
    * @param  [in] user  工件坐标号，范围[1~15]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param  [in] speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡尔空间直线运动(重载函数1 增加blendMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动(重载函数1 增加blendMode)
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[1~15]
    * @param  [in] user  工件坐标号，范围[1~15]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param  [in] speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡尔空间直线运动(重载函数2 不需要输入关节位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动(重载函数2 不需要输入关节位置)
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[1~15]
    * @param  [in] user  工件坐标号，范围[1~15]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] blendMode 过渡方式；0-内切过渡；1-角点过渡
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param  [in] speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */
    public int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡尔空间圆弧运动
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动
    * @param  joint_pos_p  路径点关节位置,单位deg
    * @param  desc_pos_p   路径点笛卡尔位姿
    * @param  ptool  工具坐标号，范围[1~15]
    * @param  puser  工件坐标号，范围[1~15]
    * @param  pvel  速度百分比，范围[0~100]
    * @param  pacc  加速度百分比，范围[0~100],暂不开放
    * @param  epos_p  扩展轴位置，单位mm
    * @param  poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  offset_pos_p  位姿偏移量
    * @param  joint_pos_t  目标点关节位置,单位deg
    * @param  desc_pos_t   目标点笛卡尔位姿
    * @param  ttool  工具坐标号，范围[1~15]
    * @param  tuser  工件坐标号，范围[1~15]
    * @param  tvel  速度百分比，范围[0~100]
    * @param  tacc  加速度百分比，范围[0~100],暂不开放
    * @param  epos_t  扩展轴位置，单位mm
    * @param  toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  offset_pos_t  位姿偏移量
    * @param  ovl  速度缩放因子[0~100]/物理速度(mm/s)
    * @param  blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    * @param  velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, double oacc,int velAccParamMode)

笛卡尔空间圆弧运动(自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动(自动逆运动学计算)
    * @param [in] desc_pos_p   路径点笛卡尔位姿
    * @param [in] ptool  工具坐标号，范围[1~15]
    * @param [in] puser  工件坐标号，范围[1~15]
    * @param [in] pvel  速度百分比，范围[0~100]
    * @param [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p  扩展轴位置，单位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] desc_pos_t   目标点笛卡尔位姿
    * @param [in] ttool  工具坐标号，范围[1~15]
    * @param [in] tuser  工件坐标号，范围[1~15]
    * @param [in] tvel  速度百分比，范围[0~100]
    * @param [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t  扩展轴位置，单位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_t  位姿偏移量
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return  错误码
    */
    int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config)

笛卡尔空间圆弧运动(增加速度加速度参数模式velAccParamMode参数)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动(增加速度加速度参数模式velAccParamMode参数)
    * @param  [in] joint_pos_p  路径点关节位置,单位deg
    * @param  [in] desc_pos_p   路径点笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[1~15]
    * @param  [in] puser  工件坐标号，范围[1~15]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目标点关节位置,单位deg
    * @param  [in] desc_pos_t   目标点笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[1~15]
    * @param  [in] tuser  工件坐标号，范围[1~15]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int velAccParamMode)

笛卡尔空间圆弧运动(重载函数1 不需要输入关节位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动 (重载函数1 不需要输入关节位置)
    * @param  [in] desc_pos_p   路径点笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[1~15]
    * @param  [in] puser  工件坐标号，范围[1~15]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] desc_pos_t   目标点笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[1~15]
    * @param  [in] tuser  工件坐标号，范围[1~15]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    public int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config, int velAccParamMode)

笛卡尔空间整圆运动
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    *@brief  笛卡尔空间整圆运动
    *@param  joint_pos_p  路径点1关节位置,单位deg
    *@param  desc_pos_p   路径点1笛卡尔位姿
    *@param  ptool  工具坐标号，范围[1~15]
    *@param  puser  工件坐标号，范围[1~15]
    *@param  pvel  速度百分比，范围[0~100]
    *@param  pacc  加速度百分比，范围[0~100],暂不开放
    *@param  epos_p  扩展轴位置，单位mm
    *@param  joint_pos_t  路径点2关节位置,单位deg
    *@param  desc_pos_t   路径点2笛卡尔位姿
    *@param  ttool  工具坐标号，范围[1~15]
    *@param  tuser  工件坐标号，范围[1~15]
    *@param  tvel  速度百分比，范围[0~100]
    *@param  tacc  加速度百分比，范围[0~100],暂不开放
    *@param  epos_t  扩展轴位置，单位mm
    *@param  ovl  速度缩放因子[0~100]/物理速度(mm/s)
    *@param  offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    *@param  offset_pos  位姿偏移量
    *@param  oacc 加速度缩放因子[0-100]/物理加速度(mm/s2)
    *@param  blendR -1：阻塞；0~1000：平滑半径
    *@param  velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    *@return  错误码
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

笛卡尔空间整圆运动(自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
     * @brief  笛卡尔空间整圆运动(自动逆运动学计算)
     * @param  [in] desc_pos_p   路径点1笛卡尔位姿
     * @param  [in] ptool  工具坐标号，范围[0~14]
     * @param  [in] puser  工件坐标号，范围[0~14]
     * @param  [in] pvel  速度百分比，范围[0~100]
     * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
     * @param  [in] epos_p  扩展轴位置，单位mm
     * @param  [in] desc_pos_t   路径点2笛卡尔位姿
     * @param  [in] ttool  工具坐标号，范围[0~14]
     * @param  [in] tuser  工件坐标号，范围[0~14]
     * @param  [in] tvel  速度百分比，范围[0~100]
     * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
     * @param  [in] epos_t  扩展轴位置，单位mm
     * @param  [in] ovl  速度缩放因子，范围[0~100]
     * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
     * @param  [in] offset_pos  位姿偏移量
     * @param  [in] oacc 加速度百分比
     * @param  [in] blendR -1：阻塞；0~1000：平滑半径
     * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
     * @return  错误码
     */
    int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR,int config)

笛卡尔空间整圆运动（增加速度加速度参数模式velAccParamMode参数）
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    *@brief  笛卡尔空间整圆运动（增加速度加速度参数模式velAccParamMode参数）
    *@param  [in] joint_pos_p  路径点1关节位置,单位deg
    *@param  [in] desc_pos_p   路径点1笛卡尔位姿
    *@param  [in] ptool  工具坐标号，范围[1~15]
    *@param  [in] puser  工件坐标号，范围[1~15]
    *@param  [in] pvel  速度百分比，范围[0~100]
    *@param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    *@param  [in] epos_p  扩展轴位置，单位mm
    *@param  [in] joint_pos_t  路径点2关节位置,单位deg
    *@param  [in] desc_pos_t   路径点2笛卡尔位姿
    *@param  [in] ttool  工具坐标号，范围[1~15]
    *@param  [in] tuser  工件坐标号，范围[1~15]
    *@param  [in] tvel  速度百分比，范围[0~100]
    *@param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    *@param  [in] epos_t  扩展轴位置，单位mm
    *@param  [in] ovl  速度缩放因子，范围[0~100]
    *@param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    *@param  [in] offset_pos  位姿偏移量
    *@param  [in] oacc 加速度百分比
    *@param  [in] blendR -1：阻塞；0~1000：平滑半径
    *@param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    *@return  错误码
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

笛卡尔空间整圆运动 (重载函数1 不需要输入关节位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间整圆运动 (重载函数1 不需要输入关节位置)
    * @param  [in] desc_pos_p   路径点1笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] desc_pos_t   路径点2笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] oacc 加速度百分比
    * @param  [in] blendR -1：阻塞；0~1000：平滑半径
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [in] velAccParamMode 速度加速度参数模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  错误码
    */
    public int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int config, int velAccParamMode)

笛卡尔空间点到点运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 笛卡尔空间点到点运动 
    * @param [in] desc_pos  目标笛卡尔位姿或位姿增量
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] config  关节空间配置，[-1]-参考当前关节位置解算，[0~7]-参考特定关节空间配置解算，默认为-1
    * @return 错误码 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendT, int config);

机器人基本运动指令代码示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn=-1;
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4=new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4=new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

笛卡尔空间螺旋线运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡尔空间螺旋线运动 
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param);

笛卡尔空间螺旋线运动(自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡尔空间螺旋线运动 (自动逆运动学计算)
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @param [in] spiral_param  螺旋参数
    * @param [in] config  逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return 错误码 
    */
    int NewSpiral(DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param,int config)

螺旋线运动代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpiral(Robot robot)
    {
        int rtn=-1;
        JointPos j=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose offset_pos1=new DescPose(50, 0, 0, -30, 0, 0);
        DescPose offset_pos2=new DescPose(50, 0, 0, -5, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp=new SpiralParam(1,5.0,50.0,10.0,10.0,0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = 0.0;
        int flag = 2;

        rtn = robot.MoveJ(j, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
        System.out.println("movej errcode:"+ rtn);

        rtn = robot.NewSpiral(desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp,-1);
        System.out.println("newspiral errcode:"+ rtn);

        return 0;
    }

伺服运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 伺服运动开始，配合ServoJ、ServoCart指令使用
    * @param comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    public int ServoMoveStart (int comType)

伺服运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 伺服运动开始，配合ServoJ、ServoCart指令使用
    * @param comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    public int ServoMoveEnd (int comType)

关节空间伺服模式运动
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间伺服模式运动
    * @param  joint_pos  目标关节位置,单位deg
    * @param  axisPos  外部轴位置,单位mm
    * @param  acc  加速度百分比，范围[0~100],暂不开放，默认为0
    * @param  vel  速度百分比，范围[0~100]，暂不开放，默认为0
    * @param  cmdT  指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param  filterT 滤波时间，单位s，暂不开放，默认为0
    * @param  gain  目标位置的比例放大器，暂不开放，默认为0
    * @param  id servoJ指令ID,默认为0
    * @param comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    public int ServoJ(JointPos joint_pos, ExaxisPos axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id, int comType)

基于UDP通信的ServoJ、ServoMoveStart、ServoMoveEnd SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoJ(Robot robot)
    {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Received UDP reply from robot]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("内容 (content): " + content);
            return 0;
        });
        int rtn=-1;

        JointPos j=new JointPos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        double vel = 0.0;
        double acc = 0.0;
        double cmdT = 0.016;
        double filterT = 0.0;
        double gain = 0.0;
        int flag = 0;
        int count = 300;
        double dt = 0.1;
        int cmdID = 0;
        int comType = 1;
        int ret = robot.GetActualJointPosDegree(j);
        if (ret == 0)
        {
            robot.ServoMoveStart(comType);
            count = 300;
            while (count>0)
            {
                robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                j.J1 += dt;
                j.J2 += dt;
                j.J4 += dt;
                j.J5 += dt;
                j.J6 += dt;
                epos.axis1 += dt;
                count -= 1;
                robot.Sleep(10);
            }
            robot.ServoMoveEnd(comType);

            robot.Sleep(1000);
            robot.ServoMoveStart(comType);
            count = 300;
            while (count>0)
            {
                robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                j.J1 -= dt;
                j.J2 -= dt;
                j.J4 -= dt;
                j.J5 -= dt;
                j.J6 -= dt;
                epos.axis1 -= dt;
                count -= 1;
                robot.Sleep(10);
            }
            robot.ServoMoveEnd(comType);
        }
        else
        {
            System.out.println("GetActualJointPosDegree errcode:"+ ret);
        }
    }

关节空间伺服模式运动示例程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestServoJ()
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        JointPos j5 = new JointPos();
        ExaxisPos ePos=new ExaxisPos();
        int ret = robot.GetActualJointPosDegree(j5);
        if (ret == 0)
        {
            int count = 200;
            while (count > 0)
            {
                robot.ServoJ(j5, ePos,100, 100, 0.008, 0, 0);
                j5.J1 += 0.2;//1关节位置增加
                count -= 1;
                robot.WaitMs((int)(8));
            }
        }
    }

关节扭矩控制开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节扭矩控制开始
    * @param  comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return  错误码
    */
    public int ServoJTStart (int comType)

关节扭矩控制
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关节扭矩控制
    * @param torque j1~j6关节扭矩，单位Nm
    * @param interval 指令周期，单位s，范围[0.001~0.008]
    * @param checkFlag 检测策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同时限制
    * @param jPowerLimit 关节最大功率限制(W)
    * @param jVelLimit 关节最大速度(°/s)
    * @param  comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return 错误码
    */
    public int ServoJT(double[] torque, double interval, int checkFlag, double[] jPowerLimit, double[] jVelLimit, int comType)

关节扭矩控制结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节扭矩控制结束
    * @param comType 指令下发类型；0-xmlrpc；1-UDP(对应机器人20007端口)
    * @return  错误码
    */
    public int ServoJTEnd (int comType)

关节空间伺服模式运动示例程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoJT(Robot robot)
    {

        robot.DragTeachSwitch(1);
        List<Number> joint_toq=new ArrayList<>();
        joint_toq=robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); //   #servoJT开始
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

基于UDP通信的ServoJT、ServoJTStart、ServoJTEnd SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void ServoJTWithSafety(Robot robot)
    {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Received UDP reply from robot]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("content: " + content);
            return 0;
        });
        while (true) {
            robot.ResetAllError();
            robot.Sleep(500);
            List<Number> torques;
            torques=robot.GetJointTorques(1);
            robot.ServoJTStart(1); //   #servoJT开始
            ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);
            int checkFlag = 3;//-1,3
            double[] jPowerLimit = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
            double[] jVelLimit = { 50, 50, 50, 50, 50, 50};//180.1,-1
            int count = 800000;
            int error = 0;
            int comType = 1;

            double[] tor=new double[]{(double)torques.get(1),(double)torques.get(2),(double)torques.get(3),(double)torques.get(4),(double)torques.get(5),(double)torques.get(6)};

            while (true) {
                tor[0] = 0.08;//  #每次1轴增加0.01NM，运动100次
                error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit, comType);  //# 关节空间伺服模式运动
                System.out.printf("ServoJT rtn is %d\n", error);
                count = count - 1;
                robot.Sleep(1);
                pkg = robot.GetRobotRealTimeState();
                System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
                if (pkg.jt_cur_pos[0] > 30)
                    break;
            }

            tor = new double[]{(double) torques.get(1), (double) torques.get(2), (double) torques.get(3), (double) torques.get(4), (double) torques.get(5), (double) torques.get(6)};
            while (true) {
                tor[0] = -0.08;//  #每次1轴增加0.01NM，运动100次
                error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit, 1);  //# 关节空间伺服模式运动
                System.out.printf("ServoJT rtn is %d\n", error);
                count = count - 1;
                robot.Sleep(1);
                pkg = robot.GetRobotRealTimeState();
                System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
                if (pkg.jt_cur_pos[0] < 0)
                    break;
            }

            robot.DragTeachSwitch(0);

            error = robot.ServoJTEnd(1);  //#伺服运动结束
        }
    }

具有超速保护的关节扭矩控制代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void ServoJTWithSafety(Robot robot)
    {
        robot.ResetAllError();
        robot.Sleep(500);
        List<Number> torques;
        torques=robot.GetJointTorques(1);
        robot.ServoJTStart(); //   #servoJT开始
        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        robot.DragTeachSwitch(1);
        int checkFlag = 3;//-1,3
        //double[] jPowerLimit = {1.0,1.0,1.0,1.0,1.0,1.0};//5001
        double[] jPowerLimit = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double[] jVelLimit = { 50, 50, 50, 50, 50, 50};//180.1,-1
        int count = 800000;
        int error = 0;
        double[] tor=new double[]{(double)torques.get(1),(double)torques.get(2),(double)torques.get(3),(double)torques.get(4),(double)torques.get(5),(double)torques.get(6)};
        while (count > 0)
        {
            tor[2] = tor[2]+0.01;//  #每次1轴增加0.01NM，运动100次
            error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit);  //# 关节空间伺服模式运动
            System.out.printf("ServoJT rtn is %d\n", error);
            count = count - 1;
            robot.Sleep(1);
            pkg=robot.GetRobotRealTimeState();
            System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
        }
        robot.DragTeachSwitch(0);
        error = robot.ServoJTEnd();  //#伺服运动结束
    }

笛卡尔空间伺服模式运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief 笛卡尔空间伺服模式运动
    *@param mode 0-绝对运动(基坐标系)，1-增量运动(基坐标系)，2-增量运动(工具坐标系)
    *@param desc_pose 目标笛卡尔位姿或位姿增量
    *@param exaxis 扩展轴位置
    *@param pos_gain 位姿增量比例系数，仅在增量运动下生效，范围[0~1]
    *@param acc 加速度百分比，范围[0~100],暂不开放，默认为0
    *@param vel 速度百分比，范围[0~100]，暂不开放，默认为0
    *@param cmdT 指令下发周期，单位s，建议范围[0.001~0.016]
    *@param filterT 滤波时间，单位s，暂不开放，默认为0
    *@param gain 目标位置的比例放大器，暂不开放，默认为0
    *@return 错误码
    */
    public int ServoCart(int mode, DescPose desc_pose, ExaxisPos exaxis, double[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain)

笛卡尔空间伺服模式运动代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestServoCart1(Robot robot)
    {
        DescPose desc_pos_dt = new DescPose(83.00800, 50.525000 , 29.246 , 179.629 , -7.138 , -166.975 );
        ExaxisPos exaxis = new ExaxisPos( 100.0, 0.0, 0.0, 0.0 );
        double[] pos_gain = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int mode = 0;
        double vel = 0.0;
        double acc = 0.0;
        double cmdT = 0.001;
        double filterT = 0.0;
        double gain = 0.0;
        int flag = 0;
        int count = 5000;
        robot.SetSpeed(20);
        while (count>0)
        {
            int rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            System.out.printf("ServoCart rtn is %d\n", rtn);
            count -= 1;
            desc_pos_dt.tran.x += 0.01;
            exaxis.axis1 += 0.01;
        }
        robot.CloseRPC();
    }

样条运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  样条运动开始
    * @return  错误码
    */
    int SplineStart();

关节运动PTP
+++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl);

关节空间样条运动 (自动正运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间样条运动 (自动正运动学计算)
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @return  错误码
    */
    int SplinePTP(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl)

样条运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  样条运动结束
    * @return  错误码
    */
    int SplineEnd(); 

样条运动代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpline(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4=new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:"+ err1);
        robot.SplineStart();
        robot.SplinePTP(j1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
        return 0;
    }

新样条运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @param [in] type   0-圆弧过渡，1-给定点位为路径点
    * @param [in] averageTime  全局平均衔接时间(ms)(10 ~  )，默认2000
    * @return 错误码 
    */ 
    int NewSplineStart(int type, int averageTime);
    
新样条指令点
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 增加样条运动指令点 
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] lastFlag 是否为最后一个点，0-否，1-是
    * @return 错误码 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag);

新样条指令点(自动逆运动学计算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 新样条指令点(自动逆运动学计算)
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] lastFlag 是否为最后一个点，0-否，1-是
    * @param  [in] config 逆解关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @return  错误码
    */
    int NewSplinePoint(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag,int config)

新样条运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @return 错误码 
    */ 
    int NewSplineEnd();
    
新样条运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestNewSpline(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4=new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5=new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);


        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;


        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:"+ err1);
        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(desc_pos1, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos2, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos3, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos4, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos5, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplineEnd();
        return 0;
    }

终止运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 终止运动
    * @return  错误码
    */
    int StopMotion();

暂停运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
      * @brief 暂停运动 
      * @return 错误码 
    */  
    int PauseMotion();

恢复运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 恢复运动 
    * @return 错误码 
    */ 
    int ResumeMotion();

运动暂停、恢复、停止代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPause(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5=new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5=new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);
        int rtn=-1;
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        robot.Sleep(1000);
        robot.PauseMotion();

        robot.Sleep(1000);
        robot.ResumeMotion();

        robot.Sleep(1000);
        robot.StopMotion();

        robot.Sleep(1000);

        return 0;
    }

点位整体偏移开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  点位整体偏移开始
    * @param  [in]  flag  0-基坐标系下/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in]  offset_pos  位姿偏移量
    * @return  错误码
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


点位整体偏移结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  点位整体偏移结束
    * @return  错误码
    */
    int PointsOffsetDisable(); 

点位偏移代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOffset(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1=new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.Sleep(1000);
        robot.PointsOffsetEnable(0, offset_pos1);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.PointsOffsetDisable();

        return 0;
    }

控制箱AO飞拍开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飞拍开始
    * @param [in] AONum 控制箱AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飞拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飞拍停止
    * @return 错误码
    */
    int MoveAOStop();
    
末端AO飞拍开始
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飞拍开始
    * @param [in] AONum 末端AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飞拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飞拍停止
    * @return 错误码
    */
    int MoveToolAOStop();

AO飞拍代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMoveAO(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1=new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 20.0;
        double acc = 20.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.Sleep(1000);

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();

        return 0;
    }

开始Ptp运动FIR滤波
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 开始Ptp运动FIR滤波
    * @param [in] maxAcc 最大加速度极值(deg/s2)
    * @param [in] maxJek 统一关节急动度极值(deg/s3)
    * @return 错误码
    */
    int PtpFIRPlanningStart(double maxAcc,double maxJek);

关闭Ptp运动FIR滤波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关闭Ptp运动FIR滤波
    * @return 错误码
    */
    int PtpFIRPlanningEnd();

开始LIN、ARC运动FIR滤波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 开始LIN、ARC运动FIR滤波
    * @param [in] maxAccLin 线加速度极值(mm/s2)
    * @param [in] maxAccDeg 角加速度极值(deg/s2)
    * @param [in] maxJerkLin 线加加速度极值(mm/s3)
    * @param [in] maxJerkDeg 角加加速度极值(deg/s3)
    * @return 错误码
    */
    int LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

关闭LIN、ARC运动FIR滤波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关闭LIN、ARC运动FIR滤波
    * @return 错误码
    */
    int LinArcFIRPlanningEnd();

FIR滤波代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFIR(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos midjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos endjointPos=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose middescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose enddescPose=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.PtpFIRPlanningStart(1000, 1000);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.PtpFIRPlanningEnd();

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        robot.MoveL(startjointPos, startdescPose, 0, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveC(midjointPos, middescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        return 0;
    }

加速度平滑开启
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief 加速度平滑开启
     * @param [in] saveFlag 是否断电保存
     * @return  错误码
     */
    public int AccSmoothStart(boolean saveFlag)

加速度平滑关闭
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief 加速度平滑关闭
     * @param [in] saveFlag 是否断电保存
     * @return  错误码
     */
    public int AccSmoothEnd(boolean saveFlag)

加速度平滑代码示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAccSmooth(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0,0,0,0,0,0);
        int rtn = robot.AccSmoothStart(false);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AccSmoothEnd(false);

        robot.CloseRPC();
        return 0;
    }

指定姿态速度开启
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 指定姿态速度开启
     * @param [in] ratio 姿态速度百分比[0-300]
     * @return  错误码
     */
    int AngularSpeedStart(int ratio)

指定姿态速度关闭
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 指定姿态速度关闭
     * @return  错误码
     */
    int AngularSpeedEnd();

机器人指定姿态速度代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

开始奇异位姿保护
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  开始奇异位姿保护
    * @param  [in]  protectMode 奇异保护模式，0：关节模式；1-笛卡尔模式
    * @param  [in]  minShoulderPos 肩奇异调整范围(mm), 默认100
    * @param  [in]  minElbowPos 肘奇异调整范围(mm), 默认50
    * @param  [in]  minWristPos 腕奇异调整范围(°), 默认10
    * @return  错误码
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇异位姿保护
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  停止奇异位姿保护
    * @return  错误码
    */
    int SingularAvoidEnd();

机器人奇异位姿保护代码示例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

清空运动指令队列
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 清空运动指令队列
    * @return 错误码
    */
    public int MotionQueueClear()

移动到相贯线起始点
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveToIntersectLineStart(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);
            
相贯线运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveIntersectLine(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos[] exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);
                
机器人相贯线运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestIntersectLineMove(Robot robot)
    {
        DescPose[] mainPoint = new DescPose[6];
        DescPose[] piecePoint = new DescPose[6];
        ExaxisPos[] mainExaxisPos = new ExaxisPos[6];
        ExaxisPos[] pieceExaxisPos = new ExaxisPos[6];
        int extAxisFlag = 1;
        ExaxisPos[] exaxisPos = new ExaxisPos[4];
        DescPose offset =new DescPose(0.0, 2.0 ,30.0, -2.0, 0.0, 0.0 );
        mainPoint[0] = new DescPose(490.004, -383.194, 402.735, -9.332, -1.528, 69.594);
        mainPoint[1] = new DescPose(444.950, -407.117, 389.011, -5.546, -2.196, 65.279);
        mainPoint[2] = new DescPose(445.168, -463.605, 355.759, -1.544, -10.886, 57.104);
        mainPoint[3] = new DescPose(507.529, -485.385, 343.013, -0.786, -4.834, 61.799);
        mainPoint[4] = new DescPose(554.390, -442.647, 367.701, -4.761, -10.181, 64.925);
        mainPoint[5] = new DescPose(532.552, -394.003, 396.467, -13.732, -13.592, 67.411);
        mainExaxisPos[0] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[1] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[2] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[3] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[4] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[5] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        piecePoint[0] = new DescPose( 505.571, -192.408, 316.759, 38.098, 37.051, 139.447);
        piecePoint[1] =new DescPose(533.837, -201.558, 332.340, 34.644, 42.339, 137.748);
        piecePoint[2] =new DescPose(530.386, -225.085, 373.808, 35.431, 45.111, 137.560);
        piecePoint[3] =new DescPose(485.646, -229.195, 383.778, 33.870, 45.173, 137.064);
        piecePoint[4] =new DescPose(460.551, -212.161, 354.256, 28.856, 45.602, 135.930);
        piecePoint[5] =new DescPose(474.217, -197.124, 324.611, 42.469, 41.133, 148.167);
        pieceExaxisPos[0] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[1] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[2] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[3] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[4] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[5] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        exaxisPos[0] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        exaxisPos[1] = new ExaxisPos(-44.994, 90.000, 0.000, 0.000);
        exaxisPos[2] = new ExaxisPos(-59.992, 0.002, 0.000, 0.000);
        exaxisPos[3] = new ExaxisPos(-44.994, -89.997, 0.000, 0.000);
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0;
        int moveType = 1;
        int moveDirection = 1;
        int  rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        System.out.printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        System.out.printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return ;
    }
                
原地空运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 原地空运动
    * @return 错误码
    */
    public int MoveStationary()

原地空运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void test_RecordandReplay(Robot robot)
    {
        int rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 1, 10, 100);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        rtn = robot.MoveStationary();
        System.out.printf("MoveStationary rtn is %d\n", rtn);
        rtn = robot.LaserSensorRecord1(0, 10);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }

定点摆动开始
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 定点摆动开始
    * @param [in] weaveNum 摆动编号[0-7]
    * @param [in] mode 0-工具坐标系；1-参考点
    * @param [in] refPoint 参考点笛卡尔坐标[x,y,z,a,b,c]
    * @param [in] weaveTime 摆动时间[s]
    * @return 错误码
    */
    public int OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime)
    
定点摆动结束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 定点摆动结束
    * @return 错误码
    */
    public int OriginPointWeaveEnd();
        
定点摆动的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOriginPointWeave(Robot robot) {
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);
        robot.MoveJ(j, 1, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        
        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();

        robot.Sleep(2000);

        robot.MoveJ(j, 1, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();

        robot.Sleep(1000);
        return 0;
    }