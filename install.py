import subprocess
import sys
#Adding pip & general update
subprocess.call("sudo apt-get update", shell=True)
subprocess.call("sudo apt-get install python-pip", shell=True)

#Update & Remove
subprocess.call('sudo apt-get dist-upgrade', shell=True)
subprocess.call("sudo apt autoremove", shell=True)

#TensorFlow
subprocess.call("sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev", shell=True)
subprocess.call("sudo apt-get install python3-pip", shell=True)
subprocess.call("pip3 install --user pip", shell=True)

#Python packages
subprocess.call("sudo pip3 install -U numpy==1.16.1", shell=True)
subprocess.call("pip3 install -U future==0.17.1", shell=True)
subprocess.call("pip3 install -U mock==3.0.5", shell=True)
subprocess.call("pip3 install -U h5py==2.9.0", shell=True)
subprocess.call("pip3 install -U keras_preprocessing==1.0.5", shell=True)
subprocess.call("pip3 install -U keras_applications==1.0.6", shell=True)
subprocess.call("pip3 install -U enum34", shell=True)
subprocess.call("pip3 install -U futures", shell=True)
subprocess.call("pip3 install -U testresources", shell=True)
subprocess.call("pip3 install -U setuptools", shell=True)
subprocess.call("pip3 install -U protobuf", shell=True)

subprocess.call('pip3 install --no-cache --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu', shell=True)

#OpenAI Dependencies
subprocess.call("sudo pip3 install -U --no-dependencies pyglet==1.3.2", shell=True)

#OpenAI Gym
subprocess.call('sudo pip3 install -U --no-dependencies gym', shell=True)
#Might need to use pip here if errors arise

#Weights&Biases
subprocess.call('sudo -H pip3 install -U wandb', shell=True)
#Might need to use pip here if errors arise