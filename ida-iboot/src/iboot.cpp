#include <ida.hpp>
#include <idaldr.h>

#include "common.h"

int idaapi accept_file(qstring* fileformatname, qstring* processor, linput_t* li, const char* filename) {
	return 0;
}

void idaapi load_file(linput_t* file, ushort neflags, const char* formatname) {
}

int idaapi save_file(FILE* file, const char* formatname) {
	return 0;
}
 
EXPORT loader_t LDSC = {
	IDP_INTERFACE_VERSION,
	0,
	accept_file,
	load_file,
	save_file,
	nullptr,
	nullptr
};
