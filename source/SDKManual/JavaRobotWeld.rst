Soldagem do Robô
===================

.. toctree::
    :maxdepth: 5


Definir Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros da curva de processo de soldagem
    * @param [in] id Número do processo de soldagem (1-99)
    * @param [in] param Parâmetros do processo de soldagem
    * @return Código de erro
    */
    int WeldingSetProcessParam(int id, WeldingProcessParam param);

Obter Parâmetros da Curva de Processo de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros da curva de processo de soldagem
    * @param [in] id Número do processo de soldagem (1-99)
    * @param [out] param Parâmetros do processo de soldagem
    * @return Código de erro
    */
    int WeldingGetProcessParam(int id, WeldingProcessParam param);

Definir Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a relação entre corrente de soldagem e saída analógica
    * @param [in] relation Valores da relação
    * @return Código de erro
    */
    int WeldingSetCurrentRelation(WeldCurrentAORelation relation);

Definir Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a relação entre tensão de soldagem e saída analógica
    * @param [in] relation Valores da relação tensão de soldagem-saída analógica
    * @return Código de erro
    */
    int WeldingSetVoltageRelation(WeldVoltageAORelation relation);

Obter Relação entre Corrente de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a relação entre corrente de soldagem e saída analógica
    * @param [out] relation Valores da relação
    * @return Código de erro
    */
    int WeldingGetCurrentRelation(WeldCurrentAORelation relation);

Obter Relação entre Tensão de Soldagem e Saída Analógica
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém a relação entre tensão de soldagem e saída analógica
    * @param [out] relation Valores da relação tensão de soldagem-saída analógica
    * @return Código de erro
    */
    int WeldingGetVoltageRelation(WeldVoltageAORelation relation);

Definir Corrente de Soldagem
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a corrente de soldagem
    * @param [in] ioType Tipo de E/S de controle 0-E/S da caixa de controle; 1-E/S estendida
    * @param [in] current Valor da corrente de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica da caixa de controle para corrente de soldagem (0-1)
    * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
    * @return Código de erro
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

Definir Tensão de Soldagem
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a tensão de soldagem
    * @param [in] ioType Tipo de E/S de controle 0-E/S da caixa de controle; 1-E/S estendida
    * @param [in] voltage Valor da tensão de soldagem (A)
    * @param [in] AOIndex Porta de saída analógica da caixa de controle para tensão de soldagem (0-1)
    * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
    * @return Código de erro
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

Definir Parâmetros de Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
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
    * @param [in] weaveRotAngle Ângulo de direção da oscilação (rotação em torno do eixo X da oscilação), em graus
    * @return Código de erro
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle)

Exemplo de Código para Definir Parâmetros de Soldagem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSetWeldParam(Robot robot)
    {
        WeldingProcessParam para1 = new WeldingProcessParam(177, 27, 1000, 178, 28, 176, 26, 1000);
        WeldingProcessParam para2 = new WeldingProcessParam(188, 28, 555, 199, 29, 133, 23, 333);

        robot.WeldingSetProcessParam(1, para1);
        robot.WeldingSetProcessParam(2, para2);

        double startCurrent = 0;
        double startVoltage = 0;
        int startTime = 0;
        double weldCurrent = 0;
        double weldVoltage = 0;
        double endCurrent = 0;
        double endVoltage = 0;
        int endTime = 0;

        WeldingProcessParam param = new WeldingProcessParam(startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
        robot.WeldingGetProcessParam(1, param);
        robot.WeldingGetProcessParam(2, param);

        WeldCurrentAORelation rela1 = new WeldCurrentAORelation(0, 400, 0, 10, 0);
        int rtn = robot.WeldingSetCurrentRelation(rela1);

        WeldVoltageAORelation rela2 = new WeldVoltageAORelation(0, 40, 0, 10, 1);
        rtn = robot.WeldingSetVoltageRelation(rela2);

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;
        int curIndex = 0;
        int volIndex = 0;
        WeldCurrentAORelation rela3 = new WeldCurrentAORelation(current_min, current_max, output_vmin, output_vmax, curIndex);
        rtn = robot.WeldingGetCurrentRelation(rela3);

        WeldVoltageAORelation rela4 = new WeldVoltageAORelation(0, 0, 0, 0, 0);
        rtn = robot.WeldingGetVoltageRelation(rela4);

        rtn = robot.WeldingSetCurrent(0, 100, 0, 0);

        robot.Sleep(3000);

        rtn = robot.WeldingSetVoltage(0, 10, 0, 0);

        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000, 0);

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);

        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        List<Integer> inter = new ArrayList<>();
        List<Number> num = new ArrayList<>();

        inter = robot.WeldingGetCheckArcInterruptionParam();
        num = robot.WeldingGetReWeldAfterBreakOffParam();

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            robot.Sleep(1000);
            robot.SetWeldMachineCtrlMode(1);
            robot.Sleep(1000);
        }
        return 0;
    }

Definir Parâmetros de Oscilação em Tempo Real
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

Definir Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô
    * @param [in] checkEnable Se habilita a detecção; 0-não habilita; 1-habilita
    * @param [in] arcInterruptTimeLength Duração de confirmação da interrupção do arco (ms)
    * @return Código de erro
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

Obter Parâmetros de Detecção de Interrupção Inesperada do Arco de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros de detecção de interrupção inesperada do arco de soldagem do robô
    * @return List[0]:código de erro; List[1]:double se habilita detecção; 0-não habilita; 1-habilita; List[2]:duração de confirmação da interrupção do arco (ms)
    */
    List<Integer> WeldingGetCheckArcInterruptionParam();

