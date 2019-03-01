from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.11.12', 80, 'admin', 'Supervisor')
media = mycam.create_media_service()

# Create ptz service object
ptz = mycam.create_ptz_service()

# Get target profile
media_profile = media.GetProfiles()[0]

request = ptz.create_type('AbsoluteMove')
request.ProfileToken = media_profile._token
print ptz.GetStatus({"ProfileToken": media.GetProfiles()[0]._token})
request.Position.PanTilt = {'_x': 0.68, '_y': -0.5}
request.Position.Zoom = {'_x': 0.9}
ptz.AbsoluteMove(request)
print ptz.GetStatus({"ProfileToken": media.GetProfiles()[0]._token})
