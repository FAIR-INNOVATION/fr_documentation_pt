Movimento do Robô
========================

.. toctree::
    :maxdepth: 5


Movimento Jog
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento jog
    * @param [in] ref 0-jog por junta, 2-jog no sistema de coordenadas base, 4-jog no sistema de coordenadas da ferramenta, 8-jog no sistema de coordenadas da peça
    * @param [in] nb 1-junta1 (ou eixo X), 2-junta2 (ou eixo Y), 3-junta3 (ou eixo Z), 4-junta4 (ou rotação em torno do eixo X), 5-junta5 (ou rotação em torno do eixo Y), 6-junta6 (ou rotação em torno do eixo Z)
    * @param [in] dir 0-direção negativa, 1-direção positiva
    * @param [in] vel Percentagem de velocidade, [0~100]
    * @param [in] acc Percentagem de aceleração, [0~100]
    * @param [in] max_dis Ângulo máximo por movimento jog, em [°] ou distância, em [mm]
    * @return Código de erro
    */
    errno_t StartJOG(uint8_t ref, uint8_t nb, uint8_t dir, float vel, float acc, float max_dis);

Parada Desacelerada do Movimento Jog
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Parada desacelerada do movimento jog
    * @param [in] ref 1-parada de jog por junta, 3-parada de jog no sistema de coordenadas base, 5-parada de jog no sistema de coordenadas da ferramenta, 9-parada de jog no sistema de coordenadas da peça
    * @return Código de erro
    */
    errno_t StopJOG(uint8_t ref);

Parada Imediata do Movimento Jog
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Parada imediata do movimento jog
    * @return Código de erro
    */
    errno_t ImmStopJOG();

Exemplo de Código de Controle de Movimento Jog do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestJOG(void)
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
        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0);
            robot.Sleep(1000);
            robot.ImmStopJOG();
            robot.Sleep(1000);
        }
        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0);
            robot.Sleep(1000);
            robot.ImmStopJOG();
            robot.Sleep(1000);
        }
        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0);
            robot.Sleep(1000);
            robot.StopJOG(5);
            robot.Sleep(1000);
        }
        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0);
            robot.Sleep(1000);
            robot.StopJOG(9);
            robot.Sleep(1000);
        }
        robot.CloseRPC();
        return 0;
    }

Movimento no Espaço Articular
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento no espaço articular
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] blendT [-1.0]-movimento até o final (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), em ms
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @return Código de erro
    */
    errno_t MoveJ(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos *epos, float blendT, uint8_t offset_flag, DescPose *offset_pos);

Movimento no Espaço Articular (com cálculo automático de cinemática direta)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento no espaço articular (com cálculo automático de cinemática direta)
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] blendT [-1.0]-movimento até o final (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), em ms
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @return Código de erro
    */
    errno_t MoveJ(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos* epos, float blendT, uint8_t offset_flag, DescPose* offset_pos);

Movimento Linear no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param [in] speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    errno_t MoveL(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos, float oacc = 100.0, int velAccParamMode = 0, int overSpeedStrategy = 0, int speedPercent = 10);

Movimento Linear no Espaço Cartesiano (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param [in] speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    errno_t MoveL(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos* epos, uint8_t search, uint8_t offset_flag, DescPose* offset_pos, int config = -1, int overSpeedStrategy = 0, int speedPercent = 10);

Movimento Circular no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano
    * @param [in] joint_pos_p Posição articular do ponto de passagem, em graus
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] puser Número da coordenada da peça, intervalo [0~14]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Deslocamento de pose
    * @param [in] joint_pos_t Posição articular do ponto alvo, em graus
    * @param [in] desc_pos_t Pose cartesiana do ponto alvo
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] tuser Número da coordenada da peça, intervalo [0~14]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t Deslocamento de pose
    * @param [in] ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    errno_t MoveC(JointPos *joint_pos_p, DescPose *desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos *epos_p, uint8_t poffset_flag, DescPose *offset_pos_p, JointPos *joint_pos_t, DescPose *desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos *epos_t, uint8_t toffset_flag, DescPose *offset_pos_t, float ovl, float blendR, float oacc = 100.0, int velAccParamMode = 0);

Movimento Circular no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] puser Número da coordenada da peça, intervalo [0~14]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Deslocamento de pose
    * @param [in] desc_pos_t Pose cartesiana do ponto alvo
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] tuser Número da coordenada da peça, intervalo [0~14]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t Deslocamento de pose
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t MoveC(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, uint8_t poffset_flag, DescPose* offset_pos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, uint8_t toffset_flag, DescPose* offset_pos_t, float ovl, float blendR, int config = -1);

