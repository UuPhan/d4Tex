import os
import shutil

meta_folder = "./meta/Texture/"
payload_folder = "./payload/Texture/"
process_folder = "./_process/"

# Loop through files in the meta folder
for filename in os.listdir(meta_folder):
    meta_file_path = os.path.join(meta_folder, filename)

    with open(meta_file_path, "rb") as meta_file:
        meta_file.seek(24)
        fmeta = meta_file.read(2)
        meta_file.seek(32)
        hmeta = meta_file.read(4)

    # Find the corresponding file in the payload folder
    payload_file_path = os.path.join(payload_folder, filename)

    # Check if the payload file exists
    if os.path.isfile(payload_file_path):
        # Create the process folder if it doesn't exist
        os.makedirs(process_folder, exist_ok=True)

        # Create the new file path in the process folder
        process_file_path = os.path.join(process_folder, filename)

        # Copy the payload file to the process folder
        shutil.copyfile(payload_file_path, process_file_path)

        # Open the copied file in binary mode
        with open(process_file_path, "r+b") as process_file:
            file_content = process_file.read()
            process_file.seek(0)
            process_file.write(fmeta)
            process_file.write(hmeta)
            process_file.write(file_content)
            
        print(f"Processed file: {filename}")
    else:
        print(f"Payload file not found for: {filename}")
