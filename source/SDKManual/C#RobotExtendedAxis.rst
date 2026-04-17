Eixos Extensores
===========================

.. toctree:: 
    :maxdepth: 5

Configurar Parâmetros do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Configurar parâmetros do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] servoCompany Fabricante do servo driver, 1-Dynatect
    * @param [in] servoModel Modelo do servo driver, 1-FD100-750C
    * @param [in] servoSoftVersion Versão do software do servo driver, 1-V1.0
    * @param [in] servoResolution Resolução do codificador
    * @param [in] axisMechTransRatio Relação de transmissão mecânica
    * @return Código de erro
    */
    int AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

Obter Parâmetros de Configuração do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter parâmetros de configuração do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [out] servoCompany Fabricante do servo driver, 1-Dynatect
    * @param [out] servoModel Modelo do servo driver, 1-FD100-750C
    * @param [out] servoSoftVersion Versão do software do servo driver, 1-V1.0
    * @param [out] servoResolution Resolução do codificador
    * @param [out] axisMechTransRatio Relação de transmissão mecânica
    * @return Código de erro
    */
    int AuxServoGetParam(int servoId, ref int servoCompany, ref int servoModel, ref int servoSoftVersion, ref int servoResolution, ref double axisMechTransRatio);

Habilitar/Desabilitar Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Habilitar/Desabilitar eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] status Estado de habilitação, 0-desabilitar, 1-habilitar
    * @return Código de erro
    */
    int AuxServoEnable(int servoId, int status);

Definir Modo de Controle do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir modo de controle do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] mode Modo de controle, 0-modo posição, 1-modo velocidade
    * @return Código de erro
    */
    int AuxServoSetControlMode(int servoId, int mode);

Definir Posição Alvo do Eixo Extensor 485 (Modo Posição)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir posição alvo do eixo extensor 485 (modo posição)
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] pos Posição alvo, mm ou °
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @return Código de erro
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed);

Definir Velocidade Alvo do Eixo Extensor 485 (Modo Velocidade)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir velocidade alvo do eixo extensor 485 (modo velocidade)
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @return Código de erro
    */
    int AuxServoSetTargetSpeed(int servoId, double speed);

Definir Torque Alvo do Eixo Extensor 485 (Modo Torque) -- Temporariamente não disponível
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir torque alvo do eixo extensor 485 (modo torque) -- Temporariamente não disponível
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] torque Torque alvo, Nm
    * @return Código de erro
    */
    int AuxServoSetTargetTorque(int servoId, double torque);

Definir Homing do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir homing do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [in] mode Modo de homing, 1-homing na posição atual; 2-homing no limite negativo; 3-homing no limite positivo
    * @param [in] searchVel Velocidade de busca do zero, mm/s ou °/s
    * @param [in] latchVel Velocidade de fixação, mm/s ou °/s
    * @return Código de erro
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

Limpar Informações de Erro do Eixo Extensor 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Limpar informações de erro do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @return Código de erro
    */
    int AuxServoClearError(int servoId);

Obter Status do Servo do Eixo Extensor 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Obter status do servo do eixo extensor 485
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @param [out] servoErrCode Código de falha do servo driver
    * @param [out] servoState Estado do servo driver  bit0:0-desabilitado; 1-habilitado;  bit1:0-parado; 1-em movimento;  bit2 0-limite positivo não acionado; 1-limite positivo acionado; bit3 0-limite negativo não acionado; 1-limite negativo acionado; bit4 0-posicionamento não concluído; 1-posicionamento concluído;  bit5: 0-homing não concluído; 1-homing concluído
    * @param [out] servoPos Posição atual do servo mm ou °
    * @param [out] servoSpeed Velocidade atual do servo mm/s ou °/s
    * @param [out] servoTorque Torque atual do servo Nm
    * @return Código de erro
    */
    int AuxServoGetStatus(int servoId, ref int servoErrCode, ref int servoState, ref double servoPos, ref double servoSpeed, ref double servoTorque);

Definir Número do Eixo de Dados do Eixo Extensor 485 no Feedback de Estado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Definir número do eixo de dados do eixo extensor 485 no feedback de estado
    * @param [in] servoId ID do servo driver, intervalo [1-15], correspondente ao ID do escravo
    * @return Código de erro
    */
    int AuxServosetStatusID(int servoId);

Definir Aceleração/Desaceleração de Movimento do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: C#
    :linenos:

    /**
    * @brief Definir aceleração/desaceleração de movimento do eixo extensor 485
    * @param [in] acc Aceleração do movimento do eixo extensor 485
    * @param [in] dec Desaceleração do movimento do eixo extensor 485
    * @return   Código de erro
    */
    int AuxServoSetAcc(double acc, double dec);

Definir Aceleração/Desaceleração de Parada de Emergência do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: C#
    :linenos:

    /**
    * @brief Definir aceleração/desaceleração de parada de emergência do eixo extensor 485
    * @param [in] acc Aceleração da parada de emergência do eixo extensor 485
    * @param [in] dec Desaceleração da parada de emergência do eixo extensor 485
    * @return   Código de erro
    */
    int AuxServoSetEmergencyStopAcc(double acc, double dec);

Obter Aceleração/Desaceleração de Movimento do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: C#
    :linenos:

    /**
    * @brief Obter aceleração/desaceleração de movimento do eixo extensor 485
    * @param [out] acc Aceleração do movimento do eixo extensor 485
    * @param [out] dec Desaceleração do movimento do eixo extensor 485
    * @return   Código de erro
    */
    int AuxServoGetAcc(ref double acc, ref double dec);