Movimento Circular Completo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento circular completo no espaço cartesiano
    * @param [in] joint_pos_p Posição articular do ponto de passagem 1, em graus
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem 1
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] puser Número da coordenada da peça, intervalo [0~14]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] joint_pos_t Posição articular do ponto de passagem 2, em graus
    * @param [in] desc_pos_t Pose cartesiana do ponto de passagem 2
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] tuser Número da coordenada da peça, intervalo [0~14]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    * @param [in] blendR -1: bloqueante; 0~1000: raio de suavização
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    errno_t Circle(JointPos* joint_pos_p, DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, JointPos* joint_pos_t, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int velAccParamMode = 0);

Movimento Circular Completo no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento circular completo no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem 1
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] puser Número da coordenada da peça, intervalo [0~14]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] desc_pos_t Pose cartesiana do ponto de passagem 2
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] tuser Número da coordenada da peça, intervalo [0~14]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] oacc Percentagem de aceleração
    * @param [in] blendR -1: bloqueante; 0~1000: raio de suavização
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t Circle(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int config = -1);

Movimento Ponto a Ponto no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento ponto a ponto no espaço cartesiano
    * @param [in] desc_pos Pose cartesiana alvo ou incremento de pose
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendT [-1.0]-movimento até o final (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), em ms
    * @param [in] config Configuração do espaço articular, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular, padrão -1
    * @return Código de erro
    */
    errno_t MoveCart(DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

Exemplo de Código de Instruções Básicas de Movimento do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMove(void)
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

        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float oacc = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, oacc, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&j3, &desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &j4, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, oacc, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&j3, &desc_pos3, tool, user, vel, acc, &epos, &j1, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(&desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, -1, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, -1, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&desc_pos3, tool, user, vel, acc, &epos, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, blendR, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        robot.CloseRPC();
        return 0;
    }

Movimento Helicoidal no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento helicoidal no espaço cartesiano
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] spiral_param Parâmetros da espiral
    * @return Código de erro
    */
    errno_t NewSpiral(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, ExaxisPos *epos, float ovl, uint8_t offset_flag, DescPose *offset_pos, SpiralParam spiral_param);

Movimento Helicoidal no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento helicoidal no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] spiral_param Parâmetros da espiral
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t NewSpiral(DescPose* desc_pos, int tool, int user, float vel, float acc, ExaxisPos* epos, float ovl, uint8_t offset_flag, DescPose* offset_pos, SpiralParam spiral_param, int config = -1);

