from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
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

home_joints_list =  robot.JointsHome().tolist()
print (home_joints_list)
j1home = home_joints_list[0]
j2home = home_joints_list[1]
j3home = home_joints_list[2]
print (j1home, j2home, j3home)
limitneg,limitpos,pp = robot.JointLimits()
print (limitneg,  "\n" ,limitpos ,"\n" )
aprox = 100
a0 = transl(850,0,400+aprox)
a1 = transl(850,0,400)
a2 = transl(750,0,400)
a3 = transl(750,50,400)
a4 = transl(850,50,400)

A = [a0, a1, a2, a3, a4]

for i in range(5):
    robot.MoveJ(A[i]*rotx(-pi))
