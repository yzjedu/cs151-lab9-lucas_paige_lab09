# Algorithm Document

Purpose: Ask the user what file they want to choose.  
Name: read_filename  
Parameters: none  
Return: filename  
Algorithm: 
1. ask the user the file name they want saved as filename
2. while the input is not the name of a file
   1. Prompt the user to enter the filename
3. Return the filename

Purpose: Read the file to a list    
Name: read_file_to_list  
parameter: filename    
Return: names  
Algorithm:  
1. set file data to oen the filename for reading
2. set names list to read the lines of the file data
3. close the file data
4. return the names list

Purpose: Assign the seats to the names  
Name: assign_seats  
Parameter: names  
Return: none   
Algorithm:
1. set table_count to 1
2. set seat count to 1
3. for name in names
   4. output message: 'Table {table}, Seat {seat}, {name}
   6. if seat == 5
      7. set seat to 1
      8. add 1 to table
