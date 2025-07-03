from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode, WindowProperties

class ShopSimulator(ShowBase):
    """
    Main class for the Shop Simulator game using Panda3D.

    This class initializes the Panda3D environment, sets up the scene,
    and handles the main game loop.
    """
    def __init__(self):
        # Initialize the ShowBase class which is the foundation of Panda3D
        ShowBase.__init__(self)

        # Set window title and properties
        self.set_window_properties()

        # Display title on screen
        self.title = OnscreenText(
            text="Shop Simulator",
            style=1,
            fg=(1, 1, 1, 1),
            pos=(0, 0.9),
            scale=0.1,
            shadow=(0, 0, 0, 0.5),
            align=TextNode.ACenter
        )

        # Add instructions text
        self.instructions = OnscreenText(
            text="Press ESC to quit",
            style=1,
            fg=(1, 1, 1, 1),
            pos=(0, -0.9),
            scale=0.05,
            align=TextNode.ACenter
        )

        # Set up key event handlers
        self.accept("escape", self.quit_game)

        # Set up a simple environment (to be expanded later)
        self.setup_environment()

    def set_window_properties(self):
        """Set up the window properties for the game."""
        props = WindowProperties()
        props.setTitle("Shop Simulator")
        props.setSize(1024, 768)
        self.win.requestProperties(props)

    def setup_environment(self):
        """Set up the initial 3D environment."""
        # Set a simple background color for now
        self.setBackgroundColor(0.5, 0.5, 0.8)

        # In the future, this will load 3D models for the shop, items, etc.
        # For now, just add a message
        self.environment_text = OnscreenText(
            text="3D Shop Environment (Coming Soon)",
            style=1,
            fg=(1, 1, 1, 1),
            pos=(0, 0),
            scale=0.07,
            align=TextNode.ACenter
        )

    def quit_game(self):
        """Exit the game cleanly."""
        self.userExit()


def main():
    """Initialize and start the Shop Simulator game."""
    app = ShopSimulator()
    app.run()


if __name__ == '__main__':
    main()
