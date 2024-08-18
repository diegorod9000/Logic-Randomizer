import os

def scan_directory_and_create_txt(directory_path, output_file):
    # Create/open the output file in write mode
    with open(output_file, 'w') as txt_file:
        txt_file.write("ALL_ALCHEMY = [\n")
        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Check if the file ends with ".acp"
                if file.endswith('.acp'):
                    # Remove the ".acp" extension
                    filename_without_extension = os.path.splitext(file)[0]
                    # Write the filename to the output file, followed by a newline
                    txt_file.write('"'+filename_without_extension + '",\n')
        txt_file.write("];")

# Example usage
directory_path = '/Library/Application Support/Logic/Plug-In Settings'
output_file = 'all_alchemy.js'
scan_directory_and_create_txt(directory_path, output_file)