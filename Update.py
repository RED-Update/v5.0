import sys
import time
import base64
import shutil
import os
import subprocess

def NewCopy():
    if not os.path.exists("/home/pi/RDC/FileCopy.py"):
        try:
            shutil.copy('/home/pi/REDRDC/FileCopy.py', '/home/pi/RDC/')
        except:
            print("Python File not available for copy")

    if not os.path.exists("/etc/init/FCopy.conf"):
        try:
            shutil.copy('/home/pi/REDRDC/FCopy.conf', '/etc/init/')
        except:
            print("config File not available for copy")



def count_files(in_directory):
    joiner=(in_directory + os.path.sep).__add__
    return sum(
            os.path.isfile(filename)
            for filename
            in map(joiner, os.listdir(in_directory))
    )

def updateProc():
    try:
        root_src_dir = '/home/pi/NewFirmware/'
        root_dst_dir = '/home/pi/REDRDC/'
        print("Copy Done")
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
        print("Returned True")
        return True

    except shutil.Error as e:        
        print('Error: %s' % e)

    except IOError as e:
        print('Error: %s' % e.strerror)

    except:
        print ("unknown error!")

    return False

# main entry point
time.sleep(1)
NewCopy()
while True:
    NewFiles = count_files('/home/pi/NewFirmware/')
    
    if NewFiles > 0:
        time.sleep(5)
        if updateProc() == True:
            # update was good, lets sleep for 10 mins and check again
            print("Sleeping for 10 minutes")
            time.sleep(10)
        else:
            time.sleep(10)
            print("Sleeping for 10 seconds")
    else:
        time.sleep(10)
        print("No new files")