Exemplo de Código de Movimento Helicoidal
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSpiral(void)
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
      JointPos j(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      DescPose desc_pos(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose offset_pos1(50, 0, 0, -30, 0, 0);
      DescPose offset_pos2(50, 0, 0, -5, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      SpiralParam sp;
      sp.circle_num = 5;
      sp.circle_angle = 5.0;
      sp.rad_init = 50.0;
      sp.rad_add = 10.0;
      sp.rotaxis_add = 10.0;
      sp.rot_direction = 0;
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = 0.0;
      uint8_t flag = 2;
      robot.SetSpeed(20);
      rtn = robot.MoveJ(&j, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos1);
      printf("movej errcode:%d\n", rtn);
      rtn = robot.NewSpiral(&desc_pos, tool, user, vel, acc, &epos, ovl, flag, &offset_pos2, sp);
      printf("newspiral errcode:%d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

Início do Movimento Servo
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Início do movimento servo, para uso com instruções ServoJ e ServoCart
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoMoveStart(int comType = 0);

Fim do Movimento Servo
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Fim do movimento servo, para uso com instruções ServoJ e ServoCart
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoMoveEnd(int comType = 0);

Movimento no Modo Servo no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento no modo servo no espaço articular
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] axisPos Posição do eixo externo, em mm
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param [in] vel Percentagem de velocidade, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param [in] cmdT Período de envio de instrução, em s, intervalo recomendado [0.001~0.0016]
    * @param [in] filterT Tempo de filtro, em s, temporariamente não disponível, padrão 0
    * @param [in] gain Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0
    * @param [in] id ID da instrução ServoJ, padrão 0
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoJ(JointPos *joint_pos, ExaxisPos* axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id = 0, int comType = 0);

Programa de Exemplo de Movimento no Modo Servo no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoJ(void)
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
        JointPos j(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.008;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 500;
        float dt = 0.1;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, &j);
        if (ret == 0)
        {
            robot.ServoMoveStart();
            while (count)
            {
                robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID);
                j.jPos[0] += dt;
                count -= 1;
                robot.WaitMs(cmdT * 1000);
            }
            robot.ServoMoveEnd();
        }
        else
        {
            printf("GetActualJointPosDegree errcode:%d\n", ret);
        }
        robot.CloseRPC();
        return 0;
    }

Exemplo de Código de Movimento no Modo Servo no Espaço Articular com comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    void UDPFrameCallBack(int srcType, int count, int cmdID, int len, std::string content)
    {
        cout << "recv cmd: cmdID:  " << to_string(cmdID) << "  content is " << content << "  count is " << count << endl;;
            return;
    }

    int TestServoJUDP(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        int rtn = 0;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        rtn = robot.SetCmdRpyCallback(UDPFrameCallBack);
        printf("SetCmdRpyCallback rtn is %d\n", rtn);
        rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 50);
        JointPos j(0, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        while (true)
        {
            robot.MoveJ(&j, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
            float vel = 0.0;
            float acc = 0.0;
            float cmdT = 0.016;
            float filterT = 0.0;
            float gain = 0.0;
            uint8_t flag = 0;
            float dt = 0.1;
            int cmdID = 0;
            int ret = robot.GetActualJointPosDegree(flag, &j);
            if (ret != 0)
            {
                printf("GetActualJointPosDegree errcode:%d\n", ret);
            }
            int comType = 1;
            int count = 300;
            rtn = robot.ServoMoveStart(comType);
            printf("ServoMoveStart rtn is %d\n", rtn);
            while (count)
            {
                rtn = robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                printf("ServoJ rtn is %d\n", rtn);
                j.jPos[0] += dt;
                j.jPos[1] += dt;
                j.jPos[2] += dt;
                j.jPos[3] += dt;
                j.jPos[4] += dt;
                j.jPos[5] += dt;
                epos.ePos[0] += dt;
                count -= 1;
                robot.Sleep(15);
            }
            robot.ServoMoveEnd(comType);
            printf("ServoMoveEnd rtn is %d\n", rtn);
            count = 300;
            robot.ServoMoveStart(comType);
            printf("ServoMoveStart rtn is %d\n", rtn);
            while (count)
            {
                robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                printf("ServoJ rtn is %d\n", rtn);
                j.jPos[0] -= dt;
                j.jPos[1] -= dt;
                j.jPos[2] -= dt;
                j.jPos[3] -= dt;
                j.jPos[4] -= dt;
                j.jPos[5] -= dt;
                epos.ePos[0] -= dt;
                count -= 1;
                robot.Sleep(15);
            }
            robot.ServoMoveEnd(comType);
            printf("ServoMoveEnd rtn is %d\n", rtn);
        }
        robot.Sleep(4000);
        robot.CloseRPC();
        return 0;
    }

Início do Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início do controle de torque articular
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoJTStart(int comType = 0);

Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Controle de torque articular
    * @param [in] torque Torque das juntas j1~j6, em Nm
    * @param [in] interval Período de instrução, em s, intervalo [0.001~0.008]
    * @param [in] checkFlag Estratégia de detecção 0-sem limitação; 1-limitação de potência; 2-limitação de velocidade; 3-limitação simultânea de potência e velocidade
    * @param [in] jPowerLimit Limite máximo de potência da junta (W)
    * @param [in] jVelLimit Velocidade máxima da junta (°/s)
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoJT(float torque[], double interval, int checkFlag, double jPowerLimit[6], double jVelLimit[6], int comType = 0);

Fim do Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Fim do controle de torque articular
    * @param [in] comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoJTEnd(int comType = 0);

Exemplo de Código de Controle de Torque Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    int TestServoJT(void)
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
        robot.DragTeachSwitch(1);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);
        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001);
            count = count - 1;
            robot.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
        robot.CloseRPC();
        return 0;
    }

Exemplo de Código de Controle de Torque Articular com Proteção contra Excesso de Velocidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int ServoJTWithSafety(FRRobot* robot)
    {
        robot->ResetAllError();
        robot->Sleep(500);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot->GetJointTorques(1, torques);
        robot->ServoJTStart();
        ROBOT_STATE_PKG pkg = {};
        robot->DragTeachSwitch(1);
        int checkFlag = 3;
        //double jPowerLimit[6] = {1, 1, 1, 1, 1, 1};
        double jPowerLimit[6] = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double jVelLimit[6] = { 181, 80, 80, 80, 80, 80 };
        int count = 800000;
        int error = 0;
        while (count > 0)
        {
            torques[2] = torques[2] + 0.01;
            error = robot->ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit);
            if (error != 0)
            {
                robot->ServoJTEnd();
            }
            printf("ServoJT rtn is %d\n", error);
            count = count - 1;
            robot->Sleep(1);
            robot->GetRobotRealTimeState(&pkg);
            printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
        }
        robot->DragTeachSwitch(0);
        error = robot->ServoJTEnd();
        return 0;
    }

Exemplo de Código de Controle de Torque Articular com comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void UDPFrameCallBack(int srcType, int count, int cmdID, int len, std::string content)
    {
        cout << "recv cmd: cmdID:  " << to_string(cmdID) << "  content is " << content << "  count is " << count << endl;

        return;
    }
    int TestServoJTUDP(void)
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetCmdRpyCallback(UDPFrameCallBack);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        robot.SetReConnectParam(true, 30000, 500);
        JointPos j(0, -90, 90, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        robot.MoveJ(&j, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);
        int comType = 1;
        int count = 100;
        int checkFlag = 3;
        double jPowerLimit[6] = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double jVelLimit[6] = { 80, 80, 80, 80, 80, 80 };
        rtn = robot.ServoJTStart(comType);
        printf("ServoJTStart rtn is %d\n", rtn);
        while (true)
        {
            torques[0] = 0.05;
            rtn = robot.ServoJT(torques, 0.001, checkFlag, jPowerLimit, jVelLimit, comType);
            printf("ServoJT rtn is %d\n", rtn);
            robot.Sleep(1);
            robot.GetRobotRealTimeState(&pkg);
            if (pkg.jt_cur_pos[0] > 30)
            {
                break;
            }
        }
        while (true)
        {
            torques[0] = -0.03;
            rtn = robot.ServoJT(torques, 0.001, checkFlag, jPowerLimit, jVelLimit, comType);
            printf("ServoJT rtn is %d\n", rtn);
            robot.Sleep(1);
            robot.GetRobotRealTimeState(&pkg);
            if (pkg.jt_cur_pos[0] < 0 || pkg.jt_cur_pos[1] < -110)
            {
                break;
            }
        }
        rtn = robot.ServoJTEnd(comType);
        printf("ServoJTEnd rtn is %d\n", rtn);
        robot.DragTeachSwitch(0);
        robot.Sleep(1000);
        robot.CloseRPC();
        return 0;
    }

Movimento no Modo Servo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento no modo servo no espaço cartesiano
    * @param [in] mode 0-movimento absoluto (sistema de coordenadas base), 1-movimento incremental (sistema de coordenadas base), 2-movimento incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana alvo ou incremento de pose
    * @param [in] exaxis Posição do eixo estendido
    * @param [in] pos_gain Coeficiente de escala do incremento de pose, ativo apenas em movimento incremental, intervalo [0~1]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param [in] vel Percentagem de velocidade, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param [in] cmdT Período de envio de instrução, em s, intervalo recomendado [0.001~0.016]
    * @param [in] filterT Tempo de filtro, em s, temporariamente não disponível, padrão 0
    * @param [in] gain Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0
    * @return Código de erro
    */
    errno_t ServoCart(int mode, DescPose *desc_pose, ExaxisPos exaxis, float pos_gain[6], float acc, float vel, float cmdT, float filterT, float gain);

Exemplo de Código de Movimento no Modo Servo no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoCart(void)
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
        DescPose desc_pos_dt = { 83.00800, 50.525000 , 29.246 , 179.629 , -7.138 , -166.975 };
        ExaxisPos exaxis = { 100.0, 0.0, 0.0, 0.0 };
        float pos_gain[6] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int mode = 0;
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.001;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 5000;
        robot.SetSpeed(20);
        while (count)
        {
            rtn = robot.ServoCart(mode, &desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            printf("ServoCart rtn is %d\n", rtn);
            count -= 1;
            desc_pos_dt.tran.x += 0.01;
            exaxis.ePos[0] += 0.01;
        }
        robot.CloseRPC();
        return 0;
    }

Início do Movimento Spline
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Início do movimento spline
    * @return Código de erro
    */
    errno_t SplineStart();

Movimento Spline no Espaço Articular (com cálculo automático de cinemática direta)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento spline no espaço articular (com cálculo automático de cinemática direta)
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @return Código de erro
    */
    errno_t SplinePTP(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl);