Definir Parâmetros de Recuperação de Interrupção de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define os parâmetros de recuperação de interrupção de soldagem do robô
    * @param [in] enable Se habilita a recuperação de interrupção de soldagem
    * @param [in] length Distância de sobreposição da solda (mm)
    * @param [in] velocity Percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100)
    * @param [in] moveType Modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP
    * @return Código de erro
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);

Obter Parâmetros de Recuperação de Interrupção de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obtém os parâmetros de recuperação de interrupção de soldagem do robô
    * @return List[0]:código de erro; List[1]:int se habilita recuperação de interrupção de soldagem; List[2]:double distância de sobreposição da solda (mm);
    * @return List[3]:double percentagem de velocidade do robô ao retornar ao ponto de reabertura de arco (0-100); List[4]:int modo de movimento do robô até o ponto de reabertura de arco; 0-LIN; 1-PTP
    */
    List<Number> WeldingGetReWeldAfterBreakOffParam();

Definir Porta DO Estendida do Modo de Controle da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a porta DO estendida do modo de controle da máquina de solda
    * @param [in] DONum Porta DO do modo de controle da máquina de solda (0-127)
    * @return Código de erro
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

Definir Modo de Controle da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define o modo de controle da máquina de solda
    * @param mode Modo de controle da máquina de solda; 0-modo unário CC; 1-modo unário pulsado; 2-modo JOB; 3-modo controle local; 4-modo separado; 5-modo CC/CV; 6-TIG; 7-CMT
    * @param ioType Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    * @return Código de erro* @return Código de erro
    */
    public int SetWeldMachineCtrlMode(int mode, int ioType)

Início da Soldagem
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da soldagem
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] arcNum Número do arquivo de configuração da máquina de solda
    * @param [in] timeout Tempo limite de abertura de arco
    * @return Código de erro
    */
    int ARCStart(int ioType, int arcNum, int timeout);

Fim da Soldagem
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da soldagem
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] arcNum Número do arquivo de configuração da máquina de solda
    * @param [in] timeout Tempo limite de extinção do arco
    * @return Código de erro
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

Início da Oscilação
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @return Código de erro
    */
    int WeaveStart(int weaveNum);

Fim da Oscilação
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da oscilação
    * @param [in] weaveNum Número de configuração dos parâmetros de oscilação de soldagem
    * @return Código de erro
    */
    int WeaveEnd(int weaveNum);

Alimentação de Arame para Frente
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Alimentação de arame para frente
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] wireFeed Controle de alimentação de arame 0-parar alimentação; 1-alimentar
    * @return Código de erro
    */
    int SetForwardWireFeed(int ioType, int wireFeed);

Alimentação de Arame para Trás
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Alimentação de arame para trás
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] wireFeed Controle de alimentação de arame 0-parar alimentação; 1-alimentar
    * @return Código de erro
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

Fornecimento de Gás
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fornecimento de gás
    * @param [in] ioType Tipo de E/S 0-E/S do controlador; 1-E/S estendida
    * @param [in] airControl Controle de fornecimento de gás 0-parar fornecimento; 1-fornecer
    * @return Código de erro
    */
    int SetAspirated(int ioType, int airControl);

Definir Retomada de Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a retomada de soldagem do robô após interrupção
    * @return Código de erro
    */
    int WeldingStartReWeldAfterBreakOff();

Definir Saída da Soldagem do Robô Após Interrupção
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define a saída da soldagem do robô após interrupção
    * @return Código de erro
    */
    int WeldingAbortWeldAfterBreakOff();

Exemplo de Código de Controle de Soldagem do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWelding(Robot robot)
    {
        robot.WeldingSetCurrent(0, 230, 0, 0);
        robot.WeldingSetVoltage(0, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCEnd(1, 0, 10000);
        robot.WeaveEnd(0);
        return 0;
    }

Início da Soldagem por Segmentos
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] tool Número da ferramenta
    * @param [in] user Número da peça
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
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, boolean isWeave, int weaveNum, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos);

Exemplo de Código de Soldagem por Segmentos do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSegWeld(Robot robot)
    {
        robot.WeldingSetCurrent(0, 230, 0, 0);
        robot.WeldingSetVoltage(0, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint, p2Desc);

        int rtn = robot.SegmentWeldStart(p1Desc, p2Desc, p1Joint, p2Joint, 20, 20, 0, 0, 5000, true, 0, 1, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese);
        return 0;
    }

Início da Oscilação de Simulação
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da oscilação de simulação
    * @param [in] weaveNum Número do parâmetro de oscilação
    * @return Código de erro
    */
    int WeaveStartSim(int weaveNum);

Fim da Oscilação de Simulação
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da oscilação de simulação
    * @param [in] weaveNum Número do parâmetro de oscilação
    * @return Código de erro
    */
    int WeaveEndSim(int weaveNum);

Início da Detecção de Alerta de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da detecção de alerta de trajetória (sem movimento)
    * @param [in] weaveNum Número do parâmetro de oscilação
    * @return Código de erro
    */
    int WeaveInspectStart(int weaveNum);

Fim da Detecção de Alerta de Trajetória (Sem Movimento)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da detecção de alerta de trajetória (sem movimento)
    * @param [in] weaveNum Número do parâmetro de oscilação
    * @return Código de erro
    */
    int WeaveInspectEnd(int weaveNum);

Início da Mudança Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Início da mudança gradual da oscilação
    * @param [in] weaveChangeFlag 1-alterar parâmetro de oscilação; 2-alterar parâmetro de oscilação + velocidade de soldagem
    * @param [in] weaveNum Número da oscilação
    * @param [in] velStart Velocidade inicial de soldagem, (cm/min)
    * @param [in] velEnd Velocidade final de soldagem, (cm/min)
    * @return Código de erro
    */
    int WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd)

Exemplo de Código de Soldagem com Mudança Gradual de Oscilação do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWeave(Robot robot)
    {
        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveStartSim(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.WeaveEndSim(0);
        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveInspectStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.WeaveInspectEnd(0);

        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveL(p1Joint, p1Desc, 1, 1, 100, 100, 50, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1, 0, 50, 30);
        robot.MoveL(p2Joint, p2Desc, 1, 1, 100, 100, 1, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
        return 0;
    }

Fim da Mudança Gradual da Oscilação
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.2-3.7.9

.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da mudança gradual da oscilação
    * @return Código de erro
    */
    int WeaveChangeEnd();

E/S Estendida - Configurar Sinal de Detecção de Gás da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de detecção de gás da máquina de solda
    * @param [in] DONum Número DO estendido do sinal de detecção de gás
    * @return Código de erro
    */
    int SetAirControlExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Abertura de Arco da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de abertura de arco da máquina de solda
    * @param [in] DONum Número DO estendido do sinal de abertura de arco da máquina de solda
    * @return Código de erro
    */
    int SetArcStartExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Alimentação de Arame para Trás da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de alimentação de arame para trás da máquina de solda
    * @param [in] DONum Número DO estendido do sinal de alimentação de arame para trás
    * @return Código de erro
    */
    int SetWireReverseFeedExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Alimentação de Arame para Frente da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de alimentação de arame para frente da máquina de solda
    * @param [in] DONum Número DO estendido do sinal de alimentação de arame para frente
    * @return Código de erro
    */
    int SetWireForwardFeedExtDoNum(int DONum);

E/S Estendida - Configurar Sinal de Sucesso de Abertura de Arco da Máquina de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de sucesso de abertura de arco da máquina de solda
    * @param [in] DINum Número DI estendido do sinal de sucesso de abertura de arco
    * @return Código de erro
    */
    int SetArcDoneExtDiNum(int DINum);

E/S Estendida - Configurar Sinal de Prontidão da Máquina de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de prontidão da máquina de solda
    * @param [in] DINum Número DI estendido do sinal de prontidão da máquina de solda
    * @return Código de erro
    */
    int SetWeldReadyExtDiNum(int DINum);

E/S Estendida - Configurar Sinal de Recuperação de Interrupção de Soldagem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief E/S estendida - configurar sinal de recuperação de interrupção de soldagem
    * @param [in] reWeldDINum Número DI estendido do sinal de retomada de soldagem após interrupção
    * @param [in] abortWeldDINum Número DI estendido do sinal de saída de soldagem após interrupção
    * @return Código de erro
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

Exemplo de Código para Configurar Sinais de Soldagem com E/S Estendida
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExtDIConfig(Robot robot)
    {
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);

        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);

        return 0;
    }

Controle de Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.2-3.7.9

.. code-block:: Java
    :linenos:

    /**
    * @brief Controle de rastreamento de arco
    * @param [in] flag Chave, 0-desligar; 1-ligar
    * @param [in] delaytime Tempo de atraso, em ms
    * @param [in] isLeftRight Compensação de desvio esquerda/direita
    * @param [in] klr Coeficiente de ajuste esquerda/direita (sensibilidade)
    * @param [in] tStartLr Tempo de início da compensação esquerda/direita cyc
    * @param [in] stepMaxLr Quantidade máxima de compensação por vez esquerda/direita mm
    * @param [in] sumMaxLr Quantidade máxima total de compensação esquerda/direita mm
    * @param [in] isUpLow Compensação de desvio acima/abaixo
    * @param [in] kud Coeficiente de ajuste acima/abaixo (sensibilidade)
    * @param [in] tStartUd Tempo de início da compensação acima/abaixo cyc
    * @param [in] stepMaxUd Quantidade máxima de compensação por vez acima/abaixo mm
    * @param [in] sumMaxUd Quantidade máxima total de compensação acima/abaixo
    * @param [in] axisSelect Seleção do sistema de coordenadas acima/abaixo, 0-oscilação; 1-ferramenta; 2-base
    * @param [in] referenceType Modo de definição da corrente de referência acima/abaixo, 0-feedback; 1-constante
    * @param [in] referSampleStartUd Início da amostragem da corrente de referência acima/abaixo (feedback), cyc
    * @param [in] referSampleCountUd Contagem do ciclo de amostragem da corrente de referência acima/abaixo (feedback), cyc
    * @param [in] referenceCurrent Corrente de referência acima/abaixo mA
    * @param [in] offsetType Tipo de rastreamento com deslocamento, 0-sem deslocamento; 1-amostragem; 2-percentagem
    * @param [in] offsetParameter Parâmetro de deslocamento; amostragem (tempo de início da amostragem de deslocamento, padrão um ciclo); percentagem (percentagem de deslocamento (-100 ~ 100))
    * @return Código de erro
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

Seleção da Banda de Passagem AI do Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Seleção da banda de passagem AI do rastreamento de arco
    * @param channel Banda de passagem AI do rastreamento de arco, [0-3]
    * @return Código de erro
    */
    public int ArcWeldTraceExtAIChannelConfig(int channel)

Ativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Ativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes
    * @return Código de erro
    */
    public int ArcWeldTraceReplayStart()

