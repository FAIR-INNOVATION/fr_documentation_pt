
CNDE功能操作
=====================

输入配置与输入数据
~~~~~~~~~~~~~~~~~~~~~~~~~

客户端通过CNDE向机器人发送数据帧对机器人DO、AO输出、输入寄存器等进行控制，在发送输入数据前，需要先配置需要控制的功能内容。表2-1为CNDE输入配置内容格式，包含配方编号及一系列输入配置功能名称（表1-2）；对应的表3-2为输入数据内容格式，包含配方编号和输入数据字节组。

CNDE数据输入支持最多8个配方，在发送输入数据时，机器人将根据收到数据中的配方编号匹配到对应的配方配置功能名称组，并解析数据得到其中每个功能名称的输入数据值，进而根据输入的数据进行机器人控制操作。

.. centered:: 表3-1 输入配置内容格式

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **配方编号**
     - **功能名称字符串**

   * - 长度(byte)
     - 1
     - --

   * - 内容
     - 0 ~ 7
     - 一系列输入数据功能名称

.. centered:: 表3-2 输入数据内容格式

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **配方编号**
     - **数据字节组**

   * - 长度(byte)
     - 1
     - --

   * - 内容
     - 0 ~ 7
     - 输入数据内容

输入配置时，机器人控制器在收到配置名称组后会对每个名称进行校验，若所配置的功能名称正确无误，则机器人会反馈用“,”分割的所有配置功能的数据类型名称；若配置的功能名称有误，则机器人会反馈相应的错误内容。输入配置数据帧(16进制)示例如下：

.. image:: cnde/001.png
   :width: 6in
   :align: center

其中配置输入功能名称组总长度为54个字节，加上输入配方编号1个字节，共55个字节，转成16进制为0x0037，在小端模式下，对应输入数据帧中的数据长度即为“37 00”。

此时机器人将反馈一条类型为字符提示消息(本文3.3.1节字符提示消息)的数据帧：

.. image:: cnde/002.png
   :width: 6in
   :align: center

消息类型“00”表示这是一条执行成功的反馈消息，客户端可以提取“输入数据配置类型”和表1-3对比，得到输入配置的字节长度，本示例中数据总长度为1*5+4*30+8*30 = 365个字节。

若输入配置名称有误：

.. image:: cnde/003.png
   :width: 6in
   :align: center

其对应的反馈信息为：

.. image:: cnde/004.png
   :width: 6in
   :align: center

输入数据可以按一定的周期循环输入，也可以仅在有需要的时候输入，循环输入时机器人可以处理的最快周期为1ms，但较快的输入周期会带来一定的机器人系统资源开销，建议您根据实际情况合理设置数据输入周期。

另外向机器人发送数据帧时，机器人不会有反馈信息，除非发送的数据帧长度或数据异常。输入数据帧示例如下，其中输入数据配方编号与输入数据字节组长度应该与输入配置相符：

.. image:: cnde/005.png
   :width: 6in
   :align: center

输出配置与输出数据
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

客户端通过CNDE获取机器人状态反馈可以根据需要自定义状态反馈内容和反馈周期，使用机器人CNDE状态反馈需要以下三个步骤：①输出配置；②启动输出；③接收输出数据。

输出配置
+++++++++++++++++++++++

输出配置帧内容包含输出周期和输出功能名称组(所有可配置名称见表1-1)，输出周期可配置范围为1 ~ 200ms，输出数据字节数最大支持4096byte。输出功能名称组为一系列用“,”分隔的输出功能名称字符串，客户端发送输出配置帧后，机器人会对配置的功能名称进行校验，若所配置的功能名称均为当前机器人CNDE支持的功能名称，则机器人反馈一系列“,”分隔的数据类型组合；否则若检验输出配置名称失败，则反馈对应的错误信息。

.. centered:: 表3-3 输出配置内容

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **输出周期(ms)**
     - **功能名称字符串**

   * - 长度(byte)
     - 2
     - --

   * - 内容
     - 1-200
     - 输出功能名称组

如输出配置帧如下：

.. image:: cnde/006.png
   :width: 6in
   :align: center

