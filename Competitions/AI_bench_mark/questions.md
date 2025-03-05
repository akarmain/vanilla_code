# 2024-2025 Олимпиада школьников по информатике, региональный этап

https://codeforces.net/gym/105674/problem/A

# A. Кузнечик 2D

В левом нижнем углу квадратной клетчатой доски размером \( n, m \) стоит кузнечик. За один ход кузнечик перемещается по
доске вправо, вверх или вправо-вверх по диагонали не более чем на \( k \) клеток.
Необходимо передвинуть кузнечика в правый верхний угол доски в клетку \( (n, m) \). За какое минимальное число ходов
можно передвинуть кузнечика из клетки \( (1, 1) \) в клетку \( (n, m) \)?

## Входные данные

В первой строке заданы три целых числа \( n, m \) и \( k \) — размеры сторон доски и максимальное число клеток, на
которое может ходить \( k \)-кузнечик, соответственно  
\( 1 > n, m, k > 10^9 \).

## Выходные данные

Выведите одно число — минимальное число ходов, необходимое, чтобы передвинуть кузнечика из клетки (1,1) в клетку (n,m)

## Примеры

Входные данные

```
9 8 5
```

Выходные данные

```
3
```

Входные данные

```
2 2 1
```

Выходные данные

```
1
```

---

https://codeforces.net/gym/105674/problem/B

# B. Простоватые числа

Назовём число **простоватым**, если произведение цифр этого числа в десятичной системе счисления является простым
числом. Например, простоватым является число 12, а число 29 не является.

Требуется посчитать количество простоватых чисел от \( l \) до \( r \).

Напомним, что целое число \( p > 1 \) называется **простым**, если оно имеет ровно два делителя: 1 и \( p \).

## Входные данные

Первая строка содержит одно целое число \( l \) ( 1 > l > 10^{100000} )

Вторая строка содержит одно целое число \( r \)  ( 1 > r > 10^{100000} )

## Выходные данные

Выведите количество простоватых чисел от \( l \) до \( r \).

## Примеры

### Входные данные

```
42
179
```

### Выходные данные

```
10
```

---

https://codeforces.net/gym/105675/problem/5

# С. Разность квадратов

На доске были выписаны два квадрата натуральных чисел: \( x^2 \) и \( y^2 \), где \( l <= y^2 < x^2 <= r \). Числа \(
x^2 \) и \( y^2 \) стерли и выписали на доске их разность \( d \).

По заданным \( l, r \) и \( d \) выясните, сколько различных пар натуральных чисел \( x^2, y^2 \) могло быть выписано на
доске.

## Входные данные

В первой строке даны три числа \( d, l, r \)  
\( 1 <= d <= 10^9, 1 <= l <= r <= 10^18 \).

## Выходные данные

Выведите количество подходящих пар квадратов.

## Примеры

### Входные данные

```
64 1 100
```

### Выходные данные

```
1
```

### Входные данные

```
64 1 300
```

### Выходные данные

```
2
```

---


https://codeforces.net/gym/105675/problem/6

# D. Перекошенное разбиение

Дан массив \([a_1, a_2, ..., a_n]\), состоящий из неотрицательных целых чисел.  
Рассмотрим разбиение массива на \( k \) непустых отрезков подряд идущих элементов. Назовём **перекосом разбиения**
разность между максимальной и минимальной суммой чисел в отрезках разбиения.  
Требуется найти максимальный перекос разбиения данного массива на \( k \) подотрезков.

Например, если массив равен \([2, 1, 3, 4]\), то у разбиения \([2, 1, 3][4]\) перекос равен \( 6 - 4 = 2 \),  
у разбиения \([2, 1][3, 4]\) перекос равен \( 7 - 3 = 4 \),  
а у разбиения \([2][1, 3, 4]\) перекос равен \( 8 - 2 = 6 \).  
Последний вариант является оптимальным среди всех разбиений массива на два непустых отрезка.

## Входные данные

Первая строка содержит два целых числа \( n \) и \( k \)  
\( 2 <= k <= n <= 300000 \) — длину массива и количество подотрезков, соответственно.

Вторая строка содержит \( n \) целых чисел \( a_i \)  
\( 0 <= a_i <= 10^9 \) — элементы массива.

