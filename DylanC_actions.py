# This project is designed to handle automation in Ableton Live, a digital audio workstation. This is a work
# in progress, and I continue to update it as I need to. MIDI controllers have knobs, sliders, and buttons
# that can be mapped to different controls in the program, such as volume and play/stop for different tracks
# or slots. Without this script, a slider can be mapped to one thing at a time, which is quite limiting. This code
# allows me to dynamically map differnt buttons depending on anything I want. For example, I can map a button to
# do one thing and immediately remap it something else. It also allows me to have different modes, so that I can
# cycle through different layouts depending on what I am working on, such as having one map for when I am recording,
# and another map for when I'm editing notes in a MIDI track.

# I am actually doing this on Obsidian damn

from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# I've set up my default project template to have different groups of tracks, and because audio tracks are
# different from midi tracks, many actions behave differently depending on which type they belong to.
instrument_list = ['drum', 'vocal', 'synth', 'keyboard', 'guitar', 'bass', 'soundfx', 'ambience']
midi_groups = ['drum', 'synth', 'keyboard', 'soundfx', 'ambience']
audio_groups = ['vocal', 'guitar', 'bass']

# Dictionary with assignments for controls on the midi device. Right now I only have one map, but I will add more
# in the future.
menu_dict = {1: ['Basic', {'Faders': {'FADER_DAW_01': '"%ssend 1"/VOL',
                                      'FADER_DAW_02': '"%ssend 2"/VOL',
                                      'FADER_DAW_03': '"%ssend 3"/VOL',
                                      'FADER_DAW_04': '"%ssend 4"/VOL',
                                      'FADER_DAW_05': '"%ssend 5"/VOL',
                                      'FADER_DAW_06': '"%ssend 6"/VOL',
                                      'FADER_DAW_07': '"%ssend 7"/VOL',
                                      'FADER_DAW_08': '"%ssend 8"/VOL',
                                      'FADER_DAW_09': '"%s group"/VOL',
                                      },
                           'Knobs': {'ENC_DAW_01': 'SEL/DEV(SEL) P1',
                                     'ENC_DAW_02': 'SEL/DEV(SEL) P2',
                                     'ENC_DAW_03': 'SEL/DEV(SEL) P3',
                                     'ENC_DAW_04': 'SEL/DEV(SEL) P4',
                                     'ENC_DAW_05': 'SEL/DEV(SEL) P5',
                                     'ENC_DAW_06': 'SEL/DEV(SEL) P6',
                                     'ENC_DAW_07': 'SEL/DEV(SEL) P7',
                                     'ENC_DAW_08': 'SEL/DEV(SEL) P8',
                                     },
                           'Transport': {'$BTN_SAVE$': 'SEL/SNAP_DRUMS',
                                         '$BTN_UNDO$': '"drum set routing"/DEV(1.ALL.1) RESET',
                                         '$BTN_PUNCH$': 'SEL/SNAP_DRUMS_RECALL',
                                         '$BTN_METRO$': 'METRO',
                                         '$BTN_CAT_CHAR$': 'LEFT',
                                         '$BTN_PRESET$': 'RIGHT',
                                         '$BTN_LOOP$': 'SEL/MUTE',
                                         '$BTN_TRANSPORT_LEFT$': 'LEFT',
                                         '$BTN_TRANSPORT_RIGHT$': 'RIGHT',
                                         '$KNOB_PUSH$': 'KNOB_SWITCH mode',
                                         '$PART_1_ON$': 'PAD_FUNCTION +',
                                         '$PART_2_ON$': 'PAD_FUNCTION -',
                                         '$PART_1_OFF$': 'BANK_UP',
                                         '$PART_2_OFF$': 'BANK_DOWN',
                                         '$SUSTAIN_PEDAL_C$': 'PEDAL_REC record',
                                         'EXPRESSION_PEDAL': '"routing"/DEV(1) P1'
                                         },
                           'Knob Functions Up-Down': {"$KNOB_UP_11$": "SEL/SCENE_MOVE UP-11",
                                                      "$KNOB_UP_10$": "SEL/SCENE_MOVE UP-10",
                                                      "$KNOB_UP_9$": "SEL/SCENE_MOVE UP-9",
                                                      "$KNOB_UP_8$": "SEL/SCENE_MOVE UP-8",
                                                      "$KNOB_UP_7$": "SEL/SCENE_MOVE UP-7",
                                                      "$KNOB_UP_6$": "SEL/SCENE_MOVE UP-6",
                                                      "$KNOB_UP_5$": "SEL/SCENE_MOVE UP-5",
                                                      "$KNOB_UP_4$": "SEL/SCENE_MOVE UP-4",
                                                      "$KNOB_UP_3$": "SEL/SCENE_MOVE UP-3",
                                                      "$KNOB_UP_2$": "SEL/SCENE_MOVE UP-2",
                                                      "$KNOB_UP_1$": "SEL/SCENE_MOVE UP-1",
                                                      "$KNOB_DOWN_1$": "SEL/SCENE_MOVE DOWN-1",
                                                      "$KNOB_DOWN_2$": "SEL/SCENE_MOVE DOWN-2",
                                                      "$KNOB_DOWN_3$": "SEL/SCENE_MOVE DOWN-3",
                                                      "$KNOB_DOWN_4$": "SEL/SCENE_MOVE DOWN-4",
                                                      "$KNOB_DOWN_5$": "SEL/SCENE_MOVE DOWN-5",
                                                      "$KNOB_DOWN_6$": "SEL/SCENE_MOVE DOWN-6",
                                                      "$KNOB_DOWN_7$": "SEL/SCENE_MOVE DOWN-7",
                                                      "$KNOB_DOWN_8$": "SEL/SCENE_MOVE DOWN-8",
                                                      "$KNOB_DOWN_9$": "SEL/SCENE_MOVE DOWN-9",
                                                      "$KNOB_DOWN_10$": "SEL/SCENE_MOVE DOWN-10",
                                                      "$KNOB_DOWN_11$": "SEL/SCENE_MOVE DOWN-11"
                                                      },
                           'Knob Functions Left-Right': {"$KNOB_UP_1$": "SEL/LR_MOVE LEFT-1",
                                                         "$KNOB_UP_2$": "SEL/LR_MOVE LEFT-2",
                                                         "$KNOB_UP_3$": "SEL/LR_MOVE LEFT-3",
                                                         "$KNOB_UP_4$": "SEL/LR_MOVE LEFT-4",
                                                         "$KNOB_UP_5$": "SEL/LR_MOVE LEFT-5",
                                                         "$KNOB_UP_6$": "SEL/LR_MOVE LEFT-6",
                                                         "$KNOB_UP_7$": "SEL/LR_MOVE LEFT-7",
                                                         "$KNOB_UP_8$": "SEL/LR_MOVE LEFT-8",
                                                         "$KNOB_UP_9$": "SEL/LR_MOVE LEFT-9",
                                                         "$KNOB_UP_10$": "SEL/LR_MOVE LEFT-10",
                                                         "$KNOB_UP_11$": "SEL/LR_MOVE LEFT-11",
                                                         "$KNOB_DOWN_1$": "SEL/LR_MOVE RIGHT-1",
                                                         "$KNOB_DOWN_2$": "SEL/LR_MOVE RIGHT-2",
                                                         "$KNOB_DOWN_3$": "SEL/LR_MOVE RIGHT-3",
                                                         "$KNOB_DOWN_4$": "SEL/LR_MOVE RIGHT-4",
                                                         "$KNOB_DOWN_5$": "SEL/LR_MOVE RIGHT-5",
                                                         "$KNOB_DOWN_6$": "SEL/LR_MOVE RIGHT-6",
                                                         "$KNOB_DOWN_7$": "SEL/LR_MOVE RIGHT-7",
                                                         "$KNOB_DOWN_8$": "SEL/LR_MOVE RIGHT-8",
                                                         "$KNOB_DOWN_9$": "SEL/LR_MOVE RIGHT-9",
                                                         "$KNOB_DOWN_10$": "SEL/LR_MOVE RIGHT-10",
                                                         "$KNOB_DOWN_11$": "SEL/LR_MOVE RIGHT-11",
                                                         },
                           }]}

