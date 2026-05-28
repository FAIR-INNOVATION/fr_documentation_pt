Soldagem do Robô
======================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros da Curva do Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Define os parâmetros da curva do processo de soldagem
    * @param  [in] id Número do processo de soldagem (1-99)
    * @param  [in] startCurrent Corrente de partida do arco (A)
    * @param  [in] startVoltage Tensão de partida do arco (V)
    * @param  [in] startTime Tempo de partida do arco (ms)
    * @param  [in] weldCurrent Corrente de soldagem (A)
    * @param  [in] weldVoltage Tensão de soldagem (V)
    * @param  [in] endCurrent Corrente de parada do arco (A)
    * @param  [in] endVoltage Tensão de parada do arco (V)
    * @param  [in] endTime Tempo de parada do arco (ms)
    * @return  Código de erro
    */
    int WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

Obter Parâmetros da Curva do Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Obtém os parâmetros da curva do processo de soldagem
    * @param  [in] id Número do processo de soldagem (1-99)
    * @param  [out] startCurrent Corrente de partida do arco (A)
    * @param  [out] startVoltage Tensão de partida do arco (V)
    * @param  [out] startTime Tempo de partida do arco (ms)
    * @param  [out] weldCurrent Corrente de soldagem (A)
    * @param  [out] weldVoltage Tensão de soldagem (V)
    * @param  [out] endCurrent Corrente de parada do arco (A)
    * @param  [out] endVoltage Tensão de parada do arco (V)
    * @param  [out] endTime Tempo de parada do arco (ms)
    * @return  Código de erro
    */
    int WeldingGetProcessParam(int id, ref double startCurrent, ref double startVoltage, ref double startTime, ref double weldCurrent, ref double weldVoltage, ref double endCurrent, ref double endVoltage, ref double endTime);

Definir Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Define a relação entre corrente de soldagem e saída analógica
    * @param [in] currentMin Valor da corrente no ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    * @param [in] currentMax Valor da corrente no ponto direito da relação linear corrente de soldagem-saída analógica (A)
    * @param [in] outputVoltageMin Valor da tensão de saída analógica no ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    * @param [in] outputVoltageMax Valor da tensão de saída analógica no ponto direito da relação linear corrente de soldagem-saída analógica (V)
    * @return Código de erro
    */
    int WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

Definir Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Define a relação entre tensão de soldagem e saída analógica
    * @param [in] weldVoltageMin Valor da tensão de soldagem no ponto esquerdo da relação linear tensão de soldagem-saída analógica (A)
    * @param [in] weldVoltageMax Valor da tensão de soldagem no ponto direito da relação linear tensão de soldagem-saída analógica (A)
    * @param [in] outputVoltageMin Valor da tensão de saída analógica no ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    * @param [in] outputVoltageMax Valor da tensão de saída analógica no ponto direito da relação linear tensão de soldagem-saída analógica (V)
    * @return Código de erro
    */
    int WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

Obter Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a relação entre corrente de soldagem e saída analógica
    * @param [out] currentMin Valor da corrente no ponto esquerdo da relação linear corrente de soldagem-saída analógica (A)
    * @param [out] currentMax Valor da corrente no ponto direito da relação linear corrente de soldagem-saída analógica (A)
    * @param [out] outputVoltageMin Valor da tensão de saída analógica no ponto esquerdo da relação linear corrente de soldagem-saída analógica (V)
    * @param [out] outputVoltageMax Valor da tensão de saída analógica no ponto direito da relação linear corrente de soldagem-saída analógica (V)
    * @return Código de erro
    */
    int WeldingGetCurrentRelation(ref double currentMin, ref double currentMax, ref double outputVoltageMin, ref double outputVoltageMax);

Obter Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém a relação entre tensão de soldagem e saída analógica
    * @param [out] weldVoltageMin Valor da tensão de soldagem no ponto esquerdo da relação linear tensão de soldagem-saída analógica (A)
    * @param [out] weldVoltageMax Valor da tensão de soldagem no ponto direito da relação linear tensão de soldagem-saída analógica (A)
    * @param [out] outputVoltageMin Valor da tensão de saída analógica no ponto esquerdo da relação linear tensão de soldagem-saída analógica (V)
    * @param [out] outputVoltageMax Valor da tensão de saída analógica no ponto direito da relação linear tensão de soldagem-saída analógica (V)
    * @return Código de erro
    */
    int WeldingGetVoltageRelation(ref double weldVoltageMin, ref double weldVoltageMax, ref double outputVoltageMin, ref double outputVoltageMax);

Definir Corrente de Soldagem
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Define a corrente de soldagem
    * @param [in] ioType Tipo de controle IO 0-IO do painel de controle；1-IO de extensão
    * @param [in] current Valor da corrente de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica do painel de controle para corrente de soldagem (0-1)
    * @return Código de erro
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex);

Definir Tensão de Soldagem
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Define a tensão de soldagem
    * @param [in] ioType Tipo de controle IO 0-IO do painel de controle；1-IO de extensão
    * @param [in] voltage Valor da tensão de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica do painel de controle para tensão de soldagem (0-1)
    * @return Código de erro
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex);

