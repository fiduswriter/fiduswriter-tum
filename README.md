# fiduswriter-tum

Fidus Writer integration for the Fidus Writer instance of the Technical University of Munich (TUM).


To install:

```
sudo bash
apt install python3-pip
cd /var/snap/fiduswriter/current
git clone git@github.com:fiduswriter/fiduswriter-tum.git
ln -s fiduswriter-tum/tum .
cd tum
pip3 install -r requirements.txt --target .
exit
```

Execute `fiduswriter.configure` and add strings for LDAP_USER and LDAP_PASSWORD to access ldap://ads.mwn.de.

Remember that this repository does not renew itself. You need to manually install new versions.
