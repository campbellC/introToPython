This course covers a selection of Python and programming topics aimed at
researchers in mathematics. As such it assumes a fairly high willingness to
self-teach and read documentation, and the topics it covers reflect as much my
interests as an attempt to cover 'the important stuff'.

A few things are missing - the tex file for the first object lesson vanished
and I think I must have `rm`'ed it by accident at some point. Also, for the
scripting session you should download fresh wikipedia page dump files and use
GNU `shuf` (or something) to retrieve some random subset.  I would not suggest
using the wiki page dumps without vetting them since the page titles can be
highly inappropriate...

# Errata 
I have realised a couple of mistakes crept in during writing this.  Some are
small and inconsequential, a few are important and worth correcting. I will
update this as they come to mind.

1) `__repr__()` is *not* supposed to be a printable form of an object for a
user to see. It is better to use `__str__()` for that purpose, and in
particular `print` looks for `__str__()` first.

`__repr__()` should be used to give a printable description of how the object
is made. Standard library types have the property that the return of
`__repr__()` should be runnable Python code that would recreate the same object
- i.e.  `eval(repr(x)) == x` should be true. This is a guiding principle and
  its as always up to you how you treat it.




