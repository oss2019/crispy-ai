from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):     #creates a token for account activation in case
                                                                        # of signup
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)        #six.text_type() converts anything given as arguments in text format
        )

account_activation_token = AccountActivationTokenGenerator()