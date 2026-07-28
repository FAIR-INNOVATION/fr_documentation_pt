Movimento do Robô
========================

.. toctree::
    :maxdepth: 5


Movimento Jog
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento Jog
    * @param [in] refType 0-jog por junta, 2-jog no sistema de coordenadas base, 4-jog no sistema de coordenadas da ferramenta, 8-jog no sistema de coordenadas da peça
    * @param [in] nb 1-junta1 (ou eixo X), 2-junta2 (ou eixo Y), 3-junta3 (ou eixo Z), 4-junta4 (ou rotação em torno do eixo X), 5-junta5 (ou rotação em torno do eixo Y), 6-junta6 (ou rotação em torno do eixo Z)
    * @param [in] dir 0-direção negativa, 1-direção positiva
    * @param [in] vel Percentagem de velocidade, [0~100]
    * @param [in] acc Percentagem de aceleração, [0~100]
    * @param [in] max_dis Ângulo máximo por movimento jog, em [°] ou distância, em [mm]
    * @return Código de erro
    */
    int StartJOG(int refType, int nb, int dir, double vel, double acc, double max_dis);

Parada Desacelerada do Movimento Jog
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parada desacelerada do movimento jog
    * @param [in] stopType 1-parada de jog por junta, 3-parada de jog no sistema de coordenadas base, 5-parada de jog no sistema de coordenadas da ferramenta, 9-parada de jog no sistema de coordenadas da peça
    * @return Código de erro
    */
    int StopJOG(int stopType);

Parada Imediata do Movimento Jog
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parada imediata do movimento jog
    * @return Código de erro
    */
    int ImmStopJOG();

Exemplo de Código de Controle de Movimento Jog do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestJOG(Robot robot)
    {
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
        return 0;
    }

Movimento no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

Movimento no Espaço Articular (com cálculo automático de cinemática direta)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
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
    int MoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos)

Movimento Linear no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (sobrecarga 1 com blendMode)
    * @param joint_pos Posição articular alvo, em graus
    * @param desc_pos Pose cartesiana alvo
    * @param tool Número da coordenada da ferramenta, intervalo [1~15]
    * @param user Número da coordenada da peça, intervalo [1~15]
    * @param vel Percentagem de velocidade, intervalo [0~100]
    * @param acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    * @param blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param epos Posição do eixo estendido, em mm
    * @param search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param offset_pos Deslocamento de pose
    * @param oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    * @param velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @param overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, double oacc, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] user Número da coordenada da peça, intervalo [1~15]
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
    int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] user Número da coordenada da peça, intervalo [1~15]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param [in] speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (sobrecarga 1 com blendMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (sobrecarga 1 com blendMode)
    * @param [in] joint_pos Posição articular alvo, em graus
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] user Número da coordenada da peça, intervalo [1~15]
    * @param [in] vel Percentagem de velocidade, intervalo [0~100]
    * @param [in] acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param [in] epos Posição do eixo estendido, em mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param [in] speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (sobrecarga 2 sem necessidade de posição articular)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano (sobrecarga 2 sem necessidade de posição articular)
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] user Número da coordenada da peça, intervalo [1~15]
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
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão 0
    * @param [in] speedPercent Percentagem limite de redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    public int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Circular no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano
    * @param joint_pos_p Posição articular do ponto de passagem, em graus
    * @param desc_pos_p Pose cartesiana do ponto de passagem
    * @param ptool Número da coordenada da ferramenta, intervalo [1~15]
    * @param puser Número da coordenada da peça, intervalo [1~15]
    * @param pvel Percentagem de velocidade, intervalo [0~100]
    * @param pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param epos_p Posição do eixo estendido, em mm
    * @param poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param offset_pos_p Deslocamento de pose
    * @param joint_pos_t Posição articular do ponto alvo, em graus
    * @param desc_pos_t Pose cartesiana do ponto alvo
    * @param ttool Número da coordenada da ferramenta, intervalo [1~15]
    * @param tuser Número da coordenada da peça, intervalo [1~15]
    * @param tvel Percentagem de velocidade, intervalo [0~100]
    * @param tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param epos_t Posição do eixo estendido, em mm
    * @param toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param offset_pos_t Deslocamento de pose
    * @param ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    * @param blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    * @param velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, double oacc, int velAccParamMode)

Movimento Circular no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] puser Número da coordenada da peça, intervalo [1~15]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Deslocamento de pose
    * @param [in] desc_pos_t Pose cartesiana do ponto alvo
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] tuser Número da coordenada da peça, intervalo [1~15]
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
    int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config)

Movimento Circular no Espaço Cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
    * @param [in] joint_pos_p Posição articular do ponto de passagem, em graus
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] puser Número da coordenada da peça, intervalo [1~15]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Deslocamento de pose
    * @param [in] joint_pos_t Posição articular do ponto alvo, em graus
    * @param [in] desc_pos_t Pose cartesiana do ponto alvo
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] tuser Número da coordenada da peça, intervalo [1~15]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t Deslocamento de pose
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int velAccParamMode)