Definir Parâmetros de Oscilação
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /** 
    * @brief Define os parâmetros de oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação
    * @param [in] weaveType Tipo de oscilação 0-Oscilação triangular plana；1-Oscilação triangular vertical tipo L；2-Oscilação circular horária；3-Oscilação circular anti-horária；4-Oscilação senoidal plana；5-Oscilação senoidal vertical tipo L；6-Oscilação triangular vertical；7-Oscilação senoidal vertical
    * @param [in] weaveFrequency Frequência de oscilação (Hz)
    * @param [in] weaveIncStayTime Modo de espera 0-ciclo não inclui tempo de espera；1-ciclo inclui tempo de espera
    * @param [in] weaveRange Amplitude de oscilação (mm)
    * @param [in] weaveLeftRange Comprimento da corda esquerda da oscilação triangular vertical (mm)
    * @param [in] weaveRightRange Comprimento da corda direita da oscilação triangular vertical (mm)
    * @param [in] additionalStayTime Tempo de espera no ponto do vértice da oscilação triangular vertical (mm)
    * @param [in] weaveLeftStayTime Tempo de espera à esquerda da oscilação (ms)
    * @param [in] weaveRightStayTime Tempo de espera à direita da oscilação (ms)
    * @param [in] weaveCircleRadio Razão de retorno da oscilação circular (0-100%)
    * @param [in] weaveStationary Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera；1-posição parada durante o tempo de espera
    * @param [in] weaveYawAngle Ângulo de azimute da direção da oscilação (rotação em torno do eixo Z da oscilação), unidade °
    * @return Código de erro 
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle=0);

Exemplo de Código para Definir Parâmetros de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
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

        robot.WeldingGetProcessParam(1, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 1 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);
        robot.WeldingGetProcessParam(2, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 2 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);

        int rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
        Console.WriteLine("WeldingSetCurrentRelation rtn is: " + rtn);

        rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
        Console.WriteLine("WeldingSetVoltageRelation rtn is: " + rtn);

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;
        int curIndex = 0;
        int volIndex = 0;
        rtn = robot.WeldingGetCurrentRelation(ref current_min, ref current_max, ref output_vmin, ref output_vmax, ref curIndex);
        Console.WriteLine("WeldingGetCurrentRelation rtn is: " + rtn);
        Console.WriteLine("current min " + current_min + " current max " + current_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingGetVoltageRelation(ref vol_min, ref vol_max, ref output_vmin, ref output_vmax, ref volIndex);
        Console.WriteLine("WeldingGetVoltageRelation rtn is: " + rtn);
        Console.WriteLine("vol min " + vol_min + " vol max " + vol_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingSetCurrent(1, 100, 0, 0);
        Console.WriteLine("WeldingSetCurrent rtn is: " + rtn);

        System.Threading.Thread.Sleep(3000);

        rtn = robot.WeldingSetVoltage(1, 10, 0, 0);
        Console.WriteLine("WeldingSetVoltage rtn is: " + rtn);

        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
        Console.WriteLine("rtn is: " + rtn);

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);

        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        Console.WriteLine("WeldingSetCheckArcInterruptionParam    " + rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        Console.WriteLine("WeldingSetReWeldAfterBreakOffParam    " + rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(ref checkEnable, ref arcInterruptTimeLength);
        Console.WriteLine("WeldingGetCheckArcInterruptionParam  checkEnable  " + checkEnable + "   arcInterruptTimeLength  " + arcInterruptTimeLength);
        rtn = robot.WeldingGetReWeldAfterBreakOffParam(ref enable, ref length, ref velocity, ref moveType);
        Console.WriteLine("WeldingGetReWeldAfterBreakOffParam  enable = " + enable + ", length = " + length + ", velocity = " + velocity + ", moveType = " + moveType);

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(1000);
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(1000);
        }

    }

Definir Parâmetros de Oscilação Online
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Define os parâmetros de oscilação online
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação
    * @param [in] weaveType Tipo de oscilação 0-Oscilação triangular plana；1-Oscilação triangular vertical tipo L；2-Oscilação circular horária；3-Oscilação circular anti-horária；4-Oscilação senoidal plana；5-Oscilação senoidal vertical tipo L；6-Oscilação triangular vertical；7-Oscilação senoidal vertical
    * @param [in] weaveFrequency Frequência de oscilação (Hz)
    * @param [in] weaveIncStayTime Modo de espera 0-ciclo não inclui tempo de espera；1-ciclo inclui tempo de espera
    * @param [in] weaveRange Amplitude de oscilação (mm)
    * @param [in] weaveLeftStayTime Tempo de espera à esquerda da oscilação (ms)
    * @param [in] weaveRightStayTime Tempo de espera à direita da oscilação (ms)
    * @param [in] weaveCircleRadio Razão de retorno da oscilação circular (0-100%)
    * @param [in] weaveStationary Espera na posição de oscilação, 0-posição continua se movendo durante o tempo de espera；1-posição parada durante o tempo de espera
    * @return Código de erro
    */
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

Definir Parâmetros de Detecção de Interrupção Acidental do Arco de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define os parâmetros de detecção de interrupção acidental do arco de soldagem
    * @param [in] checkEnable Se habilita a detecção; 0-desabilitar; 1-habilitar
    * @param [in] arcInterruptTimeLength Duração de confirmação da interrupção do arco (ms)
    * @return Código de erro
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength)

Obter Parâmetros de Detecção de Interrupção Acidental do Arco de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os parâmetros de detecção de interrupção acidental do arco de soldagem
    * @param [out] checkEnable Se habilita a detecção; 0-desabilitar; 1-habilitar
    * @param [out] arcInterruptTimeLength Duração de confirmação da interrupção do arco (ms)
    * @return Código de erro
    */
    int WeldingGetCheckArcInterruptionParam(ref int checkEnable, ref int arcInterruptTimeLength)

Definir Parâmetros de Recuperação de Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define os parâmetros de recuperação de interrupção de soldagem
    * @param[in] enable Se habilita a recuperação de interrupção de soldagem
    * @param[in] length Distância de sobreposição da solda (mm)
    * @param[in] velocity Porcentagem de velocidade do robô ao retornar ao ponto de reinício do arco (0-100)
    * @param[in] moveType Modo de movimento do robô até o ponto de reinício do arco; 0-LIN；1-PTP
    * @return Código de erro
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType)

Obter Parâmetros de Recuperação de Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os parâmetros de recuperação de interrupção de soldagem
    * @param [out] enable Se habilita a recuperação de interrupção de soldagem
    * @param [out] length Distância de sobreposição da solda (mm)
    * @param [out] velocity Porcentagem de velocidade do robô ao retornar ao ponto de reinício do arco (0-100)
    * @param [out] moveType Modo de movimento do robô até o ponto de reinício do arco; 0-LIN；1-PTP
    * @return Código de erro
    */
    int WeldingGetReWeldAfterBreakOffParam(ref int enable, ref double length, ref double velocity, ref int moveType)

Definir Número da Porta DO de Extensão para Modo de Controle da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define o número da porta DO de extensão para o modo de controle da fonte de solda
    * @param DONum Porta DO do modo de controle da fonte de solda (0-127)
    * @return Código de erro
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

