// https://stackoverflow.com/questions/13464364/ip-address-overlapping-in-range-of-cidr
bool cidr_overlap(uint32_t ip1, int n1,
                  uint32_t ip2, int n2)
{
    return (ip1 <= (ip2 | ((1ul << (32-n2))-1)))
        || (ip2 <= (ip1 | ((1ul << (32-n1))-1)));
}
