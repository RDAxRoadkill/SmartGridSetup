# Check if Tensorflow works correctly
import tensorflow as tf
import numpy as np
from tensorflow import keras
import subprocess
import sys
import wandb

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=500)
print(model.predict([10.0]))

# Check if Gym works correctly
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    #env.render() Doesn't work since no monitor is connected.
    env.step(env.action_space.sample()) # take a random action
env.close()

#Setup wandb
subprocess.call("wandb login a8c0cf2b1dfe6c4d79eccdd47a8342f4972d9dfe", shell=True)
from wandb.keras import WandbCallback
wandb.init(project="nano_init")

