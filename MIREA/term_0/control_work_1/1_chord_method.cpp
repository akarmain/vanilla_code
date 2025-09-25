#include <cmath>
#include <iostream>
#include <stdexcept>
using namespace std;
double f(double x) { return acos((1 - x * x) / (1 + x * x)) - x; }

double regula_falsi(double l, double r, double tol = 1e-6,
                    int max_iter = 1000) {
  double fl = f(l);
  double fr = f(r);

  if (!isfinite(fl) || !isfinite(fr)) {
    throw runtime_error(
        "f(l) или f(r) не конечны (NaN/Inf). Проверь домен функции.");
  }

  if (fl == 0.0)
    return l;
  if (fr == 0.0)
    return r;
  if (fl * fr > 0.0) {
    throw runtime_error(
        "На [l, r] нет смены знака: f(l)*f(r) > 0. Нужен интервал со скобкой.");
  }

  double m = l;
  double fm = fl;

  for (int iter = 0; iter < max_iter; ++iter) {
    double denom = (fr - fl);
    if (fabs(denom) < 1e-15) {
      m = 0.5 * (l + r);
    } else {
      m = (l * fr - r * fl) / denom;
    }

    if (m < l)
      m = 0.5 * (l + r);
    if (m > r)
      m = 0.5 * (l + r);

    fm = f(m);
    if (!isfinite(fm)) {
      m = 0.5 * (l + r);
      fm = f(m);
    }

    if (fabs(fm) <= tol)
      return m;
    if (fabs(r - l) <= tol)
      return m;

    if (fl * fm < 0.0) {
      r = m;
      fr = fm;
    } else if (fm * fr < 0.0) {
      l = m;
      fl = fm;
    } else {
      return m;
    }
  }
  return m;
}

int main() {
  try {
    double l = 2.0, r = 4.0;
    double tol = 1e-6;
    int max_iter = 1000;

    double root = regula_falsi(l, r, tol, max_iter);
    cout << "x* ≈ " << root << "\n";
    cout << "f(x*) = " << f(root) << "\n";
  } catch (const exception &e) {
    cerr << "Ошибка: " << e.what() << "\n";
    return 1;
  }
  return 0;
}

// #include <iostream>
// using namespace std;
// #include <cmath>

// // double f(double x) { return (100 / x) + 10; }
// double f(double x) { return acos((1 - x * x) / (1 + x * x)) - x; }

// double x_intercept_two_points(double x1, double y1, double x2, double y2) {
//   double dy = y2 - y1;
//   return (x1 * y2 - x2 * y1) / dy;
// }

// int main() {
//   double l, r, m, ans;
//   l = 2;
//   r = 4;
//   m = 1;
//   while (abs(f(m)) > 0.001) {
//     cout << "-----NEW----- " << endl;
//     double x1 = l;
//     double y1 = f(x1);
//     double x2 = r;
//     double y2 = f(x2);

//     m = x_intercept_two_points(x1, y1, x2, y2);
//     if (m < 0) {
//       l = m;
//       ans = m;
//     } else {
//       r = m;
//       ans = m;
//     }
//   }
//   cout << "ANS: " << ans << endl;
// }
