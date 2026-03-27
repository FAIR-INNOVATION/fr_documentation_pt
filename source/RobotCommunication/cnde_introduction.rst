CNDE简介
==================

协作机器人可配置网络数据交换协议（以下简称CNDE）是一种客户端通过UDP通讯进行机器人控制和获取机器人反馈状态的方式。

表1-1为CNDE可以获取到的机器人所有状态集合，客户端可以从表中任意挑选若干个需要的状态，并使机器人按照设定的反馈周期进行状态反馈。

同样，客户端也可以从表1-2中挑选需要的机器人控制功能组合进行机器人控制操作。客户端和机器人CNDE通信数据需按照指定的帧格式，机器人CNDE通讯端口为20006。

使用机器人CNDE功能主要有以下四个步骤：

①输入、输出数据内容配置：客户端向机器人发送一条输入、输出配置指令，其中指令内容形如“std_DI_box,cfg_DI_box,motion_queue_len”等一系列控制或状态功能名称，机器人端记录并识别这些名称后向客户端反馈对应功能数据类型如“UINT8,UINT8,INT32”，即表示配置成功。

②启动机器人CNDE数据输出：客户端向机器人发送一条启动CNDE数据输出指令，机器人即开始按照配置的周期以字节数组(小端模式)的形式将机器人状态数据通过UDP发送至客户端。

③解析机器人状态数据：客户端循环接收机器人反馈的状态数据，并根据输出配置时机器人反馈的数据类型和表1-3中每个数据类型对应的字节长度进行数据解析，得到每个状态的实际数值。机器人CNDE输出数据最多支持4096个字节，可配置CNDE输出周期为1 ~ 200ms。

④发送机器人控制数据：客户端根据输入配置时机器人反馈的数据类型和表1-3中每个数据类型对应的字节长度进行控制数据组包，并通过UDP通讯发送到机器人，机器人端收到控制数据后进行数据解析和机器人控制操作。机器人CNDE输入支持256个配方，客户端可以根据需要先配置多个输入配方，在向机器人发送输入数据时需要指定当前数据对应的配方编号。

.. centered:: 表1-1 机器人输出配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据类型**
     - **描述**

   * - std_DI_box
     - UINT8
     - 控制箱标准DI输入(bit0 ~ bit7表示DI0 ~ DI7)

   * - cfg_DI_box
     - UINT8
     - 控制箱可配置CI输入(bit0 ~ bit7表示CI0 ~ CI7)

   * - cfg_DI_tool
     - UINT8
     - 控制箱可配置工具DI输入(bit0 ~ bit2表示toolDI0 ~ toolDI1)

   * - std_AI0_box
     - DOUBLE
     - 控制箱模拟量输入AI0(0 ~ 4095)

   * - std_AI1_box
     - DOUBLE
     - 控制箱模拟量输入AI1(0 ~ 4095)

   * - std_AI_tool
     - DOUBLE
     - 末端工具模拟量输入tool_AI0(0 ~ 4095)

   * - run_up_time
     - DOUBLE
     - 机器人开机时间统计(s)

   * - target_joint_pos
     - DOUBLE_6
     - 关节1-6目标位置(°)

   * - target_joint_vel
     - DOUBLE_6
     - 关节1-6目标速度(°/s)

   * - target_joint_acc
     - DOUBLE_6
     - 关节1-6目标加速度(°/s2)

   * - target_joint_current
     - DOUBLE_6
     - 关节1-6目标电流(A)

   * - target_joint_torque
     - DOUBLE_6
     - 关节1-6目标扭矩(Nm)

   * - actual_joint_pos
     - DOUBLE_6
     - 关节1-6当前位置(°)

   * - actual_joint_vel
     - DOUBLE_6
     - 关节1-6当前速度(°/s)

   * - actual_joint_current
     - DOUBLE_6
     - 关节1-6当前电流(A)

   * - actual_joint_torque
     - DOUBLE_6
     - 关节1-6目标扭矩(Nm)

   * - actual_TCP_pos
     - DOUBLE_6
     - 工具当前位置DKR(mm)

   * - actual_TCP_vel
     - DOUBLE_6
     - 工具当前速度DKR(mm/s)

   * - actual_TCP_force
     - DOUBLE_6
     - 工具合力DKR(N)

   * - target_TCP_pos
     - DOUBLE_6
     - 工具目标位置DKR(mm)

   * - target_TCP_vel
     - DOUBLE_6
     - 工具目标速度DKR(mm/s)

   * - std_DO_box
     - UINT8
     - 控制箱标准DO输出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO输出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool
     - UINT8
     - 控制箱标准工具DO输出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模拟量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模拟量AO1 (0.0 ~ 4095.0)

   * - std_AO_tool
     - DOUBLE
     - 工具模拟量AO1 (0.0 ~ 4095.0)

   * - robot_mode
     - UINT8
     - 机器人模式(0-自动；1-手动)

   * - collision_level
     - UINT8_6
     - 关节1-6碰撞等级(1 ~ 10)

   * - speed_scaling_man
     - DOUBLE
     - 手动模式速度百分比(0 ~ 100)

   * - speed_scaling_auto
     - DOUBLE
     - 自动模式速度百分比(0 ~ 100)

   * - program_state
     - UINT8
     - 机器人程序运行状态(1-停止；2-运动中；3-暂停；4-拖动)

   * - line_number
     - INT32
     - 当前程序运行行号

   * - payload
     - DOUBLE
     - 负载质量(kg)

   * - pay_cog
     - DOUBLE_3
     - 负载质心(x,y,z)(mm)

   * - motion_queue_len
     - INT32
     - 当前运动队列长度
   
   * - ft_sensor_data
     - DOUBLE_6
     - 力传感器原始数据

   * - main_code
     - INT32
     - 主故障码

   * - sub_code
     - INT32
     - 子故障码

   * - emergency_stop
     - UINT8
     - 急停状态

   * - motion_done
     - INT32
     - 运动完成状态

   * - timestamp_us
     - UINT64
     - 机器人系统时间(us)

   * - output_BIT_reg_8xX
     - UINT8_X
     - BIT型机器人输出寄存器(8xX表示寄存器个数，若您需要16个BIT型输出寄存器，则实际名称为：“output_BIT_reg_8x2”，机器人最多支持128个BIT型输出寄存器)

   * - output_INT_reg_X
     - INT32_X
     - INT型机器人输出寄存器(X表示寄存器个数，若您需要16个INT型输出寄存器，则实际名称为：“output_INT_reg_16”，机器人最多支持64个INT型输出寄存器)

   * - output_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型机器人输出寄存器(X表示寄存器个数，若您需要16个DOUBLE型输出寄存器，则实际名称为：“output_DOUBLE_reg_16”，机器人最多支持64个DOUBLE型输出寄存器)

   * - ft_sensor_data
     - DOUBLE_6
     - 力传感器数据

