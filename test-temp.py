import scripts.nsproc as proc
import scripts.nsdraw as draw
import scripts.nscolor as nsc
import scripts.nssys as nss

def run():
    k = proc.kernel((11, 11), proc.KERNEL_TYPE_CIRCULAR_FADE)
    print(k)

nss.execMonitor(run,True)
