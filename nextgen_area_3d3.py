from panda3d.core import Point3, CollisionNode , CollisionSphere, CollisionHandlerEvent , TextNode
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText


class MyApp(ShowBase):
    def __init__(self):
        super().__init__()


                # Create an OnscreenText object
        self.message = OnscreenText(
            text="JIT displayed!",
            pos=(0, 0),  # Position (centered)
            scale=0.1,   # Text size
            fg=(1, 1, 1, 1),  # Text color (white)
            align=TextNode.ACenter,  # Center alignment
            mayChange=True  # Allow text to change dynamically
        )

        # Load the village model (replace with your actual path)
        self.village = self.loader.loadModel("halls_green_haa_emplacement.glb")
        self.village.reparentTo(self.render)
        self.village.setScale(2)  # Adjust the scale as needed
        self.village.setPos(3, 60, -16)  # Adjust the position
        self.village.setHpr(180, 90, 0)  # Rotate 180 degrees around the X-axis


        # Load the cube model (replace with your actual path)
        self.cube = self.loader.loadModel("ant.glb")
        self.cube.reparentTo(self.render)
        self.cube.setScale(0.03)  # Adjust the scale as needed
        self.cube.setPos(3, 60, -12)  # Adjust the position
        self.cube.setHpr(0, 90, 0)  # Rotate 180 degrees around the X-axis


                # Create collision solids for both models (spheres, boxes, etc.)
        # For simplicity, let's use CollisionSphere for both models
        self.village_collide = self.village.attachNewNode(CollisionNode("village_collide"))
        self.village_collide.node().addSolid(CollisionSphere(0, 0, 0, 1))  # Adjust radius as needed
        self.village_collide.show()

        self.ant_collide = self.cube.attachNewNode(CollisionNode("ant_collide"))
        self.ant_collide.node().addSolid(CollisionSphere(0, 0, 0, 0.5))  # Adjust radius as needed
        self.ant_collide.show()

        # Set up collision handlers
        self.collision_handler = CollisionHandlerEvent()
        self.collision_handler.addInPattern("%fn-into-%in")

        # Register collision events
       # self.accept("ant_collide-into-village_collide", self.handle_collision)

        # Rotate the cube smoothly
        self.taskMgr.add(self.rotate_cube, "rotate_cube")

        # Disable culling to prevent model disappearance
        self.cube.setTwoSided(True)

        # Set initial velocity
        self.velocity = Point3(0, 0, 0)

        # Register key handlers
        self.accept("w", self.set_velocity, ["forward"])
        self.accept("a", self.set_velocity, ["left"])
        self.accept("s", self.set_velocity, ["backward"])
        self.accept("d", self.set_velocity, ["right"])
        self.accept("w-up", self.set_velocity, ["stop"])
        self.accept("a-up", self.set_velocity, ["stop"])
        self.accept("s-up", self.set_velocity, ["stop"])
        self.accept("d-up", self.set_velocity, ["stop"])

    def rotate_cube(self, task):
        dt = globalClock.getDt()  # Get delta time
        self.cube.setH(self.cube.getH() + 3 * dt)  # Rotate at 30 degrees per second

        # Move the cube based on velocity
        self.cube.setPos(self.cube.getPos() + self.velocity * dt)

        return task.cont

    def set_velocity(self, direction):
        if direction == "forward":
            self.velocity.setY(1)
        elif direction == "backward":
            self.velocity.setY(-1)
        elif direction == "left":
            self.velocity.setX(-1)
        elif direction == "right":
            self.velocity.setX(1)
        elif direction == "stop":
            self.velocity.setX(0)
            self.velocity.setY(0)

        

if __name__ == "__main__":
    app = MyApp()
    app.run()
