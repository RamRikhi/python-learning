# Author: Rikhi
# Date: 03/09/2022
# Copyright @ 2022

import os

# This python program is able to print current directory file names

files = os.listdir()

for index in files:
    print(index)