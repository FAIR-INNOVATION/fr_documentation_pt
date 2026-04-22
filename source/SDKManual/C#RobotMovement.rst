Movimento do Robô
===========================

.. toctree:: 
    :maxdepth: 5


Movimento JOG
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Movimento JOG
    * @param [in] refType Tipo de JOG: 0-JOG por junta, 2-JOG no sistema de coordenadas base, 4-JOG no sistema de coordenadas da ferramenta, 8-JOG no sistema de coordenadas da peça
    * @param [in] nb 1-junta 1 (ou eixo X), 2-junta 2 (ou eixo Y), 3-junta 3 (ou eixo Z), 4-junta 4 (ou rotação em torno de X), 5-junta 5 (ou rotação em torno de Y), 6-junta 6 (ou rotação em torno de Z)
    * @param [in] dir 0-direção negativa, 1-direção positiva
    * @param [in] vel Percentual de velocidade, [0~100]
    * @param [in] acc Percentual de aceleração, [0~100]
    * @param [in] max_dis Ângulo máximo para movimento único, em [°] ou distância, em [mm]
    * @return Código de erro
    */ 
    int StartJOG(byte refType, byte nb, byte dir, float vel, float acc, float max_dis);

Parada Desacelerada do Movimento JOG
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Parada desacelerada do movimento JOG
    * @param  [in]  ref  1-Parada do JOG por junta, 3-Parada do JOG no sistema de coordenadas base, 5-Parada do JOG no sistema de coordenadas da ferramenta, 9-Parada do JOG no sistema de coordenadas da peça
    * @return  Código de erro
    */
    int StopJOG(byte stopType);

Parada Imediata do Movimento JOG
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Parada imediata do movimento JOG
    * @return  Código de erro
    */
    int ImmStopJOG(); 

Exemplo de Código de Controle de Movimento JOG do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJOG_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        robot.SetSpeed(35);
        robot.StartJOG(0, 1, 0, 15, 20.0f, 30.0f);   // Movimento de junta única, StartJOG é não bloqueante. Outros comandos de movimento (incluindo StartJOG) recebidos durante o movimento serão descartados.
        Thread.Sleep(1000);
        robot.StopJOG(1);  // Parada desacelerada do movimento de junta única do robô
        //robot.ImmStopJOG();  // Parada imediata do movimento de junta única do robô
        robot.StartJOG(0, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(2, 1, 0, 15, 20.0f, 30.0f);   // JOG no sistema de coordenadas base
        Thread.Sleep(1000);
        robot.StopJOG(3);  // Parada desacelerada do movimento de junta única do robô
        //robot.ImmStopJOG();  // Parada imediata do movimento de junta única do robô
        robot.StartJOG(2, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(4, 1, 0, 15, 20.0f, 30.0f);   // JOG no sistema de coordenadas da ferramenta
        Thread.Sleep(1000);
        robot.StopJOG(5);  // Parada desacelerada do movimento de junta única do robô
        //robot.ImmStopJOG();  // Parada imediata do movimento de junta única do robô
        robot.StartJOG(4, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(8, 1, 0, 15, 20.0f, 30.0f);   // JOG no sistema de coordenadas da peça
        Thread.Sleep(1000);
        robot.StopJOG(9);  // Parada desacelerada do movimento de junta única do robô
        //robot.ImmStopJOG();  // Parada imediata do movimento de junta única do robô
        robot.StartJOG(8, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
    }

Movimento no Espaço das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento no espaço das juntas
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] epos  Posição do eixo extensor, unidade mm
    * @param  [in] blendT [-1.0]-movimento até o fim (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), unidade ms
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @return  Código de erro
    */
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos); 

Movimento no Espaço das Juntas (com cálculo automático de cinemática direta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief  Movimento no espaço das juntas (com cálculo automático de cinemática direta)
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] epos  Posição do eixo extensor, unidade mm
    * @param  [in] blendT [-1.0]-movimento até o fim (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), unidade ms
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @return Código de erro 
    */ 
    int MoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos)

Movimento Linear no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento linear no espaço cartesiano
    * @param [in] joint_pos Posição de junta alvo, unidade deg
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param [in] user Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade [0~100] / velocidade física (mm/s)
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param [in] epos Posição do eixo extensor, unidade mm
    * @param [in] search 0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Quantidade de deslocamento da pose
    * @param [in] oacc Fator de escala de aceleração [0-100] / aceleração física (mm/s2)
    * @param [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @param [in] overSpeedStrategy Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão é 0
    * @param [in] speedPercent Percentual limite para redução de velocidade permitida [0-100], padrão 10%
    * @return Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, float oacc, int velAccParamMode, int overSpeedStrategy = 0, int speedPercent = 10)

