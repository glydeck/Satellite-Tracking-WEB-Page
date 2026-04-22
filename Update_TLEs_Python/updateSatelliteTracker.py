#######################################################
#                                                     #
#  Python Program to Retrieve new Keplarian Elements  # 
#     and build a new Satellite Tracker WEB Page      #
#                                                     #
#######################################################

# Step 1
# Retrieve Keplarian Data from WEB
import urllib.request
# Create 'kepelements.txt' & 'file2.txt' in write mode ('w')
with open("kepelements.txt", "w") as file:
    with open("file2.txt", "w") as file:
        file.close() 
with open('kepelements.txt', 'r+') as file:
    # Purge content from kepelements.txt
    # Important: move the cursor to the beginning before truncating
    file.seek(0) 
    file.truncate(0)
    file.close()

# RequestWEB_data

import requests

# 1. Define the URL of the online text file
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=amateur&FORMAT=2le"

# 2. Fetch the content from the URL
response = requests.get(url)

# 3. Check if the request was successful
if response.status_code == 200:
    # 4. Write the content to a local file
    with open("kepelements.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("kepelements.txt created successfully.")
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")

# Step 2
# Build file2.txt with current Keplarian Elements
#
# LIST OF SATELLITES:
# Sat 01 - 25544 = International Space Station
# Sat 02 - 22825 = AO-27
# Sat 03 - 39444 = FUNcube-1, also known as AO-73
# Sat 04 - 43017 = AO-91 (Fox-1B)
# Sat 05 - 61781 = AO-123 ASRTU-OSCAR 123
# Sat 06 - 27607 = SO-50

with open('file2.txt', 'r+') as file:
    # Purge content from file2.txt
    # Important: move the cursor to the beginning before truncating
    file.seek(0) 
    file.truncate(0)

#Satellite 01
search_string_01 = "1 25544"
search_string_02 = "2 25544"

# Find & write Keplarian Data for Satellite 01
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   25544:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')
            
#Satellite 02
search_string_01 = "1 22825"
search_string_02 = "2 22825"

# Find & write Keplarian Data for Satellite 02
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   22825:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')
            
#Satellite 03
search_string_01 = "1 39444"
search_string_02 = "2 39444"

# Find & write Keplarian Data for Satellite 03
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   39444:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')
            
#Satellite 04
search_string_01 = "1 43017"
search_string_02 = "2 43017"

# Find & write Keplarian Data for Satellite 04
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   43017:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')

#Satellite 05
search_string_01 = "1 61781"
search_string_02 = "2 61781"

# Find & write Keplarian Data for Satellite 05
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   61781:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')

#Satellite 05
search_string_01 = "1 27607"
search_string_02 = "2 27607"

# Find & write Keplarian Data for Satellite 05
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_01 in file:
        if search_string_01 in line_01:
            print(f"   27607:['{line_01.strip()}',\n", file=target_file, end='')
#file.close()  # Must be called explicitly
with open("kepelements.txt", "r") as file, open('file2.txt', 'a') as target_file:
    for line_02 in file:
        if search_string_02 in line_02:
            print(f"          '{line_02.strip()}'],\n", file=target_file, end='')
print("file2.txt created successfully.")

# Step 3
# Combine files file1.txt, file2.txt and file3.txt into a single HTML page
# List of files to be merged
filenames = ['file1.txt', 'file2.txt', 'file3.txt']

# Open the destination file in write mode
with open('satellite_tracker.html', 'w') as outfile:
    for fname in filenames:
        # Open each input file in read mode
        with open(fname) as infile:
            # Read content and write it to the destination
            outfile.write(infile.read())
            # Optional: Add a newline between files
            outfile.write("\n")
print("satellite_tracker.html built successfully.")
