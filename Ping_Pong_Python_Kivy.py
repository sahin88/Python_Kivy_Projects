import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle, Ellipse
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.core.window import Window
import time
from kivy.core.audio import SoundLoader





class layout(Widget):
	def __init__(self,**kwargs):

		super().__init__(*kwargs)


		with self.canvas:

			Color(1,1,1,1)
			self.player_1=Ellipse(pos=(400, 400),size=(50,50))
			self.x=+10
			Color(1,1,1,1)
			self.kutuk=Rectangle(pos=(0, Window.height/2),size=(20,125))


			Color(1,1,1,1)

			self.pl=Rectangle(pos=(Window.width-20, Window.height/2),size=(20,125))
			self.sabit=5
			self.sabitt=10
			print(self.sabit)

		Clock.schedule_interval(self.motion,1/60.)

		
		self.sound=SoundLoader.load('/home/alex/Downloads/mpp.wav')
		self.sound.play()
		self._keyboard=Window.request_keyboard(self._on_keyboard_down,self)
		self._keyboard.bind(on_key_down=self.on_key_down)

	def _on_keyboard_down(self):
		self._keyboard.unbind(on_key_down=on_key_down)
		self._keyboard=None

	def on_key_down(self, keyboard,keycode,text,modifiers):
		curx=self.pl.pos[0]
		cury=self.pl.pos[1]

		if text=='p' :
			newx=curx
			newy=cury+35
		if text=='m':
			newx=curx
			newy=cury-35

		self.pl.pos=(newx,newy)



		




		

	def motion(self,*args):
        

		c1=self.player_1.pos[0]
		c2=self.player_1.pos[1]

		c1=c1+self.sabit
		c2=c2+self.sabitt
		

		#print(c1)
		if(c2>float(Window.height)):
			self.sabitt = -self.sabitt
		if(c2<0):
			self.sabitt = -self.sabitt


		if (c1 >float(Window.width-20)) or c1<0:
			self.sabit = -self.sabit


		self.player_1.pos=(c1,c2)







class MyApp(App):
	def build(self):
		return layout()

if __name__ == '__main__':
	MyApp().run()
