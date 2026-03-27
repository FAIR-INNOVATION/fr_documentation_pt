CNDE数据帧协议格式
=========================

协作机器人CNDE通讯协议如下，客户端向机器人发送数据及机器人向客户端反馈数据均需要遵循该协议；协议通过帧类型区分不同功能的数据帧，帧类型定义见表2-2；不同类型帧对应不用的数据内容，具体数据内容定义见表3-1 ~ 表3-7。

.. centered:: 表2-1 机器人CNDE数据帧格式

.. list-table::
   :widths: 20 20 20 20 20 20 20
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **帧头**
     - **帧计数**
     - **帧类型**
     - **数据长度**
     - **内容**
     - **帧尾**
   
   * - **长度(byte)**
     - 2
     - 1
     - 1
     - 2
     - --
     - 2
   
   * - **内容**
     - 0x5A5A
     - 0 ~ 255
     - 0 ~ 8
     - “数据内容”的字节个数
     - 数据帧内容
     - 0xA5A5

.. centered:: 表2-2 机器人CNDE数据帧类型

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **类型**
     - **数值**
     - **数据帧方向**

   * - 输入配置帧（控制配置）
     - 0x00
     - Client->Robot

   * - 输出配置帧（状态配置）
     - 0x01
     - Client->Robot

   * - CNDE输出启动
     - 0x02
     - Client->Robot

   * - CNDE输出停止
     - 0x03
     - Client->Robot

   * - 输出数据帧（状态数据）
     - 0x04
     - Robot->Client

   * - 输入数据帧（控制数据）
     - 0x05
     - Client->Robot

   * - 字符提示消息
     - 0x06
     - Client->Robot, Robot->Client

   * - 设置机器人CNDE协议版本号
     - 0x07
     - Client->Robot

   * - 获取机器人软固件版本
     - 0x08
     - Client->Robot, Robot->Client