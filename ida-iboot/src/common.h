#ifndef _COMMON_H
#define _COMMON_H

#if defined(_WIN32) || defined(_WIN64)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#endif