Notas de Atualização de Versão
====================================

.. toctree::
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **Número da Versão**
     - **Data**
     - **Descrição da Atualização**

   * - V3.9.4
     - 2026-03-25
     - | 1. A interface ServoJTStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 2. A interface ServoJTEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 3. A interface ServoJT() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 4. A interface ServoMoveStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 5. A interface ServoMoveEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 6. A interface ServoJ() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 7. A interface SetWeldMachineCtrlMode() adicionou um parâmetro de seleção de modo de controle;
       | 8. A interface ExtDevGetUDPComParam() adicionou a obtenção do parâmetro de comunicação UDP: reconexão automática após reinicialização da caixa de controle;
       | 9. Adicionada a interface SetAxleGenComEnable() para ativar a função de transmissão transparente de uso geral da extremidade;
       | 10. Adicionada a interface SndRcvAxleGenComCmdData() para enviar dados não periódicos da extremidade e aguardar resposta;
       | 11. Adicionada a interface SetRobotStopOnComDisc() para definir a parada da operação do robô quando a comunicação da porta for desconectada;
       | 12. Adicionada a interface GetRobotStopOnComDisc() para obter o parâmetro de parada da operação do robô quando a comunicação da porta for desconectada;
       | 13. Adicionada a interface SetDIConfig() para definir a função da porta CI configurável da caixa de controle;
       | 14. Adicionada a interface GetDIConfig() para obter a função da porta CI configurável da caixa de controle;
       | 15. Adicionada a interface SetDOConfig() para definir a função da porta CO configurável da caixa de controle;
       | 16. Adicionada a interface GetDOConfig() para obter a função da porta CO configurável da caixa de controle;
       | 17. Adicionada a interface SetToolDIConfig() para definir a função da porta End-CI configurável da extremidade;
       | 18. Adicionada a interface GetToolDIConfig() para obter a função da porta End-CI configurável da extremidade;
       | 19. Adicionada a interface SetDIConfigLevel() para definir o estado ativo do CI configurável da caixa de controle;
       | 20. Adicionada a interface GetDIConfigLevel() para obter o estado ativo do CI configurável da caixa de controle;
       | 21. Adicionada a interface SetDOConfigLevel() para definir o estado ativo do CO configurável da caixa de controle;
       | 22. Adicionada a interface GetDOConfigLevel() para obter o estado ativo do CO configurável da caixa de controle;
       | 23. Adicionada a interface SetToolDIConfigLevel() para definir o estado ativo do CI configurável da extremidade;
       | 24. Adicionada a interface GetToolDIConfigLevel() para obter o estado ativo do CI configurável da extremidade;
       | 25. Adicionada a interface SetStandardDILevel() para definir o estado ativo do DI padrão da caixa de controle;
       | 26. Adicionada a interface GetStandardDILevel() para obter o estado ativo do DI padrão da caixa de controle;
       | 27. Adicionada a interface SetStandardDOLevel() para definir o estado ativo do DO padrão da caixa de controle;
       | 28. Adicionada a interface GetStandardDOLevel() para obter o estado ativo do DO padrão da caixa de controle;
       | 29. Adicionada a interface SetExAxisCmdDoneTimeUDP() para definir o tempo de conclusão do posicionamento do eixo estendido;
       | 30. Adicionada a interface OpenLuaDownload() para baixar arquivos Lua de protocolo aberto;
       | 31. Adicionada a interface OpenLuaDelete() para excluir arquivos Lua de protocolo aberto;
       | 32. Adicionada a interface AllOpenLuaDelete() para excluir arquivos Lua de protocolo aberto;
       | 33. Adicionada a interface SendUDPFrameUDP() para enviar quadros de comando;
       | 34. Adicionada a interface SetCmdRpyCallback() para definir a função de retorno de chamada do resultado da execução do comando enviado pelo SDK via UDP;
       | 35. Adicionada a interface SetVelReducePara() para definir parâmetros de velocidade segura;
       | 36. Adicionada a interface OriginPointWeaveStart() para iniciar oscilação em ponto fixo;
       | 37. Adicionada a interface OriginPointWeaveEnd() para finalizar oscilação em ponto fixo;
       | 38. Adicionada a interface SetUserLEDColor() para definir a cor da luz da extremidade do robô personalizada pelo usuário;
       | 39. Adicionada a interface MoveToTPDStart() para mover até o ponto inicial de gravação da trajetória TPD;

   * - V3.9.3
     - 2026-02-11
     - | 1. A interface ServoCart() adicionou um parâmetro de eixo estendido
       | 2. A interface SetOutputResetCtlBoxDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 3. A interface SetOutputResetCtlBoxAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 4. A interface SetOutputResetAxleDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 5. A interface SetOutputResetAxleAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 6. A interface SetOutputResetExtDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 7. A interface SetOutputResetExtAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 8. A interface SetOutputResetSmartToolDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 9. Adicionada a interface GetInverseKinExaxis() para solução de cinemática inversa incluindo posição do eixo estendido

   * - V3.9.2
     - 2026-01-26
     - | 1. A interface FT_RotInsertion() adicionou um parâmetro de estratégia de tratamento para quando força/torque não são detectados
       | 2. A interface LaserSensorRecordandReplay() adicionou parâmetros relacionados ao rastreamento de ponto fixo do robô
       | 3. Adicionada a interface MoveStationary()
       | 4. Adicionada a interface TCPComputeRPY()
       | 5. Adicionada a interface TCPComputeXYZ()
       | 6. Adicionada a interface TCPRecordFlangePosStart()
       | 7. Adicionada a interface TCPRecordFlangePosEnd()
       | 8. Adicionada a interface TCPGetRecordFlangePos()
       | 9. Adicionada a interface PhotoelectricSensorTCPCalibration()

   * - V3.9.1
     - 2025-12-25
     - | 1. A interface MoveL() adicionou o parâmetro de fator de escala de velocidade oacc/parâmetro de aceleração física
       | 2. A interface MoveC() adicionou o parâmetro de fator de escala de velocidade oacc/parâmetro de aceleração física
       | 3. A interface Circle() otimizou a descrição dos parâmetros de velocidade física e aceleração física
       | 4. Adicionada a função sobrecarregada FT_Control(), com parâmetros de limiar de ativação rx, ry e coeficiente de ajuste de torque
       | 5. Adicionada a interface SerCoderCompenParams()

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
     - | 1. FT_Control() adicionou parâmetros de massa e amortecimento
       | 2. Adicionada a interface JointSensitivityCalibration()
       | 3. Adicionada a interface JointSensitivityCollect()
       | 4. Adicionada a interface MotionQueueClear()
       | 5. Adicionada a interface GetSlavePortErrCounter()
       | 6. Adicionada a interface SlavePortErrCounterClear()
       | 7. Adicionada a interface SetVelFeedForwardRatio()
       | 8. Adicionada a interface GetVelFeedForwardRatio()
       | 9. Adicionada a interface RobotMCULogCollect()
       | 10. A estrutura de estado adicionou contagem de instruções ServoJ e dados de posição alvo da última instrução
       | 11. A estrutura de parâmetros da nova espiral SpiralParam adicionou modo de parâmetro de velocidade/aceleração

   * - V3.8.6
     - 2025-09-19
     - | 1. A interface SetLoadCoord() adicionou o parâmetro de número da carga
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
       | 33. A estrutura de estado adicionou dados de sistemas de coordenadas de ferramenta, peça, ferramenta externa, eixo estendido e massa do centro de carga

   * - V3.8.5
     - 2025-08-20
     - | 1. Adicionada a interface OpenLuaUpload()
       | 2. Adicionada a interface GetFieldBusConfig()
       | 3. Adicionada a interface FieldBusSlaveWriteDO()
       | 4. Adicionada a interface FieldBusSlaveWriteAO()
       | 5. Adicionada a interface FieldBusSlaveReadDI()
       | 6. Adicionada a interface FieldBusSlaveReadAI()
       | 7. Adicionada a interface FieldBusSlaveWaitDI()
       | 8. Adicionada a interface FieldBusSlaveWaitAI()
       | 9. Adicionada a interface SetSuckerCtrl()
       | 10. Adicionada a interface GetSuckerState()
       | 11. Adicionada a interface WaitSuckerState()
       | 12. Adicionada a interface MoveL() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 13. Adicionada a função sobrecarregada MoveL() 1
       | 14. Adicionada a função sobrecarregada MoveL() 2
       | 15. Adicionada a interface MoveC() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 16. Adicionada a função sobrecarregada MoveC() 1
       | 17. Adicionada a interface Circle() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 18. Adicionada a função sobrecarregada Circle() 1
       | 19. Adicionada a interface SetExAxisRobotPlan()

   * - V3.8.4
     - 2025-07-17
     - | 1. A interface ExtAxisMove() adicionou o parâmetro de suavização blend
       | 2. Adicionada a interface SetFocusCalibPoint()
       | 3. Adicionada a interface ComputeFocusCalib()
       | 4. Adicionada a interface SetFocusPosition()
       | 5. Adicionada a interface FocusStart()
       | 6. Adicionada a interface FocusEnd()
       | 7. Adicionada a interface SetEncoderUpgrade()
       | 8. Adicionada a interface SetJointFirmwareUpgrade()
       | 9. Adicionada a interface SetCtrlFirmwareUpgrade()
       | 10. Adicionada a interface SetEndFirmwareUpgrade()
       | 11. Adicionada a interface JointAllParamUpgrade()

   * - V3.8.3
     - 2025-06-24
     - | 1. A interface Circle() adicionou parâmetros de percentagem de aceleração e raio de suavização
       | 2. A interface EndForceDragControl() adicionou um parâmetro de sinalização de detecção de colisão do robô durante arrasto auxiliar
       | 3. A interface ServoJ() adicionou um parâmetro de ID de instrução
       | 4. Adicionada a interface SetSSHScpCmd()
       | 5. Adicionada a interface SetWideBoxTempFanMonitorParam()
       | 6. Adicionada a interface GetWideBoxTempFanMonitorParam()
       | 7. A estrutura de estado adicionou dados de estado de temperatura da caixa de controle e corrente da ventoinha

   * - V3.8.2
     - 2025-06-13
     - | 1. A interface WeaveSetPara() adicionou o parâmetro de ângulo de inclinação da direção da oscilação (deflexão em torno do eixo X da oscilação)
       | 2. A interface WeaveChangeStart() adicionou parâmetros de número da oscilação, velocidade inicial de soldagem e velocidade final de soldagem
       | 3. A interface ExtDevSetUDPComParam() adicionou o parâmetro para estabelecer conexão automaticamente após reinicialização com perda de energia
       | 4. A interface SetCollisionDetectionMethod() adicionou a seleção do modo de limiar do nível de colisão
       | 5. A interface PtpFIRPlanningStart() adicionou o valor extremo de jerk uniforme das juntas
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
     - | 1. A interface ConveyorSetParam() adicionou parâmetros de tipo de movimento de rastreamento, distância inicial de rastreamento e distância final de rastreamento
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
     - | 1. A interface EndForceDragControl() adicionou o parâmetro de evitação de singularidade
       | 2. A interface ArcWeldTraceControl() adicionou o parâmetro de deslocamento
       | 3. Adicionada a interface WeaveChangeStart()
       | 4. Adicionada a interface WeaveChangeEnd()
       | 5. Adicionada a interface LoadTrajectoryLA()
       | 6. Adicionada a interface MoveTrajectoryLA()
       | 7. Adicionada a interface CustomCollisionDetectionStart()
       | 8. Adicionada a interface CustomCollisionDetectionEnd()