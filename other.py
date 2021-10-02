import os

def delete(filename):

    if os.path.exists(filename):
        os.remove(filename)

def delete_all():
    delete("temp.log")
    delete("error.log")
    delete("log.log")