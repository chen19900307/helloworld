import cProfile,pstats,StringIO

def profiler(func):
    def wrapper(*args,**kwargs):
        datafn = func.__name__ + ".profile"

        prof = cProfile.Profile()
        retval = prof.runcall(func,*args,**kwargs)

        s = StringIO.StringIO()
        sortby = 'cumulative'

        ps = pstats.Stats(prof,stream=s).sort_stats(sortby)
        ps.print_starts()
        print s.getvalue(（）
        return retval

        return wrapper
