前言
++++++++++
fairino_hardware为法奥协作机器人基于ROS2开发的API接口，旨在针对入门级用户更便捷的使用法奥SDK。通过参数配置文件对默认参数的配置，即可适应不同的客户要求。 

fairino_hardware
++++++++++++++++++++++++++++
本章节说明APP运行环境如何配置。

基本环境安装
--------------

推荐在Ubuntu22.04LTS(Jammy)上使用，系统安装完毕后，需要安装ROS2，推荐用ros2-humble，全部的ROS2的安装可以参考教程：https://docs.ros.org/en/humble/index.html。
在正式编译fairino_hardware前，还需要安装官方ros2_control包，全部的ros2_control安装可以参考教程：https://control.ros.org/humble/index.html。官方提供两种ros2_control安装方式，分别为指令安装方式和源码编译安装方式，由于指令安装方式可能会导致功能包安装不全，故推荐使用源码编译安装方式。

下面对ROS2(humble)的过程详细阐述：

1.打开shell窗口

.. code-block:: shell
    :linenos:

    locale  # check for UTF-8

    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    locale  # verify settings

2.设置源

.. code-block:: shell
    :linenos:
    
    sudo apt install software-properties-common
    sudo add-apt-repository universe

    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

3.安装ROS2

.. code-block:: shell
    :linenos:

    sudo apt update
    sudo apt upgrade
    sudo apt install ros-humble-desktop

4.最后安装dev工具

.. code-block:: shell
    :linenos:

    sudo apt install ros-dev-tools

下面对ros2_control的安装过程详细阐述：

1.首先source ROS2的资源

.. code-block:: shell
    :linenos:

    source /opt/ros/humble/setup.bash

2.创建ros2_control工作空间，下载资源

.. code-block:: shell
    :linenos:

    mkdir -p ~/ros2_control_ws/src
    cd ~/ros2_control_ws/
    wget https://raw.githubusercontent.com/ros-controls/ros2_control_ci/master/ros_controls.$ROS_DISTRO.repos
    vcs import src < ros_controls.$ROS_DISTRO.repos

3.安装依赖包

.. code-block:: shell
    :linenos:

    rosdep update --rosdistro=$ROS_DISTRO
    sudo apt-get update
    rosdep install --from-paths src --ignore-src -r -y

4.编译ros2_control

.. code-block:: shell
    :linenos:

    . /opt/ros/${ROS_DISTRO}/setup.sh
    colcon build --symlink-install




编译及构建fairino_hardware
------------------------------------------
1. 创建colcon工作区
fairino_hardware有两个功能包组成，一个是自定义数据结构的功能包fairino_msgs，另外一个是程序主体fairino_hardware功能包。在安装好基本环境后，先创建一个colcon工作区，比如:

首先必须source ROS2和ros2_control的资源

.. code-block:: shell
    :linenos:

    source /opt/ros/humble/setup.bash
    source ~/ros2_control_ws/install/setup.bash

然后再创建工作区

.. code-block:: shell
    :linenos:

    cd ~/
    mkdir -p ros2_ws/src

2. 编译功能包
将安装包的代码拷贝至ros2_ws/src目录下，那么在ros2_ws目录下运行如下命令：

.. code-block:: shell
    :linenos:

    source ~/ros2_control_ws/install/setup.bash

待指令完成之后，运行以下指令：

.. code-block:: shell
    :linenos:

    colcon build --packages-select fairino_msgs

等待上一条命令完成编译后，再使用以下指令编译fairino_hardware:

.. code-block::  shell
    :linenos:

    colcon build --packages-select fairino_hardware

快速开始
++++++++++++++

启动流程
-----------------
在Ubuntu下打开命令行，输入：

.. code-block::  shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    ros2 run fairino_hardware ros2_cmd_server

.. image:: img/fr_ros2_001.png
    :width: 6in
    :align: center

查看机械臂状态反馈流程
--------------------------
机械臂的状态反馈是通过topic发布的，用户可以通过ros2自带的命令观察到状态数据刷新，也可以编写程序获取该数据，下面展示如何通过ros2命令观察机械臂状态数据。

