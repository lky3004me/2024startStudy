def assemble_instruction(instruction):
    # 명령어들을 opcode에 따라 매핑
    opcode_map = {
        "ADD": "0000",
        "SUB": "0001",
        "MOV": "0010",
        "AND": "0011",
        "OR": "0100",
        "NOT": "0101",
        "MULT": "0110",
        "LSFTL": "0111",
        "LSFTR": "1000",
        "ASFTR": "1001",
        "RL": "1010",
        "RR": "1011"
    }

    parts = instruction.split()
    cmd = parts[0]
    rd = int(parts[1])
    ra = int(parts[2])
    if cmd[-1] == 'C':  # immediate value를 사용하는 경우
        rb = int(parts[3])
        cmd = cmd[:-1]
        c_flag = '1'
    else:  # 일반적인 경우
        rb = int(parts[3])
        c_flag = '0'

    # opcode 결정
    opcode = opcode_map[cmd]

    # rd, ra, rb를 3비트 이진수로 변환
    rd_bin = f"{rd:03b}"
    ra_bin = f"{ra:03b}"
    rb_bin = f"{rb:04b}" if c_flag == '1' else f"{rb:03b}"

    # 결과 16비트 명령어 생성
    result = opcode + c_flag + "0" + rd_bin + ra_bin + rb_bin

    return result

# 입력받기
instruction = input().strip()
# 명령어 변환
binary_instruction = assemble_instruction(instruction)
# 결과 출력
print(binary_instruction)
