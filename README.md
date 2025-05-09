# fiduswriter-tum

Fidus Writer integration for the Fidus Writer instance of the Technical University of Munich (TUM).

Installation
============

To install run this on the command line:

```
sudo bash
apt install python3-pip
cd /var/snap/fiduswriter/current
git clone git@github.com:fiduswriter/fiduswriter-tum.git
ln -s fiduswriter-tum/fiduswriter/tum .
pip3 install -r tum/requirements.txt --target .
exit
sudo fiduswriter.configure
```

You will be presented with the configuration file. Add strings for LDAP_USER and LDAP_PASSWORD to access ldap://ads.mwn.de.

To manually mark users no longer registered with TUM as inactive, run:

```
sudo fiduswriter.manage check_tum_user_state
```

If you want to delete users not registered with TUM directly, run it with the `--delete` flag:

```
sudo fiduswriter.manage check_tum_user_state --delete
```

If you want the system to do this process automatically, set up a cronjob by typing:

```
sudo crontab -e
```

In the editor that comes up enter a line such as the following to run the command automatically every Sunday at 3:25 am and not delete users directly:

```
25 3 * * 7 /snap/bin/fiduswriter.manage check_tum_user_state
```

----
Remember that this repository does not update automatically like the main Fidus Writer package. You need to install new versions manually.
