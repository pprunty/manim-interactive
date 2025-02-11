# Makefile for managing Manim setup and usage

.PHONY: help install config upgrade interactive run export sublime short video

# Variables
MANIM_DIR         = _manimlib
PROJECTS_DIR      = projects
CURRENT_YEAR      = $(shell date +%Y)
CUSTOM_CONFIG     = custom_config.yml
MANIM_REPO        = https://github.com/3b1b/manim.git
OUTPUT_DIR        = exports
SUBLIME_USER_DIR  = $(shell find ~/Library/Application\ Support/Sublime\ Text*/Packages/User -type d 2>/dev/null | head -n 1)
SUBLIME_CUSTOM_DIR= sublime_custom_commands
SUBLIME_DOWNLOAD_URL=https://www.sublimetext.com/download
INTERACTIVE_CONFIG= custom_config.yml

# Old base path stored as an environment variable:
MANIM_OLD_BASE    = /Users/pprunty/GitHub/manim

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help            Display this help message"
	@echo "  install         Install dependencies and set up Manim in editable mode"
	@echo "  config          Configure custom settings for Manim"
	@echo "  upgrade         Upgrade the Manim library to the latest version"
	@echo "  interactive     Run an interactive animation"
	@echo "  run             Run an animation (make run f=<file> [s=<scene>])"
	@echo "  export          Export an animation as a video (make export f=<file> s=<scene>)"
	@echo "  sublime         Configure Sublime Text with custom Manim commands"
	@echo "  short           Update resolution for short-form videos (2160x3840)"
	@echo "  video           Update resolution for standard videos (3840x2160)"
	@echo ""
	@echo "Interactive Target Usage:"
	@echo "  make interactive f=<file> [s=<scene>]"
	@echo "    f=<file>      Path to the Python file containing the animation"
	@echo "    s=<scene>     Name of the scene to render"
	@echo ""

install:
	@echo "Installing dependencies..."
	brew install ffmpeg mactex
	@echo "Installing Manim library in editable mode..."
	pip install -e $(MANIM_DIR)
	pip install setuptools
	@echo "Installation complete. The 'manimgl' command should now be available on your system."
	manimgl --help

	@echo "Configuring custom_config.yml dynamically..."
	CURRENT_DIR=$(shell pwd)
	PARENT_DIR=$(shell dirname $(CURRENT_DIR))
	@sed -i.bak \
	    -e "s|$(MANIM_OLD_BASE)|$(CURRENT_DIR)|g" \
	    -e "s|/Users/pprunty/GitHub|$(PARENT_DIR)|g" \
	    $(CUSTOM_CONFIG)
	@echo "custom_config.yml updated with current paths:"
	@echo "  Base Directory: $(CURRENT_DIR)"
	@echo "  Parent Directory: $(PARENT_DIR)"
	@cp custom_config.yml ~/custom_config.yml			
	@cat $(CUSTOM_CONFIG)

config:
	@echo "Configuring custom settings..."
	@if [ -f "$(CUSTOM_CONFIG)" ]; then \
		echo "Found existing configuration: $(CUSTOM_CONFIG)"; \
	else \
		echo "Creating a new custom configuration file..."; \
		echo "directories.base: $(PROJECTS_DIR)/output" > $(CUSTOM_CONFIG); \
	fi
	@echo "Opening configuration file for edits..."
	vim $(CUSTOM_CONFIG)
	@echo "Configuration complete."

upgrade:
	@echo "Upgrading to the latest version of Manim..."
	@read -p "Are you sure you want to proceed? (yes/no): " confirm && [ $$confirm = "yes" ] || exit 1;
	@echo "Cloning the latest version of Manim..."
	git clone $(MANIM_REPO) $(MANIM_DIR)/latest_manim
	@echo "Replacing the current Manim library with the latest version..."
	rm -rf $(MANIM_DIR)/manimlib
	mv $(MANIM_DIR)/latest_manim/manimlib $(MANIM_DIR)/manimlib
	rm -rf $(MANIM_DIR)/latest_manim
	@echo "Reinstalling the upgraded Manim library..."
	pip install -e $(MANIM_DIR)
	pip install setuptools
	@echo "Upgrading complete and Manim reinstalled."

run:
	@echo "Running animation..."
	@if [ -z "$(f)" ]; then \
		f="$(PROJECTS_DIR)/examples/guide.py"; \
	fi; \
	if [ -z "$(s)" ]; then \
		echo "Command: manimgl $$f"; \
		manimgl $$f -f; \
	else \
		echo "Command: manimgl $$f $$s -f"; \
		manimgl $$f $$s -f; \
	fi
	@echo "Animation executed. Press the space bar or right arrow key to play animation."

