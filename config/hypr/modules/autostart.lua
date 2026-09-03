-- See https://wiki.hypr.land/Configuring/Basics/Autostart/

hl.on("hyprland.start", function () 
	-- GNOME Keyring
	hl.exec_cmd("dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP")
	hl.exec_cmd("gnome-keyring-daemon --start --components=secrets,ssh,pkcs11")
	
	-- Extensions
	hl.exec_cmd("hyprland-per-window-layout")
		
	-- Services
	hl.exec_cmd("systemctl --user start hyprpolkitagent")
	
	-- Apps and applets
	hl.exec_cmd("ashell")
	hl.exec_cmd("vicinae server")
end)
