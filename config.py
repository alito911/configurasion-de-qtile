# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#import os

#import subprocess

#from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os #PARA QUE FUNCIONE EL AUTOSTART

mod = "mod4"
terminal = guess_terminal()
color_barra ="#282a36"
tamaño_barra = 20
fuente_predeterminada = "Ubuntu Mono Nerd Font"
tamaño_fuente = 11
color_activo = "#f1fa8c"
tamaño_iconos = 18
tamaño_iconos2 = 16
color_fg = "#ffffff"
color_bg = "#282a36"
color_inactivo = "#ff9780"
color_oscuro = "#44475a"
color_claro = "#bd93f9"
color_urgent = "#ff5555"
color_texto1 = "#bd93f9"
color_grupo1 = "#ff7f00"
color_grupo2 = "#d600f7"
color_actualizaciones = "#bc0000"
dispositivo_red = "wlo2"
color_grupo3 = "#007bff"
color_grupo4 = "#c60000"

#espacio para definir las funciones

def fc_separador():
    return widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = color_fg,
            background = color_bg,
            )
def fc_separador2():
    return widget.Sep(
            linewidth = 0,
            padding = 145,
            foreground = color_fg,
            background = color_bg,
            )
#def fc_separador3():
#    return widget.Sep(
#            linewidth = 0,
#            padding = 50,
#            foreground = color_fg,
#            background = color_bg,
#            )

def fc_rectangulo(vColor,tipo):
    if tipo == 0:
        icono = ""
    else:
        icono = ""
    return widget.TextBox(
        text = icono,
        fontsize = tamaño_barra + 5,
        foreground = vColor,
        background = color_bg,
        padding = -1
    )

def fc_icono(icono,color_grupo):
    return widget.TextBox(
        text = icono,
        foreground = color_fg,
        background = color_grupo,
        fontsize = tamaño_iconos
    )

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawn("bash /home/tigo/.config/rofi/launchers/type-2/launcher.sh"), desc="Spawn a command using a prompt widget"),
    #bloqueo de pantalla
    Key([mod], "p", lazy.spawn("betterlockscreen -l")),
    #inisio de rofi
    Key([mod], "z", lazy.spawn("zsh /home/alejandro/.config/rofi/launchers/type-6/launcher.sh"), desc="abrir rofi"),
    #abrir aplicasiones
    Key([mod], "o",  lazy.spawn("gnome-boxes")),
    Key([mod], "u", lazy.spawn("firefox"), desc="abrir firefox"),
    Key([mod, "control"], "u", lazy.spawn("librewolf")),
    Key([mod], "i", lazy.spawn("code"), desc="abrir code"),
    Key([mod, "control"], "y", lazy.spawn("kitty ranger"), desc="gestor de archibo con terminal"),
    Key([mod, "control"], "t", lazy.spawn("Thunar"), desc="gestor de archibo comun"),
]

groups = [Group(i) for i in[
    " \uf303 ", " \uf489 ", " \ue743 ", " \ue70c ", " \uea83 ", " \ueb44 ", " \uea8c ", " \ueb65 ", " \uea6c "
    ]]

