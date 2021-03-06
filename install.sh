#!/bin/bash

function brew_check {
	if [ -f "/usr/local/bin/brew" ]; then
		echo "It looks like you have brew installed, so we're going to install dependencies";
		echo "Updating brew (this may take a while)";
		install_deps;
	else
		echo "[!] It doesn't look like you have brew installed. You're going to want to do this so that dependecies can be installed.";
		echo "Or, if you'd like, we can install it now? (y/n): "
		read input;
		if [ "$input" = "y" ]; then
			ruby -e "\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)";
			echo "Now that brew is installed, we'll install our dependencies";
			install_deps
		else 
			echo "Okay, exiting..."
			exit;
		fi
	fi
}

function install_deps {
	brew update; brew install mp4box ffmpeg;
}

arg=("$@");
if [ "${arg[0]}" = "--without-brew-check" ]; then
	echo "Not going to check for brew";
else
	brew_check;
fi

if [ -f "/usr/bin/metamaker" ]; then
	echo "[!] /usr/bin/metamaker aready exists, overwrite it? (y/n): ";
	read input;
	if [ "$input" = "y" ]; then
		echo "Overwriting metamaker...";
		sudo cp metamaker.py /usr/bin/metamaker;
		echo "[+] metamaker.py copied to /usr/bin as metamaker";
	else
		echo "Okay, exiting...";
		exit;
	fi
fi

echo " Install imdbpy using pip (ignore warnings if imdbpy is already installed";
pip install imdbpy;

echo " Copying metamaker.py to /usr/bin as metamaker";
sudo cp metamaker.py /usr/bin/metamaker;
echo " [+] metamaker.py copied to /usr/bin as metamaker";

echo " If you're reading this, then everything should be installed. Congrats! 🎉 🎉 ";
exit;


