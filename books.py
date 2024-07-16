from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Load a model
        self.cube = self.loader.loadModel("magic_book_stylized.glb")
        self.cube.reparentTo(self.render)
        
        # Set initial scale
        self.cube.setScale(1)
        self.cube.setPos(0, 0, 0)

        # Center the model and set it at a distance from the camera
        distance_from_camera = 10  # Adjust this value as needed
        self.cube.setPos(0, distance_from_camera, 0)
        
        # Ensure the camera is looking at the model
        self.camera.setPos(0, -20, 10)  # Adjust the camera position
        self.camera.lookAt(self.cube)

        # Add the rotation task
        self.taskMgr.add(self.rotate_cube, "RotateCubeTask")

        # Accept the 'w' key to scale the cube to zero
        self.accept("w", self.scale_cube)

    def scale_cube(self):
        self.cube.setScale(0, 0, 0)

    def rotate_cube(self, task):
        angle_degrees = task.time * 50.0  # Rotate 50 degrees per second
        self.cube.setHpr(angle_degrees, 0, 0)
        return task.cont    

app = MyApp()
app.run()
