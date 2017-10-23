# Projeto 2.1

Por Jean Luca e Pedro de la Peña

## Modulação  

A modulação consiste na multiplicação de um sinal por uma portadora, dada pela fórmula

p(t) = A*cos(2πf*t)

sendo A a amplitude, fc a frequencia arbitrária da portadora e t o tempo.

Ao realizar a modulação, torna-se possível enviar mais um sinal em um mesmo meio. Contudo, no final da recepção é preciso que ocorra uma demodulação para recuperar os áudios originais. O processo consiste na multiplicação pela portadora anteriormente utilizada. 

## Portadoras utilizadas

A freqquência de corte utilizada foi de 2000Hz. Levando isso em conta, as frequências das duas portadoras utilizadas deveriam ser maiores que o valor de corte e devem ser inferiores ao valor de 22050Hz, metade do valor da frequência de amostragem. Contudo, levamos em conta valores até 18000Hz pois os microfones imbutidos nos (nossos) notebooks não são muito eficazes quando expostos a frequências superiores à estas.

Além disso, as frequências das portadoras não podem ser muito próximas umas das oturas para não se misturarem e impossibilitarem os audios originais de serem recuperados no final do processo de recepção. 
Isto posto, temos as frequências de 5000Hz e 10000Hz.

Contudo, o código permite que o usuário defina as frequências das portadoras, porém deve ter em mente o que foi listado anteriormente

## Bandas ocupadas
Devido ao fato da frequência de corte (apresentada nos gráficos) ser de 2000Hz, a banda utilizada é de 4000Hz. 

Contudo, o código permite que o usuário defina a frequência de corte que irá utilizar, o que consequentemente, afetará o tamanho da banda. Em termos gerais, a banda é equivalente a 2 vezes a frequência de corte. 


## Gráficos


| Tom   | Sinal Transmitido       |Sinal Recebido        |
|:-----:|-------------------------|----------------------|
|1      | ![1](img/transmitido1.png)        |![1](img/recebido1.png)      |
|2      | ![2](img/transmitido2.png)        |![2](img/recebido2.png)      |
|3      | ![3](img/transmitido3.png)        |![3](img/recebido3.png)      |
|4      | ![4](img/transmitido4.png)        |![4](img/recebido4.png)      |
|5      | ![5](img/transmitido5.png)        |![5](img/recebido5.png)      |
|6      | ![6](img/transmitido6.png)        |![6](img/recebido6.png)      |
|7      | ![7](img/transmitido7.png)        |![7](img/recebido7.png)      |
|8      | ![8](img/transmitido8.png)        |![8](img/recebido8.png)      |
|9      | ![9](img/transmitido9.png)        |![9](img/recebido9.png)      | 
|0      | ![0](img/transmitido0.png)        |![0](img/recebido0.png)      |


## Comparação entre enviado e recebido


