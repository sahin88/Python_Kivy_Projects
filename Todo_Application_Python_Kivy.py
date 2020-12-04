import kivy
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.screenmanager import ScreenManager ,Screen 
from kivy.uix.button import Button 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.theming import ThemeManager
from kivy.uix.gridlayout import GridLayout #NDIconLabel
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.picker import MDDatePicker,MDTimePicker	

from kivymd.uix.label import MDLabel
from kivymd.uix.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem, ThreeLineListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivy.properties import ObjectProperty, StringProperty

from kivymd.uix.list import  MDList
from kivymd.uix.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView
from kivymd.uix.toolbar import MDBottomAppBar


Builder.load_string("""
#:import MDLabel kivymd.uix.label.MDLabel
#:import MDTextFieldRound kivymd.uix.textfield.MDTextFieldRound
#:import MDBottomAppBar kivymd.uix.toolbar.MDBottomAppBar
#:import MDRaisedButton kivymd.uix.button.MDRaisedButton
#:import NavigationLayout kivymd.uix.navigationdrawer.NavigationLayout
#:import MDNavigationDrawer kivymd.uix.navigationdrawer.MDNavigationDrawer

#:import NDIconLabel kivymd.uix.navigationdrawer.NDIconLabel
#:import OneLineIconListItem kivymd.uix.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.uix.list.OneLineAvatarIconListItem
#:import OneLineIconListItem kivymd.uix.list.TwoLineListItem
#:import MDToolbar kivymd.uix.toolbar.MDToolbar




<ScreenManagement>:
	MainWindow:
		name:'first'	
	SecondWindow:
		name:'second'

<MainWindow>:
	plus_button:plus_button
	text_input_one:text_input_one
	list_flat:list_flat
	text_input:text_input
	time_input:time_input
	toolba:toolba
	bittik:bittik
	NavigationLayout:
		MDNavigationDrawer:
			anim_type:'slide_above_simple'
			drawer_logo:'/home/alex/crash_course_kivy/einstein.jpg'
			
			NavigationDrawerSubheader:
				text:'cool menu'
			NavigationDrawerIconButton:
				icon:'lock'
				text:'this is this'
				on_release:
					print('clicked')
			NavigationDrawerIconButton:
			    icon: 'email'
			    text: 'sahinmuratogur@gmail.com'
       
     

		FloatLayout:
			id:bittik

			
			ScrollView:
			
				FloatLayout:
					id:list_flat
					
					size_hint_y :None
					height:800
					

			OneLineListItem:
				text:'Date'
				font_size:6
				pos_hint:{'x':0, 'top':.77}
				size_hint:(.25, None)
		
			MDIconButton:
		    	icon:'calendar'

		    	font_size:9
		    	pos_hint:{'x':.2,'top':.77}
		    	size_hint:(.40, None)
		    	on_release:root.date_picker() 

		    MDTextField:
		    	id:text_input
		    	text:''
		    	font_size:18
		    	multinline:'False'
		    	size_hint:(.29,None)
		    	pos_hint:{'x':0,'top':.70}
		    OneLineListItem:
				text:'Time'
				font_size:12
				pos_hint:{'x':.48, 'top':.77}
				size_hint:(.25, None)
			MDIconButton:  
		    	icon:'clock'
		    	text:'Time'
		    	pos_hint:{'x':.64,'top':.77}
		    	size_hint:(.4, None)
		    	on_release:root.time_picker()
		    MDTextField:
		    	id:time_input
		    	text:''
		    	multinline:'False'
		    	size_hint:(.26,None)
		    	pos_hint:{'x':.47,'top':.70}
			MDToolbar:
				id:toolba
				title:'Deep Learning'+'\\n'+'ToDoApp'
				md_bg_color:app.theme_cls.primary_color	
				right_action_items:[["dots-vertical", lambda x:x]]
				elevation: 6
				pos_hint:{'x':0,'top':1}
				size_hint:(1,None)

			MDTextFieldRound:
				id:text_input_one
				_outline_color:app.theme_cls.primary_color
				icon:'plus_button'
				pos_hint:{'x':.0,'top':.88}
				size_hint:(1, None)
				hint_text:'Please enter an activity!'
				background_color: 1,1,0,1
				cursor_color: 0,1,0,1
				foreground_color:0,0,0,1
				focus:True

		    MDIconButton:
		    	id:plus_button
		    	icon:'plus'
		    	pos_hint:{'x':.87,'top':.88}
		    	md_bg_color:app.theme_cls.primary_color
		    	on_release:root.add_button()


<SecondWindow>:
	MDRaisedButton:
		text:'go back'
		on_release:
			app.root.current='first'
			root.manager.transition.direction ='right'

""")