Obter Aceleração/Desaceleração de Parada de Emergência do Eixo Extensor 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: C#
    :linenos:

    /**
    * @brief Obter aceleração/desaceleração de parada de emergência do eixo extensor 485
    * @param [out] acc Aceleração da parada de emergência do eixo extensor 485
    * @param [out] dec Desaceleração da parada de emergência do eixo extensor 485
    * @return   Código de erro
    */
    int AuxServoGetEmergencyStopAcc(ref double acc, ref double dec);

Exemplo de Código de Controle do Eixo Extensor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:

    private void button64_Click(object sender, EventArgs e)
    {
        int retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45);
        Console.WriteLine($"AuxServoSetParam is: {retval}");

        int servoCompany = 0;
        int servoModel = 0;
        int servoSoftVersion = 0;
        int servoResolution = 0;
        double axisMechTransRatio = 0;
        retval = robot.AuxServoGetParam(1, ref servoCompany, ref servoModel, ref servoSoftVersion, ref servoResolution, ref axisMechTransRatio);
        Console.WriteLine($"servoCompany {servoCompany}\n" +
            $"servoModel {servoModel}\n" +
            $"servoSoftVersion {servoSoftVersion}\n" +
            $"servoResolution {servoResolution}\n" +
            $"axisMechTransRatio {axisMechTransRatio}\n");

        retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14);
        Console.WriteLine($"AuxServoSetParam is: {retval}");

        retval = robot.AuxServoGetParam(1, ref servoCompany, ref servoModel, ref servoSoftVersion, ref servoResolution, ref axisMechTransRatio);
        Console.WriteLine($"servoCompany {servoCompany}\n" +
            $"servoModel {servoModel}\n" +
            $"servoSoftVersion {servoSoftVersion}\n" +
            $"servoResolution {servoResolution}\n" +
            $"axisMechTransRatio {axisMechTransRatio}\n");

        retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);
        Console.WriteLine($"AuxServoSetParam is: {retval}");
        Thread.Sleep(3000);

        robot.AuxServoSetAcc(3000, 3000);
        robot.AuxServoSetEmergencyStopAcc(5000, 5000);
        Thread.Sleep(1000);
        double emagacc = 0, acc = 0;
        double emagdec = 0, dec = 0;
        robot.AuxServoGetEmergencyStopAcc(ref emagacc, ref emagdec);
        Console.WriteLine($"emergency acc is {emagacc}  dec is {emagdec}");
        robot.AuxServoGetAcc(ref acc, ref dec);
        Console.WriteLine($"acc is {acc}  dec is {dec}");

        robot.AuxServoSetControlMode(1, 0);
        Thread.Sleep(2000);

        retval = robot.AuxServoEnable(1, 0);
        Console.WriteLine($"AuxServoEnable disenable {retval}");
        Thread.Sleep(1000);
        int servoerrcode = 0;
        int servoErrCode = 0;
        int servoState = 0;
        double servoPos = 0;
        double servoSpeed = 0;
        double servoTorque = 0;
        retval = robot.AuxServoGetStatus(1, ref servoErrCode, ref servoState, ref servoPos, ref servoSpeed, ref servoTorque);
        Console.WriteLine($"AuxServoGetStatus servoState {servoState}");
        Thread.Sleep(1000);

        retval = robot.AuxServoEnable(1, 1);
        Console.WriteLine($"AuxServoEnable enable {retval}");
        Thread.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, ref servoErrCode, ref servoState, ref servoPos, ref servoSpeed, ref servoTorque);
        Console.WriteLine($"AuxServoGetStatus servoState {servoState}");
        Thread.Sleep(1000);

        retval = robot.AuxServoHoming(1, 1, 5, 1);
        Console.WriteLine($"AuxServoHoming {retval}");
        Thread.Sleep(3000);

        retval = robot.AuxServoSetTargetPos(1, 200, 30);
        Console.WriteLine($"AuxServoSetTargetPos {retval}");
        Thread.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, ref servoErrCode, ref servoState, ref servoPos, ref servoSpeed, ref servoTorque);
        Console.WriteLine($"AuxServoGetStatus servoSpeed {servoSpeed}");
        Thread.Sleep(8000);

        robot.AuxServoSetControlMode(1, 1);
        Thread.Sleep(2000);

        robot.AuxServoEnable(1, 0);
        Thread.Sleep(1000);
        robot.AuxServoEnable(1, 1);
        Thread.Sleep(1000);
        robot.AuxServoSetTargetSpeed(1, 100, 80);

        Thread.Sleep(5000);
        robot.AuxServoSetTargetSpeed(1, 0, 80);
    }

Configurar Parâmetros de Comunicação UDP do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:

    /**
    * @brief Configurar parâmetros de comunicação UDP do eixo extensor
    * @param [in] ip Endereço IP do PLC
    * @param [in] port Número da porta
    * @param [in] period Período de comunicação (ms, padrão é 2, não modifique este parâmetro)
    * @param [in] lossPkgTime Tempo de detecção de perda de pacotes (ms)
    * @param [in] lossPkgNum Número de perdas de pacotes
    * @param [in] disconnectTime Duração para confirmar desconexão da comunicação
    * @param [in] reconnectEnable Habilitar reconexão automática em caso de desconexão 0-desabilitar 1-habilitar
    * @param [in] reconnectPeriod Intervalo do período de reconexão (ms)
    * @param [in] reconnectNum Número de tentativas de reconexão
    * @param [in] selfConnect Estabelecer conexão automaticamente após reinicialização por falta de energia; 0-não estabelecer; 1-estabelecer
    * @return Código de erro
    */
    int ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum, int selfConnect);

