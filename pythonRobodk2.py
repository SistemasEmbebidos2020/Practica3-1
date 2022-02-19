from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
RDK = Robolink()

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
reference = robot.Parent()
print (reference)
robot.setPoseFrame(reference)
pose_ref=robot.Pose()
print (pose_ref)
posi = Pose_2_TxyzRxyz(pose_ref)
print (posi)
home_joints =  robot.JointsHome()
print (home_joints)
robot.MoveJ(home_joints)
pose_ref=robot.Pose()

limitneg,limitpos,pp = robot.JointLimits()
print (limitneg,  "\n" ,limitpos ,"\n" )
aprox = -100
a0 = pose_ref*transl(100,0,0+aprox)
a1 = pose_ref*transl(100,0,0)
a2 = pose_ref*transl(75,0,0)
a3 = pose_ref*transl(0,50,0)
a4 = pose_ref*transl(75,100,0)
a5 = pose_ref*transl(0,150,0)
a6 = pose_ref*transl(75,200,0)
a7 = pose_ref*transl(100,200,0)
a8 = pose_ref*transl(100,200,0+aprox)

A = [a0, a1, a2, a3, a4, a5, a6, a7,a8]
for i in range(9):
    robot.MoveJ(A[i]*rotx(-pi))
