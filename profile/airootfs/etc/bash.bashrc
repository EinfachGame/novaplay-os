#
# /etc/bash.bashrc – NovaPlay OS
#
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ $DISPLAY ]] && shopt -s checkwinsize

# Neon-Eingabezeile: [benutzer@pc ordner] ❯
PS1='\[\e[1;35m\]\u\[\e[0;36m\]@\h \[\e[1;37m\]\W \[\e[1;35m\]❯\[\e[0m\] '

case ${TERM} in
  Eterm*|alacritty*|aterm*|foot*|gnome*|konsole*|kterm*|putty*|rxvt*|tmux*|xterm*)
    PROMPT_COMMAND+=('printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"')
    ;;
  screen*)
    PROMPT_COMMAND+=('printf "\033_%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"')
    ;;
esac

if [[ -r /usr/share/bash-completion/bash_completion ]]; then
  . /usr/share/bash-completion/bash_completion
fi

# NovaPlay-Logo mit Systeminfos (nur im grafischen Terminal)
if [[ -n $DISPLAY || -n $WAYLAND_DISPLAY ]] && command -v fastfetch >/dev/null; then
  fastfetch
fi