Movimento Circular no Espaço Cartesiano (sobrecarga 1 sem necessidade de posição articular)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento circular no espaço cartesiano (sobrecarga 1 sem necessidade de posição articular)
    * @param [in] desc_pos_p Pose cartesiana do ponto de passagem
    * @param [in] ptool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] puser Número da coordenada da peça, intervalo [1~15]
    * @param [in] pvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo estendido, em mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Deslocamento de pose
    * @param [in] desc_pos_t Pose cartesiana do ponto alvo
    * @param [in] ttool Número da coordenada da ferramenta, intervalo [1~15]
    * @param [in] tuser Número da coordenada da peça, intervalo [1~15]
    * @param [in] tvel Percentagem de velocidade, intervalo [0~100]
    * @param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo estendido, em mm
    * @param [in] toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t Deslocamento de pose
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o final (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), em mm
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-resolver com base na posição articular atual, [0~7]-resolver com base em uma configuração específica do espaço articular
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    public int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config, int velAccParamMode)

Movimento Circular Completo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    *@brief Movimento circular completo no espaço cartesiano
    *@param joint_pos_p Posição articular do ponto de passagem 1, em graus
    *@param desc_pos_p Pose cartesiana do ponto de passagem 1
    *@param ptool Número da coordenada da ferramenta, intervalo [1~15]
    *@param puser Número da coordenada da peça, intervalo [1~15]
    *@param pvel Percentagem de velocidade, intervalo [0~100]
    *@param pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    *@param epos_p Posição do eixo estendido, em mm
    *@param joint_pos_t Posição articular do ponto de passagem 2, em graus
    *@param desc_pos_t Pose cartesiana do ponto de passagem 2
    *@param ttool Número da coordenada da ferramenta, intervalo [1~15]
    *@param tuser Número da coordenada da peça, intervalo [1~15]
    *@param tvel Percentagem de velocidade, intervalo [0~100]
    *@param tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    *@param epos_t Posição do eixo estendido, em mm
    *@param ovl Fator de escala de velocidade [0~100]/velocidade física (mm/s)
    *@param offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    *@param offset_pos Deslocamento de pose
    *@param oacc Fator de escala de aceleração [0-100]/aceleração física (mm/s2)
    *@param blendR -1: bloqueante; 0~1000: raio de suavização
    *@param velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    *@return Código de erro
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

Movimento Circular Completo no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
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
    int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int config)

Movimento Circular Completo no Espaço Cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    *@brief Movimento circular completo no espaço cartesiano (com parâmetro de modo de parâmetro de velocidade/aceleração velAccParamMode)
    *@param [in] joint_pos_p Posição articular do ponto de passagem 1, em graus
    *@param [in] desc_pos_p Pose cartesiana do ponto de passagem 1
    *@param [in] ptool Número da coordenada da ferramenta, intervalo [1~15]
    *@param [in] puser Número da coordenada da peça, intervalo [1~15]
    *@param [in] pvel Percentagem de velocidade, intervalo [0~100]
    *@param [in] pacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    *@param [in] epos_p Posição do eixo estendido, em mm
    *@param [in] joint_pos_t Posição articular do ponto de passagem 2, em graus
    *@param [in] desc_pos_t Pose cartesiana do ponto de passagem 2
    *@param [in] ttool Número da coordenada da ferramenta, intervalo [1~15]
    *@param [in] tuser Número da coordenada da peça, intervalo [1~15]
    *@param [in] tvel Percentagem de velocidade, intervalo [0~100]
    *@param [in] tacc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível
    *@param [in] epos_t Posição do eixo estendido, em mm
    *@param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    *@param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    *@param [in] offset_pos Deslocamento de pose
    *@param [in] oacc Percentagem de aceleração
    *@param [in] blendR -1: bloqueante; 0~1000: raio de suavização
    *@param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    *@return Código de erro
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

Movimento Circular Completo no Espaço Cartesiano (sobrecarga 1 sem necessidade de posição articular)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento circular completo no espaço cartesiano (sobrecarga 1 sem necessidade de posição articular)
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
    * @param [in] velAccParamMode Modo de parâmetro de velocidade/aceleração; 0-percentagem; 1-velocidade física (mm/s) aceleração (mm/s2)
    * @return Código de erro
    */
    public int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int config, int velAccParamMode)

Movimento Ponto a Ponto no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int MoveCart(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendT, int config);

Exemplo de Código de Instruções Básicas de Movimento do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn=-1;
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4=new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4=new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode, 0, 10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode, 0, 10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

Movimento Helicoidal no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @return Código de erro
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param);

Movimento Helicoidal no Espaço Cartesiano (com cálculo automático de cinemática inversa)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
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
    int NewSpiral(DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param, int config)

