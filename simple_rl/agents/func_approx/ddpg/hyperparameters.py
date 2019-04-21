# Hyperparameters
BUFFER_SIZE = int(1e6)
BATCH_SIZE = 64
GAMMA = 0.99
TAU = 0.01
LRA = 1e-4
LRC = 1e-4
HIDDEN_1 = 400
HIDDEN_2 = 300

MAX_EPISODES = 50000
MAX_STEPS = 200
GLOBAL_LINEAR_EPS_DECAY = 1e-6  # complete decay over 1 million transitions
OPTION_LINEAR_EPS_DECAY = 3e-6  # complete decay over 5 hundred thousand transitions
EPS_MIN = 0.1                   # lowest that epsilon will be to always have some exploration noise
PRINT_EVERY = 10
