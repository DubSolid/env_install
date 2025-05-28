from dataclasses import dataclass, field
import subprocess
import os
import shutil


@dataclass
class Path:
    repo_name:  str = field(default_factory=lambda: "env_install")
    url:        str = field(default_factory=lambda: "https://github.com/DubSolid/env_install")
    repo_path:  str = field(default_factory=lambda: "./env_install")

    nvim_source: str = field(init=False)
    tmux_source: str = field(init=False)
    nvim_target_directory: str = field(init=False)
    tmux_target_directory: str = field(init=False) 

    def __post_init__(self):
        self.nvim_source = os.path.join(self.repo_path, "nvim")
        self.tmux_source = os.path.join(self.repo_path, "tmux")
        self.nvim_target_directory = os.path.expanduser("~/.config/nvim")
        self.tmux_target_directory = os.path.expanduser("~/.config/tmux")
    

def download_repo(paths: Path):
    if not os.path.exists(paths.repo_name):
        try:
            subprocess.run(["git", "clone", paths.url], check=True)
            print("Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repo: {e}")
    else:
        print(f"Repository '{paths.repo_name}' already exists.")


def copy_files(paths: Path):
    if not os.path.exists(paths.nvim_target_directory):
        try:
            shutil.copytree(paths.nvim_source, paths.nvim_target_directory)
            print("Neovim files successfully copied to target path.")
        except Exception as e:
            print(f"Failed to copy nvim files: {e}")
    else:
        print(f"Directory '{paths.nvim_target_directory}' already exists.")

    if not os.path.exists(paths.tmux_target_directory):
        try:
            shutil.copytree(paths.tmux_source, paths.tmux_target_directory)
            print("Tmux files successfully copied to target path.")
        except Exception as e:
            print(f"Failed to copy tmux files: {e}")
    else:
        print(f"Directory '{paths.tmux_target_directory}' already exists.")


if __name__ == "__main__":
    paths = Path()
    download_repo(paths)
    copy_files(paths)