Obter Parâmetros de Configuração de Comunicação UDP do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Obter parâmetros de comunicação UDP do eixo extensor
    * @param [out] ip Endereço IP do PLC
    * @param [out] port Número da porta
    * @param [out] period Período de comunicação (ms, padrão é 2, não modifique este parâmetro)
    * @param [out] lossPkgTime Tempo de detecção de perda de pacotes (ms)
    * @param [out] lossPkgNum Número de perdas de pacotes
    * @param [out] disconnectTime Duração para confirmar desconexão da comunicação
    * @param [out] reconnectEnable Habilitar reconexão automática em caso de desconexão 0-desabilitar 1-habilitar
    * @param [out] reconnectPeriod Intervalo do período de reconexão (ms)
    * @param [out] reconnectNum Número de tentativas de reconexão
    * @param [out] selfConnect Reconectar automaticamente após reiniciar a caixa de controle; 0-não reconectar; 1-reconectar
    * @return Código de erro
    */
    public int ExtDevGetUDPComParam(ref string ip, ref int port, ref int period, ref int lossPkgTime, ref int lossPkgNum, ref int disconnectTime, ref int reconnectEnable, ref int reconnectPeriod, ref int reconnectNum, ref int selfConnect)

Carregar Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Carregar comunicação UDP
    * @return Código de erro
    */
    int ExtDevLoadUDPDriver();

Descarregar Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Descarregar comunicação UDP
    * @return Código de erro
    */
    int ExtDevUnloadUDPDriver();

Restaurar Conexão Após Desconexão Anormal da Comunicação UDP do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Restaurar conexão após desconexão anormal da comunicação UDP do eixo extensor
    * @return Código de erro
    */
    int ExtDevUDPClientComReset();

Fechar Comunicação Após Desconexão Anormal da Comunicação UDP do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Fechar comunicação após desconexão anormal da comunicação UDP do eixo extensor
    * @return Código de erro
    */
    int ExtDevUDPClientComClose();

Configurar Parâmetros do Eixo Extensor UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Configurar parâmetros do eixo extensor UDP
    * @param [in] axisID Número do eixo
    * @param [in] axisType Tipo de eixo extensor 0-translação; 1-rotação
    * @param [in] axisDirection Direção do eixo extensor 0-positiva; 1-negativa
    * @param [in] axisMax Posição máxima do eixo extensor mm
    * @param [in] axisMin Posição mínima do eixo extensor mm
    * @param [in] axisVel Velocidade mm/s
    * @param [in] axisAcc Aceleração mm/s2
    * @param [in] axisLead Passo mm
    * @param [in] encResolution Resolução do codificador
    * @param [in] axisOffect Deslocamento do eixo extensor no ponto de início da solda
    * @param [in] axisCompany Fabricante do driver 1-Hokuyo; 2-Inovance; 3-Panasonic
    * @param [in] axisModel Modelo do driver 1-Hokuyo-SV-XD3EA040L-E, 2-Hokuyo-SV-X2EA150A-A, 1-Inovance-SV620PT5R4I, 1-Panasonic-MADLN15SG, 2-Panasonic-MSDLN25SG, 3-Panasonic-MCDLN35SG
    * @param [in] axisEncType Tipo de codificador 0-incremental; 1-absoluto
    * @return Código de erro
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

Definir Posição de Instalação do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir posição de instalação do eixo extensor
    * @param [in] installType 0-robô instalado no eixo externo, 1-robô instalado fora do eixo externo
    * @return Código de erro
    */
    int SetRobotPosToAxis(int installType);

Definir Configuração de Parâmetros DH do Sistema do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir configuração de parâmetros DH do sistema do eixo extensor
    * @param [in]  axisConfig Configuração do eixo externo, 0-trilho deslizante linear 1 DOF, 1-posicionador L de 2 DOF, 2-3 DOF, 3-4 DOF, 4-posicionador de 1 DOF
    * @param [in]  axisDHd1 Parâmetro DH do eixo externo d1 mm
    * @param [in]  axisDHd2 Parâmetro DH do eixo externo d2 mm
    * @param [in]  axisDHd3 Parâmetro DH do eixo externo d3 mm
    * @param [in]  axisDHd4 Parâmetro DH do eixo externo d4 mm
    * @param [in]  axisDHa1 Parâmetro DH do eixo externo a1 mm
    * @param [in]  axisDHa2 Parâmetro DH do eixo externo a2 mm
    * @param [in]  axisDHa3 Parâmetro DH do eixo externo a3 mm
    * @param [in]  axisDHa4 Parâmetro DH do eixo externo a4 mm
    * @return Código de erro
    */
    int SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

Habilitar Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Habilitar eixo extensor UDP
    * @param [in] axisID Número do eixo[1-4]
    * @param [in] status 0-desabilitar; 1-habilitar
    * @return Código de erro
    */
    int ExtAxisServoOn(int axisID, int status);

Homing do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Homing do eixo extensor UDP
    * @param [in] axisID Número do eixo[1-4]
    * @param [in] mode Modo de homing 0-homing na posição atual, 1-homing no limite negativo, 2-homing no limite positivo
    * @param [in] searchVel Velocidade de busca do zero (mm/s)
    * @param [in] latchVel Velocidade de fixação do zero (mm/s)
    * @return Código de erro
    */
    int ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

