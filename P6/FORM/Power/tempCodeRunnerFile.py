import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Power")
sys.path.append(os.path.normpath(model_dir))

from controller import AppController