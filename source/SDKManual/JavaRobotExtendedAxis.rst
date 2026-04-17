Eixo de Extensão
=================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define os parâmetros do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] param Parâmetros do eixo de extensão 485
    * @return Código de erro 
    */
    int AuxServoSetParam(int servoId, Axis485Param param)
    
Obter Parâmetros do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém os parâmetros de configuração do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [out] param Parâmetros do eixo de extensão 485
    * @return Código de erro 
    */
    int AuxServoGetParam(int servoId, Axis485Param param);

Habilitar/Desabilitar Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Habilita/desabilita o eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] status Estado de habilitação, 0-desabilitar, 1-habilitar
    * @return Código de erro 
    */
    int AuxServoEnable(int servoId, int status);
        
Definir Modo de Controle do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o modo de controle do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] mode Modo de controle, 0-modo posição, 1-modo velocidade
    * @return Código de erro 
    */
    int AuxServoSetControlMode(int servoId, int mode);

Definir Posição Alvo do Eixo de Extensão 485 (Modo Posição)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a posição alvo do eixo de extensão 485 (modo posição)
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] pos Posição alvo, mm ou °
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @param [in] acc Porcentagem de aceleração [0-100]
    * @return Código de erro 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed, double acc);
    
Definir Torque Alvo do Eixo de Extensão 485 (Modo Torque) - Temporariamente não disponível
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o torque alvo do eixo de extensão 485 (modo torque) - Temporariamente não disponível
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] torque Torque alvo, Nm
    * @return Código de erro 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
Definir Homing do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o homing do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] mode Modo de homing, 1-homing na posição atual; 2-homing no limite negativo; 3-homing no limite positivo
    * @param [in] searchVel Velocidade de busca, mm/s ou °/s
    * @param [in] latchVel Velocidade de fixação, mm/s ou °/s
    * @param [in] acc Porcentagem de aceleração [0-100]
    * @return Código de erro 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

Limpar Informações de Erro do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Limpa as informações de erro do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @return Código de erro 
    */
    int AuxServoClearError(int servoId);

Obter Estado do Servo do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém o estado do servo do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] servoErrCode Código de falha do servo driver
    * @param [in] servoState Estado do servo driver bit0:0-desabilitado; 1-habilitado; bit1:0-parado; 1-em movimento; bit4:0-posicionamento não concluído; 1-posicionamento concluído; bit5:0-homing não concluído; 1-homing concluído
    * @param [in] servoPos Posição atual do servo mm ou °
    * @param [in] servoSpeed Velocidade atual do servo mm/s ou °/s
    * @param [in] servoTorque Torque atual do servo Nm
    * @return Código de erro 
    */
    int AuxServoGetStatus(int servoId, int[] servoErrCode, int[] servoState, double[] servoPos, double[] servoSpeed, double[] servoTorque)

Definir Velocidade Alvo do Eixo de Extensão 485 (Modo Velocidade)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a velocidade alvo do eixo de extensão 485 (modo velocidade)
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @param [in] acc Porcentagem de aceleração [0-100]
    * @return Código de erro 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed, double acc);

Definir Número do Eixo de Dados do Eixo de Extensão 485 no Feedback de Estado
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define o número do eixo de dados do eixo de extensão 485 no feedback de estado
    * @param [in] servoId ID do servo driver, faixa [1-16], correspondente ao ID do escravo
    * @return Código de erro 
    */
    int AuxServosetStatusID(int servoId);

Definir Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a aceleração/desaceleração do movimento do eixo de extensão 485
    * @param [in] acc Aceleração do movimento do eixo de extensão 485
    * @param [in] dec Desaceleração do movimento do eixo de extensão 485
    * @return Código de erro 
    */
    int AuxServoSetAcc(double acc, double dec)

Definir Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Define a aceleração/desaceleração de parada de emergência do eixo de extensão 485
    * @param [in] acc Aceleração de parada de emergência do eixo de extensão 485
    * @param [in] dec Desaceleração de parada de emergência do eixo de extensão 485
    * @return Código de erro 
    */
    int AuxServoSetEmergencyStopAcc(double acc, double dec)

Obter Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a aceleração/desaceleração do movimento do eixo de extensão 485
    * @return List[0]: Código de erro; List[1]: Aceleração do movimento do eixo de extensão 485; List[2]: Desaceleração do movimento do eixo de extensão 485 
    */
    List<Number> AuxServoGetAcc()

