from dis import dis  # Disassembled Python bytecode

print("compile tuple ->")
dis(compile('123, "a"', 'string', 'eval'))

print("compile list ->")
dis(compile('[1,2,3, "a"]', 'string', 'eval'))
