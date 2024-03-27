from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

# ---- Variables para el Sensor Ultrasónico ---
# Variable para Trigger
trigger = Pin(15, Pin.OUT)

# Variable para Echo
echo = Pin(14, Pin.IN)

# Variable "distancia"
distancia = 0

# ---- Variables para la Pantalla LED I2C ---
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

# Variable para encontrar la dirección de la pantalla
direccion = i2c.scan()[0]

# Variable para 2 filas y 16 columnas de la pantalla
lcd = I2cLcd(i2c,direccion,2,16)

while True:
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()

    while echo.value() == 0:
        inicio = utime.ticks_us()
    while echo.value() == 1:
        final = utime.ticks_us()

    # Calcula la distancia del objeto al sensor
    duracion = final - inicio
    distancia = (duracion * 0.0343) / 2
    print("Distancia: {:0.1f} centimetros".format(distancia))
    lcd.putstr("Distancia: {:0.1f} centimetros".format(distancia))
    utime.sleep(2) # Medición en cada 3 segundos
    lcd.clear() #Limpia la pantalla
