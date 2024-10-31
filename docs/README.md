# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`
# Описание решения 
- Square: ввод стороны квадрата и нахождение его площади или периметра
- Circle: ввод радиуса круга и нахождение его площади или периметра 
- Triangle: ввод сторон треугольника и нахождение его площади или периметра
# Описание каждой функции и пример её вызова
## Функции для квадрата
   -area(a)-принимает сторону квадрата a и находит его площадь
   -perimeter(a)-принимает сторону квадрата a и находит его периметр
### Примеры вызова функций
   -area(a) a=4, возвращает число 16
   -perimeter (a) a=6, возвращает число 24 
## Функции для круга
   -area(r)-принимает радиус круга r и находит его площадь
   -perimeter(a)-принимает радиус круга r и находит его периметр
### Примеры вызова функций
   -area(r) r=7, возвращает число 153.86
   -perimeter(a) r=2, возвращает число 12.56
## Функции для треугольника
   -area(a, b, c)-принимает стороны треугольника и находит его площадь
   -perimeter(a, b, c)-принимает стороны треугольника и находит его периметр
### Примеры вызова функций
   -area (a, b, c) a=7 b=8 c=9, возвращает число 12
   -perimeter(a, b ,c ) a=2 b=4 c=7, возвращает число 11
# История коммитов
-6128a2c (HEAD -> documentation) added documentation
-2944c15 added documentation
-efa1caa added documentation
-b5b0fae (origin/develop) L-04: Update docs for calculate.py
-d76db2a L-04: Add calculate.py
-51c40eb L-04: Doc updated for triangle
-d080c78 L-04: Triangle added
-d078c8d (origin/main, main) L-03: Docs added
-8ba9aeb L-03: Circle and square added