Iniciar Jog do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Iniciar jog do eixo extensor UDP
    * @param [in] axisID Número do eixo[1-4]
    * @param [in] direction Direção de rotação 0-reversa; 1-direta
    * @param [in] vel Velocidade (mm/s)
    * @param [in] acc Aceleração (mm/s2)
    * @param [in] maxDistance Distância máxima de jog
    * @return Código de erro
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);

Parar Jog do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Parar jog do eixo extensor UDP
    * @param [in] axisID Número do eixo[1-4]
    * @return Código de erro
    */
    int ExtAxisStopJog(int axisID);

Exemplo de Código de Configuração e Jog do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void btnJog_Click(object sender, EventArgs e)
    {
        int rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5,1);
        Console.WriteLine("ExtDevSetUDPComParam rtn is " + rtn);
        string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        rtn = robot.ExtDevGetUDPComParam(ref ip, ref port, ref period, ref lossPkgTime, ref lossPkgNum, ref disconnectTime, ref reconnectEnable, ref reconnectPeriod, ref reconnectNum);
        string param = "\nip " + ip + "\nport " + port.ToString() + "\nperiod  " + period.ToString() + "\nlossPkgTime " + lossPkgTime.ToString() + "\nlossPkgNum  " + lossPkgNum.ToString() + "\ndisConntime  " + disconnectTime.ToString() + "\nreconnecable  " + reconnectEnable.ToString() + "\nreconnperiod  " + reconnectPeriod.ToString() + "\nreconnnun  " + reconnectNum.ToString();
        Console.WriteLine("ExtDevGetUDPComParam rtn is " + rtn + param);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        Console.WriteLine("ExtAxisServoOn axis id 1 rtn is " + rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        Console.WriteLine("ExtAxisServoOn axis id 2 rtn is " + rtn);
        Thread.Sleep(2000);

        rtn = robot.ExtAxisSetHoming(1, 0, 10, 2);
        Console.WriteLine("ExtAxisSetHoming 1 rtnn is  " + rtn);
        Thread.Sleep(2000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
        Console.WriteLine("ExtAxisSetHoming 2 rtnn is  " + rtn);

        Thread.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        Console.WriteLine("SetRobotPosToAxis rtn is " + rtn);
        rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
        Console.WriteLine("SetAxisDHParaConfig rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905f, 262144, 200, 1, 0, 0);
        Console.WriteLine("ExtAxisParamConfig axis 1 rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444f, 262144, 200, 1, 0, 0);
        Console.WriteLine("ExtAxisParamConfig axis 2 rtn is " + rtn);

        Thread.Sleep(3000);
        robot.ExtAxisStartJog(1, 0, 10, 10, 30);
        Thread.Sleep(1000);
        robot.ExtAxisStopJog(1);
        Thread.Sleep(3000);
        robot.ExtAxisServoOn(1, 0);

        Thread.Sleep(3000);
        robot.ExtAxisStartJog(2, 0, 10, 10, 30);
        Thread.Sleep(1000);
        robot.ExtAxisStopJog(2);
        Thread.Sleep(3000);
        robot.ExtAxisServoOn(2, 0);
        Thread.Sleep(3000);
        robot.ExtDevUnloadUDPDriver();
    }

Definir Ponto de Referência do Sistema de Coordenadas do Eixo Extensor - Método dos Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir ponto de referência do sistema de coordenadas do eixo extensor - método dos quatro pontos
    * @param [in]  pointNum Número do ponto[1-4]
    * @return Código de erro
    */
    int ExtAxisSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Eixo Extensor - Método dos Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Calcular sistema de coordenadas do eixo extensor - método dos quatro pontos
    * @param [out]  coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    int ExtAxisComputeECoordSys(DescPose& coord);

Aplicar Sistema de Coordenadas do Eixo Extensor
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Aplicar sistema de coordenadas do eixo extensor
    * @param [in]  applyAxisId ID do eixo extensor a ser aplicado bit0-bit3 correspondem aos números dos eixos extensores 1-4, por exemplo, aplicar eixos extensores 1 e 3, então é 0b 0000 0101; ou seja, 5
    * @param [in]  axisCoordNum Número do sistema de coordenadas do eixo extensor
    * @param [in]  coord Valor do sistema de coordenadas
    * @param [in]  calibFlag Flag de calibração 0-não, 1-sim
    * @return Código de erro
    */
    int ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

Definir Pose do Ponto de Referência de Calibração no Sistema de Coordenadas da Extremidade do Posicionador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir pose do ponto de referência de calibração no sistema de coordenadas da extremidade do posicionador
    * @param [in] pos Valor da pose
    * @return Código de erro
    */
    int SetRefPointInExAxisEnd(DescPose pos);

Definir Ponto de Referência do Sistema de Coordenadas do Posicionador
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir ponto de referência do sistema de coordenadas do posicionador
    * @param [in]  pointNum Número do ponto[1-4]
    * @return Código de erro
    */
    int PositionorSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Posicionador - Método dos Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Calcular sistema de coordenadas do posicionador - método dos quatro pontos
    * @param [out] coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    int PositionorComputeECoordSys(DescPose& coord);

Obter Sistema de Coordenadas do Eixo Extensor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:

    /**
    * @brief Obter sistema de coordenadas do eixo extensor
    * @param [out] coord Sistema de coordenadas do eixo extensor
    * @return Código de erro
    */
    int ExtAxisGetCoord(ref DescPose coord);

Exemplo de Código de Calibração do Sistema de Coordenadas do Eixo Extensor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:

    private void button66_Click(object sender, EventArgs e)
    {
        int rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5,1);
        Console.WriteLine("ExtDevSetUDPComParam rtn is " + rtn);
        string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        rtn = robot.ExtDevGetUDPComParam(ref ip, ref port, ref period, ref lossPkgTime, ref lossPkgNum, ref disconnectTime, ref reconnectEnable, ref reconnectPeriod, ref reconnectNum);
        string param = "\nip " + ip + "\nport " + port.ToString() + "\nperiod  " + period.ToString() + "\nlossPkgTime " + lossPkgTime.ToString() + "\nlossPkgNum  " + lossPkgNum.ToString() + "\ndisConntime  " + disconnectTime.ToString() + "\nreconnecable  " + reconnectEnable.ToString() + "\nreconnperiod  " + reconnectPeriod.ToString() + "\nreconnnun  " + reconnectNum.ToString();
        Console.WriteLine("ExtDevGetUDPComParam rtn is " + rtn + param);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        Console.WriteLine("ExtAxisServoOn axis id 1 rtn is " + rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        Console.WriteLine("ExtAxisServoOn axis id 2 rtn is " + rtn);
        Thread.Sleep(2000);

        robot.ExtAxisSetHoming(1, 0, 10, 2);
        Thread.Sleep(2000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
        Console.WriteLine("ExtAxisSetHoming rtnn is  " + rtn);

        Thread.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        Console.WriteLine("SetRobotPosToAxis rtn is " + rtn);
        rtn = robot.SetAxisDHParaConfig(1, 128.5f, 206.4f, 0, 0, 0, 0, 0, 0);
        Console.WriteLine("SetAxisDHParaConfig rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905f, 262144, 200, 1, 0, 0);
        Console.WriteLine("ExtAxisParamConfig axis 1 rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444f, 262144, 200, 1, 0, 0);
        Console.WriteLine("ExtAxisParamConfig axis 1 rtn is " + rtn);

        DescPose toolCoord = new DescPose(0, 0, 210, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);

        JointPos jSafe = new JointPos(115.193f, -96.149f, 92.489f, -87.068f, -89.15f, -83.488f);
        JointPos j1 = new JointPos(117.559f, -92.624f, 100.329f, -96.909f, -94.057f, -83.488f);
        JointPos j2 = new JointPos(112.239f, -90.096f, 99.282f, -95.909f, -89.824f, -83.488f);
        JointPos j3 = new JointPos(110.839f, -83.473f, 93.166f, -89.22f, -90.499f, -83.487f);
        JointPos j4 = new JointPos(107.935f, -83.572f, 95.424f, -92.873f, -87.933f, -83.488f);

        DescPose descSafe = new DescPose();
        DescPose desc1 = new DescPose();
        DescPose desc2 = new DescPose();
        DescPose desc3 = new DescPose();
        DescPose desc4 = new DescPose();
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin( jSafe,  ref descSafe);
        robot.MoveJ( jSafe,  descSafe, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        Thread.Sleep(2000);

        robot.GetForwardKin( j1, ref desc1);
        robot.MoveJ( j1,  desc1, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        Thread.Sleep(2000);

        DescPose actualTCPPos = new DescPose();
        robot.GetActualTCPPose(0, ref actualTCPPos);
        robot.SetRefPointInExAxisEnd(actualTCPPos);
        rtn = robot.PositionorSetRefPoint(1);
        Console.WriteLine("PositionorSetRefPoint 1 rtn is " + rtn);
        Thread.Sleep(2000);

        robot.MoveJ( jSafe,  descSafe, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.GetForwardKin( j2, ref desc2);
        rtn = robot.MoveJ( j2,  desc2, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.PositionorSetRefPoint(2);
        Console.WriteLine("PositionorSetRefPoint 2 rtn is " + rtn);
        Thread.Sleep(2000);

        robot.MoveJ( jSafe,  descSafe, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.GetForwardKin( j3, ref desc3);
        robot.MoveJ( j3,  desc3, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.PositionorSetRefPoint(3);
        Console.WriteLine("PositionorSetRefPoint 3 rtn is " + rtn);
        Thread.Sleep(2000);

        robot.MoveJ( jSafe,  descSafe, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        Thread.Sleep(1000);
        robot.GetForwardKin(j4, ref desc4);
        robot.MoveJ(j4, desc4, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(4);
        Console.WriteLine("PositionorSetRefPoint 4 rtn is " + rtn);
        Thread.Sleep(2000);

        DescPose axisCoord = new DescPose();
        robot.PositionorComputeECoordSys(ref axisCoord);
        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        Console.WriteLine("PositionorComputeECoordSys rtn is {0} {1} {2} {3} {4} {5}", axisCoord.tran.x, axisCoord.tran.y, axisCoord.tran.z, axisCoord.rpy.rx, axisCoord.rpy.ry, axisCoord.rpy.rz);
        rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1);
        Console.WriteLine("ExtAxisActiveECoordSys rtn is " + rtn);
    }

Movimento do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4

.. code-block:: C#
    :linenos:

    /**
    * @brief Movimento do eixo extensor UDP
    * @param [in] pos Posição alvo
    * @param [in] ovl Percentual de velocidade
    * @param [in] blend Parâmetro de suavização (mm ou ms)
    * @return Código de erro
    */
    int ExtAxisMove(ExaxisPos pos, double ovl, double blend=-1);

Exemplo de Código de Movimento do Eixo Extensor UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void button66_Click(object sender, EventArgs e)
    {
        ExaxisPos axisPos;
        axisPos.ePos[0] = 20;
        axisPos.ePos[1] = 0;
        axisPos.ePos[2] = 0;
        axisPos.ePos[3] = 0;
        robot.ExtAxisMove(axisPos, 50);
    }

Movimento Síncrono do Eixo Extensor UDP com Movimento de Junta do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Movimento síncrono do eixo extensor UDP com movimento de junta do robô
    * @param [in] joint_pos Posição de junta alvo, unidade deg
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] epos Posição do eixo extensor, unidade mm
    * @param [in] blendT [-1.0]-movimento até o fim (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), unidade ms
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Quantidade de deslocamento da pose
    * @return  Código de erro
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void btnSyncMoveJ_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        //1. Calibre e aplique o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são as seguintes:
        //    int SetToolPoint(int point_num);  //Definir ponto de referência da ferramenta - método de seis pontos
        //    int ComputeTool(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta
        //    int SetTcp4RefPoint(int point_num);    //Definir ponto de referência da ferramenta - método de quatro pontos
        //    int ComputeTcp4(ref DescPose tcp_pose);   //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //Definir e aplicar sistema de coordenadas da ferramenta
        //    int SetToolList(int id, DescPose coord, int type, int install);   //Definir e aplicar lista de sistemas de coordenadas da ferramenta

        //2. Defina os parâmetros de comunicação UDP e carregue a comunicação UDP
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3. Defina os parâmetros do eixo extensor, incluindo o tipo de eixo extensor, parâmetros do driver do eixo extensor, parâmetros DH do eixo extensor
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1);  //Posição de instalação do eixo extensor
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um parâmetro de driver precisa ser definido. Se você escolher um tipo de eixo extensor que inclui vários eixos, precisa definir os parâmetros do driver para cada eixo.

        //4. Habilite o eixo selecionado e execute o homing
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5. Calibre e aplique o sistema de coordenadas do eixo extensor (Nota: As interfaces de calibração para posicionadores e trilhos deslizantes lineares são diferentes. Abaixo estão as interfaces para posicionadores)
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /* Você precisa calibrar o eixo extensor usando pontos em quatro posições diferentes, portanto, precisa chamar esta interface 4 vezes para completar a calibração */
        DescPose coord = new DescPose( );
        robot.PositionorComputeECoordSys(ref coord); //Calcular o resultado da calibração do eixo extensor
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //Aplicar o resultado da calibração ao sistema de coordenadas do eixo extensor

        //6. Calibre o sistema de coordenadas da peça no eixo extensor. Você precisará usar as seguintes interfaces
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7. Registre o ponto de início do seu movimento de junta síncrono
        DescPose startdescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos startjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto de início do seu eixo extensor */);

        //8. Registre as coordenadas do ponto final do seu movimento de junta síncrono
        DescPose enddescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos endjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos endexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo extensor */);

        //9. Escreva o programa de movimento síncrono
        //Mova para o ponto de início, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
    }

Movimento Síncrono do Eixo Extensor UDP com Movimento Linear do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Movimento síncrono do eixo extensor UDP com movimento linear do robô
    * @param [in] joint_pos  Posição de junta alvo, unidade deg
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user  Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param [in] epos  Posição do eixo extensor, unidade mm
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Quantidade de deslocamento da pose
    * @return Código de erro
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void btnSyncMoveL_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1. Calibre e aplique o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são as seguintes:
        //    int SetToolPoint(int point_num);  //Definir ponto de referência da ferramenta - método de seis pontos
        //    int ComputeTool(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta
        //    int SetTcp4RefPoint(int point_num);    //Definir ponto de referência da ferramenta - método de quatro pontos
        //    int ComputeTcp4(ref DescPose tcp_pose);   //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //Definir e aplicar sistema de coordenadas da ferramenta
        //    int SetToolList(int id, DescPose coord, int type, int install);   //Definir e aplicar lista de sistemas de coordenadas da ferramenta

        //2. Defina os parâmetros de comunicação UDP e carregue a comunicação UDP
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3. Defina os parâmetros do eixo extensor, incluindo o tipo de eixo extensor, parâmetros do driver do eixo extensor, parâmetros DH do eixo extensor
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1);  //Posição de instalação do eixo extensor
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um parâmetro de driver precisa ser definido. Se você escolher um tipo de eixo extensor que inclui vários eixos, precisa definir os parâmetros do driver para cada eixo.

        //4. Habilite o eixo selecionado e execute o homing
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5. Calibre e aplique o sistema de coordenadas do eixo extensor
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /* Você precisa calibrar o eixo extensor usando pontos em quatro posições diferentes, portanto, precisa chamar esta interface 4 vezes para completar a calibração */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //Calcular o resultado da calibração do eixo extensor
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //Aplicar o resultado da calibração ao sistema de coordenadas do eixo extensor

        //6. Calibre o sistema de coordenadas da peça no eixo extensor. Você precisará usar as seguintes interfaces
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7. Registre o ponto de início do seu movimento linear síncrono
        DescPose startdescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos startjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto de início do seu eixo extensor */);

        //8. Registre as coordenadas do ponto final do seu movimento linear síncrono
        DescPose enddescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos endjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos endexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo extensor */);

        //9. Escreva o programa de movimento síncrono
        //Mova para o ponto de início, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
    }

Movimento Síncrono do Eixo Extensor UDP com Movimento de Arco do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Movimento síncrono do eixo extensor UDP com movimento de arco do robô
    * @param [in] joint_pos_p  Posição de junta do ponto de caminho, unidade deg
    * @param [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param [in] ptool  Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] puser  Número da coordenada da peça, intervalo [0~14]
    * @param [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p  Posição do eixo extensor no ponto intermediário, unidade mm
    * @param [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p  Quantidade de deslocamento da pose
    * @param [in] joint_pos_t  Posição de junta do ponto alvo, unidade deg
    * @param [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param [in] ttool  Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] tuser  Número da coordenada da peça, intervalo [0~14]
    * @param [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t  Posição do eixo extensor, unidade mm
    * @param [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t  Quantidade de deslocamento da pose	 
    * @param [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @return Código de erro
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void btnSyncMoveC_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1. Calibre e aplique o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são as seguintes:
        //    int SetToolPoint(int point_num);  //Definir ponto de referência da ferramenta - método de seis pontos
        //    int ComputeTool(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta
        //    int SetTcp4RefPoint(int point_num);    //Definir ponto de referência da ferramenta - método de quatro pontos
        //    int ComputeTcp4(ref DescPose tcp_pose);   //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //Definir e aplicar sistema de coordenadas da ferramenta
        //    int SetToolList(int id, DescPose coord, int type, int install);   //Definir e aplicar lista de sistemas de coordenadas da ferramenta

        //2. Defina os parâmetros de comunicação UDP e carregue a comunicação UDP
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3. Defina os parâmetros do eixo extensor, incluindo o tipo de eixo extensor, parâmetros do driver do eixo extensor, parâmetros DH do eixo extensor
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1);  //Posição de instalação do eixo extensor
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um parâmetro de driver precisa ser definido. Se você escolher um tipo de eixo extensor que inclui vários eixos, precisa definir os parâmetros do driver para cada eixo.

        //4. Habilite o eixo selecionado e execute o homing
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5. Calibre e aplique o sistema de coordenadas do eixo extensor
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /* Você precisa calibrar o eixo extensor usando pontos em quatro posições diferentes, portanto, precisa chamar esta interface 4 vezes para completar a calibração */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //Calcular o resultado da calibração do eixo extensor
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //Aplicar o resultado da calibração ao sistema de coordenadas do eixo extensor

        //6. Calibre o sistema de coordenadas da peça no eixo extensor. Você precisará usar as seguintes interfaces
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7. Registre o ponto de início do seu movimento de arco síncrono
        DescPose startdescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos startjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto de início do seu eixo extensor */);

        //8. Registre as coordenadas do ponto final do seu movimento de arco síncrono
        DescPose enddescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos endjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos endexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo extensor */);

        //8. Registre as coordenadas do ponto intermediário do seu movimento de arco síncrono
        DescPose middescPose = new DescPose(/* Insira suas coordenadas */);
        JointPos midjointPos = new JointPos(/* Insira suas coordenadas */);
        ExaxisPos midexaxisPos = new ExaxisPos(/* Insira a coordenada do eixo extensor quando o robô estiver no ponto intermediário do arco */);

        //9. Escreva o programa de movimento síncrono
        //Mova para o ponto de início, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
    }

Definir DO de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir DO de extensão
    * @param [in] DONum Número do DO
    * @param [in] bOpen Estado true-ligar; false-desligar
    * @param [in] smooth Suavizar ou não
    * @param [in] block Bloquear ou não
    * @return Código de erro
    */
    int SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);

Definir AO de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir AO de extensão
    * @param [in] AONum Número do AO
    * @param [in] value Valor analógico [0-4095]
    * @param [in] block Bloquear ou não
    * @return Código de erro
    */
    int SetAuxAO(int AONum, double value, bool block);

Definir Tempo de Filtragem de Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir tempo de filtragem de entrada DI de extensão
    * @param [in] filterTime Tempo de filtragem (ms)
    * @return Código de erro
    */
    int SetAuxDIFilterTime(int filterTime);

Definir Tempo de Filtragem de Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Definir tempo de filtragem de entrada AI de extensão
    * @param [in] filterTime Tempo de filtragem (ms)
    * @return Código de erro
    */
    int SetAuxAIFilterTime(int filterTime);

Aguardar Entrada DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Aguardar entrada DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] bOpen Estado 0-desligado; 1-ligado
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Continuar movimento ou não
    * @return Código de erro
    */
    int WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);

Aguardar Entrada AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Aguardar entrada AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] sign 0-maior que; 1-menor que
    * @param [in] value Valor do AI
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Continuar movimento ou não
    * @return Código de erro
    */
    int WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);

