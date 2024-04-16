from panda3d.core import PointLight, AmbientLight

def setup_ambient_light(node_path):
    #adding Ambient light to the renderer
    alight = AmbientLight("alight")
    alight.setColor((0.08,0.08,0.08,1))
    alnp = node_path.attachNewNode(alight)
    node_path.setLight(alnp)

def setup_point_light(node_path, pos):
    #adding point light to the render
    plight = PointLight("plight")
    plight.setShadowCaster(True, 1024,1024)
    plight.setColor((1,1,1,1))
    plnp = node_path.attachNewNode(plight)
    plnp.setPos(pos[0],pos[1],pos[2])
    #plight.setAttenuation(1,4,0,0)
    node_path.setLight(plnp)

    return plnp    
