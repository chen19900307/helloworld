from functools import wraps

import cProfile,pstats,StringIO

def profiler(func):
    def wrapper(*args,**kwargs):
        datafn = func.__name__ + ".profile"

        prof = cProfile.Profile()
        retval = prof.runcall(func,*args,**kwargs)

        s = StringIO.StringIO()
        sortby = 'cumulative'

        ps = pstats.Stats(prof,stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()
        return retval

    return wrapper
def memo(fn):
	cache = {}
	miss = object()

	@wraps(fn)
	def wrapper(*args):
		result = cache.get(args,miss)
		if result is miss:
			result = fn(*args)
			cache[args] = result
		return result
	return wrapper
@profiler
@memo
def fib(n):
	if n<2:
		return n
	return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	print fib(10)

	print fib(20)

	print fib(23)
