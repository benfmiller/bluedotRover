# bluedotRover
Blue Dot controller for Rover

## Service Files

To implement a service file, link the service file with "ln -s" into /etc/systemd/system , run systemctl daemon-reload, and start/enable the service. These allow the rover to automatically start the camera stream, rover controller, and twilio texter services at boot and restart them when they fail. The twilio texter just texts my phone the ip address of the raspberry pi in case I need to access it through ssh. I also set up VNC connect for convenience.

## Camera Stream

To see the original camera folder GH page, go to [https://github.com/EbenKouao/pi-camera-stream-flask](https://github.com/EbenKouao/pi-camera-stream-flask). This streams the output from the raspberry pi camera over wifi on port 5000. The camera I got is also capable of auto-switching to infrared when the lighting is low. The camera was not implemented in the final build.

## Controller Interface

The rover controller interface uses the android bluedot app. I found this to be truly wonderful. I was planning on implementing a flask app to communicate with the rover, but the bluedot app was signficantly niftier to use. [Bluedot](https://bluedot.readthedocs.io/en/latest/index.html).

A pea spreader is set up on the rover which is controlled by the left blue dot.

Photos will be up shortly.