.. centered:: 表1-2 机器人输入控制配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据类型**
     - **描述**

   * - speed_mask
     - UINT8
     - 全局速度设置掩码：0-不生效；1-生效

   * - speed
     - UINT8
     - 设置全局速度（0-100）

   * - std_DO_mask
     - UINT8
     - 控制箱标准DO输出控制掩码(bit0 ~ bit7表示DO0 ~ DO7)

   * - std_DO_box
     - UINT8
     - 控制箱标准DO输出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_mask
     - UINT8
     - 控制箱可配置CO输出控制掩码(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO输出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool_mask
     - UINT8
     - 控制箱标准工具DO输出控制掩码(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - cfg_DO_tool
     - UINT8
     - 控制箱标准工具DO输出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO_mask
     - UINT8
     - 机器人模拟量输出控制掩码(bit0 ~ bit1表示控制箱AO0 ~ AO1；bit2表示工具AO0)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模拟量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模拟量AO1 (0.0 ~ 4095.0)

   * - std_AO0_tool
     - DOUBLE
     - 工具模拟量AO1 (0.0 ~ 4095.0)

   * - input_BIT_reg_8xX
     - UINT8_X
     - BIT型机器人输入寄存器(8xX表示寄存器个数，若您需要16个BIT型输入寄存器，则实际名称为：“input_BIT_reg_8x2”，机器人最多支持128个BIT型寄存器)

   * - input_INT_reg_X
     - INT32_X
     - INT型机器人输入寄存器(X表示寄存器个数，若您需要16个INT型输入寄存器，则实际名称为：“input_INT_reg_16”，机器人最多支持64个INT型寄存器)
  
   * - input_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型机器人输入寄存器(X表示寄存器个数，若您需要16个DOUBLE型输入寄存器，则实际名称为：“input_DOUBLE_reg_16”，机器人最多支持64个DOUBLE型寄存器)

.. centered:: 表1-3 数据类型及字节长度对应关系

.. list-table::
   :widths: 60 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **数据类型**
     - **字节长度**

   * - UINT8
     - 1

   * - INT32
     - 4

   * - DOUBLE
     - 8

   * - UINT8_X
     - 1*X

   * - INT32_X
     - 4*X

   * - DOUBLE_X
     - 8*X