Obter Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém a aceleração/desaceleração de parada de emergência do eixo de extensão 485
    * @return List[0]: Código de erro; List[1]: Aceleração de parada de emergência do eixo de extensão 485; List[2]: Desaceleração de parada de emergência do eixo de extensão 485
    */
    List<Number> AuxServoGetEmergencyStopAcc()

Exemplo de Código de Controle do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int Test485Auxservo(Robot robot)
    {
        Axis485Param ax=new Axis485Param(1, 1, 1, 131072, 15.45);
        int retval = robot.AuxServoSetParam(1, ax);

        Axis485Param ax2=new Axis485Param();
        retval = robot.AuxServoGetParam(1, ax2);

        ax.servoCompany=10;
        ax.servoModel=11;
        ax.servoSoftVersion=12;
        ax.servoResolution=13;
        ax.axisMechTransRatio=14;

        retval = robot.AuxServoSetParam(1, ax);

        retval = robot.AuxServoGetParam(1,ax2);

        ax.servoCompany=1;
        ax.servoModel=1;
        ax.servoSoftVersion=1;
        ax.servoResolution=131072;
        ax.axisMechTransRatio=36;

        retval = robot.AuxServoSetParam(1, ax);
        robot.Sleep(3000);

        robot.AuxServoSetAcc(3000, 3000);
        robot.AuxServoSetEmergencyStopAcc(5000, 5000);
        robot.Sleep(1000);
        double emagacc = 0, acc = 0;
        double emagdec = 0, dec = 0;

        List<Number> aux=new ArrayList<>();

        aux=robot.AuxServoGetEmergencyStopAcc();
        aux=robot.AuxServoGetAcc();

        robot.AuxServoSetControlMode(1, 0);
        robot.Sleep(2000);

        retval = robot.AuxServoEnable(1, 0);
        robot.Sleep(1000);
        int[] servoerrcode =new int[]{0};
        int[] servoErrCode=new int[]{0};
        int[] servoState=new int[]{0};
        double[] servoPos=new double[]{0};
        double[] servoSpeed=new double[]{0};
        double[] servoTorque=new double[]{0};
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(1000);;

        retval = robot.AuxServoEnable(1, 1);
        robot.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(1000);

        retval = robot.AuxServoHoming(1, 1, 5, 1,100);
        robot.Sleep(3000);

        retval = robot.AuxServoSetTargetPos(1, 200, 30,100);
        robot.Sleep(1000);
        retval = robot.AuxServoGetStatus(1, servoErrCode, servoState, servoPos, servoSpeed, servoTorque);
        robot.Sleep(8000);


        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);

        robot.AuxServoEnable(1, 0);
        robot.Sleep(1000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(1000);
        robot.AuxServoSetTargetSpeed(1, 100, 80);

        robot.Sleep(5000);
        robot.AuxServoSetTargetSpeed(1, 0, 80);

        robot.CloseRPC();
        return 0;
    }

Configuração dos Parâmetros de Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Configuração dos parâmetros de comunicação UDP do eixo de extensão
    * @param [in] param Parâmetros de comunicação
    * @return Código de erro
    */
    int ExtDevSetUDPComParam(UDPComParam param);     

Obter Configuração dos Parâmetros de Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros de comunicação UDP do eixo de extensão
    * @param [out] ip Endereço IP do CLP
    * @param [out] port Número da porta
    * @param [out] period Período de comunicação (ms, padrão 2, não modifique este parâmetro)
    * @param [out] lossPkgTime Tempo de detecção de perda de pacotes (ms)
    * @param [out] lossPkgNum Número de perdas de pacotes
    * @param [out] disconnectTime Duração de confirmação de desconexão da comunicação
    * @param [out] reconnectEnable Habilitação de reconexão automática em caso de desconexão da comunicação 0-desabilitar 1-habilitar
    * @param [out] reconnectPeriod Intervalo de reconexão (ms)
    * @param [out] reconnectNum Número de tentativas de reconexão
    * @param [out] selfConnect Se reconecta automaticamente após reinicialização do painel de controle; 0-não reconectar; 1-reconectar
    * @return Código de erro
    */
    public int ExtDevGetUDPComParam(ref string ip, ref int port, ref int period, ref int lossPkgTime, ref int lossPkgNum, ref int disconnectTime, ref int reconnectEnable, ref int reconnectPeriod, ref int reconnectNum, ref int selfConnect)    