Desativação da Compensação de Rastreamento de Arco + Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Desativação da compensação de rastreamento de arco + múltiplas camadas e múltiplos passes
    * @return Código de erro
    */
    public int ArcWeldTraceReplayEnd()

Mudança de Coordenadas de Deslocamento - Soldagem de Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Mudança de coordenadas de deslocamento - soldagem de múltiplas camadas e múltiplos passes
    * @param pointO Pose cartesiana do ponto de referência
    * @param pointX Pose cartesiana do ponto de direção de deslocamento no eixo X do ponto de referência
    * @param pointZ Pose cartesiana do ponto de direção de deslocamento no eixo Z do ponto de referência
    * @param dx Quantidade de deslocamento na direção X (mm)
    * @param dz Quantidade de deslocamento na direção Z (mm)
    * @param dry Quantidade de deslocamento em torno do eixo Y (°)
    * @param offset Deslocamento calculado
    * @return Código de erro
    */
    public int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dz, double dry, DescPose offset)

Exemplo de Código de Rastreamento de Arco com Soldagem de Múltiplas Camadas e Múltiplos Passes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestArcWeldTrace(Robot robot)
    {
        JointPos mulitilineorigin1_joint = new JointPos(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
        DescPose mulitilineorigin1_desc = new DescPose(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);

        DescTran mulitilineX1_desc = new DescTran(0, 0, 0);
        mulitilineX1_desc.x = -677.556;
        mulitilineX1_desc.y = 211.949;
        mulitilineX1_desc.z = -1.206;

        DescTran mulitilineZ1_desc = new DescTran(0, 0, 0);
        mulitilineZ1_desc.x = -677.564;
        mulitilineZ1_desc.y = 190.956;
        mulitilineZ1_desc.z = 19.817;

        JointPos mulitilinesafe_joint = new JointPos(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
        DescPose mulitilinesafe_desc = new DescPose(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
        JointPos mulitilineorigin2_joint = new JointPos(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
        DescPose mulitilineorigin2_desc = new DescPose(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);

        DescTran mulitilineX2_desc = new DescTran(0, 0, 0);
        mulitilineX2_desc.x = -563.965;
        mulitilineX2_desc.y = 220.355;
        mulitilineX2_desc.z = -0.680;

        DescTran mulitilineZ2_desc = new DescTran(0, 0, 0);
        mulitilineZ2_desc.x = -563.968;
        mulitilineZ2_desc.y = 215.362;
        mulitilineZ2_desc.z = 4.331;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset = new DescPose(0, 0, 0, 0, 0, 0);

        robot.Sleep(10);
        int error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0, epos, 0, 0, offset, 0, 100);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, 0, epos, 0, 0, offset, 0, 100);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0, epos, 0, 0, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.WeaveStart(0);

        error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10, 0, 0);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, 0, epos, 0, 0, offset, 0, 100);

        error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10, 0, 0);

        error = robot.WeaveEnd(0);

        error = robot.ARCEnd(1, 0, 10000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0, epos, 0, 1, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);

        error = robot.ArcWeldTraceReplayStart();

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, 0, epos, 0, 1, offset, 0, 100);

        error = robot.ArcWeldTraceReplayEnd();

        error = robot.ARCEnd(1, 0, 10000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0, epos, 0, 1, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);

        error = robot.ArcWeldTraceReplayStart();

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, 0, epos, 0, 1, offset, 0, 100);

        error = robot.ArcWeldTraceReplayEnd();

        error = robot.ARCEnd(1, 0, 3000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        robot.CloseRPC();
        return 0;
    }

Seleção do Canal AI de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Seleção do canal AI de feedback de corrente da máquina de solda para rastreamento de arco
    * @param [in] channel Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1
    * @return Código de erro
    */
    int ArcWeldTraceAIChannelCurrent(int channel)

Seleção do Canal AI de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Seleção do canal AI de feedback de tensão da máquina de solda para rastreamento de arco
    * @param [in] channel Canal; 0-AI estendido 0; 1-AI estendido 1; 2-AI estendido 2; 3-AI estendido 3; 4-AI da caixa de controle 0; 5-AI da caixa de controle 1
    * @return Código de erro
    */
    int ArcWeldTraceAIChannelVoltage(int channel)

Parâmetros de Conversão de Feedback de Corrente da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Parâmetros de conversão de feedback de corrente da máquina de solda para rastreamento de arco
    * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
    * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
    * @param [in] currentLow Valor de corrente da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
    * @param [in] currentHigh Valor de corrente da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]
    * @return Código de erro
    */
    int ArcWeldTraceCurrentPara(double AILow, double AIHigh, double currentLow, double currentHigh)

Parâmetros de Conversão de Feedback de Tensão da Máquina de Solda para Rastreamento de Arco
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Parâmetros de conversão de feedback de tensão da máquina de solda para rastreamento de arco
    * @param [in] AILow Limite inferior do canal AI, valor padrão 0V, intervalo [0-10V]
    * @param [in] AIHigh Limite superior do canal AI, valor padrão 10V, intervalo [0-10V]
    * @param [in] voltageLow Valor de tensão da máquina de solda correspondente ao limite inferior do AI, valor padrão 0V, intervalo [0-200V]
    * @param [in] voltageHigh Valor de tensão da máquina de solda correspondente ao limite superior do AI, valor padrão 100V, intervalo [0-200V]
    * @return Código de erro
    */
    int ArcWeldTraceVoltagePara(double AILow, double AIHigh, double voltageLow, double voltageHigh)

