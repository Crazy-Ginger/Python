#!/usr/bin/env python3
from colored import fg, attr

logo =  '''
{0}               +
{1}               #
{2}              ###
{3}             #####
{4}             ######
{5}            ; #####;
{6}           +##.#####
{7}          +##########
{8}         ######{18}#####{8}##;
{9}        ###{19}############{9}+
{10}       #{20}######   #######
{11}     .######;     ;###;`\".
{12}    .#######;     ;#####.
{13}    #########.   .########`
{14}   ######'           '######
{15}  ;####                 ####;
{16}  ##'                     '##
{17} #'                         `#
'''


colours = []
for i in range(21):
    colours.append((fg(i)))
print (colours)
print (logo.format(*colours))
# print ("{0}These are words, hopefully in another colour".format((fg(1))))

