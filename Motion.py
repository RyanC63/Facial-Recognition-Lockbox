from gpiozero import MotionSensor

pir = MotionSensor(6)

while True:
    pir.wait_for_motion()
    print ("You Moved")
    pir.wait_for_no_motion()
