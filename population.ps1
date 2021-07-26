function nb-year([int]$p0, [double]$percent, [int]$aug, [int]$p)
{
  $year = 0
  $more = $p0
  $percent /= 100

  while($more -lt $p){$more = $more + $more * $percent + $aug; $year++}
  return $year
}