Title: Getting Started with Particle Electron
Date: 2018-05-07 20:00
Category: openCV
Status: published

Currently watching: Cavs vs Raptors Game 4, 2018 NBA Playoffs

### Getting Started with Particle Electron

IoT – The internet of things always seems like a hot topic. You wanted to get 
involved so you went to the [Particle Store](https://store.particle.io/) and 
bought an Electron to get started.

We will walk through the process of quickly setting up a **Particle Electron** and
loading your first IoT application.

*Note: Nearly all the information in this guide is available at 
[www.docs.particle.io](https://docs.particle.io/guide/getting-started/intro/electron/)
Go there for more detail in most any Particle related topic.*

#### What you need

- [Particle.io Account](https://login.particle.io/login)
- Particle Electron
- USB Cable
- Computer (This guide uses macOS)

#### Setting up

##### 1. [Activate your Particle Electron.](https://setup.particle.io/)  


The next few steps assume some knowledge of the command line.  If you have never 
used command line before check out [this guide](https://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything)
so that it becomes less intimidating.

##### 2. [Install Particle Command Line Interface Tool (CLI)](https://docs.particle.io/guide/getting-started/connect/electron/)

Copy and paste the following command into your terminal.

    bash <( curl -sL https://particle.io/install-cli )
    
If that doesn't work, you will probably have to install [Homebrew](https://brew.sh/)
and redo the above command.

If you are unable to install the CLI tool, go to [This page](https://docs.particle.io/guide/tools-and-features/cli/electron/)
for extra detail on CLI installation.

##### 3. Particle CLI

try typing the following command into your bash terminal:

    $ particle
    
This will give a list of available commands within Particle CLI.  A typical
command might follow the following format.

    $ particle [subcommand] [sub-subcommand] -option
    
For example, in order to repair an Electron with crashed firmware I would use
the command:

    $ particle device doctor
    

##### 4. Uploading code to the Particle Electron

There are a couple ways to upload code to the Electron.  We will focus on the method
I most often use because it seems to be the most reliable.

###### Editing and uploading code:

You can edit code using your text editor of choice, or use the [Particle Web Editor](https://build.particle.io/)
After creating your application click on the *Compile and download firmware binary*
button.  

Navigate your bash terminal to the same directory as the binary file you just downloaded.

Place your device into [DFU Mode](https://docs.particle.io/guide/getting-started/modes/electron/#dfu-mode-device-firmware-upgrade-) 
– Press both **MODE** and **RESET** buttons at the same time, then release **ONLY**
 the **RESET** button.
 
To upload the binary file use the following command:

    $ particle flash --usb [name_of_file].bin
    
The firmware is now on your Electron.  Congrats!

##### Useful Links

- [Particle Docs](https://docs.particle.io/guide/getting-started/intro/electron/)
- [Electron Firmware Reference](https://docs.particle.io/reference/firmware/electron/)
- [Particle Console](https://console.particle.io/)
- [Particle Build](https://build.particle.io/)



