# CHANGE A SPECIFIC LINE IN A FILE

with open('button_state.txt', 'r') as f:
    # put all the lines in a list
    list_of_lines = f.readlines()
    
    # change a specific line
    for i in range(0,2):
        
        # find the line to change
        if 'button_notes' in list_of_lines[i]:
            
            # locate the color
            color = list_of_lines[i].split(' ')
            
            # change the color
            color[1] = '#64ff64'
            
            # remove the current color
            list_of_lines[i] = list_of_lines[i][:-7]
            
            # add the new color
            list_of_lines[i] = f'{list_of_lines[i]}{color[1]}'

# write the new color to the file
with open('button_state.txt', 'w') as f:
    f.writelines(list_of_lines)
            
            