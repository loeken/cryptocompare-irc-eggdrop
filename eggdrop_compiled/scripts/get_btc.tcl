package require http 2.3

bind pubm - "*" scan_btc

proc scan_btc {nick uhost hand chan arg} {
   global botnick

   if {[string match "!btc" $arg] == 1} {

      if {$nick == $botnick} {
         return 0
      }

      set btc [get_btc $arg]

      if {$btc != "0"} {
         putserv "PRIVMSG $chan :$btc"
      }
   }
   return 0
}

proc get_btc { arg } {
   set output [exec python scripts/get_btc.py]
   return $output
}

putlog "---> btc cryptocurrency x _d3d0c3d"