Obter Valor DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Obter valor DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] isNoBlock Bloquear ou não
    * @param [out] isOpen 0-desligado; 1-ligado
    * @return Código de erro
    */
    int GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);

Obter Valor AI de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief Obter valor AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] isNoBlock Bloquear ou não
    * @param [in] value Valor de entrada
    * @return Código de erro
    */
    int GetAuxAI(int AINum, bool isNoBlock, int& value);

Exemplo de Código de E/S de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: C#
    :linenos:

    private void btnAODO_Click(object sender, EventArgs e)
    {
        int rtn;
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, true, false, true);
            Thread.Sleep(100);
        }
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, false, false, true);
            Thread.Sleep(100);
        }

        for (int i = 0; i < 409; i++)
        {
            robot.SetAuxAO(0, i * 10, true);
            robot.SetAuxAO(1, 4095 - i * 10, true);
            robot.SetAuxAO(2, i * 10, true);
            robot.SetAuxAO(3, 4095 - i * 10, true);
            Thread.Sleep(10);
        }

        robot.SetAuxDIFilterTime(10);
        robot.SetAuxAIFilterTime(0, 10);

        for (int i = 0; i < 20; i++)
        {
            bool curValue = false;
            rtn = robot.GetAuxDI(i, false, ref curValue);
            Console.WriteLine("DI" + i + "   " + curValue);
        }
        int curValueAI = -1;
        for (int i = 0; i < 4; i++)
        {
            rtn = robot.GetAuxAI(i, true, ref curValueAI);
        }

        robot.WaitAuxDI(1, false, 1000, false);
        robot.WaitAuxAI(1, 1, 132, 1000, false);
    }

