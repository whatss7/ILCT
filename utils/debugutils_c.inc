#include <stdio.h>
#include <stdarg.h>
#include <string.h>

#ifdef debug_offline
void debugp(const char *fmt, ...) {
	fprintf(stderr, "DBG: ");
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	if (fmt[strlen(fmt) - 1] != '\n') {
		fprintf(stderr, "\n");
	}
	va_end(args);
}
#else // debug_offline
void debugp(const char *fmt, ...) {}
#endif // debug_offline

int __new_main();

int main() {
    #ifdef running_offline
    freopen("in.txt", "r", stdin);
    #endif // running_offline

    #ifdef checking_offline
    freopen("out.txt", "w", stdout);
    #endif // checking_offline
    
    __new_main();
}

#define main __new_main