Movimento Spline PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento spline no espaço articular
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @return Código de erro
    */
    errno_t SplinePTP(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl);

Fim do Movimento Spline
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Fim do movimento spline
    * @return Código de erro
    */
    errno_t SplineEnd();

Exemplo de Código de Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSpline(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
      JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = -1.0;
      uint8_t flag = 0;
      robot.SetSpeed(20);
      int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.SplineStart();
      robot.SplinePTP(&j1, &desc_pos1, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j2, &desc_pos2, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j3, &desc_pos3, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j4, &desc_pos4, tool, user, vel, acc, ovl);
      robot.SplineEnd();
      err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.SplineStart();
      robot.SplinePTP(&j1, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j2, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j3, tool, user, vel, acc, ovl);
      robot.SplinePTP(&j4, tool, user, vel, acc, ovl);
      robot.SplineEnd();
      robot.CloseRPC();
      return 0;
    }

Início do Novo Movimento Spline
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início do novo movimento spline
    * @param [in] type 0-transição circular, 1-pontos fornecidos são pontos de caminho
    * @param [in] averageTime Tempo médio global de transição (ms) (10 ~ ), padrão 2000
    * @return Código de erro
    */
    errno_t NewSplineStart(int type, int averageTime=2000);

Ponto de Instrução do Novo Spline
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Ponto de instrução do novo spline
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] lastFlag Se é o último ponto, 0-não, 1-sim
    * @return Código de erro
    */
    errno_t NewSplinePoint(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

Ponto de Instrução do Novo Spline (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Ponto de instrução do novo spline (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [0~14]
    * @param [in] user Número da coordenada da peça, intervalo [0~14]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] lastFlag Se é o último ponto, 0-não, 1-sim
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t NewSplinePoint(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag, int config = -1);

Fim do Novo Movimento Spline
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Fim do novo movimento spline
    * @return Código de erro
    */
    errno_t NewSplineEnd();

Exemplo de Código do Novo Movimento Spline
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestNewSpline(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
      JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
      JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
      DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = -1.0;
      uint8_t flag = 0;
      robot.SetSpeed(20);
      int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.NewSplineStart(1, 2000);
      robot.NewSplinePoint(&j1, &desc_pos1, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j2, &desc_pos2, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j3, &desc_pos3, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j4, &desc_pos4, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&j5, &desc_pos5, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplineEnd();
      err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
      printf("movej errcode:%d\n", err1);
      robot.NewSplineStart(1, 2000);
      robot.NewSplinePoint(&desc_pos1, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos2, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos3, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos4, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplinePoint(&desc_pos5, tool, user, vel, acc, ovl, -1, 0);
      robot.NewSplineEnd();
      robot.CloseRPC();
      return 0;
    }

Parar Movimento
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Parar movimento
    * @return Código de erro
    */
    errno_t StopMotion();

Pausar Movimento
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Pausar movimento
    * @return Código de erro
    */
    errno_t PauseMotion();

Retomar Movimento
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Retomar movimento
    * @return Código de erro
    */
    errno_t ResumeMotion();

Exemplo de Código de Pausa, Retomada e Parada de Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestPause(void)
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
        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        uint8_t flag = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        rtn = robot.MoveJ(&j5, &desc_pos5, tool, user, vel, acc, ovl, &epos, 1, flag, &offset_pos);
        robot.Sleep(1000);
        robot.PauseMotion();
        robot.Sleep(1000);
        robot.ResumeMotion();
        robot.Sleep(1000);
        robot.StopMotion();
        robot.Sleep(1000);
        robot.CloseRPC();
        return 0;
    }

Início do Deslocamento Global de Pontos
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Início do deslocamento global de pontos
    * @param [in] flag 0-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @return Código de erro
    */
    errno_t PointsOffsetEnable(int flag, DescPose *offset_pos);

Fim do Deslocamento Global de Pontos
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Fim do deslocamento global de pontos
    * @return Código de erro
    */
    errno_t PointsOffsetDisable();

Exemplo de Código de Deslocamento de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestOffset(void)
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
        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1(0, 0, 50, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        uint8_t flag = 0;
        robot.SetSpeed(20);
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.Sleep(1000);
        robot.PointsOffsetEnable(0, &offset_pos1);
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.PointsOffsetDisable();
        robot.CloseRPC();
        return 0;
    }

Início da Captura com AO da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início da captura com AO da caixa de controle
    * @param [in] AONum Número da AO da caixa de controle
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000
    * @param [in] maxAOPercent Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    errno_t MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Parada da Captura com AO da Caixa de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Parada da captura com AO da caixa de controle
    * @return Código de erro
    */
    errno_t MoveAOStop();

Início da Captura com AO da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Início da captura com AO da extremidade
    * @param [in] AONum Número da AO da extremidade
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000
    * @param [in] maxAOPercent Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    errno_t MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Parada da Captura com AO da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Parada da captura com AO da extremidade
    * @return Código de erro
    */
    errno_t MoveToolAOStop();

Exemplo de Código de Captura com AO
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMoveAO(void)
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
        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1(0, 0, 50, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 20.0;
        float acc = 20.0;
        float ovl = 100.0;
        float blendT = -1.0;
        uint8_t flag = 0;
        robot.SetSpeed(20);
        robot.MoveAOStart(0, 100, 100, 20);
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveAOStop();
        robot.Sleep(1000);
        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        robot.MoveToolAOStop();
        robot.CloseRPC();
        return 0;
    }

Início do Filtro FIR para Movimento Ptp
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
    * @brief Início do filtro FIR para movimento Ptp
    * @param [in] maxAcc Valor extremo máximo de aceleração (deg/s2)
    * @param [in] maxJek Valor extremo de jerk uniforme das juntas (deg/s3)
    * @return Código de erro
    */
    errno_t PtpFIRPlanningStart(double maxAcc, double maxJek = 1000);

Desligar o Filtro FIR para Movimento Ptp
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
    * @brief Desligar o filtro FIR para movimento Ptp
    * @return Código de erro
    */
    errno_t PtpFIRPlanningEnd();

Início do Filtro FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
    * @brief Início do filtro FIR para movimento LIN e ARC
    * @param [in] maxAccLin Valor extremo de aceleração linear (mm/s2)
    * @param [in] maxAccDeg Valor extremo de aceleração angular (deg/s2)
    * @param [in] maxJerkLin Valor extremo de jerk linear (mm/s3)
    * @param [in] maxJerkDeg Valor extremo de jerk angular (deg/s3)
    * @return Código de erro
    */
    errno_t LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

Desligar o Filtro FIR para Movimento LIN e ARC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
    * @brief Desligar o filtro FIR para movimento LIN e ARC
    * @return Código de erro
    */
    errno_t LinArcFIRPlanningEnd();

Exemplo de Código de Filtro FIR
++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestFIR(void)
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
        JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos midjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos endjointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose middescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose enddescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);
        rtn = robot.PtpFIRPlanningStart(1000, 1000);
        cout << "PtpFIRPlanningStart rtn is " << rtn << endl;
        robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.PtpFIRPlanningEnd();
        cout << "PtpFIRPlanningEnd rtn is " << rtn << endl;
        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        cout << "LinArcFIRPlanningStart rtn is " << rtn << endl;
        robot.MoveL(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
        robot.MoveC(&midjointPos, &middescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, &endjointPos, &enddescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        cout << "LinArcFIRPlanningEnd rtn is " << rtn << endl;
        robot.CloseRPC();
        return 0;
    }

Ativar Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Ativar suavização de aceleração
    * @param [in] saveFlag Se salvar após desligamento
    * @return Código de erro
    */
    errno_t AccSmoothStart(bool saveFlag);

Desativar Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief Desativar suavização de aceleração
    * @param [in] saveFlag Se salvar após desligamento
    * @return Código de erro
    */
    errno_t AccSmoothEnd(bool saveFlag);

Exemplo de Código de Suavização de Aceleração
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAccSmooth(void)
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
        JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);
        rtn = robot.AccSmoothStart(0);
        cout << "AccSmoothStart rtn is " << rtn << endl;
        robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        rtn = robot.AccSmoothEnd(0);
        cout << "AccSmoothEnd rtn is " << rtn << endl;
        robot.CloseRPC();
        return 0;
    }

Ativar Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Ativar velocidade de postura especificada
    * @param [in] ratio Percentagem da velocidade de postura [0-300]
    * @return Código de erro
    */
    errno_t AngularSpeedStart(int ratio);

Desativar Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Desativar velocidade de postura especificada
    * @return Código de erro
    */
    errno_t AngularSpeedEnd();

Exemplo de Código de Velocidade de Postura Especificada do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
        JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);
        rtn = robot.AngularSpeedStart(50);
        cout << "AngularSpeedStart rtn is " << rtn << endl;
        robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        rtn = robot.AngularSpeedEnd();
        cout << "AngularSpeedEnd rtn is " << rtn << endl;
        robot.CloseRPC();
        return 0;
    }