Habilitar Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Habilitar dispositivo móvel
    * @param enable false-desabilitar; true-habilitar
    * @return Código de erro
    */
    int TractorEnable(bool enable);

Parar Movimento do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Parar movimento do dispositivo móvel
    * @return Código de erro
    */
    int TractorStop();

Homing do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Homing do dispositivo móvel
    * @return Código de erro
    */
    int  TractorHoming();

Movimento Linear do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento linear do dispositivo móvel
    * @param distance Distância do movimento linear (mm)
    * @param vel Percentual de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    int TractorMoveL(double distance, double vel);

Movimento de Arco do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento de arco do dispositivo móvel
    * @param radio Raio do movimento de arco (mm)
    * @param angle Ângulo do movimento de arco (°)
    * @param vel Percentual de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    int TractorMoveC(double radio, double angle, double vel);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgs e)
    {
        int rtn;
        robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10,1);
        robot.ExtDevLoadUDPDriver();
        rtn = robot.ExtAxisServoOn(1, 1);
        rtn = robot.ExtAxisServoOn(2, 1);
        Thread.Sleep(2000);
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        Thread.Sleep(2000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
        Thread.Sleep(4000);
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280f, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280f, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);
        robot.TractorEnable(false);
        Thread.Sleep(2000);
        robot.TractorEnable(true);
        Thread.Sleep(2000);
        robot.TractorHoming();
        Thread.Sleep(2000);
        robot.TractorMoveL(100, 2);
        Thread.Sleep(5000);
        robot.TractorStop();
        robot.TractorMoveL(-100, 20);
        Thread.Sleep(5000);
        robot.TractorMoveC(300, 90, 20);
        Thread.Sleep(10000);
        robot.TractorMoveC(300, -90, 20);
        Thread.Sleep(1000);
        robot.TractorStop();    
    }

