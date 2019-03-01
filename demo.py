from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.11.24', 80, 'admin', 'Supervisor')

media = mycam.create_media_service()
ptz = mycam.create_ptz_service()
token = media.GetProfiles()[0]._token
ptoken = media.GetProfiles()[0].PTZConfiguration._token
print ptz.GetConfiguration({"PTZConfigurationToken": ptoken})
print ptz.GetConfigurationOptions({"ConfigurationToken": token})

profile = media.GetProfiles()[0]
print profile

#ProfileToken
try:
    print "Profile Token: " + profile._token
except:
    print "Couldn't access token, ProfileToken"
#VideoSourceConfigurationToken
try:
    print "Video Source Configuration Token: " + profile.VideoSourceConfiguration._token
except:
    print "Couldn't access token, VideoSourceConfigurationToken"
#AudioSourceConfigurationToken
try:
    print "Audio Source Configuration Token: " + profile.AudioSourceConfiguration._token
except:
    print "Couldn't access token, AudioSourceConfigurationToken"
#VideoEncoderConfigurationToken
try:
    print "Video Encoder Configuration Token: " + profile.VideoEncoderConfiguration._token
except:
    print "Couldn't access token, VideoEncoderConfigurationToken"
#AudioEncoderConfigurationToken
try:
    print "Audio Encoder Configuration Token: " + profile.AudioEncoderConfiguration._token
except:
    print "Couldn't access token, AudioEncoderConfigurationToken"
#VideoAnalyticsConfigurationToken
try:
    print "Video Analytics Configuration Token: " + profile.VideoAnalyticsConfiguration._token
except:
    print "Couldn't access token, VideoAnalyticsConfigurationToken"
#PTZConfigurationToken
try:
    print "PTZ Configuration Token: " + profile.PTZConfiguration._token
except:
    print "Couldn't access token, PTZConfigurationToken"
#MetadataConfigurationToken
try:
    print "Metadata Configuration Token: " + profile.MetadataConfiguration._token
except:
    print "Couldn't access token, MetadataConfigurationToken"
#AudioOutputConfigurationToken
try:
    print "Extension: Audio Output Configuration Token: " + profile.Extension.AudioOutputConfiguration[0]._token
except:
    print "Couldn't access token, AudioOutputConfigurationToken"
#AudioDecoderConfiguration Token
try:
    print "Extension: Audio Decoder Configuration Token: " + profile.Extension.AudioDecoderConfiguration [0]._token
except:
    print "Couldn't access token, AudioDecoderConfigurationToken"
