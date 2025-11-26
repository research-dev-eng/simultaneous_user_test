
file = "./inventory/hosts.ini"

string_to_be_replaced = "server01-1510"
new_string = "playbook/server01-1510/"

with open(file, "r") as f:
    lines = f.readlines()

update_lines = [line.replace(string_to_be_replaced, new_string) for line in lines]

with open(file, "w") as f:
    f.writelines(update_lines)

print("File updated in-place successfully")

