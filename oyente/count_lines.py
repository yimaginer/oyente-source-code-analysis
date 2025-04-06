import os

def count_lines_in_py_files(directory):
    total_lines = 0
    py_files = [os.path.join(root, file) 
                for root, _, files in os.walk(directory) 
                for file in files if file.endswith('.py')]

    for py_file in py_files:
        relative_path = os.path.relpath(py_file, directory)  # 获取相对路径
        with open(py_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            total_lines += line_count
            print(f"{relative_path}: {line_count} lines")

    print(f"\nTotal lines of code in .py files: {total_lines}")

if __name__ == "__main__":
    oyente_dir = os.path.dirname(__file__)  # 当前脚本所在目录
    count_lines_in_py_files(oyente_dir)