Exemplo de Código de Movimento Helicoidal
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpiral(Robot robot)
    {
        int rtn=-1;
        JointPos j=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose offset_pos1=new DescPose(50, 0, 0, -30, 0, 0);
        DescPose offset_pos2=new DescPose(50, 0, 0, -5, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp=new SpiralParam(1, 5.0, 50.0, 10.0, 10.0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = 0.0;
        int flag = 2;

        rtn = robot.MoveJ(j, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
        System.out.println("movej errcode:" + rtn);

        rtn = robot.NewSpiral(desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp, -1);
        System.out.println("newspiral errcode:" + rtn);

        return 0;
    }

Início do Movimento Servo
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do movimento servo, para uso com instruções ServoJ e ServoCart
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoMoveStart(int comType)

Fim do Movimento Servo
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do movimento servo, para uso com instruções ServoJ e ServoCart
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoMoveEnd(int comType)

Movimento no Modo Servo no Espaço Articular
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento no modo servo no espaço articular
    * @param joint_pos Posição articular alvo, em graus
    * @param axisPos Posição do eixo externo, em mm
    * @param acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param vel Percentagem de velocidade, intervalo [0~100], temporariamente não disponível, padrão 0
    * @param cmdT Período de envio de instrução, em s, intervalo recomendado [0.001~0.0016]
    * @param filterT Tempo de filtro, em s, temporariamente não disponível, padrão 0
    * @param gain Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0
    * @param id ID da instrução ServoJ, padrão 0
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJ(JointPos joint_pos, ExaxisPos axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id, int comType)

Exemplo de Código SDK para ServoJ, ServoMoveStart, ServoMoveEnd com comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoJ(Robot robot)
    {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Received UDP reply from robot]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("content (content): " + content);
            return 0;
        });
        int rtn = -1;

        JointPos j = new JointPos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        double vel = 0.0;
        double acc = 0.0;
        double cmdT = 0.016;
        double filterT = 0.0;
        double gain = 0.0;
        int flag = 0;
        int count = 300;
        double dt = 0.1;
        int cmdID = 0;
        int comType = 1;
        int ret = robot.GetActualJointPosDegree(j);
        if (ret == 0)
        {
            robot.ServoMoveStart(comType);
            count = 300;
            while (count > 0)
            {
                robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                j.J1 += dt;
                j.J2 += dt;
                j.J4 += dt;
                j.J5 += dt;
                j.J6 += dt;
                epos.axis1 += dt;
                count -= 1;
                robot.Sleep(10);
            }
            robot.ServoMoveEnd(comType);

            robot.Sleep(1000);
            robot.ServoMoveStart(comType);
            count = 300;
            while (count > 0)
            {
                robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, comType);
                j.J1 -= dt;
                j.J2 -= dt;
                j.J4 -= dt;
                j.J5 -= dt;
                j.J6 -= dt;
                epos.axis1 -= dt;
                count -= 1;
                robot.Sleep(10);
            }
            robot.ServoMoveEnd(comType);
        }
        else
        {
            System.out.println("GetActualJointPosDegree errcode:" + ret);
        }
    }

Programa de Exemplo de Movimento no Modo Servo no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestServoJ()
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 20, 500); // Define parâmetros de reconexão
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn == 0)
        {
            System.out.println("Conexão RPC bem-sucedida");
        }
        else
        {
            System.out.println("Falha na conexão RPC");
            return;
        }
        JointPos j5 = new JointPos();
        ExaxisPos ePos = new ExaxisPos();
        int ret = robot.GetActualJointPosDegree(j5);
        if (ret == 0)
        {
            int count = 200;
            while (count > 0)
            {
                robot.ServoJ(j5, ePos, 100, 100, 0.008, 0, 0);
                j5.J1 += 0.2; // Aumenta a posição da junta 1
                count -= 1;
                robot.WaitMs((int) (8));
            }
        }
    }

Início do Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do controle de torque articular
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJTStart(int comType)

Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Controle de torque articular
    * @param torque Torque das juntas j1~j6, em Nm
    * @param interval Período de instrução, em s, intervalo [0.001~0.008]
    * @param checkFlag Estratégia de detecção 0-sem limitação; 1-limitação de potência; 2-limitação de velocidade; 3-limitação simultânea de potência e velocidade
    * @param jPowerLimit Limite máximo de potência da junta (W)
    * @param jVelLimit Velocidade máxima da junta (°/s)
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJT(double[] torque, double interval, int checkFlag, double[] jPowerLimit, double[] jVelLimit, int comType)

Fim do Controle de Torque Articular
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do controle de torque articular
    * @param comType Tipo de envio de instrução; 0-xmlrpc; 1-UDP (porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJTEnd(int comType)

Programa de Exemplo de Movimento no Modo Servo no Espaço Articular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoJT(Robot robot)
    {

        robot.DragTeachSwitch(1);
        List<Number> joint_toq = new ArrayList<>();
        joint_toq = robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); // # início do ServoJT
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

Exemplo de Código SDK para ServoJT, ServoJTStart, ServoJTEnd com comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void ServoJTWithSafety(Robot robot)
    {
        robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Received UDP reply from robot]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("content: " + content);
            return 0;
        });
        while (true) {
            robot.ResetAllError();
            robot.Sleep(500);
            List<Number> torques;
            torques = robot.GetJointTorques(1);
            robot.ServoJTStart(1); // # início do ServoJT
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);
            int checkFlag = 3; // -1,3
            double[] jPowerLimit = {10.0, 10.0, 10.0, 10.0, 10.0, 10.0};
            double[] jVelLimit = {50, 50, 50, 50, 50, 50}; // 180.1,-1
            int count = 800000;
            int error = 0;
            int comType = 1;

            double[] tor = new double[]{(double) torques.get(1), (double) torques.get(2), (double) torques.get(3), (double) torques.get(4), (double) torques.get(5), (double) torques.get(6)};

            while (true) {
                tor[0] = 0.08; // # aumenta 0.01 Nm no eixo 1 a cada vez, realiza 100 movimentos
                error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit, comType); // # movimento no modo servo no espaço articular
                System.out.printf("ServoJT rtn is %d\n", error);
                count = count - 1;
                robot.Sleep(1);
                pkg = robot.GetRobotRealTimeState();
                System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
                if (pkg.jt_cur_pos[0] > 30)
                    break;
            }

            tor = new double[]{(double) torques.get(1), (double) torques.get(2), (double) torques.get(3), (double) torques.get(4), (double) torques.get(5), (double) torques.get(6)};
            while (true) {
                tor[0] = -0.08; // # aumenta 0.01 Nm no eixo 1 a cada vez, realiza 100 movimentos
                error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit, 1); // # movimento no modo servo no espaço articular
                System.out.printf("ServoJT rtn is %d\n", error);
                count = count - 1;
                robot.Sleep(1);
                pkg = robot.GetRobotRealTimeState();
                System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
                if (pkg.jt_cur_pos[0] < 0)
                    break;
            }

            robot.DragTeachSwitch(0);

            error = robot.ServoJTEnd(1); // # fim do movimento servo
        }
    }

