"""
What upppppp ok so zip file is attached.
I'm also attaching an example log file - the specific line/number I'm interested in is the affinity (kcal/mol) in the
 "mode 1" line (for example in the attached file - the number is -6.6. What I want in terms of output is a list of that
 number & which file it corresponds to (so for this example, the list would say something like:

 -6.6     8730_ligand_1.pdbqt_log

"""
import os

if __name__ == '__main__':
    dirFiles = [f for f in os.listdir('.') if os.path.isfile(f)]
    logFiles = [file for file in dirFiles if file.endswith('.log')]

    affinity = ''
    for filename in logFiles:
        with open(f"{filename}", 'r') as currLog:
            prevLine = ''
            for line in currLog:
                # make sure the line I'm looking at is the one I want
                if line.lstrip().startswith('1') and prevLine.startswith('-'):
                    # get rid of the starting 1 and then get rid of the whitespaces so the value I want is at the front
                    splitList = line.replace('1', ' ', 1).lstrip().split(' ')
                    affinity = splitList[0]
                    print(f"{affinity}     {filename}")
                    break
                prevLine = line