class SecondWindow(Screen):
	print(dir(App))

	pass

class ScreenManagement(ScreenManager):
	pass
	

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class MainWindow(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		halley=ObjectProperty(None)
		self.first_l=[]
		
		self.second=[]
		self.add_widget( MDBottomAppBar(md_bg_color=TodoApp().theme_cls.primary_color,left_action_items=
            [['email', lambda x: x],
             ['facebook', lambda x: x],
            ['whatsapp', lambda x: x],
            ['instagram', lambda x: x]],anchor='right'))


	def add_button(self):


			
		for i in  range(len(self.second)+1):


			three_line="three_line_"+str(i)
			del_btn="del_btn_"+str(i)
			check_btn="check_btn_"+str(i)
			updt_btn="update_btn_"+str(i)
			n=.7
			y1=.08
			y=.15

			three_line=ThreeLineListItem(id=three_line, pos_hint={'x':0,'top':n-0.13*len(self.first_l)},size_hint=(.4, .01),
				text= self.text_input_one.text, secondary_text=self.text_input.text+'\n'+self.time_input.text)
			#b=IconLeftSampleWidget(icon='check-circle')
			del_btn=MDIconButton(id=del_btn,icon='delete',pos_hint={'x':.65,'top':n-0.13*len(self.first_l)},
				    	size_hint=(.15, y))
			del_btn.bind(on_release=self.delete_btn)
			check_btn=MDIconButton(id=check_btn,icon='check-circle',pos_hint={'x':.75,'top':n-0.13*len(self.first_l)},
				    	size_hint=(.15, y))
			updt_btn=MDIconButton(id=updt_btn,icon='update',pos_hint={'x':.85,'top':n-0.13*len(self.first_l)},
				    	size_hint=(.15, y))
			updt_btn.bind(on_press= self.change_page)

			check_btn.bind(on_release=self.change_check_btn)
			#print(del_btn.id)
			
			
			if i==len(self.first_l):
				for k in range(1):
					self.third=[]
					self.third.append(three_line)
					self.third.append(del_btn)
					self.third.append(check_btn)
					self.third.append(updt_btn)
					#self.ids.list_flat.add_widget(three_line)
					#self.ids.list_flat.add_widget(del_btn)
					#self.ids.list_flat.add_widget(check_btn)
					#self.ids.list_flat.add_widget(updt_btn)
				self.second.append(self.third)
				#self.first_l.append(i)
				self.text_input.text=''
				self.time_input.text=''
				self.text_input_one.text=''
				self.update_widget()
         

			    
	def delete_btn(self, instance):

	
		l=instance.id.split('_')

		for m in self.second:
			if m[1].id==instance.id:
				for teta in m:
					self.ids.list_flat.remove_widget(teta)
				
				self.second.remove(m)
		self.update_widget()

	def update_widget(self):
		self.ids.list_flat.clear_widgets()
		
		w=0
		for j in self.second:
			w +=1
			for k in j:
				k.pos_hint['top']= .6-0.13*w
			
				self.ids.list_flat.add_widget(k)	
		

		
		
	def change_check_btn(self, instance):
		if instance.icon =="check-circle-outline":
			instance.icon='check-circle'
		else:
			instance.icon ='check-circle-outline'

	def date_picker(self, *args):
		MDDatePicker(self.set_previous_date).open()

	def set_previous_date(self, date_obj):
		self.text_input.text = ' '+str(date_obj)

	def time_picker(self,*args):
		tm_dia=MDTimePicker()
		tm_dia.bind(time=self.get_time)
		tm_dia.open()
		

	def get_time(self,instance, time):
		self.time_input.text='    '+str(time)[:5]

	def change_page(self,*args):
		
		self.manager.current='second'
		self.manager.transition.direction ='left'


class TodoApp(App):
	theme_cls=ThemeManager()
	theme_cls.primary_palette='DeepOrange'
	theme_cls.theme_style='Light'
	theme_cls.accent_platte='Blue'
	Window.keyboard_anim_args={'d':.2,'t':'in_out_expo'}
	Window.softinput_mode="below_target"

	def build(self):
		Window.size=(360,640)

		return ScreenManagement()

if __name__ == '__main__':
	app=TodoApp()
	app.run()