Iniciar Proteção contra Pose Singular
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Iniciar proteção contra pose singular
    * @param [in] protectMode Modo de proteção contra singularidade, 0: modo articular; 1-modo cartesiano
    * @param [in] minShoulderPos Faixa de ajuste da singularidade do ombro (mm), padrão 100
    * @param [in] minElbowPos Faixa de ajuste da singularidade do cotovelo (mm), padrão 50
    * @param [in] minWristPos Faixa de ajuste da singularidade do pulso (°), padrão 10
    * @return Código de erro
    */
    errno_t SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

Parar Proteção contra Pose Singular
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Parar proteção contra pose singular
    * @return Código de erro
    */
    errno_t SingularAvoidEnd();

Exemplo de Código de Proteção contra Pose Singular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
        JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);
        rtn = robot.SingularAvoidStart(2, 10, 5, 5);
        cout << "SingularAvoidStart rtn is " << rtn << endl;
        robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        rtn = robot.SingularAvoidEnd();
        cout << "SingularAvoidEnd rtn is " << rtn << endl;
        robot.CloseRPC();
        return 0;
    }

Limpar Fila de Instruções de Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Limpar fila de instruções de movimento
    * @return Código de erro
    */
    errno_t MotionQueueClear();

Mover para Ponto Inicial da Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Mover para ponto inicial da linha de interseção
    * @param [in] mainPoint Poses cartesianas dos 6 pontos de ensino do tubo principal
    * @param [in] mainExaxisPos Posições dos eixos estendidos dos 6 pontos de ensino do tubo principal
    * @param [in] piecePoint Poses cartesianas dos 6 pontos de ensino do tubo auxiliar
    * @param [in] pieceExaxisPos Posições dos eixos estendidos dos 6 pontos de ensino do tubo de junção
    * @param [in] extAxisFlag Se habilita o eixo estendido; 0-não habilita; 1-habilita
    * @param [in] exaxisPos Posição do eixo estendido inicial
    * @param [in] tool Número do sistema de coordenadas da ferramenta
    * @param [in] wobj Número do sistema de coordenadas da peça
    * @param [in] vel Percentagem de velocidade
    * @param [in] acc Percentagem de aceleração
    * @param [in] ovl Fator de escala de velocidade
    * @param [in] oacc Fator de escala de aceleração
    * @param [in] moveType Tipo de movimento; 0-PTP; 1-LIN
    * @param [in] moveDirection Direção do movimento; 0-horário; 1-anti-horário
    * @param [in] offset Deslocamento
    * @return Código de erro
    */
    errno_t MoveToIntersectLineStart(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);

