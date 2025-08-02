import os

def find_files(filename, search_path):
   complete_path = ''
# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
        if filename in files:
            complete_path = os.path.join(root, filename)
            return complete_path


search_path = []
username = os.getlogin()
first_part_path1 = 'C:\\Users\\'
last_part_path1 = '\\Downloads'
complete_path = first_part_path1 + username + last_part_path1
search_path.append(complete_path)

first_part_path2 = 'C:\\Users\\'
last_part_path2 = '\\Desktop'
complete_path = first_part_path2 + username + last_part_path2
search_path.append(complete_path)

first_part_path3 = 'C:\\Users\\'
last_part_path3 = '\\Documents'
complete_path = first_part_path3 + username + last_part_path3
search_path.append(complete_path)

first_part_path4 = 'C:\\Users\\'
last_part_path4 = '\\Music'
complete_path = first_part_path4 + username + last_part_path4
search_path.append(complete_path)

first_part_path5 = 'C:\\Users\\'
last_part_path5 = '\\Pictures'
complete_path = first_part_path5 + username + last_part_path5
search_path.append(complete_path)

first_part_path6 = 'C:\\Users\\'
last_part_path6 = '\\Videos'
complete_path = first_part_path6 + username + last_part_path6
search_path.append(complete_path)


final_path = ''
for x in range(0,len(search_path)):
    if find_files('12_digits_barcodes.txt',search_path[x]):
        final_path = find_files('12_digits_barcodes.txt',search_path[x])
        break;
    else:
        continue;


list_of_barcodes = []             #string list
split_barcode = []       #string list
final_barcodes = []   #string list
odd = 0
even = 0
index = 0   #cycle through list_of_barcodes and append checksum with final barcode
            #index must be a int variable, b in for loop is a str variable
            
try:
    file = open(final_path)

    for i in file:
        doofus = i.rstrip('\n')
        list_of_barcodes.append(doofus)

    file.close()

    for word in list_of_barcodes:
        for char in word:
            split_barcode.append(char)
        
        for a in range (11,0,-2):
            odd += int(split_barcode[a])

        
        for b in range (10,-1,-2):
            even += int(split_barcode[b])

        checksum = (10 - ((3 * odd + even) % 10)) % 10

        final = list_of_barcodes[index] + str(checksum)
        final_barcodes.append(final)

        index += 1
        split_barcode = []
        odd = 0
        even = 0

    final_path = ''
    for x in range(0,len(search_path)):
        if find_files('Final_barcodes.txt',search_path[x]):
            final_path = find_files('Final_barcodes.txt',search_path[x])
            break;
        else:
            continue;
        
    file = open(final_path,'w')

    for line in final_barcodes:
        file.write(line)
        file.write('\n')
        
    file.close()

    print('Generated successfully!!!\n\n')
    input('Press \'Enter\' to exit....\n\n')

except Exception as e:
    print(e,'\n')
    input('Press Enter To Continue...\n')

except ValueError as e:
    print(e,'\n')
    input('Press Enter To Continue...\n')

except ImportError as e:
    print(e,'\n')
    input('Press Enter To Continue...\n')

except ModuleNotFoundError as e:
    print(e,'\n')
    input('Press Enter To Continue...\n')

except AttributeError as e:
    print(e,'\n')
    input('Press Enter To Continue...\n')
