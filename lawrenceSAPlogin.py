import pyautogui
class SapLogon(object):

    def __init__(self,user,password,instance):
	    self.uid = user
	    self.pid = password
	    self.instance = inst

    def activate_pre_invoke(self):
	    pyautogui.hotkey('win','d') 

    def activate_saplogon(self):
	       pyautogui.hotkey('win','r')
	       pyautogui.typewrite('saplogon')
	       pyautogui.press('enter')   

    def activeate_post_invoke(self):
	       pyautogui.hotkey('win','up')

	def open-instance(self):
		try:
		   pyautogui.hotkey('ctrl','f')
		   pyautogui.typewrite(self.instance)
		   pyautogui.press('enter')
		   return True
		except:
		   return False

	def	SapLogin(self)
	       pyautogui.typewrite(self.uid)
	       pyautogui.press('tab')
	       pyautogui.typewrite(self.pid)
	       pyautogui.press('enter')

###############################################################3
import time

if __name__ == '__main__':
	    mysap = saplogon('user','password','DCP')
	    mysap.activate_pre_invoke()
	    time.sleep(2)	
	    mysap.activate_SapLogon()
	    time.sleep(5)	
	    mysap.activate_post_invoke()
	    time.sleep(2)	
	    mysap.open_instance()
	    time.sleep(5)	
	    mysap.SapLogon()
	    time.sleep(3)
	    pyautogui.press('enter')      

  
