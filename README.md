# About

A small Python script to watch the pool of available entropy.

Written to avoid using `watch cat /proc/sys/kernel/random/entropy_avail` as entropy is consumed with each invocation of `cat`. Wasteful!

Specify the delay in seconds, e.g. `python entropy.py 5` or `python entropy.py 0.5`; otherwise the default is 1 second.
