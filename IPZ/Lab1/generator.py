# from parser import signal_program_proc

wrong_identifier = []
proc_identifier = []
var_identifiers = []
key = []
count_proc_identifier = 0
count_var_identifier = 0


def kompile(tree):
    f = open("test.asm", "w")
    f.close()
    if tree.root.leaves[0].val == "procedure-identifier":
        ident = tree.root.leaves[0].leaves[0].leaves[0].val
        if ident in proc_identifier:
            wrong_identifier.append(ident)
        proc_identifier.append(tree.root.leaves[0].leaves[0].leaves[0].val)
    if tree.root.leaves[0].val == "PROGRAM":
        proc_identifier.append(tree.root.leaves[1].leaves[0].leaves[0].val)
    print("\n\n====================CODE=========================")
    generator(tree.root)


def generator(node):
    f = open("test.asm", "a")
    global proc_identifier
    global var_identifier
    global count_proc_identifier
    global count_var_identifier
    global key
    if node.val == "PROGRAM":
        tmp = "; "
        tmp += proc_identifier[count_proc_identifier]
        tmp += "\nData segment"
        f.write(tmp)
        print(tmp)

    elif node.val == "function":
        var_identifier = {'name': node.leaves[0].leaves[0].leaves[0].val,
                          'var': node.leaves[2].leaves[0].leaves[0].val,
                          'begin': node.leaves[3].leaves[1].leaves[0].val,
                          'end': node.leaves[3].leaves[3].leaves[0].val}
        for var in var_identifiers:
            if var['name'] == var_identifier['name']:
                tmp = "\nArray {} is already exist.".format(var_identifier['name'])
                f.write(tmp)
                f.close()
                quit()
        var_identifiers.append(var_identifier)
        count_var_identifier += 1

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
        generator(node.leaves[i])
