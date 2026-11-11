FILE_NAME = "sample_data.txt"


def main():
    print("=== read() 讀取全文 ===")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")

    print("\n=== readline() 讀取第一行 ===")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        first_line = file.readline()
        print(first_line, end="")

    print("\n=== 逐行讀取 ===")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.rstrip('\n')}")

    print("=== readlines() 計算行數 ===")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"總行數：{len(lines)}")


if __name__ == "__main__":
    main()