Exemplo de Código de Controle de Torque Articular com Proteção contra Excesso de Velocidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void ServoJTWithSafety(Robot robot)
    {
        robot.ResetAllError();
        robot.Sleep(500);
        List<Number> torques;
        torques = robot.GetJointTorques(1);
        robot.ServoJTStart(); // # início do ServoJT
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.DragTeachSwitch(1);
        int checkFlag = 3; // -1,3
        //double[] jPowerLimit = {1.0,1.0,1.0,1.0,1.0,1.0};//5001
        double[] jPowerLimit = {10.0, 10.0, 10.0, 10.0, 10.0, 10.0};
        double[] jVelLimit = {50, 50, 50, 50, 50, 50}; // 180.1,-1
        int count = 800000;
        int error = 0;
        double[] tor = new double[]{(double) torques.get(1), (double) torques.get(2), (double) torques.get(3), (double) torques.get(4), (double) torques.get(5), (double) torques.get(6)};
        while (count > 0)
        {
            tor[2] = tor[2] + 0.01; // # aumenta 0.01 Nm no eixo 1 a cada vez, realiza 100 movimentos
            error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit); // # movimento no modo servo no espaço articular
            System.out.printf("ServoJT rtn is %d\n", error);
            count = count - 1;
            robot.Sleep(1);
            pkg = robot.GetRobotRealTimeState();
            System.out.printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
        }
        robot.DragTeachSwitch(0);
        error = robot.ServoJTEnd(); // # fim do movimento servo
    }

Movimento no Modo Servo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief Movimento no modo servo no espaço cartesiano
    *@param mode 0-movimento absoluto (sistema de coordenadas base), 1-movimento incremental (sistema de coordenadas base), 2-movimento incremental (sistema de coordenadas da ferramenta)
    *@param desc_pose Pose cartesiana alvo ou incremento de pose
    *@param exaxis Posição do eixo estendido
    *@param pos_gain Coeficiente de escala do incremento de pose, ativo apenas em movimento incremental, intervalo [0~1]
    *@param acc Percentagem de aceleração, intervalo [0~100], temporariamente não disponível, padrão 0
    *@param vel Percentagem de velocidade, intervalo [0~100], temporariamente não disponível, padrão 0
    *@param cmdT Período de envio de instrução, em s, intervalo recomendado [0.001~0.016]
    *@param filterT Tempo de filtro, em s, temporariamente não disponível, padrão 0
    *@param gain Amplificador proporcional da posição alvo, temporariamente não disponível, padrão 0
    *@return Código de erro
    */
    public int ServoCart(int mode, DescPose desc_pose, ExaxisPos exaxis, double[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain)

Exemplo de Código de Movimento no Modo Servo no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestServoCart1(Robot robot)
    {
        DescPose desc_pos_dt = new DescPose(83.00800, 50.525000, 29.246, 179.629, -7.138, -166.975);
        ExaxisPos exaxis = new ExaxisPos(100.0, 0.0, 0.0, 0.0);
        double[] pos_gain = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        int mode = 0;
        double vel = 0.0;
        double acc = 0.0;
        double cmdT = 0.001;
        double filterT = 0.0;
        double gain = 0.0;
        int flag = 0;
        int count = 5000;
        robot.SetSpeed(20);
        while (count > 0)
        {
            int rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            System.out.printf("ServoCart rtn is %d\n", rtn);
            count -= 1;
            desc_pos_dt.tran.x += 0.01;
            exaxis.axis1 += 0.01;
        }
        robot.CloseRPC();
    }

Início do Movimento Spline
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do movimento spline
    * @return Código de erro
    */
    int SplineStart();

Movimento PTP Articular
+++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl);

Movimento Spline no Espaço Articular (com cálculo automático de cinemática direta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
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
    int SplinePTP(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl)

Fim do Movimento Spline
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do movimento spline
    * @return Código de erro
    */
    int SplineEnd();

Exemplo de Código de Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpline(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:" + err1);
        robot.SplineStart();
        robot.SplinePTP(j1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
        return 0;
    }

Início do Novo Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do novo movimento spline
    * @param [in] type 0-transição circular, 1-pontos fornecidos são pontos de caminho
    * @param [in] averageTime Tempo médio global de transição (ms) (10 ~ ), padrão 2000
    * @return Código de erro
    */
    int NewSplineStart(int type, int averageTime);

Ponto de Instrução do Novo Spline
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Adiciona ponto de instrução de movimento spline
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
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag);

Ponto de Instrução do Novo Spline (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
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
    int NewSplinePoint(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag, int config)

Fim do Novo Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do novo movimento spline
    * @return Código de erro
    */
    int NewSplineEnd();

Exemplo de Código do Novo Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestNewSpline(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:" + err1);
        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(desc_pos1, tool, user, vel, acc, ovl, -1, 0, -1);
        robot.NewSplinePoint(desc_pos2, tool, user, vel, acc, ovl, -1, 0, -1);
        robot.NewSplinePoint(desc_pos3, tool, user, vel, acc, ovl, -1, 0, -1);
        robot.NewSplinePoint(desc_pos4, tool, user, vel, acc, ovl, -1, 0, -1);
        robot.NewSplinePoint(desc_pos5, tool, user, vel, acc, ovl, -1, 0, -1);
        robot.NewSplineEnd();
        return 0;
    }

Parar Movimento
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parar movimento
    * @return Código de erro
    */
    int StopMotion();

Pausar Movimento
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Pausar movimento
    * @return Código de erro
    */
    int PauseMotion();

Retomar Movimento
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Retomar movimento
    * @return Código de erro
    */
    int ResumeMotion();

Exemplo de Código de Pausa, Retomada e Parada de Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPause(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);
        int rtn = -1;
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        robot.Sleep(1000);
        robot.PauseMotion();

        robot.Sleep(1000);
        robot.ResumeMotion();

        robot.Sleep(1000);
        robot.StopMotion();

        robot.Sleep(1000);

        return 0;
    }

Início do Deslocamento Global de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do deslocamento global de pontos
    * @param [in] flag 0-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Deslocamento de pose
    * @return Código de erro
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos);

Fim do Deslocamento Global de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do deslocamento global de pontos
    * @return Código de erro
    */
    int PointsOffsetDisable();

Exemplo de Código de Deslocamento de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOffset(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1 = new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.Sleep(1000);
        robot.PointsOffsetEnable(0, offset_pos1);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.PointsOffsetDisable();

        return 0;
    }

Início da Captura com AO da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da captura com AO da caixa de controle
    * @param [in] AONum Número da AO da caixa de controle
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000
    * @param [in] maxAOPercent Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Parada da Captura com AO da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parada da captura com AO da caixa de controle
    * @return Código de erro
    */
    int MoveAOStop();

Início da Captura com AO da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da captura com AO da extremidade
    * @param [in] AONum Número da AO da extremidade
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000 mm/s], padrão 1000
    * @param [in] maxAOPercent Percentagem de AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Valor de compensação da zona morta em percentagem de AO, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Parada da Captura com AO da Extremidade
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parada da captura com AO da extremidade
    * @return Código de erro
    */
    int MoveToolAOStop();

Exemplo de Código de Captura com AO
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMoveAO(Robot robot)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1 = new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 20.0;
        double acc = 20.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.Sleep(1000);

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();

        return 0;
    }

Início do Filtro FIR para Movimento Ptp
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief Início do filtro FIR para movimento Ptp
    * @param [in] maxAcc Valor extremo máximo de aceleração (deg/s2)
    * @param [in] maxJek Valor extremo de jerk uniforme das juntas (deg/s3)
    * @return Código de erro
    */
    int PtpFIRPlanningStart(double maxAcc, double maxJek);

Desligar o Filtro FIR para Movimento Ptp
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Desligar o filtro FIR para movimento Ptp
    * @return Código de erro
    */
    int PtpFIRPlanningEnd();

Início do Filtro FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do filtro FIR para movimento LIN e ARC
    * @param [in] maxAccLin Valor extremo de aceleração linear (mm/s2)
    * @param [in] maxAccDeg Valor extremo de aceleração angular (deg/s2)
    * @param [in] maxJerkLin Valor extremo de jerk linear (mm/s3)
    * @param [in] maxJerkDeg Valor extremo de jerk angular (deg/s3)
    * @return Código de erro
    */
    int LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

Desligar o Filtro FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Desligar o filtro FIR para movimento LIN e ARC
    * @return Código de erro
    */
    int LinArcFIRPlanningEnd();

Exemplo de Código de Filtro FIR
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFIR(Robot robot)
    {
        JointPos startjointPos = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos midjointPos = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos endjointPos = new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);

        DescPose startdescPose = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose middescPose = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose enddescPose = new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.PtpFIRPlanningStart(1000, 1000);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.PtpFIRPlanningEnd();

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        robot.MoveL(startjointPos, startdescPose, 0, 0, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveC(midjointPos, middescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        return 0;
    }

Ativar Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief Ativar suavização de aceleração
     * @param [in] saveFlag Se salvar após desligamento
     * @return Código de erro
     */
    public int AccSmoothStart(boolean saveFlag)

Desativar Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief Desativar suavização de aceleração
     * @param [in] saveFlag Se salvar após desligamento
     * @return Código de erro
     */
    public int AccSmoothEnd(boolean saveFlag)

Exemplo de Código de Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAccSmooth(Robot robot)
    {
        JointPos startjointPos = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AccSmoothStart(false);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AccSmoothEnd(false);

        robot.CloseRPC();
        return 0;
    }

Ativar Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Ativar velocidade de postura especificada
     * @param [in] ratio Percentagem da velocidade de postura [0-300]
     * @return Código de erro
     */
    int AngularSpeedStart(int ratio)

Desativar Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief Desativar velocidade de postura especificada
     * @return Código de erro
     */
    int AngularSpeedEnd();

Exemplo de Código de Velocidade de Postura Especificada do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

Iniciar Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Iniciar proteção contra pose singular
    * @param [in] protectMode Modo de proteção contra singularidade, 0: modo articular; 1-modo cartesiano
    * @param [in] minShoulderPos Faixa de ajuste da singularidade do ombro (mm), padrão 100
    * @param [in] minElbowPos Faixa de ajuste da singularidade do cotovelo (mm), padrão 50
    * @param [in] minWristPos Faixa de ajuste da singularidade do pulso (°), padrão 10
    * @return Código de erro
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

Parar Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Parar proteção contra pose singular
    * @return Código de erro
    */
    int SingularAvoidEnd();

Aguardar Conclusão do Movimento Vazio em Posição
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:    

    /**
    * @brief Aguardar a conclusão do movimento vazio em posição
    * @return Código de erro
    */
    public int WaitStationaryMotionDone()    

Exemplo de Código de Proteção contra Pose Singular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

Limpar Fila de Instruções de Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Limpar fila de instruções de movimento
    * @return Código de erro
    */
    public int MotionQueueClear()

Mover para Ponto Inicial da Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveToIntersectLineStart(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);

Movimento na Linha de Interseção
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveIntersectLine(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos[] exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);

Exemplo de Código de Movimento na Linha de Interseção do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestIntersectLineMove(Robot robot)
    {
        DescPose[] mainPoint = new DescPose[6];
        DescPose[] piecePoint = new DescPose[6];
        ExaxisPos[] mainExaxisPos = new ExaxisPos[6];
        ExaxisPos[] pieceExaxisPos = new ExaxisPos[6];
        int extAxisFlag = 1;
        ExaxisPos[] exaxisPos = new ExaxisPos[4];
        DescPose offset = new DescPose(0.0, 2.0, 30.0, -2.0, 0.0, 0.0);
        mainPoint[0] = new DescPose(490.004, -383.194, 402.735, -9.332, -1.528, 69.594);
        mainPoint[1] = new DescPose(444.950, -407.117, 389.011, -5.546, -2.196, 65.279);
        mainPoint[2] = new DescPose(445.168, -463.605, 355.759, -1.544, -10.886, 57.104);
        mainPoint[3] = new DescPose(507.529, -485.385, 343.013, -0.786, -4.834, 61.799);
        mainPoint[4] = new DescPose(554.390, -442.647, 367.701, -4.761, -10.181, 64.925);
        mainPoint[5] = new DescPose(532.552, -394.003, 396.467, -13.732, -13.592, 67.411);
        mainExaxisPos[0] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        mainExaxisPos[1] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        mainExaxisPos[2] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        mainExaxisPos[3] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        mainExaxisPos[4] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        mainExaxisPos[5] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000);
        piecePoint[0] = new DescPose(505.571, -192.408, 316.759, 38.098, 37.051, 139.447);
        piecePoint[1] = new DescPose(533.837, -201.558, 332.340, 34.644, 42.339, 137.748);
        piecePoint[2] = new DescPose(530.386, -225.085, 373.808, 35.431, 45.111, 137.560);
        piecePoint[3] = new DescPose(485.646, -229.195, 383.778, 33.870, 45.173, 137.064);
        piecePoint[4] = new DescPose(460.551, -212.161, 354.256, 28.856, 45.602, 135.930);
        piecePoint[5] = new DescPose(474.217, -197.124, 324.611, 42.469, 41.133, 148.167);
        pieceExaxisPos[0] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[1] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[2] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[3] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[4] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[5] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        exaxisPos[0] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        exaxisPos[1] = new ExaxisPos(-44.994, 90.000, 0.000, 0.000);
        exaxisPos[2] = new ExaxisPos(-59.992, 0.002, 0.000, 0.000);
        exaxisPos[3] = new ExaxisPos(-44.994, -89.997, 0.000, 0.000);
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0;
        int moveType = 1;
        int moveDirection = 1;
        int rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        System.out.printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        System.out.printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return;
    }

Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Movimento estacionário no local
    * @return Código de erro
    */
    public int MoveStationary()

Exemplo de Código de Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void test_RecordandReplay(Robot robot)
    {
        int rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 1, 10, 100);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        rtn = robot.MoveStationary();
        System.out.printf("MoveStationary rtn is %d\n", rtn);
        rtn = robot.LaserSensorRecord1(0, 10);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }

Início da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início da oscilação em ponto fixo
    * @param [in] weaveNum Número da oscilação [0-7]
    * @param [in] mode 0-sistema de coordenadas da ferramenta; 1-ponto de referência
    * @param [in] refPoint Coordenadas cartesianas do ponto de referência [x, y, z, a, b, c]
    * @param [in] weaveTime Tempo de oscilação [s]
    * @return Código de erro
    */
    public int OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime)

Fim da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim da oscilação em ponto fixo
    * @return Código de erro
    */
    public int OriginPointWeaveEnd();

Exemplo de Código SDK de Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOriginPointWeave(Robot robot) {
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);
        robot.MoveJ(j, 1, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);

        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();

        robot.Sleep(2000);

        robot.MoveJ(j, 1, 0, 100, 100, 100.0, epos, -1.0, 0, offset_pos);
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();

        robot.Sleep(1000);
        return 0;
    }

Exemplo de Código SDK de Oscilação em Ponto Fixo (incluindo laser e eixo estendido)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOriginPointWeave(Robot robot) {
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos1 = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos2 = new ExaxisPos(5, 0, 0, 0);
        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);

        int rtn = 0;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);

        // Carregar driver UDP
        robot.ExtDevLoadUDPDriver();

        // Definir tempo de conclusão do comando do eixo externo
        rtn = robot.SetExAxisCmdDoneTime(5000.0);
        System.out.println("SetExAxisCmdDoneTime rtn is " + rtn);
        // Habilitar eixos externos 1 e 2
        rtn = robot.ExtAxisServoOn(1, 1);
        System.out.println("ExtAxisServoOn axis id 1 rtn is " + rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        System.out.println("ExtAxisServoOn axis id 2 rtn is " + rtn);
        robot.Sleep(2000);

        // Definir retorno à origem do eixo externo
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.LaserTrackingLaserOnOff(1, 0);

        // 1---sem eixo estendido
        robot.LaserTrackingTrackOnOff(1, 4);
        robot.Sleep(200);
        // Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 10);
        robot.MoveStationary();   // Executar movimento fixo
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);

        robot.Sleep(2000); // Aguardar 2 segundos

        // 2----com eixo estendido
        robot.ExtAxisMove(epos1, 100, -1);
        robot.LaserTrackingTrackOnOff(1, 4);
        // Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 20);
        robot.ExtAxisMove(epos2, 100, -1);
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);

        robot.Sleep(1000);
        return 0;
    }

Movimento em Modo Servo de Velocidade no Espaço das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  Movimento em modo servo de velocidade no espaço das juntas
    * @param   joint_vel  6 velocidades alvo das juntas, unidade deg/s
    * @param   exis_vel  4 velocidades dos eixos externos, unidade deg/s
    * @param   acc  Percentual de aceleração, intervalo [0~100], ainda não aberto, padrão 0
    * @param   vel  Percentual de velocidade, intervalo [0~100], ainda não aberto, padrão 0
    * @param   cmdT  Período do ciclo de comando, unidade s, intervalo recomendado [0.001~0.0016]
    * @param   filterT Tempo de filtro, unidade s, ainda não aberto, padrão 0
    * @param   gain  Ganho proporcional para posição alvo, ainda não aberto, padrão 0
    * @param   id  ID do comando servoJ, padrão 0
    * @param   comType Tipo de comando; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return  Código de erro
    */
    public int ServoJV(double[] joint_vel, double[] exis_vel, double acc, double vel, double cmdT, double filterT, double gain, int id, int comType)

Exemplo de Código de Movimento em Modo Servo de Velocidade no Espaço das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int ServoJVtest(Robot robot)
    {
        double[] joint_vel = new double[] { 10, 0, 0, 0, 0, 0 };
        double[] exis_vel = new double[] { 0, 0, 0, 0 };
        double acc = 0.0;
        double vel = 0.0;
        double cmdT = 0.008;
        double filterT = 0.0;
        double gain = 0.0;
        int cnt = 0;
        while (cnt < 200)
        {
            int error = robot.ServoJV(joint_vel, exis_vel, acc, vel, cmdT, filterT, gain);
            System.out.println("MAIN ServoJV rtn is " + error);
    //            robot.Sleep(10);
            cnt++;
        }

        return 0;
    }

Início do Controle MIT das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Início do controle MIT das juntas
    * @param  comType Tipo de comando; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    errno_t ServoMITStart(int comType = 0);

Fim do Controle MIT das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Fim do controle MIT das juntas
    * @param  comType Tipo de comando; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoMITEnd(int comType);

Controle MIT das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief Controle MIT das juntas
    * @param  posGain Ganhos de posição das juntas j1~j6
    * @param  desPos Posições desejadas das juntas j1~j6, unidade: deg
    * @param  velGain Ganhos de velocidade das juntas j1~j6
    * @param  desVel Velocidades desejadas das juntas j1~j6, unidade: deg/s
    * @param  torque_ff Torques feedforward j1~j6, unidade: Nm
    * @param  interval Período do ciclo de comando, unidade s, intervalo [0.001~0.008]
    * @param  comType Tipo de comando; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoMIT(double[] posGain, double[] desPos, double[] velGain, double[] desVel, double[] torque_ff, double interval, int comType)

Exemplo de Código de Controle MIT das Juntas do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int ServoMITtest(Robot robot)
    {
            robot.udpCmdClient.SetUDPCmdRpyCallback((srcType, count, cmdID, dataLen, content) -> {
            System.out.println("\n[Received UDP reply from robot]");
            System.out.println("srcType: " + srcType);
            System.out.println("count: " + count);
            System.out.println("cmdID: " + cmdID);
            System.out.println("dataLen: " + dataLen);
            System.out.println("content: " + content);
            return 0;
        });
        while (true)
        {
            robot.ResetAllError();
            robot.Sleep(500);

            double[] posGain = new double[] { 0, 0, 0, 0, 0, 0 };
            double[] desPos = new double[] { 0, 0, 0, 0, 0, 0 };
            double[] velGain = new double[] { 0, 0, 0, 0, 0, 0 };
            double[] desVel = new double[] { 0, 0, 0, 0, 0, 0 };

            List<Number> joint_toq=new ArrayList<>();
            joint_toq=robot.GetJointTorques(1);
            double[] torques=new double[]{(double)joint_toq.get(1),(double)joint_toq.get(2),(double)joint_toq.get(3),(double)joint_toq.get(4),(double)joint_toq.get(5),(double)joint_toq.get(6)};
            System.out.println("111111");

            robot.ServoMITStart(0);
            System.out.println("ServoMITStart");

            ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
            robot.DragTeachSwitch(1);
            System.out.println("DragTeachSwitch");

            double intev = 0.008;
            int error = 0;

            while (true)
            {
                torques[5] = 0.03;
                System.out.println("ServoMIT call");
                error = robot.ServoMIT(posGain, desPos, velGain, desVel, torques, intev, 0);

                System.out.println("ServoMIT111111 rtn is " + error);
                robot.Sleep(1);

                pkg = robot.GetRobotRealTimeState();
                System.out.println("pkg.jt_cur_pos[5]:" + pkg.jt_cur_pos[5]);
                if (pkg.jt_cur_pos[5] > 30)
                {
                    break;
                }
            }

            while (true)
            {
                torques[5] = -0.03;
                error = robot.ServoMIT(posGain, desPos, velGain, desVel, torques, intev, 0);

                System.out.println("ServoJT222222 rtn is " + error);
                robot.Sleep(1);

                pkg = robot.GetRobotRealTimeState();
                System.out.println("pkg.jt_cur_pos[5]:" + pkg.jt_cur_pos[5]);
                if (pkg.jt_cur_pos[5] < 0)
                {
                    break;
                }
            }

            robot.DragTeachSwitch(0);
            error = robot.ServoMITEnd(0);
        }
        // return 0;
    }

Início da Transformação dos Pontos do Sistema de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:    

    /**
    * @brief Início da transformação dos pontos do sistema de coordenadas da peça
    * @param workpieceID Número da peça [0-14]
    * @return Código de erro, 0 em caso de sucesso
    */
    public int WorkPieceTrsfStart(int workpieceID)

Fim da Transformação dos Pontos do Sistema de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:    

    /**
    * @brief Fim da transformação dos pontos do sistema de coordenadas da peça
    * @return Código de erro, 0 em caso de sucesso
    */
    public int WorkPieceTrsfEnd()

Exemplo de Código de Movimento de Transformação do Sistema de Coordenadas da Peça
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:    
    
    public static int TestWorkPieceTrsf(Robot robot) {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        JointPos j1 = new JointPos(-11.188, -64.165, -107.299, -76.706, 89.590, 92.983);
        DescPose desc1 = new DescPose(225.986, 190.694, 394.238, -6.230, -23.797, -98.972);
        JointPos j2 = new JointPos(-38.148, -97.408, -133.704, -30.999, 89.584, 92.986);
        DescPose desc2 = new DescPose(52.741, 262.917, 30.824, -5.696, -9.864, -126.092);
        JointPos j3 = new JointPos(-25.561, -123.131, -85.736, -94.911, 89.582, 93.006);
        DescPose desc3 = new DescPose(70.455, 88.410, 45.299, -4.101, 31.775, -113.199);
        JointPos j4 = new JointPos(-8.013, -125.881, -79.196, -84.440, 89.564, 93.005);
        DescPose desc4 = new DescPose(209.453, -73.895, 56.416, -4.727, 17.523, -95.906);
        JointPos j5 = new JointPos(-2.722, -94.518, -119.965, -54.518, 89.563, 93.005);
        DescPose desc5 = new DescPose(274.800, 81.106, 102.977, -5.467, -2.980, -90.711);
        JointPos j6 = new JointPos(-2.671, -56.234, -138.914, -25.099, 95.355, 92.967);
        DescPose desc6 = new DescPose(300.392, 177.281, 300.926, -1.909, -51.894, -89.703);
        JointPos j7 = new JointPos(-1.229, -121.184, -63.201, -122.331, 93.045, 93.019);
        DescPose desc7 = new DescPose(296.856, -31.294, 215.698, -0.589, 34.594, -88.954);

        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offset = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        int tool = 1;
        int workpiece = 1;
        double blend = 5.0;

        robot.MoveJ(j1, desc1, tool, workpiece, 100, 100, 100, exaxis, -1, 0, offset);
        robot.MoveJ(j2, desc2, tool, workpiece, 100, 100, 100, exaxis, blend, 0, offset);
        robot.MoveL(j3, desc3, tool, workpiece, 10, 100, 100, blend, 0, exaxis, 0, 1, offset,-1, 0,0,0);
        robot.MoveC(j4, desc4, tool, workpiece, 100, 100, exaxis, 0, offset, j5, desc5, tool, workpiece, 100, 100, exaxis, 0, offset, 10, blend,100, 0);
        robot.Circle(j6, desc6, tool, workpiece, 100, 100, exaxis, j7, desc7, tool, workpiece, 100, 100, exaxis, 10, 0, offset, 100.0, blend,0);

        int rtn = robot.WorkPieceTrsfStart(2);
        System.out.printf("WorkPieceTrsfStart rtn is %d\n", rtn);
        robot.MoveJ(j1, desc1, tool, workpiece, 100, 100, 100, exaxis, -1, 0, offset);
        robot.MoveJ(j2, desc2, tool, workpiece, 100, 100, 100, exaxis, blend, 0, offset);
        robot.MoveL(j3, desc3, tool, workpiece, 10, 100, 100, blend, 0, exaxis, 0, 1, offset,-1, 0,0,0);
        robot.MoveC(j4, desc4, tool, workpiece, 100, 100, exaxis, 0, offset, j5, desc5, tool, workpiece, 100, 100, exaxis, 0, offset, 10, blend,100, 0);
        robot.Circle(j6, desc6, tool, workpiece, 100, 100, exaxis, j7, desc7, tool, workpiece, 100, 100, exaxis, 10, 0, offset, 100.0, blend, 0);

        robot.WorkPieceTrsfEnd();
        System.out.printf("WorkPieceTrsfEnd rtn is %d\n", rtn);
        robot.Sleep(2000);
        return 0;
    }    