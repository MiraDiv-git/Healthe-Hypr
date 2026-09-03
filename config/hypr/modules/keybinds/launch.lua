local d = require("modules.keybinds.defaults")

-- Example binds, see https://wiki.hypr.land/Configuring/Basics/Binds/ for more
hl.bind(d.mainMod .. " + Q", hl.dsp.exec_cmd(d.terminal))
hl.bind(d.mainMod .. " + E", hl.dsp.exec_cmd(d.fileManager))
hl.bind(d.mainMod .. " + B", hl.dsp.exec_cmd(d.browser))
hl.bind(d.mainMod .. " + R", hl.dsp.exec_cmd(d.menu))
