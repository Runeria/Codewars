using System;
# Kata URL : https://www.codewars.com/kata/563b662a59afc2b5120000c6
class Arge {

    public static int NbYear(int p0, double percent, int aug, int p) {

      int year = 0;
      double more = p0;
      double pourcent = percent / 100;
      do
        {
          more = (int)more + more * pourcent + aug;
          year +=1;
        } while (p > more);
      return year;
    }
}