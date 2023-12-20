
# python script to generate a CMakeLists.txt from reading all the contents of the subfolder 
# named "sources" and recursively subfolders checking every code file .c or .h to add it this way, 
# do the same with .png, .html, or any other file which could be contained in this CMakeLists.txt:

# set(COMPONENT_REQUIRES )
# set(COMPONENT_PRIV_REQUIRES )

set(srcs 
                    #NO SUBFOLDER
                    "main.c"

                    #TEST FOLDER
                    "test/test_file.c"
)

idf_component_register( SRCS            "${srcs}"

                        INCLUDE_DIRS    "."
                                        "test"

                        EMBED_TXTFILES  test/cert.pem
                                        test/key.pem
                                        
                        EMBED_FILES     test/favicon.png
                                        test/admin.html
)

target_add_binary_data(${COMPONENT_TARGET} "test/app_partitions.bin" BINARY)
target_add_binary_data(${COMPONENT_TARGET} "test/test.bin" BINARY)
    
component_compile_options(-Wno-error=format= -Wno-format -Wno-stringop-overflow -Wno-char-subscripts -Wno-stringop-truncation)