Definir Modo de Controle da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define o modo de controle da fonte de solda
    * @param [in] mode Modo de controle da fonte de solda; 0-modo CC com unidade；1-modo pulsado com unidade；2-modo JOB；3-modo painel；4-modo separado；5-modo CC/CV；6-TIG；7-CMT
    * @param [in] ioType Tipo de controle; 0-IO do painel de controle；1-Protocolo de comunicação digital (UDP);2-Protocolo de comunicação digital (ModbusTCP)
    * @return Código de erro
    */
    public int SetWeldMachineCtrlMode(int mode,int ioType = 1)

Início da Soldagem
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Início da soldagem
    * @param [in] ioType tipo de IO 0-IO do controlador； 1-IO de extensão
    * @param [in] arcNum Número do arquivo de configuração da fonte de solda
    * @param [in] timeout Tempo limite de partida do arco
    * @return Código de erro
    */
    int ARCStart(int ioType, int arcNum, int timeout);

Fim da Soldagem
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da soldagem
    * @param [in] ioType tipo de IO 0-IO do controlador； 1-IO de extensão
    * @param [in] arcNum Número do arquivo de configuração da fonte de solda
    * @param [in] timeout Tempo limite de extinção do arco
    * @return Código de erro
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

Início da Oscilação
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Início da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação
    * @return Código de erro
    */
    int WeaveStart(int weaveNum);

Fim da Oscilação
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação
    * @return Código de erro
    */
    int WeaveEnd(int weaveNum);

Alimentação de Arame para Frente
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Alimentação de arame para frente
    * @param [in] ioType tipo de IO  0-IO do controlador；1-IO de extensão
    * @param [in] wireFeed Controle de alimentação de arame  0-parar alimentação；1-alimentar
    * @return Código de erro
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

Alimentação de Arame para Trás
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Alimentação de arame para trás
    * @param [in] ioType tipo de IO  0-IO do controlador；1-IO de extensão
    * @param [in] wireFeed Controle de alimentação de arame  0-parar alimentação；1-alimentar
    * @return Código de erro
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

Fluxo de Gás
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief Fluxo de gás
    * @param [in] ioType tipo de IO  0-IO do controlador；1-IO de extensão
    * @param [in] airControl Controle de fluxo de gás  0-parar fluxo；1-ativar fluxo
    * @return Código de erro
    */
    int SetAspirated(int ioType, int airControl);

Recuperar Soldagem Após Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Recupera a soldagem após interrupção de soldagem
    * @return Código de erro
    */
    int WeldingStartReWeldAfterBreakOff()

Abaortar Soldagem Após Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Aborta a soldagem após interrupção de soldagem
    * @return Código de erro
    */
    int WeldingAbortWeldAfterBreakOff()

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL (p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(1, 0, 10000);
        robot.WeaveEnd(0);
    }

Início da Soldagem por Pontos
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /** 
    * @brief Início da soldagem por pontos
    * @param [in] startDesePos Posição cartesiana do ponto inicial
    * @param [in] endDesePos Pose cartesiana do ponto final
    * @param [in] startJPos Pose articular do ponto inicial
    * @param [in] endJPos Pose articular do ponto final
    * @param [in] weldLength Comprimento do segmento soldado (mm)
    * @param [in] noWeldLength Comprimento do segmento não soldado (mm)
    * @param [in] weldIOType Tipo de IO de soldagem (0-IO do painel de controle；1-IO de extensão)
    * @param [in] arcNum Número do arquivo de configuração da fonte de solda
    * @param [in] weldTimeout Tempo limite de partida/parada do arco
    * @param [in] isWeave Se há oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação
    * @param [in] tool Número da ferramenta
    * @param [in] user Número da peça
    * @param [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm	 
    * @param [in] epos  Posição do eixo de extensão, unidade mm
    * @param [in] search  0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Valor de deslocamento da pose
    * @return Código de erro 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout,bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos);

Exemplo de Código de Soldagem por Pontos do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.SegmentWeldStart( p1Desc,  p2Desc,  p1Joint,  p2Joint, 20, 20, 0, 0, 5000, false, 0, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        Console.WriteLine("SegmentWeldStart rtn is {0}", rtn);
    }

Início da Simulação de Oscilação
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início da simulação de oscilação
    * @param  [in] weaveNum  Número do parâmetro de oscilação
    * @return  Código de erro
    */
    int WeaveStartSim(int weaveNum);

Fim da Simulação de Oscilação
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim da simulação de oscilação
    * @param  [in] weaveNum  Número do parâmetro de oscilação
    * @return  Código de erro
    */
    int WeaveEndSim(int weaveNum);

Início do Alerta de Detecção de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início do alerta de detecção de trajetória (Sem movimento)
    * @param  [in] weaveNum   Número do parâmetro de oscilação
    * @return  Código de erro
    */
    int WeaveInspectStart(int weaveNum);

Fim do Alerta de Detecção de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do alerta de detecção de trajetória (Sem movimento)
    * @param  [in] weaveNum   Número do parâmetro de oscilação
    * @return  Código de erro
    */
    int WeaveInspectEnd(int weaveNum);

Início da Transição Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início da transição gradual da oscilação
    * @param [in] weaveChangeFlag 1-alterar parâmetros de oscilação；2-alterar parâmetros de oscilação + velocidade de soldagem
    * @param [in] weaveNum Número da oscilação 
    * @param [in] velStart Velocidade inicial de soldagem (cm/min)
    * @param [in] velEnd Velocidade final de soldagem (cm/min)
    * @return  Código de erro
    */
    int WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

Fim da Transição Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim da transição gradual da oscilação
    * @return  Código de erro
    */
    int WeaveChangeEnd()

Exemplo de Código de Soldagem com Transição Gradual de Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveStartSim(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveEndSim(0);
        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveInspectStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveInspectEnd(0);

        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveL( p1Joint,  p1Desc, 1, 1, 100, 100, 50, -1,  exaxisPos, 0, 0,  offdese);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1, 0, 50, 30);
        robot.MoveL( p2Joint,  p2Desc, 1, 1, 100, 100, 1, -1,  exaxisPos, 0, 0,  offdese);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
    }

IO de Extensão - Configurar Sinal de Detecção de Gás da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de detecção de gás da fonte de solda
    * @param  [in] DONum  Número DO de extensão do sinal de detecção de gás
    * @return  Código de erro
    */
    int SetAirControlExtDoNum(int DONum);

