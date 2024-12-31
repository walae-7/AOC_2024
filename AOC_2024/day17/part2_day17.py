data = open("data.txt").read().splitlines()
reg_b = int(data[1].split(":")[1])
reg_c = int(data[2].split(":")[1])
program = data[4].split(" ")[1].split(",")
int_program = [int(x) for x in program]

print(f"program: {program[15]}")

def combo_operand_to_value(operand):
    match operand:
        case '0':
            return 0
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return reg_a
        case '5':
            return reg_b
        case '6':
            return reg_c

def power(y):
    if y == 0:
        return 1

    if y >= 1:
        return 2 * power(y - 1)


def execute_op_code(opcode, x, ip, result):
    global reg_a, reg_b, reg_c
    new_ip = ip
    new_result = result[:]
    match opcode:
        case '0':
            reg_a = int(reg_a//(power(combo_operand_to_value(x))))
            new_ip += 2
        case '1':
            reg_b = int (int(reg_b) ^ int(x) )
            new_ip += 2
        case '2':
            reg_b = int(combo_operand_to_value(x) % 8)
            new_ip += 2
        case '3':
            if reg_a != 0:
                new_ip = int(x)
            else:
                new_ip += 2
        case '4':
            reg_b = int(reg_b ^ reg_c)
            new_ip += 2

        case '5':
            if new_result != "":
                new_result += "," + str(combo_operand_to_value(x) % 8)
            else:
                new_result += str(combo_operand_to_value(x) % 8)
            new_ip += 2
        case '6':
            reg_b = int(reg_a//(power(combo_operand_to_value(x))))
            new_ip += 2
        case '7':
            reg_c = int(reg_a//(power(combo_operand_to_value(x))))
            new_ip += 2
    return new_ip, new_result


def run_program(program, reg):
    global reg_a
    reg_a = reg
    ip = 0
    result = ""
    while ip < len(program):
        opcode = program[ip]
        x = program[ip+1]
        ip, result = execute_op_code(opcode, x, ip, result)
    return list(result.split(","))

queue = [(0, 15)]
i = 15

while i >= 0 and queue:  
    element, i = queue.pop(0)
    for n in range(8):
        result = run_program(program, element + n*8**i)[i:]
        expected = program[i:]
        if result == expected:
            queue.append((element + n*8**i, i - 1))
            

print(f"this are the values of reg_a that output the program: {[element[0] for element in queue]}")
print(f"the smalles value of reg_a that outputs the program is: {min([element[0] for element in queue])}")