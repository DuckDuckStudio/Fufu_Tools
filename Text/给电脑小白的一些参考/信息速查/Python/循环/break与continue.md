# Python中的break与continue

`break`和 `continue`是两个在*循环*中常用的关键字。

1. **`break`** ：

* `break`的作用是 **结束当前的循环体** ，并且**后面的循环也不再继续执行**。
* 常用于 `for`和 `while`循环内部。
* 例如，在以下代码中，我们使用 `break`来退出循环：

  ```python
  for i in range(1, 101):
      if i == 100:
          break
  ```
* 需要特别注意的是，`break`语句总是跳出 **最近的一层循环** 。即使有多层嵌套的循环，它只会跳出当前内层的循环，而不会影响外层的循环。

2. **`continue`** ：

* `continue`的作用是 **跳出本次循环** ，然后**继续执行下一次循环**（不是继续执行当前次循环）。
* 与 `break`最大的区别在于，`continue`会继续执行下一个循环，而不是完全结束循环。
* 例如，在以下代码中，我们使用 `continue`来跳过奇数的循环：

  ```python
  for i in range(1, 6):
      if i % 2 == 0:
          print(f"begin i={i}")
          continue
      print(f"begin i={i}")
      print(f"end i={i}")
  ```
* 在多层嵌套的循环中，`continue`同样会结束本次自己所在的循环。

总结：

* `break`语句可以**跳出当前循环**，通常配合 `if`语句，在满足条件时提前结束整个循环。
* `continue`语句可以**提前结束本次循环**，通常配合 `if`语句，在满足条件时提前结束本次循环。
* 区别：`break`语句是**直接结束循环**，而 `continue`语句**只结束本次循环，还会继续执行下一次循环**