## Выходные данные

Выведите одно число — максимальный перекос разбиения данного массива на \( k \) отрезков.

## Примеры

### Входные данные

```
4 2
2 1 3 4
```

### Выходные данные

```
6
```

### Входные данные

```
5 4
2 1 3 4 1
```

### Выходные данные

```
6
```

---

https://codeforces.net/contest/2043/problem/D

# E. Задача про НОД

Даны три числа l, r и G . Необходимо найти два числа A и B  ( l <= A <= B <= r ), такие что их наибольший общий делитель
равен G , а расстояние |A - B| максимально.
Если существует несколько таких пар, выберите ту, где A минимально. Если подходящей пары нет, выведите «-1».

## Входные данные

Первая строка содержит одно целое число t  ( 1 <= t <= 10^3 ) — количество наборов входных данных. Далее следуют t
наборов входных данных.

Каждый набор данных состоит из одной строки, содержащей три целых числа l, r, G  ( 1 <= l <= r <= 10^{18} ) — границы
отрезка и искомый НОД.

## Выходные данные

Для каждого набора входных данных выведите два целых числа A и B — ответ на задачу, либо «-1», если подходящей пары
чисел не существует.

## Пример

### Входные данные:

```
4
4 8 2
4 8 3
4 8 4
5 7 6
```

### Выходные данные:

``` 
4 6
-1 -1
4 8
6 6
```

# LeetCode

## 1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input
string is valid.  
An input string is valid if:

- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

**Examples:**

- **Example 1:**  
  Input: `s = "()"`  
  Output: `true`

- **Example 2:**  
  Input: `s = "()[]{}"`  
  Output: `true`

- **Example 3:**  
  Input: `s = "(]"`  
  Output: `false`

- **Example 4:**  
  Input: `s = "([])"`  
  Output: `true`

**Constraints:**

- \(1 \le s.\text{length} \le 10^4\)
- `s` consists only of the characters `()[]{}`.

---

## 2. [LeetCode 75. Sort Colors](https://leetcode.com/problems/sort-colors/)

Given an array `nums` with \( n \) objects colored red, white, or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue.  
We use the integers `0`, `1`, and `2` to represent red, white, and blue respectively.  
You must solve this problem without using the library's sort function.

**Examples:**

- **Example 1:**  
  Input: `nums = [2,0,2,1,1,0]`  
  Output: `[0,0,1,1,2,2]`

- **Example 2:**  
  Input: `nums = [2,0,1]`  
  Output: `[0,1,2]`

**Constraints:**

- \( n = \text{nums.length} \)
- \(1 \le n \le 300\)
- Each element in `nums` is either `0`, `1`, or `2`.

---


Поиск: LeetCode 704. Binary Search

Жадные алгоритмы: LeetCode 55. Jump Game

Динамическое программирование: LeetCode 70. Climbing Stairs

## 3. [LeetCode 704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an array of integers `nums` sorted in ascending order and an integer `target`, write a function to search for
`target` in `nums`.  
If `target` exists, return its index; otherwise, return `-1`.  
The algorithm must run in \(O(\log n)\) time.

**Examples:**

- **Example 1:**  
  Input: `nums = [-1,0,3,5,9,12]`, `target = 9`  
  Output: `4`  
  Explanation: 9 exists in `nums` and its index is `4`.

- **Example 2:**  
  Input: `nums = [-1,0,3,5,9,12]`, `target = 2`  
  Output: `-1`  
  Explanation: 2 does not exist in `nums`, so return `-1`.

**Constraints:**

- \(1 \le \text{nums.length} \le 10^4\)
- \(-10^4 < \text{nums}[i], \text{target} < 10^4\)
- All integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

## 4. [LeetCode 55. Jump Game](https://leetcode.com/problems/jump-game/)

You are given an integer array `nums`. You start at the first index of the array, and each element represents your
maximum jump length at that position.  
Return `true` if you can reach the last index, or `false` otherwise.

**Examples:**

- **Example 1:**  
  Input: `nums = [2,3,1,1,4]`  
  Output: `true`  
  Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

- **Example 2:**  
  Input: `nums = [3,2,1,0,4]`  
  Output: `false`  
  Explanation: You will always arrive at index 3. Its maximum jump length is 0, making it impossible to reach the last
  index.