IO de Extensão - Configurar Sinal de Partida de Arco da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de partida de arco da fonte de solda
    * @param  [in] DONum  Número DO de extensão do sinal de partida de arco da fonte de solda
    * @return  Código de erro
    */
    int SetArcStartExtDoNum(int DONum);

IO de Extensão - Configurar Sinal de Alimentação de Arame para Trás da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de alimentação de arame para trás da fonte de solda
    * @param  [in] DONum  Número DO de extensão do sinal de alimentação de arame para trás
    * @return  Código de erro
    */
    int SetWireReverseFeedExtDoNum(int DONum);

IO de Extensão - Configurar Sinal de Alimentação de Arame para Frente da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de alimentação de arame para frente da fonte de solda
    * @param  [in] DONum  Número DO de extensão do sinal de alimentação de arame para frente
    * @return  Código de erro
    */
    int SetWireForwardFeedExtDoNum(int DONum);

IO de Extensão - Configurar Sinal de Sucesso de Partida de Arco da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de sucesso de partida de arco da fonte de solda
    * @param  [in] DINum  Número DI de extensão do sinal de sucesso de partida de arco
    * @return  Código de erro
    */
    int SetArcDoneExtDiNum(int DINum);

IO de Extensão - Configurar Sinal de Prontidão da Fonte de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de prontidão da fonte de solda
    * @param  [in] DINum  Número DI de extensão do sinal de prontidão da fonte de solda
    * @return  Código de erro
    */
    int SetWeldReadyExtDiNum(int DINum);

IO de Extensão - Configurar Sinal de Recuperação de Interrupção de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief IO de extensão - Configurar sinal de recuperação de interrupção de soldagem
    * @param  [in] reWeldDINum  Número DI de extensão do sinal de recuperação de soldagem após interrupção
    * @param  [in] abortWeldDINum  Número DI de extensão do sinal de abortagem de soldagem após interrupção
    * @return  Código de erro
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

Exemplo de Código para Configurar Sinais de Soldagem com IO de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button51_Click(object sender, EventArgs e)
    {
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);

        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);
    }

Controle de Rastreamento de Arco
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Controle de rastreamento de arco
    * @param  [in] flag Interruptor, 0-desligar；1-ligar
    * @param  [in] dalayTime Tempo de atraso, unidade ms
    * @param  [in] isLeftRight Compensação de desvio horizontal
    * @param  [in] klr Coeficiente de ajuste horizontal (sensibilidade)
    * @param  [in] tStartLr Tempo de início da compensação horizontal cyc
    * @param  [in] stepMaxLr Quantidade máxima de compensação por ciclo horizontal mm
    * @param  [in] sumMaxLr Quantidade máxima total de compensação horizontal mm
    * @param  [in] isUpLow Compensação de desvio vertical
    * @param  [in] kud Coeficiente de ajuste vertical (sensibilidade)
    * @param  [in] tStartUd Tempo de início da compensação vertical cyc
    * @param  [in] stepMaxUd Quantidade máxima de compensação por ciclo vertical mm
    * @param  [in] sumMaxUd Quantidade máxima total de compensação vertical
    * @param  [in] axisSelect Seleção do sistema de coordenadas vertical, 0-oscilação；1-ferramenta；2-base
    * @param  [in] referenceType Método de definição da corrente de referência vertical, 0-feedback；1-constante
    * @param  [in] referSampleStartUd Início da contagem de amostragem da corrente de referência vertical (feedback), cyc
    * @param  [in] referSampleCountUd Contagem do ciclo de amostragem da corrente de referência vertical (feedback), cyc
    * @param  [in] referenceCurrent Corrente de referência vertical mA
    *  @param  [in] offsetType Tipo de rastreamento com deslocamento, 0-sem deslocamento；1-amostragem；2-porcentagem  /version 3.7.9
    * @param  [in] offsetParameter Parâmetro de deslocamento; amostragem (tempo de início da amostragem de deslocamento, padrão um ciclo); porcentagem (porcentagem de deslocamento (-100 ~ 100)) /version 3.7.9
    * @return  Código de erro
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

Seleção da Faixa AI para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Seleção da faixa AI para rastreamento de arco
    * @param  [in] channel Seleção da faixa AI para rastreamento de arco, [0-3]
    * @return  Código de erro
    */
    int ArcWeldTraceExtAIChannelConfig(int channel);

Ativação da Compensação para Rastreamento de Arco + Múltiplas Camadas e Múltiplas Passadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação da compensação para rastreamento de arco + múltiplas camadas e múltiplas passadas
    * @return Código de erro
    */
    int ArcWeldTraceReplayStart();

Desativação da Compensação para Rastreamento de Arco + Múltiplas Camadas e Múltiplas Passadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

        /**
         * @brief Desativação da compensação para rastreamento de arco + múltiplas camadas e múltiplas passadas
         * @return Código de erro
         */
    int ArcWeldTraceReplayEnd();

Mudança de Coordenadas de Deslocamento - Soldagem de Múltiplas Camadas e Múltiplas Passadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
     * @brief Mudança de coordenadas de deslocamento - Soldagem de múltiplas camadas e múltiplas passadas
     * @param [in] pointO Pose cartesiana do ponto base
     * @param [in] pointX Pose cartesiana do ponto na direção de deslocamento X do ponto base
     * @param [in] pointZ Pose cartesiana do ponto na direção de deslocamento Z do ponto base
     * @param [in] dx Deslocamento na direção x (mm)
     * @param [in] dy Deslocamento na direção z (mm)
     * @param [in] db Deslocamento em torno do eixo y (°)
     * @param [out] offset Deslocamento calculado
     * @return Código de erro
     */
    int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, ref DescPose offset);

