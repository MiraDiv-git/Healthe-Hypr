------------------
-- ENTRY POINT ---
------------------

-- Use this file only to import other scripts
-- Refer to the wiki for more information.
-- https://wiki.hypr.land/Configuring/Start/

-- Basic modules
require("modules.monitors")
require("modules.autostart")
require("modules.envars")
require("modules.permissions")
require("modules.input")
require("modules.winrules")

-- Look and Feel
require("modules.look.general")
require("modules.look.curves")
require("modules.look.animations")
require("modules.look.workspaces")
require("modules.look.layouts")
require("modules.look.misc")

-- Keybinds
require("modules.keybinds.launch")
require("modules.keybinds.windows")
require("modules.keybinds.workspaces")
require("modules.keybinds.multimedia")