Carregar Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Carrega a comunicação UDP
    * @return Código de erro
    */
    int ExtDevLoadUDPDriver();

Descarregar Comunicação UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Descarrega a comunicação UDP
    * @return Código de erro
    */
    int ExtDevUnloadUDPDriver();

Restaurar Conexão Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Restaura a conexão após desconexão anormal da comunicação UDP do eixo de extensão
    * @return Código de erro
    */
    int ExtDevUDPClientComReset();

Fechar Comunicação Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fecha a comunicação após desconexão anormal da comunicação UDP do eixo de extensão
    * @return Código de erro
    */
    int ExtDevUDPClientComClose();

Configuração dos Parâmetros do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configuração dos parâmetros do eixo de extensão UDP
    * @param [in] axisID Número do eixo
    * @param [in] axisType Tipo de eixo de extensão 0-translação; 1-rotação
    * @param [in] axisDirection Direção do eixo de extensão 0-positiva; 1-negativa
    * @param [in] axisMax Posição máxima do eixo de extensão mm
    * @param [in] axisMin Posição mínima do eixo de extensão mm
    * @param [in] axisVel Velocidade mm/s
    * @param [in] axisAcc Aceleração mm/s2
    * @param [in] axisLead Passo mm
    * @param [in] encResolution Resolução do codificador
    * @param [in] axisOffect Deslocamento do ponto inicial da solda no eixo de extensão
    * @param [in] axisCompany Fabricante do driver 1-Huichuan; 2-Huichuan; 3-Panasonic
    * @param [in] axisModel Modelo do driver 1-Huichuan-SV-XD3EA040L-E, 2-Huichuan-SV-X2EA150A-A, 1-Huichuan-SV620PT5R4I, 1-Panasonic-MADLN15SG, 2-Panasonic-MSDLN25SG, 3-Panasonic-MCDLN35SG
    * @param [in] axisEncType Tipo de codificador  0-incremental; 1-absoluto
    * @return Código de erro
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, int encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

Definir Posição de Instalação do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a posição de instalação do eixo de extensão
    * @param [in] installType 0-robô instalado no eixo externo, 1-robô instalado fora do eixo externo
    * @return Código de erro
    */
    int SetRobotPosToAxis(int installType);

Definir Configuração dos Parâmetros DH do Sistema de Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a configuração dos parâmetros DH do sistema de eixo de extensão
    * @param [in]  axisConfig Configuração do eixo externo, 0-trilho linear de 1 grau de liberdade, 1-posicionador tipo L de 2 graus de liberdade, 2-3 graus de liberdade, 3-4 graus de liberdade, 4-posicionador de 1 grau de liberdade
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

Habilitar Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Habilita o eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] status 0-desabilitar; 1-habilitar
    * @return Código de erro
    */
    int ExtAxisServoOn(int axisID, int status);

Homing do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Homing do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] mode Modo de homing 0-homing na posição atual, 1-homing no limite negativo, 2-homing no limite positivo
    * @param [in] searchVel Velocidade de busca (mm/s)
    * @param [in] latchVel Velocidade de fixação da busca (mm/s)
    * @return Código de erro
    */
    int ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

Iniciar Jog do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Inicia o jog do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] direction Direção de rotação 0-reversa; 1-positiva
    * @param [in] vel Velocidade (mm/s)
    * @param [in] acc (Aceleração mm/s2)
    * @param [in] maxDistance Distância máxima de jog
    * @return Código de erro
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
Parar Jog do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Para o jog do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @return Código de erro
    */
    int ExtAxisStopJog(int axisID);

Exemplo de Código de Configuração e Jog do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static int TestUDPAxis(Robot robot)//UDP
    {
        UDPComParam para1=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
        int rtn = robot.ExtDevSetUDPComParam(para1);
        String ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        UDPComParam para2=new UDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum,0);
        rtn = robot.ExtDevGetUDPComParam(para2);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        rtn = robot.ExtAxisServoOn(2, 1);
        robot.Sleep(3000);

        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.Sleep(3000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);

        robot.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);

        robot.Sleep(4000);
        robot.ExtAxisStartJog(1, 0, 10, 10, 30);
        robot.Sleep(4000);
        robot.ExtAxisStopJog(1);
        robot.Sleep(4000);
        robot.ExtAxisServoOn(1, 0);

        robot.Sleep(4000);
        robot.ExtAxisStartJog(2, 0, 10, 10, 30);
        robot.Sleep(4000);
        robot.ExtAxisStopJog(2);
        robot.Sleep(4000);
        robot.ExtAxisServoOn(2, 0);
        robot.Sleep(4000);
        robot.ExtDevUnloadUDPDriver();

        return 0;
    }

