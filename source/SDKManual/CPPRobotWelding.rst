Soldagem do Robô
======================

.. toctree::
    :maxdepth: 5

Definir Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Define os parâmetros da curva de processo de soldagem
     * @param [in] id Número do processo de soldagem (1-99)
     * @param [in] startCurrent Corrente de abertura de arco (A)
     * @param [in] startVoltage Tensão de abertura de arco (V)
     * @param [in] startTime Tempo de abertura de arco (ms)
     * @param [in] weldCurrent Corrente de soldagem (A)
     * @param [in] weldVoltage Tensão de soldagem (V)
     * @param [in] endCurrent Corrente de fechamento de arco (A)
     * @param [in] endVoltage Tensão de fechamento de arco (V)
     * @param [in] endTime Tempo de fechamento de arco (ms)
     * @return Código de erro
     */
    errno_t WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

Obter Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém os parâmetros da curva de processo de soldagem
     * @param [in] id Número do processo de soldagem (1-99)
     * @param [out] startCurrent Corrente de abertura de arco (A)
     * @param [out] startVoltage Tensão de abertura de arco (V)
     * @param [out] startTime Tempo de abertura de arco (ms)
     * @param [out] weldCurrent Corrente de soldagem (A)
     * @param [out] weldVoltage Tensão de soldagem (V)
     * @param [out] endCurrent Corrente de fechamento de arco (A)
     * @param [out] endVoltage Tensão de fechamento de arco (V)
     * @param [out] endTime Tempo de fechamento de arco (ms)
     * @return Código de erro
     */
    errno_t WeldingGetProcessParam(int id, double& startCurrent, double& startVoltage, double& startTime, double& weldCurrent, double& weldVoltage, double& endCurrent, double& endVoltage, double& endTime);

Definir Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a relação entre corrente de soldagem e saída analógica
    * @param [in] currentMin Valor de corrente do ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    * @param [in] currentMax Valor de corrente do ponto direito da relação linear corrente de soldagem-saída analógica (A)
    * @param [in] outputVoltageMin Valor de tensão de saída analógica do ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    * @param [in] outputVoltageMax Valor de tensão de saída analógica do ponto direito da relação linear corrente de soldagem-saída analógica (V)
    * @return Código de erro
    */
    errno_t WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

Definir Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a relação entre tensão de soldagem e saída analógica
    * @param [in] weldVoltageMin Valor de tensão de soldagem do ponto esquerdo da relação linear tensão de soldagem-saída analógica (A)
    * @param [in] weldVoltageMax Valor de tensão de soldagem do ponto direito da relação linear tensão de soldagem-saída analógica (A)
    * @param [in] outputVoltageMin Valor de tensão de saída analógica do ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    * @param [in] outputVoltageMax Valor de tensão de saída analógica do ponto direito da relação linear tensão de soldagem-saída analógica (V)
    * @return Código de erro
    */
    errno_t WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

Obter Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a relação entre corrente de soldagem e saída analógica
    * @param [out] currentMin Valor de corrente do ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    * @param [out] currentMax Valor de corrente do ponto direito da relação linear corrente de soldagem-saída analógica (A)
    * @param [out] outputVoltageMin Valor de tensão de saída analógica do ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    * @param [out] outputVoltageMax Valor de tensão de saída analógica do ponto direito da relação linear corrente de soldagem-saída analógica (V)
    * @return Código de erro
    */
    errno_t WeldingGetCurrentRelation(double *currentMin, double *currentMax, double *outputVoltageMin, double *outputVoltageMax);

Obter Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a relação entre tensão de soldagem e saída analógica
    * @param [out] weldVoltageMin Valor de tensão de soldagem do ponto esquerdo da relação linear tensão de soldagem-saída analógica (A)
    * @param [out] weldVoltageMax Valor de tensão de soldagem do ponto direito da relação linear tensão de soldagem-saída analógica (A)
    * @param [out] outputVoltageMin Valor de tensão de saída analógica do ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    * @param [out] outputVoltageMax Valor de tensão de saída analógica do ponto direito da relação linear tensão de soldagem-saída analógica (V)
    * @return Código de erro
    */
    errno_t WeldingGetVoltageRelation(double *weldVoltageMin, double *weldVoltageMax, double *outputVoltageMin, double *outputVoltageMax);

Definir Corrente de Soldagem
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a corrente de soldagem
    * @param [in] ioType Tipo de E/S de controle 0-E/S da caixa de controle; 1-E/S estendida
    * @param [in] current Valor da corrente de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica da caixa de controle para corrente de soldagem (0-1)
    * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
    * @return Código de erro
    */
    errno_t WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

Definir Tensão de Soldagem
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a tensão de soldagem
    * @param [in] ioType Tipo de E/S de controle 0-E/S da caixa de controle; 1-E/S estendida
    * @param [in] voltage Valor da tensão de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica da caixa de controle para tensão de soldagem (0-1)
    * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
    * @return Código de erro
    */
    errno_t WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

Definir Parâmetros de Oscilação
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief Define os parâmetros de oscilação
     * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
     * @param [in] weaveType Tipo de oscilação 0-oscilação triangular plana; 1-oscilação triangular em L vertical; 2-oscilação circular horária; 3-oscilação circular anti-horária; 4-oscilação senoidal plana; 5-oscilação senoidal em L vertical; 6-oscilação triangular vertical; 7-oscilação senoidal vertical
     * @param [in] weaveFrequency Frequência de oscilação (Hz)
     * @param [in] weaveIncStayTime Modo de espera 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
     * @param [in] weaveRange Amplitude de oscilação (mm)
     * @param [in] weaveLeftRange Comprimento da corda esquerda da oscilação triangular vertical (mm)
     * @param [in] weaveRightRange Comprimento da corda direita da oscilação triangular vertical (mm)
     * @param [in] additionalStayTime Tempo de permanência no ponto vertical da oscilação triangular vertical (mm)
     * @param [in] weaveLeftStayTime Tempo de permanência à esquerda da oscilação (ms)
     * @param [in] weaveRightStayTime Tempo de permanência à direita da oscilação (ms)
     * @param [in] weaveCircleRadio Oscilação circular - taxa de retorno (0-100%)
     * @param [in] weaveStationary Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera; 1-posição permanece estática durante o tempo de espera
     * @param [in] weaveYawAngle Ângulo de direção da oscilação (rotação em torno do eixo Z da oscilação), em graus
     * @param [in] weaveRotAngle Ângulo de inclinação da direção da oscilação (deflexão em torno do eixo X da oscilação), em graus
     * @return Código de erro
     */
     errno_t WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle = 0);