# This dictionary is used for an action that lets me remap notes on my MIDI drum set conviently and quickly.
drum_dict = {'kick': [1, 1, 36],
             'hhpedal': [1, 2, 44],
             'closedhh': [1, 3, 42],
             'halfhh': [1, 4, 76],
             'openhh': [1, 5, 46],
             'crash': [1, 6, 49],
             'ride': [1, 7, 51],
             'china': [1, 8, 57],
             'snare': [2, 1, 38],
             'snarerim': [2, 2, 39],
             'tom1': [2, 3, 47],
             'tom1rim': [2, 4, 71],
             'tom2': [2, 5, 45],
             'tom2rim': [2, 6, 69],
             'tom3': [2, 7, 43],
             'tom3rim': [2, 8, 67],
             'tom4': [3, 1, 41],
             'tom4rim': [3, 2, 65]
             }

# Right now I have two modes for a knob in the center of the controller, wich I use to cycle through tracks left
# and right, or go up and down, and I can push the knob down to switch between them
knob_functions = [[1, 'recording_length', 'knob_switch left', 'knob_switch right'],
                  [2, 'prev_next', 'left', 'right']]


class DylanC_actions(UserActionsBase):

#Listed here are all the actions I define in the code below, as well as some variables that I use in those actions
    def create_actions(self):
        self.current_bank = 1
        self.visible_tracks = []
        self.track_index = 0
        self.tracklist_length = 0
        self.track_group = ''
        self.current_drum_ = ''
        self.current_pad_mapping = 1
        self.drum_set_routing_index = 0
        self.recording_length_8count = float(1)
        self.current_push_knob = 2
        self.up_down_true = True
        self.current_cs_mapping = 1
        self.add_global_action('trigger_action_list', self.trigger_action_list)
        self.add_global_action('show_message', self.show_message)
        self.add_global_action('knob_mapping', self.knob_mapping)
        self.add_global_action('knob_switch', self.knob_switch)
        self.add_global_action('track_mixdown', self.track_mixdown)
        self.add_global_action('cs_mapping', self.cs_mapping)
        self.add_global_action('pedal_rec', self.pedal_rec)
        self.add_track_action('current_drum', self.current_drum)
        self.add_global_action('modify_drum', self.modify_drum)
        self.add_track_action('snap_drums', self.snap_drums)
        self.add_track_action('snap_drums_recall', self.snap_drums_recall)
        self.add_track_action('device_snap', self.device_snap)
        self.add_global_action('bank_up', self.bank_up)
        self.add_global_action('bank_down', self.bank_down)
        self.add_global_action('bind_bank', self.bind_bank)
        self.add_global_action('pad_function', self.pad_function)
        self.add_track_action('next_inst_track', self.next_inst_track)
        self.add_track_action('prev_inst_track', self.prev_inst_track)
        self.add_track_action('silence_multiple', self.silence_multiple)
        self.add_track_action('arm_multiple', self.arm_multiple)
        self.add_track_action('stop_nq', self.stop_nq)
        self.add_track_action('midi_transpose_16down', self.midi_transpose_16down)
        self.add_track_action('midi_transpose_16up', self.midi_transpose_16up)
        self.add_track_action('stop_everything', self.stop_everything)
        self.add_track_action('contextual_stop_recording', self.contextual_stop_recording)
        self.add_track_action('contextual_del_clip', self.contextual_del_clip)
        self.add_track_action('contextual_rec_clip', self.contextual_rec_clip)
        self.add_track_action('scene_move', self.scene_move)
        self.add_track_action('lr_move', self.lr_move)
        self.add_track_action('rename_clip', self.rename_clip)
        self.add_track_action('trackgroup', self.trackgroup)


    # Shortcut to trigger an action without typing the code out each time
    def trigger_action_list(self, args):
        self.canonical_parent.clyphx_pro_component.trigger_action_list(str(args))

    # Shortcut to show a message to the screen without typing the code out each time
    def show_message(self, args):
        self.canonical_parent.show_message(str(args))

    # This is the code to switch between the up-down and left-right functionality of the center knob on the controller
    def knob_mapping(self, args):
        if self.up_down_true is True:
            self.up_down_true = False
            menu_choice = menu_dict[1][1]['Knob Functions Left-Right']
            self.show_message('Left Right mapping active')
        else:
            self.up_down_true = True
            menu_choice = menu_dict[1][1]['Knob Functions Up-Down']
            self.show_message('Up Down mapping active')

        for knob in menu_choice:
            self.trigger_action_list("%s = %s" % (knob, menu_choice[knob]))

    # My orignal idea for changing the length of bars to record if I'm recording a set number of bars. Not
    # yet implemented with the mode maps, but I will modify in the future
    def knob_switch(self, action_def, args):
        # If center knob is pushed cycle through knob functions in knob_funtions dictionary and assign left
        # and right accordingly
        if args == 'mode':
            if self.current_push_knob < len(knob_functions):
                self.current_push_knob += 1
            elif self.current_push_knob == len(knob_functions):
                self.current_push_knob = 1
            self.trigger_action_list('$BTN_C19$ = %s' % knob_functions[self.current_push_knob - 1][2])
            self.trigger_action_list('$BTN_C20$ = %s' % knob_functions[self.current_push_knob - 1][3])
            self.knob_mapping(args)
        # If the center knob is rotated 1 notch counterclockwise, set recording_length_8count variable to half
        # it's original value, unless it's at 1 bar (.125 * 8 = 1 bar), in wich case cycle back to 16. Same idea
        # reversed if rotated clockwise
        elif args == 'left':
            if self.recording_length_8count == 0.125:
                self.recording_length_8count = 16
            else:
                self.recording_length_8count = self.recording_length_8count / 2

        elif args == 'right':
            if self.recording_length_8count == 16:
                self.recording_length_8count = 0.125
            else:
                self.recording_length_8count = self.recording_length_8count * 2

    # Send output of all tracks armed in a track group to the designated mixdown track. Play records all of the
    # tracks until play is pressed again, and the recording stops. Delete lets you re-record in the same slot.
    # Off puts everything back to normal
    def track_mixdown(self, action_def, args):
        if args == 'on':
            track_list = []
            # Put all tracks that are armed into track_list
            for x in range(1, 9):
                if self.song().visible_tracks[self.track_index + 1 + x].arm is True:
                    track_list.append(x)
            # Remap tracks in track_list to send their outputs to the mix track for whatever track
            # I'm currently in.
            for x in track_list:
                self.trigger_action_list('"%ssend %s"/OUT "%smix"' % (self.track_group, x, self.track_group))
        # Make output of each track go back to the group audio track
        elif args == 'off':
            for x in range(1, 9):
                self.trigger_action_list('"%ssend %s"/OUT "%s group"' % (self.track_group, x, self.track_group))
        # Play the clip slot to record armed tracks. Natural behavior of the program is to stop recording
        # when play is hit again, so I don't have to code for that
        elif args == 'play':
            self.trigger_action_list('"%smix"/PLAY SEL' % self.track_group)
        # Delete the audio file in the mixdown clip slot
        elif args == 'delete':
            self.trigger_action_list('"%smix"/CLIP(SEL) DEL' % self.track_group)

    # Map everything to the layout described in the menu_dict. Not useful yet since I only have one map written
    # out so far, but this will soon change. Macros, which begin with $, are assigned with the '=' symbol, while
    # knobs use the 'BIND' keyword. Faders are skipped because they are bound with a different action
    def cs_mapping(self, action_def, args):
        for control_group in menu_dict[self.current_cs_mapping][1]:
            if control_group == 'Faders':
                continue
            for control in menu_dict[self.current_cs_mapping][1][control_group]:
                if '$' in control:
                    self.trigger_action_list('%s = %s' %
                                             (control, menu_dict[self.current_cs_mapping][1][control_group][control]))
                else:
                    self.trigger_action_list('BIND %s %s' %
                                             (control, menu_dict[self.current_cs_mapping][1][control_group][control]))
    # For a specific pedal, pressing it records all armed tracks in the group, and remaps it to stop. Pressing
    # it again stops all armed tracks in the group, and remaps it to record.
    def pedal_rec(self, action_def, args):
        if args == 'record':
            self.trigger_action_list('SEL/CONTEXTUAL_REC_CLIP')
            self.trigger_action_list('$SUSTAIN_PEDAL_C$ = PEDAL_REC stop')
        elif args == 'stop':
            self.trigger_action_list('SEL/CONTEXTUAL_STOP_RECORDING')
            self.trigger_action_list('$SUSTAIN_PEDAL_C$ = PEDAL_REC record')

    # These next four actions are used to change the mappings on a MIDI drum set I have. Remapping drums can
    # can be tedious, and lots of clicking wastes time. These actions make the process quick and easy, and
    # I've coded it so configurations can be saved and recalled when needed.
    def current_drum(self, action_def, args):
        # Resets the functions of the center knob to the default up/down scene action
        if args == 'clear':
            for knob in menu_dict[1][1]['Knob Functions Up-Down']:
                self.trigger_action_list("%s = %s" % (knob, menu_dict[1][1]['Knob Functions Up-Down'][knob]))
        else:
            # Records which drum is being hit depending on incoming midi signal on a track, and getting values
            # from the drum_dict dictionary
            chain = drum_dict[args][0]
            parameter = drum_dict[args][1]
            # Get the index of the 'drum set routing' track by cycling through the list of visible tracks.
            # I could just find the index and use that, but if I ever add a track to my default template I'd
            # have to remember and modify this, which I would like to avoid if possible
            x = 0
            while self.visible_tracks[x].name != 'drum set routing':
                x += 1

            self.drum_set_routing_index = x
            # Determine amount the current drum is being transposed by accessing the parameter that controls
            # MIDI transposing for that drum, and subtracting 63, which is the value for 0 notes transposed
            # in the plugin
            amount_transposed = (int(self.song().visible_tracks[self.drum_set_routing_index].devices[0].
                                     chains[chain - 1].devices[0].parameters[parameter].value)) - 63

            # The center knob can be turned quickly to transpose up to 11 in a single input at most. This binds
            # turning left and right to the KNOB_UP and KNOB_DOWN macros for the specific drum selected
            for x in range(1, 12):
                knob = '$KNOB_UP_%s$' % x
                self.trigger_action_list('%s = "drum set routing"/DEV(1.%s.1) P%s <%s ; MODIFY_DRUM %s'
                                         % (knob, chain, parameter, x, args))
                knob = '$KNOB_DOWN_%s$' % x
                self.trigger_action_list('%s = "drum set routing"/DEV(1.%s.1) P%s >%s ; MODIFY_DRUM %s'
                                         % (knob, chain, parameter, x, args))

            # Show how much the current drum has been transposed
            self.show_message('Bound to %s *** %s NOTES TRANSPOSED'
                              % (args, amount_transposed))

    def modify_drum(self, action_def, args):
        # Get the amount transposed for the current drum same as above
        amount_transposed = int(self.song().visible_tracks[self.drum_set_routing_index].devices[0].
                                chains[drum_dict[args][0] - 1].devices[0].parameters[drum_dict[args][1]].value) - 63
        # Trigger the note for the current drum to play so that I can hear it without hitting the actual drum
        self.trigger_action_list('MIDIA NOTE 2 %s 94' % (drum_dict[args][2] + amount_transposed))
        # Show how much the current drum has been transposed
        self.show_message('Bound to %s *** %s NOTES TRANSPOSED'
                          % (args, amount_transposed))

    # Record the drum set configuration as a snap, and save the name of the snap as the title of the MIDI clip
    def snap_drums(self, action_def, args):
        # Get a list of all scenes and find the current scene
        scene_list = list(self.song().scenes)
        scene_index = scene_list.index(self.song().view.selected_scene)
        for x in range(1, 9):
            # Check that the the track is set to record, the current group is the drum track, and and that
            # the track has a clip in it.
            if self.visible_tracks[self.track_index + 1 + x].arm is True and \
                    self.track_group == 'drum' and \
                    self.visible_tracks[self.track_index + 9 + x].clip_slots[scene_index].has_clip is True:
                # Rename the clip according to the scene and the track number in the group
                self.trigger_action_list('"drummidi %s"/CLIP(%s) NAME "drummidi %s - %s"'
                                         % (x, scene_index + 1, x, scene_index + 1))
                # Make the color of the clip yellow
                self.trigger_action_list('"drummidi %s"/CLIP(%s) COLOR 18' % (x, scene_index + 1))
                # Snap the configuration of the transpose devices on the drum set routing track with the
                # name of the clip as the name of the snap
                self.trigger_action_list('[drummidi %s - %s] "drum set routing"/SNAP DEV(1.ALL.1)'
                                         % (x, scene_index + 1))

    # Recall the snap configuration for the drums of the armed track
    def snap_drums_recall(self, action_def, args):
        # Get a list of all scenes and find the current scene
        scene_list = list(self.song().scenes)
        scene_index = scene_list.index(self.song().view.selected_scene)
        for x in range(1, 9):
            # Check that the track is armed and the current group is the drum group
            if self.visible_tracks[self.track_index + 1 + x].arm is True and \
                    self.track_group == 'drum':
                # Recall the drum configuration based on the title of the clip
                self.trigger_action_list('[drummidi %s - %s] RECALL' % (x, scene_index + 1))

    # Record a snap of the selected device in the current track
    def device_snap(self, action_def, args):
        # Get the name of the selected device
        device_name = self.song().view.selected_track.devices[0].view.selected_chain.devices[1].name
        # I assigned a designated parameter to be able to keep track of multiple snaps
        snap_number = int(self.song().view.selected_track.devices[0].view.selected_chain.devices[0]
                          .chains[0].devices[0].parameters[1].value)
        # Snap the device and name the snap after the name of the device and the current snap number plus 1
        self.trigger_action_list('[%s %s] SEL/SNAP DEV(1.SEL.2.1.1)' % (device_name, snap_number + 1))
        # Increase the snap number in the designated parameter by 1
        (self.song().view.selected_track.devices[0].view.selected_chain.devices[0]
         .chains[0].devices[0].parameters[1].value) = snap_number + 1

    # The next two methods are actions that modify what the knobs do, these will be replaced by
    # the control surface mapping functions described at the beginning, although I still use these fairly often
    # because some devices have built in banks of controls
    def bank_up(self, action_def, _):
        self.current_bank += 1
        self.trigger_action_list("$DEFAULT_BIND_USER_1_BANK_%s$" % self.current_bank)
        for x in range(1, 9):
            self.trigger_action_list('BIND ENC_DAW_0%s SEL/DEV(SEL) B%s P%s' % (x, self.current_bank, x))
        self.show_message("Bound to: Bank %s" % self.current_bank)

    def bank_down(self, action_def, _):
        self.current_bank -= 1
        self.trigger_action_list("$DEFAULT_BIND_USER_1_BANK_%s$" % self.current_bank)
        for x in range(1, 9):
            self.trigger_action_list('BIND ENC_DAW_0%s SEL/DEV(SEL) B%s P%s' % (x, self.current_bank, x))
        self.show_message("Bound to: Bank %s" % self.current_bank)

    # This action is used by pad_function below to assign pads to different parameters or actions as needed
    def bind_bank(self, action_def, args):
        self.current_bank = int(args)
        for x in range(1, 9):
            self.trigger_action_list('BIND ENC_DAW_0%s SEL/DEV(SEL) B%s P%s' % (x, args, x))
        self.show_message("Bound to: Bank %s" % args)

    # Cycle between the different modes in the maps dictionary, to add dynamic mapping for the pads on the controller
    def pad_function(self, action_def, args):
        maps = {1: ['Track Groups', 'SEL/TRACKGROUP'],
                2: ['Banks', 'BIND_BANK'],
                }
        num_of_maps = len(maps)

        # Handles the cycling of the different modes
        if args == '+':
            if self.current_pad_mapping < num_of_maps:
                self.current_pad_mapping += 1
            else:
                self.current_pad_mapping = 1
        elif args == '-':
            if self.current_pad_mapping == 1:
                self.current_pad_mapping = num_of_maps
            else:
                self.current_pad_mapping -= 1

        # Map the pads
        for x in range(1, 9):
            self.trigger_action_list('$PAD_DAW_0%s$ = %s %s' % (x, maps[self.current_pad_mapping][1], x))
        # Display a message on the screen telling me which mode I am in
        self.show_message("Pad Mapping: %s" % maps[self.current_pad_mapping][0])

    # Next two methods are for cycling between groups of tracks, and moving the control surface rings and
    # mapping for the faders accordingly
    def next_inst_track(self, action_def, args):
        # Get the list of visible tracks and save to the global variable to be used in other functions
        self.visible_tracks = list(self.song().visible_tracks)
        # Get the index for the current track
        self.track_index = self.visible_tracks.index(action_def['track'])
        # Get the length of all visible tracks
        self.tracklist_length = len(self.visible_tracks)

        # Check that the selected track is not the last track, and if it is, make the index -1 for the while loop
        if self.track_index == self.tracklist_length - 1:
            self.track_index = -1
        # Add one to the track index so that the while loop looks at the next track
        self.track_index += 1

        # Check the track to see if it's a group track one by one until the next group is found
        while str(self.visible_tracks[self.track_index].name) not in instrument_list:
            if self.track_index == self.tracklist_length - 1:
                self.track_index = -1
            self.track_index += 1


        else: # can't remember why I put an else here, but everything works, so I'll look at it later
              # TODO: test removing the else, I'm pretty sure it won't change anything

            # Store the index that was found for the next group
            self.track_group = str(self.visible_tracks[self.track_index].name)
            # Select the group track
            self.trigger_action_list('"%s"/SEL' % self.track_group)
            # Move the ring to the next group for both control surfaces being used
            ringlink = str(self.visible_tracks[self.track_index + 2].name)
            self.trigger_action_list('CS "KeyLabEssential" RING T"%s"' % ringlink)
            self.trigger_action_list('CS "Launchpad_X" RING T"%s"' % ringlink)
            # Bind all the faders to the correct mapping according to the current map mode
            for fader in menu_dict[1][1]['Faders']:
                self.trigger_action_list(('BIND %s %s' % (fader, menu_dict[1][1]['Faders'][fader])) % self.track_group)

    # Same as above, but going to the left
    def prev_inst_track(self, action_def, args):
        self.visible_tracks = list(self.song().visible_tracks)
        self.track_index = self.visible_tracks.index(action_def['track'])
        self.tracklist_length = len(self.visible_tracks)

        if self.track_index == 0:
            self.track_index = self.tracklist_length
        self.track_index -= 1

        while str(self.visible_tracks[self.track_index].name) not in instrument_list:
            if self.track_index == 0:
                self.track_index = self.tracklist_length
            self.track_index -= 1

        else:
            self.track_group = str(self.visible_tracks[self.track_index].name)
            self.trigger_action_list('"%s"/SEL' % self.track_group)

            ringlink = str(self.visible_tracks[self.track_index + 2].name)
            self.trigger_action_list('CS "KeyLabEssential" RING T"%s"' % ringlink)
            self.trigger_action_list('CS "Launchpad_X" RING T"%s"' % ringlink)
            for x in range(9):
                self.trigger_action_list('BIND ENC_1_1%s "%ssend %s"/VOL' % (x, self.track_group, x))
                self.trigger_action_list('BIND FADER_DAW_0%s "%ssend %s"/VOL' % (x, self.track_group, x))

    # Set tracks to mute according to the current track group selected
    def silence_multiple(self, action_def, args):
        self.trigger_action_list('"%ssend %s"/MUTE' % (self.track_group, args))

    # Immediately stop the track corresponding to the track group and the location of the button the
    # action is mapped to
    def stop_nq(self, action_def, args):
        self.trigger_action_list('"%ssend %s/STOP NQ' % (self.track_group, args))

    # Transpose the drum pads 16 down at a time
    def midi_transpose_16down(self, action_def, _):
        track_list_names = []
        x = 0

        # Get the location of the 'launchpad midi' track.
        # TODO: this is horribly inefficient, I need to recode this
        while len(self.visible_tracks) > x:
            track_list_names.append(str(self.visible_tracks[x].name))
            x += 1
        track_index = track_list_names.index('launchpad midi')

        # Get the current transposed amount
        current_midi_value = int(self.visible_tracks[track_index].devices[0].parameters[1].value)
        # Transpose the pads 16 notes down
        self.trigger_action_list('"launchpad midi"/DEV(1) P1 %s' % str(current_midi_value - 16))
        # Shoe a message with the current amount transposed
        self.show_message('MIDI Transpose: %s' % (next_midi_value - 64))

    # Same as above, but transposing up
    def midi_transpose_16up(self, action_def, _):
        track_list_names = []
        x = 0
        while len(self.visible_tracks) > x:
            track_list_names.append(str(self.visible_tracks[x].name))
            x += 1

        track_index = track_list_names.index('launchpad midi')

        current_midi_value = int(self.visible_tracks[track_index].devices[0].parameters[1].value)
        next_midi_value = current_midi_value + 16
        self.trigger_action_list('"launchpad midi"/DEV(1) P1 %s' % str(next_midi_value))

        self.show_message('MIDI Transpose: %s' % (next_midi_value - 64))

    # Stop everything and reset the location in the song to 0:00
    def stop_everything(self, action_def, _):  # TODO: Make play, stop, and rec buttons actually do what I want.
        # Stop everything immediately (non quantized)
        self.trigger_action_list('STOPALL NQ')
        # Reset the song to the beginning
        self.trigger_action_list('SETPLAY OFF')

        # Handles a bug where reseting doesn't work
        if str(self.song().get_current_beats_song_time()) == '001.01.01.001':
            pass
        else:
            self.trigger_action_list('RESTART')

        # Get current scene index
        scene_index = list(self.song().scenes).index(self.song().view.selected_scene) + 1
        # Track group type (MIDI or audio) changes the type of naming scheme to be used
        if self.track_group in midi_groups:
            group_type = 'midi'
        else:
            group_type = 'pass'

        # Mute all tracks in the secondary track group for midi/audio raw storage
        for x in xrange(1, 9):
            self.trigger_action_list('"%s%s %s"/CLIP(%s) MUTE ON' % (self.track_group, group_type, x, scene_index))

    # Stop recording depending on which tracks in the current track group are armed
    def contextual_stop_recording(self, action_def, _):
        # Get the location of the parameter in the drum group track where I stored the two modes
        # TODO: this is terrible, one of the early methods I made when I was new to programming. Incredibly
        # inefficient but it works. I need to update this so that this section can be just one line
        scene_list = list(self.song().scenes)
        scene_index = scene_list.index(self.song().view.selected_scene)
        drum_index = self.track_index

        while str(self.visible_tracks[drum_index].name) != 'drum':
            drum_index -= 1

        # First mode, when you click a button it stops at the next bar, and as well as stopping the associated
        # midi or audio track
        if int(self.visible_tracks[drum_index].devices[0].parameters[2].value) == 0:
            for x in range(1, 9):
                if self.visible_tracks[self.track_index + 1 + x].clip_slots[scene_index].is_recording is True:
                    self.trigger_action_list('"%ssend %s"/PLAY SEL' % (self.track_group, x))
                    if self.track_group in midi_groups:
                        self.trigger_action_list('"%smidi %s"/STOP' % (self.track_group, x))
                    elif self.track_group in audio_groups:
                        self.trigger_action_list('"%spass %s"/STOP' % (self.track_group, x))

        # I made this to get intros to work as clips and play the next clip down, but I could definitely
        # implement this better if I look at it again
        elif int(self.visible_tracks[drum_index].devices[0].parameters[2].value) == 127:
            for x in range(1, 9):
                if self.visible_tracks[self.track_index + 1 + x].clip_slots[scene_index].is_recording is True:
                    self.trigger_action_list('"%ssend %s"/PLAY EMPTY ; WAITS 1B ; SEL/RENAME_CLIP %s'
                                             % (self.track_group, x, x))
                    self.trigger_action_list('"%smidi %s"/PLAY SEL' % (self.track_group, x))

    # This mode for the pads makes each pad jump to the corresponding track group, saving the necessary
    # global variables in the process, and binding encoders and faders in the process as described in
    # next_inst_track
    # TODO: update code to implement the maps from the dictionary at the top, instead of just volume defaults
    def trackgroup(self, action_def, args):
        self.track_group = instrument_list[int(args) - 1]
        self.trigger_action_list('"%s"/SEL' % self.track_group)
        self.trigger_action_list('CS "KeyLabEssential" RING T"%s"' % (self.track_group + 'send 1'))
        self.trigger_action_list('CS "Launchpad_X" RING T"%s"' % (self.track_group + 'send 1'))
        for x in range(1, 9):
            self.trigger_action_list('BIND ENC_1_1%s "%ssend %s"/VOL' % (x, self.track_group, x))
            self.trigger_action_list('BIND FADER_DAW_0%s "%ssend %s"/VOL' % (x, self.track_group, x))
        self.visible_tracks = list(self.song().visible_tracks)
        self.track_index = self.visible_tracks.index(self.song().view.selected_track)

    # This action is used in the contextual_stop_recording function. It renames the clip as an action list,
    # and when played, it will play the length of the clip, and play the next clip a beat before the end, which
    # makes a seamless transition from the beginning of a recorded part, to the loop of the entire part. This
    # preserves reverb, and other effects which make some kind of loops jarring
    def rename_clip(self, action_def, args):
        scene_list = list(self.song().scenes)
        scene_index = scene_list.index(self.song().view.selected_scene)

        clip_length_in_beats = int(self.visible_tracks[self.track_index + 1
                                                       + int(args)].clip_slots[scene_index].clip.length)
        time_to_wait_stop = clip_length_in_beats - 4
        time_to_wait_renamed_clip = clip_length_in_beats - 1
        self.trigger_action_list('"%ssend %s"/CLIP(%s) NAMES "WAITS %s ; "%ssend %s"/PLAY >"'
                                 % (self.track_group, args, str(scene_index + 1), str(time_to_wait_renamed_clip),
                                    self.track_group, args))

        if time_to_wait_stop < 4:
            self.trigger_action_list('"%ssend %s"/PLAY %s' % (self.track_group, args, str(scene_index + 2)))
            self.trigger_action_list('"%smidi %s"/STOP' % (self.track_group, args))

        else:
            self.trigger_action_list('WAITS %s ; "%ssend %s"/PLAY %s'
                                     % (str(time_to_wait_stop), self.track_group, args, str(scene_index + 2)))
            self.trigger_action_list('WAITS %s ; "%smidi %s"/STOP'
                                     % (str(time_to_wait_stop), self.track_group, args))

    # Delete clips in the selected scene where the tracks are set to be armed
    def contextual_del_clip(self, action_def, _):
        for x in range(1, 9):
            if self.visible_tracks[self.track_index + 1 + x].arm is True:
                self.trigger_action_list('"%ssend %s"/CLIP DEL' % (self.track_group, x))
                if self.track_group in midi_groups:
                    self.trigger_action_list('"%smidi %s"/CLIP DEL' % (self.track_group, x))
                elif self.track_group in audio_groups:
                    self.trigger_action_list('"%spass %s"/CLIP DEL' % (self.track_group, x))

    # This is all a mess, and I can definitely improve the efficiency of the code, but it does work and is
    # incredibly helpful. I can record a midi or audio, preserve the original in a seperate clip on a
    # track in the subgroup, and record any effects so that I'm only playing audio files, which is magnitudes
    # less computer power than it takes to simulate effects for every part playing in the song.
    def contextual_rec_clip(self, action_def, _):
        scene_list = list(self.song().scenes)
        scene_index = scene_list.index(self.song().view.selected_scene)
        drum_index = self.track_index

        while str(self.visible_tracks[drum_index].name) != 'drum':
            drum_index -= 1

        for x in range(1, 9):
            if int(self.visible_tracks[drum_index].devices[0].parameters[3].value) == 127 and \
                    self.visible_tracks[self.track_index + 1 + x].clip_slots[scene_index].has_clip is False \
                    and self.visible_tracks[self.track_index + 1 + x].arm is True:
                # Play the clip for each track that is armed, as well as the corresponding track in the subgroup
                self.trigger_action_list('"%ssend %s"/PLAY SEL' % (self.track_group, x))
                midi_or_pass = ''
                # Handles different naming schemes and behaviors for audio and midi groups
                if self.track_group in midi_groups:
                    self.trigger_action_list('"%smidi %s"/PLAY SEL' % (self.track_group, x))
                    midi_or_pass = 'midi'
                elif self.track_group in audio_groups:
                    self.trigger_action_list('"%spass %s"/PLAY SEL' % (self.track_group, x))
                    midi_or_pass = 'pass'

                # All of this handles recording a predetermined number of bars, which is stored in
                # the self.recording_length_8count variable that is modified by the center knob mapping
                # method. A message is also shown on screen of the current predetermined length.
                self.trigger_action_list('WAITS %s ; "%ssend %s"/PLAY %s ; "%s%s %s"/STOP'
                                         % (int(self.recording_length_8count * 8 - 1), self.track_group, x,
                                            scene_index + 1, self.track_group, midi_or_pass, x))
                self.show_message('Recording Length: ------- %s Bars -------'
                                  % (int(self.recording_length_8count * 2)))

            # Default behavior is to just do the first part of the above 'if' code, and just play the
            # corresponding tracks that are armed
            elif self.visible_tracks[self.track_index + 1 + x].clip_slots[scene_index].has_clip is False \
                    and self.visible_tracks[self.track_index + 1 + x].arm is True:
                self.trigger_action_list('"%ssend %s"/PLAY SEL' % (self.track_group, x))
                if self.track_group in midi_groups:
                    self.trigger_action_list('"%smidi %s"/PLAY SEL' % (self.track_group, x))
                elif self.track_group in audio_groups:
                    self.trigger_action_list('"%spass %s"/PLAY SEL' % (self.track_group, x))

    # Simple action that allows scene movement, basically up and down in the session view
    def scene_move(self, action_def, args):
        args_list = args.split("-")
        scene_list = list(self.song().scenes)
        index = scene_index = int(scene_list.index(self.song().view.selected_scene))
        if args_list[0] == "down":
            index = scene_index + int(args_list[1]) + 1
        elif args_list[0] == "up":
            index = scene_index - int(args_list[1]) + 1
        self.trigger_action_list('SCENE SEL %s' % index)

    # Simple action that allows track movement, basically left and right in session view.
    def lr_move(self, action_def, args):
        args_list = args.split("-")
        scene_list = list(self.song().scenes)
        scene_index = int(scene_list.index(self.song().view.selected_scene)) + 1
        self.visible_tracks = list(self.song().visible_tracks)
        index = self.track_index = self.visible_tracks.index(self.song().view.selected_track)
        if args_list[0] == 'right':
            new_index = index + int(args_list[1]) + 1
            index = list(self.song().tracks).index(self.visible_tracks[new_index])
        elif args_list[0] == 'left':
            new_index = index - int(args_list[1]) + 1
            index = list(self.song().tracks).index(self.visible_tracks[new_index])
        self.trigger_action_list('%s/SEL %s' % (index, scene_index))
