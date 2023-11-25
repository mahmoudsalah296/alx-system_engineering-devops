# kill a process named killmenow
exec { 'pkill':
  command => 'pkill -f killmenow'
}
