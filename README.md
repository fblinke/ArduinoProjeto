# ArduinoProjeto
Monitoramento de temperatura em ambientes corporativos

# I) Breve Descrição do Funcionamento e Uso
Este projeto implementa um sistema de monitoramento ambiental baseado em IoT, utilizando um Arduino Uno, um sensor DHT11, e um módulo ESP8266. Ele é projetado para capturar temperatura e umidade em tempo real, acionar alertas locais (LED e buzzer) quando os limites predefinidos são excedidos e enviar notificações remotas por meio de mensagens MQTT e e-mail.

Como usar:
Montagem: Conecte o hardware de acordo com o esquema de montagem fornecido.
Código: Carregue o código no Arduino usando a IDE do Arduino e configure o script Python no computador para gerenciar alertas MQTT e e-mails.
Monitoramento: Ative o sistema. Ele iniciará o monitoramento e notificará quando condições críticas forem detectadas.

# II) Software Desenvolvido e Documentação de Código

Código do Arduino
O código para o Arduino lê dados do sensor DHT11, verifica se ultrapassam os limites predefinidos, aciona os atuadores e envia mensagens de alerta via MQTT.

Script Python para MQTT e E-mail
Esse script recebe mensagens via MQTT e envia e-mails automáticos ao detectar alertas.

# III) Descrição do Hardware Utilizado

Plataforma: Arduino Uno R3

Microcontrolador: ATmega328P

Pinos: 14 digitais, 6 analógicos

Tensão de operação: 5V

Sensor DHT11: Faixa de temperatura: 0°C a 50°C com precisão de ±2°C

Atuadores: LED (indicador visual), Buzzer (indicador sonoro).

Protoboard e Jumpers: Para conexão dos componentes.

# IV) Documentação das Interfaces, Protocolos e Módulos de Comunicação

Protocolo MQTT
Broker Utilizado: HiveMQ (gratuito e confiável).
Tópico: alertas/temperatura
Formato das Mensagens:
Exemplo: MQTT: ALERTA: Temperatura acima do limite! 28.0 °C
Fluxo de Comunicação:
Arduino publica mensagens de alerta no broker.
Script Python no computador assina o tópico e processa as mensagens.

Conexão Serial
Configuração:
Porta: COM4 (pode variar conforme o dispositivo).
Taxa de transmissão: 9600 baud.

E-mails Automáticos
Protocolo: SMTP (usando Gmail).
Formato do E-mail:
Assunto: Alerta de Temperatura
Corpo: ALERTA: Temperatura acima do limite! [valor] °C

Esta documentação fornece o suporte necessário para configurar, reproduzir e adaptar o sistema em aplicações variadas.
