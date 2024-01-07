from modules import functions as func

#################################################################################################
VERSION = "1.0"
#################################################################################################


def check_version():
    if (
        func.conf.VERSION == VERSION
        and func.greet.VERSION == VERSION
        and func.err.VERSION == VERSION
        and func.VERSION == VERSION
    ):
        return True
    else:
        return False


if not check_version():
    func.send_error_message(func.err.ERROR_VERSION_CONTROL)

func.check_python_version()
func.greeting()
