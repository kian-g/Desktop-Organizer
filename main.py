from simple_term_menu import TerminalMenu
from datetime import date
import os

file_extensions_set = set()


def main():
    while True:
        options = ["Enter file extensions", "Run", "Quit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        # If selecting file extensions
        if menu_entry_index == 0:

            extension_count = 0
            ask_extension = True
            while ask_extension:
                extension_count += 1

                ext = input(
                    f"> Enter file extension #{extension_count} (press return to stop): "
                )
                ext = ext.strip().lower().replace(".", "")

                if ext == "":
                    ask_extension = False
                    continue

                file_extensions_set.add(ext)

        # If selected run
        if menu_entry_index == 1:
            entering_dir = True

            # Loop to obtain the path to dir to organize
            while entering_dir:
                dir = input("> Enter directory to organize: ").strip()

                # Checks if input is blank or if the dir given does not exist
                if dir == "" or not os.path.isdir(dir):
                    print("Please enter a valid directory.")
                else:
                    print(f"Will organize this directory: {os.path.abspath(dir)}")
                    entering_dir = False

            print("Are you sure you want to run this? You cannot go back.")

            confirm_options = ["No", "Yes"]
            confirm_menu = TerminalMenu(confirm_options)
            confirm_entry_index = confirm_menu.show()

            # If confirm is 'No'
            if confirm_entry_index == 0:
                print("Canceling...")

            # If confirm is 'Yes'
            elif confirm_entry_index == 1:

                path = ""

                # Store created dirs to a folder so we can later check details relating to folders
                # we created
                created_dirs = []

                # Todays date to put in folder name as suffix
                today = date.today()

                # Create the designated folders
                for ext in file_extensions_set:
                    # ex for python files on Nov 18, 2025: py_2025-11-18
                    folder_name = f"{ext}_{str(today)}"
                    path = os.path.join(dir, folder_name)

                    # If the folder already exists
                    if os.path.isdir(path):
                        print(path, "is already a directory. Skipping creation.")

                        # Still append to the created dirs since the folder could be empty. If it is
                        # empty and it would've been created anyways from this script, delete as it
                        # should be deleted if it was created & is empty. This also ensures all
                        # folders that do not have content added are deleted as well since the user
                        # can type an extension of 'akjdhgsfk' and there are no files with it.
                        created_dirs.append(path)
                        continue

                    os.mkdir(path)
                    created_dirs.append(path)

                total_files_moved = 0

                for entry_name in os.listdir(dir):
                    _, file_ext = os.path.splitext(entry_name)
                    file_ext = file_ext.strip().lower().replace(".", "")

                    if file_ext in file_extensions_set:
                        current_file_path = os.path.join(dir, entry_name)
                        destination_dir = os.path.join(dir, f"{file_ext}_{str(today)}")
                        destination_file_path = os.path.join(
                            destination_dir, entry_name
                        )

                        try:
                            # Rename to move
                            os.rename(current_file_path, destination_file_path)
                            total_files_moved += 1
                        except FileNotFoundError:
                            print(f"The file {current_file_path} was not found!")
                        except:
                            print("An error occurred")

                print(f"Successfully organized {total_files_moved} files!")

                # If folder is empty after all files moved
                for folder in created_dirs:
                    if not os.listdir(folder):
                        os.rmdir(folder)
                        print(
                            f"Removed folder {folder} as it was empty after organization."
                        )

        # If quitting
        if menu_entry_index == 2:
            print("Quitting...")
            break


if __name__ == "__main__":
    main()
