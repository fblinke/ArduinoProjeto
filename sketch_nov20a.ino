#include <DHT.h>

// Configuração do DHT11
#define DHTPIN 8  // Pino digital conectado ao DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configuração dos pinos
#define LED_PIN 10
#define BUZZER_PIN 9

// Variáveis de configuração
float temperaturaLimite = 20.0;  // Defina o limite de temperatura aqui

void setup() {
  Serial.begin(9600);  // Comunicação serial para enviar dados ao computador
  dht.begin();

  // Configuração dos pinos
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  // Inicialização
  digitalWrite(LED_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);

  Serial.println("Sistema iniciado.");
}

void loop() {
  // Leitura do sensor
  float temperatura = dht.readTemperature();

  // Verifica se a leitura é válida
  if (isnan(temperatura)) {
    Serial.println("Erro: Falha ao ler o sensor DHT11!");
    return;
  }

  // Envia a temperatura via comunicação serial
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  // Verifica se a temperatura ultrapassou o limite
  if (temperatura > temperaturaLimite) {
    Serial.println("Alerta: Temperatura acima do limite!");

    // Aciona o LED e o buzzer
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    delay(2000);  // 2 segundos
    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);

    // Envia mensagem de alerta
    enviarMensagemMQTT(temperatura);
  }

  // Aguarda 2 minutos antes da próxima leitura
  delay(120000);
}

// Função para enviar mensagens via Serial (interpretação do computador)
void enviarMensagemMQTT(float temperatura) {
  String mensagem = "ALERTA: Temperatura acima do limite! " + String(temperatura) + " °C";
  Serial.println("MQTT: " + mensagem);  // Marcador para o software no computador
}
