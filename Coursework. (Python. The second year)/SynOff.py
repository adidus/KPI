import Data
import re

class SenLine:
    offset = 0
    ListLabels = []
    ListLabels_type = []
    ListVar = []
    count_sentence = 0
    def __init__(self,ListOfLexems):
        self.Label_num = -1
        self.Label_name = ''
        self.Mnemocode_num = -1
        self.Mnemocode_name = ''
        self.ListOperands = []
        self.ListOperands_type = []
        SenLine.count_sentence += 1
        if ListOfLexems[0][-1] == 'ID':
            self.Label_num = 0
            self.Label_name = ListOfLexems[0][0]
        if self.Label_name != '':
            if ListOfLexems[1][0] == ':':
                SenLine.ListLabels.append(self.Label_name)
                SenLine.ListLabels_type.append([self.Label_name,SenLine.count_sentence,Data.active_segment])
                #print(SenLine.ListLabels)

        count = 0
        for item in ListOfLexems:
            if item[-1] == 'COMMAND' or item[-1] == 'DIRECTIVE' or item[-1] == 'TYPE':
                self.Mnemocode_num = count
                self.Mnemocode_name = item[0]
                break
            count += 1
        temp = []
        temp_type = []
        if self.Mnemocode_num != -1 :
            for i in range(self.Mnemocode_num+1,len(ListOfLexems)):
                if(ListOfLexems[i][0] != ','):
                    temp.append(ListOfLexems[i][0])
                    temp_type.append(ListOfLexems[i][-1])
                else:
                    self.ListOperands.append(temp[:])
                    self.ListOperands_type.append(temp_type[:])
                    temp.clear()
                    temp_type.clear()
            if len(temp) != 0:
                self.ListOperands.append(temp[:])
                self.ListOperands_type.append(temp_type[:])
            #print(self.ListOperands)

        if isStartSegment(self):
            Data.active_segment = self.Label_name

        if isVrble(self):
            SenLine.ListVar.append([self.Label_name,self.Mnemocode_name,SenLine.count_sentence,Data.active_segment])
            if self.Label_name in Data.Segments[Data.active_segment]:
                Data.stopflag = True
            else:
                Data.Segments[Data.active_segment].append(self.Label_name)
        if isEndSegment(self):
            Data.seg.append([Data.active_segment,SenLine.count_sentence])
    def SyntaxSize(self):
        if Data.segment_end_flag:
            SenLine.offset = 0
            Data.segment_end_flag = False
        if isStartSegment(self):
            SenLine.offset = 0
        if  isEndSegment(self):
            SenLine.offset = 0
            Data.segment_end_flag = True
        if isVrble(self):
            if self.Mnemocode_name == 'DB':
                if int(self.ListOperands[0][0]) < 255 and int(self.ListOperands[0][0]) > -255:
                    Data.Var['DB'].append(self.Label_name)
                    SenLine.offset += 1
                else:
                    Data.stopflag = True
            if self.Mnemocode_name == 'DW':
                Data.Var['DW'].append(self.Label_name)
                SenLine.offset += 2
            if self.Mnemocode_name == 'DD':
                Data.Var['DD'].append(self.Label_name)
                SenLine.offset += 4
        if self.Mnemocode_name == 'STI':
            SenLine.offset += 1
            if len(self.ListOperands) != 0:
                Data.stopflag = True
        if self.Mnemocode_name == 'POP':
            if self.ListOperands_type[0][0] == '32_REG' and len(self.ListOperands) == 1:
                SenLine.offset += 1
            else:
                Data.stopflag = True


        if self.Mnemocode_name == 'CMP':
            if len(self.ListOperands) == 2:
                if self.ListOperands_type[0][0] == '32_REG' and self.ListOperands_type[1][0] == '32_REG':
                    SenLine.offset += 2
                elif self.ListOperands_type[0][0] == '8_REG' and self.ListOperands_type[1][0] == '8_REG':
                    SenLine.offset += 2
                else:
                    Data.stopflag = True
            else:
                Data.stopflag = True

        if self.Mnemocode_name == 'MOV':
            mem, off = isMemmory(self.ListOperands_type[1])
            # if self.ListOperands_type[0][0] == '32_REG' and mem:
            if re.match('32_REG|8_REG', self.ListOperands_type[0][0]) and mem:
                SenLine.offset += off
                if len(self.ListOperands[1]) > 1 and (self.ListOperands_type[1][0] == 'SEG_REG' or self.ListOperands_type[1][2] == 'SEG_REG'):
                    if re.match('SS|CS|ES', self.ListOperands[1][2]) or re.match('SS|CS|ES', self.ListOperands[1][0]):
                        SenLine.offset += 1
            elif re.match('HEX|DEC|BIN', self.ListOperands_type[1][0]):
                mem, off = isMemmory(self.ListOperands_type[0])
                print(Data.Var)
                if mem:
                    if self.ListOperands[0][0] == 'DWORD':
                        SenLine.offset += 11
                        if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                            if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                                SenLine.offset += 1
                    elif self.ListOperands[0][0] == 'BYTE':
                        SenLine.offset += 8
                        if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                            if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                                SenLine.offset += 1
                    elif self.ListOperands[0][0] in Data.Var['DD']:
                        SenLine.offset += 4
                        if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                            if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                                SenLine.offset += 1
                    elif self.ListOperands[0][0] in Data.Var['DW']:
                        SenLine.offset += 2
                        if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                            if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                                SenLine.offset += 1
                    elif self.ListOperands[0][0] in Data.Var['DB']:
                        SenLine.offset += 7

                    else:
                        Data.stopflag = True
                else:
                    Data.stopflag = True
            else:
                Data.stopflag = True

        # if self.Mnemocode_name == 'INC':
        #     mem, off = isMemmory(self.ListOperands_type[0])
        #     if mem:
        #         if self.ListOperands[0][0] == 'DWORD':
        #             SenLine.offset += 6
        #             if len(self.ListOperands[0]) > 1:
        #                 if not re.match('DS', self.ListOperands[0][2]):
        #                     SenLine.offset += 1
        #             elif not re.match('DS', self.ListOperands[0][0]):
        #                     SenLine.offset += 1
        #         elif self.ListOperands[0][0] == 'BYTE':
        #             SenLine.offset += 8
        #             if len(self.ListOperands[0]) > 1:
        #                 if not re.match('DS', self.ListOperands[0][2]):
        #                     SenLine.offset += 1
        #             elif not re.match('DS', self.ListOperands[0][0]):
        #                     SenLine.offset += 1
        #         elif self.ListOperands[0][0] in Data.Var['DD']:
        #             SenLine.offset += 5
        #             if len(self.ListOperands[0]) > 1:
        #                 if not re.match('DS', self.ListOperands[0][2]):
        #                     SenLine.offset += 1
        #             elif not re.match('DS', self.ListOperands[0][0]):
        #                     SenLine.offset += 1
        #         elif self.ListOperands[0][0] in Data.Var['DW']:
        #             SenLine.offset += 7
        #             if len(self.ListOperands[0]) > 1:
        #                 if not re.match('DS', self.ListOperands[0][2]):
        #                     SenLine.offset += 1
        #             elif not re.match('DS', self.ListOperands[0][0]):
        #                     SenLine.offset += 1
        #         elif self.ListOperands[0][0] in Data.Var['DB']:
        #             SenLine.offset += 5
        #             if len(self.ListOperands[0]) > 1:
        #                 if not re.match('DS', self.ListOperands[0][2]):
        #                     SenLine.offset += 1
        #             elif not re.match('DS', self.ListOperands[0][0]):
        #                     SenLine.offset += 1
        #         else:
        #             Data.stopflag = True
        #     else:
        #         Data.stopflag = True

        if self.Mnemocode_name == 'INC':
            mem, off = isMemmoryAND(self.ListOperands_type[0])
            if mem and len(self.ListOperands) == 1:
                SenLine.offset += off
                if self.ListOperands_type[0][0] == 'ID':
                    if self.ListOperands[0][0] in Data.Var['DW']:
                        SenLine.offset += 1
                if len(self.ListOperands[0]) > 1 and self.ListOperands_type[0][2] == 'ID':
                    if self.ListOperands[0][2] in Data.Var['DW']:
                        SenLine.offset += 1
                if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                    if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                        SenLine.offset += 1
            else:
                Data.stopflag = True


        if self.Mnemocode_name == 'AND':
            mem, off = isMemmoryAND(self.ListOperands_type[0])
            if mem and len(self.ListOperands) == 2:
                if self.ListOperands_type[1][0] == '32_REG':
                    SenLine.offset += off
                    if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                        if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                            SenLine.offset += 1
                elif self.ListOperands_type[1][0] == '8_REG':
                    SenLine.offset += off
                    if len(self.ListOperands[0]) > 1 and (self.ListOperands_type[0][0] == 'SEG_REG' or self.ListOperands_type[0][2] == 'SEG_REG'):
                        if re.match('SS|CS|ES', self.ListOperands[0][2]) or re.match('SS|CS|ES', self.ListOperands[0][0]):
                            SenLine.offset += 1
                else:
                    Data.stopflag = True
            else:
                Data.stopflag = True


        if self.Mnemocode_name == 'XOR':
            if len(self.ListOperands) == 2:
                if re.match('HEX|DEC|BIN', self.ListOperands_type[1][0]):
                    if self.ListOperands_type[0][0] == '32_REG':
                        if self.ListOperands[0][0] == 'EAX':
                            SenLine.offset += 5
                        else:
                            SenLine.offset += 6
                    elif self.ListOperands_type[0][0] == '8_REG':
                        if self.ListOperands[0][0] == 'AL':
                            SenLine.offset += 2
                        else:
                            SenLine.offset += 3
                    else:
                        Data.stopflag = True
                else:
                    Data.stopflag = True
            else:  
                Data.stopflag = True
            

        if self.Mnemocode_name == 'JNZ':
            if self.ListOperands[0][0] in SenLine.ListLabels:
                SenLine.offset += 2
            elif len(self.ListOperands) == 0:
                Data.stopflag = True
            else:
                SenLine.offset += 6
    @staticmethod
    def getOffset():
        return SenLine.offset


def isVrble(var):

    type = ['DB', 'DD', 'DW']
    if var.Label_num == 0 and var.Mnemocode_name in type:
        return True
    else:
        return False

def isStartSegment(var):
    if var.Label_num == 0 and var.Mnemocode_name == 'SEGMENT':
        Data.Segments[var.Label_name]=[]
        return True
    else:
        return False

def isEndSegment(var):
    if (var.Label_num == 0 and var.Mnemocode_name == 'ENDS') :
        return True
    else:
        return False
def isMemmory(operand):
    string = " ".join(operand)
    if string in Data.Memmory.keys():
        return True, Data.Memmory[string]
    else:
        return False, 0

def isMemmoryAND(operand):
    string = " ".join(operand)
    if string in Data.MemAND.keys():
        return True, Data.MemAND[string]
    else:
        return False, 0

def DecToHex(off):
    dec = hex(off)
    dec = dec.replace("x", "0")
    if len(dec) < 4:
        dec = "0" + dec
    return str(dec.upper())

def isReg(operand):
    if operand[0] == '32_REG' or operand[0] == '8_REG':
        return True
    else:
        return False
def idFromOperand(Operand):
    count = 0
    for item in Operand:
        if item == 'ID':
            return count
        else:
            count += 1
    return count