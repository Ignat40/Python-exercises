
def cat_single_file(file_path: str):
    with open(file_path, "r") as fd:
        data = fd.read()
        print(data)


while True:
    file_path = input("Input file path: ")
    if not file_path:
        break
    file_path.append(file_path)