import maya.cmds as cmds
def RenameFile():
  #Now_open_file_name
	name = cmds.file(q=True,shortName=True,sceneName=True)
	#Split_file_name
	name2 = name.split("_",1)
	name3 = name2[1].split(".",1)
	if  int(name3[0]) < 9:
		name4 = name2[0]+"_0"+str(int(name3[0])+1)+".mb"
		print name4
		#Save_file
		cmds.file(rename=name4)
		cmds.file(save=True, type='mayaBinary')
	else:
		name4 = name2[0]+"_"+str(int(name3[0])+1)+".mb"
		print name4
		#Save_file
		cmds.file(rename=name4)
		cmds.file(save=True, type='mayaBinary')
	
RenameFile()
