import network
import socket
import time
import ubinascii
import urequests

# Configuración de la red WiFi
ssid = "ESP32_Honeypot"
password = "12345678"

# URL del Webhook de Pastebin u otro servicio similar
webhook_url = "https://webhook.site/4cbabbe4-c4ac-4c76-8e2f-c79d55a2fb54"

# Lista de puertos comunes para escaneo básico
puertos_comunes = [80, 443, 5223, 25, 587, 143, 993, 110, 995, 2195, 2196, 123, 53, 445, 548, 389, 5353, 5228, 5229, 5230, 161, 162, 500, 1701, 4500]

# Configuración y activación de la red AP
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA_WPA2_PSK)
ap.active(True)
print("Red WiFi creada:", ssid)

def scan_network():
    # Escaneo de red básico
    print("Escaneando dispositivos conectados...")
    devices = ap.status('stations')

    for device in devices:
        mac = ubinascii.hexlify(device[0], ':').decode()
        nombre_dispositivo = "Nombre no disponible"  # Placeholder para el nombre del dispositivo

        # Intenta obtener el nombre del dispositivo
        try:
            # Este método puede no funcionar en todos los casos
            nombre_dispositivo = socket.gethostbyaddr(device[0])[0]
        except Exception:
            pass

        print(f"Dispositivo conectado - MAC: {mac}, Nombre: {nombre_dispositivo}")

        # Escaneo de puertos en el dispositivo
        puertos_abiertos = []
        for puerto in puertos_comunes:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)  # Tiempo de espera corto para escaneo rápido
                resultado = sock.connect_ex((device[0], puerto))
                
                if resultado == 0:
                    puertos_abiertos.append(puerto)
                
                sock.close()
            except Exception as e:
                print(f"Error escaneando el puerto {puerto} en {mac}: {e}")
        
        # Formatear y enviar datos al Webhook
        datos_dispositivo = {
            "MAC": mac,
            "Nombre": nombre_dispositivo,
            "Puertos_abiertos": puertos_abiertos if puertos_abiertos else "Ninguno"
        }
        
        # Enviar datos al Webhook
        try:
            respuesta = urequests.post(webhook_url, json=datos_dispositivo)
            print("Datos enviados al Webhook:", respuesta.text)
            respuesta.close()
        except Exception as e:
            print(f"Error al enviar al Webhook: {e}")

while True:
    scan_network()
    time.sleep(60)  # Realizar escaneo cada 60 segundos
