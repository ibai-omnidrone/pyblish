import maya.utils
print(".... ENTERING USER SETUP.....")


def delayedStartup():
    import pyblish.api
    import pyblish_maya
    pyblish.api.register_gui('pyblish_lite')
    pyblish_maya.setup()


if __name__ == "__main__":
    print("-------EXECUTE MAIN-----")
    try:
        maya.utils.executeDeferred(delayedStartup)
    except:
        print("ERROR: Something went wrong loading pyblish module.")
