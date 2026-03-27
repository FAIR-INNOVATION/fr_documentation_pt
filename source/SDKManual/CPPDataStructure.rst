数据结构说明
================

.. toctree:: 
    :maxdepth: 5

接口调用返回值类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    typedef  int errno_t;

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节位置数据类型
    */
    typedef  struct
    {
        double jPos[6];   /* 六个关节位置，单位deg */
    }JointPos;

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    typedef struct
    {
        double x;    /* x轴坐标，单位mm  */
        double y;    /* y轴坐标，单位mm  */
        double z;    /* z轴坐标，单位mm  */
    } DescTran;

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    typedef struct
    {
        double rx;   /* 绕固定轴X旋转角度，单位：deg  */
        double ry;   /* 绕固定轴Y旋转角度，单位：deg  */
        double rz;   /* 绕固定轴Z旋转角度，单位：deg  */
    } Rpy;

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    typedef struct
    {
        DescTran tran;      /* 笛卡尔空间位置  */
        Rpy rpy;            /* 笛卡尔空间姿态  */
    } DescPose;

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
    */
    typedef  struct
    {
        double ePos[4];   /* 四个扩展轴位置，单位mm */
    }ExaxisPos;

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    typedef struct
    {
        double fx;  /* 沿x轴受力分量，单位N  */
        double fy;  /* 沿y轴受力分量，单位N  */
        double fz;  /* 沿z轴受力分量，单位N  */
        double tx;  /* 绕x轴力矩分量，单位Nm */
        double ty;  /* 绕y轴力矩分量，单位Nm */
        double tz;  /* 绕z轴力矩分量，单位Nm */
    } ForceTorque;

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  螺旋参数数据类型
    */
    typedef  struct
    {
        int    circle_num;           /* 螺旋圈数  */
        float  circle_angle;         /* 螺旋倾角  */
        float  rad_init;             /* 螺旋初始半径，单位mm  */
        float  rad_add;              /* 半径增量  */
        float  rotaxis_add;          /* 转轴方向增量  */
        int rot_direction;   /* 旋转方向，0-顺时针，1-逆时针  */
        int velAccMode;      /* 速度加速度参数模式：0-角速度恒定；1-线速度恒定 */
    }SpiralParam;

