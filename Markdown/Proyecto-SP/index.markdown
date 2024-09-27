---
title: Presentación sobre Actuadores
layout: slide
permalink: /actuadores/
theme: moon

slides:
  - title: Introducción
    slide-data: |
      Los actuadores son dispositivos fundamentales en sistemas automáticos que convierten diversas formas de energía en movimiento. Se utilizan en robótica, maquinaria industrial, automatización de procesos y más.

  - title: Tipos de Actuadores
    slide-data: |
      Dependiendo de su funcionamiento y la energía que utilizan, los actuadores se clasifican en varios tipos:
      - **Actuadores Eléctricos**
      - **Actuadores Mecánicos**
      - **Actuadores Hidráulicos**

  - title: 1. Actuadores Eléctricos
    slide-data: |
      ## Tipos
      - **Motores Eléctricos**:
        - **Motores de corriente continua (DC)**: Control preciso de la velocidad.
        - **Motores de corriente alterna (AC)**: Operación constante.
        - **Servomotores**: Control de posición preciso.
      - **Solenoides**: Dispositivos electromagnéticos para movimiento lineal.

  - title: Funcionamiento de Actuadores Eléctricos
    slide-data: |
      1. **Inyección de Energía**: Aplicación de corriente eléctrica genera un campo magnético.
      2. **Interacción Magnética**: Movimiento rotativo o lineal según el dispositivo.
      3. **Control de Velocidad y Posición**: Ajuste de movimientos mediante controladores.
      4. **Detección de Posición**: Sensores para medir la posición en tiempo real.

  - title: Características de Actuadores Eléctricos
    slide-data: |
      - **Precisión**
      - **Facilidad de Control**
      - **Eficiencia Energética**
      - **Dependencia de Fuente de Energía**

  - title: Modo de Comunicación de Actuadores Eléctricos
    slide-data: |
      - **Protocolos de Comunicación**: I2C, SPI, RS-232, CAN.

  - title: 2. Actuadores Mecánicos
    slide-data: |
      ## Tipos
      - **Engranajes**: Transmiten movimiento y fuerza.
      - **Cilindros de Desplazamiento**: Mueven objetos mediante mecanismos de palanca.
      - **Accionadores de Tornillo**: Transforman movimiento rotativo en lineal.

  - title: Funcionamiento de Actuadores Mecánicos
    slide-data: |
      1. **Transmisión de Fuerza**: Componentes mecánicos transmiten fuerza.
      2. **Conversión de Movimiento**: Movimiento rotativo a lineal.
      3. **Control Manual o Automático**: Operación manual o automática.
      4. **Robustez y Durabilidad**: Soportan condiciones adversas.

  - title: Características de Actuadores Mecánicos
    slide-data: |
      - **Robustez**
      - **No Requieren Energía Eléctrica**
      - **Bajo Costo**

  - title: Modo de Comunicación de Actuadores Mecánicos
    slide-data: |
      - **Manual**: Control manual sin comunicación electrónica.

  - title: 3. Actuadores Hidráulicos
    slide-data: |
      ## Tipos
      - **Cilindros Hidráulicos**: Movimiento lineal mediante presión de fluido.
      - **Motores Hidráulicos**: Movimiento rotativo con alto torque.
      - **Válvulas Hidráulicas**: Controlan el flujo del fluido.

  - title: Funcionamiento de Actuadores Hidráulicos
    slide-data: |
      1. **Generación de Presión**: Motor acciona bomba hidráulica.
      2. **Transferencia de Fluido**: Fluido presurizado se dirige a cilindro o motor.
      3. **Movimiento del Pistón**: Presión genera movimiento.
      4. **Control de Movimiento**: Regulación de flujo con válvulas.
      5. **Retorno del Fluido**: Completa el ciclo de funcionamiento.

  - title: Características de Actuadores Hidráulicos
    slide-data: |
      - **Alta Fuerza**
      - **Control Preciso**
      - **Requieren Mantenimiento**

  - title: Modo de Comunicación de Actuadores Hidráulicos
    slide-data: |
      - **Control por Válvulas**: Válvulas hidráulicas regulan el flujo.
---

{% for slide in page.slides %}
<section data-background="{% if slide.background %}{{slide.background}}{% else %}{{page.background}}{% endif %}">
  <h1>{{slide.title}}</h1>
  {{ slide.slide-data }}
</section>
{% endfor %}
