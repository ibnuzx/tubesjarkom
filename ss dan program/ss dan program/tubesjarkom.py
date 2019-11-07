"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'server', ip='192.168.1.1/24', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'client', ip='192.168.1.2/24', mac='00:00:00:00:00:02' )
        s1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( h1, s1, bw='2' )
        self.addLink( h2, s1, bw='10' )


topos = { 'mytopo': ( lambda: MyTopo() ) }
