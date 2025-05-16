# Salt

## links
https://docs.saltproject.io/salt/install-guide/en/latest/topics/install-by-operating-system/linux-deb.html

## cmd.run
https://docs.saltproject.io/en/3006/py-modindex.html
salt 'main-vm-ubuntu-olivia' cmd.run 'ls'

## sls
https://docs.saltproject.io/salt/user-guide/en/latest/topics/states.html

/srv/salt/nmap.sls
install_tree_now:
  pkg.installed:
    - pkgs:
        - nmap

/srv/salt/uname.sls
cmd-test:
  cmd.run:
    - name: uname -a

salt main-vm-ubuntu-olivia state.sls uname