Exemplo de Código de Rastreamento de Arco
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void WeldTraceControlWithCtrlBoxAI(Robot robot)
    {
        DescPose startdescPose = new DescPose(-473.86, 257.879, -20.849, -37.317, -42.021, 2.543);
        JointPos startjointPos = new JointPos(-43.487, -76.526, 95.568, -104.445, -89.356, 3.72);

        DescPose safedescPose = new DescPose(-504.043, 275.181, 40.908, -28.002, -42.025, -14.044);
        JointPos safejointPos = new JointPos(-39.078, -76.732, 87.227, -99.47, -94.301, 18.714);

        DescPose enddescPose = new DescPose(-499.844, 141.225, 7.72, -34.856, -40.17, 13.13);
        JointPos endjointPos = new JointPos(-31.305, -82.998, 99.401, -104.426, -89.35, 3.696);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        // Movimento inicial para ponto seguro
        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 20, 100, exaxisPos, -1, 0, offdese);

        WeldCurrentAORelation current = new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation voltage = new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(current); // Relação corrente-saída analógica
        robot.WeldingSetVoltageRelation(voltage); // Relação tensão-saída analógica
        robot.WeldingSetVoltage(0, 25, 1, 0); // Definir tensão
        robot.WeldingSetCurrent(0, 260, 0, 0); // Definir corrente

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        System.out.println("ArcWeldTraceAIChannelCurrent rtn is " + rtn);

        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        System.out.println("ArcWeldTraceAIChannelVoltage rtn is " + rtn);

        rtn = robot.ArcWeldTraceCurrentPara(0.0, 5, 0, 500);
        System.out.println("ArcWeldTraceCurrentPara rtn is " + rtn);

        rtn = robot.ArcWeldTraceVoltagePara(1.018, 10, 0, 50);
        System.out.println("ArcWeldTraceVoltagePara rtn is " + rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offdese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offdese);
    }

Definir Portas E/S Estendidas para Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Define as portas E/S estendidas para busca de posição do arame de solda
    * @param [in] searchDoneDINum Porta DO de sucesso na busca de posição do arame (0-127)
    * @param [in] searchStartDONum Porta DO de controle de início/parada da busca de posição do arame (0-127)
    * @return Código de erro
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

Programa de Exemplo
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    private static void TestUDPWireSearch(Robot robot)
    {
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10, 0);
        robot.ExtDevSetUDPComParam(param); // comunicação UDP com eixo estendido

        robot.SetWireSearchExtDIONum(0, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        DescPose descStart = new DescPose(-158.767, -510.596, 271.709, -179.427, -0.745, -137.349);
        JointPos jointStart = new JointPos(61.667, -79.848, 108.639, -119.682, -89.700, -70.985);

        DescPose descEnd = new DescPose(0.332, -516.427, 270.688, 178.165, 0.017, -119.989);
        JointPos jointEnd = new JointPos(79.021, -81.839, 110.752, -118.298, -91.729, -70.981);

        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);

        DescPose descREF0A = new DescPose(-66.106, -560.746, 270.381, 176.479, -0.126, -126.745);
        JointPos jointREF0A = new JointPos(73.531, -75.588, 102.941, -116.250, -93.347, -69.689);

        DescPose descREF0B = new DescPose(-66.109, -528.440, 270.407, 176.479, -0.129, -126.744);
        JointPos jointREF0B = new JointPos(72.534, -79.625, 108.046, -117.379, -93.366, -70.687);

        DescPose descREF1A = new DescPose(72.975, -473.242, 270.399, 176.479, -0.129, -126.744);
        JointPos jointREF1A = new JointPos(87.169, -86.509, 115.710, -117.341, -92.993, -56.034);

        DescPose descREF1B = new DescPose(31.355, -473.238, 270.405, 176.480, -0.130, -126.745);
        JointPos jointREF1B = new JointPos(82.117, -87.146, 116.470, -117.737, -93.145, -61.090);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  // ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  // ponto de direção
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  // ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  // ponto de direção
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  // ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  // ponto de direção
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  // ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  // ponto de direção
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef = {"REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = {"RES0", "RES1", "#", "#", "#", "#"};
        int offectFlag = 0;
        //DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        DescOffset offset = new DescOffset();
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offset);
        robot.PointsOffsetEnable(0, offset.offset);
        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);
        robot.PointsOffsetDisable();
    }

Início da Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da busca de posição do arame de solda
    * @param [in] refPos 1-ponto de referência 0-ponto de contato
    * @param [in] searchVel Velocidade de busca %
    * @param [in] searchDis Distância de busca mm
    * @param [in] autoBackFlag Flag de retorno automático, 0-não automático; -automático
    * @param [in] autoBackVel Velocidade de retorno automático %
    * @param [in] autoBackDis Distância de retorno automático mm
    * @param [in] offectFlag 1-busca com deslocamento; 0-busca no ponto ensinado
    * @return Código de erro
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

Fim da Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da busca de posição do arame de solda
    * @param [in] refPos 1-ponto de referência 2-ponto de contato
    * @param [in] searchVel Velocidade de busca %
    * @param [in] searchDis Distância de busca mm
    * @param [in] autoBackFlag Flag de retorno automático, 0-não automático; -automático
    * @param [in] autoBackVel Velocidade de retorno automático %
    * @param [in] autoBackDis Distância de retorno automático mm
    * @param [in] offectFlag 1-busca com deslocamento; 2-busca no ponto ensinado
    * @return Código de erro
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

