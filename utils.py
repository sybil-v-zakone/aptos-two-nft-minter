def read_file_lines(path: str) -> list[str]:
    with open(file=path, mode="r") as file:
        return [line.strip() for line in file]
