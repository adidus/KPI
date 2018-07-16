import os
import Data
import LexicalAnalysis as LexAn
import SynOff as syntax

def main():
    asm_file = open(Data.WAYTOASM)
    tmp_file = open(Data.WAYTOLST,'w')
    count_line = 0
    j = 0
    ListOfSen = []
    SenLine_string = []
    SenLine_offset = []
    offset = []
    for line in asm_file:
        line = line.replace('\n',''). replace('\t','')
        lst = LexAn.ParseFileToList(line)
        if len(lst) == 0:
            continue
        #print(lst)
        SenLine = []
        SenLine.append([line])
        i = 0;
        count = len(lst)
        while i < count:
            _type = LexAn.SetLexemeType(lst[i])
            SenLine.append([lst[i], _type])
            i += 1

        #print(SenLine[1:])
        ListOfSen.append(syntax.SenLine(SenLine[1:]))
        #print(syntax.isStartSegment(ListOfSen[j]))
        ListOfSen[j].SyntaxSize()
        you = syntax.DecToHex(ListOfSen[j].getOffset())
        SenLine_offset.append(you)
        SenLine_string.append(SenLine[0][0])
        #print(you)
        #print(SenLine[0][0])
        j += 1
        if(Data.stopflag == True):
            print('(! Error on line {0})'.format(j+1), file = tmp_file )
            break
    offset.append('0000')
    offset.extend(SenLine_offset)
    #offset.pop()

    #print(offset)
    #print(SenLine_string)
    offset[-2] = offset[-3]
    for j in range(0,len(SenLine_string)):
        print(offset[j]+'     '+SenLine_string[j],file = tmp_file )
    print('N a m e        Size	      Length    Align	Combine Class',file= tmp_file)
    for item in Data.seg:
        print(item[0].ljust(10,'.')+'     '+'32 Bit'+ '     ' + offset[item[1]-1]+'     '+'PARA	   NONE' ,file = tmp_file)
    print('N a m e        Type	   Value	 Attr', file = tmp_file)
    for item in syntax.SenLine.ListLabels_type:
        print(item[0].ljust(10,'.') + '     ' + 'NEAR' + '     ' + offset[item[1]] + '     ' + item[2],file = tmp_file)

    for item in syntax.SenLine.ListVar:
        print(item[0].ljust(10,'.')+'     '+item[1].ljust(4,' ') +'     '+offset[item[2]-1]+ '     '+item[3],file = tmp_file)
    print('@FILENAME  . . . . . . . . . . .')
    print(syntax.SenLine.ListVar)
    print(Data.Segments)
    print (tmp_file)
    tmp_file.close()




    
    my_file = open(Data.WAYTOASM, 'r')
    my_string = my_file.read()
    print(my_string)
    my_file.close()
    print(Data.Var)

    # while i < count:
    #     lst[i] = lst[i].upper()
    #     if re.match('\'.*',lst[i]) or re.match('".*',lst[i]):
    #         lst[i] += ' ' + lst[i+1]
    #         lst.pop()
    #         count -= 1
    #         lst[i] = lst[i].lower()
    #
    #     if re.search('.([:\\+\\*\\[\\],])',lst[i]):
    #         pat = '([{}])'.format(re.escape(string.punctuation))
    #         buf = lst[i+1:count]
    #         s = lst[i]
    #         DelFromList(lst,i,count-1)
    #         tmp = re.split(pat, s)
    #
    #         for node in tmp:
    #             if node == '':
    #                 tmp.remove(node)
    #         lst.extend(tmp)
    #         lst.extend(buf)
    #         count = len(lst)
    #
    #     i+=1
    # i=0

main()