Definir Ponto de Referência do Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência do sistema de coordenadas do eixo de extensão - Método de quatro pontos
    * @param [in]  pointNum Número do ponto [1-4]
    * @return Código de erro
    */
    int ExtAxisSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas do eixo de extensão - Método de quatro pontos
    * @param [out]  coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    int ExtAxisComputeECoordSys(DescPose coord);

Definir Ponto de Referência do Sistema de Coordenadas do Posicionador
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o ponto de referência do sistema de coordenadas do posicionador
    * @param [in]  pointNum Número do ponto [1-4]
    * @return Código de erro
    */
    int PositionorSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Posicionador - Método de Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas do posicionador - Método de quatro pontos
    * @param [out] coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    int PositionorComputeECoordSys(DescPose coord);

Definir Pose do Ponto de Referência de Calibração no Sistema de Coordenadas da Extremidade do Posicionador
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a pose do ponto de referência de calibração no sistema de coordenadas da extremidade do posicionador
    * @param [in] pos Valor da pose
    * @return Código de erro
    */
    int SetRefPointInExAxisEnd(DescPose pos);

Aplicar Sistema de Coordenadas do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aplica o sistema de coordenadas do eixo de extensão
    * @param [in]  applyAxisId Número do eixo de extensão bit0-bit3 correspondem aos números dos eixos de extensão 1-4, por exemplo, aplicar eixos de extensão 1 e 3 é 0b 0000 0101; ou seja, 5
    * @param [in]  axisCoordNum Número do sistema de coordenadas do eixo de extensão
    * @param [in]  coord Valor do sistema de coordenadas
    * @param [in]  calibFlag Flag de calibração 0-não, 1-sim
    * @return Código de erro
    */
    int ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

Obter Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /** 
    * @brief Obtém o sistema de coordenadas do eixo de extensão
    * @param [out] coord Sistema de coordenadas do eixo de extensão
    * @return Código de erro
    */
    int ExtAxisGetCoord(DescPose coord);

