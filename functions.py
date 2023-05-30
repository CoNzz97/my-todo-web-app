FILEPATH = "todos.txt"


def read_file(file_path="todos.txt"):
    with open(file_path, "r") as file:
        file_output = file.readlines()
        return file_output


def write_file(to_write, file_path="todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(to_write)


if __name__ == "__main__":
    print("Hello")
    print(read_file())
