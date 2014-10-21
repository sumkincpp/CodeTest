 /* 
 * Copyright (c) 1982, 1986, 1988, 1990, 1993, 1994
 *     The Regents of the University of California.  All rights reserved.
 *
 * Redistribution and use in source and binary form, with or without
 * modifications, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *      This product includes software developed by the University of 
 *      California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ''AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

 unsigned short cksum(struct ip *ip, int len){
   long sum = 0;  /* assume 32 bit long, 16 bit short */

   while(len > 1){
     sum += *((unsigned short*) ip)++;
     if(sum & 0x80000000)   /* if high order bit set, fold */
       sum = (sum & 0xFFFF) + (sum >> 16);
     len -= 2;
   }

   if(len)       /* take care of left over byte */
     sum += (unsigned short) *(unsigned char *)ip;
  
   while(sum>>16)
     sum = (sum & 0xFFFF) + (sum >> 16);

   return ~sum;
 }

 /* taken from TCP/IP Illustrated Vol. 2(1995) by Gary R. Wright and W. Richard
    Stevens. Page 236 */
