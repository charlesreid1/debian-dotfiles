# This is the bash profile.
#
# This file sets PATH and bash options.
#
# to add your own non-committed machine-specific settings,
# use ~/.extra

# Must
EDITOR="vim"
GIT_EDITOR="vim"

# Better man pages
PAGER="most"

# Go stuff
GOROOT=$HOME/go
GOPATH=$HOME/go

# Set $PATH here
PATH="${HOME}/scripts:${PATH}"
PATH="/usr/local/bin:$PATH"
PATH="/usr/local/sbin:${PATH}" # homebrew admin tools
PATH="${PATH}:${GOROOT}/bin"
PATH="/usr/local/opt/coreutils/libexec/gnubin:${PATH}"
PATH="${HOME}/bin:${PATH}"
if [[ ("$HOSTNAME" == "seawater") || ("$HOSTNAME" == "bascom") ]]; then
    PATH="${HOME}/bin/elasticsearch-5.4.2/bin:${PATH}"

    # assume-role cli util:
    # Add homebrew-installed ruby to path:
    # (WARNING: THIS CAN CAUSE PROBLEMS!)
    export PATH="/usr/local/opt/ruby/bin:$PATH"

    # Add homebrew-ruby-gem-installed packages to path:
    export PATH="/usr/local/lib/ruby/gems/2.6.0/bin:$PATH"

    # aws - load config file when using assume-role
    export AWS_SDK_LOAD_CONFIG="1"
fi

# Tell git not to look for getext.sh
# since pyenv has trouble with that
export GIT_INTERNAL_GETTEXT_TEST_FALLBACKS=1

if [[ "$HOSTNAME" == "bascom" ]]; then
    # git tab completion
    source ${HOME}/.git-completion.bash
fi

# goenv installer
export GOENV_ROOT="$HOME/.goenv"
export PATH="$GOENV_ROOT/bin:$PATH"

# Only enable this if you are using go.
# This will add half a second every time you
# open a new shell.
#eval "$(goenv init -)"

# pyenv installer
# https://github.com/pyenv/pyenv-installer
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

export PATH

# Just let homebrew take care of PYTHONPATH, yeah?
# But if you really needed to, you could set it here.


# Bash history

HISTFILE="$HOME/.bash_history"
HISTFILESIZE=1000000000
HISTIGNORE="ls:cls:clc:clear:pwd:l:ll:[ ]*"
HISTSIZE=1000000
HISTTIMEFORMAT=': %Y-%m-%d_%H:%M:%S; '

# Save Bash history
shopt -s cmdhist;
# Append to the Bash history file, rather than overwriting it
shopt -s histappend;
# Write history to .bash_history immediately.
# -a writes current/new lines to history file
# -n reloads only new commands
# https://askubuntu.com/a/673283
PROMPT_COMMAND='history -a;history -n'

# don't try to autocomplete commands when tab is pressed and line is empty
shopt -s no_empty_cmd_completion

if [[ "$HOSTNAME" == "bascom" ]]; then
    # aws cli tab-completion
    # https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-completion.html
    complete -C "$(pyenv which aws_completer)" aws
fi


#############################
# modified mathias

# Load the shell dotfiles, and then some:
# * ~/.path can be used to extend `$PATH`.
# * ~/.extra can be used for other settings you don’t want to commit.
for file in ~/.{path,bash_prompt,exports,aliases,functions,extra}; do
	[ -r "$file" ] && [ -f "$file" ] && source "$file";
done;
unset file;

# Case-insensitive globbing (used in pathname expansion)
shopt -s nocaseglob;

# Autocorrect typos in path names when using `cd`
shopt -s cdspell;

if [ -f /etc/bash_completion ]; then
	source /etc/bash_completion;
fi;

if [[ "$HOSTNAME" == "bascom" ]]; then
    # Enable tab completion for `g` by marking it as an alias for `git`
    if type _git &> /dev/null && [ -f /usr/local/etc/bash_completion.d/git-completion.bash ]; then
    	complete -o default -o nospace -F _git g;
    fi;
fi
