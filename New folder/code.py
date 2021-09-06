import tkinter
import socket
import sys
import smtplib
 

if __name__ == '__main__':
   HOST = '127.0.0.1' 
   PORT = 5789

   while True:
      a = tkinter.Tk()
      a.geometry('350x350')
      a.frame1 = tkinter.Label(a,width = 400,height = 400,bg = '#AAAAAA')
      a.frame1.pack() 
      soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
      try:
         soc.bind((HOST, PORT))
       
      except socket.error as massage:
         print('Bind failed. Error Code : ' + str(massage[0]) + ' Message ' + massage[1])
         sys.exit()
          
      print('Socket binding operation completed')
   
      soc.listen(9)
   
      conn, address = soc.accept()
      print('Connected with ' + address[0] + ':' + str(address[1]))

   
      data = conn.recv(1024).decode()
      soc.close()
      a.frame1.configure(text = data)
      a.after(10000, lambda: a.destroy())
      a.mainloop()

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

  

   


  
  
