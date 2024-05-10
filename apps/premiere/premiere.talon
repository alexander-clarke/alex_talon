os: windows
app: adobe_premiere_pro
-

pause: key(space)

# parrot(shush): key(space)


# deck(pedal_left): user.ripple_trim_previous_edit_to_play_head()

# deck(pedal_middle): user.cut_at_play_head()

# deck(pedal_right): user.ripple_trim_next_edit_to_play_head()


shright | (shuttle right): user.shuttle_right()
shleft | (shuttle left): user.shuttle_left()

fleft | (frame left): user.frame_left()
fright | (frame right): user.frame_right()

cleft | (clip left): user.clip_left()
cright | (clip right): user.clip_right()

ripple left: user.ripple_trim_previous_edit_to_play_head()

ripple right: user.ripple_trim_next_edit_to_play_head()

trim left: user.trim_previous_edit_to_play_head()
trim right: user.trim_next_edit_to_play_head()

select forwards: key(shift-a)

speed change: key(ctrl-r)

feet moving: user.feet_moving()

feet cutting: user.feet_cutting()
