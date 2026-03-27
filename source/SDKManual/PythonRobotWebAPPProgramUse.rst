机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadDefaultProgConfig(flag,program_name)``"
    "描述", "设置开机自动加载默认的作业程序"
    "必选参数", "- ``flag``：1-开机自动加载默认程序，0-不自动加载默认程序
    - ``program_name``：作业程序名及路径，如“/fruser/movej.lua”，其中/fruser/为QX固定路径，/usr/local/etc/controller/lua/为LA固定路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

加载指定的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramLoad(program_name)``"
    "描述", "加载指定的作业程序"
    "必选参数", "- ``program_name``：作业程序名及路径，如“/fruser/movej.lua”，其中/fruser/为QX固定路径，/usr/local/etc/controller/lua/为LA固定路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取已加载的作业程序名
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLoadedProgram()``"
    "描述", "获取已加载的作业程序名"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``program_name``：已加载的作业程序名"

获取当前机器人作业程序的执行行号
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurrentLine()``"
    "描述", "获取当前机器人作业程序的执行行号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``line_num``：当前机器人作业程序的执行行号"

运行当前加载的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramRun()``"
    "描述", "运行当前加载的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

暂停当前运行的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramPause()``"
    "描述", "暂停当前运行的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

恢复当前暂停的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramResume()``"
    "描述", "恢复当前暂停的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

终止当前运行的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "终止当前运行的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取机器人作业程序执行状态
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetProgramState()``"
    "描述", "获取机器人作业程序执行状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``:机器人作业程序执行状态，1-程序停止或无程序运行，2-程序运行中，3-程序暂停"

机器人LUA程序操作代码示例
++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    program_name = "/fruser/test0610.lua"
    loaded_name = ""
    state = 0
    line = 0
    robot.Mode(0)
    robot.LoadDefaultProgConfig(0, program_name)
    robot.ProgramLoad(program_name)
    robot.ProgramRun()
    time.sleep(1)
    robot.ProgramPause()
    error,state = robot.GetProgramState()
    print(f"program state:{state}")
    error,line = robot.GetCurrentLine()
    print(f"current line:{line}")
    error,loaded_name = robot.GetLoadedProgram()
    print(f"program name:{loaded_name}")
    time.sleep(1)
    robot.ProgramResume()
    time.sleep(1)
    robot.ProgramStop()
    time.sleep(1)
    robot.CloseRPC()

下载Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LuaDownLoad(fileName, savePath)``"
    "描述", "下载Lua文件"
    "必选参数", "- ``fileName``：要下载的lua文件名 如“test.lua”
    - ``savePath``：保存文件本地路径 如“D://Down/”"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

删除Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaDelete(fileName)``"
    "描述", "删除Lua文件"
    "必选参数", "- ``fileName``：要删除的lua文件名“test.lua”"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取当前所有lua文件名称
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLuaList()``"
    "描述", "获取当前所有lua文件名称"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``lua_num``：lua文件数量
    - ``luaNames``：lua文件名列表"

上传Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaUpload(filePath)``"
    "描述", "上传Lua文件"
    "必选参数", "- ``filePath``：上传文件的全路径名  如D://test/test.lua"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - errorStr(lua文件存在错误返回)"

机器人LUA文件上传下载代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn,lua_num,luaNames = robot.GetLuaList()
    print(f"res is:{rtn}")
    print(f"size is:{lua_num}")
    for name in luaNames:
        print(name)
    rtn = robot.LuaDownLoad("test0610.lua", "D://zDOWN/")
    print(f"LuaDownLoad rtn is:{rtn}")
    rtn = robot.LuaUpload("D://zDOWN/test0610.lua")
    print(f"LuaUpload rtn is:{rtn}")
    rtn = robot.LuaDelete("test0610.lua")
    print(f"LuaDelete rtn is:{rtn}")
    robot.CloseRPC()
    