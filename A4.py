import serial
import time
import paho.mqtt.client as mqtt

# Configuração do Arduino
arduino_port = 'COM4'  # Substitua pela porta correta
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Configuração do MQTT
broker = "broker.hivemq.com"  # Endereço do broker MQTT
port = 1883
topic = "alertas/temperatura"
client = mqtt.Client()

# Conecta ao broker MQTT
client.connect(broker, port, 60)

def enviar_email(temperatura):
    # Função para enviar e-mail via serviços externos (ex.: SMTP, IFTTT)
    print(f"Enviando e-mail: ALERTA de temperatura ({temperatura} °C)")

def processar_mensagem(mensagem):
    if "ALERTA" in mensagem:
        temperatura = mensagem.split("! ")[1].split(" °C")[0]
        print(f"Alerta recebido: {mensagem}")
        
        # Publica mensagem no broker MQTT
        client.publish(topic, mensagem)
        print(f"Mensagem publicada no MQTT: {mensagem}")

        # Envia e-mail de alerta
        enviar_email(temperatura)

while True:
    try:
        # Lê dados da porta serial
        linha = ser.readline().decode('utf-8').strip()
        if linha and "MQTT" in linha:
            mensagem = linha.split("MQTT: ")[1]
            processar_mensagem(mensagem)
        
        time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando programa.")
        ser.close()
        break


import smtplib
from email.mime.text import MIMEText

def enviar_email(temperatura):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "gmail.com"
    sender_password = "senha"
    recipient_email = "@hotmail.com"

    mensagem = MIMEText(f"ALERTA: Temperatura acima do limite! {temperatura} °C")
    mensagem['Subject'] = "Alerta de Temperatura"
    mensagem['From'] = sender_email
    mensagem['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, mensagem.as_string())
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
