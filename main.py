from simple_term_menu import TerminalMenu
from datetime import date
import os

directory_path = "../"
files_exts = set()


def main():
    while True:
        options = ["Enter file extensions", "Run", "Quit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        # If selecting file extensions
        if menu_entry_index == 0:

            ext_count = 0
            ask_ext = True
            while ask_ext:
                ext_count += 1

                ext = input(
                    f"> Enter file extension #{ext_count} (press return to stop): "
                )
                ext = ext.strip().lower().replace(".", "")

                if ext == "":
                    ask_ext = False
                    continue

                files_exts.add(ext)

        if menu_entry_index == 1:
            entering_dir = True

            while entering_dir:
                dir = input("> Enter directory to organize: ").strip()

                if dir == "" or not os.path.isdir(dir):
                    print("Please enter a valid directory.")
                else:
                    print(f"Will organize this directory: {os.path.abspath(dir)}")
                    entering_dir = False

            print("Are you sure you want to run this? You cannot go back.")

            confirm_options = ["No", "Yes"]
            confirm_menu = TerminalMenu(confirm_options)
            confirm_entry_index = confirm_menu.show()

            if confirm_entry_index == 0:
                print("Canceling...")
            elif confirm_entry_index == 1:

                path = ""
                created_dirs = []

                today = date.today()
                # Create the designated folders
                for ext in files_exts:
                    # py_2025-11-18
                    folder_name = f"{ext}_{str(today)}"
                    path = os.path.join(dir, folder_name)

                    if os.path.isdir(path):
                        print(path, "is already a directory. Skipping creation.")
                        created_dirs.append(path)
                        continue

                    os.mkdir(path)
                    created_dirs.append(path)

                total_files_moved = 0

                for entry_name in os.listdir(dir):
                    file_name, file_ext = os.path.splitext(entry_name)
                    file_ext = file_ext.strip().lower().replace(".", "")

                    if file_ext in files_exts:
                        current_file_path = os.path.join(dir, entry_name)
                        destination_dir = os.path.join(dir, f"{file_ext}_{str(today)}")
                        destination_file_path = os.path.join(
                            destination_dir, entry_name
                        )

                        try:
                            os.rename(current_file_path, destination_file_path)
                            total_files_moved += 1
                        except FileNotFoundError:
                            print(f"The file {current_file_path} was not found!")
                        except:
                            print("An error occurred")

                print(f"Successfully organized {total_files_moved} files!")

                for folder in created_dirs:
                    if not os.listdir(folder):
                        os.rmdir(folder)
                        print(
                            f"Removed folder {folder} as it was empty after organization."
                        )

        if menu_entry_index == 2:
            print("Quitting...")
            break


main()
