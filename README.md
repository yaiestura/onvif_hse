# ONVIF Practice Codesheet HSE

- Description:

Higher School of Economics Network Video Technologies practice course code, including stuff from basic ONVIF requests such as PTZ camera move, lens focus move to more advanced projects with OpenCV, VideoAnalytics and ImageMagick.
Request to ONVIF devices is processed using [Python2.7 ONVIF library](https://github.com/quatanium/python-onvif), for Python3 use [onvif-zeep library](https://github.com/FalkTannhaeuser/python-onvif-zeep).


# ONVIF Practice #1
In the words of Jack Jansen(the maintainer of MacPython):

> Python is a truly wonderful language. When somebody comes up with a good idea it takes about 1 minute and five lines to program something that almost does what you want. Then it takes only an hour to extend the script to 300 lines, after which it still does almost what you want.

- ## Useful resources

- [ONVIF Standart](https://www.onvif.org/)
- [Devicemgmt Service Description](https://www.onvif.org/ver10/device/wsdl/devicemgmt.wsdl)
- [Media Service Description](https://www.onvif.org/ver10/media/wsdl/media.wsdl)
- [Imaging Service Description](https://www.onvif.org/ver20/imaging/wsdl/imaging.wsdl)

- ## [demo.py](https://github.com/yaiestura/onvif_hse/blob/master/demo.py)
This script allows to retreive ONVIF IP-camera PTZ Configurations, Supported PTZ Spaces including their Pan, Tilt, Zoom (Min, Max) ranges and retreive Media Profile and its configuration tokens.
- ## [absolute.py](https://github.com/yaiestura/onvif_hse/blob/master/absolute.py)
A script created to decide if an ONVIF IP-Camera supports Absolute PTZ Move option(camera takes PTZ Vector(Pan, Tilt, Zoom) and Speed(an optional) as arguments. The test is based on PTZ Service: GetStatus and AbsoluteMove functions.
- ## [abs_move.py](https://github.com/yaiestura/onvif_hse/blob/master/abs_move.py)
This is a naive solution to move an IP-Camera with an Absolute Move feature. In order to move AbsoluteMove type request is created and request. Position takes PanTilt or Zoom dictionary mapping as a parameter.
- ## [ptz_control.py](https://github.com/yaiestura/onvif_hse/blob/master/ptz_control.py)
A script to Move camera in Continious Mode, using keyboard NumPad bindings to move, zoom camera and GoToHomePosition.
- ## [focus.py](https://github.com/yaiestura/onvif_hse/blob/master/focus.py)
A naive solution to move IP-camera's lens focus in Continuous Mode, AbsoluteMove in 90% of used devices is not supported, and Move GetStatus command is usually returns 0.0 value.
