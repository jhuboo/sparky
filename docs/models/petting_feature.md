## Petting Feature for Robot

### Things Needed
- Robot obviously with everything that Sparky already has so far
- Camera
- Trained ML models that can be used to detect a human in front of the robot
- Ultrasonic sensor to detect hand motion over the robot
- Some kind of sensor that senses that the hand is static OR moving (aka petting)
- LCD screen for face
- Speaker

## Basic Overview of how to implement it
- How to access hand position (petting vs other motion)
- How do we want robot to respond?
- Any potential difficulties that might arise

- Detect hand motion back and forth
	- What about sideways?
	- What about non-linear motion / jerky motion / incomplete motion
		- Probably use Ultrasonic sensor
		- Might need to use other sensor
- Response
	- Change in facial expression
	- Cute speaker noise
- Difficulties
	- Adding our own audio
	- Distinguishing between different gestures
	- Adjust sensivity of ultrasonic sensor

## How it works
- Robot Standing
- If no hand motion detect above robot
	- Do nothing
- If hand motion detected above robot (Ultrasonic sensor)
	- Implement Response
- Once response is finished, wait 30 sec before resuming detection of hand motion
