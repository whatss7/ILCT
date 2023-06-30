#ifdef PYRUN_DEBUG_MODE
#include <bits/stdc++.h>
using namespace std;

#ifdef running_offline
int ___unused = (freopen("in.txt", "r", stdin), 0);
#endif // running_offline

#ifdef checking_offline
int ___unused_2 = (freopen("out.txt", "w", stdout), 0);
#endif // checking_offline

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
void debuge(function<void()> action) {
	action();
}
#else // debug_offline
void debugp(const char *fmt, ...) {}
void debuge(function<void()> action) {}
#endif // debug_offline
#endif // PYRUN_DEBUG_MODE

#ifdef PYRUN_HACK_MODE
#include <bits/stdc++.h>
void debugp(const char *fmt, ...) {}
void debuge(std::function<void()> action) {}
int __new_main();
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	auto start = std::chrono::high_resolution_clock::now();
	__new_main();
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	std::cerr << "\nTime elapsed: " << duration.count() / 1000.0 << " ms.\n";
}
#define main __new_main
#endif

#ifdef PYRUN_HACKGEN_MODE
#include <bits/stdc++.h>
using namespace std;
void debugp(const char *fmt, ...) {}
void debuge(std::function<void()> action) {}
int ___unused_2 = (freopen("in.txt", "w", stdout), 0);
#endif