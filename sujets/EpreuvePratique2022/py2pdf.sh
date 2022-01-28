TERM=xterm-256color vim '+hardcopy >out.ps' +q $1
ps2pdf out.ps $1.pdf
rm out.ps
