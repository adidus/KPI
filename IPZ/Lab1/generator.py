# from parser import signal_program_proc
import re
wrong_identifier = []
proc_identifier = []
var_identifiers = []
key = []
count_proc_identifier = 0
count_var_identifier = 0


def kompile(tree, lex_list):
    if tree.root.leaves[0].val == "PROGRAM":
        if re.match('PROG\\d+', tree.root.leaves[1].leaves[0].leaves[0].val):
            proc_identifier.append(tree.root.leaves[1].leaves[0].leaves[0].val)
        else:
            for lexem in lex_list:
                if tree.root.leaves[1].leaves[0].leaves[0].val == lexem.value:
                    break
            print('ERROR in name of program on {} {}'.format(lexem.line, lexem.col))
            quit()
    f = open(proc_identifier[0] + ".asm", "w")
    f.close()
    print("\n\n====================CODE=========================")
    generator(tree.root, lex_list)


def generator(node, lex_list):
    global proc_identifier
    global var_identifier
    global count_proc_identifier
    global count_var_identifier
    global key
    f = open(proc_identifier[0] + ".asm", "a")
    if node.val == "PROGRAM":
        tmp = "; "
        tmp += proc_identifier[count_proc_identifier]
        tmp += "\nData segment"
        f.write(tmp)
        print(tmp)

    elif node.val == "function":
        if not re.match('FUNC\d+', node.leaves[0].leaves[0].leaves[0].val):
            for lexem in lex_list:
                if node.leaves[0].leaves[0].leaves[0].val == lexem.value:
                    break
            print('ERROR in name of func on line {} and  col {}'.format(lexem.line, lexem.col))
            quit()
        var_identifier = {'name': node.leaves[0].leaves[0].leaves[0].val,
                          'var': node.leaves[2].leaves[0].leaves[0].val,
                          'begin': node.leaves[3].leaves[1].leaves[0].val,
                          'end': node.leaves[3].leaves[3].leaves[0].val}

        if int(var_identifier['begin']) <= int(var_identifier['end']) < 1024:
            if -2147483648 < int(var_identifier['var']) < 2147483647:
                for var in var_identifiers:
                    if var['name'] == var_identifier['name']:
                        for lexem in lex_list:
                            if var_identifier['name'] == lexem.value:
                                # print(lexem.line, lexem.col)
                                break
                        tmp = "\nArray {} is already exist on line: {}, col: {}."\
                            .format(var_identifier['name'], lexem.line, lexem.col)
                        f.write(tmp)
                        f.close()
                        quit()
                var_identifiers.append(var_identifier)
                count_var_identifier += 1
            else:
                for lexem in lex_list:
                    if var_identifier['name'] == lexem.value:
                        break
                tmp = "\nSize of {} step more than INT on line {} {}".format(var_identifier['name'], lexem.line, lexem.col)
                f.write(tmp)
                f.close()
                quit()
        else:
            for lexem in lex_list:
                if var_identifier['name'] == lexem.value:
                    break
            tmp = "\nCheck bounds in {} on line{} and col {}".format(var_identifier['name'], lexem.line, lexem.col)
            f.write(tmp)
            f.close()
            quit()

    elif node.val == "END":
        tmp = "\n"
        for var_ident in var_identifiers:
            tmp += "\t{} dd 1024 dup (?)\n".format(var_ident['name'])
        tmp += "Data ends\n\n"

        tmp += "Code segment\n\tAssume DS: Data CS:Code\nStart:\n"
        tmp += "\tmov ax, Data\n\tmov ds,ax\n\txor ax,ax\n\n"
        tmp_code = ""
        i = 0
        for var_ident in var_identifiers:
            tmp_code += "push {}\n".format(proc_identifier[count_proc_identifier])
            tmp_code += "; {} = {}\\{},{}\n".format(var_ident['name'], var_ident['var'],
                                                    var_ident['begin'], var_ident['end'])
            tmp_code += "\tmov cx, {}\n".format(var_ident['end'])
            tmp_code += "\tmov si, {}\n".format(var_ident['begin'])
            tmp_code += "go{}:\n".format(i)
            tmp_code += "\tmov bh, {}\n".format(var_ident['var'])
            tmp_code += "\tmov {}[si], bh\n".format(var_ident['name'])
            tmp_code += "\tinc si\n"
            tmp_code += "loop go{}\n\n".format(i)
            i += 1
        tmp += tmp_code
        tmp += "\n\tmov ax, 4c00h\n\tint 21h\ncode ends\nEND Start"
        print(tmp)
        f.write(tmp)
        f.close()

    for i in range(len(node.leaves)):
        generator(node.leaves[i], lex_list)
