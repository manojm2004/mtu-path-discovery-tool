import subprocess
import platform

def test_mtu(host, size):
    param = '-f -l' if platform.system().lower() == 'windows' else '-M do -s'
    cmd = f'ping {host} {param} {size} -n 1'
    print(f'Testing MTU payload size: {size} bytes to {host}...')

if __name__ == '__main__':
    test_mtu('8.8.8.8', 1472)
