function nbYear($p0, $percent, $aug, $p)
{
  $year = 0;
  $more = $p0;
  $percent /= 100;
  do
  {
   $more = ((int)($more + $more * $percent + $aug));
   $year++;
  } while ($more < $p);
  return $year;
}