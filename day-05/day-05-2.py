fo = open("input.txt", "r")
instr_list = fo.readline().strip().split(",")
fo.close()

# Convert all strings to ints in instruction list
for i in range(0, len(instr_list)):
    instr_list[i] = int(instr_list[i])

init_instr_list = instr_list.copy()
noun = 0
verb = 0
expected_output = 19690720
found = False
for i in range(0, 99):
    if found:
        break
    for j in range(0, 99):
        # Set initial conditions for program
        ip = 0
        instr_list = init_instr_list.copy()
        instr_list[1] = i
        instr_list[2] = j
        while ip < len(instr_list):
            # Add instruction
            if instr_list[ip] == 1:
                # Get addresses for opcode
                ref_a = instr_list[ip+1]
                ref_b = instr_list[ip+2]
                out = instr_list[ip+3]
                # Perform add operation
                instr_list[out] = instr_list[ref_a] + instr_list[ref_b]
                # Step to next instruction
                ip += 4
            # Multiply instruction
            elif instr_list[ip] == 2:
                # Get addresses for opcode
                ref_a = instr_list[ip+1]
                ref_b = instr_list[ip+2]
                out = instr_list[ip+3]
                # Perform multiply operation
                instr_list[out] = instr_list[ref_a] * instr_list[ref_b]
                # Step to next instruction
                ip += 4        
            # Stop execution instruction
            elif instr_list[ip] == 99:
                break
            # Unknown instruction
            else:
                print("Unknown instruction")
        if instr_list[0] == expected_output:
            noun = i
            verb = j
            break
    
print(str(100 * noun + verb))
