# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import *

suits = [" of Clubs", "of Diamonds", "of Hearts", "of Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "Kings"]
def print_board(s):
    s_count = 1
    for stack in s:
        print("Stack "+ str(s_count)+ ":")
        for card in stack:
            #print(card)
            print(values[card[1]-1],suits[card[0]])
        print("\n")
        s_count +=1
    
def getStacks(pid):
    PROCESS_ID = pid # From TaskManager 
    address_list = [0x01008B04,0x01008B58,0x01008BAC,0x01008C00,0x01008C54,0x01008CA8,0x01008CFC,0x01008D50]
    
    PROCESS_HEADER_ADDR = 0x01008B04 # From SysInternals VMMap utility
    
    # read from addresses
    STRLEN = 24
    
    PROCESS_VM_READ = 0x0010
    
    k32 = WinDLL('kernel32')
    k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
    k32.OpenProcess.restype = HANDLE
    k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
    k32.ReadProcessMemory.restype = BOOL
    
    process = k32.OpenProcess(PROCESS_VM_READ, 0, PROCESS_ID)
    
    stacks_strings = []
                
    for j in range(8):
        current_stack = []
        if (j < 4):
            STRLEN = 28
        else:
            STRLEN = 24
        
        PROCESS_HEADER_ADDR = address_list[j]
        
        buf = create_string_buffer(STRLEN)
        s = c_size_t()
        if k32.ReadProcessMemory(process, PROCESS_HEADER_ADDR, buf, STRLEN, byref(s)):
            print("Stack " + str(j+1) + " Retrieved!")
        else:
            print("fail")
    
        #print()
        str_buf = (str(buf.raw)[2:])[:-1]
        #print(str_buf)
        list_buf = (str_buf.split("\\x00\\x00\\x00"))
        #print(list_buf)
    
        for i in list_buf:
            if(i!=''):
                print("Next:", i)
                if(i=="\\t"):
                    current_stack.append("09")
                elif(i=="\\r"):
                    current_stack.append("0D")
                elif(i=="\\n"):
                    current_stack.append("0A")
                elif(i[:4]=="\\x00"):
                    current_stack.append("00")
                    if(i[:6]=="\\x00\\x"):
                        current_stack.append(i[6:])
                    elif(i=="\\x00\\t"):
                        current_stack.append("09")
                    elif(i=="\\x00\\r"):
                        current_stack.append("0D")
                    elif(i=="\\x00\\n"):
                        current_stack.append("0A")
                    else:
                        current_stack.append(i[4:].encode("utf-8").hex())
                elif(i[:2]=="\\x"):
                    current_stack.append(i[2:])
                else:
                    current_stack.append(i.encode("utf-8").hex())
        print(current_stack)
        stacks_strings.append(current_stack)
            
    #order is clubs, diamonds, spades, hearts
    final_stacks = []
    for stack in stacks_strings:
        stack_tuples = []
        for card in stack:
            if(int(card,16)>52):
                raise Exception("CARD OUT OF BOUNDS", int(card,16))
            suit = int(card,16) % 4 #0 is club, 1 is diamonds, 2 is hearts, 3 is spades
            value = int(card,16)//4 +1
            stack_tuples.append((suit, value))
        final_stacks.append(stack_tuples)
    print()
    return(final_stacks)
    

#print_board(getStacks(1988))
    
    
        