其中配置输出功能名称组总长度为48个字节，加上输出周期2个字节，共50个字节，转成16进制为0x0032，在小端模式下，对应输入数据帧中的数据长度即为“32 00”。

此时机器人将反馈一条类型为字符提示消息(本文3.3.1节字符提示消息)的数据帧：

.. image:: cnde/007.png
   :width: 6in
   :align: center

消息类型“00”表示这是一条执行成功的反馈消息，客户端可以提取“输出数据配置类型”和表1-3对比，得到输出配置的字节长度，本示例中数据总长度为1+8*10+4 = 85个字节。

若输入配置名称有误，如“queue”误写为“quene”：

.. image:: cnde/008.png
   :width: 6in
   :align: center

其对应的反馈信息为：

.. image:: cnde/009.png
   :width: 6in
   :align: center

输出启动和停止
+++++++++++++++++++++++++

机器人CNDE输出配置完成后，发送启动CNDE输出启动指令，机器人即按照配置的输出周期和输出内容进行状态反馈输出，同样发送CNDE停止输出指令，机器人将停止状态反馈输出。CNDE启动、停止指令没有指令内容，相应数据长度为0。

.. centered:: 表3-4 CNDE输出启动、停止内容

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据字节组**

   * - 长度(byte)
     - 0

   * - 内容
     - 无

启动机器人CNDE输出数据帧示例如下：

.. image:: cnde/010.png
   :width: 3in
   :align: center

客户端接收输出数据
+++++++++++++++++++++++

机器人CNDE数据输出启动后，客户端需要一个循环接收机器人反馈的数据信息，且客户端的循环接收频率要高于配置的输出数据频率，否则可能会发生数据丢包。机器人输出数据内容如表3-5；机器人输出数据字节组长度为输出配置的所有功能数据字节长度总和，字节数组为1字节对齐的按配置功能顺序的所有状态数据组合。

.. centered:: 表3-5 CNDE输出数据内容

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据字节组**

   * - 长度(byte)
     - --

   * - 内容
     - 输出数据字节组

机器人输出数据帧示例如下：

.. image:: cnde/011.png
   :width: 4in
   :align: center

CNDE辅助功能
~~~~~~~~~~~~~~~~~

字符串提示消息
++++++++++++++++++

客户端和机器人之间可以通过CNDE相互发送字符串提示消息，消息内容包括消息类型和消息字符串(表3-6)，其中消息类型定义如表3-7。当CNDE客户端向机器人发送输入配置、输出配置、输出启动、输出停止等指令时，机器人均回复一条字符提示消息。

若上述指令执行成功，则机器人反馈消息类型为“成功”，对应消息类型数值码为0x00；反之若上述指令执行失败，则机器人反馈消息类型为“错误”，对应消息类型数值为0x03，客户端可根据反馈的消息类型开判断指令执行结果，若消息类型为“错误”，则可以提取错误信息以分析错误原因。

.. centered:: 表3-6 字符串提示消息内容

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **消息类型**
     - **消息字符串**

   * - 长度(byte)
     - 1
     - --

   * - 内容
     - 0 ~ 4
     - 消息字符串

.. centered:: 表3-7 机器人CNDE字符提示消息类型

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **类型**
     - **数值**

   * - 成功
     - 0x00

   * - 信息
     - 0x01

   * - 警告
     - 0x02

   * - 错误
     - 0x03

   * - 故障
     - 0x04

切换机器人CNDE协议版本号
++++++++++++++++++++++++++++++++++++++

当前机器人CNDE仅有一个版本，版本号为“FR-CNDE-V0001”，因此本功能为预留功能，暂未开放使用。

获取机器人软固件版本信息
+++++++++++++++++++++++++++++++++++++++++

客户端通过CNDE向机器人发送获取软固件版本信息指令，指令内容为空，机器人收到请求后会反馈一条字符提示消息，消息内容包括机器人型号、机器人软件版本、机器人固件版本、机器人硬件版本等相关信息。

末端透传功能周期数据获取（CNDE）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CNDE配置描述
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

末端透传功能开启后，可在CNDE中配置"axle_gen_com_data"选项及周期，从而获取末端读取的外设的周期数据，反馈的数据帧定义如下。

.. centered:: 表3-8  末端透传功能周期数据CNDE反馈协议定义

.. list-table::
   :widths: 30 30 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Byte 1**
     - **Byte 2**
     - **Byte 3-130**

   * - ErrorCode
     - Len
     - Data

   * - 0-通信正常
     - 周期数据的长度
     - 数据帧Buffer

   * - 1-末端与机器人通信异常
     - 错误码不为0时长度清零
     - 错误码不为0时Buffer清零

   * - 2-末端485通信异常	
     - 
     - 

以倍益康艾灸头外设周期数据配置为例，代码显示配置为获取末端周期透传数据，获取周期50ms。

末端透传CNDE配置代码示意:

.. code-block:: 
    :linenos:

    tring outputCfg = "axle_gen_com_data";    //获取末端透传周期数据
    byte[] sendBuffer = new byte[] { };
    byte[] cfgBuffer = Encoding.UTF8.GetBytes(outputCfg);
    CNDEPkg pkg  = new CNDEPkg();
    pkg.type = 1;  //输出配置
    pkg.len = (ushort)(2 + outputCfg.Length);
    pkg.data.Clear();
    UInt16 period = 50;   //50ms update
    byte[] periodBt = new byte[2] {0, 0};
    Int16ToByte(period, ref periodBt);
    pkg.data.AddRange(periodBt);  //通讯周期
    pkg.data.AddRange(cfgBuffer); 
    pkg.ToBytes(ref sendBuffer);

基于CNDE的倍益康艾灸头周期数据解包代码示例:
  
.. code-block:: 
    :linenos:

    if (pkg.type == 4)
    {
        int size = Marshal.SizeOf(putDate);
        IntPtr structPtr = Marshal.AllocHGlobal(size);
        Marshal.Copy(pkg.data.ToArray(), 0, structPtr, size);
        putDate = (OUTPKG)Marshal.PtrToStructure(structPtr, typeof(OUTPKG));

        int errorcode = putDate.axle_gen_com_data[0];
        int datalen = putDate.axle_gen_com_data[1];
        // 过滤异常包
        if ((errorcode != 0) || (datalen == 0) ||
        (putDate.axle_gen_com_data[2] != 0xAB) || 
        (putDate.axle_gen_com_data[3] != 0xBA))
        {
            Console.WriteLine($"rcv data is error");
            continue;
        }
        // 按照倍益康艾灸头协议进行组包
        int curTem = putDate.axle_gen_com_data[6];
        int targetTem = putDate.axle_gen_com_data[7];
        int genData1 = putDate.axle_gen_com_data[8] << 8 | putDate.axle_gen_com_data[9];
        int genData2 = putDate.axle_gen_com_data[10] << 8 | putDate.axle_gen_com_data[11];
        int genData3 = putDate.axle_gen_com_data[12] << 8 | putDate.axle_gen_com_data[13];
        int genData4 = putDate.axle_gen_com_data[14] << 8 | putDate.axle_gen_com_data[15];
        int genData5 = putDate.axle_gen_com_data[16] << 8 | putDate.axle_gen_com_data[17];
        int genData6 = putDate.axle_gen_com_data[18] << 8 | putDate.axle_gen_com_data[19];

        Console.WriteLine($"the data is errorcode {errorcode};  datalen  {datalen}  curTem  {curTem}; targetTem  {targetTem}  genData1  {genData1}  genData2  {genData2}  genData3  {genData3}  genData4  {genData4}  genData5  {genData5}  genData6  {genData6}  ");
        udpClient.Client.ReceiveTimeout = 100;
        Marshal.FreeHGlobal(structPtr);
    }

基于末端透传功能倍益康艾灸头非周期数据通信代码示例:
  
.. code-block:: 
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

        int[] rcvdata = new int[16];
        int ret = 0;
        int cnt = 1;

        JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
        DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

        JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
        DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        //开启末端透传功能
        robot.SetAxleGenComEnable(1);
        robot.SetAxleLuaEnable(1);

        while(cnt<=10)
        { 
            //读取版本号
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            //读取艾灸头在位状态
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            //开启艾灸头激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            //关闭艾灸头激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }