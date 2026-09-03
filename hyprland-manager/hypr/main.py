#!/usr/bin/env python3
import argparse
import subprocess

config = {
    "hypr_version": "0.1.0",
    "hyman_version": "unreleased"
}

version_string = f"""hypr: {config['hypr_version']}
hyman: {config['hyman_version']}"""

def exec(cmd: str):
    subprocess.run(cmd, shell=True)

parser = argparse.ArgumentParser(
    prog="hypr",
    description="Healthe Hypr CLI manager",
    formatter_class=argparse.RawTextHelpFormatter
)

# version
parser.add_argument(
    '-v', '--version', 
    action='version', 
    version=version_string
)

subparsers = parser.add_subparsers(dest="command", title="commands", metavar="<command>")



##################
### ARGS BLOCK ###
##################

# exit
exit_parser = subparsers.add_parser("exit", help="Exit Hyprland session")

# edit
edit_parser = subparsers.add_parser("edit", help="Edit config file in ~/.config/hypr/")
edit_parser.add_argument("file", nargs="?", help="Name of the file to edit")
edit_parser.add_argument('-rm', '--remove', nargs="+", metavar="FILE", help="Removes config files")
edit_parser.add_argument('-e', '--editor', type=str, help="Editor binary (default: nano)")
edit_parser.add_argument('-l', '--list', action="store_true", help="Shows all config files")

# pkg general flags
pkg_parent = argparse.ArgumentParser(add_help=False)
pkg_parent.add_argument("--aur", action="store_true", default=argparse.SUPPRESS, help="Use yay instead of pacman")
pkg_parent.add_argument("-y", "--noconfirm", action="store_true", default=argparse.SUPPRESS, help="Bypass confirmation prompts")

# pkg
pkg_parser = subparsers.add_parser("pkg", help="Manage system packages", parents=[pkg_parent])
pkg_subparsers = pkg_parser.add_subparsers(dest="pkg_action", metavar="<action>")

# pkg install
install_p = pkg_subparsers.add_parser("install", help="Install package", parents=[pkg_parent])
install_p.add_argument("package", help="Package name")

# pkg remove
remove_p = pkg_subparsers.add_parser("remove", help="Remove package", parents=[pkg_parent])
remove_p.add_argument("package", help="Package name")
remove_p.add_argument("--force", action="store_true", default=argparse.SUPPRESS, help="Force remove breaking dependencies (-Rdd)")

# pkg unorphan
pkg_subparsers.add_parser("unorphan", help="Remove orphan packages", parents=[pkg_parent])

# pkg search
search_p = pkg_subparsers.add_parser("search", help="Search package", parents=[pkg_parent])
search_p.add_argument("query", help="Search query")

# pkg list
pkg_subparsers.add_parser("list", help="List installed packages", parents=[pkg_parent])

# pkg info
info_p = pkg_subparsers.add_parser("info", help="Show package info", parents=[pkg_parent])
info_p.add_argument("package", help="Package name")

# pkg update
update_p = pkg_subparsers.add_parser("update", help="Fetches package database", parents=[pkg_parent])

#pkg upgrade
upgrade_p = pkg_subparsers.add_parser("upgrade", 
    help="Upgrades selected package or everything if nothing scepified", parents=[pkg_parent])
upgrade_p.add_argument("package", nargs="?", help="Package name")

# pkg pull
pull_p = pkg_subparsers.add_parser("pull", help="Pulls package from AUR", parents=[pkg_parent])
pull_p.add_argument("package", help="Package name")

args = parser.parse_args()



###################
### LOGIC BLOCK ###
###################

if args.command == "exit":
    exec("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch 'hl.dsp.exit()'")


elif args.command == "edit":
    BLACKLIST = { "hyprland", "hyprland.lua", "hyprland.conf",
                  "hyprpaper.conf", "hyprpaper.lua" }

    if args.remove:
        to_delete = []
        for f in args.remove:
            if f in BLACKLIST:
                print(f"Error: '{f}' is protected and cannot be removed.")
            else:
                to_delete.append(f"~/.config/hypr/{f}")
        
        if to_delete:
            exec(f"rm -f {' '.join(to_delete)}")

    elif getattr(args, "list", False):
        exec("ls ~/.config/hypr/")
    elif args.file:
        editor = args.editor if args.editor else "nano"
        exec(f"{editor} ~/.config/hypr/{args.file}")
    else:
        edit_parser.print_help()


elif args.command == "pkg":
    is_aur = getattr(args, "aur", False)
    noconfirm = " --noconfirm" if getattr(args, "noconfirm", False) else ""
    pm = "yay" if is_aur else "sudo pacman"
    
    if args.pkg_action == "install":
        exec(f"{pm} -S{noconfirm} {args.package}")
    elif args.pkg_action == "remove":
        rm_flag = "-Rdd" if getattr(args, "force", False) else "-Rns"
        exec(f"{pm} {rm_flag}{noconfirm} {args.package}")
    elif args.pkg_action == "unorphan":
        cmd = f"yay -Qtdq | yay -Rns{noconfirm} -" if is_aur else f"sudo pacman -Rns{noconfirm} $(pacman -Qtdq)"
        exec(cmd)
    elif args.pkg_action == "search":
        exec(f"{pm} -Ss {args.query}")
    elif args.pkg_action == "list":
        exec(f"{pm} -Qe")
    elif args.pkg_action == "info":
        exec(f"{pm} -Si {args.package}")
    elif args.pkg_action == "update":
        exec(f"{pm} -Sy")
    elif args.pkg_action == "upgrade":
        if args.package:
            exec(f"{pm} -Syu {args.package}")
        else:
            exec(f"{pm} -Syu")
    elif args.pkg_action == "pull":
        if is_aur:
            exec(f"yay -G {args.package}")
        else:
            print("This command can be executed only with --aur")
    else:
        pkg_parser.print_help()

else:
    parser.print_help()