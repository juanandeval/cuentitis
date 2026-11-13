#!/usr/bin/env python3
"""Valida lecturas.json antes de subirlo. Uso: python3 validate.py"""
import json, sys
TOPICS={"Animales","Dinosaurios","Espacio","Fútbol","Princesas y reyes","Superhéroes","Piratas","Coches","Cocina","Ciencia","Dragones","Robots"}
BANDS={"5-6","7-8","9-10","11-12"}; err=0; ids=set()
def bad(i,m):
    global err; err+=1; print(f"✗ {i}: {m}")
data=json.load(open("lecturas.json",encoding="utf-8"))
for r in data:
    i=r.get("id","(sin id)")
    if i in ids: bad(i,"id repetido")
    ids.add(i)
    if r.get("band") not in BANDS: bad(i,"band inválido")
    if r.get("hero") not in {"niño","niña","neutro"}: bad(i,"hero inválido")
    if not r.get("topics") or not set(r["topics"])<=TOPICS: bad(i,"topics inválidos")
    n=sum(len(p.split()) for p in r.get("paragraphs",[]))
    if not 350<=n<=650: print(f"! {i}: {n} palabras (objetivo ~400-550)")
    qs=r.get("questions",[])
    if len(qs)!=5: bad(i,"debe tener 5 preguntas")
    opts=3 if r.get("band") in("5-6","7-8") else 4
    for k,q in enumerate(qs,1):
        if len(q.get("options",[]))!=opts: bad(i,f"pregunta {k}: debe tener {opts} opciones")
        if not isinstance(q.get("answer"),int) or not 0<=q["answer"]<len(q.get("options",[])): bad(i,f"pregunta {k}: answer inválido")
print(f"{len(data)} lecturas, {err} errores"); sys.exit(1 if err else 0)
