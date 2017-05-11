
### Look at netmiko-tools inventory  
cat ~/.netmiko.yml  

### List devices in inventory  
netmiko-grep --list-devices  

### Search for 'interface' line 'cisco' group  
netmiko-grep 'interface' cisco  

### Retrieve 'show arp' output from the juniper1 device
netmiko-show --cmd 'show arp' juniper1   

### Configure logging buffer on arista-sw5
netmiko-cfg --cmd 'logging buffered 20000' arista-sw5  

### Make configuration changes specified in 'logging_change.txt' file
netmiko-cfg --infile logging_change.txt arista  
