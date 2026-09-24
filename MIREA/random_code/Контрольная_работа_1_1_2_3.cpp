// Варианты: I (имя), l (корни), c (летний период по номеру дня)

#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
  cout << "Enter coefficients a, b, c (separated by space): ";
  double a, b, c;
  if (!(cin >> a >> b >> c))
    return 0;

  cout << "Enter option symbol (I / l / c): ";
  char opt;
  if (!(cin >> opt))
    return 0;

  // Константа для имени студента (замените на своё!)
  const string student = "Karmaev Andrey";

  // "точность" для сравнения с нулём
  const double EPS = 1e-9;

  switch (opt) {
  case 'c': {
    cout << "Enter day number (1..365): ";
    int d;
    if (!(cin >> d))
      return 0;

    int startDay = 152; // 01.06
    int endDay = 243;   // 31.08

    cout << "Result: ";
    if (1 <= d && d <= 365 && startDay <= d && d <= endDay) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
    return 0;
  }
  case 'l': {
    // Вариант l: найти корни уравнения a*x^2 + b*x + c = 0
    cout << fixed << setprecision(6);

    cout << "Roots: ";
    // Случаи вырождения
    if (fabs(a) < EPS && fabs(b) < EPS && fabs(c) < EPS) {
      cout << "any real number\n";
      return 0;
    }

    if (fabs(a) < EPS && fabs(b) < EPS) {
      cout << "no roots\n";
      return 0;
    }

    if (fabs(a) < EPS) {
      // Линейный случай
      double x = -c / b;
      cout << "x=" << x << "\n";
      return 0;
    }

    double D = b * b - 4.0 * a * c;
    if (D < -EPS) {
      cout << "no roots\n";
      return 0;
    }

    if (fabs(D) <= EPS) {
      double x = -b / (2.0 * a);
      cout << "x=" << x << "\n";
      return 0;
    }

    // D > 0
    double sqrtD = sqrt(max(0.0, D));
    double x1 = (-b - sqrtD) / (2.0 * a);
    double x2 = (-b + sqrtD) / (2.0 * a);
    if (x1 > x2)
      swap(x1, x2);
    cout << "x1=" << x1 << " x2=" << x2 << "\n";
    return 0;
  }
  case 'I':
    cout << "Result: " << student << "\n";
    return 0;
  default:
    std::cout << "x is undefined" << "\n";
    break;
  }

  // Неизвестный символ
  cout << "Unknown option symbol!\n";
  return 0;
}
