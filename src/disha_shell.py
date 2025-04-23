import os
import subprocess

def disha_shell():
    print("🌟 Welcome to disha-shell! Type 'exit' to quit.\n")

    while True:
        try:
            # Show prompt with current directory
            current_dir = os.getcwd()
            cmd = input(f"disha-shell:{current_dir}> ").strip()

            if cmd == "":
                continue
            elif cmd == "exit":
                print("Goodbye! 👋")
                break
            elif cmd.startswith("cd"):
                # Change directory
                parts = cmd.split(maxsplit=1)
                if len(parts) > 1:
                    path = parts[1]
                else:
                    path = os.path.expanduser("~")  # go home
                try:
                    os.chdir(path)
                except Exception as e:
                    print(f"❌ cd: {e}")
            else:
                # Run other shell commands
                subprocess.run(cmd, shell=True)
        except KeyboardInterrupt:
            print("\n🛑 Use 'exit' to quit.")
        except EOFError:
            print("\nBye!")
            break

if __name__ == "__main__":
    disha_shell()
