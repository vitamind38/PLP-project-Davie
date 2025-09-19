def file_read_write():
    filename = input("Enter the name of the file to read: ")
    
    try:
        
        with open(filename, "r") as file:
            content = file.read()
        
        
        modified_content = content.upper()
        
        
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)
        
        print("File read successfully ✅")
        print("Modified content written to 'output.txt'")
    
    except FileNotFoundError:
        print("Error: The file does not exist ❌")
    except IOError:
        print("Error: Could not read the file ❌")


file_read_write()