Movimento Linear no Espaço Cartesiano (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento linear no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param [in] user  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param [in] epos  Posição do eixo extensor, unidade mm
    * @param [in] search  0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Quantidade de deslocamento da pose
    * @param [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @param [in] overSpeedStrategy  Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão é 0
    * @param [in] speedPercent  Percentual limite para redução de velocidade permitida [0-100], padrão 10%
    * @return  Código de erro
    */
    int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento linear no espaço cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] epos  Posição do eixo extensor, unidade mm
    * @param  [in] search  0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @param  [in] overSpeedStrategy  Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão é 0
    * @param  [in] speedPercent  Percentual limite para redução de velocidade permitida [0-100], padrão 10%
    * @return  Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (sobrecarga 1 com blendMode adicionado)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento linear no espaço cartesiano (sobrecarga 1 com blendMode adicionado)
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param  [in] epos  Posição do eixo extensor, unidade mm
    * @param  [in] search  0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @param  [in] overSpeedStrategy  Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão é 0
    * @param  [in] speedPercent  Percentual limite para redução de velocidade permitida [0-100], padrão 10%
    * @return  Código de erro
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento Linear no Espaço Cartesiano (sobrecarga 2 sem necessidade de posição de junta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento linear no espaço cartesiano (sobrecarga 2 sem necessidade de posição de junta)
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] blendMode Modo de transição; 0-transição tangente; 1-transição de canto
    * @param  [in] epos  Posição do eixo extensor, unidade mm
    * @param  [in] search  0-sem busca de posição do arame, 1-com busca de posição do arame
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @param  [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @param  [in] overSpeedStrategy  Estratégia de tratamento de excesso de velocidade, 1-padrão; 2-parar com erro em caso de excesso de velocidade; 3-redução adaptativa de velocidade, padrão é 0
    * @param  [in] speedPercent  Percentual limite para redução de velocidade permitida [0-100], padrão 10%
    * @return  Código de erro
    */
    public int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int velAccParamMode, int overSpeedStrategy, int speedPercent)

Movimento de Arco no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de arco no espaço cartesiano
    * @param  [in] joint_pos_p  Posição de junta do ponto de caminho, unidade deg
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo extensor, unidade mm
    * @param  [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_p  Quantidade de deslocamento da pose
    * @param  [in] joint_pos_t  Posição de junta do ponto alvo, unidade deg
    * @param  [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo extensor, unidade mm
    * @param  [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_t  Quantidade de deslocamento da pose
    * @param  [in] ovl  Fator de escala de velocidade [0~100] / velocidade física (mm/s)
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] oacc Fator de escala de aceleração [0-100] / aceleração física (mm/s2)
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @return  Código de erro
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc,ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p,JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc,ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t,float ovl, float blendR, float oacc, int velAccParamMode)

Movimento de Arco no Espaço Cartesiano (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de arco no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param [in] puser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_p  Posição do eixo extensor, unidade mm
    * @param [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p  Quantidade de deslocamento da pose
    * @param [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param [in] tuser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos_t  Posição do eixo extensor, unidade mm
    * @param [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t  Quantidade de deslocamento da pose
    * @param [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @return  Código de erro
    */
    int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config)

Movimento de Arco no Espaço Cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de arco no espaço cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
    * @param  [in] joint_pos_p  Posição de junta do ponto de caminho, unidade deg
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo extensor, unidade mm
    * @param  [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_p  Quantidade de deslocamento da pose
    * @param  [in] joint_pos_t  Posição de junta do ponto alvo, unidade deg
    * @param  [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo extensor, unidade mm
    * @param  [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_t  Quantidade de deslocamento da pose
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @return  Código de erro
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int velAccParamMode)

Movimento de Arco no Espaço Cartesiano (sobrecarga 1 sem necessidade de posição de junta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de arco no espaço cartesiano (sobrecarga 1 sem necessidade de posição de junta)
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo extensor, unidade mm
    * @param  [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_p  Quantidade de deslocamento da pose
    * @param  [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [1~15]
    * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo extensor, unidade mm
    * @param  [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos_t  Quantidade de deslocamento da pose
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @return  Código de erro
    */
    public int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config, int velAccParamMode)

Movimento Ponto a Ponto no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Movimento ponto a ponto no espaço cartesiano
    * @param [in] desc_pos Pose cartesiana alvo no sistema de coordenadas base
    * @param [in] tool Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param [in] user Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendT [-1.0]-movimento até o fim (bloqueante), [0~500.0]-tempo de suavização (não bloqueante), unidade ms
    * @param [in] config Configuração do espaço de junta, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com referência a uma configuração específica do espaço de junta, padrão é -1
    * @return Código de erro
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

Movimento de Círculo Completo no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de círculo completo no espaço cartesiano
    * @param  [in] joint_pos_p  Posição de junta do ponto de caminho 1, unidade deg
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho 1
    * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo extensor, unidade mm
    * @param  [in] joint_pos_t  Posição de junta do ponto de caminho 2, unidade deg
    * @param  [in] desc_pos_t   Pose cartesiana do ponto de caminho 2
    * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo extensor, unidade mm
    * @param  [in] ovl  Fator de escala de velocidade [0~100] / velocidade física (mm/s)
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @param  [in] oacc Fator de escala de aceleração [0-100] / aceleração física (mm/s2)
    * @param  [in] blendR -1: bloqueante; 0~1000: raio de suavização
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @return  Código de erro
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc,ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser,float tvel, float tacc, ExaxisPos epos_t, float ovl, int offset_flag,DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

Movimento de Círculo Completo no Espaço Cartesiano (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
     * @brief  Movimento de círculo completo no espaço cartesiano (com cálculo automático de cinemática inversa)
     * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho 1
     * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
     * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [0~14]
     * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
     * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
     * @param  [in] epos_p  Posição do eixo extensor, unidade mm
     * @param  [in] desc_pos_t   Pose cartesiana do ponto de caminho 2
     * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
     * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [0~14]
     * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
     * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
     * @param  [in] epos_t  Posição do eixo extensor, unidade mm
     * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
     * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
     * @param  [in] offset_pos  Quantidade de deslocamento da pose
     * @param  [in] oacc Percentual de aceleração
     * @param  [in] blendR -1: bloqueante; 0~1000: raio de suavização
     * @param  [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
     * @return  Código de erro
     */
    int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR,int config)

Movimento de Círculo Completo no Espaço Cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    *@brief  Movimento de círculo completo no espaço cartesiano (com parâmetro de modo de velocidade/aceleração velAccParamMode adicionado)
    *@param  [in] joint_pos_p  Posição de junta do ponto de caminho 1, unidade deg
    *@param  [in] desc_pos_p   Pose cartesiana do ponto de caminho 1
    *@param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    *@param  [in] puser  Número do sistema de coordenadas da peça, intervalo [1~15]
    *@param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    *@param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    *@param  [in] epos_p  Posição do eixo extensor, unidade mm
    *@param  [in] joint_pos_t  Posição de junta do ponto de caminho 2, unidade deg
    *@param  [in] desc_pos_t   Pose cartesiana do ponto de caminho 2
    *@param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [1~15]
    *@param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [1~15]
    *@param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    *@param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    *@param  [in] epos_t  Posição do eixo extensor, unidade mm
    *@param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    *@param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    *@param  [in] offset_pos  Quantidade de deslocamento da pose
    *@param  [in] oacc Percentual de aceleração
    *@param  [in] blendR -1: bloqueante; 0~1000: raio de suavização
    *@param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    *@return  Código de erro
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

Movimento de Círculo Completo no Espaço Cartesiano (sobrecarga 1 sem necessidade de posição de junta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento de círculo completo no espaço cartesiano (sobrecarga 1 sem necessidade de posição de junta)
    * @param  [in] desc_pos_p   Pose cartesiana do ponto de caminho 1
    * @param  [in] ptool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] puser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] pvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] pacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_p  Posição do eixo extensor, unidade mm
    * @param  [in] desc_pos_t   Pose cartesiana do ponto de caminho 2
    * @param  [in] ttool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] tuser  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] tvel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] tacc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] epos_t  Posição do eixo extensor, unidade mm
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @param  [in] oacc Percentual de aceleração
    * @param  [in] blendR -1: bloqueante; 0~1000: raio de suavização
    * @param  [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @param  [in] velAccParamMode Modo do parâmetro de velocidade/aceleração; 0-porcentagem; 1-velocidade física (mm/s) / aceleração física (mm/s2)
    * @return  Código de erro
    */
    public int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int config, int velAccParamMode)

Exemplo de Código de Movimento de Círculo Completo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    private void btnMovetest_Click(object sender, EventArgs e)
    {
        int rtn = 0;
        DescPose middescPoseCir1 = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosCir1 = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseCir1 = new DescPose(-524.862, -217.402, 308.459, -171.425, -4.810, 156.088);
        JointPos endjointPosCir1 = new JointPos(11.399, -78.055, 104.603, -125.421, -85.770, -54.721);

        DescPose middescPoseCir2 = new DescPose(-482.691, -587.899, 318.594, -171.001, -4.999, -172.996);
        JointPos midjointPosCir2 = new JointPos(42.314, -53.600, 67.296, -112.969, -85.533, -54.721);
        DescPose enddescPoseCir2 = new DescPose(-403.942, -489.061, 317.038, -163.189, -10.425, -175.627);
        JointPos endjointPosCir2 = new JointPos(39.959, -70.616, 96.679, -134.243, -82.276, -54.721);

        DescPose middescPoseMoveC = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosMoveC = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseMoveC = new DescPose(-524.862, -217.402, 308.459, -171.425, -4.810, 156.088);
        JointPos endjointPosmoveC = new JointPos(11.399, -78.055, 104.603, -125.421, -85.770, -54.721);

        DescPose middescPoseCir3 = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosCir3 = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseCir3 = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos endjointPosCir3 = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose middescPoseCir4 = new DescPose(-482.691, -587.899, 318.594, -171.001, -4.999, -172.996);
        JointPos midjointPosCir4 = new JointPos(42.314, -53.600, 67.296, -112.969, -85.533, -54.721);
        DescPose enddescPoseCir4 = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos endjointPosCir4 = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose startdescPose = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos startjointPos = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose linedescPose = new DescPose(-403.942, -489.061, 317.038, -163.189, -10.425, -175.627);
        JointPos linejointPos = new JointPos(39.959, -70.616, 96.679, -134.243, -82.276, -54.721);


        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);


        robot.MoveJ(startjointPos, startdescPose, 3, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.Circle(midjointPosCir1, middescPoseCir1, 3, 0, 100, 100, exaxisPos, endjointPosCir1, enddescPoseCir1, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle1" + rtn);
        rtn = robot.Circle(midjointPosCir2, middescPoseCir2, 3, 0, 100, 100, exaxisPos, endjointPosCir2, enddescPoseCir2, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle2" + rtn);

        robot.MoveC(midjointPosMoveC, middescPoseMoveC, 3, 0, 100, 100, exaxisPos, 0, offdese, endjointPosmoveC, enddescPoseMoveC, 3, 0, 100, 100, exaxisPos, 0, offdese, 100, 20);
        rtn = robot.Circle(midjointPosCir3, middescPoseCir3, 3, 0, 100, 100, exaxisPos, endjointPosCir3, enddescPoseCir3, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle3" + rtn);
        rtn = robot.MoveL(linejointPos, linedescPose, 3, 0, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        Console.WriteLine("MoveL " + rtn);
        rtn = robot.Circle(midjointPosCir4, middescPoseCir4, 3, 0, 100, 100, exaxisPos, endjointPosCir4, enddescPoseCir4, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle4" + rtn);
    }

Exemplo de Código de Instruções Básicas de Movimento do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    public void TestMove()
        int rtn;
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos j2 = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos j3 = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);
        JointPos j4 = new JointPos(-31.154f, -95.317f, 94.276f, -88.079f, -89.740f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose desc_pos2 = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose desc_pos3 = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);
        DescPose desc_pos4 = new DescPose(-443.165f, 147.881f, 480.951f, 179.511f, -0.775f, -15.409f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float oacc = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos,j1, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        Console.WriteLine($"MoveCart errcode:{rtn}");
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,desc_pos4, tool, user, vel, acc, epos, flag, offset_pos,ovl, blendR, -1, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
    }

Movimento de Espiral no Espaço Cartesiano
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento de espiral no espaço cartesiano
    * @param [in] joint_pos Posição de junta alvo, unidade deg
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param [in] user Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos Posição do eixo extensor, unidade mm
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Quantidade de deslocamento da pose
    * @param [in] spiral_param Parâmetros da espiral
    * @return Código de erro
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, ExaxisPos epos, float ovl, byte offset_flag, DescPose offset_pos, SpiralParam spiral_param); 

Movimento de Espiral no Espaço Cartesiano (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento de espiral no espaço cartesiano (com cálculo automático de cinemática inversa)
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] epos  Posição do eixo extensor, unidade mm
    * @param [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Quantidade de deslocamento da pose
    * @param [in] spiral_param  Parâmetros da espiral
    * @param [in] config  Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @return Código de erro 
    */
    int NewSpiral(DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param,int config)

Exemplo de Código de Movimento de Espiral
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public static int TestSpiral(Robot robot)
    {
        int rtn=-1;
        JointPos j=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose offset_pos1=new DescPose(50, 0, 0, -30, 0, 0);
        DescPose offset_pos2=new DescPose(50, 0, 0, -5, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp=new SpiralParam(1,5.0,50.0,10.0,10.0,0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = 0.0;
        int flag = 2;

        rtn = robot.MoveJ(j, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
         Console.WriteLine("movej errcode:"+ rtn);

        rtn = robot.NewSpiral(desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp,-1);
        Console.WriteLine("newspiral errcode:"+ rtn);

        return 0;
    }

Início do Movimento Servo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Início do movimento servo, para uso com as instruções ServoJ e ServoCart
    * @param[in] comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoMoveStart (int comType = 0)

Fim do Movimento Servo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do movimento servo, para uso com as instruções ServoJ e ServoCart
    * @param[in] comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return  Código de erro
    */
    public int ServoMoveEnd (int comType = 0)

Movimento no Modo Servo no Espaço das Juntas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento no modo servo no espaço das juntas
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] axisPos  Posição do eixo externo, unidade mm
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível, padrão é 0
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100], temporariamente não disponível, padrão é 0
    * @param  [in] cmdT  Período de envio da instrução, unidade s, intervalo recomendado [0.001~0.0016]
    * @param  [in] filterT Tempo de filtragem, unidade s, temporariamente não disponível, padrão é 0
    * @param  [in] gain  Amplificador proporcional da posição alvo, temporariamente não disponível, padrão é 0
    * @param  [in] id ID da instrução servoJ, padrão é 0
    * @param  [in] comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return  Código de erro
    */
    public int ServoJ(JointPos joint_pos, ExaxisPos axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id = 0, int comType = 0)

Exemplo de Código SDK para ServoJ, ServoMoveStart, ServoMoveEnd com Comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    public void TestServoJUDP()
    {
        // Assinar callback
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 300;
        float dt = 0.1f;
        int cmdID = 0;

        while (true)
        {
            JointPos j = new JointPos(0, -90, 90, 0, 0, 0);
            ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
            DescPose offset_pos = new DescPose(0, -90, 90, 0, 0, 0);
            robot.MoveJ(j, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            int ret = robot.GetActualJointPosDegree(flag, ref j);
            if (ret == 0)
            {
                count = 300;
                cmdID += 1;
                robot.ServoMoveStart(1);

                while (count > 0)
                {
                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, 1);
                    j.jPos[0] += dt;
                    j.jPos[1] += dt;
                    j.jPos[3] += dt;
                    j.jPos[4] += dt;
                    j.jPos[5] += dt;
                    epos.ePos[0] += dt;
                    count -= 1;
                    Thread.Sleep(1);
                    robot.GetRobotRealTimeState(ref pkg);
                }
                robot.ServoMoveEnd(1);

                Thread.Sleep(1000);
                count = 300;
                robot.ServoMoveStart(1);
                while (count > 0)
                {
                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, 1);
                    j.jPos[0] -= dt;
                    j.jPos[1] -= dt;
                    j.jPos[3] -= dt;
                    j.jPos[4] -= dt;
                    j.jPos[5] -= dt;
                    epos.ePos[0] -= dt;
                    count -= 1;
                    Thread.Sleep(1);
                    robot.GetRobotRealTimeState(ref pkg);
                }
                robot.ServoMoveEnd(1);
            }
            else
            {
                Console.WriteLine($"GetActualJointPosDegree errcode:{ret}");
            }
        }
    }

Exemplo de Código de Movimento no Modo Servo no Espaço das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3

.. code-block:: c#
    :linenos:

    private void btnJointServoMove_Click(object sender, EventArgs e)
    {
        JointPos j = new JointPos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 500;
        float dt = 0.1f;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, ref j);
        if (ret == 0)
        {
            robot.ServoMoveStart();

            try
            {
                while (count > 0)
                {

                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID);


                    j.jPos[0] += dt;
                    count--;


                    robot.WaitMs((int)(cmdT * 1000));
                }
            }
            finally
            {

                robot.ServoMoveEnd();
            }
        }
        else
        {
            Console.WriteLine($"GetActualJointPosDegree error code: {ret}");

        }
    }

Início do Controle de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Início do controle de torque de junta
    * @param [in] comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJTStart (int comType = 0)

Controle de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Controle de torque de junta
    * @param [in] torque Torque das juntas j1~j6, unidade Nm
    * @param [in] interval Período da instrução, unidade s, intervalo [0.001~0.008]
    * @param [in] checkFlag Estratégia de detecção 0-sem restrição; 1-limitar potência; 2-limitar velocidade; 3-limitar potência e velocidade simultaneamente
    * @param [in] jPowerLimit Limite máximo de potência da junta (W)
    * @param [in] jVelLimit Velocidade máxima da junta (°/s)
    * @param [in]  comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return Código de erro
    */
    public int ServoJT(double[] torque, double interval, int checkFlag, double[] jPowerLimit, double[] jVelLimit, int comType = 0)

Fim do Controle de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do controle de torque de junta
    * @param[in] comType Tipo de envio da instrução; 0-xmlrpc; 1-UDP (correspondente à porta 20007 do robô)
    * @return  Código de erro
    */
    public int ServoJTEnd (int comType = 0)

Exemplo de Código SDK para ServoJT, ServoJTStart, ServoJTEnd com Comunicação UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoJTWithSafetyUDP()
    {
        // Assinar callback
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[Resposta UDP] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };
        while (true)
        {
            robot.ResetAllError();
            Thread.Sleep(500);

            JointPos j = new JointPos(7.053, -89.699, 156.141, -72.751, 7.829, 1.889);
            ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
            DescPose offset_pos = new DescPose(-151.288, -321.186, 221.989, 89.140, 4.361, -0.795);
            robot.MoveJ(j, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            double[] torques = new double[6] { 0, 0, 0, 0, 0, 0 };
            robot.GetJointTorques(1, torques);

            robot.ServoJTStart(1);
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);

            int checkFlag = 0;
            double[] jPowerLimit = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
            double[] jVelLimit = new double[6] { 50, 50, 50, 50, 50, 50 };
            int error = 0;
            while (true)
            {

                torques[0] = 0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 1);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] > 30)
                {
                    break;
                }
            }

            while (true)
            {

                torques[0] = -0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 1);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] < 0)
                {
                    break;
                }
            }

            robot.DragTeachSwitch(0);
            error = robot.ServoJTEnd(1);
        }
        return 0;
    }

Exemplo de Código de Controle de Torque de Junta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button27_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }

Exemplo de Código de Controle de Torque de Junta com Proteção contra Excesso de Velocidade
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoJTWithSafety()
    {
        robot.ResetAllError();
        Thread.Sleep(500);

        double[] torques = new double[6] { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        robot.ServoJTStart();
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.DragTeachSwitch(1);

        int checkFlag = 0;
        double[] jPowerLimit = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        //double[] jPowerLimit = new double[6] { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        // double[] jVelLimit = new double[6] { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double[] jVelLimit = new double[6] {50, 50, 50, 50, 50, 50 };
        int count = 80000;
        int errorNum = 0;
        int error = 0;
        while (count > 0)
        {
            
            torques[2] = torques[2] + 0.01; 
            error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit); 

            Console.WriteLine($"ServoJT rtn is {error}");
            count = count - 1;
            Thread.Sleep(1);
                
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
            if (error != 0)
            {
                errorNum++;
                if (errorNum > 5)
                {
                    break;
                }

            }
        }
        robot.DragTeachSwitch(0);
        error = robot.ServoJTEnd();

        return 0;
    }

Movimento no Modo Servo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento no modo servo no espaço cartesiano
    * @param [in] mode 0-movimento absoluto (sistema de coordenadas base), 1-movimento incremental (sistema de coordenadas base), 2-movimento incremental (sistema de coordenadas da ferramenta)
    * @param [in] desc_pos Pose cartesiana alvo ou incremento de pose
    * @param [in] exaxis Posição do eixo extensor
    * @param [in] pos_gain Coeficiente de proporcionalidade do incremento de pose, válido apenas no movimento incremental, intervalo [0~1]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível, padrão é 0
    * @param [in] vel Percentual de velocidade, intervalo [0~100], temporariamente não disponível, padrão é 0
    * @param [in] cmdT Período de envio da instrução, unidade s, intervalo recomendado [0.001~0.016]
    * @param [in] filterT Tempo de filtragem, unidade s, temporariamente não disponível, padrão é 0
    * @param [in] gain Amplificador proporcional da posição alvo, temporariamente não disponível, padrão é 0
    * @return Código de erro
    */
    public int ServoCart(int mode, DescPose desc_pose, ExaxisPos exaxis, double[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain);

Exemplo de Código de Movimento no Modo Servo no Espaço Cartesiano
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestServoCart()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        int rtn;
        DescPose desc_pos_dt = new DescPose(83.00800f, 50.525000f, 29.246f, 179.629f, -7.138f, -166.975f);
        ExaxisPos exaxis = new ExaxisPos(100.0f, 0.0f, 0.0f, 0.0f);
        double[] pos_gain = { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        int mode = 0;
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.001f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 5000;

        robot.SetSpeed(20);

        while (count > 0)
        {
            rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            Console.WriteLine($"ServoCart rtn is {rtn}");
            count -= 1;
            desc_pos_dt.tran.x += 0.01f;
            exaxis.ePos[0] += 0.01f;
        }
    }

Início do Movimento Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início do movimento spline
    * @return  Código de erro
    */
    int SplineStart();

Movimento PTP Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento spline no espaço das juntas
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]   
    * @return  Código de erro
    */
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl);

Movimento Spline no Espaço das Juntas (com cálculo automático de cinemática direta)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  Movimento spline no espaço das juntas (com cálculo automático de cinemática direta)
    * @param  [in] joint_pos  Posição de junta alvo, unidade deg
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @return  Código de erro
    */
    int SplinePTP(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl)

Fim do Movimento Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim do movimento spline
    * @return  Código de erro
    */
    int SplineEnd(); 

Exemplo de Código de Movimento Spline
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSplineMove_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");

        robot.SplineStart();
        robot.SplinePTP(j1, desc_pos1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, desc_pos2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, desc_pos3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, desc_pos4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
    }

Início do Movimento Nova Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief Início do movimento nova spline
    * @param [in] type  0-transição de arco, 1-pontos dados são pontos de caminho
    * @param [in] averageTime  Tempo de transição médio global (ms)(10 ~ ), padrão 2000
    * @return Código de erro 
    */ 
    int NewSplineStart(int type, int averageTime=2000);

Ponto de Instrução Nova Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Adicionar ponto de instrução de movimento spline
    * @param [in] joint_pos Posição de junta alvo, unidade deg
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param [in] user Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param [in] vel Percentual de velocidade, intervalo [0~100]
    * @param [in] acc Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, intervalo [0~100]
    * @param [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param [in] lastFlag  É o último ponto? 0-não, 1-sim
    * @return Código de erro 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

Ponto de Instrução Nova Spline (com cálculo automático de cinemática inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief Ponto de instrução nova spline (com cálculo automático de cinemática inversa)
    * @param  [in] desc_pos   Pose cartesiana alvo
    * @param  [in] tool  Número do sistema de coordenadas da ferramenta, intervalo [0~14]
    * @param  [in] user  Número do sistema de coordenadas da peça, intervalo [0~14]
    * @param  [in] vel  Percentual de velocidade, intervalo [0~100]
    * @param  [in] acc  Percentual de aceleração, intervalo [0~100], temporariamente não disponível
    * @param  [in] ovl  Fator de escala de velocidade, intervalo [0~100]
    * @param  [in] blendR [-1.0]-movimento até o fim (bloqueante), [0~1000.0]-raio de suavização (não bloqueante), unidade mm
    * @param  [in] lastFlag  É o último ponto? 0-não, 1-sim
    * @param  [in] config Configuração do espaço de junta para cinemática inversa, [-1]-resolver com referência à posição atual da junta, [0~7]-resolver com base em uma configuração específica do espaço de junta
    * @return  Código de erro
    */
    int NewSplinePoint(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag,int config)

Fim do Movimento Nova Spline
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Fim do movimento nova spline
    * @return Código de erro 
    */ 
    int NewSplineEnd();

Exemplo de Código de Movimento Nova Spline
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnNewSpline_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");

        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(j1, desc_pos1, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j2, desc_pos2, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j3, desc_pos3, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j4, desc_pos4, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j5, desc_pos5, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplineEnd();
    }

Terminar Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Terminar movimento
    * @return  Código de erro
    */
    int StopMotion();

Pausar Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
      * @brief Pausar movimento 
      * @return Código de erro 
    */  
    int PauseMotion();

Retomar Movimento
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief Retomar movimento 
    * @return Código de erro 
    */ 
    int ResumeMotion();

Exemplo de Código de Pausa, Retomada e Parada de Movimento
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMotionPause_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PauseMotion();

        Thread.Sleep(1000);
        robot.ResumeMotion();

        Thread.Sleep(1000);
        robot.StopMotion();

        Thread.Sleep(1000);

    }

Início do Deslocamento Geral de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Início do deslocamento geral de pontos
    * @param  [in]  flag  0-deslocamento no sistema de coordenadas base/peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param  [in] offset_pos  Quantidade de deslocamento da pose
    * @return  Código de erro
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 

Fim do Deslocamento Geral de Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  Fim do deslocamento geral de pontos
    * @return  Código de erro
    */
    int PointsOffsetDisable(); 

Exemplo de Código de Deslocamento de Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnPointOffect_Click(object sender, EventArgs e)
    {
        JointPos j1, j2;
        DescPose desc_pos1, desc_pos2, offset_pos, offset_pos1;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos1 = new DescPose(50.0, 50.0, 50.0, 5.0, 5.0, 5.0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;
        int type = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetEnable(type, offset_pos1);
        Thread.Sleep(1000);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetDisable();
    }

Início do "Flying Shot" AO da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Início do "Flying Shot" AO da caixa de controle
    * @param [in] AONum Número do AO da caixa de controle
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000mm/s], padrão 1000
    * @param [in] maxAOPercent Percentual AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Percentual AO de compensação da zona morta, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Fim do "Flying Shot" AO da Caixa de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do "Flying Shot" AO da caixa de controle
    * @return Código de erro
    */
    int MoveAOStop();

Início do "Flying Shot" AO da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Início do "Flying Shot" AO da extremidade
    * @param [in] AONum Número do AO da extremidade
    * @param [in] maxTCPSpeed Valor máximo da velocidade TCP [1-5000mm/s], padrão 1000
    * @param [in] maxAOPercent Percentual AO correspondente ao valor máximo da velocidade TCP, padrão 100%
    * @param [in] zeroZoneCmp Percentual AO de compensação da zona morta, inteiro, padrão 20%, intervalo [0-100]
    * @return Código de erro
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

Fim do "Flying Shot" AO da Extremidade
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do "Flying Shot" AO da extremidade
    * @return Código de erro
    */
    int MoveToolAOStop();

Exemplo de Código do "Flying Shot" AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMoveAO_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;

        robot.SetSpeed(5);

        robot.MoveAOStart(0,100,100,20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();
    }

Início do Planejamento FIR para Movimento PTP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:


    /**
    * @brief Início do planejamento FIR para movimento PTP
    * @param [in] maxAcc Valor extremo da aceleração máxima (deg/s2)
    * @param [in] maxJek Valor extremo da jerk (taxa de variação da aceleração) uniforme da junta (deg/s3)
    * @return Código de erro
    */
    int PtpFIRPlanningStart(double maxAcc, double maxJek=1000);

Fim do Planejamento FIR para Movimento PTP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do planejamento FIR para movimento PTP
    * @return Código de erro
    */
    int PtpFIRPlanningEnd();

Início do Planejamento FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Início do planejamento FIR para movimento LIN e ARC
    * @param [in] maxAccLin Valor extremo da aceleração linear (mm/s2)
    * @param [in] maxAccDeg Valor extremo da aceleração angular (deg/s2)
    * @param [in] maxJerkLin Valor extremo da jerk linear (mm/s3)
    * @param [in] maxJerkDeg Valor extremo da jerk angular (deg/s3)
    * @return Código de erro
    */
    int LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

Fim do Planejamento FIR para Movimento LIN e ARC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim do planejamento FIR para movimento LIN e ARC
    * @return Código de erro
    */
    int LinArcFIRPlanningEnd();

Exemplo de Código de Filtro FIR
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2

.. code-block:: c#
    :linenos:


    private void button69_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos midjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos endjointPos = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose middescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose enddescPose = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.PtpFIRPlanningStart(1000,1000);
        Console.WriteLine("PtpFIRPlanningStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.PtpFIRPlanningEnd();
        Console.WriteLine("PtpFIRPlanningEnd rtn is " + rtn);

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        Console.WriteLine("LinArcFIRPlanningStart rtn is " + rtn);
        robot.MoveL( startjointPos,  startdescPose, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese, 1, 1);
        robot.MoveC( midjointPos,  middescPose, 0, 0, 100, 100,  exaxisPos, 0,  offdese,  endjointPos,  enddescPose, 0, 0, 100, 100,  exaxisPos, 0,  offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        Console.WriteLine("LinArcFIRPlanningEnd rtn is " + rtn);
    }

Ativação da Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação da suavização de aceleração
    * @param  [in] saveFlag Salvar configuração após reinicialização?
    * @return  Código de erro
    */
    int AccSmoothStart(bool saveFlag);

Desativação da Suavização de Aceleração
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Desativação da suavização de aceleração
    * @param  [in] saveFlag Salvar configuração após reinicialização?
    * @return  Código de erro
    */
    int AccSmoothEnd(bool saveFlag);

Exemplo de Código
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button1_Click(object sender, EventArgs e)
    {

        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AccSmoothStart(false);
        Console.WriteLine("AccSmoothStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AccSmoothEnd(false);
        Console.WriteLine("AccSmoothEnd rtn is " + rtn);
    }

Ativação da Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação da velocidade de postura especificada
    * @param [in] ratio Percentual da velocidade de postura [0-300]
    * @return  Código de erro
    */
    int AngularSpeedStart(int ratio);

Desativação da Velocidade de Postura Especificada
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Desativação da velocidade de postura especificada
    * @return  Código de erro
    */
    int AngularSpeedEnd();

Exemplo de Código de Velocidade de Postura Especificada do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button71_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AngularSpeedStart(50);
        Console.WriteLine("AngularSpeedStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AngularSpeedEnd();
        Console.WriteLine("AngularSpeedEnd rtn is " + rtn);
    }

Início da Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Início da proteção contra pose singular
    * @param [in] protectMode Modo de proteção contra singularidade, 0: modo de junta; 1-modo cartesiano
    * @param [in] minShoulderPos Faixa de ajuste da singularidade do ombro (mm), padrão 100
    * @param [in] minElbowPos Faixa de ajuste da singularidade do cotovelo (mm), padrão 50
    * @param [in] minWristPos Faixa de ajuste da singularidade do pulso (°), padrão 10
    * @return Código de erro
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

Fim da Proteção contra Pose Singular
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da proteção contra pose singular
    * @return Código de erro
    */
    int SingularAvoidEnd();

Exemplo de Código
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    private void btnTestSingularAvoidEArc_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.SingularAvoidStart(2, 10, 5, 5);
        Console.WriteLine("SingularAvoidStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.SingularAvoidEnd();
        Console.WriteLine("SingularAvoidEnd rtn is " + rtn);
    }

Ativação do Sinal de Parada de Segurança
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Ativação do sinal de parada de segurança
    * @return Código de erro
    */
    int GetSafetyCode();

Limpar Fila de Instruções de Movimento
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7

.. code-block:: c#
    :linenos:

    /**
    * @brief Limpar fila de instruções de movimento
    * @return Código de erro
    */
    public int MotionQueueClear();

Mover para o Ponto de Início da Linha de Interseção (Conexão Tubular)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Mover para o ponto de início da linha de interseção
    * @param [in] mainPoint Pose cartesiana dos 6 pontos de ensinamento do tubo principal
    * @param [in] mainExaxisPos Posição do eixo extensor dos 6 pontos de ensinamento do tubo principal
    * @param [in] piecePoint Pose cartesiana dos 6 pontos de ensinamento do tubo auxiliar
    * @param [in] pieceExaxisPos Posição do eixo extensor dos 6 pontos de ensinamento do tubo auxiliar
    * @param [in] extAxisFlag Habilitar eixo extensor? 0-não habilitar; 1-habilitar
    * @param [in] exaxisPos Posição do eixo extensor no ponto de início
    * @param [in] tool Número do sistema de coordenadas da ferramenta
    * @param [in] wobj Número do sistema de coordenadas da peça
    * @param [in] vel Percentual de velocidade
    * @param [in] acc Percentual de aceleração
    * @param [in] ovl Fator de escala de velocidade
    * @param [in] oacc Fator de escala de aceleração
    * @param [in] moveType Tipo de movimento; 0-PTP; 1-LIN
    * @param [in] moveDirection Direção do movimento; 0-horário; 1-anti-horário
    * @param [in] offset Quantidade de deslocamento
    * @return Código de erro
    */
    public int MoveToIntersectLineStart(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);

Movimento da Linha de Interseção (Conexão Tubular)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento da linha de interseção
    * @param [in] mainPoint Pose cartesiana dos 6 pontos de ensinamento do tubo principal
    * @param [in] mainExaxisPos Posição do eixo extensor dos 6 pontos de ensinamento do tubo principal
    * @param [in] piecePoint Pose cartesiana dos 6 pontos de ensinamento do tubo auxiliar
    * @param [in] pieceExaxisPos Posição do eixo extensor dos 6 pontos de ensinamento do tubo auxiliar
    * @param [in] extAxisFlag Habilitar eixo extensor? 0-não habilitar; 1-habilitar
    * @param [in] exaxisPos Posição do eixo extensor no ponto de início
    * @param [in] tool Número do sistema de coordenadas da ferramenta
    * @param [in] wobj Número do sistema de coordenadas da peça
    * @param [in] vel Percentual de velocidade
    * @param [in] acc Percentual de aceleração
    * @param [in] ovl Fator de escala de velocidade
    * @param [in] oacc Fator de escala de aceleração
    * @param [in] moveDirection Direção do movimento; 0-horário; 1-anti-horário
    * @param [in] offset Quantidade de deslocamento
    * @return Código de erro
    */
    public int MoveIntersectLine(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos[] exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);

Exemplo de Código de Movimento da Linha de Interseção do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
            return ;
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
        return ;
    }

Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Movimento estacionário no local
    * @return Código de erro
    */
    public int MoveStationary()

Exemplo de Código de Movimento Estacionário no Local
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void LaserSensorRecordandReplay()
    {
        int rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 1, 10, 100);
        Console.WriteLine($"LaserSensorRecordandReplay rtn is {rtn}");
        rtn = robot.MoveStationary();
        Console.WriteLine($"MoveStationary rtn is {rtn}");
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord1 rtn is {rtn}"); 
    }

Início da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Início da oscilação em ponto fixo
    * @param [in] weaveNum Número da oscilação [0-7]
    * @param [in] mode 0-sistema de coordenadas da ferramenta; 1-ponto de referência
    * @param [in] refPoint Coordenadas cartesianas do ponto de referência [x, y, z, a, b, c]
    * @param [in] weaveTime Tempo de oscilação [s]
    * @return Código de erro
    */
    public int OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime);

Fim da Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief Fim da oscilação em ponto fixo
    * @return Código de erro
    */
    public int OriginPointWeaveEnd();

Exemplo de Código SDK para Oscilação em Ponto Fixo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void TestOriginPointWeave()
    {
        // Criar objeto de posição de junta
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        // Coordenadas do ponto de referência
        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);

        //// Primeiro movimento
        robot.MoveJ(j, 1, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // Iniciar oscilação em ponto fixo (modo 0)
        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();   // Executar movimento fixo (assumindo que este método existe)
        robot.OriginPointWeaveEnd();

        Thread.Sleep(2000);         // Aguardar 2 segundos

        // Segundo movimento
        robot.MoveJ(j, 1, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // Iniciar oscilação em ponto fixo (modo 1)
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();
    }

Exemplo de Código SDK para Oscilação em Ponto Fixo (incluindo Laser e Eixo Extensor)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void TestOriginPointWeave2()
    {
        // Criar objeto de posição de junta
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos1 = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos2 = new ExaxisPos(5, 0.000, 0.000, 0.000);

        // Coordenadas do ponto de referência
        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);

        int rtn = 0;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);

        // Carregar driver UDP
        robot.ExtDevLoadUDPDriver();

        // Definir tempo de conclusão do comando do eixo extensor
        rtn = robot.SetExAxisCmdDoneTime(5000.0);
        Console.WriteLine("SetExAxisCmdDoneTime rtn is " + rtn);

        // Habilitar eixos extensores 1 e 2
        rtn = robot.ExtAxisServoOn(1, 1);
        Console.WriteLine("ExtAxisServoOn axis id 1 rtn is " + rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        Console.WriteLine("ExtAxisServoOn axis id 2 rtn is " + rtn);
        Thread.Sleep(2000);

        // Definir homing do eixo extensor
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.LaserTrackingLaserOnOff(1);


        //// 1---Sem eixo extensor
        robot.LaserTrackingTrackOnOff(1, 4);
        robot.Sleep(200);
        // Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 10);
        robot.MoveStationary();   // Executar movimento fixo
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);

        Thread.Sleep(2000);         // Aguardar 2 segundos

        //// 2----Com eixo extensor
        robot.ExtAxisMove(epos1, 100, -1);
        robot.LaserTrackingTrackOnOff(1, 4);
        // Iniciar oscilação em ponto fixo
        robot.OriginPointWeaveStart(0, 0, refPoint, 20);
        robot.ExtAxisMove(epos2, 100, -1);
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);
    }