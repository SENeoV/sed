import os

def generate_cmake_lists(root_folder):
    cmake_content = "# Auto-generated CMakeLists.txt\n\n"
    cmake_content += "set(COMPONENT_REQUIRES )\n"
    cmake_content += "set(COMPONENT_PRIV_REQUIRES )\n\n"

    source_files = []
    embed_txt_files = []
    embed_files = []

    for foldername, subfolders, filenames in os.walk(os.path.join(root_folder, "sources")):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            relative_path = os.path.relpath(file_path, root_folder)

            if filename.endswith(('.c', '.h')):
                source_files.append(f'\t\t\t\t"{relative_path}"\n')
            elif filename.endswith('.txt'):
                embed_txt_files.append(f'\t\t\t\t\t\t"{relative_path}"\n')
            elif filename.endswith(('.png', '.html')):
                embed_files.append(f'\t\t\t\t\t\t"{relative_path}"\n')

    cmake_content += "set(srcs\n"
    cmake_content += "".join(source_files)
    cmake_content += ")\n\n"

    cmake_content += 'idf_component_register(SRCS ${srcs}\n'
    cmake_content += '\t\t\tINCLUDE_DIRS "."\n'
    
    for foldername, _, _ in os.walk(os.path.join(root_folder, "sources")):
        if foldername != root_folder:
            relative_path = os.path.relpath(foldername, root_folder)
            cmake_content += f'\t\t\t\t\t\t"{relative_path}"\n'
    
    cmake_content += '\t\t\tEMBED_TXTFILES\n'
    cmake_content += "".join(embed_txt_files)
    cmake_content += '\t\t\tEMBED_FILES\n'
    cmake_content += "".join(embed_files)
    cmake_content += ')\n\n'

    cmake_content += 'target_add_binary_data(${COMPONENT_TARGET} "test/app_partitions.bin" BINARY)\n'
    cmake_content += 'target_add_binary_data(${COMPONENT_TARGET} "test/test.bin" BINARY)\n\n'
    
    cmake_content += 'component_compile_options(-Wno-error=format= -Wno-format -Wno-stringop-overflow -Wno-char-subscripts -Wno-stringop-truncation)\n'

    cmake_file_path = os.path.join(root_folder, "CMakeLists.txt")
    with open(cmake_file_path, "w") as cmake_file:
        cmake_file.write(cmake_content)

    print(f"CMakeLists.txt generated at: {cmake_file_path}")

if __name__ == "__main__":
    project_folder = os.path.dirname(os.path.abspath(__file__))
    generate_cmake_lists(project_folder)