Calcular Deslocamento da Busca de Posição do Arame de Solda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Calcular deslocamento da busca de posição do arame de solda
    * @param [in] seamType Tipo de solda
    * @param [in] method Método de cálculo
    * @param [in] varNameRef Pontos de referência 1-6, "#" indica ausência de ponto variável
    * @param [in] varNameRes Pontos de contato 1-6, "#" indica ausência de ponto variável
    * @param [out] offset Deslocamento da pose [x, y, z, a, b, c] e modo de deslocamento
    * @return Código de erro
    */
    int GetWireSearchOffset(int seamType, int method, String[] varNameRef, String[] varNameRes, DescOffset offset);

Aguardar Conclusão da Busca de Posição do Arame de Solda
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Aguardar conclusão da busca de posição do arame de solda
    * @return Código de erro
    */
    int WireSearchWait(String name);

Escrever Ponto de Contato da Busca de Posição do Arame no Banco de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Escrever ponto de contato da busca de posição do arame no banco de dados
    * @param [in] varName Nome do ponto de contato "RES0" ~ "RES99"
    * @param [in] pos Dados do ponto de contato [x, y, x, a, b, c]
    * @return Código de erro
    */
    int SetPointToDatabase(String varName, DescPose pos);

Exemplo de Código de Busca de Posição do Arame de Solda do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWireSearch(Robot robot)
    {
        DescPose toolCoord = new DescPose(0, 0, 200, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);
        DescPose wobjCoord = new DescPose(0, 0, 0, 0, 0, 0);
        robot.SetWObjCoord(1, wobjCoord, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(216.543, 445.175, 93.465, 179.683, 1.757, -112.641);
        JointPos jointStart = new JointPos(-128.345, -86.660, 114.679, -119.625, -89.219, 74.303);

        DescPose descEnd = new DescPose(111.143, 523.384, 87.659, 179.703, 1.835, -97.750);
        JointPos jointEnd = new JointPos(-113.454, -81.060, 109.328, -119.954, -89.218, 74.302);

        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 100);

        DescPose descREF0A = new DescPose(142.135, 367.604, 86.523, 179.728, 1.922, -111.089);
        JointPos jointREF0A = new JointPos(-126.794, -100.834, 128.922, -119.864, -89.218, 74.302);

        DescPose descREF0B = new DescPose(254.633, 463.125, 72.604, 179.845, 2.341, -114.704);
        JointPos jointREF0B = new JointPos(-130.413, -81.093, 112.044, -123.163, -89.217, 74.303);

        DescPose descREF1A = new DescPose(92.556, 485.259, 47.476, -179.932, 3.130, -97.512);
        JointPos jointREF1A = new JointPos(-113.231, -83.815, 119.877, -129.092, -89.217, 74.303);

        DescPose descREF1B = new DescPose(203.103, 583.836, 63.909, 179.991, 2.854, -103.372);
        JointPos jointREF1B = new JointPos(-119.088, -69.676, 98.692, -121.761, -89.219, 74.303);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);  // ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 1, 0, offdese, 0, 10);  // ponto de direção
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);  // ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 1, 0, offdese, 0, 10);  // ponto de direção
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);  // ponto inicial
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 1, 0, offdese, 0, 10);  // ponto de direção
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);  // ponto inicial
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 1, 0, offdese, 0, 10);  // ponto de direção
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef = new String[]{"REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = new String[]{"RES0", "RES1", "#", "#", "#", "#"};
        int offectFlag = 0;

        DescPose pos = new DescPose(0, 0, 0, 0, 0, 0);
        DescOffset offectPos = new DescOffset();
        offectPos.offset = pos;
        offectPos.offsetFlag = 0;

        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectPos);
        robot.PointsOffsetEnable(0, pos);
        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, 0, exaxisPos, 1, 0, offdese, 0, 10);
        robot.PointsOffsetDisable();

        robot.CloseRPC();
        return 0;
    }

Definir Início da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
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
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend)

Definir Fim da Mudança Gradual da Tensão de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Define o fim da mudança gradual da tensão de soldagem
    * @return Código de erro
    */
    int WeldingSetVoltageGradualChangeEnd()

Definir Início da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Define o início da mudança gradual da corrente de soldagem
    * @param [in] IOType Tipo de controle; 0-E/S da caixa de controle; 1-protocolo de comunicação digital (UDP); 2-protocolo de comunicação digital (ModbusTCP)
    * @param [in] currentStart Corrente de soldagem inicial (A)
    * @param [in] currentEnd Corrente de soldagem final (A)
    * @param [in] AOIndex Número da porta AO da caixa de controle (0-1)
    * @param [in] blend Se suaviza 0-não suaviza; 1-suaviza
    * @return Código de erro
    */
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend)

Definir Fim da Mudança Gradual da Corrente de Soldagem
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Define o fim da mudança gradual da corrente de soldagem
    * @return Código de erro
    */
    int WeldingSetCurrentGradualChangeEnd()

Exemplo de Código de Mudança Gradual de Corrente e Tensão de Soldagem do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void WeldparamChange(Robot robot)
    {
        DescPose startdescPose = new DescPose(-484.707, 276.996, -14.013, -37.657, -40.508, -1.548);
        JointPos startjointPos = new JointPos(-45.421, -75.673, 93.627, -104.302, -87.938, 6.005);

        DescPose enddescPose = new DescPose(-508.767, 137.109, -13.966, -37.639, -40.508, -1.559);
        JointPos endjointPos = new JointPos(-32.768, -80.947, 100.254, -106.201, -87.201, 18.648);

        DescPose safedescPose = new DescPose(-484.709, 294.436, 13.621, -37.660, -40.508, -1.545);
        JointPos safejointPos = new JointPos(-46.604, -75.410, 89.109, -100.003, -88.012, 4.823);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        WeldCurrentAORelation cur = new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation vol = new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(cur);
        robot.WeldingSetVoltageRelation(vol);

        robot.WeldingSetVoltage(0, 25, 1, 0); // ---- definir tensão
        robot.WeldingSetCurrent(0, 260, 0, 0); // ---- definir corrente

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        int rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);
        System.out.println("ArcWeldTraceControl rtn is " + rtn);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(2, 1, 24, 36);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }

Definir Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
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
    public int CustomWeaveSetPara(int id, int pointNum, DescTran[] point, double[] stayTime, double frequency, int incStayType, int stationary)

Obter Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
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
    public int CustomWeaveGetPara(int id, int[] pointNum, DescTran[] point, double[] stayTime, double[] frequency, int[] incStayType, int[] stationary)

Exemplo de Código de Parâmetros de Oscilação Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestCustomWeaveSetPara(Robot robot)
    {
        DescTran[] point = new DescTran[10];
        point[0] = new DescTran();
        point[0].x = -3;
        point[0].y = -3;
        point[0].z = 0;

        point[1] = new DescTran();
        point[1].x = -6;
        point[1].y = 0;
        point[1].z = 0;

        point[2] = new DescTran();
        point[2].x = -3;
        point[2].y = 3;
        point[2].z = 0;

        point[3] = new DescTran();
        point[3].x = 0;
        point[3].y = 0;
        point[3].z = 0;
        point[4] = new DescTran(0, 0, 0);
        point[5] = new DescTran(0, 0, 0);
        point[6] = new DescTran(0, 0, 0);
        point[7] = new DescTran(0, 0, 0);
        point[8] = new DescTran(0, 0, 0);
        point[9] = new DescTran(0, 0, 0);

        double[] stayTime = new double[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0);
        System.out.println("CustomWeaveSetPara rtn is :" + rtn);
        robot.Sleep(1000);

        int[] pointNum = new int[1];
        double[] frequency = new double[1];
        int[] incStayType = new int[1];
        int[] stationary = new int[1];
        robot.CustomWeaveGetPara(2, pointNum, point, stayTime, frequency, incStayType, stationary);
        System.out.println("pointNum is :" + pointNum[0]);
        for (int i = 0; i < pointNum[0]; i++)
        {
            System.out.println("point:" + i + ", " + point[i].x + ", " + point[i].y + ", " + point[i].z);
        }
        System.out.println("fre is :" + frequency[0] + ", stay is:" + incStayType[0] + ", " + stationary[0]);

        robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000,
                6.000000, 5.000000, 50, 100, 100,
                0, 1, 0.000000, 0.000000);

        DescPose desc_p1 = new DescPose(-288.650, 367.807, 288.404, 0.000, -0.001, 0.001);
        DescPose desc_p2 = new DescPose(-431.714, 367.815, 288.415, 0.001, 0.001, 0.000);
        DescPose desc_p3 = new DescPose(-348.666, 427.798, 288.404, -0.000, -0.000, 0.001);
        JointPos j1 = new JointPos(140.656, -84.560, -91.707, -93.734, 90.000, 50.655);
        JointPos j2 = new JointPos(149.873, -98.298, -77.599, -94.103, 90.000, 59.873);
        JointPos j3 = new JointPos(139.773, -96.173, -80.014, -93.814, 90.000, 49.772);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.Circle(j3, desc_p3, 3, 0, 100, 100, epos, j2, desc_p2, 3, 0, 100, 100, epos, 10, -1, offset_pos, 0, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveC(j3, desc_p3, 3, 0, 100, 100, epos, 0, offset_pos, j2, desc_p2, 3, 0, 100, 100, epos, 0, offset_pos, 10, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2, 3, 0, 100, 100, 10, -1, epos, 0, 0, offset_pos, 0, 0, 100);
        robot.WeaveEnd(0);

        robot.CloseRPC();
    }

Configuração de Parâmetros da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configuração de parâmetros da soldadora a laser
    * @param  io_type Tipo de comunicação 0-IO 1-UDP
    * @param  num Número do grupo a ser configurado (1~10)
    * @param  scanSpeed Velocidade de varredura
    * @param  scanWidth Largura de varredura
    * @param  peakPower Potência de pico
    * @param  dutyCycle Ciclo de trabalho
    * @param  freq Frequência
    * @return Código de erro
    */
    public int SetLaserWeldingParam(int io_type, int num, int scanSpeed, int scanWidth, int peakPower, int dutyCycle, int freq);

Iniciar/Parar Soldagem a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Iniciar/parar soldagem a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param status Palavra de controle 0-laser desligado 1-laser ligado
    * @param max_waittime Tempo máximo de espera em milissegundos, padrão 10000
    * @return Código de erro
    */
    public int SetLaserWeldingStartEnd(int io_type, int status, int max_waittime)

Habilitar/Desabilitar Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Habilitar/desabilitar soldadora a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param status 0-desabilitar 1-habilitar
    * @return Código de erro
    */
    public int SetLaserWeldingEnable(int io_type, int status)

Reset de Falha da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Reset de falha da soldadora a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param status Palavra de controle 0-inválido 1-reset de falha
    * @return Código de erro
    */
    public int ResetLaserWeldingErr(int io_type, int status)

Obter Estado de Operação da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obter estado de operação da soldadora a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param  status Palavra de controle 0-parado 1-operando
    * @return Código de erro
    */
    public int GetLaserWeldingRunningState(int io_type, int[] status)

