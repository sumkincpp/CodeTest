uint32_t netmask_bits(uint32_t address)
{
  uint32_t zero_bits = 0;

  while((address & 1) == 0) {
    address >>= 1;
    zero_bits++;
  }

  return 32 - zero_bits;
}
