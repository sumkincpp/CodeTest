#
# https://stackoverflow.com/questions/9546324/adding-directory-to-path-environment-variable-in-windows
#
$PATH = [Environment]::GetEnvironmentVariable("PATH")
$xampp_path = "C:\xampp\php"
# To set the variable for all users, machine-wide, the last line should be like:
if( $PATH -notlike "*"+$xampp_path+"*" ){
    [Environment]::SetEnvironmentVariable("PATH", "$PATH;$xampp_path", "Machine")
}
