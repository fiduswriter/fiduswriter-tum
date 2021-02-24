# fiduswriter-tum

Fidus Writer integration for the Fidus Writer instance of the Technical University of Munich (TUM).


To install run this on the command line:

```
sudo bash
apt install python3-pip
cd /var/snap/fiduswriter/current
git clone git@github.com:fiduswriter/fiduswriter-tum.git
ln -s fiduswriter-tum/tum .
pip3 install -r tum/requirements.txt --target .
exit
sudo fiduswriter.configure
```

You will be presented with the configuration file. Add strings for LDAP_USER and LDAP_PASSWORD to access ldap://ads.mwn.de.

Remember that this repository does not update automatically the way the main Fidus Writer package does. You need to manually install new versions.
