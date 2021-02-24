import ldap3

from django.contrib.auth.models import User
from django.conf import settings

from base.management import BaseCommand


def init_ldap():
    server = ldap3.Server('ldap://ads.mwn.de')
    connection = ldap3.Connection(
        server,
        'CN=%s,OU=Users,ou=TU,ou=IAM,dc=ads,dc=mwn,dc=de' % settings.LDAP_USER,
        settings.LDAP_PASSWORD
    )
    return connection


def check_user_in_ldap(connection, email):
    return connection.search(
        'ou=Users,ou=TU,ou=IAM,dc=ads,dc=mwn,dc=de',
        '(proxyAddresses=smtp:%s)' % email
    )


class Command(BaseCommand):
    help = 'Verify state of users in Active Directory. Deactivate old users.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Whether to delete instead of deactivate old users.'
        )

    def handle(self, *args, **options):
        if not (
            hasattr(settings, 'LDAP_USER') and
            hasattr(settings, 'LDAP_PASSWORD')
        ):
            self.stdout.write(
                'Please set LDAP_USER and LDAP_PASSWORD in configuration.py.'
            )
            return
        connection = init_ldap()
        connection.bind()
        activate_count = 0
        delete_count = 0
        deactivate_count = 0

        for user in User.objects.all():
            if check_user_in_ldap(connection, user.email):
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    activate_count += 1
            elif options['delete']:
                user.delete()
                delete_count += 1
            elif user.is_active:
                user.is_active = False
                user.save()
                deactivate_count += 1
        connection.unbind()
        self.stdout.write(
            'Activated: %s, Deactivated: %s, Deleted: %s, Verified: %s' % (
                activate_count,
                deactivate_count,
                delete_count,
                len(User.objects.all())
            )
        )
