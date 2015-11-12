// https://stackoverflow.com/questions/14543443/in-c-how-do-you-redirect-stdin-stdout-stderr-to-files-when-making-an-execvp-or
// In child process -- >
else if (pid == 0)
{
    dup2(fileno(someopenfile), STDIN_FILENO);
    dup2(fileno(someotherfile), STDOUT_FILENO);
    dup2(fileno(somethirdopenfile), STDERR_FILENO);
    fclose(someopenfile);
    fclose(someotheropenfile);
    fclose(somethirdopenfile);
    execvp(args[0], args);
    // handle error ...
}
