with open('all_subtitles_raw.txt', 'r') as read_file:
    data = read_file.read()

lines = []
current_line = ''
line_nr = 0

# split parts
for line in data.split('\n'):
    if line == '':
        if current_line != '': lines.append(current_line)
        current_line = ''
        line_nr = 0
    else:
        if line_nr == 2: current_line = line
        elif line_nr > 2: current_line += ' ' + line
        line_nr += 1

#tack together
data = ''
for line in lines:
    data += line + '\n'

# check and print chars
letters = {}
for l in data:
    if l in letters: letters[l] += 1
    else: letters[l] = 1

d = sorted(letters, key = letters.get)

for letter in d:
    print letter + '\t' + str(letters[letter])

# write back to file
with open('all_subtitles_clean.txt', 'w') as write_file:
    write_file.write(data)
