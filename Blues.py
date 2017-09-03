tones = ['Cb','Gb','Db','Ab','Eb','Bb','F','C','G','D','A','E','B','F#','C#']
tonality = input('Enter a Root note to start practice:')
try: 
    x = tonality[0].upper() # Convert 1st letter to uppercase
    if  len(tonality)>1: # Convert second letter, if exists, to lowercase
        y = tonality[1].lower()
        tonality = x+y+tonality[2:] #retain the full lenght
    else:
        tonality = x+tonality[1:] # retain the full lenght     
except:
    print ('Stop typing wrong tones and start playing the blues...')
    exit() 
if tonality in tones: # check if the input belongs to the TONES LIST
    print (tonality)
    if tonality == 'Cb':
         tonality = 'B'
         print ('Your tone was altered enharmonically for your own safety')
    elif tonality == 'C#':
         tonality = 'Db'
         print ('Your tone was altered enharmonically for your own safety')
    root_position = tones.index(tonality) #finding the position of the tonality given by the user
    subdominant_position = root_position - 1
    dominant_position = root_position + 1
    print ('Start playing the blues using:')
    print ('I -', tones[root_position],',','IV -',tones[subdominant_position],',','V -', tones[dominant_position])
    print ()
    print ('Goodbye!')
else : print ('Stop typing wrong tones and start playing the blues...') 

    