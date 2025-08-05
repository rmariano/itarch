+++
title = "strncpy and strncat for copying strings in C"
slug = "copying-strings-in-c"
date = 2015-09-27T18:34:44+03:00
tags = ['linux', 'C', 'security', 'best-practices']
+++

Recently, I\'ve read an interesting article[^1], explaining why the
`strncpy` function in C is not safer than `strcpy`. The post was very
interesting, but what\'s more, it suggested an alternative idiom for
copying strings in C, that might probably be the way to go.

Later, in another article[^2] that compared some functionality in C,
Python and Go, one of the comments pointed out that very same idiom.
That grabbed my attention, so I decided to try it in an example.

The problem with `strncpy` seems to be the way it manages the source
string to be copied. Based on the sample code provided in the
documentation[^3] (that should be just a reference), the break condition
is up to `n` characters (the third parameter) or until the source string
is exhausted, whatever happens first. This should not be a problem,
unless `n < strlen(source_string)`. That parameter would make `strncpy`
to finish before it can put a `\0` character at the end of the target
string, leaving an invalid array of characters[^4].

This is an example.

```c
#include <stdio.h>  /* stdout, fprintf */
#include <string.h>  /* strncpy, strlen */

#define TARGET 10

int main(int argc, char* argv[]) {

    char *src = "Castle";  /* 6 chars long */
    char dst[TARGET] = "__________";

    dst[TARGET - 1] = '\0';

    fprintf(stdout, "%s\n", dst);   /* must be: '_________' */
    /* What happens if I pass a wrong length (lower than the actual
    * strlen) */
    strncpy(dst, src, 3);
    fprintf(stdout, "%s\n", dst);   /* must be: 'Cas______' */
    /* If I copy the string correctly, by passing the right
    * length, then strcnpy behaves as expected */
    strncpy(dst, src, strlen(src) + 1);
    fprintf(stdout, "%s\n", dst);   /* must be: 'Castle' */

    return 0;
}
```

On this example, the target array is represented by the variable `dst`,
and I used a fixed-length string, on purpose for the demonstration,
simulating what would actually happen. I null-terminated it so the
program can finish successfully, because otherwise the operations on it
would not end until the delimiter is reached, and we cannot know when
that will happen, considering what\'s in memory at that time. In
addition, the unpredictable behaviour will lead to errors, and probably
to memory corruption. The underscore, should be interpreted as slots:
regions or reserved memory that are there, but empty.

The proposed idiom uses `strncat` (see[^5]), tricking the function by
passing it an empty string as the first parameter, and then the actual
string we need to copy. This call will render the same result, but
without the previous side effect. Let\'s see an example:

```c
#include <stdio.h>  /* stdout, fprintf */
#include <string.h>  /* strncat, strlen */

#define TARGET 10

int main(int argc, char* argv[]) {

    char *src = "Castle";  /* 6 chars long */
    char dst[TARGET] = "__________";
    dst[TARGET - 1] = '\0';

    fprintf(stdout, "%s\n", dst);   /* must be: '_________' */
    /* Prepare destination string */
    dst[0] = '\0';
    /* Copy with strncat */
    strncat(dst, src, 3);
    fprintf(stdout, "%s\n", dst);   /* must be: 'Cas' */
    /* If I copy the string correctly, by passing the right
    * length, then strcnpy behaves as expected */
    dst[0] = '\0';
    strncat(dst, src, strlen(src) + 1);
    fprintf(stdout, "%s\n", dst);   /* must be: 'Castle' */
    /* If I try to overrun the buffer */
    dst[0] = '\0';
    strncat(dst, src, strlen(src) + 10);
    fprintf(stdout, "%s\n", dst);   /* must be: 'Castle' */

    return 0;
}
```

Here we see, the error is no longer present, probably because of the
difference on the implementation (the snippet on the documentation[^6]
gives us a hint on what it does, so we can spot the change).

This might seem as a little issue, but it raised some concerns on the
Linux kernel development, at the point that a new function was
developed. The `strscpy` function is being included in the Kernel
development for *Linux 4.3-rc4*[^7] because it *is* a better interface.
Some of the problems mentioned in the commit message, that inspired this
new version, are the ones described on the previous paragraphs.

This makes me wonder, if this should be the \"correct\" way for
performing this operation \"safely\" in C. In all cases, the error is
the same (not checking the boundaries, and trusting the input), and
should be avoided. What I mean by this, is that we cannot simply rely on
those functions being secure, the security must be in our code, so the
proper way to handle these situations is to *code defensively*: do not
trust user input, always check the boundaries, error codes, memory
allocation, status of the pointer (a `free` for every `malloc` but not
for a `NULL` pointer, etc.).

[^1]: <https://the-flat-trantor-society.blogspot.com.ar/2012/03/no-strncpy-is-not-safer-strcpy.html>.

[^2]: <https://blog.surgut.co.uk/2015/08/go-enjoy-python3.html>.

[^3]: [strncpy documentation](https://linux.die.net/man/3/strncpy/).

[^4]: An array of characters that is not null-terminated, is invalid.

[^5]: [strncat manual page](https://linux.die.net/man/3/strncat/).

[^6]: [strncat manual page](https://linux.die.net/man/3/strncat/).

[^7]: <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=30c44659f4a3e7e1f9f47e895591b4b40bf62671>.
