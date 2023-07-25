import os

if_executed = False

os.chdir('pdf')

for filename in os.listdir(os.getcwd()):
    if ' ' in filename:
        os.rename(filename, filename.replace(' ', '_'))
        print('change filename... padding done!')
        if_executed = True

if not if_executed:
    print('no change filename...')

os.chdir('..')