Exemplo de Código de Rastreamento de Arco para Soldagem de Múltiplas Camadas e Múltiplas Passadas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    private void button52_Click(object sender, EventArgs e)
    {
        JointPos mulitilineorigin1_joint = new JointPos(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
        DescPose mulitilineorigin1_desc = new DescPose(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);

        DescTran mulitilineX1_desc = new DescTran();
        mulitilineX1_desc.x = -677.556;
        mulitilineX1_desc.y = 211.949;
        mulitilineX1_desc.z = -1.206;

        DescTran mulitilineZ1_desc = new DescTran();
        mulitilineZ1_desc.x = -677.564;
        mulitilineZ1_desc.y = 190.956;
        mulitilineZ1_desc.z = 19.817;

        JointPos mulitilinesafe_joint = new JointPos(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
        DescPose mulitilinesafe_desc = new DescPose(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
        JointPos mulitilineorigin2_joint = new JointPos(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
        DescPose mulitilineorigin2_desc = new DescPose(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);

        DescTran mulitilineX2_desc = new DescTran();
        mulitilineX2_desc.x = -563.965;
        mulitilineX2_desc.y = 220.355;
        mulitilineX2_desc.z = -0.680;

        DescTran mulitilineZ2_desc = new DescTran();
        mulitilineZ2_desc.x = -563.968;
        mulitilineZ2_desc.y = 215.362;
        mulitilineZ2_desc.z = 4.331;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset = new DescPose(0, 0, 0, 0, 0, 0);

        Thread.Sleep(10);
        int error = robot.MoveJ( mulitilinesafe_joint,  mulitilinesafe_desc, 13, 0, 10, 100, 100,  epos, -1, 0,  offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.WeaveStart(0);
        Console.WriteLine("WeaveStart return: {0}", error);

        error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.WeaveEnd(0);
        Console.WriteLine("WeaveEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("ArcWeldTraceReplayStart return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 1, 2, 100, 100, -1, epos, 1, 1, offset, 1, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 3000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);
    }

Seleção do Canal AI para Feedback de Corrente da Fonte de Solda no Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief Seleção do canal AI para feedback de corrente da fonte de solda no rastreamento de arco
    * @param [in]  channel Canal; 0-AI de extensão 0；1-AI de extensão 1；2-AI de extensão 2；3-AI de extensão 3；4-AI do painel de controle 0；5-AI do painel de controle 1
    * @return Código de erro
    */
    int ArcWeldTraceAIChannelCurrent(int channel);

Seleção do Canal AI para Feedback de Tensão da Fonte de Solda no Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Seleção do canal AI para feedback de tensão da fonte de solda no rastreamento de arco
    * @param [in]  channel Canal; 0-AI de extensão 0；1-AI de extensão 1；2-AI de extensão 2；3-AI de extensão 3；4-AI do painel de controle 0；5-AI do painel de controle 1
    * @return Código de erro
    */
    int ArcWeldTraceAIChannelVoltage(int channel);

Parâmetros de Conversão do Feedback de Corrente da Fonte de Solda no Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Parâmetros de conversão do feedback de corrente da fonte de solda no rastreamento de arco
    * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, faixa [0-10V]
    * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, faixa [0-10V]
    * @param [in] currentLow Valor da corrente da fonte de solda correspondente ao limite inferior do canal AI, valor padrão 0V, faixa [0-200V]
    * @param [in] currentHigh Valor da corrente da fonte de solda correspondente ao limite superior do canal AI, valor padrão 100V, faixa [0-200V]
    * @return Código de erro
    */
    int ArcWeldTraceCurrentPara(float AILow, float AIHigh, float currentLow, float currentHigh);

Parâmetros de Conversão do Feedback de Tensão da Fonte de Solda no Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Parâmetros de conversão do feedback de tensão da fonte de solda no rastreamento de arco
    * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, faixa [0-10V]
    * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, faixa [0-10V]
    * @param [in] voltageLow Valor da tensão da fonte de solda correspondente ao limite inferior do canal AI, valor padrão 0V, faixa [0-200V]
    * @param [in] voltageHigh Valor da tensão da fonte de solda correspondente ao limite superior do canal AI, valor padrão 100V, faixa [0-200V]
    * @return Código de erro
    */
    int ArcWeldTraceVoltagePara(float AILow, float AIHigh, float voltageLow, float voltageHigh);

Exemplo de Código de Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose safetydescPose = new DescPose(-504.043, 275.181, 40.908, -28.002, -42.025, -14.044);
        JointPos safetyjointPos = new JointPos(-39.078, -76.732, 87.227, -99.47, -94.301, 18.714);
        DescPose startdescPose = new DescPose(-473.86, 257.879, -20.849, -37.317, -42.021, 2.543);
        JointPos startjointPos = new JointPos(-43.487, -76.526, 95.568, -104.445, -89.356, 3.72);



        DescPose enddescPose = new DescPose(-499.844, 141.225, 7.72, -34.856, -40.17, 13.13);
        JointPos endjointPos = new JointPos(-31.305, -82.998, 99.401, -104.426, -89.35, 3.696);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);
        robot.WeldingSetVoltage(0, 25, 1, 0);// ----definir tensão
        robot.WeldingSetCurrent(0, 260, 0, 0);// ----definir corrente

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        Console.WriteLine("ArcWeldTraceAIChannelCurrent rtn is " + rtn);
        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        Console.WriteLine("ArcWeldTraceAIChannelVoltage rtn is " + rtn);
        rtn = robot.ArcWeldTraceCurrentPara((float)0, (float)5, (float)0, (float)500);
        Console.WriteLine("ArcWeldTraceCurrentPara rtn is " + rtn);
        rtn = robot.ArcWeldTraceVoltagePara((float)1.018, (float)10, (float)0, (float)50);
        Console.WriteLine("ArcWeldTraceVoltagePara rtn is " + rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        // robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
    }

Definir Portas IO de Extensão para Busca de Posição do Arame
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Define as portas IO de extensão para busca de posição do arame
    * @param searchDoneDINum Porta DO de sucesso da busca de posição do arame (0-127)
    * @param searchStartDONum Porta DO de controle de início/parada da busca de posição do arame (0-127)
    * @return Código de erro
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

Início da Busca de Posição do Arame
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início da busca de posição do arame
    * @param  [in] refPos  1-ponto de referência 0-ponto de contato
    * @param  [in] searchVel   Velocidade de busca %
    * @param  [in] searchDis  Distância de busca mm
    * @param  [in] autoBackFlag Flag de retorno automático, 0-não automático；1-automático
    * @param  [in] autoBackVel  Velocidade de retorno automático %
    * @param  [in] autoBackDis  Distância de retorno automático mm
    * @param  [in] offectFlag  1-busca com deslocamento；0-busca com ponto de ensino
    * @return  Código de erro
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

Fim da Busca de Posição do Arame
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim da busca de posição do arame
    * @param  [in] refPos  1-ponto de referência 2-ponto de contato
    * @param  [in] searchVel   Velocidade de busca %
    * @param  [in] searchDis  Distância de busca mm
    * @param  [in] autoBackFlag Flag de retorno automático, 0-não automático；1-automático
    * @param  [in] autoBackVel  Velocidade de retorno automático %
    * @param  [in] autoBackDis  Distância de retorno automático mm
    * @param  [in] offectFlag  1-busca com deslocamento；2-busca com ponto de ensino
    * @return  Código de erro
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

Calcular Deslocamento da Busca de Posição do Arame
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Calcular deslocamento da busca de posição do arame
    * @param  [in] seamType  Tipo de solda
    * @param  [in] method   Método de cálculo
    * @param  [in] varNameRef Ponto de referência 1-6, "#" indica nenhum ponto variável
    * @param  [in] varNameRes Ponto de contato 1-6, "#" indica nenhum ponto variável
    * @param  [out] offectFlag 0-deslocamento aplicado diretamente ao ponto de instrução；1-deslocamento requer transformação de coordenadas no ponto de instrução
    * @param  [out] offect Deslocamento da pose [x, y, z, a, b, c]
    * @return  Código de erro
    */
    int GetWireSearchOffset(int seamType, int method, string[] varNameRef, string[] varNameRes, ref int offsetFlag, ref DescPose offset);

Aguardar Conclusão da Busca de Posição do Arame
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Aguardar conclusão da busca de posição do arame
    * @return  Código de erro
    */
    int WireSearchWait(string name);

Escrever Ponto de Contato da Busca de Posição do Arame no Banco de Dados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Escrever ponto de contato da busca de posição do arame no banco de dados
    * @param  [in] varName  Nome do ponto de contato “RES0” ~ “RES99”
    * @param  [in] pos  Dados do ponto de contato [x, y, x, a, b, c]
    * @return  Código de erro
    */
    int SetPointToDatabase(string varName, DescPose pos);

Exemplo de Código de Busca de Posição do Arame do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button53_Click(object sender, EventArgs e)
    {
        DescPose toolCoord=new DescPose(0, 0, 200, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);
        DescPose wobjCoord=new DescPose(0, 0, 0, 0, 0, 0);
        robot.SetWObjCoord(1, wobjCoord, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(216.543, 445.175, 93.465, 179.683, 1.757, -112.641);
        JointPos jointStart = new JointPos(-128.345, -86.660, 114.679, -119.625, -89.219, 74.303);

        DescPose descEnd = new DescPose(111.143, 523.384, 87.659, 179.703, 1.835, -97.750);
        JointPos jointEnd = new JointPos(-113.454, -81.060, 109.328, -119.954, -89.218, 74.302);

        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

        DescPose descREF0A = new DescPose(142.135, 367.604, 86.523, 179.728, 1.922, -111.089);
        JointPos jointREF0A = new JointPos(-126.794, -100.834, 128.922, -119.864, -89.218, 74.302);

        DescPose descREF0B = new DescPose(254.633, 463.125, 72.604, 179.845, 2.341, -114.704);
        JointPos jointREF0B = new JointPos(-130.413, -81.093, 112.044, -123.163, -89.217, 74.303);

        DescPose descREF1A = new DescPose(92.556, 485.259, 47.476, -179.932, 3.130, -97.512);
        JointPos jointREF1A = new JointPos(-113.231, -83.815, 119.877, -129.092, -89.217, 74.303);

        DescPose descREF1B = new DescPose(203.103, 583.836, 63.909, 179.991, 2.854, -103.372);
        JointPos jointREF1B = new JointPos(-119.088, -69.676, 98.692, -121.761, -89.219, 74.303);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //ponto de direção
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //ponto de direção
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //ponto de direção
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //ponto de direção
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        string[] varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
        string[] varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
        int offectFlag = 0;
        DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, ref offectFlag, ref offectPos);
        robot.PointsOffsetEnable(0, offectPos);
        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);
        robot.PointsOffsetDisable();
    }

Início da Transição Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Início da transição gradual da tensão de soldagem
    * @param [in] IOType Tipo de controle; 0-IO do painel de controle；1-Protocolo de comunicação digital (UDP);2-Protocolo de comunicação digital (ModbusTCP)
    * @param [in] voltageStart Tensão inicial de soldagem (V)
    * @param [in] voltageEnd Tensão final de soldagem (V)
    * @param [in] AOIndex Número da porta AO do painel de controle (0-1)
    * @param [in] blend Se é suave 0-não suave；1-suave
    * @return Código de erro
    */
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

Fim da Transição Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da transição gradual da tensão de soldagem
    * @return Código de erro
    */
    int WeldingSetVoltageGradualChangeEnd();

Início da Transição Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Início da transição gradual da corrente de soldagem
    * @param [in] IOType Tipo de controle; 0-IO do painel de controle；1-Protocolo de comunicação digital (UDP);2-Protocolo de comunicação digital (ModbusTCP)
    * @param [in] voltageStart Corrente inicial de soldagem (A)
    * @param [in] voltageEnd Corrente final de soldagem (A)
    * @param [in] AOIndex Número da porta AO do painel de controle (0-1)
    * @param [in] blend Se é suave 0-não suave；1-suave
    * @return Código de erro
    */
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

Fim da Transição Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da transição gradual da corrente de soldagem
    * @return Código de erro
    */
    int WeldingSetCurrentGradualChangeEnd();

Exemplo de Código de Transição Gradual da Corrente e Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(-319.303, -240.689, 116.379, -175.879, -0.337, 148.239);
        JointPos startjointPos = new JointPos(20.474, -103.554, 126.774, -116.682, -87.746, -37.709);

        DescPose enddescPose = new DescPose(-454.166, -327.159, 62.217, 177.199, -2.276, 154.955);
        JointPos endjointPos = new JointPos(27.176, -74.423, 104.557, -119.315, -93.514, -37.698);

        DescPose safedescPose = new DescPose(-375.533, -543.319, 19.798, 177.486, -2.489, 175.825);
        JointPos safejointPos = new JointPos(48.074, -59.714, 89.955, -119.777, -93.508, -37.683);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);

        robot.WeldingSetVoltage(0, 25, 1, 0);//
        robot.WeldingSetCurrent(0, 260, 0, 0);// 

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        int rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        Console.WriteLine($"WeldingSetCurrentGradualChangeStart rtn is {rtn}");
        rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        Console.WriteLine($"WeldingSetVoltageGradualChangeStart rtn is {rtn}");

        rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        Console.WriteLine($"ArcWeldTraceControl rtn is {rtn}");

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        rtn = robot.WeaveChangeStart(2, 1, 24, 36);
        Console.WriteLine($"WeaveChangeStart rtn is {rtn}");
        //robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }

Definir Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Definir parâmetros de oscilação personalizada
     * @param [in] id Número da oscilação personalizada: 0-2
     * @param [in] pointNum Número de pontos de oscilação 0-10
     * @param [in] point Dados do ponto final de movimento x, y, z
     * @param [in] stayTime Tempo de pausa da oscilação ms
     * @param [in] frequency Frequência de oscilação Hz
     * @param [in] incStayType Modo de espera: 0-ciclo não inclui tempo de espera；1-ciclo inclui tempo de espera
     * @param [in] stationary Espera na posição de oscilação: 0-continua movimento durante o tempo de espera；1-posição parada durante o tempo de espera
     * @return  Código de erro
     */
    public int CustomWeaveSetPara(int id, int pointNum, DescTran[] points, double[] stayTimes, double frequency, int incStayType, int stationary)

Obter Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief Obter parâmetros de oscilação personalizada
     * @param [in] id Número da oscilação personalizada: 0-2
     * @param [out] pointNum Número de pontos de oscilação 0-10
     * @param [out] point Dados do ponto final de movimento x, y, z
     * @param [out] stayTime Tempo de pausa da oscilação ms
     * @param [out] frequency Frequência de oscilação Hz
     * @param [out] incStayType Modo de espera: 0-ciclo não inclui tempo de espera；1-ciclo inclui tempo de espera
     * @param [out] stationary Espera na posição de oscilação: 0-continua movimento durante o tempo de espera；1-posição parada durante o tempo de espera
     * @return  Código de erro
     */
    public int CustomWeaveGetPara(int id, ref int pointNum, ref DescTran[] points, ref double[] stayTimes, ref double frequency, ref int incStayType, ref int stationary)

Exemplo de Código de Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestCoordMain5()
    {  
        DescTran[] points = new DescTran[10];
        for (int i = 0; i < 10; i++)
        {
            points[i] = new DescTran();
        }
        points[0].x = -3;
        points[0].y = -3;
        points[0].z = 0;
        points[1].x = -6;
        points[1].y = 0;
        points[1].z = 0;
        points[2].x = -3;
        points[2].y = 3;
        points[2].z = 0;
        points[3].x = 0;
        points[3].y = 0;
        points[3].z = 0;
        double[] stayTimes = new double[10] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        int rtn = robot.CustomWeaveSetPara(2, 4, points, stayTimes, 1.000, 0, 0);
        Console.WriteLine($"CustomWeaveSetPara rtn is {rtn}");
        System.Threading.Thread.Sleep(1000);
        int pointNum = 0;
        double frequency = 0;
        int incStayType = 0;
        int stationary = 0;
        rtn = robot.CustomWeaveGetPara(2, ref pointNum, ref points, ref stayTimes, ref frequency, ref incStayType, ref stationary);
        Console.WriteLine($"pointNum is {pointNum}");
        for (int i = 0; i < pointNum; i++)
        {
            Console.WriteLine($"point {i}, point x y z {points[i].x:F6} {points[i].y:F6} {points[i].z:F6}");
        }
        Console.WriteLine($"fre is {frequency:F6}, stay is {incStayType} {stationary}");
        robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
        DescPose desc_p1 = new DescPose(-288.650, 367.807, 288.404, 0.000, -0.001, 0.001);
        DescPose desc_p2 = new DescPose(-431.714, 367.815, 288.415, 0.001, 0.001, 0.000);    
        DescPose desc_p3 = new DescPose(-348.666, 427.798, 288.404, -0.000, -0.000, 0.001);
        JointPos j1 = new JointPos(140.656,  -84.560,  -91.707, -93.734,  90.000,50.655 );
        JointPos j2 = new JointPos ( 149.873, -98.298, -77.599,  -94.103,  90.000,  59.873 );
        JointPos j3 = new JointPos (139.773,  -96.173, -80.014,  -93.814,  90.000,  49.772 );
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos = new DescPose(0,0,0,0,0,0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.Circle(j3, desc_p3, 3, 0, 100, 100, epos, j2, desc_p2, 3, 0, 100, 100, epos, 10, -1, offset_pos, 100, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveC(j3, desc_p3, 3, 0, 100, 100, epos, 0, offset_pos, j2, desc_p2, 3, 0, 100, 100, epos, 0, offset_pos, 10, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2, 3, 0, 100, 100, 10, -1, epos, 0, 0, offset_pos, 0, 0, 10);
        robot.WeaveEnd(0);
    }

Configuração de Parâmetros da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Escreve os parâmetros de configuração para um dos 10 grupos de processo da máquina de solda a laser e configura a máquina de solda
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] num Número do grupo a ser definido (1~10)
    * @param[in] scanSpeed Velocidade de varredura
    * @param[in] scanWidth Largura de varredura
    * @param[in] peakPower Potência de pico
    * @param[in] dutyCycle Ciclo de trabalho
    * @param[in] freq Frequência
    * @return Código de erro
    */
    public int SetLaserWeldingParam(int io_type, int num, int scanSpeed, int scanWidth, int peakPower, int dutyCycle, int freq)

Definir Início/Parada da Soldagem a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Liga/desliga a máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status Palavra de controle 0-laser desligado 1-laser ligado
    * @param[in] max_waittime Tempo máximo de espera
    * @return Código de erro
    */
    public int SetLaserWeldingStartEnd(int io_type, int status, int max_waittime)

Habilitar/Desabilitar Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Habilita/desabilita a máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status 0-desabilitar 1-habilitar
    * @return Código de erro
    */
    public int SetLaserWeldingEnable(int io_type, int status)

Redefinição de Falha da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Redefine a falha da máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[in] status Palavra de controle 0-inválido 1-redefinição de falha
    * @return Código de erro
    */
    public int ResetLaserWeldingErr(int io_type, int status)

Obter Estado de Funcionamento da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado de funcionamento da máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] status Palavra de controle 0-parado 1-em funcionamento
    * @return Código de erro
    */
    public int GetLaserWeldingRunningState(int io_type, ref int status)

Obter Estado de Falha da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém o estado de falha da máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] status 0-sem falha 1-falha presente
    * @return Código de erro
    */
    public int GetLaserWeldingErrState(int io_type, ref int status)

Obter Parâmetros Configurados da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os parâmetros de configuração para um dos 10 grupos de processo da máquina de solda a laser
    * @param[in] num Número do grupo a ser definido (1~10)
    * @param[out] scanSpeed Velocidade de varredura
    * @param[out] scanWidth Largura de varredura
    * @param[out] peakPower Potência de pico
    * @param[out] dutyCycle Ciclo de trabalho
    * @param[out] freq Frequência
    * @return Código de erro
    */
    public int GetLaserWeldingParamTarget(int num, ref int scanSpeed, ref int scanWidth, ref int peakPower, ref int dutyCycle, ref int freq)

Obter Parâmetros de Configuração Atualmente Ativos da Máquina de Solda a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Obtém os parâmetros de configuração atualmente ativos da máquina de solda a laser
    * @param[in] io_type Tipo de comunicação 0-IO 1-UDP
    * @param[out] scanSpeed Velocidade de varredura
    * @param[out] scanWidth Largura de varredura
    * @param[out] peakPower Potência de pico
    * @param[out] dutyCycle Ciclo de trabalho
    * @param[out] freq Frequência
    * @return Código de erro
    */
    public int GetLaserWeldingParamActual(int io_type, ref int scanSpeed, ref int scanWidth, ref int peakPower, ref int dutyCycle, ref int freq)
    
Configurar a Porta DO de Habilitação de IO Estendido da Máquina de Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Define o IO estendido da máquina de solda a laser, porta DO de habilitação
    * @param[in] ctrlModeDONum Número da porta DO estendida para habilitação da máquina de solda a laser
    * @return Código de erro
    */
    public int SetLaserWeldingEnableExtDoNum(int ctrlModeDONum)

Configurar a Porta DO de Início de IO Estendido da Máquina de Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Define o IO estendido da máquina de solda a laser, porta DO de início
    * @param[in] ctrlModeDONum Número da porta DO estendida para início (laser ligado/desligado) da máquina de solda a laser
    * @return Código de erro
    */
    public int SetLaserWeldingStartExtDoNum(int ctrlModeDONum)

Configurar a Porta DO de Redefinição de Falha de IO Estendido da Máquina de Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Define o IO estendido da máquina de solda a laser, porta DO de redefinição de falha
    * @param[in] ctrlModeDONum Número da porta DO estendida para redefinição de falha da máquina de solda a laser
    * @return Código de erro
    */
    public int SetLaserWeldingErrResetExtDoNum(int ctrlModeDONum)

Configurar o DI Estendido para Estado de Funcionamento (Estado Laser Ligado) da Máquina de Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Configura o DI estendido para o estado de funcionamento (estado laser ligado) da máquina de solda a laser
    * @param[in] diNum Porta DI estendida para o estado de funcionamento (estado laser ligado) da máquina de solda a laser
    * @return Código de erro
    */
    public int SetLaserWeldingRunningStateExtDiNum(int diNum)
    
Configurar a Porta DI de Estado de Falha de IO Estendido da Máquina de Solda a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief Configura o DI estendido para o estado de falha da máquina de solda a laser
    * @param[in] diNum Porta DI estendida para o estado de falha da máquina de solda a laser
    * @return Código de erro
    */
    public int SetLaserWeldingErrStateExtDiNum(int diNum)
        
Exemplo de Código de Soldagem a Laser
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    private void btnLaserWeld_Click(object sender, EventArgs e)
    {

        int rtn = -1;
        // Carregar driver UDP
        rtn = robot.ExtDevLoadUDPDriver();
        if (rtn != 0)
        {
            Console.WriteLine("Failed to load UDP driver, error code: " + rtn);
        }
        Thread.Sleep(1000);

        // Definir parâmetros de soldagem a laser: io_type=1, num=3, scanSpeed=2000, scanWidth=3, peakPower=1500, dutyCycle=100, freq=1000
        rtn = robot.SetLaserWeldingParam(1, 3, 2000, 3, 1500, 100, 1000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingParam failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("SetLaserWeldingParam success");
        }

        // Definir o número da porta DO de início
        rtn = robot.SetLaserWeldingStartExtDoNum(1);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartExtDoNum failed, error code: " + rtn);
        }

        // Definir modo 0 (modo de ensino)
        rtn = robot.Mode(0);
        if (rtn != 0)
        {
            Console.WriteLine("Set mode 0 failed, error code: " + rtn);
        }
        Thread.Sleep(1000);


        DescPose desc_pos1 = new DescPose(-303.721, -206.960, 297.105, 152.209, 19.857, 109.166);
        DescPose desc_pos2 = new DescPose(-301.575, -254.888, 284.786, 155.919, 26.946, 111.629);
        DescPose desc_safe = new DescPose(-344.386, -280.830, 435.073, 173.835, 15.333, 124.931);


        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offset = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        // Mover para o primeiro ponto de soldagem
        int error = robot.MoveL(desc_pos1, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to pos1 return: " + error);

        // Iniciar laser (laser ligado)
        rtn = robot.SetLaserWeldingStartEnd(1, 1, 10000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartEnd (start) failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("Laser started");
        }

        // Mover para o segundo ponto de soldagem (durante a soldagem)
        rtn = robot.MoveL(desc_pos2, 0, 0, 30, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to pos2 return: " + rtn);

        Thread.Sleep(500);
        // Parar laser (laser desligado)
        rtn = robot.SetLaserWeldingStartEnd(1, 0, 10000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartEnd (stop) failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("Laser stopped");
        }

        // Mover para ponto de segurança
        rtn = robot.MoveL(desc_safe, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to safe_pos return: " + rtn);

        // Definir modo 1 (modo remoto)
        rtn = robot.Mode(1);
        if (rtn != 0)
        {
            Console.WriteLine("Set mode 1 failed, error code: " + rtn);
        }
        Thread.Sleep(1000);

        // Fechar conexão
        robot.CloseRPC();
        Thread.Sleep(1000);

        Console.WriteLine("Test completed");

        return ;
    }