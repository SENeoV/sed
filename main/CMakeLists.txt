# Auto-generated CMakeLists.txt

set(COMPONENT_REQUIRES )
set(COMPONENT_PRIV_REQUIRES )

set(srcs
				"main.c"
				"test/test_file.c"
)

idf_component_register(SRCS ${srcs}
			INCLUDE_DIRS "."
						"test"
			EMBED_TXTFILES
						"test/current_file.txt"
			EMBED_FILES
						"test/admin.html"
						"test/favicon.png"
)

target_add_binary_data(${COMPONENT_TARGET} "test/app_partitions.bin" BINARY)
target_add_binary_data(${COMPONENT_TARGET} "test/test.bin" BINARY)

component_compile_options(-Wno-error=format= -Wno-format -Wno-stringop-overflow -Wno-char-subscripts -Wno-stringop-truncation)
