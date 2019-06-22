import cherrypy
import serial
import sys
import time

class Server():
    @cherrypy.expose
    def index(self, x, y):
        self.x = list(str(x))
        self.y = list(str(y))

        print(self.x, self.y)
        
        # In this part you have to figure out how to connect your Rasperry to your Arduino through a serial port, it's very boring good luck.
        # In my case it worked by plugging the Arduino to the Raspberry in its USB port and the port seems to be called "ttyACM0"
        # you could try to do the same but it's easier to check out your name.
        self.ser = serial.Serial("/dev/" + sys.argv[1], 9600) # ttyACM0

        for i in range(3):
            self.send(x[i])

        time.sleep(0.001)

        for i in range(3):
            self.send(y[i])

    def send(self, src):
        self.ser.write(src.encode())

def main():
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.quickstart(Server())

if __name__ == "__main__":
    main()
