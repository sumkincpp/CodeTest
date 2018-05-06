function title {
    echo -ne "\033]0;"$*"\007"
}

# Setting title
title $(hostname)
