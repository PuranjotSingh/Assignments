def pascal_triangle(num):
   trow = [1]
   y = [0]
   for x in range(max(num,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return num>=1

a=int(input("Input the number of rows"))
pascal_triangle(a)
