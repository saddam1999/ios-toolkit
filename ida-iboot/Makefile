.PHONY: all clean

SRCS := $(shell find src/ -name '*.cpp')
OBJS_WINDOWS := $(patsubst src/%, obj/windows/%.obj, $(SRCS))
OBJS_LINUX := $(patsubst src/%, obj/linux/%.o, $(SRCS))

CLANG := clang++

CFLAGS := \
	-Werror \
	-Wall \
	-Wno-nullability-completeness \
	-Wno-unused-private-field \
	-Wno-varargs \
	-O3 \
	-flto \
	-g \
	-I$(IDASDK)/include \
	-I$(IDASDK)/ldr

CFLAGS_WINDOWS := \
	-target x86_64-unknown-windows \
	$(CFLAGS)

LDFLAGS_WINDOWS := \
	-target x86_64-pc-windows \
	-Wl,-subsystem:windows \
	-Wl,-debug \
	-fuse-ld=lld-link

CFLAGS_LINUX := \
	$(CFLAGS) \
	-target x86_64-linux-gnu

LDFLAGS_LINUX := \
	-target x86_64-linux-gnu

TARGET ?= linux

all: $(TARGET)

windows: bin/iboot.dll
linux: bin/iboot.so

clean:
	mkdir -p bin obj
	rm -r bin obj

bin/iboot.dll: $(OBJS_WINDOWS)
	mkdir -p $(@D)
	$(CLANG) $(LDFLAGS_WINDOWS) -o $@ $^

bin/iboot.so: $(OBJS_LINUX)
	mkdir -p $(@D)
	$(CLANG) $(LDFLAGS_LINUX) -o $@ $^

obj/windows/%.cpp.obj: src/%.cpp
	mkdir -p $(@D)
	$(CLANG) $(CFLAGS_WINDOWS) -c -o $@ $<

obj/linux/%.cpp.o: src/%.cpp
	mkdir -p $(@D)
	$(CLANG) $(CFLAGS_LINUX) -c -o $@ $<
