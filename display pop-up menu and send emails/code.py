import tkinter
import socket
import sys
import time
import smtplib

class A:
   #creates parent window
   def __init__(self):    
      self.root = tkinter.Tk()
      self.root.geometry('500x500')
      self.frame1 = tkinter.Label(self.root,width = 400,height = 400,bg = '#AAAAAA')
      self.frame1.pack()

   def hey(self,s):
      self.frame1.configure(text = s)

   def run(self,data):
      self.hey(data)
      self.root.after(5000, lambda: self.root.destroy()) # Destroy the widget after 30 seconds
      self.root.mainloop()

if __name__ == '__main__':
    while True:
      a = A()
      HOST = '127.0.0.1' 
      PORT = 5789
      soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
      try:
        soc.bind((HOST, PORT))
      except socket.error as massage:
        print('Bind failed. Error Code : ' + str(massage[0]) + ' Message ' + massage[1])
        sys.exit()
   
      soc.listen(9)
   
      conn, address = soc.accept()
      print('Connected with ' + address[0] + ':' + str(address[1]))

      data = conn.recv(1024).decode()
      soc.close()
      a.run(data)

      ##send email
      gmail_user = "erfanbahrami1999@gmail.com"
      gmail_password = "12erfan%behi$@@"

      try: 
         #Create your SMTP session 
         smtp = smtplib.SMTP('smtp.gmail.com', 587) 

         #Use TLS to add security 
         smtp.starttls() 

         #User Authentication 
         smtp.login("erfanbahrami1999@gmail.com","12erfan%behi$@@")
    
         #Defining The Message 
         message = "Message_you_need_to_send" 
    
         #Sending the Email
         smtp.sendmail("erfanbahrami1999@gmail.com", "erfanbahrami@ec.iut.ac.ir",message) 

         #Terminating the session 
         smtp.quit() 
         print ("Email sent successfully!") 

      except Exception as ex: 
         print("Something went wrong....",ex) 

      if not data:
        break

  
   