Exemplo de Código para Definir Parâmetros de Soldagem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestSetWeldParam(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000);
        robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333);
        double startCurrent = 0;
        double startVoltage = 0;
        double startTime = 0;
        double weldCurrent = 0;
        double weldVoltage = 0;
        double endCurrent = 0;
        double endVoltage = 0;
        double endTime = 0;
        robot.WeldingGetProcessParam(1, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
        cout << "the Num 1 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
        robot.WeldingGetProcessParam(2, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
        cout << "the Num 2 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
        rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
        cout << "WeldingSetCurrentRelation rtn is: " << rtn << endl;
        rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
        cout << "WeldingSetVoltageRelation rtn is: " << rtn << endl;
        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;
        int curIndex = 0;
        int volIndex = 0;
        rtn = robot.WeldingGetCurrentRelation(&current_min, &current_max, &output_vmin, &output_vmax, &curIndex);
        cout << "WeldingGetCurrentRelation rtn is: " << rtn << endl;
        cout << "current min " << current_min << " current max " << current_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
        rtn = robot.WeldingGetVoltageRelation(&vol_min, &vol_max, &output_vmin, &output_vmax, &volIndex);
        cout << "WeldingGetVoltageRelation rtn is: " << rtn << endl;
        cout << "vol min " << vol_min << " vol max " << vol_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
        rtn = robot.WeldingSetCurrent(0, 100, 0, 0);
        cout << "WeldingSetCurrent rtn is: " << rtn << endl;
        this_thread::sleep_for(chrono::seconds(3));
        rtn = robot.WeldingSetVoltage(0, 10, 0, 0);
        cout << "WeldingSetVoltage rtn is: " << rtn << endl;
        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
        cout << "rtn is: " << rtn << endl;
        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);
        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        printf("WeldingSetCheckArcInterruptionParam  %d\n", rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        printf("WeldingSetReWeldAfterBreakOffParam  %d\n", rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(&checkEnable, &arcInterruptTimeLength);
        printf("WeldingGetCheckArcInterruptionParam checkEnable %d  arcInterruptTimeLength %d\n", checkEnable, arcInterruptTimeLength);
        rtn = robot.WeldingGetReWeldAfterBreakOffParam(&enable, &length, &velocity, &moveType);
        printf("WeldingGetReWeldAfterBreakOffParam enable = %d, length = %lf, velocity = %lf, moveType = %d\n", enable, length, velocity, moveType);
        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            int getCtrlMode = -1;
            robot.SetWeldMachineCtrlMode(0);
            robot.GetWeldMachineCtrlMode(getCtrlMode);
            printf("GetWeldMachineCtrlMode %d\n", getCtrlMode);
            robot.Sleep(1000);
            robot.SetWeldMachineCtrlMode(1);
            robot.GetWeldMachineCtrlMode(getCtrlMode);
            printf("GetWeldMachineCtrlMode %d\n", getCtrlMode);
            robot.Sleep(1000);
        }
        robot.CloseRPC();
        return 0;
    }

Definir Parâmetros de Oscilação em Tempo Real
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define parâmetros de oscilação em tempo real
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @param [in] weaveType Tipo de oscilação 0-oscilação triangular plana; 1-oscilação triangular em L vertical; 2-oscilação circular horária; 3-oscilação circular anti-horária; 4-oscilação senoidal plana; 5-oscilação senoidal em L vertical; 6-oscilação triangular vertical; 7-oscilação senoidal vertical
    * @param [in] weaveFrequency Frequência de oscilação (Hz)
    * @param [in] weaveIncStayTime Modo de espera 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    * @param [in] weaveRange Amplitude de oscilação (mm)
    * @param [in] weaveLeftStayTime Tempo de permanência à esquerda da oscilação (ms)
    * @param [in] weaveRightStayTime Tempo de permanência à direita da oscilação (ms)
    * @param [in] weaveCircleRadio Oscilação circular - taxa de retorno (0-100%)
    * @param [in] weaveStationary Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera; 1-posição permanece estática durante o tempo de espera
    * @return Código de erro
    */
    errno_t WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

Definir Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Define os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô
     * @param [in] checkEnable Se habilita a detecção; 0-não habilita; 1-habilita
     * @param [in] arcInterruptTimeLength Duração de confirmação da interrupção do arco (ms)
     * @return Código de erro
    */
    errno_t WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

Obter Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô
     * @param [out] checkEnable Se habilita a detecção; 0-não habilita; 1-habilita
     * @param [out] arcInterruptTimeLength Duração de confirmação da interrupção do arco (ms)
     * @return Código de erro
    */
    errno_t WeldingGetCheckArcInterruptionParam(int* checkEnable, int* arcInterruptTimeLength);

Definir Parâmetros de Recuperação de Interrupção de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Define os parâmetros de recuperação de interrupção de soldagem do robô
     * @param [in] enable Se habilita a recuperação de interrupção de soldagem
     * @param [in] length Distância de sobreposição da solda (mm)
     * @param [in] velocity Percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100)
     * @param [in] moveType Modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP
     * @return Código de erro
    */
    errno_t WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);

Obter Parâmetros de Recuperação de Interrupção de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém os parâmetros de recuperação de interrupção de soldagem do robô
     * @param [out] enable Se habilita a recuperação de interrupção de soldagem
     * @param [out] length Distância de sobreposição da solda (mm)
     * @param [out] velocity Percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100)
     * @param [out] moveType Modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP
     * @return Código de erro
    */
    errno_t WeldingGetReWeldAfterBreakOffParam(int* enable, double* length, double* velocity, int* moveType);

Definir Porta DO Estendida do Modo de Controle da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a porta DO estendida do modo de controle da máquina de solda
    * @param DONum Porta DO do modo de controle da máquina de solda (0-127)
    * @return Código de erro
    */
    errno_t SetWeldMachineCtrlModeExtDoNum(int DONum);

Definir Modo de Controle da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o modo de controle da máquina de solda
    * @param [in] mode Modo de controle da máquina de solda; 0-modo unário CC; 1-modo unário pulsado; 2-modo JOB; 3-modo controle local; 4-modo separado; 5-modo CC/CV; 6-TIG; 7-CMT
    * @param [in] ioType Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    * @return Código de erro
    */
    errno_t SetWeldMachineCtrlMode(int mode, int ioType = 1);

Obter Modo de Controle da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-V3.9.8
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o modo de controle da máquina de solda
    * @param [out] mode Modo de controle da máquina de solda; 0-modo único CC; 1-modo único pulsado; 2-modo JOB; 3-modo controle local; 4-modo separado; 5-modo CC/CV; 6-TIG; 7-CMT
    * @return Código de erro
    */
    errno_t GetWeldMachineCtrlMode(int& mode);

Início da Soldagem
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início da soldagem
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] arcNum Número do arquivo de configuração da máquina de solda
    * @param [in] timeout Tempo limite de abertura de arco
    * @return Código de erro
    */
    errno_t ARCStart(int ioType, int arcNum, int timeout);

Fim da Soldagem
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Fim da soldagem
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] arcNum Número do arquivo de configuração da máquina de solda
    * @param [in] timeout Tempo limite de extinção do arco
    * @return Código de erro
    */
    errno_t ARCEnd(int ioType, int arcNum, int timeout);

Início da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @return Código de erro
    */
    errno_t WeaveStart(int weaveNum);

Fim da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Fim da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @return Código de erro
    */
    errno_t WeaveEnd(int weaveNum);

Alimentação de Arame para Frente
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Alimentação de arame para frente
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] wireFeed Controle de alimentação de arame 0-parar alimentação; 1-alimentar
    * @return Código de erro
    */
    errno_t SetForwardWireFeed(int ioType, int wireFeed);

Alimentação de Arame para Trás
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Alimentação de arame para trás
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] wireFeed Controle de alimentação de arame 0-parar alimentação; 1-alimentar
    * @return Código de erro
    */
    errno_t SetReverseWireFeed(int ioType, int wireFeed);

Fornecimento de Gás
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Fornecimento de gás
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] airControl Controle de fornecimento de gás 0-parar fornecimento; 1-fornecer
    * @return Código de erro
    */
    errno_t SetAspirated(int ioType, int airControl);

Definir Retomada de Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Define a retomada de soldagem do robô após interrupção
     * @return Código de erro
    */
    errno_t WeldingStartReWeldAfterBreakOff();

Definir Saída da Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
     * @brief Define a saída da soldagem do robô após interrupção
     * @return Código de erro
     */
    errno_t WeldingAbortWeldAfterBreakOff();

Exemplo de Código de Controle de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestWelding(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SetForwardWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetForwardWireFeed(0, 0);
      robot.SetReverseWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetReverseWireFeed(0, 0);
      robot.SetAspirated(0, 1);
      robot.Sleep(1000);
      robot.SetAspirated(0, 0);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.WeaveStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.ARCEnd(1, 0, 10000);
      robot.WeaveEnd(0);
      robot.WeldingStartReWeldAfterBreakOff();
      robot.WeldingAbortWeldAfterBreakOff();
      robot.CloseRPC();
      return 0;
    }

