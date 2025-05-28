import subprocess
import os
import shutil

def download_and_copy():
    repo_name = "env_install"
    url = "https://github.com/DubSolid/env_install"

    nvim_target_directory = os.path.expanduser("~/.config/nvim")
    tmux_target_directory = os.path.expanduser("~/.config/tmux")

    repo_path = "./env_install"
    nvim_source = os.path.join(repo_path, "nvim")
    tmux_source = os.path.join(repo_path, "tmux")

    # TODO: Check if repo is already cloned correctly
    if not os.path.exists(repo_name):
        try:
            subprocess.run(["git", "clone", url], check=True)
            print("Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repo: {e}")
    else:
        print(f"Repository '{repo_name}' already exists.")

    if not os.path.exists(nvim_target_directory):
        try:
            shutil.copytree(nvim_source, nvim_target_directory)
            print("Neovim files successfully copied to target path.")
        except Exception as e:
            print(f"Failed to copy nvim files: {e}")
    else:
        print(f"Directory '{nvim_target_directory}' already exists.")

    if not os.path.exists(tmux_target_directory):
        try:
            shutil.copytree(tmux_source, tmux_target_directory)
            print("Tmux files successfully copied to target path.")
        except Exception as e:
            print(f"Failed to copy tmux files: {e}")
    else:
        print(f"Directory '{tmux_target_directory}' already exists.")

if __name__ == "__main__":
    download_and_copy()

