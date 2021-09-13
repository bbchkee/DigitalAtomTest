import numpy as np
import argparse
import time
from sys import exit

def model_bugs(bugs, stones):
    free_spaces = [stones]
    for i in range(bugs):
        free_spaces_index = np.argmax(free_spaces) # find the bigger area
        current_space = free_spaces[free_spaces_index]-1 # bug is digged
        new_spaces = [current_space//2, (current_space//2) + (current_space%2)] # calculate the space around
        del free_spaces[free_spaces_index]
        free_spaces+=new_spaces
    return new_spaces
    
def math_bugs(bugs, stones):
    rounded_bugs = 2**(np.floor(np.log2(bugs))) # calculate the spacing
    left = ((stones-bugs) // (rounded_bugs)) // 2 
    right = left + ((stones-bugs) // (rounded_bugs)) % 2
    return left, right

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bugs', action='store', dest='bugs', type = int, help = 'Number of bugs')
parser.add_argument('-s', '--stones', action='store', dest='stones', type = int, help = 'Number of stones')
parser.add_argument('-m', '--mode', action='store', dest='mode', default = 'auto', help = 'Modes: model (slower, precise), math (faster, less precision), auto (choosing mode depends on numbers)')

args = parser.parse_args()
bugs = args.bugs
stones = args.stones
mode = args.mode

start_time = time.time()

if bugs > stones:
    print('Too much bugs!')
    exit()
elif bugs <= 0:
    print('Bugs need to be positive!')
    exit()

if mode == 'math':
    print('Running approximation...')
    left, right = math_bugs(bugs, stones)
    print('Estimated number of stones = [%i, %i]' % (left, right))
    print('Elapsed time = %f seconds' % (time.time()-start_time))

if mode == 'model':
    print('Running model (may take time) ...')
    left, right = model_bugs(bugs,stones)
    print('Calculated number of stones = [%i, %i]' % (left, right))
    print('Elapsed time = %f seconds' % (time.time()-start_time))

if mode == 'auto':
    if bugs <= 10000 and stones <= 100000:
        print('Auto-setting to model mode (slow, precise)')
        left, right = model_bugs(bugs,stones)
        print('Calculated number of stones = [%i, %i]' % (left, right))
        print('Elapsed time = %f seconds' % (time.time()-start_time))
    else:
        print('Auto-setting to math mode (fast, less precise)')
        left, right = math_bugs(bugs,stones)
        print('Calculated number of stones = [%i, %i]' % (left, right))
        print('Elapsed time = %f seconds' % (time.time()-start_time))
