sub _filetype {
    my $self = shift;
    my $file = shift;

    return unless defined $file;

    return SYMLINK  if (-l $file);      # Symlink

    return FILE     if (-f _);          # Plain file

    return DIR      if (-d _);          # Directory

    return FIFO     if (-p _);          # Named pipe

    return SOCKET   if (-S _);          # Socket

    return BLOCKDEV if (-b _);          # Block special

    return CHARDEV  if (-c _);          # Character special

    ### shouldn't happen, this is when making archives, not reading ###
    return LONGLINK if ( $file eq LONGLINK_NAME );

    return UNKNOWN;                         # Something else (like what?)

}
