# Hyperparameters
BUFFER_SIZE = int(1e6)
BATCH_SIZE = 64
GAMMA = 0.99
TAU = 0.001
LRA = 1e-4
LRC = 1e-3
HIDDEN_1 = 400
HIDDEN_2 = 300

MAX_EPISODES = 50000
MAX_STEPS = 200
epsilon_decay = 1. / 100000
PRINT_EVERY = 10