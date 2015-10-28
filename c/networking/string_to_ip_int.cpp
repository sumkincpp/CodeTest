uint32_t convert_ip(const std::string ip)
{
    int a, b, c, d;

    if (sscanf(ip.c_str(), "%d.%d.%d.%d", &a, &b, &c, &d) != 4)
        return 0;

    return (a << 24) | (b << 16) | (c << 8) | d;
}