在ubuntu下打开命令行，输入：

.. code-block:: shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    ros2 topic echo /nonrt_state_data

可以看到命令行窗口中不断刷新的状态数据，如下图所示。

.. image:: img/fr_ros2_002.png
    :width: 6in
    :align: center

下发指令流程
--------------------------
在ubuntu下打开命令行，输入：

.. code-block:: shell
    :linenos:

    cd ros2_ws
    source install/setup.bash
    rqt

以上命令执行完毕后，会调出一个rqt GUI界面，如下图所示。

.. image:: img/fr_ros2_003.png
    :width: 6in
    :align: center

在GUI界面选择plugins->serivce->serivce caller，调出如下界面，选择/fairino_remote_command_service这项，在界面expression中输入指令字符串点击call即可看到下方对话框中跳出回复信息。

.. image:: img/fr_ros2_004.png
    :width: 6in
    :align: center

.. important:: 

   - 输入字符串规则说明：

   程序内部对输入的字符串形式进行了筛选，函数输入的格式必须是 [函数名]() 这样的形式，且圆括号的参数字符串必须是由字母，数字，逗号还有负号组成，出现其他字符或者空格均会报错。

   - 指令反馈值说明：

   除了GET指令会反馈一串字符串，其余的函数反馈值都是int型，一般0为出现错误，1为正确执行，如果出现其他的值那么参考xmlrpc SDK中定义的错误代码对应的错误。

修改参数流程
--------------------------
由于简化SDK是改进自原生的SDK接口，能够简化是因为赋予了一些参数默认值，而在实际使用过程中也会遇到默认参数无法满足要求的情况，这个时候可以通过修改对应默认参数的数值，然后加载到节点中。

源代码文件中存在一个fairino_remotecmdinterface_para.yaml参数文件，文件中的参数为预先设置的默认参数，用于简化指令输入参数，可以根据自己的具体需要修改其中的参数，然后使用命令动态修改参数: ros2 param load fr_command_server ~/ros2_ws/src/fairino_hardware/fairino_remotecmdinterface_para.yaml。

API说明
++++++++++++++