控制器状态反馈数据包
+++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  控制器状态反馈数据包
     */
    typedef struct _ROBOT_STATE_PKG
    {
        uint16_t frame_head;      // 帧头，约定为0x5A5A 
        uint8_t  frame_cnt;       // 帧计数，循环计数0-255 
        uint16_t data_len;        // 数据内容的长度 
        uint8_t  program_state;   // 程序运行状态，1-停止；2-运行；3-暂停；
        uint8_t  robot_state;     // 机器人运动状态，1-停止；2-运行；3-暂停；4-拖动 
        int      main_code;       // 主故障码 
        int      sub_code;        // 子故障码 
        uint8_t  robot_mode;      // 机器人模式，1-手动模式；0-自动模式； 
        double   jt_cur_pos[6];   // 6个轴当前关节位置，单位deg 
        double   tl_cur_pos[6];   // 工具当前位置
                                  // tl_cur_pos[0]，沿x轴位置，单位mm，
                                  // tl_cur_pos[1]，沿y轴位置，单位mm，
                                  // tl_cur_pos[2]，沿z轴位置，单位mm，
                                  // tl_cur_pos[3]，绕固定轴X旋转角度，单位deg
                                  // tl_cur_pos[4]，绕固定轴y旋转角度，单位deg
                                  // tl_cur_pos[5]，绕固定轴z旋转角度，单位deg 
        double   flange_cur_pos[6]; // 末端法兰当前位置
                                    // flange_cur_pos[0]，沿x轴位置，单位mm，
                                    // flange_cur_pos[1]，沿y轴位置，单位mm，
                                    // flange_cur_pos[2]，沿z轴位置，单位mm，
                                  // flange_cur_pos[3]，绕固定轴X旋转角度，单位deg
                                  // flange_cur_pos[4]，绕固定轴y旋转角度，单位deg
                                  // flange_cur_pos[5]，绕固定轴z旋转角度，单位deg
        double   actual_qd[6];      // 当前6个关节速度，单位deg/s 
        double   actual_qdd[6];     // 当前6个关节加速度，单位deg/s^2 
        double   target_TCP_CmpSpeed[2]; 
    // target_TCP_CmpSpeed[0]，TCP合成指令速度(位置)，单位mm/s
                     // target_TCP_CmpSpeed[1]，TCP合成指令速度(姿态)，单位deg/s  */
        double   target_TCP_Speed[6];    // TCP指令速度
                         // target_TCP_Speed[0]，沿x轴速度，单位mm/s，
                         // target_TCP_Speed[1]，沿y轴速度，单位mm/s，
                         // target_TCP_Speed[2]，沿z轴速度，单位mm/s，
                         // target_TCP_Speed[3]，绕固定轴X旋转角速度，单位deg/s
                         // target_TCP_Speed[4]，绕固定轴y旋转角速度，单位deg/s
                         // target_TCP_Speed[5]，绕固定轴z旋转角速度，单位deg/s */
        double   actual_TCP_CmpSpeed[2]; 
    // actual_TCP_CmpSpeed[0]，TCP合成实际速度(位置)，单位mm/s
                  // actual_TCP_CmpSpeed[1]，TCP合成实际速度(姿态)，单位deg/s 
        double   actual_TCP_Speed[6];    // TCP实际速度
                        // actual_TCP_Speed[0]，沿x轴速度，单位mm/s，
                        // actual_TCP_Speed[1]，沿y轴速度，单位mm/s，
                        // actual_TCP_Speed[2]，沿z轴速度，单位mm/s，
                        // actual_TCP_Speed[3]，绕固定轴X旋转角速度，单位deg/s
                        // actual_TCP_Speed[4]，绕固定轴y旋转角速度，单位deg/s
                        // actual_TCP_Speed[5]，绕固定轴z旋转角速度，单位deg/s 
        double   jt_cur_tor[6];      // 6个轴当前扭矩，单位N·m 
        int      tool;               // 应用的工具坐标系编号 
        int      user;               // 应用的工件坐标系编号 
        uint8_t  cl_dgt_output_h;    // 控制箱数字量IO输出15-8 
        uint8_t  cl_dgt_output_l;    // 控制箱数字量IO输出7-0 
        uint8_t  tl_dgt_output_l;    // 工具数字量IO输出7-0，仅bit0-bit1有效 
        uint8_t  cl_dgt_input_h;     // 控制箱数字量IO输入15-8 
        uint8_t  cl_dgt_input_l;     // 控制箱数字量IO输入7-0 
        uint8_t  tl_dgt_input_l;     // 工具数字量IO输入7-0，仅bit0-bit1有效 
        uint16_t cl_analog_input[2]; // cl_analog_input[0]，控制箱模拟量输入0
                                     //cl_analog_input[1]，控制箱模拟量输入1 
        uint16_t tl_anglog_input;    // 工具模拟量输入 
        double   ft_sensor_raw_data[6]; // 力矩传感器原始数据
                                      // ft_sensor_raw_data[0]，沿x轴力，单位N
                                      // ft_sensor_raw_data[1]，沿y轴力，单位N
                                      // ft_sensor_raw_data[2]，沿z轴力，单位N
                                      // ft_sensor_raw_data[3]，沿x轴力矩，单位Nm
                                      // ft_sensor_raw_data[4]，沿y轴力矩，单位Nm
                                      // ft_sensor_raw_data[5]，沿z轴力矩，单位Nm 
        double   ft_sensor_data[6];     // 力矩传感器数据，
                                        // ft_sensor_data[0]，沿x轴力，单位N
                                        // ft_sensor_data[1]，沿y轴力，单位N
                                        // ft_sensor_data[2]，沿z轴力，单位N
                                        // ft_sensor_data[3]，沿x轴力矩，单位Nm
                                        // ft_sensor_data[4]，沿y轴力矩，单位Nm
                                        // ft_sensor_data[5]，沿z轴力矩，单位Nm 
        uint8_t  ft_sensor_active;   // 力矩传感器激活状态，0-复位，1-激活 
        uint8_t  EmergencyStop;      // 急停标志，0-急停未按下，1-急停按下 
        int      motion_done;        // 运动到位信号，1-到位，0-未到位 
        uint8_t  gripper_motiondone; // 夹爪运动完成信号，1-完成，0-未完成 
        int      mc_queue_len;       // 运动指令队列长度 
        uint8_t  collisionState;     // 碰撞检测，1-碰撞，0-无碰撞 
        int      trajectory_pnum;    // 轨迹点编号 
        uint8_t  safety_stop0_state; // 安全停止信号SI0 
        uint8_t  safety_stop1_state; // 安全停止信号SI1 
        uint8_t  gripper_fault_id;   // 错误夹爪号 
        uint16_t gripper_fault;      // 夹爪故障 
        uint16_t gripper_active;     // 夹爪激活状态 
        uint8_t  gripper_position;   // 夹爪位置 
        int8_t   gripper_speed;      // 夹爪速度 
        int8_t   gripper_current;    // 夹爪电流 
        int      gripper_temp;       // 夹爪温度 
        int      gripper_voltage;    // 夹爪电压 
        robot_aux_state aux_state;   // 485扩展轴状态
        EXT_AXIS_STATUS extAxisStatus[4];  // UDP扩展轴状态 
        uint16_t extDIState[8];        // 扩展DI输入
        uint16_t extDOState[8];        // 扩展DO输出
        uint16_t extAIState[4];        // 扩展AI输入
        uint16_t extAOState[4];        // 扩展AO输出
        int rbtEnableState;            // 机器人使能状态
        double   jointDriverTorque[6];        //机器人关节驱动器扭矩
        double   jointDriverTemperature[6];   //机器人关节驱动器温度
        RobotTime robotTime;           // 机器人系统时间
        int softwareUpgradeState;      // 机器人软件升级状态
        uint16_t endLuaErrCode;        // 末端LUA运行状态
        uint16_t cl_analog_output[2];  // 控制箱模拟量输出
        uint16_t tl_analog_output;     // 工具模拟量输出
        float gripperRotNum;           // 旋转夹爪当前旋转圈数
        uint8_t gripperRotSpeed;       // 旋转夹爪当前旋转速度百分比
        uint8_t gripperRotTorque;      // 旋转夹爪当前旋转力矩百分比
        WELDING_BREAKOFF_STATE weldingBreakOffState;  //焊接中断状态
        double jt_tgt_tor[6];                 // 关节指令力矩
        int smartToolState;                   // SmartTool手柄按钮状态
        float wideVoltageCtrlBoxTemp;         //宽电压控制箱温度
        uint16_t wideVoltageCtrlBoxFanCurrent;//宽电压控制箱风扇电流(mA)
        double toolCoord[6];        //工具坐标系
        double wobjCoord[6];        //工件坐标系
        double extoolCoord[6];      //外部工具坐标系
        double exAxisCoord[6];      //扩展轴坐标系
        double load;                //负载质量
        double loadCog[3];          //负载质心
        double lastServoTarget[6];  //队列中最后一个ServoJ目标位置
        int servoJCmdNum;           //servoJ指令计数
        uint16_t check_sum;         // 和校验
    }ROBOT_STATE_PKG;