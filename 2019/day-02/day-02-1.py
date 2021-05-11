fo = open("input.txt", "r")
instr_list = fo.readline().strip().split(",")
fo.close()

# Convert all strings to ints in instruction list
for i in range(0, len(instr_list)):
    instr_list[i] = int(instr_list[i])
i = 0
while i < len(instr_list):
    # Add instruction
    if instr_list[i] == 1:
        # Get addresses for opcode
        ref_a = instr_list[i+1]
        ref_b = instr_list[i+2]
        out = instr_list[i+3]
        # Perform add operation
        instr_list[out] = instr_list[ref_a] + instr_list[ref_b]
        # Step to next instruction
        i += 4
    # Multiply instruction
    elif instr_list[i] == 2:
        # Get addresses for opcode
        ref_a = instr_list[i+1]
        ref_b = instr_list[i+2]
        out = instr_list[i+3]
        # Perform multiply operation
        instr_list[out] = instr_list[ref_a] * instr_list[ref_b]
        # Step to next instruction
        i += 4        
    # Stop execution instruction
    elif instr_list[i] == 99:
        break
    # Unknown instruction
    else:
        print("Unknown instruction")

output = open("output.txt", "w")
print(*instr_list, sep=",", file=output)
output.close()
