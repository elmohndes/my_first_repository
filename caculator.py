import tkinter as tk
import parser

class Caculator:
 def __init__(self):
	self.root = tk.Tk()
	self.root.title("Calculator")
	self.display = tk.Entry(self.root, font = ('calibri', 25))
	self.display.grid(row = 0, columnspan = 7, sticky = tk.W + tk.E)
	self.var = len(self.display.get())

 def numbers(self):
       	button0 = tk.Button(self.root, text = "0", command = lambda:self.funButton(0))
	button1 = tk.Button(self.root, text = "1", command = lambda:self.funButton(1))
       	button2 = tk.Button(self.root, text = "2", command = lambda:self.funButton(2))
       	button3 = tk.Button(self.root, text = "3", command = lambda:self.funButton(3))
       	button4 = tk.Button(self.root, text = "4", command = lambda:self.funButton(4))
       	button5 = tk.Button(self.root, text = "5", command = lambda:self.funButton(5))
       	button6 = tk.Button(self.root, text = "6", command = lambda:self.funButton(6))
       	button7 = tk.Button(self.root, text = "7", command = lambda:self.funButton(7))
       	button8 = tk.Button(self.root, text = "8", command = lambda:self.funButton(8))
	button9 = tk.Button(self.root, text = "9", command = lambda:self.funButton(9))

	button0.grid(row = 5,column = 0, sticky = tk.W + tk.E)
	button1.grid(row = 2, column = 0, sticky = tk.W + tk.E)
	button2.grid(row = 2, column = 1, sticky = tk.W + tk.E)
	button3.grid(row = 2, column = 2, sticky = tk.W + tk.E)
	button4.grid(row = 3, column = 0, sticky = tk.W + tk.E)
	button5.grid(row = 3, column = 1, sticky = tk.W + tk.E)
	button6.grid(row = 3, column = 2, sticky = tk.W + tk.E)
	button7.grid(row = 4, column = 0, sticky = tk.W + tk.E)
	button8.grid(row = 4, column = 1, sticky = tk.W + tk.E)
	button9.grid(row = 4, column = 2, sticky = tk.W + tk.E)

 def operations(self):
	add = tk.Button(self.root, text = "+", command = lambda:self.do_operations('+'))
	sub = tk.Button(self.root, text = "-", command = lambda:self.do_operations('-'))
	mul = tk.Button(self.root, text = "*", command = lambda:self.do_operations('*'))
	div = tk.Button(self.root, text = "/", command = lambda:self.do_operations('/'))
	cal = tk.Button(self.root, text = "=", command = self.get_result)
	clear = tk.Button(self.root, text = "clear", command = self.clear_all)

	add.grid(row = 2, column = 4, sticky = tk.E + tk.W)
	sub.grid(row = 2, column = 5, sticky = tk.E + tk.W)
	mul.grid(row = 3, column = 4, sticky = tk.E + tk.W)
	div.grid(row = 3, column = 5, sticky = tk.E + tk.W)
	cal.grid(row = 4, column = 5, sticky = tk.E + tk.W)
	clear.grid(row = 4, column = 4, sticky = tk.E + tk.W)

 def clear_all(self):
	self.display.delete(0, tk.END)
	self.var = 0

 def funButton(self,i):
	self.display.insert(self.var,i)
	self.var += 1

 def do_operations(self, sign):
	self.display.insert(self.var, sign)
	self.var += 1

 def get_result(self):
       	 whole_string = self.display.get()
#	try:
	 formula = parser.expr(whole_string).compile()
	 result = eval(formula)
	 self.clear_all()
	 self.display.insert(0,result)
	 self.var = len(str(result))
#	except Exception:
#	 self.clear_all()
#	 self.display.insert(0, "Error")

 def run(self):
	self.root.mainloop()


object = Caculator()
object.numbers()
object.operations()
object.run()
