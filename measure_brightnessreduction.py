import matplotlib.pyplot as plt
import cv2
import math
import numpy    as np
import argparse
import os
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', action='store',
                        nargs=None,
                        const=None,
                        default=None,
                        type=str,
                        help='Image file to measure brightness')
    args = parser.parse_args()
    if not os.path.exist(args.input):
        print('Error\n {} dosse not exist.' .format(args.input))
        sys.exit()