Movimento na Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento na linha de interseção
    * @param [in] mainPoint Poses cartesianas dos 6 pontos de ensino do tubo principal
    * @param [in] mainExaxisPos Posições dos eixos estendidos dos 6 pontos de ensino do tubo principal
    * @param [in] piecePoint Poses cartesianas dos 6 pontos de ensino do tubo auxiliar
    * @param [in] pieceExaxisPos Posições dos eixos estendidos dos 6 pontos de ensino do tubo de junção
    * @param [in] extAxisFlag Se habilita o eixo estendido; 0-não habilita; 1-habilita
    * @param [in] exaxisPos Posição do eixo estendido inicial
    * @param [in] tool Número do sistema de coordenadas da ferramenta
    * @param [in] wobj Número do sistema de coordenadas da peça
    * @param [in] vel Percentagem de velocidade
    * @param [in] acc Percentagem de aceleração
    * @param [in] ovl Fator de escala de velocidade
    * @param [in] oacc Fator de escala de aceleração
    * @param [in] moveDirection Direção do movimento; 0-horário; 1-anti-horário
    * @param [in] offset Deslocamento
    * @return Código de erro
    */
    errno_t MoveIntersectLine(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos[4], int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);

Exemplo de Código de Movimento na Linha de Interseção do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    void TestIntersectLineMove()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(3);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        DescPose mainPoint[6] = {};
        DescPose piecePoint[6] = {};
        ExaxisPos mainExaxisPos[6] = {};
        ExaxisPos pieceExaxisPos[6] = {};
        int extAxisFlag = 1;
        ExaxisPos exaxisPos[4] = {};
        DescPose offset = { 0.0, 2.0 ,30.0, -2.0, 0.0, 0.0 };
        mainPoint[0] = {490.004, -383.194, 402.735, -9.332, -1.528, 69.594};
        mainPoint[1] = {444.950, -407.117, 389.011, -5.546, -2.196, 65.279};
        mainPoint[2] = {445.168, -463.605, 355.759, -1.544, -10.886, 57.104};
        mainPoint[3] = {507.529, -485.385, 343.013, -0.786, -4.834, 61.799};
        mainPoint[4] = {554.390, -442.647, 367.701, -4.761, -10.181, 64.925};
        mainPoint[5] = {532.552, -394.003, 396.467, -13.732, -13.592, 67.411};
        mainExaxisPos[0] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[1] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[2] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[3] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[4] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[5] = { -29.996, 0.000, 0.000, 0.000 };
        piecePoint[0] = { 505.571, -192.408, 316.759, 38.098, 37.051, 139.447 };
        piecePoint[1] = {533.837, -201.558, 332.340, 34.644, 42.339, 137.748};
        piecePoint[2] = {530.386, -225.085, 373.808, 35.431, 45.111, 137.560};
        piecePoint[3] = {485.646, -229.195, 383.778, 33.870, 45.173, 137.064};
        piecePoint[4] = {460.551, -212.161, 354.256, 28.856, 45.602, 135.930};
        piecePoint[5] = {474.217, -197.124, 324.611, 42.469, 41.133, 148.167};
        pieceExaxisPos[0] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[1] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[2] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[3] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[4] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[5] = { -29.996, -0.000, 0.000, 0.000 };
        exaxisPos[0] = {-29.996, -0.000, 0.000, 0.000};
        exaxisPos[1] = {-44.994, 90.000, 0.000, 0.000};
        exaxisPos[2] = {-59.992, 0.002, 0.000, 0.000};
        exaxisPos[3] = {-44.994, -89.997, 0.000, 0.000};
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0;
        int moveType = 1;
        int moveDirection = 1;
        rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return;
    }

Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento estacionário no local
    * @return Código de erro
    */
    errno_t MoveStationary();

