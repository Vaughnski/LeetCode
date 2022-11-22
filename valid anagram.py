s = ''.join(sorted(s, key=str.lower))
t = ''.join(sorted(t, key=str.lower))
return True if s == t else False