API说明
=========================

.. toctree:: 
   :maxdepth: 6

act 指令
-------------

以下所有act指令使用POST，URL为/action/act。

保存示教点
+++++++++++++

指令名称：save_point。 

指令参数：

.. code-block:: c++
    :linenos:

    /** 
    * @param  string name记录的示教点名称
    * @param  string speed 速度
    * @param  string elbow_speed 肘速度
    * @param  string acc加速度
    * @param  string elbow_acc 肘加速度
    * @param  string toolnum 工具号
    * @param  string workpiecenum 工件号
    */ 

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "save_point",
        data:{
            name: "point1",
            speed: "100",
            elbow_speed: "100",
            acc: "100",
            elbow_acc: "100",
            toolnum: "1",
            workpiecenum: "1"
        }
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @return status:404 "fail"
    */ 

sta 指令
-------------

以下所有sta指令使用POST，URL为/action/sta。

获取机器人状态数据
++++++++++++++++++++

指令名称：basic。 

指令参数：无。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "basic",
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 
    * @param  object joints 关节位置
    * @param  object tcp 笛卡尔位姿
    * @param  array exAxisPos 外部轴位置
    * @return status:404 "fail"
    */
    {
        joints: {
            j1: "90",
            j2: "90",
            j3: "90",
            j4: "90",
            j5: "90",
            j6: "90",
        },
        tcp: {
            x: "100",
            x: "100",
            z: "100",
            rx: "90",
            ry: "90",
            rz: "90",
        },
        exAxisPos: [0,0,0,0]
    }

get 指令
-------------

以下所有get指令使用POST，URL为/action/get。 

获取示教点
+++++++++++++

指令名称：get_points()。

指令参数：无。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "get_points"
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  ${point_name}: object 示教点相关信息
    * @return status:404 "fail"
    */ 

指令反馈案例：

.. code-block:: c++
    :linenos:

    {
        "localpoint1": {
            "name":"localpoint1",
            "elbow_speed":"1",
            "elbow_acc":"1",
            "x": "1",
            "y": "1",
            "z": "1",
            "rx": "1",
            "ry": "1",
            "rz": "1",
            "j1": "1",
            "j2": "1",
            "j3": "1",
            "j4": "1",
            "j5": "1",
            "j6": "1",
            "toolnum": "1",
            "workpiecenum": "1",
            "speed": "1",
            "acc": "1",
            "E1": "1",
            "E2: "1",
            "E3": "1",
            "E4": "1"
        }
    }


获取系统配置
+++++++++++++

指令名称：get_syscfg()。

指令参数：无。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "get_syscfg"
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  string log_count 记录最大日志天数
    * @param  string language 当前使用语言包
    * @param  string lifespan 超时时间
    * * @return status:404 "fail"
    */ 

指令反馈案例：

.. code-block:: c++
    :linenos:

    {
        log_count:"10",
        language:"zh",
        lifespan:"1800"
    }

set 指令
-------------

以下所有set指令使用POST，URL为/action/set。

下发系统变量指令
++++++++++++++++++

指令名称：511。

指令参数：

.. code-block:: c++
    :linenos:

    /** 
    * @param int index系统变量序号:1-20 
    * @param int value系统变量值 
    */ 

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: 511,
        data:{
            content:"SetSysVarValue(2,1)"
        }
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 1：代表成功，0：代表失败
    * @return status:404 "fail"
    */

指令反馈案例：

.. code-block:: c++
    :linenos:

    1

获取系统变量指令
+++++++++++++++++++

指令名称：512。

指令参数：

.. code-block:: c++
    :linenos:

    /** 
    * @param int index系统变量序号:1-20 
    * /

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: 512,
        data:{
            content:"GetSysVarValue(2)"
        }
    }

指令反馈：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200
    * @param int value系统变量值 
    * @return status:404 "fail"
    * /

指令反馈案例：

.. code-block:: c++
    :linenos:

    1

better-sqlite3指令
-----------------------

查询数据库中第一行记录
++++++++++++++++++++++

指令参数：

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 数据库名称(包含绝对路径) 
    * @param string sql sql语句
    * @return string result 查询到的第一行记录
    */

指令内容：

.. code-block:: c++
    :linenos:

    queryget(string db_name, string sql);

查询数据库中所有记录
+++++++++++++++++++++

指令参数：

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 数据库名称(包含绝对路径)
    * @param string sql sql语句
    * @return string result 查询到的所有记录
    */

指令内容：

.. code-block:: c++
    :linenos:

    queryall(string db_name, string sql);

执行数据库语句
+++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 数据库名称(包含绝对路径)
    * @param string sql sql语句
    * @param object obj sql 语句执行所需的参数
    * @return \
    */

指令参数：

.. code-block:: c++
    :linenos:

    exec(string db_name, string sql, object obj);

指令内容：

socket指令
-----------------------

socket send
++++++++++++++++++++++

指令参数：

.. code-block:: c++
    :linenos:

    /**
    * @param string send_content socket 通信指令发送内容
    * @return \
    */

指令内容：

.. code-block:: c++
    :linenos:

    socket_cmd.send(string send_content);//8065
    socket_file.send(string send_content);//8067

socket recv
+++++++++++++++++++++

指令参数：

.. code-block:: c++
    :linenos:

    /**
    * @return string recv_content socket 通信指令回复内容
    */

指令内容：

.. code-block:: c++
    :linenos:

    socket_cmd.recv();//8065
    socket_file.recv();//8067

文件操作指令
---------------------------

写入文件内容
++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param String filename文件路径
    * @param string content要写入的内容
    * @return true/false
    */

    write(filename, content);

读取文件内容
++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param String filename文件路径
    * @param string content要写入的内容
    * @return String 文件内容
    */

    read(filename);

修改文件权限
++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @param String filename文件路径
    * @param Number mode权限模式（如0644）
    * @return true/false
    */

    chmod(filename, mode);

读取目录内容，包括子目录
++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @param String path文件路径
    * @return Array 文件名数组
    */

    readdir(path);

压缩解压指令
---------------------------

.. note:: 
    区分LA与QX版本：

    LA模块导入：var execSync = require('child_process').execSync;

    QX模块导入：var tar_utils = require('/usr/local/etc/node/sys/tools/tar_utils');

创建tar.gz压缩文件
+++++++++++++++++++++++++++++++++

创建tar.gz压缩文件示例(LA)：

.. code-block:: javascript
    :linenos:
    
    var cmd = 'cd / && tar -zcvf ' + FILENAME + '-C ' + DIR;
    execSync(cmd);
    
创建tar.gz压缩文件指令描述(QX)：

.. code-block:: c++
    :linenos:
    
    /**
    * @param {Array|String} sourcePaths 源文件/目录路径数组或单个路径
    * @param String targetFile目标压缩文件路径
    * @param Function callback 回调函数，参数为(error) 
    * @param String basePath基础路径，默认为'/'
    * @return \
    */

    createTarGz(sourcePaths, targetFile, callback, basePath);

解压tar.gz文件
+++++++++++++++++++++++++++++++++

解压tar.gz文件示例(LA)：

.. code-block:: javascript
    :linenos:

    var cmd = 'cd / && tar -zxvf ' + FILENAME;
    execSync(cmd);

解压tar.gz文件指令描述(QX)：

.. code-block:: c++
    :linenos:
    
    /**
    * @param String sourceFile源压缩文件路径
    * @param String targetDir目标解压目录
    * @param Function callback 回调函数，参数为(error) 
    * @return \
    */
    extractTarGz(sourceFile, targetDir, callback);