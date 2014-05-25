import maya.cmds as mc

def NomalCylinder():
	size = 0.5
	obj = mc.ls(sl=True,fl=True)
	if obj:
		for i in obj:
			val = 0
			cy  = mc.polyCylinder(r=size,h=2,sx=8,sy=1,sz=1,ax=(0,1,0),rcp=0,cuv=3,ch=1)
			pos = mc.xform(i,q=True,t=True,ws=True)
			for axis in ['X','Y','Z']:
				mc.setAttr('%s.translate%s'%(cy[0],axis),pos[val])
				val += 1
			source = i.split('.')
			mc.normalConstraint(source[0],cy,weight=1,aimVector=(0,1,0),upVector=(0,1,0),worldUpType="vector",worldUpVector=(0,1,0))
			mc.geometryConstraint(source[0],cy,weight=1)
		print 'Create!'
	else:
		print 'Not select'
