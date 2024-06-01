from dev.magicmq.pyspigot import PySpigot as ps
from org.bukkit.event.block import BlockBreakEvent
from org.bukkit import Bukkit

Bukkit.broadcastMessage('HI ALL')


def join_event(event):
    player = event.getPlayer()
    player.sendMessage('you break block')


ps.listener.registerListener(join_event, BlockBreakEvent)