for i, group in enumerate(groups):
    numeroEscritorio =str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            #Or, use below if you prefer not to switch to that group.
             # mod1 + shift + letter of group = move focused window to group
               #Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #    desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1),
    layout.MonadTall(
        border_focus=["#A09F9F"],
        border_width=2,
        margin=6,
        single_border_width=0,
        single_margin=0
        ),
    layout.Max(),
     #Try more layouts by unleashing below layouts.
     #layout.Stack(num_stacks=2),
     #layout.Bsp(),
     #layout.Matrix(),
     #layout.MonadWide(
     #   border_focus=["#A09F9F"],
     #  border_width=2,
     #  margin=6,
     #  single_border_width=0,
     #  single_margin=0
     #  ),
     # layout.RatioTile(
     #     border_focus=["#A09F9F"],
     #    border_width=2,
     #   margin=6,
     #   single_border_width=0,
     #   single_margin=0
     #   ),
     #layout.Tile(),
     #layout.TreeTab(),
     #layout.VerticalTile(border_width=0),
     # layout.Zoomy(),
     layout.Floating(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
          top=bar.Bar(
        [
            widget.GroupBox(
                 active=color_activo,
                 border_width = 1,
                 disable_drag = True,
                 fontsize = tamaño_iconos,
                 fereground = color_fg,
                 highlight_method = "text",
                 inactive = color_inactivo,
                 margin_x = 0,
                 margin_y = 5,
                 other_screen_border = color_oscuro,
                 padding_x = 0,
                 padding_y = 10,
                 this_current_screen_border = color_claro,
                 this_screen_border = color_claro,
                 urgent_alert_method = "block",
                 urgent_border = color_urgent,
             ),
            #fc_separador(),
            #widget.Prompt(),
            #widget.WindowName(
            #    foreground = color_texto1,
            #    background = color_bg
            #),
            fc_separador2(),
            widget.Systray(),

            #widget.Systray(
            # icon_size = tamaño_iconos2,
            # background = color_bg,
            # ),
            #panel de recursos
            fc_rectangulo(color_grupo1, 0),
            fc_icono("", color_grupo1),
            widget.ThermalSensor(
                 foreground = color_fg,
                 background = color_grupo1,
                 threshold = 50,
                 tag_sensor = "Core 0",
                 fmt = "T1:{}"
             ),
            widget.ThermalSensor(
                 foreground = color_fg,
                 background = color_grupo1,
                 threshold = 50,
                 tag_sensor = "Core 1",
                 fmt = "T2:{}"
             ),
            fc_icono("  ", color_grupo1),
            widget.Memory(
                 foreground = color_fg,
                 background = color_grupo1
             ),
            fc_rectangulo(color_grupo1, 1),
            fc_separador(),

            #panel de atualizasiones
            fc_rectangulo(color_grupo2, 0),
            fc_icono("", color_grupo2),
            widget.CheckUpdates(
                 background = color_grupo2,
                 colour_have_updates = color_actualizaciones,
                 colour_no_updates = color_fg,
                 no_update_string = "0",
                 display_format = "Updates: {updates}",
                 update_interval = 3600,
                 distro="Arch_checkupdates",
                 execute="kitty -e sudo pacman -Syu"
             ),

            fc_icono(" 龍", color_grupo2),
            widget.Net (
                 foreground = color_fg,
                 background = color_grupo2,
                 format = "{down}   {up}",
                 interface = dispositivo_red,
                 use_bits = "true"
             ),
            fc_rectangulo(color_grupo2, 1),
            fc_separador(),

            #reloj
            fc_rectangulo(color_grupo3, 0),
            widget.Clock(
                 background = color_grupo3,
                 foreground = color_fg,
                 format="%d/%m/%Y %A %H:%M"
             ),
            fc_rectangulo(color_grupo3, 1),
            fc_separador(),
            fc_rectangulo(color_grupo4, 0),
            widget.CurrentLayoutIcon (
                 background = color_grupo4,
                 scale = 0.9
             ),
            widget.CurrentLayout(
                 background = color_grupo4
             ),
            fc_rectangulo(color_grupo4, 1),   
            ],
            tamaño_barra,
            background=color_barra,
            #fc_separador3(),
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
        # "zsh /home/alejandro/.screenlayout/resolucion.sh",
        "nitrogen --restore &",
        "picom --no-vsync &",
        "setxkbmap latam &",
        "udiskie -t &",
        "nm-applet &",
        "cbatticon -u 5 &",
        "volumeicon &",
]

for x in autostart:
    os.system(x)

#@hook.subscribe.startup_once

# def autostart():

#    home = os.path.expanduser('~')

#    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
