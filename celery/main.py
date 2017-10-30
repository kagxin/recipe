from proj.tasks import add, mul, xsum
from proj.celery import app
from celery import group, chain, chord

r = add.delay(4, 4)
print(r.id)
print(r.get())
res = app.AsyncResult(r.id)
print(res.get())

add.subtask((2, 2), countdown=10)

s1 = add.s(2)
res = s1.delay(2)
print(res.get())

g = group(add.s(i, i) for i in range(10))
r = g()
print(r.get())


pg2 = group(add.s(i) for i in range(10))
res = pg2.delay(2)
print(res.get())

c = chain(add.s(2) | mul.s(8))
r = c.delay(2)
print(r.get())

c = chain(add.s(2, 3) | mul.s(8))
r = c()
print(r.get())


c = add.s(2, 3) | mul.s(3)
r = c()
print(r.get())


