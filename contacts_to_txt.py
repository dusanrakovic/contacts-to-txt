import re
import codecs

# Opening vcf file (file which has been created upon extracting from Contacts app)
# Change name in line below to match the name of those from your phone
file_in = open('PIM00001.vcf')

# Opening txt file where contact information will be extracted
# Change name in line below as you like, or leave it like this
# Encoding is set to UTF-8
# File is open in write mode; if you want to append contacts to existing .txt file
# with same name, change parameter from 'w' to 'a'
file_out = open('Contacts.txt', 'w', encoding='utf-8')


# Function which checks every single line if it need to be encoded
def check_encoding(line):
    if line[:2] == 'FN' and 'UTF-8' in line:
        line = decoding(line)
        return line
    else:
        return line

# Function which decodes encoded lines
def decoding(line):
    item_name, item_value = line.split(':', 1)
    item_cleaned = re.sub('=', '', item_value)
    item_decoded = codecs.decode(item_cleaned, 'hex').decode('utf-8', errors='ignore')
    line = item_name + ':' + item_decoded
    return line

# Function which returns clean record for parts of contacts information
def txt_output(line):
    if_dict = {'BE':'\n', 'FN':'Name: ', 'TE':'Phone: ', 'EM':'E-mail: ', 
               'UR':'Website: ', 'OR':'Organization: ', 'TI':'Title: '}
    x = line[:2]
    if x in if_dict and x != 'BE':
        item_name, item_value = line.split(':', 1)
        output = if_dict[x] + item_value
        return output
    elif x == 'BE':
        output = if_dict[x]
        return output

# Main part of program
for line in (file_in):
    line = line.rstrip()    
    line = check_encoding(line)
    line = txt_output(line)
    
    if line is None:
        pass
    else:
        file_out.write(line + '\n')

file_in.close()
file_out.close()
