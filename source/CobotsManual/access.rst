WebApp 访问登录
===================

.. toctree:: 
   :maxdepth: 6

访问登录WebApp界面
--------------------

1. 开启控制箱并将网线连接PC；
2. PC打开chrome浏览器访问目标网址192.168.58.2；
3. 输入用户名和密码点击登录即可登录WebApp。

初始用户名为admin，密码为123。

.. figure:: teaching_pendant_software/001.png
   :width: 6in
   :align: center

.. centered:: 图表 2.1‑1 登录界面

简单认识WebApp界面
--------------------

登录成功后系统进入“初始界面”，主要包含：

1. 法奥LOGO；
2. 菜单栏缩放按钮；
3. 菜单栏；
4. 机器人控制区
5. 机器人状态区；
6. 三维模拟机器人——三维场景操作；
7. 三维模拟机器人——机器人本体操作；
8. 机器人配套功能；
9. 机器人及配套功能状态。

如下图系统初始界面示意图所示：

.. image:: teaching_pendant_software/002.png
   :align: center
   :width: 6in

.. centered:: 图表 2.2‑1 系统初始界面示意图

控制区
~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/064.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**打开示教程序按钮**
   
   作用：打开程序编程、图形化编程和节点图编程的示教程序

.. note:: 
   .. image:: teaching_pendant_software/003.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**使能按钮**
   
   作用：使能机器人

.. note:: 
   .. image:: teaching_pendant_software/004.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**开始按钮**
   
   作用：上传并开始运行示教程序

.. note:: 
   .. image:: teaching_pendant_software/005.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**停止按钮**
   
   作用：停止当前示教程序运行

.. note:: 
   .. image:: teaching_pendant_software/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**暂停/恢复按钮**
   
   作用：暂停和恢复当前示教程序

.. important::
   暂停指令在程序的末尾，无法进行判断

状态栏
~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/011.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人运行错误状态**
   
   作用：当前机器人运行有错误，无错误时隐藏

.. note:: 
   .. image:: teaching_pendant_software/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人状态**
   
   作用：Stopped-停止，Running-运行，Pause-暂停，Drag-拖动

.. note:: 
   .. image:: teaching_pendant_software/010.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人工具坐标系、工件坐标系、扩展轴坐标系和负载编号**
   
   作用：左上——当前工具坐标系编号、右上——当前工件坐标系编号、左下——当前扩展轴坐标系编号、右下——当前负载编号

.. note:: 
   .. image:: teaching_pendant_software/009.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**运行速度百分比**
   
   作用：机器人当前模式运行时速度

.. note:: 
   .. image:: teaching_pendant_software/012.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**自动模式**
   
   作用：机器人自动运行模式，开启手动切自动模式全局速度调整并指定速度时，全局速度会自动调整为指定速度

.. note:: 
   .. image:: teaching_pendant_software/013.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**手动模式**
   
   作用：机器人手动模式，进行机器人示教操作

.. note:: 
   .. image:: teaching_pendant_software/065.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人状态折叠/展开按钮**
   
   作用：折叠/展开工具坐标系、工件坐标系、扩展轴坐标系、负载、机器人拖动状态、本地/远程模式、机器人连接状态、BOOT模式和账户信息内容

点击折叠按钮，查看以下状态信息内容。

.. note:: 
   .. image:: teaching_pendant_software/008.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**工具坐标系编号**
   
   作用：展示当前应用的工具坐标系编号

.. note:: 
   .. image:: teaching_pendant_software/027.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**工件坐标系编号**
   
   作用：展示当前应用的工件坐标系编号
   
.. note:: 
   .. image:: teaching_pendant_software/028.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**扩展轴坐标系编号**
   
   作用：展示当前应用的扩展轴坐标系编号

.. note:: 
   .. image:: teaching_pendant_software/066.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**负载**
   
   作用：展示当前应用的负载重量和质心坐标X、Y、Z

.. note:: 
   .. image:: teaching_pendant_software/014.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人拖动状态**
   
   作用：当前机器人可拖动

.. note:: 
   .. image:: teaching_pendant_software/015.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人拖动状态**
   
   作用：当前机器人不可拖动

.. note:: 
   .. image:: teaching_pendant_software/068.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人本地模式**
   
   作用：当前机器人通过控制箱控制

.. note:: 
   .. image:: teaching_pendant_software/067.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**机器人远程模式**
   
   作用：当前机器人只能通过PLC控制

.. note:: 
   .. image:: teaching_pendant_software/017.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**连接状态**
   
   作用：机器人已连接

.. note:: 
   .. image:: teaching_pendant_software/016.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**未连接状态**
   
   作用：机器人未连接

.. note:: 
   .. image:: teaching_pendant_software/018.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**账户信息**
   
   作用：显示用户名和权限及登出用户
