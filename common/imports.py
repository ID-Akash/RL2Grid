import logging
import argparse as ap
import random as rnd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
from argparse import Namespace
from typing import Any, Deque, Dict, List, Optional, Tuple, Type, Union

import gymnasium as gym
# `gym.logger.set_level` was removed in gymnasium >= 1.0; guard for compatibility.
if hasattr(gym.logger, "set_level"):
    gym.logger.set_level(logging.ERROR)
else:
    logging.getLogger("gymnasium").setLevel(logging.ERROR)
import numpy as np
import wandb as wb

import torch as th
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim





