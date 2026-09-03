local d = require("modules.keybinds.defaults")

-- Example binds, see https://wiki.hypr.land/Configuring/Basics/Binds/ for more

-- Switch workspaces with mainMod + [0-9]
-- Move active window to a workspace with mainMod + SHIFT + [0-9]
for i = 1, 10 do
    local key = i % 10 -- 10 maps to key 0
    hl.bind(d.mainMod .. " + " .. key,             hl.dsp.focus({ workspace = i}))
    hl.bind(d.mainMod .. " + SHIFT + " .. key,     hl.dsp.window.move({ workspace = i }))
end

-- Example special workspace (scratchpad)
hl.bind(d.mainMod .. " + S",         hl.dsp.workspace.toggle_special(d.ws_special))
hl.bind(d.mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:" .. d.ws_special }))

-- Scroll through existing workspaces with mainMod + scroll
hl.bind(d.mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind(d.mainMod .. " + mouse_up",   hl.dsp.focus({ workspace = "e-1" }))
