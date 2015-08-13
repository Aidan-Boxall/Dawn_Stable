import animate as an
import animation_source_files as asf
import pickle

def retry():
    with open('files.pkl', 'rb')  as file:
        files = pickle.load(file)
    print "Create movie..."
    print files
    an.rotanimate(files, "rotation_whole_crys.mp4")

def delete_files():
    with open('files.pkl', 'rb')  as file:
        files = pickle.load(file)
    an.remove_files(files)

retry()