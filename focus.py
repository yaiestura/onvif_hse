from onvif import ONVIFCamera
from time import sleep

# Connected to 24 camera on 11th network
mycam = ONVIFCamera('192.168.11.24', 80 , 'admin', 'Supervisor')

# Function to perform continuous focus move
def perform_move(imaging, request):
    imaging.Move(request)
    imaging.Stop({'VideoSourceToken': vstoken})

# Function to move focus, accepts speed/position as a parameter
def move(imaging, request, speed=0.5):
    print 'moving Focus'
    request.Focus.Continuous = {'Speed': speed}
    perform_move(imaging, request)
    perform_move(imaging, request)
    perform_move(imaging, request)
    perform_move(imaging, request)

# Create imaging and media services
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()

# Access camera VideoSource token
vstoken = media.GetVideoSources()[0]._token

# Request aand retreive camera initial focus status and MoveOptions; Create request type for Move option
req1 = imaging.GetStatus({'VideoSourceToken': vstoken})
print req1
req2 = imaging.GetMoveOptions({'VideoSourceToken': vstoken})
print req2
request = imaging.create_type('Move')
request.VideoSourceToken = vstoken
imaging.Stop({'VideoSourceToken': vstoken})

# Set FocusMode to Manual in order to Manually manage lens focus parameters
focus = imaging.SetImagingSettings({'VideoSourceToken': vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'MANUAL'}}})
print focus

# Move focus in two supported directions - positive and negative with speed eq 0.9 respectively
move(imaging, request, -0.9)
sleep(2)
move(imaging, request, +0.9)

# Get camera Focus state and position after movements
req5 = imaging.GetStatus({'VideoSourceToken': vstoken})
print req5

# Set FocusMode to default state - AUTO
focus = imaging.SetImagingSettings({'VideoSourceToken': vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
