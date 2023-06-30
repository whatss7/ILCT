#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
int r(int mn, int mx) {
	if (mn == mx) return mx;
	return abs(rand() * rand()) % (mx - mn + 1) + mn;
}
int _min(int a, int b) { return a < b ? a : b; }
void print_one_case(FILE *file, int *argmn, int *argmx, int argsz, int sizepos,
                    int mn, int mx, int ins_size, bool ins_in_line, int force_size = -1) {
	int mxn = argmx[sizepos];
	int mnn = argmn[sizepos];
	int n = force_size;
	if (n < 0) n = r(argmn[sizepos], argmx[sizepos]);
	for (int i = 0; i < argsz; i++) {
		if (i == sizepos) {
			fprintf(file, "%d%c", n, i == argsz - 1 ? '\n' : ' ');
		} else {
			fprintf(file, "%d%c", r(argmn[i], argmx[i]),
			        i == argsz - 1 ? '\n' : ' ');
		}
	}
	if(ins_in_line){
		for (int i = 0; i < n; i++) {
			for (int i = 0; i < ins_size; i++) {
				fprintf(file, "%d%c", r(mn, mx), i == ins_size - 1 ? '\n' : ' ');
			}
		}
	} else {
		for (int i = 0; i < ins_size; i++) {
			for (int i = 0; i < n; i++) {
				fprintf(file, "%d%c", r(mn, mx), i == n - 1 ? '\n' : ' ');
			}
		}
	}
}
int main() {
	FILE *fout = fopen("in.txt", "w");
	int t = -1, mx, mn, argmn[1010], argmx[1010];
	char type[1010];
	int ins_size = 1;
	bool ins_in_line = false;
	srand((unsigned)time(NULL));
	printf("----------RANDGEN----------\n");
	printf("(0 for single case, -1 for advanced control)\n");
	while (t < 0) {
		printf("test case number: ");
		scanf("%d", &t);
		if (t < 0) {
			getchar();
			printf("type (normal, advanced): ");
			scanf("%[^\n]", type);
		}
	}
	int argcnt = 1, sizepos = 0;
	if (strcmp(type, "advanced") == 0) {
		printf("argument count: ");
		scanf("%d", &argcnt);
		printf("size position (0-indexed): ");
		scanf("%d", &sizepos);
		for (int i = 0; i < argcnt; i++) {
			printf("range for argument %d: ", i);
			scanf("%d%d", &argmn[i], &argmx[i]);
			if (argmn[i] > argmx[i]) {
				int t = argmn[i];
				argmn[i] = argmx[i];
				argmx[i] = t;
			}
		}
		printf("instance size: ");
		scanf("%d", &ins_size);
		printf("instance in one line (0 for false): ");
		int tmp;
		scanf("%d", &tmp);
		ins_in_line = (tmp != 0);
	} else {
		printf("max size: ");
		scanf("%d", &argmx[0]);
		argmn[0] = _min(argmx[0], argmx[0] / 2 + 1);
	}
	printf("number range: ");
	scanf("%d%d", &mn, &mx);
	if (t != 0) {
		fprintf(fout, "%d\n", t--);
	}
	print_one_case(fout, argmn, argmx, argcnt, sizepos, mn, mx, ins_size, ins_in_line, argmx[sizepos]);
	while (t--) {
		print_one_case(fout, argmn, argmx, argcnt, sizepos, mn, mx, ins_size, ins_in_line);
	}
	return 0;
}
