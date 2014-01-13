import maya.cmds as mc

def BlendshapeTargetsKeyAll():
	starttime = '1'
	endtime   = '100'
	sel  = mc.ls(sl=True)
	if sel:
		mesh = mc.listRelatives(sel,children=True,type='mesh')
		test = mc.listConnections(mesh[0] +'.inMesh',d=False,s=True)
		if mc.objectType(test[0],isType='blendShape') == True:
			#print 'blendShape'
			list = mc.listConnections(test[0]+'.inputTarget[0].inputTargetGroup',d=False,s=True)
			#print list
			for i in list:
				mc.currentTime(starttime)
				mc.setAttr(test[0]+'.'+i,0)
				mc.setKeyframe(test[0]+'.'+i)
				mc.currentTime(endtime)
				mc.setAttr(test[0]+'.'+i,1)
				mc.setKeyframe(test[0]+'.'+i)
				mc.currentTime(starttime)
		elif mc.objectType(test[0],isType='skinCluster') == True:
			#print 'skinCluster'
			ingeo    = mc.listConnections(test[0] +'.input[0].inputGeometry',d=False,s=True)
			blendgeo = mc.listConnections(ingeo[0] +'.inputGeometry',d=False,s=True)
			print blendgeo
			list = mc.listConnections(blendgeo[0]+'.inputTarget[0].inputTargetGroup',d=False,s=True)
			#print list
			for i in list:
				mc.currentTime(starttime)
				mc.setAttr(blendgeo[0]+'.'+i,0)
				mc.setKeyframe(blendgeo[0]+'.'+i)
				mc.currentTime(endtime)
				mc.setAttr(blendgeo[0]+'.'+i,1)
				mc.setKeyframe(blendgeo[0]+'.'+i)
				mc.currentTime(starttime)
	else:
		print 'Not Select!'
		
BlendshapeTargetsKeyAll()	