Obter Estado de Falha da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obter estado de falha da soldadora a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param  status 0-sem falha 1-com falha
    * @return Código de erro
    */
    public int GetLaserWeldingErrState(int io_type, int[] status)

Obter Parâmetros de Configuração da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obter parâmetros de configuração de um dos 10 grupos de processo da soldadora a laser
    * @param num Número do grupo a ser configurado (1~10)
    * @param params Array de parâmetros de saída: [scanSpeed, scanWidth, peakPower, dutyCycle, freq]
    * @return Código de erro
    */
    public int GetLaserWeldingParamTarget(int num, int[] params)

Obter Parâmetros de Configuração Ativos da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Obter parâmetros de configuração ativos da soldadora a laser
    * @param io_type Tipo de comunicação 0-IO 1-UDP
    * @param params Array de parâmetros de saída: [scanSpeed, scanWidth, peakPower, dutyCycle, freq]
    * @return Código de erro
    */
    public int GetLaserWeldingParamActual(int io_type, int[] params)

Configurar Porta DO de E/S Expansão para Habilitar Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para habilitar soldadora a laser
    * @param ctrlModeDONum Número da porta DO de E/S expansão para habilitar a soldadora a laser
    * @return Código de erro
    */
    public int SetLaserWeldingEnableExtDoNum(int ctrlModeDONum)

Configurar Porta DO de E/S Expansão para Iniciar Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para iniciar soldadora a laser
    * @param ctrlModeDONum Número da porta DO de E/S expansão para iniciar/parar a soldadora a laser
    * @return Código de erro
    */
    public int SetLaserWeldingStartExtDoNum(int ctrlModeDONum)

Configurar Porta DO de E/S Expansão para Reset de Falha da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configurar porta DO de E/S expansão para reset de falha da soldadora a laser
    * @param ctrlModeDONum Número da porta DO de E/S expansão para reset de falha da soldadora a laser
    * @return Código de erro
    */
    public int SetLaserWeldingErrResetExtDoNum(int ctrlModeDONum)

Configurar Porta DI de E/S Expansão para Estado de Operação (Laser Ligado) da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configurar porta DI de E/S expansão para estado de operação (laser ligado) da soldadora a laser
    * @param diNum Número da porta DI de E/S expansão para estado de operação (laser ligado) da soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    public int SetLaserWeldingRunningStateExtDiNum(int diNum);

Configurar Porta DI de E/S Expansão para Estado de Falha da Soldadora a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Configurar porta DI de E/S expansão para estado de falha da soldadora a laser
    * @param diNum Número da porta DI de E/S expansão para estado de falha da soldadora a laser
    * @return Código de erro, 0 indica sucesso, diferente de 0 indica falha
    */
    public int SetLaserWeldingErrStateExtDiNum(int diNum);

Exemplo de Código de Soldagem a Laser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int testLsaerWeld(Robot robot) {
        int rtn = -1;
        rtn = robot.ExtDevLoadUDPDriver();
        if (rtn != 0) {
            System.out.println("Falha ao carregar driver UDP, código de erro: " + rtn);
        }
        robot.Sleep(1000);
        rtn = robot.SetLaserWeldingParam(1, 3, 2000, 3, 1500, 100, 1000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingParam falhou, código de erro: " + rtn);
        } else {
            System.out.println("SetLaserWeldingParam sucesso");
        }
        rtn = robot.SetLaserWeldingStartExtDoNum(1);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartExtDoNum falhou, código de erro: " + rtn);
        }
        rtn = robot.Mode(0);
        if (rtn != 0) {
            System.out.println("Falha ao definir modo 0, código de erro: " + rtn);
        }
        robot.Sleep(1000);
        DescPose desc_pos1 = new DescPose(-303.721, -206.960, 297.105, 152.209, 19.857, 109.166);
        DescPose desc_pos2 = new DescPose(-301.575, -254.888, 284.786, 155.919, 26.946, 111.629);
        DescPose desc_safe = new DescPose(-344.386, -280.830, 435.073, 173.835, 15.333, 124.931);

        JointPos jointPos1 = new JointPos(9.827, -99.740, 120.088, -78.900, -77.241, -17.904);
        JointPos jointPos2 = new JointPos(15.251, -96.456, 120.138, -84.664, -68.542, -17.843);
        JointPos jointSafe = new JointPos(19.142, -98.078, 101.493, -83.078, -77.070, -17.794);

        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offset = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int error = robot.MoveL(desc_pos1, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0,0);
        System.out.println("MoveL para pos1 retorno: " + error);
        rtn = robot.SetLaserWeldingStartEnd(1, 1, 10000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartEnd (iniciar) falhou, código de erro: " + rtn);
        } else {
            System.out.println("Laser iniciado");
        }
        rtn = robot.MoveL(desc_pos2, 0, 0, 30, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0, 0);
        System.out.println("MoveL para pos2 retorno: " + rtn);
        rtn = robot.SetLaserWeldingStartEnd(1, 0, 10000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartEnd (parar) falhou, código de erro: " + rtn);
        } else {
            System.out.println("Laser parado");
        }
        robot.Sleep(500);
        rtn = robot.MoveL(desc_safe, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0,0);
        System.out.println("MoveL para safe_pos retorno: " + rtn);
        rtn = robot.Mode(1);
        if (rtn != 0) {
            System.out.println("Falha ao definir modo 1, código de erro: " + rtn);
        }
        robot.Sleep(1000);
        robot.CloseRPC();
        robot.Sleep(1000);

        System.out.println("Teste concluído");

        return 0;
    }