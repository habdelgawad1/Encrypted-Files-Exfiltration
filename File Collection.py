import os
def collect_files():
    collected = []
    extensions = [".txt", ".docx", ".jpg"]
    directory = os.path.dirname(os.path.abspath(__file__))

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                full_path = os.path.join(root, file)
                collected.append(full_path)

    log_file = os.path.join(directory, "files.log")  
    with open(log_file, "w") as log:
        for file_path in collected:
            log.write(file_path + "\n")

    print(f"{len(collected)} files found and logged in {log_file}")

collect_files()
