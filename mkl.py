import os

def generate_cmake_lists(root_folder):
    cmake_content = "# Auto-generated CMakeLists.txt\n\n"
    cmake_content += "set(COMPONENT_REQUIRES )\n"
    cmake_content += "set(COMPONENT_PRIV_REQUIRES )\n\n"
    cmake_content += "set(srcs\n"

    for foldername, subfolders, filenames in os.walk(os.path.join(root_folder, "sources")):
        if foldername != root_folder:
            relative_path = os.path.relpath(foldername, root_folder)
            cmake_content += f"\n\t\t\t\t# {relative_path.upper()}\n"

        for filename in filenames:
            if filename.endswith(('.c', '.h', '.png', '.html')):
                file_path = os.path.join(foldername, filename)
                relative_path = os.path.relpath(file_path, root_folder)
                cmake_content += f'\t\t\t\t"{relative_path}"\n'

    cmake_content += ")\n\n"
    cmake_content += "idf_component_register(SRCS ${srcs}\n"
    cmake_content += "\t\t\tINCLUDE_DIRS \""
    
    for foldername, _, _ in os.walk(os.path.join(root_folder, "sources")):
        if foldername != root_folder:
            relative_path = os.path.relpath(foldername, root_folder)
            cmake_content += f'"{relative_path}" '

    cmake_content += '"\n'
    cmake_content += '\t\t\t\t\t\t"test"\n'
    cmake_content += "\t\t\tEMBED_TXTFILES test/cert.pem\n"
    cmake_content += "\t\t\t\t\t\ttest/key.pem\n"
    cmake_content += "\t\t\tEMBED_FILES test/favicon.png\n"
    cmake_content += "\t\t\t\t\t\ttest/admin.html)\n\n"

    cmake_content += 'target_add_binary_data(${COMPONENT_TARGET} "test/app_partitions.bin" BINARY)\n'
    cmake_content += 'target_add_binary_data(${COMPONENT_TARGET} "test/test.bin" BINARY)\n\n'
    
    cmake_content += 'component_compile_options(-Wno-error=format= -Wno-format -Wno-stringop-overflow -Wno-char-subscripts -Wno-stringop-truncation)\n'

    with open(os.path.join(root_folder, "CMakeLists.txt"), "w") as cmake_file:
        cmake_file.write(cmake_content)

if __name__ == "__main__":
    project_folder = r"C:\Users\Javi\sed"  # Change this to your actual project folder
    generate_cmake_lists(project_folder)