Definir Estratégia de Movimento Síncrono entre Eixo Extensor e Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:


    /**
    * @brief Definir estratégia de movimento síncrono entre eixo extensor e robô
    * @param strategy Estratégia; 0-com o robô como principal; 1-eixo extensor e robô síncronos
    * @return Código de erro
    */
    int SetExAxisRobotPlan(int strategy)

Exemplo de Código de Definição de Estratégia de Movimento Síncrono entre Eixo Extensor e Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:


    private void button94_Click(object sender, EventArgs e)
    {
        JointPos joint_pos1 = new JointPos(-22.016, -49.217, 124.714, -161.100, -85.108, -0.333);
        JointPos joint_pos2 = new JointPos(-21.083, -46.613, 110.079, -147.796, -80.757, -0.330);
        JointPos joint_pos3 = new JointPos(-25.572, -60.090, 135.397, -163.889, -82.489, -0.345);
        DescPose desc_pos1 = new DescPose(2.637, -0.001, 30.673, 178.786, -4.134, 68.326);
        DescPose desc_pos2 = new DescPose(213.812, -1.440, 47.311, 177.410, 0.166, 68.946);
        DescPose desc_pos3 = new DescPose(444.342, -12.723, 82.470, -177.701, -1.325, 65.151);   
        ExaxisPos epos1 = new ExaxisPos(0.001, 0.000, 0.000, 0.000);
        ExaxisPos epos2 = new ExaxisPos(299.977, 0.000, 0.000, 0.000);
        ExaxisPos epos3 = new ExaxisPos(399.969, 0.000, 0.000, 0.000);      
        DescPose offset_pos = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.SetExAxisRobotPlan(0);
        Console.WriteLine($"SetExAxisRobotPlan rtn is {rtn}");
        Thread.Sleep(1000);
        rtn = robot.ExtAxisSyncMoveL(joint_pos1, desc_pos1, 1, 0, 100, 100, 100, -1, epos1, 0, offset_pos);
        Console.WriteLine($"ExtAxisSyncMoveL 1 rtn is {rtn}");

        rtn = robot.ExtAxisSyncMoveL(joint_pos2, desc_pos2, 1, 0, 100, 100, 100, -1, epos2, 0, offset_pos);
        Console.WriteLine($"ExtAxisSyncMoveL 2 rtn is {rtn}");
        rtn = robot.ExtAxisSyncMoveL(joint_pos3, desc_pos3, 1, 0, 100, 100, 100, -1, epos3, 0, offset_pos);
        Console.WriteLine($"ExtAxisSyncMoveL 3 rtn is {rtn}");
        Thread.Sleep(8000);
    }

Definir Tempo de Conclusão de Posicionamento do Eixo Extensor UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Definir tempo de conclusão de posicionamento do eixo extensor UDP
    * @param [in] time Tempo de conclusão de posicionamento [ms]
    * @return Código de erro
    */
    public int SetExAxisCmdDoneTime(double time)