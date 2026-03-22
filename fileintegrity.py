import hashlib
import os
import json

# File to store hash values
HASH_STORE_FILE = "hash_store.json"


def calculate_file_hash(file_path):
    """
    Calculate SHA-256 hash of a file.

    Args:
        file_path (str): Path to the file

    Returns:
        str: Hexadecimal hash value
    """
    sha256 = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def scan_directory(directory):
    """
    Scan a directory and calculate hashes for all files.

    Args:
        directory (str): Directory path

    Returns:
        dict: {file_path: hash_value}
    """
    file_hashes = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            if file_hash:
                file_hashes[file_path] = file_hash

    return file_hashes


def load_previous_hashes():
    """
    Load stored hash values from file.

    Returns:
        dict: Stored hash values
    """
    if not os.path.exists(HASH_STORE_FILE):
        return {}

    with open(HASH_STORE_FILE, 'r') as file:
        return json.load(file)


def save_hashes(hashes):
    """
    Save hash values to file.

    Args:
        hashes (dict): File hash dictionary
    """
    with open(HASH_STORE_FILE, 'w') as file:
        json.dump(hashes, file, indent=4)


def compare_hashes(old_hashes, new_hashes):
    """
    Compare old and new hashes to detect changes.

    Args:
        old_hashes (dict): Previous hashes
        new_hashes (dict): Current hashes
    """
    print("\n--- File Integrity Report ---\n")

    # Check for modified files
    for file in old_hashes:
        if file in new_hashes:
            if old_hashes[file] != new_hashes[file]:
                print(f"[MODIFIED] {file}")
        else:
            print(f"[DELETED] {file}")

    # Check for new files
    for file in new_hashes:
        if file not in old_hashes:
            print(f"[NEW] {file}")

    print("\n--- Scan Complete ---\n")


def main():
    """
    Main function to run the integrity checker.
    """
    directory = input("Enter the directory path to monitor: ")

    if not os.path.exists(directory):
        print("Invalid directory path.")
        return

    print("\nScanning files...\n")

    new_hashes = scan_directory(directory)
    old_hashes = load_previous_hashes()

    if old_hashes:
        compare_hashes(old_hashes, new_hashes)
    else:
        print("No previous record found. Creating baseline...")

    save_hashes(new_hashes)
    print("Hash values stored successfully.")


if __name__ == "__main__":
    main()