import maya.cmds as mc

def MakeBetweenLocator():
	size  = 0.2;
	posx  = 0
	posy  = 0
	posz  = 0
	count = 0
	mc.ConvertSelectionToVertices()
	sel = mc.ls(sl=True,fl=True)
	for i in sel:
		pos	   = mc.xform(i,q=True,ws=True,t=True)
		posx  += pos[0]
		posy  += pos[1]
		posz  += pos[2]
		count += 1
	#print 'Vertex count %s'%count
	dis = [posx/count,posy/count,posz/count]
	Loc = mc.spaceLocator(name='skinningPostionLocator0000',p=dis)
	mc.setAttr('%sShape.localScaleX'%Loc[0],size)
	mc.setAttr('%sShape.localScaleY'%Loc[0],size)
	mc.setAttr('%sShape.localScaleZ'%Loc[0],size)
	mc.CenterPivot()
	
MakeBetweenLocator()
