def process_file():
    """
    Reads a file, modifies its content (adds line numbers), 
    and saves a new version with error handling.
    """
    print("\n=== File Processor ===")
    
    while True:
        input_file = input("Enter the filename to read: ").strip()
        if input_file:
            break
        print("⚠️ Error: Filename cannot be empty. Try again.")
    
    output_file = f"modified_{input_file}"

    try:
        # Read the file
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            if not lines:
                raise ValueError("⚠️ Error: The file is empty.")
            
            # Modify content (add line numbers)
            modified_content = [f"{i+1}: {line}" for i, line in enumerate(lines)]
            
        # Write to new file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(modified_content)
            
        print(f"✅ Success! Modified file saved as '{output_file}'")
        print(f"📝 Total lines processed: {len(lines)}")
    
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
    except PermissionError:
        print(f"❌ Error: No permission to read '{input_file}'.")
    except UnicodeDecodeError:
        print("❌ Error: Cannot read binary or non-text file.")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__} - {e}")
    finally:
        print("\n🔚 File processing complete.")

if __name__ == "__main__":
    process_file()