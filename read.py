def modify_content(lines):
    """Add line numbers to each line."""
    return [f"{i+1}: {line}" for i, line in enumerate(lines)]

def main():
    filename = input("📂 Enter the name of the file to read from: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.readlines()
            print("✅ File read successfully.")

        modified = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.writelines(modified)
            print(f"✏️ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("🚫 Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