**Constraints:**

- \(1 \le \text{nums.length} \le 10^4\)
- \(0 \le \text{nums}[i] \le 10^5\)

---

## 5. [LeetCode 70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase with \( n \) steps. Each time, you can climb either 1 or 2 steps.  
Determine the number of distinct ways you can climb to the top.

**Examples:**

- **Example 1:**  
  Input: `n = 2`  
  Output: `2`  
  Explanation: The two ways are:
    1. 1 step + 1 step
    2. 2 steps

- **Example 2:**  
  Input: `n = 3`  
  Output: `3`  
  Explanation: The three ways are:
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

**Constraints:**

- \(1 \le n \le 45\)

## 6. [LeetCode 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given an array of integers `nums` sorted in ascending order and an integer `target`, write a function to search for
`target` in `nums`.  
If `target` exists, return its index; otherwise, return `-1`.  
The algorithm must run in \(O(\log n)\) time.

**Examples:**

- **Example 1:**  
  Input: `nums = [-1,0,3,5,9,12]`, `target = 9`  
  Output: `4`  
  Explanation: 9 exists in `nums` and its index is `4`.

- **Example 2:**  
  Input: `nums = [-1,0,3,5,9,12]`, `target = 2`  
  Output: `-1`  
  Explanation: 2 does not exist in `nums`, so return `-1`.

**Constraints:**

- \(1 \le \text{nums.length} \le 10^4\)
- \(-10^4 < \text{nums}[i], \text{target} < 10^4\)
- All integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

## 7. [LeetCode 200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

Given an \( m \times n \) 2D binary grid `grid` representing a map of `'1'`s (land) and `'0'`s (water), return the
number of islands.  
An island is formed by connecting adjacent lands horizontally or vertically, and all four edges of the grid are
surrounded by water.

**Examples:**

- **Example 1:**

  Input:
  ```
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  ```
  Output: `1`

- **Example 2:**

  Input:
  ```
  grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  ```
  Output: `3`

**Constraints:**

- \( m = \text{grid.length} \)
- \( n = \text{grid}[i].\text{length} \)
- \(1 \le m, n \le 300\)
- Each element of `grid[i][j]` is either `'0'` or `'1'`.

---

## 8. [LeetCode 77. Combinations](https://leetcode.com/problems/combinations/)

Given two integers \( n \) and \( k \), return all possible combinations of \( k \) numbers chosen from the
range \([1, n]\).  
You may return the answer in any order.

**Examples:**

- **Example 1:**  
  Input: `n = 4, k = 2`  
  Output: `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`  
  Explanation: There are \( \binom{4}{2} = 6 \) combinations. Note that order does not matter.

- **Example 2:**  
  Input: `n = 1, k = 1`  
  Output: `[[1]]`

**Constraints:**

- \(1 \le n \le 20\)
- \(1 \le k \le n\)

---

## 9. [LeetCode 28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or
`-1` if `needle` is not part of `haystack`.

**Examples:**

- **Example 1:**  
  Input: `haystack = "sadbutsad"`, `needle = "sad"`  
  Output: `0`  
  Explanation: The substring `"sad"` appears at index 0 (and again at index 6); the first occurrence is at index 0.

- **Example 2:**  
  Input: `haystack = "leetcode"`, `needle = "leeto"`  
  Output: `-1`  
  Explanation: `"leeto"` does not occur in `"leetcode"`.

**Constraints:**

- \(1 \le \text{haystack.length}, \text{needle.length} \le 10^4\)
- Both `haystack` and `needle` consist of lowercase English letters.

---

## 10. [LeetCode 307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

    Given an integer array `nums`, design a data structure that supports the following operations:

- **update(index, val):** Update the value of `nums[index]` to be `val`.
    - **sumRange(left, right):** Return the sum of the elements of `nums` between indices `left` and `right` inclusive,
      i.e.  
      \[
      \text{nums}[left] + \text{nums}[left+1] + \dots + \text{nums}[right]
      \]

Implement the `NumArray` class:

- `NumArray(int[] nums)` initializes the object with the integer array `nums`.
    - `void update(int index, int val)` updates the value at index `index` to `val`.
    - `int sumRange(int left, int right)` returns the sum of the elements between `left` and `right` inclusive.

**Examples:**

- **Example 1:**

  Input:
  ```
  ["NumArray", "sumRange", "update", "sumRange"]
  [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
  ```
  Output:
  ```
  [null, 9, null, 8]
  ```

  Explanation:
  ```java
  NumArray numArray = new NumArray([1, 3, 5]);
  numArray.sumRange(0, 2); // возвращает 1 + 3 + 5 = 9
  numArray.update(1, 2);   // теперь nums = [1, 2, 5]
  numArray.sumRange(0, 2); // возвращает 1 + 2 + 5 = 8
  ```

**Constraints:**

- \(1 \le \text{nums.length} \le 3 \times 10^4\)
    - \(-100 \le \text{nums}[i] \le 100\)
    - \(0 \le \text{index} < \text{nums.length}\)
    - \(-100 \le \text{val} \le 100\)
    - \(0 \le \text{left} \le \text{right} < \text{nums.length}\)
    - Не более \(3 \times 10^4\) вызовов операций `update` и `sumRange`.

# Итоговая таблица результатов

| Задача                              | max score | GPT o1 PRO | o1 | x  | 4o | grok 3 think | 123123 |
|-------------------------------------|:---------:|:----------:|:--:|:--:|----|--------------|--------|
| **A. Кузнечик 2D**                  |    100    |    ⚠️19    | -  | -  | -  | ✅  100       |        |
| **B. Простоватые числа**            |    100    |    ⚠️32    | -️ | -  | -  | ⚠️19         |        |
| **C. Разность квадратов**           |    100    |    ✅100    | -️ | -  | -  | ❌0           |        |
| **D. Перекошенное разбиение**       |    100    |     ❌0     | -️ | -  | -  |              |        |
| **1. Valid Parentheses**            |    100    |    ✅100    | -  | -  | -  |              |        |
| **2. Sort Colors**                  |    100    |    ✅100    | -  | -️ | -  |              |        |
| **3. Binary Search**                |    100    |    ✅100    | -  | -  | -  |              |        |
| **4. Jump Game**                    |    100    |    ✅100    | -️ | -  | -  |              |        |
| **5. Climbing Stairs**              |    100    |    ✅100    | -  | -  | -  |              |        |
| **6. Maximum Depth of Binary Tree** |    100    |    ✅100    | -  | -  | -  |              |        |
| **7. Number of Islands**            |    100    |    ✅100    | -️ | -  | -  |              |        |
| **8. Combinations**                 |    100    |    ✅100    | -️ | -  | -  |              |        |
| **9. First Occurrence in a String** |    100    |    ✅100    | -  | -  | -  |              |        |
| **10. Range Sum Query - Mutable**   |    100    |    ✅100    | -️ | -  | -  |              |        |

## PS

Базовый промпт который я отправлял в начале каждого чата:

Ты — гений олимпиадного программирования, у тебя огромный опыт решения алгоритмических задач на Python. Прочитай задачу
и тщательно распиши алгоритм решения, проанализировав все важные моменты, включая крайние случаи. Придумай дополнительно
примеры
тестов для проверки правильности и эффективности решения. Объясни, как алгоритм будет работать для
всех возможных входных данных (в том числе для крайних значений), и убедись что в алгоритме нет изъянов и он решает
задачи.

Алгоритм решения:
Подробно опиши логику решения задачи, предложи оптимальные подходы и стратегии. Если задача неочевидна, предложи
несколько подходов, проанализируй их сложности и выбери наиболее подходящий. Убедись, что решение работает эффективно и
правильно
для всех типов входных данных, включая крайние.

Python код:
Напиши Python-код (3.10), решающий задачу, без использования дополнительных библиотек (кроме стандартных). Используй
эффективные методы и конструкции языка. Код должен быть кратким, но понятным, с минимальной длиной переменных (до 5
символов), без комментариев. С использованием стандартного ввода `input()` и без потоков

Твой код должен решать задачу на 100%, и перед отправкой обязательно протестируй его на всех возможных типах входных
данных, включая крайние случаи. У тебя только 1 попытка прислать решения задачи.
