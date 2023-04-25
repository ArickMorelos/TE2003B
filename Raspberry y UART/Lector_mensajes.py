import serial //importa la librería serial dentro del codigo
s=serial.Serial("/dev/ttyACM0",9600)  //se establece el puerto UART de donde se tomaran los datos desde la Arduino hacia la Raspeberry
print (s.name) 
for i in range (7):  //imprime los siete mensajes que escribimos
    x=s.read(s)
    print (x)
s.close()
