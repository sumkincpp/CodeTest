# Group folloowing
John|Life
John|Temp
John|Admin
Peter|Life
Peter|Admin
Matt|Life
Matt|Admin
Matt|Temp
# To
John|Life,Temp,Admin
Peter|Life,Admin
Matt|Life,Admin,Temp
# ---->
$ awk -F '|' '
$1==x{
    printf ",%s", $2
    next
}
{
    x=$1
    printf "\n%s|%s", $1, $2
}
END {
    printf "\n"
}' input.txt