.. code-block:: c++
    :linenos:

    /*
    函数功能描述:存储一个关节点位信息
    id - 存储点位id号,从1开始,注意该id与CARTPoint的点位id号各自独立
    double j1-j6 - 6个关节位置,单位是度
    */
    int JNTPoint(int id, double j1, double j2, double j3, double j4, double j5, double j6)
    // 例子
    JNTPoint(1,10,11,12,13,14,15)

    /*
    函数功能描述:存储一个笛卡尔点位信息
    id - 存储点位id号,从1开始,注意该id与JNTPoint的点位id号各自独立
    double x,y,z,rx,ry,yz - 笛卡尔点位信息,位置单位是mm,角度单位是度
    */
    int CARTPoint(int id, double x,y,z,rx,ry,rz)//存储一个笛卡尔空间点位
    // 例子
    CARTPoint(1,100,110,200,0,0,0)

    /*
    函数功能描述:获取指定序号点的关节或者笛卡尔位置信息
    string name - 'JNT'或者'CART',JNT代表获取关节点位信息,'CART'代表获取笛卡尔点位信息
    int id - 点位id,从1开始
    */
    string GET(string name, int id)//获取对应id序号点位的内容,name可以输入JNT或者CART
    // 例子
    GET(JNT,1)

    /*
    函数功能描述:拖动模式开关
    uint8_t state - 1-打开拖动模式,0-关闭拖动模式
    */
    int DragTeachSwitch(uint8_t state)
    // 例子
    DragTeachSwitch(0)

    /*
    函数功能描述:机械臂使能开关
    uint8_t state - 1-机械臂使能,0-机械臂去使能
    */
    int RobotEnable(uint8_t state)
    // 例子
    RobotEnable(1)

    /*
    函数功能描述:模式切换
    uint8_t state - 1-手动模式,0-自动模式
    */
    int Mode(uint8_t state)
    // 例子
    Mode(1)

    /*
    函数功能描述:设置当前模式下机械臂速度
    float vel - 速度百分比,范围为1-100
    */
    int SetSpeed(float vel)
    // 例子
    SetSpeed(10)

    /*
    函数功能描述:设置并加载指定序号的工具坐标系
    int id - 工具坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 工具坐标系的偏移量信息
    */
    int SetToolCoord(int id, float x,float y, float z,float rx,float ry,float rz)
    // 例子
    SetToolCoord(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置工具坐标系列表
    int id - 工具坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 工具坐标系的偏移量信息
    */
    int SetToolList(int id, float x,float y, float z,float rx,float ry,float rz );
    // 例子
    SetToolList(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置外部工具坐标系
    int id - 工具坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 外部工具坐标系的偏移量信息
    */
    int SetExToolCoord(int id, float x,float y, float z,float rx,float ry,float rz);	
    // 例子
    SetExToolCoord(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置外部工具坐标系列表
    int id - 工具坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 外部工具坐标系的偏移量信息
    */
    int SetExToolList(int id, float x,float y, float z,float rx,float ry,float rz);
    // 例子
    SetExToolList(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置工件坐标系
    int id - 工件坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 工件坐标系的偏移量信息
    */
    int SetWObjCoord(int id, float x,float y, float z,float rx,float ry,float rz);
    // 例子
    SetWObjCoord(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置工件坐标系列表
    int id - 工件坐标系编号,范围1-15
    float x,y,z,rx,ry,rz - 工件坐标系的偏移量信息
    */
    int SetWObjList(int id, float x,float y, float z,float rx,float ry,float rz);
    // 例子
    SetWObjList(1,0,0,0,0,0,0)

    /*
    函数功能描述:设置末端负载重量
    float weight - 负载重量,单位kg
    */
    int SetLoadWeight(float weight);
    // 例子
    SetLoadWeight(3.5)

    /*
    函数功能描述:设置末端负载质心坐标
    float x,y,z - 质心坐标,单位为mm
    */
    int SetLoadCoord(float x,float y,float z);
    // 例子
    SetLoadCoord(10,20,30)

    /*
    函数功能描述:设置机器人安装方式
    uint8_t install - 安装方式,0-正装,1-侧装,2-倒装
    */
    int SetRobotInstallPos(uint8_t install);
    // 例子
    SetRobotInstallPos(0)

    /*
    函数功能描述:设置机器人安装角度,自由安装
    double yangle - 倾斜角
    double zangle - 旋转角
    */
    int SetRobotInstallAngle(double yangle,double zangle);
    // 例子
    SetRobotInstallAngle(90,0)


    //安全配置
    /*
    函数功能描述:设置机器人碰撞等级
    float level1-level6 - 1-6轴的碰撞等级,范围是1-10
    */
    int SetAnticollision(float level1, float level2, float level3, float level4, float level5, folat level6);
    // 例子
    SetAnticollision(1,1,1,1,1,1)

    /*
	 * @brief  设置碰撞后策略
	 * @param  [in] strategy  0-报错停止，1-继续运行
	 * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
	 * @param  [in] safeDistance  安全停止距离[1-150]mm
	 * @param  [in] safeVel 安全速度[50-250] mm/s
	 * @param  [in] safetyMargin  j1-j6安全系数[1-10]
	 * @return  错误码
    */
	int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel, int safetyMargin[])
    // 例子
    SetCollisionStrategy(1)

    /*
	 * @brief 设置机器人碰撞检测方法
	 * @param [in] method 碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
     * @param [in] thresholdMode 碰撞等级阈值方式；0-碰撞等级固定阈值方式；1-自定义碰撞检测阈值
	 * @return  错误码
    */
	int SetCollisionDetectionMethod(int method, int thresholdMode);
    // 例子
    SetCollisionDetectionMethod(0,0)


    /*
	 * @brief 设置静态下碰撞检测开始关闭
	 * @param  [in] status 0-关闭；1-开启
	 * @return  错误码
    */
	int SetStaticCollisionOnOff(int status);
    // 例子
    SetStaticCollisionOnOff(1)



    /*
	 * @brief 关节扭矩功率检测
	 * @param  [in] status 0-关闭；1-开启
	 * @param  [in] power 设定最大功率(W);
	 * @return  错误码
    */
	int SetPowerLimit(int status, double power);
    //例子
    SetPowerLimit(1,100)

    /*
	 * @brief  配置力传感器
	 * @param  [in] company  力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯，23-NBIT，24-鑫精诚(XJC)，26-NSR
	 * @param  [in] device  设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精诚XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)
	 * @param  [in] softvesion  软件版本号，暂不使用，默认为0
	 * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
	 * @return  错误码
    */
	int FT_SetConfig(int company, int device, int softvesion, int bus);
    // 例子
    FT_SetConfig(0,1,0,0)



    /*
	 * @brief  获取力传感器配置
	 * @param  [out] company  力传感器厂商，待定
	 * @param  [out] device  设备号，暂不使用，默认为0
	 * @param  [out] softvesion  软件版本号，暂不使用，默认为0
	 * @param  [out] bus 设备挂在末端总线位置，暂不使用，默认为0
	 * @return  错误码
    */
	int FT_GetConfig(int *company, int *device, int *softvesion, int *bus);
    // 例子
    FT_GetConfig()


    /*
	 * @brief  力传感器激活
	 * @param  [in] act  0-复位，1-激活
	 * @return  错误码
    */
	int FT_Activate(uint8_t act);
    // 例子
    FT_Activate(1)


    /*
	 * @brief  力传感器校零
	 * @param  [in] act  0-去除零点，1-零点矫正
	 * @return  错误码
    */
	int FT_SetZero(uint8_t act);
    // 例子
    FT_SetZero(1)

    /*
	 * @brief  碰撞守护
	 * @param  [in] flag 0-关闭碰撞守护，1-开启碰撞守护
	 * @param  [in] sensor_id 力传感器编号
	 * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
	 * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
	 * @param  [in] max_threshold 最大阈值
	 * @param  [in] min_threshold 最小阈值
	 * @note   力/扭矩检测范围：(ft-min_threshold, ft+max_threshold)
	 * @return  错误码
    */
	int FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]);
    // 例子
    FT_Guard(1,1,0,0,1,0,0,0,0,0,100,0,0,0,0,0,200,0,0,0,0,0,50,0,0,0)


    /*
	 * @brief  恒力控制
	 * @param  [in] flag 0-关闭恒力控制，1-开启恒力控制
	 * @param  [in] sensor_id 力传感器编号
	 * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
	 * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
	 * @param  [in] ft_pid 力pid参数，力矩pid参数
	 * @param  [in] adj_sign 自适应启停控制，0-关闭，1-开启
	 * @param  [in] ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
	 * @param  [in] max_dis 最大调整距离，单位mm
	 * @param  [in] max_ang 最大调整角度，单位deg
	 * @param  [in] filter_Sign 滤波开启标志 0-关；1-开，默认关闭
     * @param  [in] posAdapt_sign 姿态顺应开启标志 0-关；1-开，默认关闭
     * @param  [in] isNoBlock 阻塞标志，0-阻塞；1-非阻塞
	 * @return  错误码
    */
	int FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float ft_pid[6], uint8_t adj_sign, uint8_t ILC_sign, float max_dis, float max_ang, int filter_Sign = 0, int posAdapt_sign = 0, int isNoBlock = 0);
    // 例子
    FT_Control(1,1,0,0,1,0,0,0,0,0,-10,0,0,0,0.0005,0,0,0,0,0,0,0,100,10,0,0,0) 


    /*
	 * @brief  柔顺控制开启
	 * @param  [in] p 位置调节系数或柔顺系数
	 * @param  [in] force 柔顺开启力阈值，单位N
	 * @return  错误码
    */
	int FT_ComplianceStart(float p, float force);
    // 例子
    FT_ComplianceStart(0.005,20)


    /**
	 * @brief  柔顺控制关闭
	 * @return  错误码
    */
	int FT_ComplianceStop();
    // 例子
    FT_ComplianceStop()

    /*
    函数功能描述:设置正限位,注意设置值必须在硬限位范围内
    float limit1-limit6 - 6个关节限位值
    */
    int SetLimitPositive(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
    // 例子
    SetLimitPositve(100,90,90,90,90,90)

    /*
    函数功能描述:设置负限位,注意设置值必须在硬限位范围内
    float limit1-limit6 - 6个关节限位值
    */
    int SetLimitNegative(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
    // 例子
    SetLimitNegative(-100,-90,-90,-90,-90,-90)

    /*
    函数功能描述:错误状态清除
    */
    int ResetAllError();

    /*
    函数功能描述:关节摩擦力补偿开关
    uint8_t state - 0-关, 1-开
    */
    int FrictionCompensationOnOff(uint8_t state);
    // 例子
    FrictionCompensationOnOff(1)

    /*
    函数功能描述:设置关节摩擦力补偿系数-正装
    float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
    */
    int SetFrictionValue_level(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // 例子
    SetFrictionValue_level(1,1,1,1,1,1)

    /*
    函数功能描述:设置关节摩擦力补偿系数-侧装
    float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
    */
    int SetFrictionValue_wall(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // 例子
    SetFrictionValue_wall(0.5,0.5,0.5,0.5,0.5,0.5)

    /*
    函数功能描述:设置关节摩擦力补偿系数-倒装
    float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
    */
    int SetFrictionValue_ceiling(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
    // 例子
    SetFrictionValue_ceiling(0.5,0.5,0.5,0.5,0.5,0.5)


    //外设控制
    /*
    函数功能描述:激活夹爪
    int index - 夹爪编号
    uint8_t act - 0-复位, 1-激活
    */
    int ActGripper(int index,uint8_t act);
    // 例子
    ActGripper(1,1)

    /*
    函数功能描述:控制夹爪
    int index - 夹爪编号
    int pos - 位置百分比,范围0-100
    */
    int MoveGripper(int index,int pos);
    // 例子
    MoveGripper(1,10)


    //IO控制
    /*
    函数功能描述:设置控制箱数字量输出
    int id - io编号,范围0-15
    uint_t status - 0-关, 1-开
    */
    int SetDO(int id,uint8_t status);
    // 例子
    SetDO(1,1)

    /*
    函数功能描述:设置工具数字量输出
    int id - io编号,范围0-1
    uint_t status - 0-关, 1-开
    */
    int SetToolDO(int id,uint8_t status);
    // 例子
    SetToolDO(0,1)

    /*
    函数功能描述:设置控制箱模拟量输出
    int id - io编号,范围0-1
    float vlaue - 电流或者电压值百分比,范围0-100
    */
    int SetAO(int id,float value);
    // 例子
    SetAO(1,100)

    /*
    函数功能描述:设置工具模拟量输出
    int id - io编号,范围0
    float vlaue - 电流或者电压值百分比,范围0-100
    */
    int SetToolAO(int id,float value);
    // 例子
    SetToolAO(0,100)


    //运动指令
    /*
    函数功能描述:机器人点动
    uint8_t ref - 0-关节点动, 2-基坐标系下点动, 4-工具坐标系下点动, 8-工件坐标系下点动
    uint8_t nb - 1-关节1(或x轴),2-关节2(或y轴),3-关节3(或z轴),4-关节4(或绕x轴旋转),5-关节5(或绕y轴旋转),6-关节6(或绕z轴旋转)
    uint8_t dir - 0-负方向, 1-正方向
    float vel - 速度百分比, 范围为0-100
    */
    int StartJOG(uint8_t ref, uin8_t nb, uint8_t dir, float vel);
    // 例子
    StartJOG(1,1,1,10)

    /*
    函数功能描述:机器人点动停止
    uint8_t ref - 0-关节点动停止, 2-基坐标系下点动停止, 4-工具坐标系下点动停止, 8-工件坐标系下点动停止
    */
    int StopJOG(uint8_t ref);
    // 例子
    StopJOG(1)

    /*
    函数功能描述:机器人点动立即停止
    */
    int ImmStopJOG();

    /*
    函数功能描述:关节空间运动
    string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveJ指令支持输入关节点位或者笛卡尔点位。需要注意的,MoveJ指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
    float vel - 指令速度百分比,范围0-100
    int tool - 工具坐标系序号
    int user - 工件坐标系序号
    double expos1 - 外部轴1的位置
    double expos2 - 外部轴2的位置
    double expos3 - 外部轴3的位置
    double expos4 - 外部轴4的位置
    */
    int MoveJ(string point_name, float vel,int tool, int user,double expos1,double expos2,double expos3,double expos4);//point_name是输入预存点位信息,
    // 例子
    MoveJ(JNT1,10,1,1,0,0,0,0)

    /*
    函数功能描述:笛卡尔空间直线运动
    string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveL指令支持输入关节点位或者笛卡尔点位。需要注意的,MoveL指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
    float vel - 指令速度百分比,范围0-100
    int tool - 工具坐标系序号
    int user - 工件坐标系序号
    double expos1 - 外部轴1的位置
    double expos2 - 外部轴2的位置
    double expos3 - 外部轴3的位置
    double expos4 - 外部轴4的位置
    */
    int MoveL(string point_name,float vel,int tool,int user,double expos1,double expos2,double expos3,double expos4);
    // 例子
    MoveL(CART1,10,1,1,0,0,0,0)

    /*
    函数功能描述:笛卡尔空间圆弧运动
    string point1_name point2_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveC指令支持输入关节点位或者笛卡尔点位,但是两个点位必须同类型的,即不支持第一个点位输入关节空间点位,第二个点位输入笛卡尔点位。需要注意的,MoveC指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
    float vel - 指令速度百分比,范围0-100
    int tool - 工具坐标系序号
    int user - 工件坐标系序号
    double expos1 - 点1的外部轴1的位置
    double expos2 - 点1的外部轴2的位置
    double expos3 - 点1的外部轴3的位置
    double expos4 - 点1的外部轴4的位置
    double expos1 - 点2的外部轴1的位置
    double expos2 - 点2的外部轴2的位置
    double expos3 - 点2的外部轴3的位置
    double expos4 - 点2的外部轴4的位置
    */
    int MoveC(string point1_name,string point2_name, float vel, int tool,int user,double expos1,double expos2,double expos3,double expos4,double expos1,double expos2,double expos3,double expos4);
    // 例子
    MoveC(JNT1,JNT2,10,1,1,0,0,0,0,0,0,0,0)

    /*
    函数功能描述:样条运动开始
    */
    int SplineStart();

    /*
    函数功能描述:关节空间样条运动,该指令只支持输入JNT1这样的关节数据,输入笛卡尔点位会报错
    string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位。
    float vel - 速度百分比,范围0-100
    */
    int SplinePTP(string point_name, float vel);
    // 例子
    SplinePTP(JNT2,10)

    /*
    函数功能描述:样条运动结束
    */
    int SplineEnd();

    /*
    函数功能描述:笛卡尔空间样条运动开始
    uint8_t ctlpoint - 0-轨迹经过路径点, 1-轨迹不经过控制点,至少4个点
    */
    int NewSplineStart(uint8_t ctlpoint);
    // 例子
    NewSplineStrart(1)

    /*
    函数功能描述:笛卡尔空间样条运动,只能输入CART1这样的笛卡尔空间点位,输入关节空间点位会报错
    string point_name - 预存点位名称,比如CART1就是笛卡尔空间点位信息序号为1的点位。
    float vel - 速度百分比,范围0-100
    int lastflag - 0-不是最后一个点, 1-是最后一个点
    */
    int NewSplinePoint(string point_name, float vel, int lastflag);
    // 例子
    NewSplinePoint(JNT2,20,0)

    /*
    函数功能描述:笛卡尔空间样条运动结束
    */
    int NewSplineEnd();

    /*
    函数功能描述:停止运动
    */
    int StopMotion();

    /*
    函数功能描述:点位整体偏移开始
    int flag - 0-基坐标系下/工件坐标系下偏移, 2-工具坐标系下偏移
    double x,y,z,rx,ry,rz - 偏移位姿量
    */
    int PointsOffsetEnable(int flag,double x,double y,double z,double rx,double ry,double rz);
    // 例子
    PointsOffsetEnable(1,10,10,10,0,0,0)

    /*
    函数功能描述:点位整体偏移结束
    */
    int PointsOffsetDisable();