Exemplo de Código de Calibração do Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUDPAxisCalib(Robot robot)
    {
        UDPComParam para1=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);

        int rtn = robot.ExtDevSetUDPComParam(para1);
        String ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        UDPComParam para2=new UDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum,0);

        rtn = robot.ExtDevGetUDPComParam(para2);

        robot.ExtDevLoadUDPDriver();

        rtn = robot.ExtAxisServoOn(1, 1);
        rtn = robot.ExtAxisServoOn(2, 1);

        robot.Sleep(4000);

        rtn = robot.SetRobotPosToAxis(1);
        rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4,  0, 0, 0, 0, 0, 0);
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
        rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);

        DescPose toolCoord=new DescPose(0, 0, 210, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);

        JointPos jSafe=new JointPos(115.193, -96.149, 92.489, -87.068, -89.15, -83.488);
        JointPos j1=new JointPos(117.559, -92.624, 100.329, -96.909, -94.057, -83.488);
        JointPos j2=new JointPos(112.239, -90.096, 99.282, -95.909, -89.824, -83.488);
        JointPos j3=new JointPos(110.839, -83.473, 93.166, -89.22, -90.499, -83.487);
        JointPos j4=new JointPos(107.935, -83.572, 95.424, -92.873, -87.933, -83.488);

        DescPose descSafe =new DescPose(0,0,0,0,0,0);
        DescPose desc1 = new DescPose(0,0,0,0,0,0);
        DescPose desc2 = new DescPose(0,0,0,0,0,0);
        DescPose desc3 = new DescPose(0,0,0,0,0,0);
        DescPose desc4 = new DescPose(0,0,0,0,0,0);
        ExaxisPos exaxisPos =new ExaxisPos(0,0,0,0);
        DescPose offdese =new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(jSafe, descSafe);
        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.Sleep(2000);

        robot.GetForwardKin(j1, desc1);
        robot.MoveJ(j1, desc1, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.Sleep(2000);

        DescPose actualTCPPos =new DescPose(0,0,0,0,0,0);

        robot.GetActualTCPPose(actualTCPPos);
        robot.SetRefPointInExAxisEnd(actualTCPPos);
        rtn = robot.PositionorSetRefPoint(1);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j2, desc2);
        rtn = robot.MoveJ(j2, desc2, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(2);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j3, desc3);
        robot.MoveJ(j3, desc3, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(3);
        robot.Sleep(2000);

        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ExtAxisStartJog(1, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.ExtAxisStartJog(2, 0, 50, 50, 10);
        robot.Sleep(1000);
        robot.GetForwardKin(j4, desc4);
        robot.MoveJ(j4, desc4, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.PositionorSetRefPoint(4);
        robot.Sleep(2000);

        DescPose axisCoord = new DescPose();
        robot.PositionorComputeECoordSys(axisCoord);
        robot.MoveJ(jSafe, descSafe, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1);

        robot.CloseRPC();
        return 0;
    }

Movimento do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento do eixo de extensão UDP
    * @param [in] pos Posição alvo
    * @param [in] ovl Porcentagem de velocidade
    * @param [in] blend Parâmetro de suavização (mm ou ms)
    * @return Código de erro
    */
    int ExtAxisMove(ExaxisPos pos, double ovl, double blend)

Exemplo de Código de Movimento do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUDPAxisCalib(Robot robot)
    {
        ExaxisPos exaxisPos = new ExaxisPos( 20, 0, 0, 0 );
        robot.ExtAxisMove(exaxisPos,40);
        robot.CloseRPC();
        return 0;
    }

Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento articular do robô
    * @param [in] joint_pos  Posição articular alvo, unidade deg
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número da ferramenta, faixa [0~14]
    * @param [in] user  Número da peça, faixa [0~14]
    * @param [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] epos  Posição do eixo de extensão, unidade mm
    * @param [in] blendT [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade ms
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] ffset_pos  Valor de deslocamento da pose
    * @return Código de erro
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô (Cálculo Automático de Cinemática Direta)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Movimento síncrono do eixo de extensão UDP com movimento articular do robô (Cálculo automático de cinemática direta)
    * @param  [in] joint_pos  Posição articular alvo, unidade deg
    * @param  [in] tool  Número da ferramenta, faixa [0~14]
    * @param  [in] user  Número da peça, faixa [0~14]
    * @param  [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param  [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param  [in] epos  Posição do eixo de extensão, unidade mm
    * @param  [in] blendT [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade ms
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Valor de deslocamento da pose
    * @return  Código de erro
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos) 

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveJ(Robot robot)
    {
        //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
        //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
        //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
        //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
        //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
        //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
        //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
        //4. Habilitar e fazer homing do eixo selecionado
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
        //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7. Registrar o ponto inicial do movimento articular síncrono
        DescPose startdescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos startjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ );
        //8. Registrar as coordenadas do ponto final do movimento articular síncrono
        DescPose enddescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos endjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos endexaxisPos =new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo de extensão */);
        //9. Escrever o programa de movimento síncrono
        //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveJ(endjointPos, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
        robot.CloseRPC();
        return 0;
    }

Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento linear do robô
    * @param [in] joint_pos  Posição articular alvo, unidade deg
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número da ferramenta, faixa [0~14]
    * @param [in] user  Número da peça, faixa [0~14]
    * @param [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param [in] epos  Posição do eixo de extensão, unidade mm
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Valor de deslocamento da pose
    * @return Código de erro
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô (Cálculo Automático de Cinemática Inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Movimento síncrono do eixo de extensão UDP com movimento linear do robô (Cálculo automático de cinemática inversa)
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número da ferramenta, faixa [0~14]
    * @param  [in] user  Número da peça, faixa [0~14]
    * @param  [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param  [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param  [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param  [in] epos  Posição do eixo de extensão, unidade mm
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Valor de deslocamento da pose
    * @param  [in] config  Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular
    * @return  Código de erro
    */
    int ExtAxisSyncMoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos,int config)

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveL(Robot robot)
    {
        //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
        //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
        //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
        //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
        //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
        //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
        //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
        //4. Habilitar e fazer homing do eixo selecionado
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
        //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7. Registrar o ponto inicial do movimento articular síncrono
        DescPose startdescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos startjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ );
        //8. Registrar as coordenadas do ponto final do movimento articular síncrono
        DescPose enddescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos endjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos endexaxisPos =new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo de extensão */);
        //9. Escrever o programa de movimento síncrono
        //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveL(enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese,-1);
        robot.CloseRPC();
        return 0;
    }

Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento de arco do robô
    * @param [in] joint_pos_p  Posição articular do ponto de caminho, unidade deg
    * @param [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param [in] ptool  Número da ferramenta, faixa [0~14]
    * @param [in] puser  Número da peça, faixa [0~14]
    * @param [in] pvel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] pacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_p  Posição do eixo de extensão no ponto intermediário, unidade mm
    * @param [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p  Valor de deslocamento da pose
    * @param [in] joint_pos_t  Posição articular do ponto alvo, unidade deg
    * @param [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param [in] ttool  Número da ferramenta, faixa [0~14]
    * @param [in] tuser  Número da peça, faixa [0~14]
    * @param [in] tvel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] tacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_t  Posição do eixo de extensão, unidade mm
    * @param [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t  Valor de deslocamento da pose
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @return Código de erro
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô (Cálculo Automático de Cinemática Inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  Movimento síncrono do eixo de extensão UDP com movimento de arco do robô (Cálculo automático de cinemática inversa)
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param  [in] ptool  Número da ferramenta, faixa [0~14]
    * @param  [in] puser  Número da peça, faixa [0~14]
    * @param  [in] pvel  Porcentagem de velocidade, faixa [0~100]
    * @param  [in] pacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo de extensão, unidade mm
    * @param  [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_p  Valor de deslocamento da pose
    * @param  [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param  [in] ttool  Número da ferramenta, faixa [0~14]
    * @param  [in] tuser  Número da peça, faixa [0~14]
    * @param  [in] tvel  Porcentagem de velocidade, faixa [0~100]
    * @param  [in] tacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo de extensão, unidade mm
    * @param  [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_t  Valor de deslocamento da pose
    * @param  [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param  [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param  [in] config  Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular
    * @return  Código de erro
    */
    int ExtAxisSyncMoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR,int config)

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public int testSyncMoveC(Robot robot)
    {
        //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
        //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
        //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
        //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
        //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
        //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
        //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
        //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
        UDPComParam param=new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);
        robot.ExtDevLoadUDPDriver();
        //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
        robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
        //4. Habilitar e fazer homing do eixo selecionado
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);
        //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
        DescPose pos = new DescPose(/* Insira as coordenadas do seu ponto de calibração */ );
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
        //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);
        //7. Registrar o ponto inicial do movimento de arco síncrono
        DescPose startdescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos startjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos startexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ );
        //8. Registrar as coordenadas do ponto final do movimento de arco síncrono
        DescPose enddescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos endjointPos = new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos endexaxisPos = new ExaxisPos(/* Insira as coordenadas do ponto final do seu eixo de extensão */ );
        //9. Registrar as coordenadas do ponto intermediário do movimento de arco síncrono
        DescPose middescPose = new DescPose(/*Insira suas coordenadas*/ );
        JointPos midjointPos =new JointPos(/*Insira suas coordenadas*/ );
        ExaxisPos midexaxisPos = new ExaxisPos(/* Insira as coordenadas do eixo de extensão quando o robô estiver no ponto intermediário do arco */ );
        //10. Escrever o programa de movimento síncrono
        //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
        robot.MoveJ(startjointPos, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);
        //Iniciar movimento síncrono
        robot.ExtAxisSyncMoveC(middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0,-1);
        robot.CloseRPC();
        return 0;
    }

Definir DO de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o DO de extensão
    * @param [in] DONum Número do DO
    * @param [in] bOpen Interruptor true-ligar; false-desligar
    * @param [in] smooth Se é suave
    * @param [in] block Se é bloqueante
    * @return Código de erro
    */
    int SetAuxDO(int DONum, boolean bOpen, boolean smooth, boolean block);

Definir AO de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o AO de extensão
    * @param [in] AONum Número do AO
    * @param [in] value Valor analógico [0-4095]
    * @param [in] block Se é bloqueante
    * @return Código de erro
    */
    int SetAuxAO(int AONum, double value, boolean block);

Definir Tempo de Filtro de Entrada do DI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o tempo de filtro de entrada do DI de extensão
    * @param [in] filterTime Tempo de filtro (ms)
    * @return  Código de erro
    */
    int SetAuxDIFilterTime(int filterTime);

Definir Tempo de Filtro de Entrada do AI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o tempo de filtro de entrada do AI de extensão
    * @param [in] AONum Número do AO
    * @param [in] filterTime Tempo de filtro (ms)
    * @return Código de erro
    */
    int SetAuxAIFilterTime(int AONum, int filterTime);

Aguardar Entrada do DI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada do DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] bOpen Interruptor 0-desligar; 1-ligar
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Se continua o movimento
    * @return Código de erro
    */
    int WaitAuxDI(int DINum, boolean bOpen, int time, boolean errorAlarm);

Aguardar Entrada do AI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguarda a entrada do AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] sign 0-maior que; 1-menor que
    * @param [in] value Valor do AI
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Se continua o movimento
    * @return Código de erro
    */
    int WaitAuxAI(int AINum, int sign, int value, int time, boolean errorAlarm);
    
Obter Valor do DI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o valor do DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] isNoBlock Se é não bloqueante
    * @return List[0]: Código de erro; List[1] : isOpen 0-desligar; 1-ligar
    */
    List<Integer> GetAuxDI(int DINum, boolean isNoBlock)

Obter Valor do AI de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém o valor do AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] isNoBlock Se é não bloqueante
    * @return List[0]: Código de erro; List[1] : value Valor de entrada
    */
    List<Integer> GetAuxAI(int AINum, boolean isNoBlock);

Exemplo de Código de IO de Extensão
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAuxDOAO(Robot robot)
    {
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, true, false, true);
            robot.Sleep(100);
        }
        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, false, false, true);
            robot.Sleep(100);
        }

        for (int i = 0; i < 409; i++)
        {
            robot.SetAuxAO(0, i * 10, true);
            robot.SetAuxAO(1, 4095 - i * 10, true);
            robot.SetAuxAO(2, i * 10, true);
            robot.SetAuxAO(3, 4095 - i * 10, true);
            robot.Sleep(10);
        }

        robot.SetAuxDIFilterTime(10);
        robot.SetAuxAIFilterTime(0, 10);


        int curValue = -1;
        List<Integer> liter=new ArrayList<>();
        for (int i = 0; i < 4; i++)
        {
            liter = robot.GetAuxAI(i, true);
        }

        robot.WaitAuxDI(1, false, 1000, false);
        robot.WaitAuxAI(1, 1, 132, 1000, false);

        robot.CloseRPC();
        return 0;
    }

