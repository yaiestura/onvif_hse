# Key Bindings
# 8 - 56
# 6 - 54
# 4 - 52
# 2 - 50
# + - 43
# - - 45
# * - 42
# / - 47

from onvif import ONVIFCamera
from msvcrt import getch

# Create class for moving PTZ Cam in ContiniousMode using NumPad bindings
class my_ptz():
    def initialize(self, ip, port, username, password):
        global ptz
        print 'IP Camera initialization...'
        mycam = ONVIFCamera(ip, port, username, password)
        print 'Connected to ONVIF Camera ' + ip
        print 'Creating Media service...'
        media = mycam.create_media_service()
        print 'Creating Media service... Done.'
        token = media.GetProfiles()[0]._token
        print 'Creating PTZ service...'
        ptz = mycam.create_ptz_service()
        print 'Creating PTZ service... Done.'
        self.define_requests(token)
    
    # Define necessary requests
    def define_requests(self, token):
        print 'Defining Requests types...'
        global req_move, req_stop, req_goto_home

        req_move = ptz.create_type('ContinuousMove')
        req_move.ProfileToken = token

        req_stop = ptz.create_type('Stop')
        req_stop.ProfileToken = token

        req_goto_home = ptz.create_type('GotoHomePosition')
        req_goto_home.ProfileToken = token

        print 'Defining Requests types... Done.'
        print 'IP Camera initialization... Done.'

    def stop(self):
        ptz.Stop(req_stop)

    def move_left(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = -speed
        req_move.Velocity.PanTilt._y = 0.0
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_right(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = speed
        req_move.Velocity.PanTilt._y = 0.0
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_down(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = 0.0
        req_move.Velocity.PanTilt._y = -speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_up(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = 0.0
        req_move.Velocity.PanTilt._y = speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_right_up(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = speed
        req_move.Velocity.PanTilt._y = speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_left_up(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = -speed
        req_move.Velocity.PanTilt._y = speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_right_down(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = speed
        req_move.Velocity.PanTilt._y = -speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_left_down(self, speed=0.5):
        req_move.Velocity.Zoom._x = 0.0
        req_move.Velocity.PanTilt._x = -speed
        req_move.Velocity.PanTilt._y = -speed
        ptz.ContinuousMove(req_move)
        self.stop()

    def move_home(self):
        ptz.GotoHomePosition(req_goto_home)
   
    def zoom_in(self, speed=0.5):
        self.stop()
        req_move.Velocity.PanTilt._x = 0.0
        req_move.Velocity.PanTilt._y = 0.0
        req_move.Velocity.Zoom._x = speed
        ptz.ContinuousMove(req_move)

    def zoom_out(self, speed=0.5):
        self.stop()
        req_move.Velocity.PanTilt._x = 0.0
        req_move.Velocity.PanTilt._y = 0.0
        req_move.Velocity.Zoom._x = -speed
        ptz.ContinuousMove(req_move)

# Initialize cam, and create an infinite loop to manage Cam actions
cam = my_ptz()
cam.initialize('192.168.11.23', 80, 'admin', 'Supervisor')
while True:
    key = ord(getch())
    speed = 1
    if key == 27: #ESC
        break
    elif key == 56: #Up
        print "Move Up..."
        cam.move_up(speed)
    elif key == 50: #Down
        print "Move Down..."
        cam.move_down(speed)
    elif key == 54: #Right
        print "Move Right..."
        cam.move_right(speed)
    elif key == 52: #Left
        print "Move Left..."
        cam.move_left(speed)
    elif key == 53: #Home
        print "Go to Home Position..."
        cam.move_home()
    elif key == 57: #Right Up
        print "Move Right Up..."
        cam.move_right_up(speed)
    elif key == 55: #Left Up
        print "Move Left Up..."
        cam.move_left_up(speed)
    elif key == 49: #Left Down
        print "Move Left Down..."
        cam.move_left_down(speed)
    elif key == 51: #Right Down
        print "Move Right Down..."
        cam.move_right_down(speed)
    elif key == 43: #Plus(+)
        print "Zoom in..."
        cam.zoom_in(speed)
    elif key == 45: #Minus(-)
        print "Zoom out..."
        cam.zoom_out(speed)
    

