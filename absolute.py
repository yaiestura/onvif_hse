from onvif import ONVIFCamera
from time import sleep

class Test:
	def __init__(self,ip,port,user,passw):
		self.ip = ip
		self.port = port
		self.user = user
		self.passw = passw
		self.cam = ONVIFCamera(self.ip, self.port, self.user, self.passw)
	def AbsoluteMoveSupport(self):
		media = self.cam.create_media_service() #Creating media service
		profiles = media.GetProfiles()[0]
		token = media.GetProfiles()[0]._token          # Getting token from the first protile, we'll need it soon
		ptz = self.cam.create_ptz_service()	#Creating ptz service
		ptz_token = profiles.PTZConfiguration._token
		ptz.create_type("AbsoluteMove")
		
		try:
			pos = ptz.GetStatus({"ProfileToken": token}).Position # getting current position
			# print pos
			x = pos.PanTilt._x
			y = pos.PanTilt._y
			if ((x + 0.1) < 1):   #checking if x max or min, so we decrease or increase the number
				x1 = x + 0.1
			else:
				x1 = x - 0.1
			if ((y + 0.1) < 1):   #checking if y max or min, so we decrease or increase the number
				y1 = y + 0.1
			else:
				y1 = y - 0.1
			ptz.AbsoluteMove({"ProfileToken": token, "Position":{"PanTilt":{"_x": x1,"_y": y1}}}) #AbsoluteMove to new parameter x1
			sleep(3) 																								  #Wait for camera to move
			pos = ptz.GetStatus({"ProfileToken": token}).Position               									  #Getting new position
			x = pos.PanTilt._x
			y = pos.PanTilt._y
			print x1 - x, y1 - y
			if (((x1 - x) == 0) & ((y1 - y) == 0)):								              #Checking, if camera moved
				return 'AbsoluteMove is supported, current coordinates: ' +  str(x1) + ' ' + str(y)
			else:
				return 'AbsoluteMove is not supported, it does not follow AbsoluteMove instructions'
		except AttributeError:
			return 'AbsoluteMove is not supported, AttributeError'


Inst = Test('192.168.11.12', 80, 'admin', 'Supervisor')
print Inst.AbsoluteMoveSupport()