Exemplo de Código de Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLaserStationary(void)
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
        rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 0, 10, 100);
        printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        rtn = robot.MoveStationary();
        printf("MoveStationary rtn is %d\n", rtn);
        rtn = robot.LaserSensorRecord1(0, 10);
        printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(9999999);
        return 0;
    }

Início da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Início da oscilação em ponto fixo
    * @param [in] weaveNum Número da oscilação [0-7]
    * @param [in] mode 0-sistema de coordenadas da ferramenta; 1-ponto de referência
    * @param [in] refPoint Coordenadas cartesianas do ponto de referência [x, y, z, a, b, c]
    * @param [in] weaveTime Tempo de oscilação [s]
    * @return Código de erro
    */
    errno_t OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime);

Fim da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief Fim da oscilação em ponto fixo
    * @return Código de erro
    */
    errno_t OriginPointWeaveEnd();

Exemplo de Código SDK de Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestOriginPointWeave()
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
        JointPos j(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        DescPose refPoint = { 400.021,300.022,299.996,179.997,-0.003,-90.956 };
        robot.MoveJ(&j, 1, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
        robot.Sleep(2000);
        robot.MoveJ(&j, 1, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

Exemplo de Código de Oscilação em Ponto Fixo (incluindo sensor a laser e eixo estendido)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestOriginPointWeave()
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
        JointPos j(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos1(0, 0, 0, 0);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos2(5, 0.000, 0.000, 0.000);
        DescPose refPoint(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);
        robot.ExtDevLoadUDPDriver();
        rtn = robot.SetExAxisCmdDoneTime(5000.0);
        printf("SetExAxisCmdDoneTime rtn is %d\n", rtn);
        rtn = robot.ExtAxisServoOn(1, 1);
        printf("ExtAxisServoOn axis id 1 rtn is %d\n", rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        printf("ExtAxisServoOn axis id 2 rtn is %d\n", rtn);
        robot.Sleep(2000);
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        rtn = robot.LaserTrackingLaserOnOff(1, 0);
        printf("LaserTrackingLaserOnOff id 2 rtn is %d\n", rtn);
        robot.LaserTrackingTrackOnOff(1, 4);
        robot.Sleep(200);
        robot.OriginPointWeaveStart(0, 0, refPoint, 10);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);

        robot.Sleep(2000);

        robot.ExtAxisMove(epos1, 100, -1);
        robot.LaserTrackingTrackOnOff(1, 4);
        robot.OriginPointWeaveStart(0, 0, refPoint, 20);
        robot.ExtAxisMove(epos2, 100, -1);
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }