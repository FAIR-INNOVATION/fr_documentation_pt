Notas de Atualização de Versão
==========================================

.. toctree:: 
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **Número da Versão**
     - **Data**
     - **Descrição da Atualização**

   * - V3.9.5
     - 2026-04-24
     - | 1.Interface SetTrajectoryJSpeed() adiciona os modos de redução de velocidade e comutação direta;
       | 2.Interface FieldBusSlaveWriteAO() altera o tipo de valor de escrita para double, onde AO0~AO15 são do tipo inteiro e AO16~AO31 são do tipo ponto flutuante;
       | 3.Interface FieldBusSlaveReadAI() altera o tipo de valor de leitura para double, onde AI0~AI15 são do tipo inteiro e AI16~AI31 são do tipo ponto flutuante;
       | 4.Tipo de estrutura de feedback de estado do robô atualizado;
       | 5.Adicionado tipo de enumeração de configuração de feedback de estado do robô;
       | 6.Adicionada interface SetRobotRealtimeStateConfig() para configurar o feedback de estado CNDE do robô;
       | 7.Adicionada interface AddRobotRealtimeState() para adicionar um estado do robô à configuração de estado CNDE;
       | 8.Adicionada interface DeleteRobotRealtimeState() para remover um estado do robô da configuração de estado CNDE;
       | 9.Adicionada interface SetRobotRealtimeStatePeriod() para definir o período de feedback de estado CNDE;
       | 10.Adicionada interface GetRobotRealtimeStateConfig() para obter todos os conjuntos de estados e o período do feedback de estado CNDE atual.

   * - V3.9.4
     - 2026-03-25
     - | 1. A interface ServoJTStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 2. A interface ServoJTEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 3. A interface ServoJT() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 4. A interface ServoMoveStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 5. A interface ServoMoveEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 6. A interface ServoJ() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLPRC/UDP;
       | 7. A interface SetWeldMachineCtrlMode() adicionou um parâmetro de seleção de modo de controle;
       | 8. A interface ExtDevGetUDPComParam() adicionou a obtenção de um parâmetro de comunicação UDP: se reconectar automaticamente após reiniciar o painel de controle;
       | 9. Adicionada a interface SetAxleGenComEnable() para ativar a função de passagem direta na extremidade;
       | 10. Adicionada a interface SndRcvAxleGenComCmdData() para enviar dados aperiódicos na extremidade e aguardar resposta;
       | 11. Adicionada a interface SetRobotStopOnComDisc() para parar a operação do robô quando a comunicação da porta é desconectada;
       | 12. Adicionada a interface GetRobotStopOnComDisc() para obter o parâmetro de parada do robô quando a comunicação da porta é desconectada;
       | 13. Adicionada a interface SetDIConfig() para definir a função da porta CI configurável do painel de controle;
       | 14. Adicionada a interface GetDIConfig() para obter a função da porta CI configurável do painel de controle;
       | 15. Adicionada a interface SetDOConfig() para definir a função da porta CO configurável do painel de controle;
       | 16. Adicionada a interface GetDOConfig() para obter a função da porta CO configurável do painel de controle;
       | 17. Adicionada a interface SetToolDIConfig() para definir a função da porta End-CI configurável da extremidade;
       | 18. Adicionada a interface GetToolDIConfig() para obter a função da porta End-CI configurável da extremidade;
       | 19. Adicionada a interface SetDIConfigLevel() para definir o estado ativo da porta CI configurável do painel de controle;
       | 20. Adicionada a interface GetDIConfigLevel() para obter o estado ativo da porta CI configurável do painel de controle;
       | 21. Adicionada a interface SetDOConfigLevel() para definir o estado ativo da porta CO configurável do painel de controle;
       | 22. Adicionada a interface GetDOConfigLevel() para obter o estado ativo da porta CO configurável do painel de controle;
       | 23. Adicionada a interface SetToolDIConfigLevel() para definir o estado ativo da porta CI configurável da extremidade;
       | 24. Adicionada a interface GetToolDIConfigLevel() para obter o estado ativo da porta CI configurável da extremidade;
       | 25. Adicionada a interface SetStandardDILevel() para definir o estado ativo do DI padrão do painel de controle;
       | 26. Adicionada a interface GetStandardDILevel() para obter o estado ativo do DI padrão do painel de controle;
       | 27. Adicionada a interface SetStandardDOLevel() para definir o estado ativo do DO padrão do painel de controle;
       | 28. Adicionada a interface GetStandardDOLevel() para obter o estado ativo do DO padrão do painel de controle;
       | 29. Adicionada a interface SetExAxisCmdDoneTimeUDP() para definir o tempo de conclusão do posicionamento do eixo de extensão;
       | 30. Adicionada a interface OpenLuaDownload() para baixar o arquivo Lua de protocolo aberto;
       | 31. Adicionada a interface OpenLuaDelete() para excluir o arquivo Lua de protocolo aberto;
       | 32. Adicionada a interface AllOpenLuaDelete() para excluir o arquivo Lua de protocolo aberto;
       | 33. Adicionada a interface SendUDPFrameUDP() para enviar quadro de comando;
       | 34. Adicionada a interface SetCmdRpyCallback() para definir a função de retorno de chamada do resultado da execução do comando enviado pelo SDK via UDP;
       | 35. Adicionada a interface SetVelReducePara() para definir os parâmetros de velocidade segura;
       | 36. Adicionada a interface OriginPointWeaveStart() para iniciar oscilação em ponto fixo;
       | 37. Adicionada a interface OriginPointWeaveEnd() para encerrar oscilação em ponto fixo;
       | 38. Adicionada a interface SetUserLEDColor() para definir a cor do LED da extremidade do robô personalizada pelo usuário;
       | 39. Adicionada a interface MoveToTPDStart() para mover para o início da gravação da trajetória TPD;

   * - V3.9.3
     - 2026-02-11
     - | 1. A interface ServoCart() adicionou um parâmetro de eixo de extensão
       | 2. A interface SetOutputResetCtlBoxDO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 3. A interface SetOutputResetCtlBoxAO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 4. A interface SetOutputResetAxleDO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 5. A interface SetOutputResetAxleAO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 6. A interface SetOutputResetExtDO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 7. A interface SetOutputResetExtAO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 8. A interface SetOutputResetSmartToolDO() adicionou um parâmetro para recarregar o estado DO antes do reset após retomar da pausa
       | 9. Adicionada a interface GetInverseKinExaxis() para solução de cinemática inversa incluindo a posição do eixo de extensão
       
   * - V3.9.2
     - 2026-01-26
     - | 1. A interface FT_RotInsertion() adicionou um parâmetro de estratégia de tratamento quando nenhuma força/torque é detectada
       | 2. A interface LaserSensorRecordandReplay() adicionou parâmetros relacionados ao rastreamento pontual do robô
       | 3. Adicionada a interface MoveStationary()
       | 4. Adicionada a interface TCPComputeRPY()
       | 5. Adicionada a interface TCPComputeXYZ()
       | 6. Adicionada a interface TCPRecordFlangePosStart()
       | 7. Adicionada a interface TCPRecordFlangePosEnd()
       | 8. Adicionada a interface TCPGetRecordFlangePos()
       | 9. Adicionada a interface PhotoelectricSensorTCPCalibration()

   * - V3.9.1
     - 2025-12-25
     - | 1. A interface MoveL() adicionou um parâmetro de fator de escala de velocidade oacc / parâmetro de aceleração física;
       | 2. A interface MoveC() adicionou um parâmetro de fator de escala de velocidade oacc / parâmetro de aceleração física;
       | 3. A interface Circle() otimizou a descrição dos parâmetros sobre velocidade física e aceleração física;
       | 4. Adicionada uma função sobrecarregada FT_Control(), com parâmetros de limite de ativação rx, ry e coeficiente de ajuste de torque;
       | 5. Adicionada a interface SerCoderCompenParams();
   
   * - V3.9.0
     - 2025-11-26
     - | 1. A interface JointSensitivityCalibration() adicionou o retorno da linearidade das juntas j1~j6
       | 2. Adicionada a interface JointHysteresisError()
       | 3. Adicionada a interface JointRepeatability()
       | 4. Adicionada a interface SetAdmittanceParams()
       | 5. Adicionada a interface MoveToIntersectLineStart()
       | 6. Adicionada a interface MoveIntersectLine()

   * - V3.8.7
     - 2025-10-21
     - | 1. A interface FT_Control() adicionou parâmetros de massa e amortecimento
       | 2. Adicionada a interface JointSensitivityCalibration()
       | 3. Adicionada a interface JointSensitivityCollect()
       | 4. Adicionada a interface MotionQueueClear()
       | 5. Adicionada a interface GetSlavePortErrCounter()
       | 6. Adicionada a interface SlavePortErrCounterClear()
       | 7. Adicionada a interface SetVelFeedForwardRatio()
       | 8. Adicionada a interface GetVelFeedForwardRatio()
       | 9. Adicionada a interface RobotMCULogCollect()
       | 10. A estrutura de estado adicionou a contagem de instruções ServoJ e os dados da posição alvo da última instrução
       | 11. A estrutura de parâmetros da nova espiral (SpiralParam) adicionou o modo de parâmetro de velocidade e aceleração

   * - V3.8.6
     - 2025-09-19
     - | 1. A interface SetLoadCoord() adicionou um parâmetro de número de carga
       | 2. Adicionada a interface LaserTrackingLaserOnOff()
       | 3. Adicionada a interface LaserTrackingTrackOnOff()
       | 4. Adicionada a interface LaserTrackingSearchStart_xyz()
       | 5. Adicionada a interface LaserTrackingSearchStart_point()
       | 6. Adicionada a interface LaserTrackingSearchStop()
       | 7. Adicionada a interface LaserTrackingSensorConfig()
       | 8. Adicionada a interface LaserTrackingSensorSamplePeriod()
       | 9. Adicionada a interface LoadPosSensorDriver()
       | 10. Adicionada a interface UnLoadPosSensorDriver()
       | 11. Adicionada a interface LaserSensorRecord1()
       | 12. Adicionada a interface LaserSensorReplay()
       | 13. Adicionada a interface MoveLTR()
       | 14. Adicionada a interface LaserSensorRecordandReplay()
       | 15. Adicionada a interface MoveToLaserRecordStart()
       | 16. Adicionada a interface MoveToLaserRecordEnd()
       | 17. Adicionada a interface MoveToLaserSeamPos()
       | 18. Adicionada a interface GetLaserSeamPos()
       | 19. Adicionada a interface ImpedanceControlStartStop()
       | 20. Adicionada a interface GetToolCoordWithID()
       | 21. Adicionada a interface GetWObjCoordWithID()
       | 22. Adicionada a interface GetExToolCoordWithID()
       | 23. Adicionada a interface GetExAxisCoordWithID()
       | 24. Adicionada a interface GetTargetPayloadWithID()
       | 25. Adicionada a interface GetExAxisCoordWithID()
       | 26. Adicionada a interface GetCurWObjCoord()
       | 27. Adicionada a interface GetCurExToolCoord()
       | 28. Adicionada a interface GetCurExToolCoord()
       | 29. Adicionada a interface KernelUpgrade()
       | 30. Adicionada a interface GetKernelUpgradeResult()
       | 31. Adicionada a interface CustomWeaveSetPara()
       | 32. Adicionada a interface CustomWeaveGetPara()
       | 33. A estrutura de estado adicionou dados de ferramenta, peça, ferramenta externa, sistema de coordenadas do eixo de extensão e massa da carga, centro de gravidade

   * - V3.8.5
     - 2025-08-20
     - | 1. As instruções MoveL(), MoveC(), Circle() adicionaram o parâmetro velAccParamMode
       | 2. Adicionadas interfaces MoveJ(), SplinePTP(), ExtAxisSyncMoveJ() com cálculo automático de cinemática direta
       | 3. LoadTrajectoryLA() adicionou um parâmetro para ativar o interruptor de antecipação de velocidade constante
       | 4. Adicionadas interfaces MoveL(), MoveC(), Circle(), NewSplinePoint(), NewSpiral(), ExtAxisSyncMoveL(), ExtAxisSyncMoveC() com cálculo automático de cinemática inversa
       | 5. Adicionadas interfaces de controle de ventosa como SetSuckerCtrl(), GetSuckerState(), WaitSuckerState(), e a interface de estratégia de movimento síncrono SetExAxisRobotPlan()
       | 6. Adicionadas instruções de controle do modo escravo do robô como OpenLuaUpload(), GetFieldBusConfig(), FieldBusSlaveWriteDO(), FieldBusSlaveWriteAO(), FieldBusSlaveReadDI(), FieldBusSlaveReadAI(), FieldBusSlaveWaitDI(), FieldBusSlaveWaitAI()

   * - V3.8.4
     - 2025-07-17
     - | 1. A interface ExtAxisMove() adicionou o parâmetro de suavização blend
       | 2. Adicionada a interface SetFocusCalibPoint()
       | 3. Adicionada a interface ComputeFocusCalib()
       | 4. Adicionada a interface SetFocusPosition()
       | 5. Adicionada a interface FocusStart()
       | 6. Adicionada a interface FocusEnd()
       | 7. Adicionada a interface SetJointFirmwareUpgrade()
       | 8. Adicionada a interface SetCtrlFirmwareUpgrade()
       | 9. Adicionada a interface SetEndFirmwareUpgrade()
       | 10. Adicionada a interface JointAllParamUpgrade()
       
   * - V3.8.3
     - 2025-06-24
     - | 1. A interface Circle() adicionou parâmetros de porcentagem de aceleração e raio de suavização
       | 2. A interface EndForceDragControl() adicionou um parâmetro de flag de detecção de colisão do robô durante arrastagem assistida
       | 3. A interface ServoJ() adicionou um parâmetro de ID de instrução
       | 4. Adicionada a interface SetWideBoxTempFanMonitorParam()
       | 5. Adicionada a interface GetWideBoxTempFanMonitorParam()
       | 6. A estrutura de estado adicionou dados de temperatura do painel de controle e estado da corrente do ventilador
              
   * - V3.8.2
     - 2025-06-13
     - | 1. A interface WeaveSetPara() adicionou um parâmetro de ângulo de inclinação da direção da oscilação (rotação em torno do eixo X da oscilação)
       | 2. A interface WeaveChangeStart() adicionou parâmetros de número de oscilação, velocidade inicial de soldagem, velocidade final de soldagem
       | 3. A interface ExtDevSetUDPComParam() adicionou um parâmetro para estabelecer conexão automaticamente após reinicialização
       | 4. A interface SetCollisionDetectionMethod() adicionou a seleção do modo de limiar do nível de colisão
       | 5. A interface PtpFIRPlanningStart() adicionou o valor extremo do jerk uniforme da junta
       | 6. Adicionada a interface WeldingSetVoltageGradualChangeStart()
       | 7. Adicionada a interface WeldingSetVoltageGradualChangeEnd()
       | 8. Adicionada a interface WeldingSetCurrentGradualChangeStart()
       | 9. Adicionada a interface WeldingSetCurrentGradualChangeEnd()
       | 10. Adicionada a interface ArcWeldTraceAIChannelCurrent()
       | 11. Adicionada a interface ArcWeldTraceAIChannelVoltage()
       | 12. Adicionada a interface ArcWeldTraceCurrentPara()
       | 13. Adicionada a interface ArcWeldTraceVoltagePara()
       | 14. Adicionada a interface GetSmarttoolBtnState()
       | 15. Adicionada a interface ExtAxisGetCoord()
                     
   * - V3.8.1
     - 2025-04-24
     - | 1. A interface ConveyorSetParam() adicionou parâmetros de tipo de movimento de rastreamento, distância inicial de rastreamento, distância final de rastreamento
       | 2. Adicionada a interface AccSmoothStart()
       | 3. Adicionada a interface AccSmoothEnd()
       | 4. Adicionada a interface RbLogDownload()
       | 5. Adicionada a interface AllDataSourceDownload()
       | 6. Adicionada a interface DataPackageDownload()
       | 7. Adicionada a interface GetRobotSN()
       | 8. Adicionada a interface ShutDownRobotOS()
       | 9. Adicionada a interface ConveyorComDetect()
       | 10. Adicionada a interface ConveyorComDetectTrigger()
                     
   * - V3.8.0
     - 2025-02-12
     - | 1. A interface EndForceDragControl() adicionou um parâmetro de estratégia de ponto singular
       | 2. A interface ArcWeldTraceControl() adicionou um parâmetro de deslocamento
       | 3. Adicionada a interface WeaveChangeStart()
       | 4. Adicionada a interface WeaveChangeEnd()
       | 5. Adicionada a interface LoadTrajectoryLA()
       | 6. Adicionada a interface MoveTrajectoryLA()
       | 7. Adicionada a interface CustomCollisionDetectionStart()
       | 8. Adicionada a interface CustomCollisionDetectionEnd()