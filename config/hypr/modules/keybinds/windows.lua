local d = require("modules.keybinds.defaults")

-- Example binds, see https://wiki.hypr.land/Configuring/Basics/Binds/ for more
hl.bind(d.mainMod .. " + C", hl.dsp.window.close())
hl.bind(d.mainMod .. " + V", hl.dsp.window.float({ action = "toggle" }))
hl.bind(d.mainMod .. " + P", hl.dsp.window.pseudo())
hl.bind(d.mainMod .. " + J", hl.dsp.layout("togglesplit"))    -- dwindle only
hl.bind(d.mainMod .. " + F", hl.dsp.window.fullscreen())

-- Move focus with mainMod + arrow keys
hl.bind(d.mainMod .. " + left",  hl.dsp.focus({ direction = "left" }))
hl.bind(d.mainMod .. " + right", hl.dsp.focus({ direction = "right" }))
hl.bind(d.mainMod .. " + up",    hl.dsp.focus({ direction = "up" }))
hl.bind(d.mainMod .. " + down",  hl.dsp.focus({ direction = "down" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind(d.mainMod .. " + mouse:272", hl.dsp.window.drag(),   { mouse = true })
hl.bind(d.mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })
