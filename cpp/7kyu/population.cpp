class Arge
{
  public:
  static int nbYear(int p0, double percent, int aug, int p)
    {
    int year(0);
    double more(p0);
    double pourcent = percent / 100;
    while (more < p)
    {
      more = (more + more * pourcent + aug);
      year +=1;
    }
    return year;

    }

};