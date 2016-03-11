import time, sys, json
import rospy
from sensor_msgs.msg import Joy
import speech_recognition as sr

with open('google.key', 'r') as f:
    google_key = f.readline()

def ready(pub):
	msg = Joy()
	msg.header.stamp = rospy.Time.now()
	valueAxe = 0.0
	valueButton = 0
	standup_time = 20 #2 seconds
	for i in range (0, 20):
		msg.axes.append(valueAxe)
	for e in range (0, 17):
		msg.buttons.append(valueButton)
	rate = rospy.Rate(10)
	time.sleep(1)

	msg.buttons[3] = 1
	i=0
	bo=True
	print "STAND_UP"
	while not rospy.is_shutdown() and bo:
		i=i+1
		if (i>standup_time):
			bo=False
			msg.buttons[3] = 0
		pub.publish(msg)
		rate.sleep()

def forward(pub):
	msg = Joy()
	msg.header.stamp = rospy.Time.now()
	valueAxe = 0.0
	valueButton = 0
	walking_time = 30 #3 seconds
	for i in range (0, 20):
		msg.axes.append(valueAxe)
	for e in range (0, 17):
		msg.buttons.append(valueButton)
	rate = rospy.Rate(10)
	time.sleep(1)

	msg.axes[1] =  1
	i=0
	bo=True
	print "WALKING FORWARD"
	while not rospy.is_shutdown() and bo:
		i=i+1
		if (i>walking_time):
			bo=False
			msg.axes[1] = 0
		pub.publish(msg)
		rate.sleep()

def backwards(pub):
	msg = Joy()
	msg.header.stamp = rospy.Time.now()
	valueAxe = 0.0
	valueButton = 0
	walking_time = 30 #3 seconds
	for i in range (0, 20):
		msg.axes.append(valueAxe)
	for e in range (0, 17):
		msg.buttons.append(valueButton)
	rate = rospy.Rate(10)
	time.sleep(1)

	msg.axes[1] =  -1
	i=0
	bo=True
	print "WALKING BACKWARDS"
	while not rospy.is_shutdown() and bo:
		i=i+1
		if (i>walking_time):
			bo=False
			msg.axes[1] = 0
		pub.publish(msg)
		rate.sleep()

def right(pub):
	msg = Joy()
	msg.header.stamp = rospy.Time.now()
	valueAxe = 0.0
	valueButton = 0
	turning_time = 30 #3 seconds
	for i in range (0, 20):
		msg.axes.append(valueAxe)
	for e in range (0, 17):
		msg.buttons.append(valueButton)
	rate = rospy.Rate(10)
	time.sleep(1)

	msg.axes[2] =  -1
	i=0
	bo=True
	print "TURNING RIGHT"
	while not rospy.is_shutdown() and bo:
		i=i+1
		if (i>turning_time):
			bo=False
			msg.axes[2] = 0
		pub.publish(msg)
		rate.sleep()

def left(pub):
	msg = Joy()
	msg.header.stamp = rospy.Time.now()
	valueAxe = 0.0
	valueButton = 0
	turning_time = 30 #3 seconds
	for i in range (0, 20):
		msg.axes.append(valueAxe)
	for e in range (0, 17):
		msg.buttons.append(valueButton)
	rate = rospy.Rate(10)
	time.sleep(1)

	msg.axes[2] =  1
	i=0
	bo=True
	print "TURNING LEFT"
	while not rospy.is_shutdown() and bo:
		i=i+1
		if (i>turning_time):
			bo=False
			msg.axes[2] = 0
		pub.publish(msg)
		rate.sleep()

def main():
	rospy.init_node("voice_control", anonymous=True)
	pub = rospy.Publisher("/joy", Joy, queue_size=10)

	# obtain audio from the microphone
	r = sr.Recognizer()	
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Google Speech Recognition
	try:
		text = r.recognize_google(audio, key=google_key, language = "en-US")
		text = text.lower()
		print("Google Speech Recognition thinks you said "+text)
		if "back" in text or "bakh" in text:
			backwards(pub)
		elif "left" in text or "levt" in text:
			left(pub)
		elif "right" in text:
			right(pub)
		elif "stand" in text or "up" in text:
			ready(pub)
		elif "forward" in text or "fort worth" in text or "for what" in text or "walk" in text or "walt" in text or "world" in text or "what" in text:
			forward(pub)
		else:
			print("Unknown command '" + text +"'")

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    main()