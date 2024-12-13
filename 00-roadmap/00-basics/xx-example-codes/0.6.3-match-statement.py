command = "Hello, world!"

match command:
    case "Hello, world!":
        print("Goodbye, World!")
    case "Goodbye, World!":
        print("See you later")
    case _:
        print("No match found")

# Advanced matching

command = "remove file1.txt file2.jpg file3.pdf"

match command.split():  # ["remove", "file1.txt", "file2.jpg", "file3.pdf"]
    case ["show"]:
        print("List all files and directories: ")
    case ["remove", *files]:
        print("Removing files: {}".format(files))
    case _:
        print("Command not recognized")

## pipe operator |

command = "delete file1.txt file2.jpg file3.pdf"

match command.split():  # ["remove", "file1.txt", "file2.jpg", "file3.pdf"]
    case ["show"]:
        print("List all files and directories: ")
    case ["remove" | "delete", *files]:
        print("Removing files: {}".format(files))
    case _:
        print("Command not recognized")

## conditional test in mach case

command = "remove file1.txt file2.jpg file3.pdf --ask"

match command.split():  # ["remove", "file1.txt", "file2.jpg", "file3.pdf", "--ask"]
    case ["show"]:
        print("List all files and directories: ")
    case ["remove" | "delete", *files] if "--ask" in files:
        print("Confirmation required before removing files")
        # extra logic to delete files
    case ["remove" | "delete", *files]:
        print("Removing files: {}".format(files))
    case _:
        print("Command not recognized")
