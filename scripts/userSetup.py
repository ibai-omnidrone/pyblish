import maya.utils

def pyblish_delayed_startup():
    """
    Pyblish Framework Initialization
    :return:
    """
    print("Initialize Pyblish")
    import pyblish.api
    pyblish.api.register_gui('pyblish_qml')

    import pyblish_maya
    pyblish_maya.setup()

if __name__ == "__main__":
    try:
        maya.utils.executeDeferred(pyblish_delayed_startup)
    except:
        print("ERROR: Something went wrong loading pyblish module.")
