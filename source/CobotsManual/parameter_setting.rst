Configuração de Parâmetros do Robô
=================================================

Definindo o Método de Instalação
------------------------------------------

O método de instalação padrão do robô é a montagem horizontal. Quando o método de instalação do robô for alterado, é necessário definir o método de instalação real do robô no menu “Configurações Iniciais” -> “Básico” -> “Instalação” para garantir o funcionamento normal do robô.

Considerando cenários de implantação de robôs mais flexíveis e diversos, fornecemos uma função de instalação livre. O usuário clica em “Configurações Iniciais” -> “Básico” -> “Instalação” para entrar na página de configuração do método de instalação do robô. Ajustando manualmente os ângulos de “Inclinação da Base” e “Rotação da Base”, o modelo 3D exibirá o efeito da instalação correspondente. Após a modificação, clique no botão “Aplicar” para concluir a configuração do método de instalação do robô.

.. image:: teaching_pendant_software/026.png
   :width: 6in
   :align: center
   
.. centered:: Figura 3.1-1 Instalação do Robô

.. important::
    Após a instalação do robô, o método de instalação deve ser configurado corretamente. Caso contrário, a função de arrasto e a função de detecção de colisão do robô serão afetadas.

Definindo a Carga na Extremidade
------------------------------------------

Em “Configurações Iniciais” -> “Básico” -> “Carga”, no tipo de identificação “Identificação de Trajetória”, entre na interface de configuração da carga na extremidade.

.. note:: 
   .. image:: base/071.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Aplicar**
   
   Função: Aplica o peso da carga e as coordenadas do centro de massa correspondentes ao número da carga.

.. note:: 
   .. image:: base/072.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Modificar**
   
   Função: Abre/fecha a interface de movimento de identificação.

.. note:: 
   .. image:: base/073.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Renomear**
   
   Função: Renomeia o nome da carga.

.. note:: 
   .. image:: base/074.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Limpar**
   
   Função: Limpa as informações da carga atual (peso da carga e coordenadas do centro de massa são definidos como 0).

Ao configurar a carga na extremidade, você pode inserir diretamente a massa da ferramenta final e as coordenadas correspondentes do centro de massa X, Y e Z e, em seguida, clicar no botão “Aplicar” para definir.

Ao mesmo tempo, você pode clicar no botão “Editar” para abrir a interface “Movimento de Identificação” para realizar a identificação automática da carga. Após a conclusão da execução da identificação, aplique-a.

.. important:: 
    A massa da carga não pode exceder a capacidade máxima de carga do robô. As cargas correspondentes para cada modelo são:

   - FR3: 3 kg
   - FR5: 5 kg
   - FR10: 10 kg
   - FR16: 16 kg
   - FR20: 20 kg
   - FR30: 30 kg

   A faixa de configuração das coordenadas do centro de massa é 0-1000, em mm.

.. image:: base/016.png
   :width: 4in
   :align: center

.. centered:: Figura 3.2-1 Diagrama de Configuração de Carga
    
.. important:: 
    Após instalar uma carga na extremidade do robô, a massa da carga e as coordenadas do centro de massa devem ser configuradas corretamente. Caso contrário, a função de arrasto e a função de detecção de colisão do robô serão afetadas.

Definindo o Sistema de Coordenadas da Ferramenta
----------------------------------------------------------------

Em “Configurações Iniciais” -> “Básico” -> “Coordenadas da Ferramenta”, entre na página de coordenadas da ferramenta.

.. note:: 
   .. image:: base/071.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Aplicar**
   
   Função: Aplica o sistema de coordenadas da ferramenta.

.. note:: 
   .. image:: base/072.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Modificar**
   
   Função: Abre/fecha a interface de calibração do sistema de coordenadas.

.. note:: 
   .. image:: base/073.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Renomear**
   
   Função: Renomeia o nome do sistema de coordenadas da ferramenta.

.. note:: 
   .. image:: base/074.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Limpar**
   
   Função: Limpa as informações atuais do sistema de coordenadas da ferramenta.

As coordenadas da ferramenta permitem modificar, limpar e aplicar o sistema de coordenadas da ferramenta. Na lista suspensa do sistema de coordenadas da ferramenta, ao selecionar um sistema, os valores de coordenadas correspondentes serão exibidos abaixo (o nome do sistema pode ser personalizado), junto com o tipo de ferramenta e a posição de instalação (exibido apenas para ferramentas do tipo sensor). Após selecionar um sistema, clique no botão “Aplicar”. O sistema de coordenadas da ferramenta atualmente em uso será alterado para o selecionado, conforme mostrado abaixo.

.. image:: base/001.png
   :width: 4in
   :align: center
   
.. centered:: Figura 3.3-1 Configuração de Coordenadas da Ferramenta

Clique em “Modificar” para redefinir o sistema de coordenadas da ferramenta para o número selecionado, de acordo com as instruções. Os métodos de calibração da ferramenta são divididos em método de quatro pontos e método de seis pontos. O método de quatro pontos calibra apenas o TCP da ferramenta (ponto central da ferramenta), com sua postura sendo a mesma da postura da extremidade. O método de seis pontos adiciona dois pontos ao método de quatro pontos para calibrar a postura da ferramenta.

.. image:: base/002.png
   :width: 4in
   :align: center

.. centered:: Figura 3.3-2 Calibração do Sistema de Coordenadas da Ferramenta

.. important:: 
    1. Após instalar uma ferramenta na extremidade, a calibração e aplicação do sistema de coordenadas da ferramenta são obrigatórias. Caso contrário, a posição e postura do ponto central da ferramenta ao executar comandos de movimento do robô podem não corresponder ao esperado.

    2. Os sistemas de coordenadas da ferramenta geralmente usam toolcoord1 a toolcoord19. Aplicar toolcoord0 significa que o centro do TCP da ferramenta está no centro da flange da extremidade. Ao calibrar um sistema de coordenadas da ferramenta, primeiro aplique toolcoord0, depois selecione outro sistema de coordenadas da ferramenta para calibração e aplicação.