from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import socket
from threading import Thread
from time import sleep
import sys

helptext = """
/help
/key
/???
/calc - /calc money koef
"""
key = "MaskXyiSosi"

			
		


class Bot():
	token = "5162301869:AAHMTfqUDp49vOgkKgOb_l4KkNHN-mfqUSw"

	def __init__(self):
		print("The bot is running. Press Ctrl+C to finish")
		server = Server()
		updater = Updater(self.token, use_context=True)
		dispatcher = updater.dispatcher
		dispatcher.add_handler(CommandHandler("start", self.on_start))
		dispatcher.add_handler(MessageHandler(Filters.all, self.on_message))
		updater.start_polling()
		updater.idle()

	def on_start(self,update, context):
		chat = update.effective_chat
		context.bot.send_message(chat_id=chat.id, text="Привет, напиши /help")

	def on_message(self,update, context):
		#context.bot.send_message(chat_id=chat.id, text=message)
		chat = update.effective_chat
		self.text = update.message.text
		if self.text == "/help":
			context.bot.send_message(chat_id=chat.id, text=helptext)
		elif self.text == "/key":
			context.bot.send_message(chat_id=chat.id, text=key)
		elif self.text == "/???":
			context.bot.send_message(chat_id=chat.id, text=self.vopros())
		elif self.text.split()[0] == "/calc":
			context.bot.send_message(chat_id=chat.id, text=self.kalkulate())

	def vopros(self):
		a = ""
		b = 1000
		while b > 7:
			a += str(b) + " - 7 = " + str(b-7) + "\n"
			b-= 7
		return a

	def kalkulate(self):
		if len(self.text.split()) < 3:
			return "Error. Print /calc money kef"
		text_otvet ="Кеф|Ставка|Профит1|Профит2|  %  |\n"
		text_otvet += self.print_kef(int(self.text.split()[2]),int(self.text.split()[1]),1)
		text_otvet += self.print_kef(int(self.text.split()[2]),int(self.text.split()[1]),0.95)
		text_otvet += self.print_kef(int(self.text.split()[2]),int(self.text.split()[1]),0.9)
		text_otvet += self.print_kef(int(self.text.split()[2]),int(self.text.split()[1]),0.85)
		return text_otvet
		
	def print_kef(self,kef1,stavka1,koef):
        
                kef2 = round(stavka1 / ((kef1-1)*stavka1 * koef) + 1.005,2)
                str_line = "{:4.4}|".format(str(kef2)) 

                stavka2 = (stavka1 * (kef1 - 1) + stavka1) / kef2
                profit1 = round((kef1-1)*stavka1 - stavka2)
                profit2 = stavka2 * (kef2 - 1) - stavka1    
                procent = (profit1 + profit2) / (stavka1 + stavka2)* 100
        
                str_line += '{:6.6}|{:7.7}|{:7.7}|{:5.5}'.format(str(stavka2), str(profit1), str(profit2), str(procent))
                return str_line + "\n"


class Server():

	def __init__(self):
		self.potoki = []
		print("The bot is running. Type 0 to exit")
		self.serv_sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
		self.serv_sock_send.bind(('', 53220))
		self.serv_sock_send.listen(10)
		Thread(target= self.main).start()

	def Exit(self):
		while True:
			if(input() == 0):
				sys.exit


	def xz(self,client_sock_send,asdb):
		while True:
			data = ""
			while True:
				data = client_sock_send.recv(1024)
				if(len(data) != 0):
					break
			
			client_sock_send.sendall(str.encode("11111" ,  encoding='utf-8'))
			
	
	def main(self):
		th = Thread(target=self.Exit, args = ())
		th.start()     
		while True:
			client_sock_send, client_addr_send = self.serv_sock_send.accept()
			print('Connected by', client_addr_send)
			th = Thread(target=self.xz, args = (client_sock_send,client_addr_send,))
			th.start()        
			self.potoki.append(th)     
			
			for i in self.potoki:
				if(not i.isAlive):
					del i
					print("del")

	
if __name__ == "__main__":
	target = Bot()
	
    