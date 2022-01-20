# open the file 
# with open('button_state.txt', 'r') as f:
    
    # locate the current color 
    # color = f.read().split(' ')
    
    # change the color
    # color[1] = '#64ff64'

# write the new color to the file
# with open('button_state.txt', 'w') as f:
    # f.write(' '.join(color))
  
def test1():
    with open('button_state.txt', 'r') as f:
        for line in f.readlines():
            if 'button_notes' in line:
                print(line)
                current_Color = line.split(' ')[1]
                new_Color = '#64ff64'

    with open('button_state.txt', 'w') as f:
        f.write()

text = '#64ff64'
text = text[:-7]
print(text)