interactive:
	@echo "Running interactive animation..."
	@if [ -z "$(f)" ]; then \
		echo "Error: The 'f' (file) argument is required. Usage: make interactive f=<file> s=<scene>"; \
		exit 1; \
	fi; \
	if [ -z "$(s)" ]; then \
		echo "Error: The 's' (scene) argument is required. Usage: make interactive f=<file> s=<scene>"; \
		exit 1; \
	fi; \
	# Extract the line number of the construct function for the specified scene
	line_number=$$(awk '/class $(s)/{flag=1} /def construct/{if(flag) {print NR; exit}}' $$f); \
	if [ -z "$$line_number" ]; then \
		echo "Error: 'construct' method not found in the specified scene $(s)"; \
		exit 1; \
	fi; \
	line_number=$$((line_number + 1)); \
	echo "Line number for 'construct': $$line_number"; \
	echo "Command: manimgl $$f $$s -f -p -se $$line_number"; \
	manimgl $$f $$s -f -p -se $$line_number;
	@echo "Interactive animation executed. Press the space bar or right arrow key to play animation."

export:
	@echo "Exporting animation..."
	@if [ -z "$(f)" ] || [ -z "$(s)" ]; then \
		echo "Error: You must specify both the file (f=<file>) and the scene (s=<scene>)."; \
		exit 1; \
	fi; \
	if [ -z "$(o)" ]; then \
		o="$(OUTPUT_DIR)"; \
	fi; \
	mkdir -p $$o; \
	echo "Command: manimgl $$f $$s --uhd --fps 60 -w"; \
	manimgl $$f $$s -w;
	@echo "Export completed to $$o."

sublime:
	@echo "Checking if Sublime Text is installed..."
	@if [ -z "$(SUBLIME_USER_DIR)" ]; then \
		echo "Sublime Text is not installed."; \
		echo "Download it here: $(SUBLIME_DOWNLOAD_URL)"; \
		exit 1; \
	fi
	@cp custom_config.yml ~/custom_config.yml
	@echo "Sublime Text is installed. Sublime User directory: $(SUBLIME_USER_DIR)"
	@echo "Copying custom commands to Sublime User directory..."
	@cp -R $(SUBLIME_CUSTOM_DIR)/* "$(SUBLIME_USER_DIR)/"
	@echo "Custom commands copied."
#	@echo "Adding keybindings for Manim custom commands..."
#	@if [ ! -f "$(SUBLIME_USER_DIR)/Default (OSX).sublime-keymap" ]; then \
#		echo "Creating new keybindings file..."; \
#		touch "$(SUBLIME_USER_DIR)/Default (OSX).sublime-keymap"; \
#	fi
#	@cat >> "$(SUBLIME_USER_DIR)/Default (OSX).sublime-keymap" <<- 'EOL'
#	[
#	    { "keys": ["shift+super+r"], "command": "manim_run_scene" },
#	    { "keys": ["super+r"], "command": "manim_checkpoint_paste" },
#	    { "keys": ["super+alt+r"], "command": "manim_recorded_checkpoint_paste" },
#	    { "keys": ["super+ctrl+r"], "command": "manim_skipped_checkpoint_paste" },
#	    { "keys": ["super+e"], "command": "manim_exit" },
#	    { "keys": ["super+option+/"], "command": "comment_fold"}
#	]
#	EOL
#	@echo "Keybindings added. Restart Sublime Text to apply the changes."

short:
	@echo "Updating resolution for short-form videos (2160x3840)..."
	@if [ -f "$(INTERACTIVE_CONFIG)" ]; then \
		sed -i.bak "s/resolution: (.*)/resolution: (2160, 3840)/" $(INTERACTIVE_CONFIG); \
		echo "Resolution updated to 2160x3840 in $(INTERACTIVE_CONFIG)."; \
	else \
		echo "Error: Configuration file $(INTERACTIVE_CONFIG) not found."; \
		exit 1; \
	fi
	@cp $(INTERACTIVE_CONFIG) ~/custom_config.yml
	@echo "Copied updated configuration to ~/custom_config.yml"

video:
	@echo "Updating resolution for standard videos (3840x2160)..."
	@if [ -f "$(INTERACTIVE_CONFIG)" ]; then \
		sed -i.bak "s/resolution: (.*)/resolution: (3840, 2160)/" $(INTERACTIVE_CONFIG); \
		echo "Resolution updated to 3840x2160 in $(INTERACTIVE_CONFIG)."; \
	else \
		echo "Error: Configuration file $(INTERACTIVE_CONFIG) not found."; \
		exit 1; \
	fi
	@cp $(INTERACTIVE_CONFIG) ~/custom_config.yml
	@echo "Copied updated configuration to ~/custom_config.yml"
