from onvif import ONVIFCamera
from time import sleep

mycam = ONVIFCamera('192.168.11.24', 80 , 'admin', 'Supervisor')

def perform_move(imaging, request):
    imaging.Move(request)
    imaging.Stop({'VideoSourceToken': vstoken})

def move(imaging, request, speed=0.5):
    print 'moving Focus'
    request.Focus.Continuous = {'Speed': speed}
    perform_move(imaging, request)
    perform_move(imaging, request)
    perform_move(imaging, request)
    perform_move(imaging, request)

    

media = mycam.create_media_service()
imaging = mycam.create_imaging_service()
vstoken = media.GetVideoSources()[0]._token
req1 = imaging.GetStatus({'VideoSourceToken': vstoken})
print req1
req2 = imaging.GetMoveOptions({'VideoSourceToken': vstoken})
print req2
request = imaging.create_type('Move')
request.VideoSourceToken = vstoken
imaging.Stop({'VideoSourceToken': vstoken})
focus = imaging.SetImagingSettings({'VideoSourceToken': vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'MANUAL'}}})
print focus
move(imaging, request, +0.9)
sleep(2)
move(imaging, request, +0.9)
req5 = imaging.GetStatus({'VideoSourceToken': vstoken})
print req5
print focus
focus = imaging.SetImagingSettings({'VideoSourceToken': vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})

