# Manim Interactive

> **Version:** v1.0.0  
> **Supported Platform:** macOS (currently)

Manim Interactive is an enhanced interactive development environment built on top of [Manim](https://github.com/3b1b/manim). It provides a streamlined workflow for creating mathematical animations using an interactive window, a convenient Makefile, and integrated support for Sublime Text Editor.

---

## Table of Contents
- [Overview](#overview)
- [Why Manim](#why-manim)
- [Pre-Requisites](#pre-requisites)
- [Installation](#installation)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
    - [Step 3: Verify Installation](#step-3-verify-installation)
- [Using the Makefile](#using-the-makefile)
- [Running Animations](#running-animations)
- [Interactive Animations with Sublime Text Editor](#interactive-animations-with-sublime-text-editor)
- [Exporting Animations](#exporting-animations)
- [Resolution Shortcuts](#resolution-shortcuts)
- [Upgrading Manim](#upgrading-manim)
- [Hacking the Manim Library](#hacking-the-manim-library)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Manim Interactive is designed to make it easier to create animations using Manim. With an interactive setup, a simple Makefile, and integration with Sublime Text, you can rapidly prototype and render mathematical animations in high quality.

By the end of this guide, you’ll know how to:
- Create and run animations interactively.
- Configure and export high-resolution videos.
- Customize your workflow using keyboard shortcuts and Sublime Text integrations.

This is also the project I use to create videos for my YouTube channel, [Pixel Projects](https://www.youtube.com/channel/UC5OToaksgWe-pjkgqPkUZkw?sub_confirmation=1). To see the animations in action, check out the channel and the 
corresponding code in this repository, under `projects/2025/`.

---

## Why Manim
Manim is a powerful Python library originally designed for mathematical animations. It offers:
- **Ease of Use:** Lower learning curve compared to commercial tools.
- **Flexibility:** Full control over animation elements with Python.
- **Open-Source Freedom:** Modify and extend the code to fit your needs.

> **Note:** This project currently supports macOS only.

---

## Pre-Requisites
Before proceeding, ensure you have:
1. [Sublime Text Editor](https://www.sublimetext.com/)
2. [Homebrew](https://brew.sh/)
3. A [GitHub account](https://github.com/)
4. [Rectangle](#) (optional, for window management)
5. A [MacBook](#) (required for macOS support)


## Step 1

### Step 1: Clone the Repository

```bash
git clone https://github.com/pprunty/manim-interactive.git
```

### Step 2: Install Dependencies

The repository includes a `Makefile` that automates setup. Run:

```bash
make install
```

This command will:

1. Install `ffmpeg` and `mactex` using Homebrew.
2. Set up Manim in editable mode using Python's `pip`.
3. Install `setuptools` (required for manimgl).
4. Update the `custom_config.yml` with your local paths.

## Step 3: Verify Installation

Confirm the `manimgl` command is available:

```bash
manimgl --help
```

# Using the Makefile

The Makefile provides shortcuts for common tasks. To see available commands, run:

```bash
make --help
```

Output:

```txt
Usage: make [target]

Targets:
  help            Display this help message
  install         Install dependencies and set up Manim in editable mode
  config          Configure custom settings for Manim
  upgrade         Upgrade the Manim library to the latest version
  interactive     Run an interactive animation
  run             Run an animation (make run f=<file> [s=<scene>])
  export          Export an animation as a video (make export f=<file> s=<scene>)
  sublime         Configure Sublime Text with custom Manim commands
  short           Update resolution for short-form videos (2160x3840)
  video           Update resolution for standard videos (3840x2160)

Interactive Target Usage:
  make interactive f=<file> [s=<scene>]
    f=<file>      Path to the Python file containing the animation
    s=<scene>     Name of the scene to render
```

Common targets include:

* `install` – Set up dependencies.
* `run` – Run an animation.
* `interactive` – Launch an interactive animation session.
* `export` – Export an animation to a video file.

# Running Animations

Manim uses a `custom_config.yml` file for configuration. The project structure includes:

```
.
├── Makefile
├── custom_config.yml       # Default Manim configuration
├── manim_imports_ext.py
├── media
│   ├── images              # Image assets
│   └── vectors             # SVG references
├── projects
│   ├── 2025                # New animation projects
│   └── guides              # Guide animations
│       ├── 3d.py
│       ├── README.md
│       ├── custom_config.yml
│       ├── equation.py
│       ├── graph.py
│       ├── grouping.py
│       ├── image.py
│       └── text.py
├── stage_scenes.py
├── sublime_custom_commands # For Sublime Text configuration
└── videos                  # Exported videos
```

To run an animation:

```bash
make run f=projects/guides/text.py s=TextScene
```

This will open an interactive window with the example animation.

The animations provided in `projects/guides/*.py`.
Listed:

* `projects/guides/text.py`
* `projects/guides/image.py`
* `projects/guides/equation.py`
* `projects/guides/graph.py`
* `projects/guides/grouping.py`
* `projects/guides/3d.py`

Showcase isolated animations that can be used and referenced when creating complex
animations later.

For example, to run animations from `image.py`:

```bash
make run f=projects/guide/image.py s=MovingImageScene
```

## Keyboard Controls:

Once the animation is open in a window, you can use the following keyboard controls 
to interact with the animation:

* Scroll: Move the view vertically.
* Hold z and scroll: Zoom in/out.
* Hold d and move: Adjust the 3D perspective.
* Press r: Reset scroll position.
* Press ⌘ + q: Quit the window.

# Running Interactive Animations with Sublime Text Editor

Sublime Text Editor is used to create keyboard shortcuts that interact with Manim's animation
scenes.

To configure Sublime Text:

1. Open the project in Sublime Text.
2. Install the Terminus package:
* Press `cmd + shift + p`, select “Install Package”, and search for “Terminus.”
4. Set up key bindings: Open Preferences: Terminus Key Bindings and paste:
```json
[
    {
        "keys": ["super+1"],
        "command": "terminus_open",
        "args": {
            "cmd": ["bash", "-i", "-l"],
            "cwd": "${file_path:${folder}}",
            "panel_name": "Terminus"
        }
    },
    { "keys": ["shift+super+r"], "command": "manim_run_scene" },
    { "keys": ["super+r"], "command": "manim_checkpoint_paste" },
    { "keys": ["super+alt+r"], "command": "manim_recorded_checkpoint_paste" },
    { "keys": ["super+ctrl+r"], "command": "manim_skipped_checkpoint_paste" },
    { "keys": ["super+e"], "command": "manim_exit" },
    { "keys": ["super+option+/"], "command": "comment_fold" }
]
```
5. Copy the contents of the `sublime_custom_commands/*` folder into Sublime Text by running:
```bash
make sublime
```
6. Restart Sublime Text to finalize the setup.

Now, when you open Sublime Text Editor, you can open a terminal using `cmd + 1`.

Additionally, you can use the following Manim key bindings:

* `cmd+shift+r` – Run the current scene by highlighting `def construct(self):` in that scene. This will run the scene interactively in an animation window.
* `cmd+r` – Run a block of code by highlighting the full block you wish to animate (including consistent indentation) and pressing these keys together. Ensure the block is part of the scene you are working on and that 
it includes consistent indentation. The constructor block should not be included.
* `cmd+e` – Exit the interactive animation.

# Exporting Animations

To export an animation in high 4K resolution:

```bash
make export f=projects/guide/text.py s=TextScene
```

By default, the mp4 file will be saved at:

```text
videos/projects/guide/text/TextScene.mp4
```

> **Note:** This project currently supports macOS only.
Exports default to 4K. To change resolution, modify the --uhd flag in the Makefile and update custom_config.yml accordingly.
---

# Resolution Shortcuts

Nowadays, videos are made in vertical and horizontal resolution for long-form 4K (3840,2160) and short-form (2160, 3840) content. If you
want to make a short video, start by running:

Switch between video resolutions using:

* Short Video (Vertical short-form 4K (2160,3840))
```bash
make short
```
* Standard Video (Horizontal long-form 4K (3840,2160))
```bash
make video
```

> **Warning:** Running these commands also copies the `custom_config.yml` from `projects/guides` to the project root. This file is used by Manim key bindings in Sublime Text Editor for interactive workflows.
---

# Upgrading Manim

Manim Interactive uses a static version of the `3b1b/manim` repository, namely (#). Upgrading may affect existing projects. To upgrade:

```bash
make upgrade
```

This command:

1. Clone the latest `3b1b/manim` repository.
2. Replace the current library, at `_manimlib`.
3. Re-installs the upgraded library.

# Hacking the Manim Library

For advanced users:

* Refer to additional documentation on modifying Manim’s internals.
* Be cautious—changes here may break your animations.

# Troubleshooting

If you encounter issues:

* Verify that all installation steps completed successfully.
* Ensure that Homebrew and pip installations worked as expected.
* Consult the FAQ or search online for common issues.
* Check the project’s GitHub issues page for similar problems.

# Contributing

Contributions are welcome! Please contact me directly for guidelines on reporting bugs, submitting pull requests, and adhering to our code style.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.