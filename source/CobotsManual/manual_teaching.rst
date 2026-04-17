Ensinamento Manual do Robô
===============================

Ensinamento Manual e Registro de Pontos de Ensinamento
------------------------------------------------------------

O ensinamento manual inclui dois métodos:

- 1. Manter pressionado o botão de arrasto na extremidade para realizar o ensinamento por arrasto.
- 2. Realizar o movimento ponto a ponto no robô 3D simulado -> operações com objetos 3D.

Após ensinar a posição desejada, salve o ponto de ensinamento em “Funções Complementares do Robô” -> “Registro de Pontos de Ensinamento”. Ao salvar um ponto de ensinamento, o sistema de coordenadas do ponto é o sistema de coordenadas atualmente aplicado pelo robô.

.. image:: teaching_pendant_software/056.png
   :width: 6in
   :align: center

.. centered:: Figura 4.1‑1 Ensinamento Manual

Visualizando Informações dos Pontos de Ensinamento
------------------------------------------------------------

Clique em “Programas de Ensinamento” -> “Pontos de Ensinamento” para exibir todos os pontos de ensinamento salvos. O modo de ponto atual é dividido em “Modo de Sistema” e “Modo de Tabela de Pontos”.

Nesta interface, você pode importar e exportar arquivos de pontos de ensinamento. Selecione um ponto de ensinamento e clique no botão “Excluir” para removê-lo. Os valores x, y, z, rx, ry, rz e v do ponto de ensinamento podem ser modificados. Insira o novo valor, marque a caixa de seleção à esquerda e clique em “Modificar” na parte superior para alterar as informações do ponto de ensinamento.

Clique no botão “Iniciar Execução” para executar um único ponto de ensinamento local, movendo o robô para a posição desse ponto. Além disso, o usuário pode pesquisar pontos de ensinamento pelo nome.

.. image:: points/001.png
   :width: 6in
   :align: center

.. centered:: Figura 4.2‑1 Interface de Gerenciamento de Ensinamento

.. important:: 
    Os valores modificados para x, y, z, rx, ry, rz do ponto de ensinamento não devem exceder a área de trabalho do robô.