Habilitar Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Habilita o dispositivo móvel
    * @param [in] enable false-desabilitar; true-habilitar
    * @return Código de erro
    */
    int TractorEnable(Boolean enable);

Homing do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Homing do dispositivo móvel
    * @return Código de erro
    */
    int TractorHoming();

Movimento Linear do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Movimento linear do dispositivo móvel
    * @param [in] distance Distância do movimento linear (mm)
    * @param [in] vel Porcentagem de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    int TractorMoveL(double distance, double vel);

Movimento de Arco do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Movimento de arco do dispositivo móvel
    * @param [in] radio Raio do movimento de arco (mm)
    * @param [in] angle Ângulo do movimento de arco (°)
    * @param [in] vel Porcentagem de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    int TractorMoveC(double radio, double angle, double vel);

Parar Movimento do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief Para o movimento do dispositivo móvel
    * @return Código de erro
    */
    int TractorStop();

Exemplo de Código do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//Definir número de tentativas de reconexão, intervalo
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("Conexão RPC bem-sucedida");
        }
        else
        {
            System.out.println("Falha na conexão RPC");
            return ;
        }
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//Comunicação UDP do eixo de extensão
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);

        robot.TractorEnable(false);
        robot.Sleep(2000);
        robot.TractorEnable(true);
        robot.Sleep(2000);
        robot.TractorHoming();

        robot.Sleep(2000);
        robot.TractorMoveL(100, 20);
        robot.Sleep(5000);
        robot.TractorMoveL(-100, 20);
        robot.Sleep(5000);
        robot.TractorMoveC(300, 90, 20);
        robot.Sleep(2000);
        robot.TractorStop();//Parar dispositivo móvel
        robot.TractorMoveC(300, -90, 20);
    }
    
Configuração do Tempo de Conclusão do Posicionamento do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configuração do tempo de conclusão do posicionamento do eixo de extensão UDP
    * @param time Tempo de conclusão do posicionamento [ms]
    * @return Código de erro
    */
    public int SetExAxisCmdDoneTime(double time)