Início da Soldagem por Segmentos
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início da soldagem por segmentos
    * @param [in] startDesePos Posição cartesiana do ponto inicial
    * @param [in] endDesePos Pose cartesiana do ponto final
    * @param [in] startJPos Pose articular do ponto inicial
    * @param [in] endJPos Pose articular do ponto final
    * @param [in] weldLength Comprimento do segmento de solda (mm)
    * @param [in] noWeldLength Comprimento do segmento não soldado (mm)
    * @param [in] weldIOType Tipo de E/S de soldagem (0-E/S da caixa de controle; 1-E/S estendida)
    * @param [in] arcNum Número do arquivo de configuração da máquina de solda
    * @param [in] weldTimeout Tempo limite de abertura/fechamento de arco
    * @param [in] isWeave Se oscila
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @return Código de erro
    */
    errno_t SegmentWeldStart(DescPose *startDesePos, DescPose *endDesePos, JointPos *startJPos, JointPos *endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

Exemplo de Código de Soldagem por Segmentos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    int TestSegWeld(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      rtn = robot.SegmentWeldStart(&p1Desc, &p2Desc, &p1Joint, &p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      printf("SegmentWeldStart rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Início da Oscilação de Simulação
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Início da oscilação de simulação
     * @param [in] weaveNum Número do parâmetro de oscilação
     * @return Código de erro
     */
    errno_t WeaveStartSim(int weaveNum);

Fim da Oscilação de Simulação
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Fim da oscilação de simulação
     * @param [in] weaveNum Número do parâmetro de oscilação
     * @return Código de erro
     */
    errno_t WeaveEndSim(int weaveNum);

Início da Detecção de Alerta de Trajetória (Sem Movimento)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Início da detecção de alerta de trajetória (sem movimento)
     * @param [in] weaveNum Número do parâmetro de oscilação
     * @return Código de erro
     */
    errno_t WeaveInspectStart(int weaveNum);

Fim da Detecção de Alerta de Trajetória (Sem Movimento)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief Fim da detecção de alerta de trajetória (sem movimento)
     * @param [in] weaveNum Número do parâmetro de oscilação
     * @return Código de erro
     */
    errno_t WeaveInspectEnd(int weaveNum);

Início da Mudança Gradual da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief Início da mudança gradual da oscilação
     * @param [in] weaveChangeFlag 1-alterar parâmetro de oscilação; 2-alterar parâmetro de oscilação + velocidade de soldagem
     * @param [in] weaveNum Número da oscilação
     * @param [in] velStart Velocidade inicial de soldagem, (cm/min)
     * @param [in] velEnd Velocidade final de soldagem, (cm/min)
     * @return Código de erro
     */
     errno_t WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

Exemplo de Código de Soldagem com Mudança Gradual de Oscilação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestWeave(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveStartSim(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveEndSim(0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveInspectStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveInspectEnd(0);
      robot.WeldingSetVoltage(1, 19, 0, 0);
      robot.WeldingSetCurrent(1, 190, 0, 0);
      robot.MoveL(&p1Joint, &p1Desc, 1, 1, 100, 100, 50, -1, &exaxisPos, 0, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.WeaveStart(0);
      robot.WeaveChangeStart(1, 0, 50, 30);
      robot.MoveL(&p2Joint, &p2Desc, 1, 1, 100, 100, 1, -1, &exaxisPos, 0, 0, &offdese);
      robot.WeaveChangeEnd();
      robot.WeaveEnd(0);
      robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.ARCEnd(1, 0, 10000);
      robot.CloseRPC();
      return 0;
    }

Fim da Mudança Gradual da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  Fim da mudança gradual da oscilação
     * @return  Código de erro
     */
    errno_t WeaveChangeEnd();

E/S Estendida - Configurar Sinal de Detecção de Gás da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de detecção de gás da máquina de solda
     * @param [in] DONum Número DO estendido do sinal de detecção de gás
     * @return Código de erro
     */
    errno_t SetAirControlExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Abertura de Arco da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de abertura de arco da máquina de solda
     * @param [in] DONum Número DO estendido do sinal de abertura de arco da máquina de solda
     * @return Código de erro
     */
    errno_t SetArcStartExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Alimentação de Arame para Trás da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de alimentação de arame para trás da máquina de solda
     * @param [in] DONum Número DO estendido do sinal de alimentação de arame para trás
     * @return Código de erro
     */
    errno_t SetWireReverseFeedExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Alimentação de Arame para Frente da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de alimentação de arame para frente da máquina de solda
     * @param [in] DONum Número DO estendido do sinal de alimentação de arame para frente
     * @return Código de erro
     */
    errno_t SetWireForwardFeedExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Sucesso de Abertura de Arco da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de sucesso de abertura de arco da máquina de solda
     * @param [in] DINum Número DI estendido do sinal de sucesso de abertura de arco
     * @return Código de erro
     */
    errno_t SetArcDoneExtDiNum(int DINum);

E/S Estendida - Configurar Sinal de Prontidão da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de prontidão da máquina de solda
     * @param [in] DINum Número DI estendido do sinal de prontidão da máquina de solda
     * @return Código de erro
     */
    errno_t SetWeldReadyExtDiNum(int DINum);

E/S Estendida - Configurar Sinal de Recuperação de Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
     * @brief E/S estendida - configurar sinal de recuperação de interrupção de soldagem
     * @param [in] reWeldDINum Número DI estendido do sinal de retomada de soldagem após interrupção
     * @param [in] abortWeldDINum Número DI estendido do sinal de saída de soldagem após interrupção
     * @return Código de erro
     */
    errno_t SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);
    
Obter Configuração da Função DI Estendida
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-V3.9.8
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém a configuração da função DI estendida
     * @param [out] DIConfig Configuração de entrada DI estendida; DIConfig[0]-porta DI estendida máquina de solda pronta;
                                         DIConfig[1]-porta DI estendida início de arco bem-sucedido;
                                            DIConfig[2]-porta DI estendida retomada de interrupção de soldagem;
                                            DIConfig[3]-porta DI estendida saída de interrupção de soldagem;
                                            DIConfig[4]-porta DI estendida busca de fio bem-sucedida;
                                            DIConfig[5]-porta DI estendida status de operação da máquina de solda a laser;
                                            DIConfig[6]-porta DI estendida status de falha da máquina de solda a laser;
                                            DIConfig[7-15]-reservados
    * @return  Código de erro
    */
    errno_t GetExtDIConfig(int DIConfig[16]);
    
Obter Configuração da Função DO Estendida
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-V3.9.8
    
.. code-block:: c++
    :linenos:

    /**
     * @brief Obtém a configuração da função DO estendida
     * @param [out] DOConfig Configuração de saída DO estendida; DOConfig[0]-porta DO estendida início de arco da máquina de solda;
                                            DOConfig[1]-porta DO estendida detecção de gás;
                                            DOConfig[2]-porta DO estendida alimentação de fio para frente;
                                            DOConfig[3]-porta DO estendida alimentação de fio para trás;
                                            DOConfig[4]-porta DO estendida busca de fio;
                                            DOConfig[5]-porta DO estendida modo de controle da máquina de solda;
                                            DOConfig[6]-porta DO estendida habilitação da máquina de solda a laser;
                                            DOConfig[7]-porta DO estendida início da máquina de solda a laser (emissão de laser);
                                            DOConfig[8]-porta DO estendida reinicialização da máquina de solda a laser;
                                            DOConfig[9-15]-reservados
    * @return  Código de erro
    */
    errno_t GetExtDOConfig(int DOConfig[16]);

Exemplo de Código para Configurar Sinais de Soldagem com E/S Estendida
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestExtDIConfig(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);
        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);
        int DIConfig[16] = { 0 };
        int DOConfig[16] = { 0 };
        rtn = robot.GetExtDIConfig(DIConfig);
        printf("GetExtDIConfig rtn is %d\n welder ready %d\narc done %d\nreweld start %d\nabort reweld %d\nwiresearch done %d\nLaser welding State %d\nlaser welding error state %d\n",
            rtn, DIConfig[0], DIConfig[1], DIConfig[2], DIConfig[3], DIConfig[4], DIConfig[5], DIConfig[6]);
        rtn = robot.GetExtDOConfig(DOConfig);
        printf("GetExtDOConfig rtn is %d\n Arc Start %d\nAir Test %d\nWire forward %d\nWire Inverse %d\nwiresearch %d\nWeld Mode %d\nlaser Enable %d\nLaser On %d\nLaser Reset Error %d\n",
            rtn, DOConfig[0], DOConfig[1], DOConfig[2], DOConfig[3], DOConfig[4], DOConfig[5], DOConfig[6], DOConfig[7], DOConfig[8]);
        robot.CloseRPC();
        return 0;
    }

Controle de Rastreamento de Arco
+++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

      /**
      * @brief  Controle de rastreamento de arco
      * @param  [in] flag Chave, 0-desligar; 1-ligar
      * @param  [in] dalayTime Tempo de atraso, em ms
      * @param  [in] isLeftRight Compensação de desvio esquerda/direita
      * @param  [in] klr Coeficiente de ajuste esquerda/direita (sensibilidade);
      * @param  [in] tStartLr Tempo de início da compensação esquerda/direita cyc
      * @param  [in] stepMaxLr Quantidade máxima de compensação por vez esquerda/direita mm
      * @param  [in] sumMaxLr Quantidade máxima total de compensação esquerda/direita mm
      * @param  [in] isUpLow Compensação de desvio acima/abaixo
      * @param  [in] kud Coeficiente de ajuste acima/abaixo (sensibilidade);
      * @param  [in] tStartUd Tempo de início da compensação acima/abaixo cyc
      * @param  [in] stepMaxUd Quantidade máxima de compensação por vez acima/abaixo mm
      * @param  [in] sumMaxUd Quantidade máxima total de compensação acima/abaixo
      * @param  [in] axisSelect Seleção do sistema de coordenadas acima/abaixo, 0-oscilação; 1-ferramenta; 2-base
      * @param  [in] referenceType Modo de definição da corrente de referência acima/abaixo, 0-feedback; 1-constante
      * @param  [in] referSampleStartUd Início da amostragem da corrente de referência acima/abaixo (feedback);, cyc
      * @param  [in] referSampleCountUd Contagem do ciclo de amostragem da corrente de referência acima/abaixo (feedback);, cyc
      * @param  [in] referenceCurrent Corrente de referência acima/abaixo mA
      * @param  [in] offsetType Tipo de rastreamento com deslocamento, 0-sem deslocamento; 1-amostragem; 2-percentagem
      * @param  [in] offsetParameter Parâmetro de deslocamento; amostragem (tempo de início da amostragem de deslocamento, padrão um ciclo); percentagem (percentagem de deslocamento (-100 ~ 100))
      * @return  Código de erro
      */
     errno_t ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType = 0, int offsetParameter = 0);

Configurar Porta de Sinal de Entrada de Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  Configurar porta de sinal de entrada de rastreamento de arco
      * @param  [in] channel Banda de passagem AI do rastreamento de arco, [0-3]
      * @return  Código de erro
      */
     errno_t ArcWeldTraceExtAIChannelConfig(int channel);

Ativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Ativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes
    * @return Código de erro
    */
    errno_t ArcWeldTraceReplayStart();

Desativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Desativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes
    * @return Código de erro
    */
    errno_t ArcWeldTraceReplayEnd();

Mudança de Coordenadas de Deslocamento - Soldagem de Múltiplas Camadas e Múltiplos Passes
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Mudança de coordenadas de deslocamento - soldagem de múltiplas camadas e múltiplos passes
    * @return Código de erro
    */
    errno_t MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, DescPose& offset);

Exemplo de Código de Rastreamento de Arco com Soldagem de Múltiplas Camadas e Múltiplos Passes
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestArcWeldTrace(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      JointPos mulitilineorigin1_joint(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
      DescPose mulitilineorigin1_desc(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);
      DescTran mulitilineX1_desc;
      mulitilineX1_desc.x = -677.556;
      mulitilineX1_desc.y = 211.949;
      mulitilineX1_desc.z = -1.206;
      DescTran mulitilineZ1_desc;
      mulitilineZ1_desc.x = -677.564;
      mulitilineZ1_desc.y = 190.956;
      mulitilineZ1_desc.z = 19.817;
      JointPos mulitilinesafe_joint(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
      DescPose mulitilinesafe_desc(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
      JointPos mulitilineorigin2_joint(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
      DescPose mulitilineorigin2_desc(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);
      DescTran mulitilineX2_desc;
      mulitilineX2_desc.x = -563.965;
      mulitilineX2_desc.y = 220.355;
      mulitilineX2_desc.z = -0.680;
      DescTran mulitilineZ2_desc;
      mulitilineZ2_desc.x = -563.968;
      mulitilineZ2_desc.y = 215.362;
      mulitilineZ2_desc.z = 4.331;
      ExaxisPos epos(0, 0, 0, 0);
      DescPose offset(0, 0, 0, 0, 0, 0);
      robot.Sleep(10);
      int error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.WeaveStart(0);
      printf("WeaveStart return: %d\n", error);
      error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.WeaveEnd(0);
      printf("WeaveEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("ArcWeldTraceReplayStart return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 3000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      robot.CloseRPC();
      return 0;
    }

Seleção do Canal AI de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Seleção do canal AI de feedback de corrente da máquina de solda para rastreamento de arco
     * @param [in]  channel Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1
     * @return Código de erro
     */
     errno_t ArcWeldTraceAIChannelCurrent(int channel);

Seleção do Canal AI de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief Seleção do canal AI de feedback de tensão da máquina de solda para rastreamento de arco
     * @param [in]  channel Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1
     * @return Código de erro
     */
     errno_t ArcWeldTraceAIChannelVoltage(int channel);

Parâmetros de Conversão de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
      * @brief Parâmetros de conversão de feedback de corrente da máquina de solda para rastreamento de arco
      * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
      * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
      * @param [in] currentLow Valor de corrente da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
      * @param [in] currentHigh Valor de corrente da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]
      * @return Código de erro
      */
     errno_t ArcWeldTraceCurrentPara(float AILow, float AIHigh, float currentLow, float currentHigh);

Parâmetros de Conversão de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
      * @brief Parâmetros de conversão de feedback de tensão da máquina de solda para rastreamento de arco
      * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
      * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
      * @param [in] voltageLow Valor de tensão da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
      * @param [in] voltageHigh Valor de tensão da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]
      * @return Código de erro
      */
      errno_t ArcWeldTraceVoltagePara(float AILow, float AIHigh, float voltageLow, float voltageHigh);

Exemplo de Código de Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int WeldTraceControlWithCtrlBoxAI(FRRobot* robot)
    {
      DescPose startdescPose = { -473.86, 257.879, -20.849, -37.317, -42.021, 2.543 };
      JointPos startjointPos = { -43.487, -76.526, 95.568, -104.445, -89.356, 3.72 };

      DescPose enddescPose = { -499.844, 141.225, 7.72, -34.856, -40.17, 13.13 };
      JointPos endjointPos = { -31.305, -82.998, 99.401, -104.426, -89.35, 3.696 };

      DescPose safedescPose = { -504.043, 275.181, 40.908, -28.002, -42.025, -14.044 };
      JointPos safejointPos = { -39.078, -76.732, 87.227, -99.47, -94.301, 18.714 };

      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);

      robot->WeldingSetVoltage(0, 25, 1, 0);// ----definir tensão
      robot->WeldingSetCurrent(0, 260, 0, 0);// ----definir corrente

      int rtn = robot->ArcWeldTraceAIChannelCurrent(4);
      cout << "ArcWeldTraceAIChannelCurrent rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceAIChannelVoltage(5);
      cout << "ArcWeldTraceAIChannelVoltage rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceCurrentPara(0, 5, 0, 500);
      cout << "ArcWeldTraceCurrentPara rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceVoltagePara(1.018, 10, 0, 50);
      cout << "ArcWeldTraceVoltagePara rtn is " << rtn << endl;
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      return 0;
    }

Definir Portas E/S Estendidas para Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define as portas E/S estendidas para busca de posição do arame de solda
    * @param searchDoneDINum Porta DO de sucesso na busca de posição do arame (0-127)
    * @param searchStartDONum Porta DO de controle de início/parada da busca de posição do arame (0-127)
    * @return Código de erro
    */
    errno_t SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

Programa de Exemplo
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    void TestUDPWireSearch(FRRobot* robot)
    {
    robot->ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
    robot->ExtDevLoadUDPDriver();

    robot->SetWireSearchExtDIONum(0, 0);

    int rtn0, rtn1, rtn2 = 0;
    ExaxisPos exaxisPos = { 0.0, 0.0, 0.0, 0.0 };
    DescPose offdese = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };

    DescPose descStart = { -158.767, -510.596, 271.709, -179.427, -0.745, -137.349 };
    JointPos jointStart = { 61.667, -79.848, 108.639, -119.682, -89.700, -70.985 };

    DescPose descEnd = { 0.332, -516.427, 270.688, 178.165, 0.017, -119.989 };
    JointPos jointEnd = { 79.021, -81.839, 110.752, -118.298, -91.729, -70.981 };

    robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);

    DescPose descREF0A = { -66.106, -560.746, 270.381, 176.479, -0.126, -126.745 };
    JointPos jointREF0A = { 73.531, -75.588, 102.941, -116.250, -93.347, -69.689 };

    DescPose descREF0B = { -66.109, -528.440, 270.407, 176.479, -0.129, -126.744 };
    JointPos jointREF0B = { 72.534, -79.625, 108.046, -117.379, -93.366, -70.687 };

    DescPose descREF1A = { 72.975, -473.242, 270.399, 176.479, -0.129, -126.744 };
    JointPos jointREF1A = { 87.169, -86.509, 115.710, -117.341, -92.993, -56.034 };

    DescPose descREF1B = { 31.355, -473.238, 270.405, 176.480, -0.130, -126.745 };
    JointPos jointREF1B = { 82.117, -87.146, 116.470, -117.737, -93.145, -61.090 };

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
    rtn1 = robot->WireSearchWait("REF0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
    rtn1 = robot->WireSearchWait("REF1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
    rtn1 = robot->WireSearchWait("RES0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
    rtn1 = robot->WireSearchWait("RES1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
    vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
    int offectFlag = 0;
    DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
    rtn0 = robot->GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
    robot->PointsOffsetEnable(0, &offectPos);
    robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->PointsOffsetDisable();
    }

Início da Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  Início da busca de posição do arame de solda
    * @param  [in] refPos  1-ponto de referência 0-ponto de contato
    * @param  [in] searchVel   Velocidade de busca %
    * @param  [in] searchDis  Distância de busca mm
    * @param  [in] autoBackFlag Flag de retorno automático, 0-não automático; -automático
    * @param  [in] autoBackVel  Velocidade de retorno automático %
    * @param  [in] autoBackDis  Distância de retorno automático mm
    * @param  [in] offectFlag  1-busca com deslocamento; 0-busca no ponto ensinado
    * @return  Código de erro
    */
     errno_t WireSearchStart(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

Fim da Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  Fim da busca de posição do arame de solda
      * @param  [in] refPos  1-ponto de referência 2-ponto de contato
      * @param  [in] searchVel   Velocidade de busca %
      * @param  [in] searchDis  Distância de busca mm
      * @param  [in] autoBackFlag Flag de retorno automático, 0-não automático; -automático
      * @param  [in] autoBackVel  Velocidade de retorno automático %
      * @param  [in] autoBackDis  Distância de retorno automático mm
      * @param  [in] offectFlag  1-busca com deslocamento; 2-busca no ponto ensinado
      * @return  Código de erro
      */
     errno_t WireSearchEnd(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

Calcular Deslocamento da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  Calcular deslocamento da busca de posição do arame de solda
      * @param  [in] seamType  Tipo de solda
      * @param  [in] method   Método de cálculo
      * @param  [in] varNameRef Pontos de referência 1-6, "#" indica ausência de ponto variável
      * @param  [in] varNameRes Pontos de contato 1-6, "#" indica ausência de ponto variável
      * @param  [out] offectFlag 0-deslocamento adicionado diretamente ao ponto de comando; 1-deslocamento requer transformação de coordenadas do ponto de comando
      * @param  [out] offect Deslocamento da pose [x, y, z, a, b, c]
      * @return  Código de erro
      */
     errno_t GetWireSearchOffset(int seamType, int method, std::vector<std::string> varNameRef, std::vector<std::string> varNameRes, int& offectFlag, DescPose& offect);

Aguardar Conclusão da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  Aguardar conclusão da busca de posição do arame de solda
      * @return  Código de erro
      */
     errno_t WireSearchWait(std::string varName);

Escrever Ponto de Contato da Busca de Posição do Arame no Banco de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  Escrever ponto de contato da busca de posição do arame no banco de dados
      * @param  [in] varName  Nome do ponto de contato "RES0" ~ "RES99"
      * @param  [in] pos  Dados do ponto de contato [x, y, x, a, b, c]
      * @return  Código de erro
      */
     errno_t SetPointToDatabase(std::string varName, DescPose pos);

Exemplo de Código de Busca de Posição do Arame de Solda do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    int TestWireSearch(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose toolCoord(0, 0, 200, 0, 0, 0);
      robot.SetToolCoord(1, &toolCoord, 0, 0, 1, 0);
      DescPose wobjCoord(0, 0, 0, 0, 0, 0);
      robot.SetWObjCoord(1, &wobjCoord, 0);
      int rtn0, rtn1, rtn2 = 0;
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      DescPose descStart = { 216.543, 445.175, 93.465, 179.683, 1.757, -112.641 };
      JointPos jointStart = { -128.345, -86.660, 114.679, -119.625, -89.219, 74.303 };
      DescPose descEnd = { 111.143, 523.384, 87.659, 179.703, 1.835, -97.750 };
      JointPos jointEnd = { -113.454, -81.060, 109.328, -119.954, -89.218, 74.302 };
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      DescPose descREF0A = { 142.135, 367.604, 86.523, 179.728, 1.922, -111.089 };
      JointPos jointREF0A = { -126.794, -100.834, 128.922, -119.864, -89.218, 74.302 };
      DescPose descREF0B = { 254.633, 463.125, 72.604, 179.845, 2.341, -114.704 };
      JointPos jointREF0B = { -130.413, -81.093, 112.044, -123.163, -89.217, 74.303 };
      DescPose descREF1A = { 92.556, 485.259, 47.476, -179.932, 3.130, -97.512 };
      JointPos jointREF1A = { -113.231, -83.815, 119.877, -129.092, -89.217, 74.303 };
      DescPose descREF1B = { 203.103, 583.836, 63.909, 179.991, 2.854, -103.372 };
      JointPos jointREF1B = { -119.088, -69.676, 98.692, -121.761, -89.219, 74.303 };
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
      rtn1 = robot.WireSearchWait("REF0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
      rtn1 = robot.WireSearchWait("REF1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
      rtn1 = robot.WireSearchWait("RES0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //ponto inicial
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //ponto de direção
      rtn1 = robot.WireSearchWait("RES1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
      vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
      int offectFlag = 0;
      DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
      rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
      robot.PointsOffsetEnable(0, &offectPos);
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);
      robot.PointsOffsetDisable();
      robot.CloseRPC();
      return 0;

Definir Início da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     /**
      * @brief Define o início da mudança gradual da tensão de soldagem
      * @param [in] IOType Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
      * @param [in] voltageStart Tensão de soldagem inicial (V)
      * @param [in] voltageEnd Tensão de soldagem final (V)
      * @param [in] AOIndex Número da porta AO da caixa de controle (0-1)
      * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
      * @return Código de erro
      */
      errno_t WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

Definir Fim da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     /**
      * @brief Define o fim da mudança gradual da tensão de soldagem
      * @return Código de erro
      */
     errno_t WeldingSetVoltageGradualChangeEnd();

Definir Início da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     /**
      * @brief Define o início da mudança gradual da corrente de soldagem
      * @param [in] IOType Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
      * @param [in] voltageStart Corrente de soldagem inicial (A)
      * @param [in] voltageEnd Corrente de soldagem final (A)
      * @param [in] AOIndex Número da porta AO da caixa de controle (0-1)
      * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
      * @return Código de erro
      */
     errno_t WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

Definir Fim da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief Define o fim da mudança gradual da corrente de soldagem
     * @return Código de erro
    */
    errno_t WeldingSetCurrentGradualChangeEnd();

Exemplo de Código de Mudança Gradual de Corrente e Tensão de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int WeldparamChange(FRRobot* robot)
    {
      DescPose startdescPose = { -484.707, 276.996, -14.013, -37.657, -40.508, -1.548 };
      JointPos startjointPos = { -45.421, -75.673, 93.627, -104.302, -87.938, 6.005 };

      DescPose enddescPose = { -508.767, 137.109, -13.966, -37.639, -40.508, -1.559 };
      JointPos endjointPos = { -32.768, -80.947, 100.254, -106.201, -87.201, 18.648 };

      DescPose safedescPose = { -484.709, 294.436, 13.621, -37.660, -40.508, -1.545 };
      JointPos safejointPos = { -46.604, -75.410, 89.109, -100.003, -88.012, 4.823 };
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      int rtn = robot->WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
      cout << "WeldingSetCurrentGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
      cout << "WeldingSetVoltageGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);

      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->WeaveChangeStart(2, 1, 24, 36);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveChangeEnd();
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      robot->WeldingSetCurrentGradualChangeEnd();
      robot->WeldingSetVoltageGradualChangeEnd();
      return 0;
    }

Definir Parâmetros de Oscilação Personalizada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Define parâmetros de oscilação personalizada
    * @param [in] id Número da oscilação personalizada: 0-2
    * @param [in] pointNum Número de pontos de oscilação 0-10
    * @param [in] point Dados do ponto de extremidade de movimento x, y, z
    * @param [in] stayTime Tempo de permanência da oscilação ms
    * @param [in] frequency Frequência de oscilação Hz
    * @param [in] incStayType Modo de espera: 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    * @param [in] stationary Espera na posição de oscilação: 0-continua movimento durante o tempo de espera; 1-posição permanece estática durante o tempo de espera
    * @return Código de erro
    */
    errno_t CustomWeaveSetPara(int id, int pointNum, DescTran point[10], double stayTime[10], double frequency, int incStayType, int stationary);

Obter Parâmetros de Oscilação Personalizada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém parâmetros de oscilação personalizada
    * @param [in] id Número da oscilação personalizada: 0-2
    * @param [out] pointNum Número de pontos de oscilação 0-10
    * @param [out] point Dados do ponto de extremidade de movimento x, y, z
    * @param [out] stayTime Tempo de permanência da oscilação ms
    * @param [out] frequency Frequência de oscilação Hz
    * @param [out] incStayType Modo de espera: 0-ciclo não inclui tempo de espera; 1-ciclo inclui tempo de espera
    * @param [out] stationary Espera na posição de oscilação: 0-continua movimento durante o tempo de espera; 1-posição permanece estática durante o tempo de espera
    * @return Código de erro
    */
    errno_t CustomWeaveGetPara(int id, int& pointNum, DescTran point[10], double stayTime[10], double& frequency, int& incStayType, int& stationary);

Exemplo de Código de Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6

.. code-block:: c++
    :linenos:

    int TestCustomWeaveSetPara()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescTran point[10] = {};
      point[0].x = -3;
      point[0].y = -3;
      point[0].z = 0;
      point[1].x = -6;
      point[1].y = 0;
      point[1].z = 0;
      point[2].x = -3;
      point[2].y = 3;
      point[2].z = 0;
      point[3].x = 0;
      point[3].y = 0;
      point[3].z = 0;
      double stayTime[10] = { 0,0,0,0,0,0,0,0,0,0 };
      rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0);
      printf("CustomWeaveSetPara rtn is %d\n", rtn);
      robot.Sleep(1000);
      int pointNum = 0;
      double frequency;
      int incStayType;
      int stationary;
      robot.CustomWeaveGetPara(2, pointNum, point, stayTime, frequency, incStayType, stationary);
      printf("pointNum is %d\n", pointNum);
      for (int i = 0; i < pointNum; i++)
      {
        printf("point %d, point x y z %f %f %f\n", i, point[i].x, point[i].y, point[i].z);
      }
      printf("fre is %f, stay is %d %d \n", frequency, incStayType, stationary);
      robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
      DescPose desc_p1 = { -288.650, 367.807, 288.404, 0.000, -0.001, 0.001 };
      DescPose desc_p2 = { -431.714, 367.815, 288.415, 0.001, 0.001, 0.000 };
      DescPose desc_p3 = { -348.666, 427.798, 288.404, -0.000, -0.000, 0.001 };
      JointPos j1 = { 140.656, -84.560, -91.707, -93.734, 90.000, 50.655 };
      JointPos j2 = { 149.873, -98.298, -77.599, -94.103, 90.000, 59.873 };
      JointPos j3 = { 139.773, -96.173, -80.014, -93.814, 90.000, 49.772 };
      ExaxisPos epos = {};
      DescPose offset_pos = {};
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.Circle(&j3, &desc_p3, 3, 0, 100, 100, &epos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 10, -1, &offset_pos);
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveC(&j3, &desc_p3, 3, 0, 100, 100, &epos, 0, &offset_pos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 0, &offset_pos, 10, -1);
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveL(&j2, &desc_p2, 3, 0, 100, 100, 10, -1, &epos, 0, 0, &offset_pos, 0, 100);
      robot.WeaveEnd(0);
      robot.CloseRPC();
    }

Configuração de Parâmetros da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configuração de parâmetros da soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] Número do grupo a ser configurado (1~10)
    * @param[in] scanSpeed Velocidade de varredura
    * @param[in] scanWidth Largura de varredura
    * @param[in] peakPower Potência de pico
    * @param[in] dutyCycle Ciclo de trabalho
    * @param[in] freq Frequência
    * @return Código de erro
    */
    errno_t SetLaserWeldingParam(int io_type, int num, int scanSpeed, int scanWidth, int peakPower, int dutyCycle, int freq);

Iniciar/Parar Soldagem a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Iniciar/parar soldagem a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status Palavra de controle 0-desligar laser 1-ligar laser
    * @param[in] max_waittime Tempo máximo de espera em milissegundos, padrão 10000
    * @return Código de erro
    */
    errno_t SetLaserWeldingStartEnd(int io_type, int status, int max_waittime = 10000);

Habilitar/Desabilitar Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Habilitar/desabilitar soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status 0-desabilitar 1-habilitar
    * @return Código de erro
    */
    errno_t SetLaserWeldingEnable(int io_type, int status);

Reset de Falha da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Reset de falha da soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status Palavra de controle 0-inválido 1-reset de falha
    * @return Código de erro
    */
    errno_t ResetLaserWeldingErr(int io_type, int status);

Obter Estado de Operação da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obter estado de operação da soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] status Palavra de controle 0-parado 1-operando
    * @return Código de erro
    */
    errno_t GetLaserWeldingRunningState(int io_type, int& status);

Obter Estado de Falha da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obter estado de falha da soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] status 0-sem falha 1-com falha
    * @return Código de erro
    */
    errno_t GetLaserWeldingErrState(int io_type, int& status);

Obter Parâmetros de Configuração da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obter parâmetros de configuração da soldadora a laser
    * @param[in] Número do grupo a ser configurado (1~10)
    * @param[out] scanSpeed Velocidade de varredura
    * @param[out] scanWidth Largura de varredura
    * @param[out] peakPower Potência de pico
    * @param[out] dutyCycle Ciclo de trabalho
    * @param[out] freq Frequência
    * @return Código de erro
    */
    errno_t GetLaserWeldingParamTarget(int num, int& scanSpeed, int& scanWidth, int& peakPower, int& dutyCycle, int& freq);

Obter Parâmetros de Configuração Ativos da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obter parâmetros de configuração ativos da soldadora a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] scanSpeed Velocidade de varredura
    * @param[out] scanWidth Largura de varredura
    * @param[out] peakPower Potência de pico
    * @param[out] dutyCycle Ciclo de trabalho
    * @param[out] freq Frequência
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t GetLaserWeldingParamActual(int io_type, int& scanSpeed, int& scanWidth, int& peakPower, int& dutyCycle, int& freq);

Configurar Porta DO de E/S Expansão para Habilitar Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para habilitar soldadora a laser
    * @param[in] ctrlModeDONum Número da porta DO de E/S expansão para habilitar a soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t SetLaserWeldingEnableExtDoNum(int ctrlModeDONum);

Configurar Porta DO de E/S Expansão para Iniciar Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para iniciar soldadora a laser
    * @param[in] ctrlModeDONum Número da porta DO de E/S expansão para iniciar/parar a soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t SetLaserWeldingStartExtDoNum(int ctrlModeDONum);

Configurar Porta DO de E/S Expansão para Reset de Falha da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para reset de falha da soldadora a laser
    * @param[in] ctrlModeDONum Número da porta DO de E/S expansão para reset de falha da soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t SetLaserWeldingErrResetExtDoNum(int ctrlModeDONum);

Configurar Porta DI de E/S Expansão para Estado de Operação (Laser Ligado) da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configurar porta DI de E/S expansão para estado de operação (laser ligado) da soldadora a laser
    * @param[in] diNum Número da porta DI de E/S expansão para estado de operação da soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t SetLaserWeldingRunningStateExtDiNum(int diNum);

Configurar Porta DI de E/S Expansão para Estado de Falha da Soldadora a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configurar porta DI de E/S expansão para estado de falha da soldadora a laser
    * @param[in] diNum Número da porta DI de E/S expansão para estado de falha da soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    errno_t SetLaserWeldingErrStateExtDiNum(int diNum);

Exemplo de Código de Soldagem a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLaserWeld()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 300000, 500);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        rtn = robot.ExtDevLoadUDPDriver();
        if (rtn != 0) 
        {
            std::cout << "Falha ao carregar driver UDP, código de erro: " << rtn << std::endl;
        }
        robot.Sleep(1000);
        rtn = robot.SetLaserWeldingParam(1, 3, 2000, 3, 1500, 100, 1000);
        if (rtn != 0) 
        {
            std::cout << "SetLaserWeldingParam falhou, código de erro: " << rtn << std::endl;
        }
        else 
        {
            std::cout << "SetLaserWeldingParam sucesso" << std::endl;
        }
        rtn = robot.SetLaserWeldingStartExtDoNum(1);
        if (rtn != 0) 
        {
            std::cout << "SetLaserWeldingStartExtDoNum falhou, código de erro: " << rtn << std::endl;
        }
        rtn = robot.Mode(0);
        if (rtn != 0) 
        {
            std::cout << "Falha ao definir modo 0, código de erro: " << rtn << std::endl;
        }
        robot.Sleep(1000);
        DescPose desc_pos1(-303.721, -206.960, 297.105, 152.209, 19.857, 109.166);
        DescPose desc_pos2(-301.575, -254.888, 284.786, 155.919, 26.946, 111.629);
        DescPose desc_safe(-344.386, -280.830, 435.073, 173.835, 15.333, 124.931);
        JointPos jointPos1(9.827, -99.740, 120.088, -78.900, -77.241, -17.904);
        JointPos jointPos2(15.251, -96.456, 120.138, -84.664, -68.542, -17.843);
        JointPos jointSafe(19.142, -98.078, 101.493, -83.078, -77.070, -17.794);
        ExaxisPos exaxis(0.0, 0.0, 0.0, 0.0);
        DescPose offset(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int error = robot.MoveL(&desc_pos1,0, 0, 100, 100, 100, -1, 0, &exaxis, 0, 0, &offset, -1, 0);
        std::cout << "MoveL para pos1 retorno: " << error << std::endl;
        rtn = robot.SetLaserWeldingStartEnd(1, 1, 10000);
        if (rtn != 0)
        {
            std::cout << "SetLaserWeldingStartEnd (iniciar) falhou, código de erro: " << rtn << std::endl;
        }
        else 
        {
            std::cout << "Laser iniciado" << std::endl;
        }
        rtn = robot.MoveL(&desc_pos2,0, 0, 30, 100, 100, -1, 0, &exaxis, 0, 0, &offset, -1, 0);
        std::cout << "MoveL para pos2 retorno: " << rtn << std::endl;
        rtn = robot.SetLaserWeldingStartEnd(1, 0, 10000);
        if (rtn != 0)
        {
            std::cout << "SetLaserWeldingStartEnd (parar) falhou, código de erro: " << rtn << std::endl;
        }
        else 
        {
            std::cout << "Laser parado" << std::endl;
        }
        robot.Sleep(500);
        rtn = robot.MoveL(&desc_safe, 0, 0, 100, 100, 100, -1, 0, &exaxis, 0, 0, &offset, -1, 0);
        std::cout << "MoveL para safe_pos retorno: " << rtn << std::endl;
        rtn = robot.Mode(1);
        if (rtn != 0) 
        {
            std::cout << "Falha ao definir modo 1, código de erro: " << rtn << std::endl;
        }
        robot.Sleep(1000);
        robot.CloseRPC();
        robot.Sleep(1000);
        std::cout << "Teste concluído" << std::endl;
        return 0;
    }

Definir Retorno ao Ponto Zero do Ciclo ao Final da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define se retorna ao ponto zero do ciclo ao final da oscilação
    * @param [in] flag Se retorna ao ponto zero do ciclo ao final da oscilação; 0-não retornar; 1-retornar ao ponto zero do ciclo
    * @return Código de erro
    */
    errno_t SetWeaveBackCenterConfig(int flag);
            
Obter Parâmetros de Retorno ao Ponto Zero do Ciclo ao Final da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os parâmetros de retorno ao ponto zero do ciclo ao final da oscilação
    * @param [out] flag Se retorna ao ponto zero do ciclo ao final da oscilação; 0-não retornar; 1-retornar ao ponto zero do ciclo
    * @return Código de erro
    */
    errno_t GetWeaveBackCenterConfig(int& flag);
            
Exemplo de Código de Retorno ao Ponto Zero do Ciclo ao Final da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSplineWeaveBackCenter()
    {
    ROBOT_STATE_PKG pkg = {};
    FRRobot robot;
    robot.LoggerInit();
    robot.SetLoggerLevel(1);
    robot.SetReConnectParam(true, 30000, 500);
    int rtn = robot.SetCmdRpyCallback(UDPFrameCallBack);
    printf("SetCmdRpyCallback rtn is %d\n", rtn);
    rtn = robot.RPC("192.168.58.2");
    if (rtn != 0)
    {
        return -1;
    }
    JointPos j1(9.000, -66.067, 67.706, -103.217, -90.151, 100.669);
    JointPos j2(-4.660, -107.973, 103.734, -76.214, -89.999, 90.886);
    JointPos j3(-36.762, -77.380, 91.364, -127.159, -90.024, 54.833);
    JointPos j4(-62.875, -89.460, 86.437, -77.030, -90.012, 31.539);
    DescPose desc_pos1(-654.129, -235.344, 246.543, 6.010, -11.535, -176.787);
    DescPose desc_pos2(-273.710, -100.871, 280.935, 5.692, 9.522, 179.512);
    DescPose desc_pos3(-566.093, 311.278, 215.008, -10.453, -17.486, -174.209);
    DescPose desc_pos4(-246.558, 328.240, 292.173, 13.912, 4.437, -179.067);
    DescPose offset_pos(0, 0, 0, 0, 0, 0);
    ExaxisPos epos(0, 0, 0, 0);
    int tool = 2;
    int user = 0;
    float vel = 100.0;
    float acc = 100.0;
    float ovl = 20;
    float oacc = 100.0;
    float blendT = 0.0;
    float blendR = 0.0;
    uint8_t flag = 0;
    uint8_t search = 0;
    int blendMode = 0;
    int velAccMode = 0;
    robot.SetSpeed(1);
    robot.SetWeaveBackCenterConfig(1);
    int weaveBackConfig = 0;
    robot.GetWeaveBackCenterConfig(weaveBackConfig);
    printf("GetWeavebackCenterConfig %d: \n", weaveBackConfig);
    rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, 100.0, &epos, blendT, flag, &offset_pos);
    robot.WeaveStart(0);
    robot.NewSplineStart(0, 6000);
    robot.NewSplinePoint(&j1, &desc_pos1, tool, user, vel, acc, ovl, -1, 0);
    robot.NewSplinePoint(&j2, &desc_pos2, tool, user, vel, acc, ovl, -1, 0);
    robot.NewSplinePoint(&j3, &desc_pos3, tool, user, vel, acc, ovl, -1, 0);
    robot.NewSplinePoint(&j4, &desc_pos4, tool, user, vel, acc, ovl, -1, 1);
    robot.NewSplineEnd();
    }

Definir Deslocamento em Tempo Real da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define o deslocamento em tempo real da oscilação
    * @param [in] offset Deslocamento em tempo real [mm, °]
    * @return Código de erro
    */
    errno_t SetWeaveOffsetRT(DescPose offset);

Exemplo de Código de Velocidade e Deslocamento em Tempo Real da Oscilação
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestWeaveSpeedAndOffset()
    {
    ROBOT_STATE_PKG pkg = {};
    FRRobot robot;
    robot.LoggerInit();
    robot.SetLoggerLevel(1);
    robot.SetReConnectParam(true, 30000, 500);
    int rtn = robot.RPC("192.168.58.2");
    if (rtn != 0)
    {
        return 0;
    }
        std::cout << "============================================================" << std::endl;
    std::cout << " Teste de Velocidade e Deslocamento em Tempo Real da Oscilação" << std::endl;
    std::cout << "============================================================" << std::endl;
    ExaxisPos epos(0, 0, 0, 0);
    DescPose offset_pos(0, 0, 0, 0, 0, 0);
    JointPos j1(5.027, -84.331, -75.139, -103.690, 86.379, 20.794);
    DescPose d1(324.752, -83.339, 366.314, -172.321, -0.936, -106.047);
    JointPos j2(-35.335, -117.598, -57.174, -95.234, 90.001, -19.560);
    DescPose d2(324.999, -355.439, 260.000, 179.995, 0.003, -105.775);
    JointPos j3(59.787, -117.594, -57.183, -95.222, 90.006, 75.562);
    DescPose d3(324.998, 355.441, 260.002, 179.995, 0.003, -105.775);
    // ---- Step 1: MoveJ para o ponto inicial ----
    std::cout << "\nStep 1: MoveJ to start point" << std::endl;
    rtn = robot.MoveJ(&j1, &d1, 1, 0, 100, 100, 50, &epos, -1, 0, &offset_pos);
    std::cout << " MoveJ(j1) rtn=" << rtn << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    // ---- Step 2: MoveJ para o ponto de entrada da oscilação ----
    std::cout << "\nStep 2: MoveJ to weave entry point" << std::endl;
    rtn = robot.MoveJ(&j2, &d2, 1, 0, 100, 100, 50, &epos, -1, 0, &offset_pos);
    std::cout << " MoveJ(j2) rtn=" << rtn << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    // ---- Step 3: WeaveStart, inicia thread MoveL da oscilação ----
    std::cout << "\nStep 3: WeaveStart + MoveL in background thread" << std::endl;
    robot.WeaveStart(0);
    std::atomic<bool> weaveRunning(true);
    std::thread weaveThread([&]() {
        rtn = robot.MoveL(&j3, &d3, 1, 0, 100, 100, 5, -1, 0, &epos, 0, 0, &offset_pos, 5, 0, 0, 10);
        std::cout << " MoveL(weave) thread finished, rtn=" << rtn << std::endl;
        weaveRunning = false;
        });
    weaveThread.detach(); // Execução em segundo plano
    std::this_thread::sleep_for(std::chrono::milliseconds(500)); // Aguarda o início do movimento
    // ---- Step 4: Teste de velocidade (thread principal, MoveL oscilação em segundo plano) ----
    std::cout << "\nStep 4: SetSpeed test during weaving" << std::endl;
    std::vector<int> speedValues = { 20, 50, 80, 30, 60, 10 };
    for (int speed : speedValues)
    {
        if (!weaveRunning.load()) break;
        rtn = robot.SetSpeedInstant(speed);
        robot.GetRobotRealTimeState(&pkg);
        std::cout << " SetSpeed(" << speed << ") -> rtn=" << rtn
        << ", TCP_CmpSpeed=" << pkg.target_TCP_CmpSpeed << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    // ---- Step 5: Teste de deslocamento SetWeaveOffsetRT (thread principal, MoveL oscilação em segundo plano) ----
    std::cout << "\nStep 5: SetWeaveOffsetRT test (50 iterations, delta=0.1)" << std::endl;
    double accumOffset = 0.0;
    for (int i = 0; i < 50 && weaveRunning.load(); i++)
    {
        accumOffset += 1;
        DescPose weaveOffset(0, 0, accumOffset, 0, 0, 0);
        rtn = robot.SetWeaveOffsetRT(weaveOffset);
        robot.GetRobotRealTimeState(&pkg);
        std::cout << " [" << (i + 1) << "/50] SetWeaveOffsetRT(x=" << accumOffset << ") -> rtn=" << rtn
        << ", TCP_pos=(" << pkg.tl_cur_pos[0] << "," << pkg.tl_cur_pos[1] << "," << pkg.tl_cur_pos[2] << ")"
        << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
    // ---- Step 6: Aguarda a conclusão do MoveL oscilação, depois WeaveEnd ----
    std::cout << "\nStep 6: Wait for weave MoveL, then WeaveEnd" << std::endl;
    // Como detach foi usado, aguarda weaveRunning se tornar false
    while (weaveRunning.load()) 
    {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    robot.WeaveEnd(0);
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    // ---- Step 7: MoveL de retorno ao ponto inicial ----
    std::cout << "\nStep 7: MoveL back to start" << std::endl;
    rtn = robot.MoveL(&j1, &d1, 1, 0, 100, 100, 50, -1, 0, &epos, 0, 0, &offset_pos, 50, 0, 0, 10);
    std::cout << " MoveL(back) rtn=" << rtn << std::endl;
    robot.GetRobotRealTimeState(&pkg);
    std::cout << "\n Final robot state: main_code=" << pkg.main_code
        << ", sub_code=" << pkg.sub_code << std::endl;
    std::cout << "============================================================" << std::endl;
    std::cout << " Teste de Velocidade e Deslocamento em Tempo Real da Oscilação Concluído" << std::endl;
    std::cout << "============================================================" << std::endl;
    }