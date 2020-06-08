import pyblish.api
import pyblish_maya

pyblish.api.register_gui("pyblish_lite")  # Fallback
pyblish_maya.setup()
